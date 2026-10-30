# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BNB
**Canonical Key**: `BNB` | **Broker Instrument**: `BNBUSD.p` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 14:23:36 IST` (`2026-10-30 08:53:36 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `702.90` | **Live Ask Quote**: `706.10` | **Mid Price**: `704.50`
- **Spread Points**: `320.00` | **Spread BPS**: `45.42 bps` (Charter Threshold: `25.00 bps`)
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
  * 14-Period ATR: `3.65` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `38.01` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `732.30` | Lower -3.00σ Band: `672.09`
  * Upper +2.51σ Band: `727.38` | Lower -2.51σ Band: `677.00`
  * Upper +2.01σ Band: `722.36` | Lower -2.01σ Band: `682.02`
  * Upper +2.00σ Band: `722.26` | Lower -2.00σ Band: `682.12`
  * Upper +1.28σ Band: `715.04` | Lower -1.28σ Band: `689.35`
  * Upper +1.00σ Band: `712.23` | Lower -1.00σ Band: `692.16`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`706.51` | EMA-20=`708.35` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`712.38` (Slope: `+0.0000`) | EMA-100=`721.21`
  * Institutional Anchors: EMA-144=`726.36` | EMA-200=`730.27` (Slope: `-0.3755`) | EMA-233=`732.24`
- **Range Boundaries**: 24H High=`753.20` | 24H Low=`677.20` | Weekly High=`760.90` | Weekly Low=`677.20`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `715.24` (Distance: `-1.50%`)
  * Point of Control (POC) = `704.18` (Distance: `+0.05%`)
  * Value Area Low (VAL) = `699.26` (Distance: `+0.75%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`754.57` | POC=`744.11` | VAL=`738.60`
  * Prior Day Extremes: PDH=`759.80` | PDL=`677.20` | PDC=`696.20`
  * Monday Range Blueprint: High=`746.00` | Mid=`738.45` | Low=`730.90`
  * Developing Weekly Value Area: Weekly VAH=`751.69` | Weekly POC=`740.53` | Weekly VAL=`734.95`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`724.00` | Low=`677.90`
  * London Session (08:00-16:00 UTC): High=`717.90` | Low=`700.90`
  * New York Session (13:00-21:00 UTC): High=`708.73` | Low=`700.27`
  * Initial Balance (First Hour): IB High=`717.90` | IB Low=`712.90`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `701.68` - `707.32`
  * Optimal Trade Entry (OTE 0.705): `705.91`
  * Structural Invalidation Anchor (0.786): `710.14`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `706.19` | `706.93` | `705.74` | `706.23` | `2,954` | 2,086,561.06 USD | -686,021.78 USD | `-32.88%` | -55,931,004.44 USD | `+0.10` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `706.23` | `706.58` | `705.73` | `705.92` | `4,406` | 3,111,268.45 USD | -1,325,758.60 USD | `-42.61%` | -57,256,763.04 USD | `-0.53` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `705.92` | `705.92` | `705.06` | `705.27` | `2,312` | 1,631,430.45 USD | -1,127,360.83 USD | `-69.10%` | -58,384,123.87 USD | `-0.30` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `707.72` | `708.30` | `705.86` | `707.06` | `12,664` | 8,952,126.09 USD | -2,613,560.41 USD | `-29.19%` | -54,121,973.64 USD | `-0.78` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `707.06` | `708.59` | `705.90` | `706.20` | `7,630` | 5,397,479.08 USD | -1,123,009.01 USD | `-20.81%` | -55,244,982.65 USD | `+0.03` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `706.19` | `706.93` | `705.06` | `705.26` | `9,672` | 6,829,203.53 USD | -3,139,113.00 USD | `-45.97%` | -58,384,095.66 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `715.88` | `717.47` | `714.28` | `715.79` | `29,695` | 21,257,406.60 USD | -4,255,153.79 USD | `-20.02%` | -37,382,882.21 USD | `-0.32` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `715.79` | `715.89` | `705.71` | `707.71` | `63,287` | 44,957,687.37 USD | -10,972,666.83 USD | `-24.41%` | -48,355,549.04 USD | `-0.95` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `707.72` | `708.59` | `705.06` | `705.26` | `29,966` | 21,178,808.70 USD | -6,875,682.43 USD | `-32.46%` | -55,231,231.47 USD | `-0.46` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `697.96` | `719.84` | `681.03` | `719.55` | `524,764` | 367,784,698.06 USD | -19,177,539.23 USD | `-5.21%` | -18,402,356.22 USD | `-1.45` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `719.56` | `721.67` | `705.71` | `707.71` | `169,364` | 121,053,242.86 USD | -22,399,584.33 USD | `-18.50%` | -40,801,940.55 USD | `-1.24` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `707.72` | `708.59` | `705.06` | `705.27` | `29,966` | 21,178,865.13 USD | -6,875,710.64 USD | `-32.46%` | -47,677,651.18 USD | `+0.10` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `750.62` | `754.90` | `743.07` | `745.33` | `88,414` | 66,199,547.89 USD | 232,195.88 USD | `+0.35%` | 8,277,694.32 USD | `-1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `745.34` | `745.53` | `677.76` | `697.96` | `1,556,116` | 1,101,338,590.19 USD | -7,502,511.31 USD | `-0.68%` | 775,183.01 USD | `-1.22` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `697.96` | `719.84` | `681.03` | `719.55` | `524,764` | 367,784,698.06 USD | -19,177,539.23 USD | `-5.21%` | -18,402,356.22 USD | `-1.45` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `719.56` | `721.67` | `705.71` | `707.71` | `169,364` | 121,053,242.86 USD | -22,399,584.33 USD | `-18.50%` | -40,801,940.55 USD | `-1.24` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `707.72` | `708.59` | `705.06` | `705.27` | `29,966` | 21,178,865.13 USD | -6,875,710.64 USD | `-32.46%` | -47,677,651.18 USD | `+0.10` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| --- | **`704.50`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `704.58` | `954000000.0000` | 672.17 USD | 135,365.01 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `704.59` | `25588000000.0000` | 18,029.05 USD | 134,692.84 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `704.61` | `988000000.0000` | 696.15 USD | 116,663.79 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `704.64` | `1272000000.0000` | 896.30 USD | 115,967.64 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `704.65` | `7988000000.0000` | 5,628.74 USD | 115,071.33 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `704.66` | `27906000000.0000` | 19,664.24 USD | 109,442.59 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `704.67` | `944000000.0000` | 665.21 USD | 89,778.35 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `704.70` | `10284000000.0000` | 7,247.13 USD | 89,113.14 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `704.71` | `15766000000.0000` | 11,110.46 USD | 81,866.01 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `704.72` | `41907000000.0000` | 29,532.70 USD | 70,755.55 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `704.74` | `425000000.0000` | 299.51 USD | 41,222.85 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `704.78` | `1441000000.0000` | 1,015.59 USD | 40,923.33 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `704.79` | `7075000000.0000` | 4,986.39 USD | 39,907.74 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `704.81` | `8849000000.0000` | 6,236.86 USD | 34,921.35 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `704.82` | `12611000000.0000` | 8,888.49 USD | 28,684.49 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `704.85` | `1275000000.0000` | 898.68 USD | 19,796.01 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `704.86` | `11082000000.0000` | 7,811.26 USD | 18,897.32 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `704.87` | `456000000.0000` | 321.42 USD | 11,086.06 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `704.90` | `3740000000.0000` | 2,636.33 USD | 10,764.64 USD | `2 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `704.91` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 704.91` | `0.00%` | `-` |
| `BID` | `704.91` | `11531000000.0000` | 8,128.32 USD | 8,128.32 USD | `3 orders` | `-0.00%` | `-` |
| `ASK` | `704.92` | `1604000000.0000` | 1,130.69 USD | 1,130.69 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `705.00` | `2980000000.0000` | 2,100.90 USD | 3,231.59 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `705.02` | `1617000000.0000` | 1,140.02 USD | 4,371.61 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `705.04` | `1275000000.0000` | 898.93 USD | 5,270.54 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `705.09` | `1272000000.0000` | 896.87 USD | 6,167.41 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `705.11` | `124000000.0000` | 87.43 USD | 6,254.84 USD | `5 orders` | `+0.03%` | `-` |
| `ASK` | `705.12` | `6522000000.0000` | 4,598.79 USD | 10,853.64 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `705.15` | `1272000000.0000` | 896.95 USD | 11,750.59 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `705.17` | `4972000000.0000` | 3,506.11 USD | 15,256.69 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `705.18` | `1587000000.0000` | 1,119.12 USD | 16,375.81 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `705.20` | `300000000.0000` | 211.56 USD | 16,587.37 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `705.21` | `1271000000.0000` | 896.32 USD | 17,483.69 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `705.22` | `150000000.0000` | 105.78 USD | 17,589.48 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `705.23` | `11391000000.0000` | 8,033.27 USD | 25,622.75 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `705.24` | `7816000000.0000` | 5,512.16 USD | 31,134.91 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `705.26` | `9573000000.0000` | 6,751.45 USD | 37,886.36 USD | `3 orders` | `+0.05%` | `-` |
| `ASK` | `705.27` | `1271000000.0000` | 896.40 USD | 38,782.76 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `705.29` | `10403000000.0000` | 7,337.13 USD | 46,119.89 USD | `3 orders` | `+0.05%` | `-` |
| `ASK` | `705.31` | `5768000000.0000` | 4,068.23 USD | 50,188.12 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `705.32` | `2758000000.0000` | 1,945.27 USD | 52,133.39 USD | `2 orders` | `+0.06%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 14:22:11 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `798` | `0xea00...a918` | `LONG` | 2,889,023.59 USD | `4,098,429,000,000.00` | `787.24` | `705.42` | `0.000000` | -337,403.20 USD | `-11.68%` | `5X Cross` |
| `921` | `0xfe7c...b7ae` | `LONG` | 2,462,991.92 USD | `3,491,575,000,000.00` | `686.05` | `705.42` | `0.000000` | 67,581.06 USD | `+2.74%` | `10X Cross` |
| `1053` | `0x7d0c...1b28` | `LONG` | 2,092,098.66 USD | `2,965,934,000,000.00` | `704.22` | `705.42` | `0.000000` | 3,416.84 USD | `+0.16%` | `10X Cross` |
| `1130` | `0x27c9...d65d` | `LONG` | 1,960,521.77 USD | `2,781,237,000,000.00` | `700.84` | `705.42` | `141.92` | 11,311.06 USD | `+0.58%` | `10X Cross` |
| `1189` | `0x7737...bf66` | `SHORT` | 1,866,297.13 USD | `2,646,179,000,000.00` | `752.73` | `705.42` | `7089.26` | 125,573.46 USD | `+6.73%` | `10X Cross` |
| `1365` | `0x51f6...2b39` | `LONG` | 1,580,619.95 USD | `2,240,711,000,000.00` | `703.00` | `705.42` | `105.28` | 5,410.30 USD | `+0.34%` | `10X Cross` |
| `1495` | `0xc675...795d` | `LONG` | 1,448,823.11 USD | `2,055,214,000,000.00` | `706.91` | `705.52` | `640.82` | -4,021.56 USD | `-0.28%` | `10X Cross` |
| `1526` | `0x2edd...8179` | `LONG` | 1,416,807.52 USD | `2,008,488,000,000.00` | `714.56` | `705.52` | `0.000000` | -18,380.16 USD | `-1.30%` | `10X Cross` |
| `1589` | `0x325e...9564` | `LONG` | 1,363,426.04 USD | `1,934,212,000,000.00` | `707.43` | `705.52` | `0.000000` | -4,899.73 USD | `-0.36%` | `10X Cross` |
| `1741` | `0x07fd...689d` | `LONG` | 1,219,200.31 USD | `1,728,406,000,000.00` | `714.40` | `705.52` | `0.000000` | -15,582.67 USD | `-1.28%` | `10X Cross` |
| `1747` | `0x645b...87b8` | `LONG` | 1,214,640.09 USD | `1,721,990,000,000.00` | `747.34` | `705.52` | `0.000000` | -72,267.33 USD | `-5.95%` | `10X Cross` |
| `1793` | `0xecb6...2b00` | `SHORT` | 1,167,638.52 USD | `1,655,342,000,000.00` | `715.05` | `705.52` | `18355.49` | 16,022.30 USD | `+1.37%` | `5X Cross` |
| `1820` | `0xa4a6...46cf` | `SHORT` | 1,145,790.32 USD | `1,625,442,000,000.00` | `711.86` | `705.52` | `1625.33` | 11,302.05 USD | `+0.99%` | `10X Cross` |
| `1879` | `0xfc27...9d9d` | `LONG` | 1,095,584.21 USD | `1,553,205,000,000.00` | `701.14` | `705.52` | `0.000000` | 6,570.42 USD | `+0.60%` | `10X Cross` |
| `1905` | `0x4420...4c4b` | `LONG` | 1,071,564.00 USD | `1,520,143,000,000.00` | `704.02` | `705.52` | `203.01` | 1,353.44 USD | `+0.13%` | `10X Cross` |
| `1922` | `0x14c6...b280` | `SHORT` | 1,058,055.00 USD | `1,500,000,000,000.00` | `712.51` | `705.52` | `1465.20` | 10,706.70 USD | `+1.01%` | `10X Cross` |

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
| `Live` | `Long Liquidation` | `141.50` | 5,520.00 USD | 4,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `142.50` | 273.03 USD | 4,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `143.50` | 4,880.00 USD | 4,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `154.50` | 934.73 USD | 4,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `155.50` | 93,300.00 USD | 4,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `165.50` | 299.22 USD | 4,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `168.50` | 479.72 USD | 4,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `178.50` | 239.90 USD | 4,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `179.50` | 6,090.00 USD | 4,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `180.50` | 124.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `199.50` | 19,950.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `206.50` | 253.38 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `216.50` | 545,610.00 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `219.50` | 191.18 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `223.50` | 862.71 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `242.50` | 8,280.00 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `249.50` | 1,300.00 USD | 4,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `253.50` | 1,340.00 USD | 4,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `265.50` | 158.50 USD | 4,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `267.50` | 21,200.00 USD | 4,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `274.50` | 4,880.00 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `279.50` | 425.12 USD | 4,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `281.50` | 19,550.00 USD | 4,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `287.50` | 428.09 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `293.50` | 11,740.00 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `299.50` | 121.90 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `311.50` | 154,780.00 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `312.50` | 500.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `316.50` | 721.30 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `326.50` | 500.85 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `327.50` | 314.07 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `332.50` | 376.06 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `341.50` | 1,200.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `342.50` | 650.75 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `343.50` | 950.46 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `347.50` | 9,580.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `359.50` | 212.10 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `363.50` | 340.60 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `365.50` | 1,650.00 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `366.50` | 549.75 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `367.50` | 146.63 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `368.50` | 15,810.00 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `370.50` | 16,670.00 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `372.50` | 10,510.00 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `373.50` | 15,780.00 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `374.50` | 1,820.00 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `377.50` | 1,400.00 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `378.50` | 643.45 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `381.50` | 1,910.00 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `382.50` | 10,870.00 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `384.50` | 1,060.00 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `385.50` | 1,800.00 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `386.50` | 2,170.00 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `387.50` | 392.54 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `391.50` | 6,880.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `392.50` | 710.82 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `393.50` | 600.48 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `394.50` | 1,950.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `395.50` | 158.20 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `396.50` | 317.20 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `397.50` | 522.32 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `399.50` | 603.64 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `402.50` | 7,650.00 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `403.50` | 102.09 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `409.50` | 613.02 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `410.50` | 105.91 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `411.50` | 3,480.00 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `413.50` | 10,690.00 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `414.50` | 3,700.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `416.50` | 2,350.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `417.50` | 4,780.00 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `418.50` | 318.06 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `419.50` | 2,650.00 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `421.50` | 2,320.00 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `422.50` | 1,440.00 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `423.50` | 32,950.00 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `424.50` | 31,520.00 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `429.50` | 846.12 USD | 3,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `435.50` | 551.34 USD | 3,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `436.50` | 1,060.00 USD | 3,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `438.50` | 1,790.00 USD | 3,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `440.50` | 1,440.00 USD | 3,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `448.50` | 3,350.00 USD | 3,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `449.50` | 193.28 USD | 3,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `456.50` | 4,730.00 USD | 3,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `462.50` | 662.30 USD | 3,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `463.50` | 927.00 USD | 3,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `464.50` | 396.68 USD | 3,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `469.50` | 4,370.00 USD | 3,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `473.50` | 473.50 USD | 3,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `475.50` | 5,320.00 USD | 3,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `481.50` | 615.36 USD | 3,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `482.50` | 6,840.00 USD | 3,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `484.50` | 2,840.00 USD | 3,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `485.50` | 2,890.00 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `486.50` | 207.25 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `487.50` | 256.91 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `488.50` | 2,300.00 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `492.50` | 1,320.00 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `493.50` | 1,840.00 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `498.50` | 12,120.00 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `499.50` | 1,470.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `500.50` | 2,900.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `501.50` | 14,130.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `502.50` | 109.04 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `504.50` | 680.57 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `505.50` | 9,270.00 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `506.50` | 60,750.00 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `507.50` | 2,950.00 USD | 3,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `508.50` | 992.08 USD | 3,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `509.50` | 3,100.00 USD | 3,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `510.50` | 4,080.00 USD | 3,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `511.50` | 5,180.00 USD | 3,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `513.50` | 2,520.00 USD | 3,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `514.50` | 53,600.00 USD | 3,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `515.50` | 6,470.00 USD | 3,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `517.50` | 23,390.00 USD | 3,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `519.50` | 968.35 USD | 3,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `520.50` | 75,280.00 USD | 3,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `521.50` | 838.05 USD | 3,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `522.50` | 44,110.00 USD | 3,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `524.50` | 833.43 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `526.50` | 1,700.00 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `528.50` | 326.08 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `529.50` | 223,290.00 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `530.50` | 18,330.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `531.50` | 208.88 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `532.50` | 422.81 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `534.50` | 555.35 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `535.50` | 100.14 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `539.50` | 490.94 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `540.50` | 471.32 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `543.50` | 10,350.00 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `544.50` | 210,830.00 USD | 3,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `545.50` | 1,580.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `546.50` | 530.11 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `548.50` | 1,980.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `549.50` | 1,370.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `550.50` | 633.63 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `551.50` | 1,250.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `552.50` | 12,900.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `553.50` | 2,740.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `556.50` | 5,670.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `558.50` | 279.25 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `560.50` | 582.36 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `567.50` | 107.83 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `569.50` | 144.08 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `571.50` | 712,450.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `572.50` | 8,800.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `574.50` | 783.04 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `575.50` | 163,270.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `576.50` | 4,810.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `578.50` | 7,640.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `580.50` | 35,850.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `581.50` | 580.34 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `582.50` | 690.26 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `583.50` | 3,060.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `584.50` | 292.25 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `585.50` | 210.19 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `586.50` | 2,360.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `587.50` | 5,240.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `588.50` | 397.24 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `589.50` | 28,310.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `590.50` | 2,420.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `592.50` | 840.76 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `593.50` | 46,860.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `595.50` | 3,000.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `596.50` | 14,060.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `597.50` | 2,180.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `598.50` | 1,100.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `600.50` | 945.19 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `601.50` | 16,880.00 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `602.50` | 222.32 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `603.50` | 23,410.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `604.50` | 2,780.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `606.50` | 60,810.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `607.50` | 4,250.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `609.50` | 2,550.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `609.90` | 39,280,000.00 USD | 39,280,000.00 USD | 30,470.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `611.50` | 1,580.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `612.50` | 12,250.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `613.50` | 120.25 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `614.50` | 4,280.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `616.50` | 1,540.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `617.50` | 156.23 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `618.50` | 932.70 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `619.50` | 1,410.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `620.50` | 6,520.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `620.90` | 39,250,000.00 USD | 39,250,000.00 USD | 0.00 USD | 55,460.00 USD | 265,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `621.50` | 13,930.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `621.90` | 38,930,000.00 USD | 38,930,000.00 USD | 310,160.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `623.50` | 415.25 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `624.50` | 3,270.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `625.50` | 14,200.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `626.50` | 964.81 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `626.90` | 38,620,000.00 USD | 38,620,000.00 USD | 42,610.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `627.50` | 104.17 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `628.50` | 148.95 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `628.90` | 38,580,000.00 USD | 38,580,000.00 USD | 261,840.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `629.50` | 981.39 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `629.90` | 38,310,000.00 USD | 38,310,000.00 USD | 0.00 USD | 0.00 USD | 255,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `630.50` | 153.21 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `630.90` | 38,060,000.00 USD | 38,060,000.00 USD | 230,570.00 USD | 50,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `631.50` | 2,900.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `631.90` | 37,780,000.00 USD | 37,780,000.00 USD | 58,820.00 USD | 88,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `632.50` | 3,560.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `633.90` | 37,630,000.00 USD | 37,630,000.00 USD | 70,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `634.30` | 48,740,000.00 USD | 48,740,000.00 USD | 28,010.00 USD | 47,460.00 USD | 80,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `634.50` | 5,900.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `634.90` | 37,560,000.00 USD | 37,560,000.00 USD | 0.00 USD | 51,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `635.10` | 48,590,000.00 USD | 48,590,000.00 USD | 0.00 USD | 9,540.00 USD | 82,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `635.50` | 155.06 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `635.90` | 48,500,000.00 USD | 48,500,000.00 USD | 140,670.00 USD | 40,910.00 USD | 12,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `635.90` | 37,510,000.00 USD | 37,510,000.00 USD | 90,060.00 USD | 17,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `636.50` | 1,110.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `636.70` | 48,300,000.00 USD | 48,300,000.00 USD | 120,680.00 USD | 25,980.00 USD | 240,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `637.50` | 47,910,000.00 USD | 47,910,000.00 USD | 69,730.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `637.50` | 305.36 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `638.30` | 47,840,000.00 USD | 47,840,000.00 USD | 24,710.00 USD | 37,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `638.50` | 6,710.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `639.10` | 47,780,000.00 USD | 47,780,000.00 USD | 225,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `639.50` | 455.96 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `639.90` | 47,560,000.00 USD | 47,560,000.00 USD | 21,450.00 USD | 0.00 USD | 184,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `640.50` | 1,320,000.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `640.90` | 37,400,000.00 USD | 37,400,000.00 USD | 0.00 USD | 0.00 USD | 224,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `641.50` | 47,350,000.00 USD | 47,350,000.00 USD | 59,370.00 USD | 0.00 USD | 4,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `641.90` | 37,170,000.00 USD | 37,170,000.00 USD | 0.00 USD | 40,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `642.30` | 47,290,000.00 USD | 47,290,000.00 USD | 177,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `642.50` | 8,480.00 USD | 420,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `642.90` | 37,130,000.00 USD | 37,130,000.00 USD | 171,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `643.10` | 47,110,000.00 USD | 47,110,000.00 USD | 86,980.00 USD | 6,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `643.50` | 339.12 USD | 412,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `643.90` | 47,020,000.00 USD | 47,020,000.00 USD | 29,750.00 USD | 13,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `643.90` | 36,960,000.00 USD | 36,960,000.00 USD | 35,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `644.70` | 46,970,000.00 USD | 46,970,000.00 USD | 423,260.00 USD | 27,730.00 USD | 341,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `644.90` | 36,930,000.00 USD | 36,930,000.00 USD | 0.00 USD | 24,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `645.50` | 46,180,000.00 USD | 46,180,000.00 USD | 61,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `645.90` | 36,900,000.00 USD | 36,900,000.00 USD | 0.00 USD | 0.00 USD | 73,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `646.30` | 46,120,000.00 USD | 46,120,000.00 USD | 156,000.00 USD | 11,780.00 USD | 184,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `646.50` | 463.54 USD | 411,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `646.90` | 36,830,000.00 USD | 36,830,000.00 USD | 45,640.00 USD | 18,000.00 USD | 105,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `647.10` | 45,770,000.00 USD | 45,770,000.00 USD | 204,530.00 USD | 31,640.00 USD | 33,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `647.90` | 45,500,000.00 USD | 45,500,000.00 USD | 136,750.00 USD | 4,630.00 USD | 7,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `647.90` | 36,660,000.00 USD | 36,660,000.00 USD | 122,600.00 USD | 16,830.00 USD | 14,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `648.50` | 1,940.00 USD | 411,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `648.70` | 45,350,000.00 USD | 45,350,000.00 USD | 92,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `648.90` | 36,510,000.00 USD | 36,510,000.00 USD | 0.00 USD | 0.00 USD | 14,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `649.50` | 45,260,000.00 USD | 45,260,000.00 USD | 96,580.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `649.50` | 1,620.00 USD | 409,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `649.90` | 36,490,000.00 USD | 36,490,000.00 USD | 162,040.00 USD | 15,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `650.30` | 45,160,000.00 USD | 45,160,000.00 USD | 17,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `650.50` | 457.30 USD | 407,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `650.90` | 36,310,000.00 USD | 36,310,000.00 USD | 23,920.00 USD | 14,650.00 USD | 14,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `651.10` | 45,140,000.00 USD | 45,140,000.00 USD | 184,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `651.50` | 9,650.00 USD | 407,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `651.90` | 44,960,000.00 USD | 44,960,000.00 USD | 0.00 USD | 0.00 USD | 94,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `651.90` | 36,260,000.00 USD | 36,260,000.00 USD | 92,240.00 USD | 33,210.00 USD | 140,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `652.50` | 652.50 USD | 397,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `652.70` | 44,860,000.00 USD | 44,860,000.00 USD | 30,730.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `652.90` | 35,990,000.00 USD | 35,990,000.00 USD | 213,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `653.50` | 44,830,000.00 USD | 44,830,000.00 USD | 43,630.00 USD | 26,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `653.50` | 97,720.00 USD | 396,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `654.30` | 44,760,000.00 USD | 44,760,000.00 USD | 73,900.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `654.50` | 414.95 USD | 299,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `654.90` | 35,780,000.00 USD | 35,780,000.00 USD | 163,670.00 USD | 8,370.00 USD | 21,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `655.10` | 44,690,000.00 USD | 44,690,000.00 USD | 88,130.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `655.50` | 122.58 USD | 298,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `655.90` | 44,600,000.00 USD | 44,600,000.00 USD | 209,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `655.90` | 35,590,000.00 USD | 35,590,000.00 USD | 47,200.00 USD | 16,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `656.70` | 44,390,000.00 USD | 44,390,000.00 USD | 113,920.00 USD | 40,970.00 USD | 825,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `656.90` | 35,520,000.00 USD | 35,520,000.00 USD | 105,420.00 USD | 0.00 USD | 10,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `657.50` | 43,410,000.00 USD | 43,410,000.00 USD | 248,110.00 USD | 0.00 USD | 21,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `657.90` | 35,410,000.00 USD | 35,410,000.00 USD | 0.00 USD | 7,610.00 USD | 19,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `658.30` | 43,140,000.00 USD | 43,140,000.00 USD | 795,080.00 USD | 14,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `658.50` | 15,090.00 USD | 298,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `658.90` | 35,380,000.00 USD | 35,380,000.00 USD | 0.00 USD | 18,790.00 USD | 13,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `659.10` | 42,330,000.00 USD | 42,330,000.00 USD | 119,820.00 USD | 7,460.00 USD | 81,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `659.50` | 45,510.00 USD | 283,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `659.90` | 42,120,000.00 USD | 42,120,000.00 USD | 111,490.00 USD | 0.00 USD | 14,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `659.90` | 35,350,000.00 USD | 35,350,000.00 USD | 38,970.00 USD | 12,000.00 USD | 98,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `660.50` | 3,410.00 USD | 238,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `660.70` | 42,000,000.00 USD | 42,000,000.00 USD | 90,670.00 USD | 83,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `660.90` | 35,200,000.00 USD | 35,200,000.00 USD | 277,360.00 USD | 17,690.00 USD | 14,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `661.50` | 41,820,000.00 USD | 41,820,000.00 USD | 468,220.00 USD | 19,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `661.50` | 20,140.00 USD | 234,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `661.90` | 34,890,000.00 USD | 34,890,000.00 USD | 123,210.00 USD | 13,120.00 USD | 692,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `662.30` | 41,330,000.00 USD | 41,330,000.00 USD | 165,160.00 USD | 136,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `662.50` | 2,850.00 USD | 214,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `662.90` | 34,060,000.00 USD | 34,060,000.00 USD | 166,320.00 USD | 144,590.00 USD | 36,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `663.10` | 41,030,000.00 USD | 41,030,000.00 USD | 259,470.00 USD | 5,000.00 USD | 44,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `663.50` | 21,880.00 USD | 211,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `663.90` | 40,720,000.00 USD | 40,720,000.00 USD | 45,960.00 USD | 64,390.00 USD | 64,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `663.90` | 33,710,000.00 USD | 33,710,000.00 USD | 943,280.00 USD | 18,740.00 USD | 22,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `664.50` | 10,080.00 USD | 189,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `664.70` | 40,550,000.00 USD | 40,550,000.00 USD | 1,330,000.00 USD | 0.00 USD | 61,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `664.90` | 32,730,000.00 USD | 32,730,000.00 USD | 237,720.00 USD | 22,990.00 USD | 50,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `665.50` | 39,160,000.00 USD | 39,160,000.00 USD | 702,330.00 USD | 4,540.00 USD | 11,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `665.50` | 5,110.00 USD | 179,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `665.90` | 32,420,000.00 USD | 32,420,000.00 USD | 398,250.00 USD | 60,610.00 USD | 63,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `666.30` | 38,440,000.00 USD | 38,440,000.00 USD | 315,600.00 USD | 93,680.00 USD | 750,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `666.50` | 3,150.00 USD | 174,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `666.90` | 31,890,000.00 USD | 31,890,000.00 USD | 425,290.00 USD | 33,320.00 USD | 53,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `667.10` | 37,280,000.00 USD | 37,280,000.00 USD | 902,750.00 USD | 25,280.00 USD | 40,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `667.50` | 1,380.00 USD | 171,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `667.90` | 36,310,000.00 USD | 36,310,000.00 USD | 385,370.00 USD | 150,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `667.90` | 31,380,000.00 USD | 31,380,000.00 USD | 1,050,000.00 USD | 67,080.00 USD | 67,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `668.50` | 1,450.00 USD | 170,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `668.70` | 35,770,000.00 USD | 35,770,000.00 USD | 771,830.00 USD | 39,300.00 USD | 3,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `668.90` | 30,200,000.00 USD | 30,200,000.00 USD | 738,400.00 USD | 70,910.00 USD | 72,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `669.50` | 34,960,000.00 USD | 34,960,000.00 USD | 481,670.00 USD | 61,020.00 USD | 29,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `669.50` | 5,330.00 USD | 168,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `669.90` | 29,320,000.00 USD | 29,320,000.00 USD | 240,000.00 USD | 38,130.00 USD | 71,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `670.30` | 34,390,000.00 USD | 34,390,000.00 USD | 661,320.00 USD | 50,060.00 USD | 1,500,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `670.50` | 2,970.00 USD | 163,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `670.90` | 28,970,000.00 USD | 28,970,000.00 USD | 760,980.00 USD | 135,260.00 USD | 102,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `671.10` | 32,180,000.00 USD | 32,180,000.00 USD | 557,780.00 USD | 13,720.00 USD | 45,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `671.50` | 830.65 USD | 160,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `671.90` | 31,560,000.00 USD | 31,560,000.00 USD | 2,030,000.00 USD | 18,180.00 USD | 6,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `671.90` | 27,970,000.00 USD | 27,970,000.00 USD | 255,560.00 USD | 26,430.00 USD | 684,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `672.50` | 5,320.00 USD | 159,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `672.70` | 29,510,000.00 USD | 29,510,000.00 USD | 136,910.00 USD | 63,880.00 USD | 857,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `672.90` | 27,000,000.00 USD | 27,000,000.00 USD | 1,010,000.00 USD | 159,740.00 USD | 31,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `673.50` | 28,450,000.00 USD | 28,450,000.00 USD | 329,360.00 USD | 298,210.00 USD | 1,560,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `673.50` | 40,830.00 USD | 154,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `673.90` | 25,800,000.00 USD | 25,800,000.00 USD | 335,670.00 USD | 268,790.00 USD | 60,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `674.30` | 26,260,000.00 USD | 26,260,000.00 USD | 328,930.00 USD | 407,150.00 USD | 94,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `674.50` | 4,100.00 USD | 113,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `674.90` | 25,130,000.00 USD | 25,130,000.00 USD | 143,690.00 USD | 129,800.00 USD | 860,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `675.10` | 25,430,000.00 USD | 25,430,000.00 USD | 2,050,000.00 USD | 72,240.00 USD | 392,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `675.50` | 74,720.00 USD | 109,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `675.90` | 22,920,000.00 USD | 22,920,000.00 USD | 621,390.00 USD | 348,940.00 USD | 210,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `675.90` | 24,000,000.00 USD | 24,000,000.00 USD | 394,120.00 USD | 131,610.00 USD | 1,840,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `676.50` | 1,960.00 USD | 34,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `676.70` | 21,740,000.00 USD | 21,740,000.00 USD | 218,210.00 USD | 174,670.00 USD | 281,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `676.90` | 21,640,000.00 USD | 21,640,000.00 USD | 2,140,000.00 USD | 428,700.00 USD | 502,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `677.50` | 21,060,000.00 USD | 21,060,000.00 USD | 214,450.00 USD | 157,160.00 USD | 276,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `677.50` | 438.34 USD | 32,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `677.90` | 18,560,000.00 USD | 18,560,000.00 USD | 752,200.00 USD | 28,030.00 USD | 484,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `678.30` | 20,420,000.00 USD | 20,420,000.00 USD | 1,700,000.00 USD | 157,380.00 USD | 269,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `678.50` | 5,220.00 USD | 32,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `678.90` | 17,300,000.00 USD | 17,300,000.00 USD | 244,010.00 USD | 98,010.00 USD | 43,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `679.10` | 18,290,000.00 USD | 18,290,000.00 USD | 246,070.00 USD | 81,100.00 USD | 34,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `679.50` | 3,580.00 USD | 26,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `679.90` | 17,920,000.00 USD | 17,920,000.00 USD | 1,550,000.00 USD | 246,160.00 USD | 298,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `679.90` | 16,910,000.00 USD | 16,910,000.00 USD | 89,860.00 USD | 65,770.00 USD | 321,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `680.50` | 22,380.00 USD | 23,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `680.70` | 15,830,000.00 USD | 15,830,000.00 USD | 202,340.00 USD | 126,150.00 USD | 187,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `680.90` | 16,430,000.00 USD | 16,430,000.00 USD | 10,590.00 USD | 64,440.00 USD | 167,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `681.50` | 15,310,000.00 USD | 15,310,000.00 USD | 565,710.00 USD | 414,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `681.50` | 939.79 USD | 939.79 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `681.90` | 16,190,000.00 USD | 16,190,000.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `682.30` | 14,330,000.00 USD | 14,330,000.00 USD | 323,390.00 USD | 16,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `682.90` | 14,430,000.00 USD | 14,430,000.00 USD | 39,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `683.10` | 13,990,000.00 USD | 13,990,000.00 USD | 662,310.00 USD | 59,430.00 USD | 37,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `683.90` | 13,230,000.00 USD | 13,230,000.00 USD | 405,890.00 USD | 0.00 USD | 50,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `683.90` | 14,390,000.00 USD | 14,390,000.00 USD | 77,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `684.70` | 12,780,000.00 USD | 12,780,000.00 USD | 138,250.00 USD | 58,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `684.90` | 14,320,000.00 USD | 14,320,000.00 USD | 1,490,000.00 USD | 116,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `685.50` | 12,580,000.00 USD | 12,580,000.00 USD | 589,300.00 USD | 32,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `685.90` | 12,710,000.00 USD | 12,710,000.00 USD | 122,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `686.30` | 11,960,000.00 USD | 11,960,000.00 USD | 937,160.00 USD | 21,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `686.90` | 12,590,000.00 USD | 12,590,000.00 USD | 53,070.00 USD | 71,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `687.10` | 11,000,000.00 USD | 11,000,000.00 USD | 1,010,000.00 USD | 181,980.00 USD | 98,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `687.90` | 9,710,000.00 USD | 9,710,000.00 USD | 192,040.00 USD | 75,530.00 USD | 215,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `687.90` | 12,460,000.00 USD | 12,460,000.00 USD | 142,930.00 USD | 504,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `688.70` | 9,230,000.00 USD | 9,230,000.00 USD | 459,070.00 USD | 107,080.00 USD | 490,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `688.90` | 11,820,000.00 USD | 11,820,000.00 USD | 70,480.00 USD | 253,790.00 USD | 1,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `689.50` | 8,170,000.00 USD | 8,170,000.00 USD | 77,980.00 USD | 37,360.00 USD | 760,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `689.90` | 9,550,000.00 USD | 9,550,000.00 USD | 170,280.00 USD | 0.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `690.30` | 7,300,000.00 USD | 7,300,000.00 USD | 31,110.00 USD | 63,780.00 USD | 212,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `690.90` | 8,340,000.00 USD | 8,340,000.00 USD | 109,680.00 USD | 186,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `691.10` | 6,990,000.00 USD | 6,990,000.00 USD | 0.00 USD | 129,500.00 USD | 75,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `691.90` | 6,790,000.00 USD | 6,790,000.00 USD | 184,180.00 USD | 86,780.00 USD | 116,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `691.90` | 8,050,000.00 USD | 8,050,000.00 USD | 67,140.00 USD | 256,450.00 USD | 1,810,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `692.70` | 6,400,000.00 USD | 6,400,000.00 USD | 673,080.00 USD | 45,970.00 USD | 50,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `692.90` | 5,920,000.00 USD | 5,920,000.00 USD | 803,940.00 USD | 252,070.00 USD | 87,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `693.50` | 5,630,000.00 USD | 5,630,000.00 USD | 145,470.00 USD | 207,190.00 USD | 328,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `693.90` | 4,770,000.00 USD | 4,770,000.00 USD | 0.00 USD | 131,550.00 USD | 317,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `694.30` | 4,950,000.00 USD | 4,950,000.00 USD | 174,860.00 USD | 117,630.00 USD | 180,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `694.90` | 4,320,000.00 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 661,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `695.10` | 4,470,000.00 USD | 4,470,000.00 USD | 306,060.00 USD | 64,240.00 USD | 175,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `695.90` | 3,930,000.00 USD | 3,930,000.00 USD | 153,900.00 USD | 34,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `695.90` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 128,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `696.70` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 95,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `698.30` | 3,640,000.00 USD | 3,640,000.00 USD | 479,860.00 USD | 0.00 USD | 24,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `698.90` | 3,530,000.00 USD | 3,530,000.00 USD | 575,930.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `699.10` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 31,670.00 USD | 42,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `699.90` | 3,070,000.00 USD | 3,070,000.00 USD | 134,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `700.70` | 2,930,000.00 USD | 2,930,000.00 USD | 190,120.00 USD | 42,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `700.90` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 72,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `701.50` | 2,700,000.00 USD | 2,700,000.00 USD | 207,370.00 USD | 222,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `701.90` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 190,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `702.30` | 2,270,000.00 USD | 2,270,000.00 USD | 384,090.00 USD | 98,960.00 USD | 138,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `702.50` | 12,510.00 USD | 12,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `702.90` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 114,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `703.10` | 1,650,000.00 USD | 1,650,000.00 USD | 512,150.00 USD | 58,910.00 USD | 298,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `703.90` | 778,100.00 USD | 778,100.00 USD | 155,960.00 USD | 12,800.00 USD | 376,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `703.90` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `704.70` | 232,430.00 USD | 232,430.00 USD | 62,230.00 USD | 23,130.00 USD | 147,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `704.90` | 1,550,000.00 USD | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `706.30` | 121,180.00 USD | 121,180.00 USD | 121,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `708.50` | 4,550.00 USD | 17,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `709.90` | 677,910.00 USD | 677,910.00 USD | 677,910.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `711.10` | 560,620.00 USD | 560,620.00 USD | 401,530.00 USD | 0.00 USD | 37,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `711.90` | 850,080.00 USD | 850,080.00 USD | 250,690.00 USD | 0.00 USD | 38,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `712.90` | 794,220.00 USD | 794,220.00 USD | 0.00 USD | 116,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `714.50` | 1,920.00 USD | 18,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `715.10` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 415,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `715.90` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 917,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `718.90` | 1,570,000.00 USD | 1,570,000.00 USD | 775,390.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `719.10` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 82,030.00 USD | 36,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `719.90` | 2,720,000.00 USD | 2,720,000.00 USD | 244,770.00 USD | 71,280.00 USD | 104,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `719.90` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 256,450.00 USD | 1,810,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `720.50` | 424.37 USD | 19,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `720.70` | 3,920,000.00 USD | 3,920,000.00 USD | 881,010.00 USD | 250,840.00 USD | 69,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `720.90` | 4,670,000.00 USD | 4,670,000.00 USD | 803,940.00 USD | 146,010.00 USD | 87,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `721.50` | 4,470,000.00 USD | 4,470,000.00 USD | 174,820.00 USD | 240,840.00 USD | 127,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `721.50` | 33,260.00 USD | 52,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `721.90` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 106,060.00 USD | 317,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `722.30` | 5,260,000.00 USD | 5,260,000.00 USD | 274,310.00 USD | 123,420.00 USD | 391,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `722.50` | 1,950.00 USD | 54,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `722.90` | 5,550,000.00 USD | 5,550,000.00 USD | 0.00 USD | 131,550.00 USD | 326,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `723.10` | 5,970,000.00 USD | 5,970,000.00 USD | 257,560.00 USD | 283,040.00 USD | 176,360.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `723.50` | 2,170.00 USD | 56,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `723.90` | 6,800,000.00 USD | 6,800,000.00 USD | 380,140.00 USD | 359,630.00 USD | 88,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `723.90` | 6,820,000.00 USD | 6,820,000.00 USD | 806,150.00 USD | 128,880.00 USD | 335,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `724.50` | 525.26 USD | 57,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `724.70` | 7,350,000.00 USD | 7,350,000.00 USD | 498,970.00 USD | 45,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `725.50` | 7,790,000.00 USD | 7,790,000.00 USD | 289,330.00 USD | 120,790.00 USD | 38,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `725.50` | 1,530.00 USD | 58,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `725.90` | 7,950,000.00 USD | 7,950,000.00 USD | 0.00 USD | 0.00 USD | 1,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `726.30` | 8,060,000.00 USD | 8,060,000.00 USD | 256,420.00 USD | 10,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `726.50` | 4,600.00 USD | 63,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `726.90` | 8,560,000.00 USD | 8,560,000.00 USD | 552,080.00 USD | 58,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `727.10` | 8,660,000.00 USD | 8,660,000.00 USD | 502,440.00 USD | 75,120.00 USD | 24,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `727.50` | 342.65 USD | 63,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `727.90` | 8,850,000.00 USD | 8,850,000.00 USD | 136,640.00 USD | 48,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `727.90` | 9,970,000.00 USD | 9,970,000.00 USD | 575,930.00 USD | 201,080.00 USD | 639,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `728.50` | 41,080.00 USD | 104,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `728.70` | 9,470,000.00 USD | 9,470,000.00 USD | 369,860.00 USD | 48,340.00 USD | 207,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `728.90` | 11,450,000.00 USD | 11,450,000.00 USD | 1,360,000.00 USD | 125,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `729.50` | 10,400,000.00 USD | 10,400,000.00 USD | 171,580.00 USD | 295,150.00 USD | 458,580.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `729.50` | 170,730.00 USD | 275,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `729.90` | 11,820,000.00 USD | 11,820,000.00 USD | 0.00 USD | 365,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `730.30` | 12,980,000.00 USD | 12,980,000.00 USD | 1,950,000.00 USD | 459,490.00 USD | 176,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `730.50` | 28,620.00 USD | 304,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `730.90` | 12,480,000.00 USD | 12,480,000.00 USD | 127,820.00 USD | 219,090.00 USD | 313,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `731.10` | 16,940,000.00 USD | 16,940,000.00 USD | 1,600,000.00 USD | 156,290.00 USD | 2,200,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `731.50` | 2,200.00 USD | 306,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `731.90` | 17,800,000.00 USD | 17,800,000.00 USD | 206,640.00 USD | 152,280.00 USD | 502,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `731.90` | 14,180,000.00 USD | 14,180,000.00 USD | 0.00 USD | 114,370.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `732.50` | 136,960.00 USD | 443,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `732.70` | 20,780,000.00 USD | 20,780,000.00 USD | 1,610,000.00 USD | 119,840.00 USD | 1,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `732.90` | 14,630,000.00 USD | 14,630,000.00 USD | 0.00 USD | 93,300.00 USD | 363,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `733.50` | 21,520,000.00 USD | 21,520,000.00 USD | 62,230.00 USD | 317,290.00 USD | 363,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `733.50` | 15,610.00 USD | 458,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `733.90` | 15,790,000.00 USD | 15,790,000.00 USD | 123,040.00 USD | 128,230.00 USD | 903,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `734.30` | 22,500,000.00 USD | 22,500,000.00 USD | 735,390.00 USD | 43,390.00 USD | 200,410.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `734.50` | 152,680.00 USD | 611,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `734.90` | 16,320,000.00 USD | 16,320,000.00 USD | 456,850.00 USD | 73,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `735.10` | 23,370,000.00 USD | 23,370,000.00 USD | 656,080.00 USD | 197,510.00 USD | 16,020.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `735.50` | 22,600.00 USD | 634,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `735.90` | 24,900,000.00 USD | 24,900,000.00 USD | 642,960.00 USD | 131,120.00 USD | 755,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `735.90` | 16,660,000.00 USD | 16,660,000.00 USD | 90,800.00 USD | 53,030.00 USD | 202,770.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `736.50` | 8,670.00 USD | 642,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `736.70` | 25,410,000.00 USD | 25,410,000.00 USD | 366,260.00 USD | 58,820.00 USD | 90,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `736.90` | 17,070,000.00 USD | 17,070,000.00 USD | 176,450.00 USD | 65,770.00 USD | 163,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `737.50` | 26,040,000.00 USD | 26,040,000.00 USD | 409,970.00 USD | 126,150.00 USD | 87,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `737.50` | 8,780.00 USD | 651,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `737.90` | 17,300,000.00 USD | 17,300,000.00 USD | 0.00 USD | 64,440.00 USD | 167,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `738.30` | 26,590,000.00 USD | 26,590,000.00 USD | 466,620.00 USD | 85,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `738.50` | 8,290.00 USD | 660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `738.90` | 18,170,000.00 USD | 18,170,000.00 USD | 0.00 USD | 166,070.00 USD | 703,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `739.10` | 27,700,000.00 USD | 27,700,000.00 USD | 157,860.00 USD | 16,030.00 USD | 934,700.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `739.50` | 74,970.00 USD | 734,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `739.90` | 27,920,000.00 USD | 27,920,000.00 USD | 187,730.00 USD | 31,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `739.90` | 19,980,000.00 USD | 19,980,000.00 USD | 1,180,000.00 USD | 0.00 USD | 626,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `740.50` | 3,980.00 USD | 738,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `740.70` | 28,340,000.00 USD | 28,340,000.00 USD | 246,020.00 USD | 166,390.00 USD | 12,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `740.90` | 21,190,000.00 USD | 21,190,000.00 USD | 1,180,000.00 USD | 0.00 USD | 33,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `741.50` | 28,970,000.00 USD | 28,970,000.00 USD | 622,710.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `741.50` | 9,510.00 USD | 748,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `741.90` | 21,810,000.00 USD | 21,810,000.00 USD | 287,970.00 USD | 100,540.00 USD | 230,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `742.30` | 29,040,000.00 USD | 29,040,000.00 USD | 56,310.00 USD | 15,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `742.50` | 67,300.00 USD | 815,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `742.90` | 22,460,000.00 USD | 22,460,000.00 USD | 485,340.00 USD | 0.00 USD | 162,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `743.10` | 29,370,000.00 USD | 29,370,000.00 USD | 317,640.00 USD | 15,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `743.50` | 47,230.00 USD | 862,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `743.90` | 29,950,000.00 USD | 29,950,000.00 USD | 16,710.00 USD | 129,570.00 USD | 436,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `743.90` | 23,010,000.00 USD | 23,010,000.00 USD | 160,880.00 USD | 194,060.00 USD | 199,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `744.50` | 117,700.00 USD | 980,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `744.70` | 31,970,000.00 USD | 31,970,000.00 USD | 1,040,000.00 USD | 111,890.00 USD | 871,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `744.90` | 23,260,000.00 USD | 23,260,000.00 USD | 0.00 USD | 244,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `745.50` | 32,870,000.00 USD | 32,870,000.00 USD | 713,060.00 USD | 106,000.00 USD | 78,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `745.50` | 30,410.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `745.90` | 23,710,000.00 USD | 23,710,000.00 USD | 396,930.00 USD | 57,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `746.30` | 33,600,000.00 USD | 33,600,000.00 USD | 451,300.00 USD | 61,130.00 USD | 219,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `746.50` | 187,000.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `746.90` | 24,980,000.00 USD | 24,980,000.00 USD | 324,750.00 USD | 0.00 USD | 948,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `747.10` | 35,080,000.00 USD | 35,080,000.00 USD | 521,800.00 USD | 74,380.00 USD | 881,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `747.90` | 35,460,000.00 USD | 35,460,000.00 USD | 163,850.00 USD | 84,260.00 USD | 133,250.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `748.50` | 23,390.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `748.70` | 35,880,000.00 USD | 35,880,000.00 USD | 404,050.00 USD | 0.00 USD | 17,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `748.90` | 25,380,000.00 USD | 25,380,000.00 USD | 337,680.00 USD | 61,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `749.50` | 36,290,000.00 USD | 36,290,000.00 USD | 406,170.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `749.50` | 69,770.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `749.90` | 25,790,000.00 USD | 25,790,000.00 USD | 404,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `750.30` | 36,380,000.00 USD | 36,380,000.00 USD | 92,750.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `750.50` | 575,140.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `750.90` | 25,860,000.00 USD | 25,860,000.00 USD | 70,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `751.10` | 36,470,000.00 USD | 36,470,000.00 USD | 88,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `751.50` | 11,400.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `751.90` | 37,020,000.00 USD | 37,020,000.00 USD | 86,270.00 USD | 25,010.00 USD | 433,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `751.90` | 25,960,000.00 USD | 25,960,000.00 USD | 105,420.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `752.50` | 57,900.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `752.70` | 37,470,000.00 USD | 37,470,000.00 USD | 349,490.00 USD | 0.00 USD | 105,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `752.90` | 26,320,000.00 USD | 26,320,000.00 USD | 0.00 USD | 0.00 USD | 351,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `753.50` | 37,900,000.00 USD | 37,900,000.00 USD | 158,100.00 USD | 3,810.00 USD | 262,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `753.90` | 26,840,000.00 USD | 26,840,000.00 USD | 406,900.00 USD | 83,030.00 USD | 33,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `754.30` | 38,450,000.00 USD | 38,450,000.00 USD | 438,760.00 USD | 70,850.00 USD | 43,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `754.50` | 863,450.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `754.90` | 26,900,000.00 USD | 26,900,000.00 USD | 0.00 USD | 59,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `755.10` | 38,840,000.00 USD | 38,840,000.00 USD | 157,340.00 USD | 192,190.00 USD | 37,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `755.90` | 39,540,000.00 USD | 39,540,000.00 USD | 576,050.00 USD | 62,280.00 USD | 66,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `755.90` | 27,020,000.00 USD | 27,020,000.00 USD | 120,600.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `756.50` | 3,750.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `756.70` | 39,700,000.00 USD | 39,700,000.00 USD | 87,170.00 USD | 24,970.00 USD | 49,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `756.90` | 27,180,000.00 USD | 27,180,000.00 USD | 0.00 USD | 160,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `757.50` | 40,110,000.00 USD | 40,110,000.00 USD | 198,850.00 USD | 179,910.00 USD | 32,720.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `757.50` | 2,010.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `757.90` | 27,660,000.00 USD | 27,660,000.00 USD | 475,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `758.30` | 41,120,000.00 USD | 41,120,000.00 USD | 757,140.00 USD | 34,450.00 USD | 218,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `758.50` | 180,270.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `758.90` | 29,160,000.00 USD | 29,160,000.00 USD | 1,190,000.00 USD | 55,460.00 USD | 265,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `759.10` | 42,160,000.00 USD | 42,160,000.00 USD | 861,530.00 USD | 117,910.00 USD | 54,810.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `759.50` | 3,830.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `759.90` | 42,530,000.00 USD | 42,530,000.00 USD | 335,910.00 USD | 21,070.00 USD | 15,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `759.90` | 29,520,000.00 USD | 29,520,000.00 USD | 310,160.00 USD | 0.00 USD | 42,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `760.50` | 367,770.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `760.70` | 42,940,000.00 USD | 42,940,000.00 USD | 308,190.00 USD | 52,630.00 USD | 53,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `760.90` | 29,870,000.00 USD | 29,870,000.00 USD | 264,540.00 USD | 27,650.00 USD | 61,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `761.50` | 43,910,000.00 USD | 43,910,000.00 USD | 720,170.00 USD | 8,690.00 USD | 232,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `761.50` | 2,360.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `761.90` | 30,490,000.00 USD | 30,490,000.00 USD | 46,720.00 USD | 282,090.00 USD | 288,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `762.30` | 44,260,000.00 USD | 44,260,000.00 USD | 128,330.00 USD | 124,370.00 USD | 98,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `762.50` | 367.52 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `762.90` | 32,530,000.00 USD | 32,530,000.00 USD | 1,290,000.00 USD | 427,600.00 USD | 324,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `763.10` | 46,870,000.00 USD | 46,870,000.00 USD | 1,940,000.00 USD | 142,770.00 USD | 523,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `763.50` | 603,420.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `763.90` | 47,960,000.00 USD | 47,960,000.00 USD | 890,720.00 USD | 68,590.00 USD | 131,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `763.90` | 35,570,000.00 USD | 35,570,000.00 USD | 2,260,000.00 USD | 329,860.00 USD | 450,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `764.50` | 76,450.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `764.70` | 48,940,000.00 USD | 48,940,000.00 USD | 687,580.00 USD | 147,600.00 USD | 146,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `764.90` | 37,480,000.00 USD | 37,480,000.00 USD | 1,250,000.00 USD | 308,520.00 USD | 346,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `765.50` | 49,340,000.00 USD | 49,340,000.00 USD | 217,860.00 USD | 62,870.00 USD | 118,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `765.90` | 40,850,000.00 USD | 40,850,000.00 USD | 2,560,000.00 USD | 228,800.00 USD | 585,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `766.30` | 50,360,000.00 USD | 50,360,000.00 USD | 652,360.00 USD | 146,240.00 USD | 220,700.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `766.50` | 2,850.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `766.90` | 45,470,000.00 USD | 45,470,000.00 USD | 3,530,000.00 USD | 285,740.00 USD | 801,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `767.10` | 51,780,000.00 USD | 51,780,000.00 USD | 1,230,000.00 USD | 21,380.00 USD | 166,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `767.90` | 52,880,000.00 USD | 52,880,000.00 USD | 851,190.00 USD | 39,510.00 USD | 207,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `767.90` | 49,710,000.00 USD | 49,710,000.00 USD | 3,510,000.00 USD | 173,810.00 USD | 557,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `768.50` | 156.77 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `768.70` | 53,300,000.00 USD | 53,300,000.00 USD | 380,150.00 USD | 25,300.00 USD | 20,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `768.90` | 51,290,000.00 USD | 51,290,000.00 USD | 1,050,000.00 USD | 92,840.00 USD | 436,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `769.50` | 53,640,000.00 USD | 53,640,000.00 USD | 285,410.00 USD | 44,280.00 USD | 8,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `769.90` | 53,330,000.00 USD | 53,330,000.00 USD | 1,240,000.00 USD | 322,290.00 USD | 486,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `770.30` | 53,820,000.00 USD | 53,820,000.00 USD | 82,200.00 USD | 66,110.00 USD | 28,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `770.50` | 881.45 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `770.90` | 55,620,000.00 USD | 55,620,000.00 USD | 1,860,000.00 USD | 259,380.00 USD | 170,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `771.10` | 54,390,000.00 USD | 54,390,000.00 USD | 156,280.00 USD | 56,560.00 USD | 361,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `771.50` | 9,260.00 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `771.90` | 55,180,000.00 USD | 55,180,000.00 USD | 140,150.00 USD | 70,310.00 USD | 582,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `771.90` | 58,460,000.00 USD | 58,460,000.00 USD | 2,000,000.00 USD | 431,660.00 USD | 411,300.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `772.50` | 2,450.00 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `772.70` | 55,550,000.00 USD | 55,550,000.00 USD | 221,230.00 USD | 134,200.00 USD | 16,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `772.90` | 61,480,000.00 USD | 61,480,000.00 USD | 2,310,000.00 USD | 316,340.00 USD | 397,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `773.50` | 56,250,000.00 USD | 56,250,000.00 USD | 618,270.00 USD | 12,950.00 USD | 68,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `773.50` | 4,670.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `773.90` | 63,280,000.00 USD | 63,280,000.00 USD | 1,220,000.00 USD | 270,430.00 USD | 304,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `774.30` | 56,850,000.00 USD | 56,850,000.00 USD | 583,550.00 USD | 11,780.00 USD | 1,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `774.90` | 65,430,000.00 USD | 65,430,000.00 USD | 1,140,000.00 USD | 515,010.00 USD | 490,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `775.10` | 57,040,000.00 USD | 57,040,000.00 USD | 67,380.00 USD | 34,120.00 USD | 86,160.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `775.50` | 544.40 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `775.90` | 57,220,000.00 USD | 57,220,000.00 USD | 98,960.00 USD | 24,070.00 USD | 56,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `775.90` | 67,690,000.00 USD | 67,690,000.00 USD | 1,670,000.00 USD | 274,120.00 USD | 316,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `776.50` | 89,520.00 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `776.70` | 57,580,000.00 USD | 57,580,000.00 USD | 253,970.00 USD | 13,880.00 USD | 92,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `776.90` | 69,280,000.00 USD | 69,280,000.00 USD | 1,370,000.00 USD | 106,550.00 USD | 115,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `777.50` | 58,240,000.00 USD | 58,240,000.00 USD | 510,620.00 USD | 112,090.00 USD | 36,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `777.50` | 209.15 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `777.90` | 71,190,000.00 USD | 71,190,000.00 USD | 1,470,000.00 USD | 240,260.00 USD | 196,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `778.30` | 59,340,000.00 USD | 59,340,000.00 USD | 683,420.00 USD | 72,880.00 USD | 346,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `778.50` | 8,100.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `778.90` | 72,450,000.00 USD | 72,450,000.00 USD | 994,320.00 USD | 117,290.00 USD | 152,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `779.10` | 60,070,000.00 USD | 60,070,000.00 USD | 620,220.00 USD | 33,020.00 USD | 77,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `779.90` | 60,260,000.00 USD | 60,260,000.00 USD | 75,250.00 USD | 75,710.00 USD | 37,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `779.90` | 73,470,000.00 USD | 73,470,000.00 USD | 758,640.00 USD | 125,670.00 USD | 135,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `780.50` | 4,150.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `780.70` | 60,570,000.00 USD | 60,570,000.00 USD | 203,640.00 USD | 32,870.00 USD | 70,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `780.90` | 75,020,000.00 USD | 75,020,000.00 USD | 1,220,000.00 USD | 93,770.00 USD | 240,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `781.50` | 61,040,000.00 USD | 61,040,000.00 USD | 286,730.00 USD | 66,560.00 USD | 121,700.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `781.50` | 1,830.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `781.90` | 77,320,000.00 USD | 77,320,000.00 USD | 1,790,000.00 USD | 118,390.00 USD | 386,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `782.30` | 61,830,000.00 USD | 61,830,000.00 USD | 562,770.00 USD | 6,820.00 USD | 224,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `782.90` | 79,620,000.00 USD | 79,620,000.00 USD | 1,840,000.00 USD | 36,140.00 USD | 427,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `783.10` | 62,350,000.00 USD | 62,350,000.00 USD | 438,920.00 USD | 18,800.00 USD | 61,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `783.90` | 62,470,000.00 USD | 62,470,000.00 USD | 115,530.00 USD | 0.00 USD | 4,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `783.90` | 80,120,000.00 USD | 80,120,000.00 USD | 437,000.00 USD | 10,100.00 USD | 54,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `784.50` | 121.60 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `784.70` | 62,790,000.00 USD | 62,790,000.00 USD | 315,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `784.90` | 80,720,000.00 USD | 80,720,000.00 USD | 424,680.00 USD | 81,720.00 USD | 92,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `785.50` | 62,890,000.00 USD | 62,890,000.00 USD | 96,290.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `785.50` | 457.95 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `785.90` | 81,760,000.00 USD | 81,760,000.00 USD | 932,150.00 USD | 60,930.00 USD | 48,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `786.30` | 62,980,000.00 USD | 62,980,000.00 USD | 85,400.00 USD | 6,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `786.50` | 4,780.00 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `786.90` | 82,500,000.00 USD | 82,500,000.00 USD | 601,980.00 USD | 28,250.00 USD | 104,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `787.10` | 63,030,000.00 USD | 63,030,000.00 USD | 39,820.00 USD | 16,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `787.50` | 315,000.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `787.90` | 63,770,000.00 USD | 63,770,000.00 USD | 373,310.00 USD | 24,670.00 USD | 341,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `787.90` | 82,910,000.00 USD | 82,910,000.00 USD | 261,000.00 USD | 56,730.00 USD | 91,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `788.50` | 1,580.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `788.60` | 63,810,000.00 USD | 63,810,000.00 USD | 38,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `788.90` | 83,800,000.00 USD | 83,800,000.00 USD | 750,800.00 USD | 111,010.00 USD | 28,790.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `789.50` | 1,540.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `789.90` | 84,470,000.00 USD | 84,470,000.00 USD | 327,320.00 USD | 99,920.00 USD | 244,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `790.50` | 632.40 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `790.90` | 85,300,000.00 USD | 85,300,000.00 USD | 657,830.00 USD | 107,360.00 USD | 68,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `791.90` | 86,260,000.00 USD | 86,260,000.00 USD | 841,380.00 USD | 16,830.00 USD | 96,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `792.90` | 86,480,000.00 USD | 86,480,000.00 USD | 205,450.00 USD | 0.00 USD | 14,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `793.50` | 1,280.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `793.90` | 86,640,000.00 USD | 86,640,000.00 USD | 166,240.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `794.50` | 3,640.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `794.90` | 86,900,000.00 USD | 86,900,000.00 USD | 236,740.00 USD | 15,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `795.50` | 518.67 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `795.90` | 87,160,000.00 USD | 87,160,000.00 USD | 93,020.00 USD | 14,650.00 USD | 154,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `796.50` | 567.11 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `796.90` | 87,250,000.00 USD | 87,250,000.00 USD | 62,760.00 USD | 33,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `797.50` | 1,760.00 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `797.90` | 87,360,000.00 USD | 87,360,000.00 USD | 103,930.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `799.50` | 610.02 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `800.50` | 776.49 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `801.50` | 3,410.00 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `802.50` | 778,380.00 USD | 5,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `803.50` | 2,700.00 USD | 5,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `804.50` | 105.39 USD | 5,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `805.50` | 15,370.00 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `806.50` | 2,890.00 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `807.50` | 28,850.00 USD | 5,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `808.50` | 11,780.00 USD | 5,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `809.50` | 173.23 USD | 5,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `812.50` | 434.69 USD | 5,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `814.50` | 692.32 USD | 5,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `815.50` | 8,150.00 USD | 5,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `816.50` | 15,410.00 USD | 5,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `817.50` | 325.37 USD | 5,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `818.50` | 7,720.00 USD | 5,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `821.50` | 27,280.00 USD | 5,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `822.50` | 10,870.00 USD | 5,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `826.50` | 618,360.00 USD | 6,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `828.50` | 2,230.00 USD | 6,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `833.50` | 2,920.00 USD | 6,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `834.50` | 1,010.00 USD | 6,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `837.50` | 3,570.00 USD | 6,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `838.50` | 21,840.00 USD | 6,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `840.50` | 1,150.00 USD | 6,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `841.50` | 2,830.00 USD | 6,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `842.50` | 35,770.00 USD | 6,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `845.50` | 10,760.00 USD | 6,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `848.50` | 289.34 USD | 6,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `850.50` | 108.86 USD | 6,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `851.50` | 285.25 USD | 6,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `855.50` | 7,140.00 USD | 6,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `856.50` | 29,740.00 USD | 6,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `857.50` | 68,600.00 USD | 6,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `858.50` | 523,680.00 USD | 6,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `859.50` | 16,380.00 USD | 6,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `865.50` | 18,900.00 USD | 6,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `868.50` | 290,990.00 USD | 7,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `871.50` | 499.37 USD | 7,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `873.50` | 326.69 USD | 7,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `877.50` | 614,250.00 USD | 7,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `878.50` | 92,600.00 USD | 7,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `879.50` | 14,060.00 USD | 7,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `880.50` | 663.02 USD | 7,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `881.50` | 22,280.00 USD | 7,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `885.50` | 1,770.00 USD | 7,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `886.50` | 812.92 USD | 7,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `887.50` | 385.18 USD | 7,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `888.50` | 88,850.00 USD | 7,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `891.50` | 4,330.00 USD | 7,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `893.50` | 173.34 USD | 7,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `894.50` | 26,840.00 USD | 7,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `895.50` | 223,880.00 USD | 8,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `896.50` | 79,560.00 USD | 8,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `898.50` | 127.59 USD | 8,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `899.50` | 5,400.00 USD | 8,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `901.50` | 50,030.00 USD | 8,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `902.50` | 305.05 USD | 8,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `903.50` | 9,270.00 USD | 8,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `904.50` | 63,930.00 USD | 8,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `906.50` | 37,400.00 USD | 8,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `907.50` | 6,470.00 USD | 8,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `908.50` | 9,280.00 USD | 8,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `909.50` | 634.83 USD | 8,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `910.50` | 16,510.00 USD | 8,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `911.50` | 35,180.00 USD | 8,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `913.50` | 116.93 USD | 8,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `914.50` | 30,060.00 USD | 8,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `918.50` | 133,350.00 USD | 8,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `925.50` | 9,260.00 USD | 8,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `928.50` | 651.81 USD | 8,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `933.50` | 954.04 USD | 8,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `934.50` | 65,420.00 USD | 8,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `939.50` | 3,140.00 USD | 8,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `940.50` | 2,680.00 USD | 8,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `952.50` | 202.88 USD | 8,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `955.50` | 19,020.00 USD | 8,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `964.50` | 6,940.00 USD | 8,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `965.50` | 1,360.00 USD | 8,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `969.50` | 5,780.00 USD | 8,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `970.50` | 1,940.00 USD | 8,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `977.50` | 60,020.00 USD | 8,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `981.50` | 14,480.00 USD | 8,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `983.50` | 14,300.00 USD | 8,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `985.50` | 2,560.00 USD | 8,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `990.50` | 28,300.00 USD | 8,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `992.50` | 2,140.00 USD | 8,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `993.50` | 975.62 USD | 8,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `994.50` | 285,750.00 USD | 9,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `995.50` | 313.58 USD | 9,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `996.50` | 22,470.00 USD | 9,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `997.50` | 632,460.00 USD | 9,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `998.50` | 9,550.00 USD | 9,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `999.50` | 36,850.00 USD | 9,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1003.50` | 838.93 USD | 9,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1005.50` | 297,210.00 USD | 10,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1008.50` | 29,110.00 USD | 10,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1009.50` | 51,370.00 USD | 10,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1011.50` | 302.44 USD | 10,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1014.50` | 761,510.00 USD | 11,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1024.50` | 2,850.00 USD | 11,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1026.50` | 494.77 USD | 11,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1032.50` | 720,280.00 USD | 11,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1048.50` | 65,530.00 USD | 11,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1050.50` | 500.04 USD | 11,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1058.50` | 15,250.00 USD | 11,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1060.50` | 909.91 USD | 11,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1062.50` | 635.38 USD | 11,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1064.50` | 1,760.00 USD | 11,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1066.50` | 7,810.00 USD | 11,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1072.50` | 120.12 USD | 11,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1073.50` | 1,610.00 USD | 11,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1083.50` | 69,250.00 USD | 11,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1087.50` | 5,770.00 USD | 11,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1088.50` | 15,780.00 USD | 11,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1093.50` | 120,790.00 USD | 12,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1096.50` | 810.31 USD | 12,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1109.50` | 75,720.00 USD | 12,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1116.50` | 60,360.00 USD | 12,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1119.50` | 136,380.00 USD | 12,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1125.50` | 150.82 USD | 12,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1134.50` | 1,520.00 USD | 12,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1137.50` | 341,250.00 USD | 12,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1143.50` | 23,170.00 USD | 12,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1145.50` | 359.69 USD | 12,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1146.50` | 119.24 USD | 12,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1154.50` | 11,720.00 USD | 12,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1155.50` | 154.84 USD | 12,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1166.50` | 249.63 USD | 12,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1172.50` | 1,690.00 USD | 12,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1178.50` | 66,060.00 USD | 12,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1183.50` | 166.87 USD | 12,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1191.50` | 57,560.00 USD | 12,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1197.50` | 463.43 USD | 12,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1203.50` | 118,860.00 USD | 12,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1207.50` | 385.19 USD | 12,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1213.50` | 42,470.00 USD | 12,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1215.50` | 30,370.00 USD | 13,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1222.50` | 21,230.00 USD | 13,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1224.50` | 1,030.00 USD | 13,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1226.50` | 3,720.00 USD | 13,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1238.50` | 1,750,000.00 USD | 14,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1246.50` | 199.44 USD | 14,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1249.50` | 4,720.00 USD | 14,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1251.50` | 100.12 USD | 14,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1254.50` | 6,630.00 USD | 14,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1259.50` | 5,030.00 USD | 14,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1263.50` | 113,720.00 USD | 14,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1268.50` | 6,870.00 USD | 14,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1272.50` | 24,700.00 USD | 14,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1282.50` | 61,720.00 USD | 15,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1284.50` | 348.10 USD | 15,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1288.50` | 109,920.00 USD | 15,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1292.50` | 19,310.00 USD | 15,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1295.50` | 181.37 USD | 15,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1299.50` | 4,020.00 USD | 15,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1307.50` | 165,900.00 USD | 15,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1309.50` | 206.90 USD | 15,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1312.50` | 227.06 USD | 15,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1313.50` | 1,850.00 USD | 15,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1315.50` | 92,080.00 USD | 15,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1317.50` | 7,590.00 USD | 15,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1319.50` | 14,130.00 USD | 15,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1321.50` | 2,640.00 USD | 15,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1324.50` | 151,090.00 USD | 15,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1327.50` | 138.06 USD | 15,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1328.50` | 289.61 USD | 15,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1330.50` | 23,470.00 USD | 15,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1341.50` | 30,850.00 USD | 15,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1344.50` | 40,620.00 USD | 15,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1359.50` | 121.00 USD | 15,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1367.50` | 761.70 USD | 15,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1368.50` | 4,110.00 USD | 15,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1369.50` | 46,880.00 USD | 15,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1380.50` | 60,040.00 USD | 15,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1386.50` | 2,520.00 USD | 15,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1390.50` | 510.31 USD | 15,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1392.50` | 69,620.00 USD | 15,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1398.50` | 4,830.00 USD | 15,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1401.50` | 252,270.00 USD | 16,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1405.50` | 4,770.00 USD | 16,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1407.50` | 4,010.00 USD | 16,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `141.50` | 4,970,000.00 USD | 0.00 USD | 5,520.00 USD | `-79.99%` | `38,980,000,000.00` |
| `Live` | `Long` | `142.50` | 4,960,000.00 USD | 0.00 USD | 273.03 USD | `-79.85%` | `1,916,000,000.00` |
| `Live` | `Long` | `143.50` | 4,960,000.00 USD | 0.00 USD | 4,880.00 USD | `-79.71%` | `34,000,000,000.00` |
| `Live` | `Long` | `154.50` | 4,960,000.00 USD | 0.00 USD | 934.73 USD | `-78.15%` | `6,050,000,000.00` |
| `Live` | `Long` | `155.50` | 4,960,000.00 USD | 0.00 USD | 93,300.00 USD | `-78.01%` | `600,000,000,000.00` |
| `Live` | `Long` | `165.50` | 4,860,000.00 USD | 0.00 USD | 299.22 USD | `-76.60%` | `1,808,000,000.00` |
| `Live` | `Long` | `168.50` | 4,860,000.00 USD | 0.00 USD | 479.72 USD | `-76.17%` | `2,847,000,000.00` |
| `Live` | `Long` | `178.50` | 4,860,000.00 USD | 0.00 USD | 239.90 USD | `-74.76%` | `1,344,000,000.00` |
| `Live` | `Long` | `179.50` | 4,860,000.00 USD | 0.00 USD | 6,090.00 USD | `-74.62%` | `33,907,000,000.00` |
| `Live` | `Long` | `180.50` | 4,850,000.00 USD | 0.00 USD | 124.00 USD | `-74.48%` | `687,000,000.00` |
| `Live` | `Long` | `199.50` | 4,850,000.00 USD | 0.00 USD | 19,950.00 USD | `-71.79%` | `100,000,000,000.00` |
| `Live` | `Long` | `206.50` | 4,830,000.00 USD | 0.00 USD | 253.38 USD | `-70.80%` | `1,227,000,000.00` |
| `Live` | `Long` | `216.50` | 4,830,000.00 USD | 0.00 USD | 545,610.00 USD | `-69.39%` | `2,520,143,000,000.00` |
| `Live` | `Long` | `219.50` | 4,290,000.00 USD | 0.00 USD | 191.18 USD | `-68.96%` | `871,000,000.00` |
| `Live` | `Long` | `223.50` | 4,290,000.00 USD | 0.00 USD | 862.71 USD | `-68.40%` | `3,860,000,000.00` |
| `Live` | `Long` | `242.50` | 4,290,000.00 USD | 0.00 USD | 8,280.00 USD | `-65.71%` | `34,129,000,000.00` |
| `Live` | `Long` | `249.50` | 4,280,000.00 USD | 0.00 USD | 1,300.00 USD | `-64.72%` | `5,229,000,000.00` |
| `Live` | `Long` | `253.50` | 4,280,000.00 USD | 0.00 USD | 1,340.00 USD | `-64.16%` | `5,281,000,000.00` |
| `Live` | `Long` | `265.50` | 4,280,000.00 USD | 0.00 USD | 158.50 USD | `-62.46%` | `597,000,000.00` |
| `Live` | `Long` | `267.50` | 4,280,000.00 USD | 0.00 USD | 21,200.00 USD | `-62.18%` | `79,269,000,000.00` |
| `Live` | `Long` | `274.50` | 4,260,000.00 USD | 0.00 USD | 4,880.00 USD | `-61.19%` | `17,770,000,000.00` |
| `Live` | `Long` | `279.50` | 4,250,000.00 USD | 0.00 USD | 425.12 USD | `-60.48%` | `1,521,000,000.00` |
| `Live` | `Long` | `281.50` | 4,250,000.00 USD | 0.00 USD | 19,550.00 USD | `-60.20%` | `69,447,000,000.00` |
| `Live` | `Long` | `287.50` | 4,230,000.00 USD | 0.00 USD | 428.09 USD | `-59.35%` | `1,489,000,000.00` |
| `Live` | `Long` | `293.50` | 4,230,000.00 USD | 0.00 USD | 11,740.00 USD | `-58.50%` | `40,000,000,000.00` |
| `Live` | `Long` | `299.50` | 4,220,000.00 USD | 0.00 USD | 121.90 USD | `-57.65%` | `407,000,000.00` |
| `Live` | `Long` | `311.50` | 4,220,000.00 USD | 0.00 USD | 154,780.00 USD | `-55.95%` | `496,876,000,000.00` |
| `Live` | `Long` | `312.50` | 4,060,000.00 USD | 0.00 USD | 500.00 USD | `-55.81%` | `1,600,000,000.00` |
| `Live` | `Long` | `316.50` | 4,060,000.00 USD | 0.00 USD | 721.30 USD | `-55.25%` | `2,279,000,000.00` |
| `Live` | `Long` | `326.50` | 4,060,000.00 USD | 0.00 USD | 500.85 USD | `-53.83%` | `1,534,000,000.00` |
| `Live` | `Long` | `327.50` | 4,060,000.00 USD | 0.00 USD | 314.07 USD | `-53.69%` | `959,000,000.00` |
| `Live` | `Long` | `332.50` | 4,060,000.00 USD | 0.00 USD | 376.06 USD | `-52.99%` | `1,131,000,000.00` |
| `Live` | `Long` | `341.50` | 4,060,000.00 USD | 0.00 USD | 1,200.00 USD | `-51.71%` | `3,500,000,000.00` |
| `Live` | `Long` | `342.50` | 4,060,000.00 USD | 0.00 USD | 650.75 USD | `-51.57%` | `1,900,000,000.00` |
| `Live` | `Long` | `343.50` | 4,060,000.00 USD | 0.00 USD | 950.46 USD | `-51.43%` | `2,767,000,000.00` |
| `Live` | `Long` | `347.50` | 4,060,000.00 USD | 0.00 USD | 9,580.00 USD | `-50.86%` | `27,554,000,000.00` |
| `Live` | `Long` | `359.50` | 4,050,000.00 USD | 0.00 USD | 212.10 USD | `-49.17%` | `590,000,000.00` |
| `Live` | `Long` | `363.50` | 4,050,000.00 USD | 0.00 USD | 340.60 USD | `-48.60%` | `937,000,000.00` |
| `Live` | `Long` | `365.50` | 4,050,000.00 USD | 0.00 USD | 1,650.00 USD | `-48.32%` | `4,504,000,000.00` |
| `Live` | `Long` | `366.50` | 4,050,000.00 USD | 0.00 USD | 549.75 USD | `-48.18%` | `1,500,000,000.00` |
| `Live` | `Long` | `367.50` | 4,050,000.00 USD | 0.00 USD | 146.63 USD | `-48.04%` | `399,000,000.00` |
| `Live` | `Long` | `368.50` | 4,050,000.00 USD | 0.00 USD | 15,810.00 USD | `-47.90%` | `42,904,000,000.00` |
| `Live` | `Long` | `370.50` | 4,030,000.00 USD | 0.00 USD | 16,670.00 USD | `-47.61%` | `45,000,000,000.00` |
| `Live` | `Long` | `372.50` | 4,010,000.00 USD | 0.00 USD | 10,510.00 USD | `-47.33%` | `28,204,000,000.00` |
| `Live` | `Long` | `373.50` | 4,000,000.00 USD | 0.00 USD | 15,780.00 USD | `-47.19%` | `42,262,000,000.00` |
| `Live` | `Long` | `374.50` | 3,990,000.00 USD | 0.00 USD | 1,820.00 USD | `-47.05%` | `4,868,000,000.00` |
| `Live` | `Long` | `377.50` | 3,990,000.00 USD | 0.00 USD | 1,400.00 USD | `-46.62%` | `3,716,000,000.00` |
| `Live` | `Long` | `378.50` | 3,980,000.00 USD | 0.00 USD | 643.45 USD | `-46.48%` | `1,700,000,000.00` |
| `Live` | `Long` | `381.50` | 3,980,000.00 USD | 0.00 USD | 1,910.00 USD | `-46.06%` | `5,000,000,000.00` |
| `Live` | `Long` | `382.50` | 3,980,000.00 USD | 0.00 USD | 10,870.00 USD | `-45.92%` | `28,414,000,000.00` |
| `Live` | `Long` | `384.50` | 3,970,000.00 USD | 0.00 USD | 1,060.00 USD | `-45.63%` | `2,746,000,000.00` |
| `Live` | `Long` | `385.50` | 3,970,000.00 USD | 0.00 USD | 1,800.00 USD | `-45.49%` | `4,675,000,000.00` |
| `Live` | `Long` | `386.50` | 3,970,000.00 USD | 0.00 USD | 2,170.00 USD | `-45.35%` | `5,625,000,000.00` |
| `Live` | `Long` | `387.50` | 3,970,000.00 USD | 0.00 USD | 392.54 USD | `-45.21%` | `1,013,000,000.00` |
| `Live` | `Long` | `391.50` | 3,960,000.00 USD | 0.00 USD | 6,880.00 USD | `-44.64%` | `17,576,000,000.00` |
| `Live` | `Long` | `392.50` | 3,960,000.00 USD | 0.00 USD | 710.82 USD | `-44.50%` | `1,811,000,000.00` |
| `Live` | `Long` | `393.50` | 3,960,000.00 USD | 0.00 USD | 600.48 USD | `-44.36%` | `1,526,000,000.00` |
| `Live` | `Long` | `394.50` | 3,960,000.00 USD | 0.00 USD | 1,950.00 USD | `-44.22%` | `4,947,000,000.00` |
| `Live` | `Long` | `395.50` | 3,950,000.00 USD | 0.00 USD | 158.20 USD | `-44.08%` | `400,000,000.00` |
| `Live` | `Long` | `396.50` | 3,950,000.00 USD | 0.00 USD | 317.20 USD | `-43.94%` | `800,000,000.00` |
| `Live` | `Long` | `397.50` | 3,950,000.00 USD | 0.00 USD | 522.32 USD | `-43.79%` | `1,314,000,000.00` |
| `Live` | `Long` | `399.50` | 3,950,000.00 USD | 0.00 USD | 603.64 USD | `-43.51%` | `1,511,000,000.00` |
| `Live` | `Long` | `402.50` | 3,950,000.00 USD | 0.00 USD | 7,650.00 USD | `-43.09%` | `19,000,000,000.00` |
| `Live` | `Long` | `403.50` | 3,950,000.00 USD | 0.00 USD | 102.09 USD | `-42.95%` | `253,000,000.00` |
| `Live` | `Long` | `409.50` | 3,950,000.00 USD | 0.00 USD | 613.02 USD | `-42.10%` | `1,497,000,000.00` |
| `Live` | `Long` | `410.50` | 3,940,000.00 USD | 0.00 USD | 105.91 USD | `-41.96%` | `258,000,000.00` |
| `Live` | `Long` | `411.50` | 3,940,000.00 USD | 0.00 USD | 3,480.00 USD | `-41.82%` | `8,455,000,000.00` |
| `Live` | `Long` | `413.50` | 3,940,000.00 USD | 0.00 USD | 10,690.00 USD | `-41.53%` | `25,853,000,000.00` |
| `Live` | `Long` | `414.50` | 3,930,000.00 USD | 0.00 USD | 3,700.00 USD | `-41.39%` | `8,934,000,000.00` |
| `Live` | `Long` | `416.50` | 3,930,000.00 USD | 0.00 USD | 2,350.00 USD | `-41.11%` | `5,644,000,000.00` |
| `Live` | `Long` | `417.50` | 3,920,000.00 USD | 0.00 USD | 4,780.00 USD | `-40.97%` | `11,448,000,000.00` |
| `Live` | `Long` | `418.50` | 3,920,000.00 USD | 0.00 USD | 318.06 USD | `-40.83%` | `760,000,000.00` |
| `Live` | `Long` | `419.50` | 3,920,000.00 USD | 0.00 USD | 2,650.00 USD | `-40.68%` | `6,316,000,000.00` |
| `Live` | `Long` | `421.50` | 3,920,000.00 USD | 0.00 USD | 2,320.00 USD | `-40.40%` | `5,496,000,000.00` |
| `Live` | `Long` | `422.50` | 3,910,000.00 USD | 0.00 USD | 1,440.00 USD | `-40.26%` | `3,419,000,000.00` |
| `Live` | `Long` | `423.50` | 3,910,000.00 USD | 0.00 USD | 32,950.00 USD | `-40.12%` | `77,799,000,000.00` |
| `Live` | `Long` | `424.50` | 3,880,000.00 USD | 0.00 USD | 31,520.00 USD | `-39.98%` | `74,245,000,000.00` |
| `Live` | `Long` | `429.50` | 3,850,000.00 USD | 0.00 USD | 846.12 USD | `-39.27%` | `1,970,000,000.00` |
| `Live` | `Long` | `435.50` | 3,850,000.00 USD | 0.00 USD | 551.34 USD | `-38.42%` | `1,266,000,000.00` |
| `Live` | `Long` | `436.50` | 3,850,000.00 USD | 0.00 USD | 1,060.00 USD | `-38.28%` | `2,420,000,000.00` |
| `Live` | `Long` | `438.50` | 3,850,000.00 USD | 0.00 USD | 1,790.00 USD | `-38.00%` | `4,087,000,000.00` |
| `Live` | `Long` | `440.50` | 3,840,000.00 USD | 0.00 USD | 1,440.00 USD | `-37.71%` | `3,259,000,000.00` |
| `Live` | `Long` | `448.50` | 3,840,000.00 USD | 0.00 USD | 3,350.00 USD | `-36.58%` | `7,470,000,000.00` |
| `Live` | `Long` | `449.50` | 3,840,000.00 USD | 0.00 USD | 193.28 USD | `-36.44%` | `430,000,000.00` |
| `Live` | `Long` | `456.50` | 3,840,000.00 USD | 0.00 USD | 4,730.00 USD | `-35.45%` | `10,359,000,000.00` |
| `Live` | `Long` | `462.50` | 3,830,000.00 USD | 0.00 USD | 662.30 USD | `-34.60%` | `1,432,000,000.00` |
| `Live` | `Long` | `463.50` | 3,830,000.00 USD | 0.00 USD | 927.00 USD | `-34.46%` | `2,000,000,000.00` |
| `Live` | `Long` | `464.50` | 3,830,000.00 USD | 0.00 USD | 396.68 USD | `-34.32%` | `854,000,000.00` |
| `Live` | `Long` | `469.50` | 3,830,000.00 USD | 0.00 USD | 4,370.00 USD | `-33.61%` | `9,301,000,000.00` |
| `Live` | `Long` | `473.50` | 3,830,000.00 USD | 0.00 USD | 473.50 USD | `-33.05%` | `1,000,000,000.00` |
| `Live` | `Long` | `475.50` | 3,830,000.00 USD | 0.00 USD | 5,320.00 USD | `-32.77%` | `11,182,000,000.00` |
| `Live` | `Long` | `481.50` | 3,820,000.00 USD | 0.00 USD | 615.36 USD | `-31.92%` | `1,278,000,000.00` |
| `Live` | `Long` | `482.50` | 3,820,000.00 USD | 0.00 USD | 6,840.00 USD | `-31.78%` | `14,184,000,000.00` |
| `Live` | `Long` | `484.50` | 3,820,000.00 USD | 0.00 USD | 2,840.00 USD | `-31.49%` | `5,864,000,000.00` |
| `Live` | `Long` | `485.50` | 3,810,000.00 USD | 0.00 USD | 2,890.00 USD | `-31.35%` | `5,947,000,000.00` |
| `Live` | `Long` | `486.50` | 3,810,000.00 USD | 0.00 USD | 207.25 USD | `-31.21%` | `426,000,000.00` |
| `Live` | `Long` | `487.50` | 3,810,000.00 USD | 0.00 USD | 256.91 USD | `-31.07%` | `527,000,000.00` |
| `Live` | `Long` | `488.50` | 3,810,000.00 USD | 0.00 USD | 2,300.00 USD | `-30.93%` | `4,712,000,000.00` |
| `Live` | `Long` | `492.50` | 3,810,000.00 USD | 0.00 USD | 1,320.00 USD | `-30.36%` | `2,682,000,000.00` |
| `Live` | `Long` | `493.50` | 3,810,000.00 USD | 0.00 USD | 1,840.00 USD | `-30.22%` | `3,720,000,000.00` |
| `Live` | `Long` | `498.50` | 3,800,000.00 USD | 0.00 USD | 12,120.00 USD | `-29.51%` | `24,317,000,000.00` |
| `Live` | `Long` | `499.50` | 3,790,000.00 USD | 0.00 USD | 1,470.00 USD | `-29.37%` | `2,948,000,000.00` |
| `Live` | `Long` | `500.50` | 3,790,000.00 USD | 0.00 USD | 2,900.00 USD | `-29.23%` | `5,804,000,000.00` |
| `Live` | `Long` | `501.50` | 3,790,000.00 USD | 0.00 USD | 14,130.00 USD | `-29.09%` | `28,185,000,000.00` |
| `Live` | `Long` | `502.50` | 3,770,000.00 USD | 0.00 USD | 109.04 USD | `-28.95%` | `217,000,000.00` |
| `Live` | `Long` | `504.50` | 3,770,000.00 USD | 0.00 USD | 680.57 USD | `-28.67%` | `1,349,000,000.00` |
| `Live` | `Long` | `505.50` | 3,770,000.00 USD | 0.00 USD | 9,270.00 USD | `-28.52%` | `18,331,000,000.00` |
| `Live` | `Long` | `506.50` | 3,760,000.00 USD | 0.00 USD | 60,750.00 USD | `-28.38%` | `119,940,000,000.00` |
| `Live` | `Long` | `507.50` | 3,700,000.00 USD | 0.00 USD | 2,950.00 USD | `-28.24%` | `5,809,000,000.00` |
| `Live` | `Long` | `508.50` | 3,700,000.00 USD | 0.00 USD | 992.08 USD | `-28.10%` | `1,951,000,000.00` |
| `Live` | `Long` | `509.50` | 3,700,000.00 USD | 0.00 USD | 3,100.00 USD | `-27.96%` | `6,091,000,000.00` |
| `Live` | `Long` | `510.50` | 3,690,000.00 USD | 0.00 USD | 4,080.00 USD | `-27.82%` | `8,000,000,000.00` |
| `Live` | `Long` | `511.50` | 3,690,000.00 USD | 0.00 USD | 5,180.00 USD | `-27.68%` | `10,118,000,000.00` |
| `Live` | `Long` | `513.50` | 3,690,000.00 USD | 0.00 USD | 2,520.00 USD | `-27.39%` | `4,914,000,000.00` |
| `Live` | `Long` | `514.50` | 3,680,000.00 USD | 0.00 USD | 53,600.00 USD | `-27.25%` | `104,175,000,000.00` |
| `Live` | `Long` | `515.50` | 3,630,000.00 USD | 0.00 USD | 6,470.00 USD | `-27.11%` | `12,554,000,000.00` |
| `Live` | `Long` | `517.50` | 3,620,000.00 USD | 0.00 USD | 23,390.00 USD | `-26.83%` | `45,193,000,000.00` |
| `Live` | `Long` | `519.50` | 3,600,000.00 USD | 0.00 USD | 968.35 USD | `-26.54%` | `1,864,000,000.00` |
| `Live` | `Long` | `520.50` | 3,600,000.00 USD | 0.00 USD | 75,280.00 USD | `-26.40%` | `144,633,000,000.00` |
| `Live` | `Long` | `521.50` | 3,520,000.00 USD | 0.00 USD | 838.05 USD | `-26.26%` | `1,607,000,000.00` |
| `Live` | `Long` | `522.50` | 3,520,000.00 USD | 0.00 USD | 44,110.00 USD | `-26.12%` | `84,425,000,000.00` |
| `Live` | `Long` | `524.50` | 3,480,000.00 USD | 0.00 USD | 833.43 USD | `-25.84%` | `1,589,000,000.00` |
| `Live` | `Long` | `526.50` | 3,480,000.00 USD | 0.00 USD | 1,700.00 USD | `-25.55%` | `3,234,000,000.00` |
| `Live` | `Long` | `528.50` | 3,480,000.00 USD | 0.00 USD | 326.08 USD | `-25.27%` | `617,000,000.00` |
| `Live` | `Long` | `529.50` | 3,480,000.00 USD | 0.00 USD | 223,290.00 USD | `-25.13%` | `421,708,000,000.00` |
| `Live` | `Long` | `530.50` | 3,250,000.00 USD | 0.00 USD | 18,330.00 USD | `-24.99%` | `34,547,000,000.00` |
| `Live` | `Long` | `531.50` | 3,230,000.00 USD | 0.00 USD | 208.88 USD | `-24.85%` | `393,000,000.00` |
| `Live` | `Long` | `532.50` | 3,230,000.00 USD | 0.00 USD | 422.81 USD | `-24.71%` | `794,000,000.00` |
| `Live` | `Long` | `534.50` | 3,230,000.00 USD | 0.00 USD | 555.35 USD | `-24.42%` | `1,039,000,000.00` |
| `Live` | `Long` | `535.50` | 3,230,000.00 USD | 0.00 USD | 100.14 USD | `-24.28%` | `187,000,000.00` |
| `Live` | `Long` | `539.50` | 3,230,000.00 USD | 0.00 USD | 490.94 USD | `-23.72%` | `910,000,000.00` |
| `Live` | `Long` | `540.50` | 3,230,000.00 USD | 0.00 USD | 471.32 USD | `-23.58%` | `872,000,000.00` |
| `Live` | `Long` | `543.50` | 3,230,000.00 USD | 0.00 USD | 10,350.00 USD | `-23.15%` | `19,044,000,000.00` |
| `Live` | `Long` | `544.50` | 3,220,000.00 USD | 0.00 USD | 210,830.00 USD | `-23.01%` | `387,204,000,000.00` |
| `Live` | `Long` | `545.50` | 3,010,000.00 USD | 0.00 USD | 1,580.00 USD | `-22.87%` | `2,900,000,000.00` |
| `Live` | `Long` | `546.50` | 3,010,000.00 USD | 0.00 USD | 530.11 USD | `-22.73%` | `970,000,000.00` |
| `Live` | `Long` | `548.50` | 3,010,000.00 USD | 0.00 USD | 1,980.00 USD | `-22.44%` | `3,611,000,000.00` |
| `Live` | `Long` | `549.50` | 3,010,000.00 USD | 0.00 USD | 1,370.00 USD | `-22.30%` | `2,496,000,000.00` |
| `Live` | `Long` | `550.50` | 3,010,000.00 USD | 0.00 USD | 633.63 USD | `-22.16%` | `1,151,000,000.00` |
| `Live` | `Long` | `551.50` | 3,000,000.00 USD | 0.00 USD | 1,250.00 USD | `-22.02%` | `2,271,000,000.00` |
| `Live` | `Long` | `552.50` | 3,000,000.00 USD | 0.00 USD | 12,900.00 USD | `-21.88%` | `23,349,000,000.00` |
| `Live` | `Long` | `553.50` | 2,990,000.00 USD | 0.00 USD | 2,740.00 USD | `-21.74%` | `4,955,000,000.00` |
| `Live` | `Long` | `556.50` | 2,990,000.00 USD | 0.00 USD | 5,670.00 USD | `-21.31%` | `10,193,000,000.00` |
| `Live` | `Long` | `558.50` | 2,980,000.00 USD | 0.00 USD | 279.25 USD | `-21.03%` | `500,000,000.00` |
| `Live` | `Long` | `560.50` | 2,980,000.00 USD | 0.00 USD | 582.36 USD | `-20.75%` | `1,039,000,000.00` |
| `Live` | `Long` | `567.50` | 2,980,000.00 USD | 0.00 USD | 107.83 USD | `-19.76%` | `190,000,000.00` |
| `Live` | `Long` | `569.50` | 2,980,000.00 USD | 0.00 USD | 144.08 USD | `-19.47%` | `253,000,000.00` |
| `Live` | `Long` | `571.50` | 2,980,000.00 USD | 0.00 USD | 712,450.00 USD | `-19.19%` | `1,246,635,000,000.00` |
| `Live` | `Long` | `572.50` | 2,270,000.00 USD | 0.00 USD | 8,800.00 USD | `-19.05%` | `15,374,000,000.00` |
| `Live` | `Long` | `574.50` | 2,260,000.00 USD | 0.00 USD | 783.04 USD | `-18.77%` | `1,363,000,000.00` |
| `Live` | `Long` | `575.50` | 2,260,000.00 USD | 0.00 USD | 163,270.00 USD | `-18.63%` | `283,700,000,000.00` |
| `Live` | `Long` | `576.50` | 2,100,000.00 USD | 0.00 USD | 4,810.00 USD | `-18.48%` | `8,349,000,000.00` |
| `Live` | `Long` | `578.50` | 2,090,000.00 USD | 0.00 USD | 7,640.00 USD | `-18.20%` | `13,202,000,000.00` |
| `Live` | `Long` | `580.50` | 2,080,000.00 USD | 0.00 USD | 35,850.00 USD | `-17.92%` | `61,765,000,000.00` |
| `Live` | `Long` | `581.50` | 2,050,000.00 USD | 0.00 USD | 580.34 USD | `-17.78%` | `998,000,000.00` |
| `Live` | `Long` | `582.50` | 2,050,000.00 USD | 0.00 USD | 690.26 USD | `-17.64%` | `1,185,000,000.00` |
| `Live` | `Long` | `583.50` | 2,050,000.00 USD | 0.00 USD | 3,060.00 USD | `-17.50%` | `5,239,000,000.00` |
| `Live` | `Long` | `584.50` | 2,040,000.00 USD | 0.00 USD | 292.25 USD | `-17.35%` | `500,000,000.00` |
| `Live` | `Long` | `585.50` | 2,040,000.00 USD | 0.00 USD | 210.19 USD | `-17.21%` | `359,000,000.00` |
| `Live` | `Long` | `586.50` | 2,040,000.00 USD | 0.00 USD | 2,360.00 USD | `-17.07%` | `4,022,000,000.00` |
| `Live` | `Long` | `587.50` | 2,040,000.00 USD | 0.00 USD | 5,240.00 USD | `-16.93%` | `8,916,000,000.00` |
| `Live` | `Long` | `588.50` | 2,030,000.00 USD | 0.00 USD | 397.24 USD | `-16.79%` | `675,000,000.00` |
| `Live` | `Long` | `589.50` | 2,030,000.00 USD | 0.00 USD | 28,310.00 USD | `-16.65%` | `48,027,000,000.00` |
| `Live` | `Long` | `590.50` | 2,010,000.00 USD | 0.00 USD | 2,420.00 USD | `-16.51%` | `4,106,000,000.00` |
| `Live` | `Long` | `592.50` | 2,000,000.00 USD | 0.00 USD | 840.76 USD | `-16.22%` | `1,419,000,000.00` |
| `Live` | `Long` | `593.50` | 2,000,000.00 USD | 0.00 USD | 46,860.00 USD | `-16.08%` | `78,961,000,000.00` |
| `Live` | `Long` | `595.50` | 1,960,000.00 USD | 0.00 USD | 3,000.00 USD | `-15.80%` | `5,043,000,000.00` |
| `Live` | `Long` | `596.50` | 1,950,000.00 USD | 0.00 USD | 14,060.00 USD | `-15.66%` | `23,572,000,000.00` |
| `Live` | `Long` | `597.50` | 1,940,000.00 USD | 0.00 USD | 2,180.00 USD | `-15.52%` | `3,646,000,000.00` |
| `Live` | `Long` | `598.50` | 1,940,000.00 USD | 0.00 USD | 1,100.00 USD | `-15.37%` | `1,832,000,000.00` |
| `Live` | `Long` | `600.50` | 1,940,000.00 USD | 0.00 USD | 945.19 USD | `-15.09%` | `1,574,000,000.00` |
| `Live` | `Long` | `601.50` | 1,930,000.00 USD | 0.00 USD | 16,880.00 USD | `-14.95%` | `28,061,000,000.00` |
| `Live` | `Long` | `602.50` | 1,920,000.00 USD | 0.00 USD | 222.32 USD | `-14.81%` | `369,000,000.00` |
| `Live` | `Long` | `603.50` | 1,920,000.00 USD | 0.00 USD | 23,410.00 USD | `-14.67%` | `38,785,000,000.00` |
| `Live` | `Long` | `604.50` | 1,890,000.00 USD | 0.00 USD | 2,780.00 USD | `-14.53%` | `4,607,000,000.00` |
| `Live` | `Long` | `606.50` | 1,890,000.00 USD | 0.00 USD | 60,810.00 USD | `-14.24%` | `100,260,000,000.00` |
| `Live` | `Long` | `607.50` | 1,830,000.00 USD | 0.00 USD | 4,250.00 USD | `-14.10%` | `7,002,000,000.00` |
| `Live` | `Long` | `609.50` | 1,830,000.00 USD | 0.00 USD | 2,550.00 USD | `-13.82%` | `4,188,000,000.00` |
| `Live` | `Long` | `611.50` | 1,820,000.00 USD | 0.00 USD | 1,580.00 USD | `-13.54%` | `2,584,000,000.00` |
| `Live` | `Long` | `612.50` | 1,820,000.00 USD | 0.00 USD | 12,250.00 USD | `-13.39%` | `20,000,000,000.00` |
| `Live` | `Long` | `613.50` | 1,810,000.00 USD | 0.00 USD | 120.25 USD | `-13.25%` | `196,000,000.00` |
| `Live` | `Long` | `614.50` | 1,810,000.00 USD | 0.00 USD | 4,280.00 USD | `-13.11%` | `6,973,000,000.00` |
| `Live` | `Long` | `616.50` | 1,810,000.00 USD | 0.00 USD | 1,540.00 USD | `-12.83%` | `2,500,000,000.00` |
| `Live` | `Long` | `617.50` | 1,800,000.00 USD | 0.00 USD | 156.23 USD | `-12.69%` | `253,000,000.00` |
| `Live` | `Long` | `618.50` | 1,800,000.00 USD | 0.00 USD | 932.70 USD | `-12.55%` | `1,508,000,000.00` |
| `Live` | `Long` | `619.50` | 1,800,000.00 USD | 0.00 USD | 1,410.00 USD | `-12.40%` | `2,279,000,000.00` |
| `Live` | `Long` | `620.50` | 1,800,000.00 USD | 0.00 USD | 6,520.00 USD | `-12.26%` | `10,506,000,000.00` |
| `Live` | `Long` | `621.50` | 1,790,000.00 USD | 0.00 USD | 13,930.00 USD | `-12.12%` | `22,412,000,000.00` |
| `Live` | `Long` | `623.50` | 1,780,000.00 USD | 0.00 USD | 415.25 USD | `-11.84%` | `666,000,000.00` |
| `Live` | `Long` | `624.50` | 1,780,000.00 USD | 0.00 USD | 3,270.00 USD | `-11.70%` | `5,239,000,000.00` |
| `Live` | `Long` | `625.50` | 1,780,000.00 USD | 0.00 USD | 14,200.00 USD | `-11.56%` | `22,702,000,000.00` |
| `Live` | `Long` | `626.50` | 1,760,000.00 USD | 0.00 USD | 964.81 USD | `-11.41%` | `1,540,000,000.00` |
| `Live` | `Long` | `627.50` | 1,760,000.00 USD | 0.00 USD | 104.17 USD | `-11.27%` | `166,000,000.00` |
| `Live` | `Long` | `628.50` | 1,760,000.00 USD | 0.00 USD | 148.95 USD | `-11.13%` | `237,000,000.00` |
| `Live` | `Long` | `629.50` | 1,760,000.00 USD | 0.00 USD | 981.39 USD | `-10.99%` | `1,559,000,000.00` |
| `Live` | `Long` | `630.50` | 1,760,000.00 USD | 0.00 USD | 153.21 USD | `-10.85%` | `243,000,000.00` |
| `Live` | `Long` | `631.50` | 1,760,000.00 USD | 0.00 USD | 2,900.00 USD | `-10.71%` | `4,587,000,000.00` |
| `Live` | `Long` | `632.50` | 1,760,000.00 USD | 0.00 USD | 3,560.00 USD | `-10.57%` | `5,633,000,000.00` |
| `Live` | `Long` | `634.50` | 1,750,000.00 USD | 0.00 USD | 5,900.00 USD | `-10.28%` | `9,302,000,000.00` |
| `Live` | `Long` | `635.50` | 1,750,000.00 USD | 0.00 USD | 155.06 USD | `-10.14%` | `244,000,000.00` |
| `Live` | `Long` | `636.50` | 1,750,000.00 USD | 0.00 USD | 1,110.00 USD | `-10.00%` | `1,743,000,000.00` |
| `Live` | `Long` | `637.50` | 1,750,000.00 USD | 0.00 USD | 305.36 USD | `-9.86%` | `479,000,000.00` |
| `Live` | `Long` | `638.50` | 1,750,000.00 USD | 0.00 USD | 6,710.00 USD | `-9.72%` | `10,515,000,000.00` |
| `Live` | `Long` | `639.50` | 1,740,000.00 USD | 0.00 USD | 455.96 USD | `-9.58%` | `713,000,000.00` |
| `Live` | `Long` | `640.50` | 1,740,000.00 USD | 0.00 USD | 1,320,000.00 USD | `-9.44%` | `2,059,440,000,000.00` |
| `Live` | `Long` | `642.50` | 420,530.00 USD | 0.00 USD | 8,480.00 USD | `-9.15%` | `13,199,000,000.00` |
| `Live` | `Long` | `643.50` | 412,050.00 USD | 0.00 USD | 339.12 USD | `-9.01%` | `527,000,000.00` |
| `Live` | `Long` | `646.50` | 411,710.00 USD | 0.00 USD | 463.54 USD | `-8.59%` | `717,000,000.00` |
| `Live` | `Long` | `648.50` | 411,250.00 USD | 0.00 USD | 1,940.00 USD | `-8.30%` | `2,988,000,000.00` |
| `Live` | `Long` | `649.50` | 409,310.00 USD | 0.00 USD | 1,620.00 USD | `-8.16%` | `2,501,000,000.00` |
| `Live` | `Long` | `650.50` | 407,690.00 USD | 0.00 USD | 457.30 USD | `-8.02%` | `703,000,000.00` |
| `Live` | `Long` | `651.50` | 407,230.00 USD | 0.00 USD | 9,650.00 USD | `-7.88%` | `14,806,000,000.00` |
| `Live` | `Long` | `652.50` | 397,580.00 USD | 0.00 USD | 652.50 USD | `-7.74%` | `1,000,000,000.00` |
| `Live` | `Long` | `653.50` | 396,930.00 USD | 0.00 USD | 97,720.00 USD | `-7.60%` | `149,529,000,000.00` |
| `Live` | `Long` | `654.50` | 299,210.00 USD | 0.00 USD | 414.95 USD | `-7.46%` | `634,000,000.00` |
| `Live` | `Long` | `655.50` | 298,800.00 USD | 0.00 USD | 122.58 USD | `-7.31%` | `187,000,000.00` |
| `Live` | `Long` | `658.50` | 298,680.00 USD | 0.00 USD | 15,090.00 USD | `-6.89%` | `22,916,000,000.00` |
| `Live` | `Long` | `659.50` | 283,590.00 USD | 0.00 USD | 45,510.00 USD | `-6.75%` | `69,000,000,000.00` |
| `Live` | `Long` | `660.50` | 238,080.00 USD | 0.00 USD | 3,410.00 USD | `-6.61%` | `5,167,000,000.00` |
| `Live` | `Long` | `661.50` | 234,670.00 USD | 0.00 USD | 20,140.00 USD | `-6.47%` | `30,450,000,000.00` |
| `Live` | `Long` | `662.50` | 214,530.00 USD | 0.00 USD | 2,850.00 USD | `-6.32%` | `4,297,000,000.00` |
| `Live` | `Long` | `663.50` | 211,680.00 USD | 0.00 USD | 21,880.00 USD | `-6.18%` | `32,975,000,000.00` |
| `Live` | `Long` | `664.50` | 189,800.00 USD | 0.00 USD | 10,080.00 USD | `-6.04%` | `15,175,000,000.00` |
| `Live` | `Long` | `665.50` | 179,720.00 USD | 0.00 USD | 5,110.00 USD | `-5.90%` | `7,683,000,000.00` |
| `Live` | `Long` | `666.50` | 174,600.00 USD | 0.00 USD | 3,150.00 USD | `-5.76%` | `4,728,000,000.00` |
| `Live` | `Long` | `667.50` | 171,450.00 USD | 0.00 USD | 1,380.00 USD | `-5.62%` | `2,067,000,000.00` |
| `Live` | `Long` | `668.50` | 170,070.00 USD | 0.00 USD | 1,450.00 USD | `-5.48%` | `2,164,000,000.00` |
| `Live` | `Long` | `669.50` | 168,630.00 USD | 0.00 USD | 5,330.00 USD | `-5.33%` | `7,967,000,000.00` |
| `Live` | `Long` | `670.50` | 163,290.00 USD | 0.00 USD | 2,970.00 USD | `-5.19%` | `4,436,000,000.00` |
| `Live` | `Long` | `671.50` | 160,320.00 USD | 0.00 USD | 830.65 USD | `-5.05%` | `1,237,000,000.00` |
| `Live` | `Long` | `672.50` | 159,490.00 USD | 0.00 USD | 5,320.00 USD | `-4.91%` | `7,908,000,000.00` |
| `Live` | `Long` | `673.50` | 154,170.00 USD | 0.00 USD | 40,830.00 USD | `-4.77%` | `60,630,000,000.00` |
| `Live` | `Long` | `674.50` | 113,330.00 USD | 0.00 USD | 4,100.00 USD | `-4.63%` | `6,078,000,000.00` |
| `Live` | `Long` | `675.50` | 109,230.00 USD | 0.00 USD | 74,720.00 USD | `-4.49%` | `110,607,000,000.00` |
| `Live` | `Long` | `676.50` | 34,520.00 USD | 0.00 USD | 1,960.00 USD | `-4.35%` | `2,901,000,000.00` |
| `Live` | `Long` | `677.50` | 32,560.00 USD | 0.00 USD | 438.34 USD | `-4.20%` | `647,000,000.00` |
| `Live` | `Long` | `678.50` | 32,120.00 USD | 0.00 USD | 5,220.00 USD | `-4.06%` | `7,688,000,000.00` |
| `Live` | `Long` | `679.50` | 26,900.00 USD | 0.00 USD | 3,580.00 USD | `-3.92%` | `5,266,000,000.00` |
| `Live` | `Long` | `680.50` | 23,320.00 USD | 0.00 USD | 22,380.00 USD | `-3.78%` | `32,894,000,000.00` |
| `Live` | `Long` | `681.50` | 939.79 USD | 0.00 USD | 939.79 USD | `-3.64%` | `1,379,000,000.00` |
| `Live` | `Short` | `702.50` | 12,510.00 USD | 12,510.00 USD | 0.00 USD | `-0.67%` | `17,808,000,000.00` |
| `Live` | `Short` | `708.50` | 17,060.00 USD | 4,550.00 USD | 0.00 USD | `+0.18%` | `6,418,000,000.00` |
| `Live` | `Short` | `714.50` | 18,980.00 USD | 1,920.00 USD | 0.00 USD | `+1.03%` | `2,691,000,000.00` |
| `Live` | `Short` | `720.50` | 19,400.00 USD | 424.37 USD | 0.00 USD | `+1.88%` | `589,000,000.00` |
| `Live` | `Short` | `721.50` | 52,660.00 USD | 33,260.00 USD | 0.00 USD | `+2.02%` | `46,099,000,000.00` |
| `Live` | `Short` | `722.50` | 54,620.00 USD | 1,950.00 USD | 0.00 USD | `+2.16%` | `2,702,000,000.00` |
| `Live` | `Short` | `723.50` | 56,780.00 USD | 2,170.00 USD | 0.00 USD | `+2.30%` | `2,996,000,000.00` |
| `Live` | `Short` | `724.50` | 57,310.00 USD | 525.26 USD | 0.00 USD | `+2.44%` | `725,000,000.00` |
| `Live` | `Short` | `725.50` | 58,840.00 USD | 1,530.00 USD | 0.00 USD | `+2.58%` | `2,108,000,000.00` |
| `Live` | `Short` | `726.50` | 63,440.00 USD | 4,600.00 USD | 0.00 USD | `+2.72%` | `6,327,000,000.00` |
| `Live` | `Short` | `727.50` | 63,780.00 USD | 342.65 USD | 0.00 USD | `+2.87%` | `471,000,000.00` |
| `Live` | `Short` | `728.50` | 104,850.00 USD | 41,080.00 USD | 0.00 USD | `+3.01%` | `56,385,000,000.00` |
| `Live` | `Short` | `729.50` | 275,590.00 USD | 170,730.00 USD | 0.00 USD | `+3.15%` | `234,042,000,000.00` |
| `Live` | `Short` | `730.50` | 304,210.00 USD | 28,620.00 USD | 0.00 USD | `+3.29%` | `39,182,000,000.00` |
| `Live` | `Short` | `731.50` | 306,410.00 USD | 2,200.00 USD | 0.00 USD | `+3.43%` | `3,007,000,000.00` |
| `Live` | `Short` | `732.50` | 443,370.00 USD | 136,960.00 USD | 0.00 USD | `+3.57%` | `186,979,000,000.00` |
| `Live` | `Short` | `733.50` | 458,980.00 USD | 15,610.00 USD | 0.00 USD | `+3.71%` | `21,280,000,000.00` |
| `Live` | `Short` | `734.50` | 611,660.00 USD | 152,680.00 USD | 0.00 USD | `+3.86%` | `207,869,000,000.00` |
| `Live` | `Short` | `735.50` | 634,260.00 USD | 22,600.00 USD | 0.00 USD | `+4.00%` | `30,729,000,000.00` |
| `Live` | `Short` | `736.50` | 642,930.00 USD | 8,670.00 USD | 0.00 USD | `+4.14%` | `11,775,000,000.00` |
| `Live` | `Short` | `737.50` | 651,720.00 USD | 8,780.00 USD | 0.00 USD | `+4.28%` | `11,906,000,000.00` |
| `Live` | `Short` | `738.50` | 660,000.00 USD | 8,290.00 USD | 0.00 USD | `+4.42%` | `11,222,000,000.00` |
| `Live` | `Short` | `739.50` | 734,970.00 USD | 74,970.00 USD | 0.00 USD | `+4.56%` | `101,377,000,000.00` |
| `Live` | `Short` | `740.50` | 738,950.00 USD | 3,980.00 USD | 0.00 USD | `+4.70%` | `5,376,000,000.00` |
| `Live` | `Short` | `741.50` | 748,460.00 USD | 9,510.00 USD | 0.00 USD | `+4.85%` | `12,824,000,000.00` |
| `Live` | `Short` | `742.50` | 815,760.00 USD | 67,300.00 USD | 0.00 USD | `+4.99%` | `90,634,000,000.00` |
| `Live` | `Short` | `743.50` | 862,980.00 USD | 47,230.00 USD | 0.00 USD | `+5.13%` | `63,520,000,000.00` |
| `Live` | `Short` | `744.50` | 980,680.00 USD | 117,700.00 USD | 0.00 USD | `+5.27%` | `158,091,000,000.00` |
| `Live` | `Short` | `745.50` | 1,010,000.00 USD | 30,410.00 USD | 0.00 USD | `+5.41%` | `40,794,000,000.00` |
| `Live` | `Short` | `746.50` | 1,200,000.00 USD | 187,000.00 USD | 0.00 USD | `+5.55%` | `250,506,000,000.00` |
| `Live` | `Short` | `748.50` | 1,220,000.00 USD | 23,390.00 USD | 0.00 USD | `+5.84%` | `31,248,000,000.00` |
| `Live` | `Short` | `749.50` | 1,290,000.00 USD | 69,770.00 USD | 0.00 USD | `+5.98%` | `93,085,000,000.00` |
| `Live` | `Short` | `750.50` | 1,870,000.00 USD | 575,140.00 USD | 0.00 USD | `+6.12%` | `766,346,000,000.00` |
| `Live` | `Short` | `751.50` | 1,880,000.00 USD | 11,400.00 USD | 0.00 USD | `+6.26%` | `15,176,000,000.00` |
| `Live` | `Short` | `752.50` | 1,940,000.00 USD | 57,900.00 USD | 0.00 USD | `+6.40%` | `76,944,000,000.00` |
| `Live` | `Short` | `754.50` | 2,800,000.00 USD | 863,450.00 USD | 0.00 USD | `+6.68%` | `1,144,401,000,000.00` |
| `Live` | `Short` | `756.50` | 2,800,000.00 USD | 3,750.00 USD | 0.00 USD | `+6.97%` | `4,960,000,000.00` |
| `Live` | `Short` | `757.50` | 2,800,000.00 USD | 2,010.00 USD | 0.00 USD | `+7.11%` | `2,652,000,000.00` |
| `Live` | `Short` | `758.50` | 2,990,000.00 USD | 180,270.00 USD | 0.00 USD | `+7.25%` | `237,673,000,000.00` |
| `Live` | `Short` | `759.50` | 2,990,000.00 USD | 3,830.00 USD | 0.00 USD | `+7.39%` | `5,039,000,000.00` |
| `Live` | `Short` | `760.50` | 3,360,000.00 USD | 367,770.00 USD | 0.00 USD | `+7.53%` | `483,591,000,000.00` |
| `Live` | `Short` | `761.50` | 3,360,000.00 USD | 2,360.00 USD | 0.00 USD | `+7.67%` | `3,099,000,000.00` |
| `Live` | `Short` | `762.50` | 3,360,000.00 USD | 367.52 USD | 0.00 USD | `+7.81%` | `482,000,000.00` |
| `Live` | `Short` | `763.50` | 3,960,000.00 USD | 603,420.00 USD | 0.00 USD | `+7.96%` | `790,332,000,000.00` |
| `Live` | `Short` | `764.50` | 4,040,000.00 USD | 76,450.00 USD | 0.00 USD | `+8.10%` | `100,000,000,000.00` |
| `Live` | `Short` | `766.50` | 4,040,000.00 USD | 2,850.00 USD | 0.00 USD | `+8.38%` | `3,719,000,000.00` |
| `Live` | `Short` | `768.50` | 4,040,000.00 USD | 156.77 USD | 0.00 USD | `+8.66%` | `204,000,000.00` |
| `Live` | `Short` | `770.50` | 4,040,000.00 USD | 881.45 USD | 0.00 USD | `+8.95%` | `1,144,000,000.00` |
| `Live` | `Short` | `771.50` | 4,050,000.00 USD | 9,260.00 USD | 0.00 USD | `+9.09%` | `12,000,000,000.00` |
| `Live` | `Short` | `772.50` | 4,050,000.00 USD | 2,450.00 USD | 0.00 USD | `+9.23%` | `3,173,000,000.00` |
| `Live` | `Short` | `773.50` | 4,060,000.00 USD | 4,670.00 USD | 0.00 USD | `+9.37%` | `6,032,000,000.00` |
| `Live` | `Short` | `775.50` | 4,060,000.00 USD | 544.40 USD | 0.00 USD | `+9.65%` | `702,000,000.00` |
| `Live` | `Short` | `776.50` | 4,150,000.00 USD | 89,520.00 USD | 0.00 USD | `+9.79%` | `115,281,000,000.00` |
| `Live` | `Short` | `777.50` | 4,150,000.00 USD | 209.15 USD | 0.00 USD | `+9.94%` | `269,000,000.00` |
| `Live` | `Short` | `778.50` | 4,160,000.00 USD | 8,100.00 USD | 0.00 USD | `+10.08%` | `10,401,000,000.00` |
| `Live` | `Short` | `780.50` | 4,160,000.00 USD | 4,150.00 USD | 0.00 USD | `+10.36%` | `5,318,000,000.00` |
| `Live` | `Short` | `781.50` | 4,160,000.00 USD | 1,830.00 USD | 0.00 USD | `+10.50%` | `2,337,000,000.00` |
| `Live` | `Short` | `784.50` | 4,160,000.00 USD | 121.60 USD | 0.00 USD | `+10.93%` | `155,000,000.00` |
| `Live` | `Short` | `785.50` | 4,160,000.00 USD | 457.95 USD | 0.00 USD | `+11.07%` | `583,000,000.00` |
| `Live` | `Short` | `786.50` | 4,170,000.00 USD | 4,780.00 USD | 0.00 USD | `+11.21%` | `6,080,000,000.00` |
| `Live` | `Short` | `787.50` | 4,480,000.00 USD | 315,000.00 USD | 0.00 USD | `+11.35%` | `400,000,000,000.00` |
| `Live` | `Short` | `788.50` | 4,490,000.00 USD | 1,580.00 USD | 0.00 USD | `+11.49%` | `2,000,000,000.00` |
| `Live` | `Short` | `789.50` | 4,490,000.00 USD | 1,540.00 USD | 0.00 USD | `+11.63%` | `1,947,000,000.00` |
| `Live` | `Short` | `790.50` | 4,490,000.00 USD | 632.40 USD | 0.00 USD | `+11.77%` | `800,000,000.00` |
| `Live` | `Short` | `793.50` | 4,490,000.00 USD | 1,280.00 USD | 0.00 USD | `+12.20%` | `1,616,000,000.00` |
| `Live` | `Short` | `794.50` | 4,490,000.00 USD | 3,640.00 USD | 0.00 USD | `+12.34%` | `4,580,000,000.00` |
| `Live` | `Short` | `795.50` | 4,490,000.00 USD | 518.67 USD | 0.00 USD | `+12.48%` | `652,000,000.00` |
| `Live` | `Short` | `796.50` | 4,490,000.00 USD | 567.11 USD | 0.00 USD | `+12.62%` | `712,000,000.00` |
| `Live` | `Short` | `797.50` | 4,500,000.00 USD | 1,760.00 USD | 0.00 USD | `+12.76%` | `2,208,000,000.00` |
| `Live` | `Short` | `799.50` | 4,500,000.00 USD | 610.02 USD | 0.00 USD | `+13.05%` | `763,000,000.00` |
| `Live` | `Short` | `800.50` | 4,500,000.00 USD | 776.49 USD | 0.00 USD | `+13.19%` | `970,000,000.00` |
| `Live` | `Short` | `801.50` | 4,500,000.00 USD | 3,410.00 USD | 0.00 USD | `+13.33%` | `4,250,000,000.00` |
| `Live` | `Short` | `802.50` | 5,280,000.00 USD | 778,380.00 USD | 0.00 USD | `+13.47%` | `969,946,000,000.00` |
| `Live` | `Short` | `803.50` | 5,280,000.00 USD | 2,700.00 USD | 0.00 USD | `+13.61%` | `3,365,000,000.00` |
| `Live` | `Short` | `804.50` | 5,280,000.00 USD | 105.39 USD | 0.00 USD | `+13.75%` | `131,000,000.00` |
| `Live` | `Short` | `805.50` | 5,300,000.00 USD | 15,370.00 USD | 0.00 USD | `+13.90%` | `19,085,000,000.00` |
| `Live` | `Short` | `806.50` | 5,300,000.00 USD | 2,890.00 USD | 0.00 USD | `+14.04%` | `3,580,000,000.00` |
| `Live` | `Short` | `807.50` | 5,330,000.00 USD | 28,850.00 USD | 0.00 USD | `+14.18%` | `35,727,000,000.00` |
| `Live` | `Short` | `808.50` | 5,340,000.00 USD | 11,780.00 USD | 0.00 USD | `+14.32%` | `14,574,000,000.00` |
| `Live` | `Short` | `809.50` | 5,340,000.00 USD | 173.23 USD | 0.00 USD | `+14.46%` | `214,000,000.00` |
| `Live` | `Short` | `812.50` | 5,340,000.00 USD | 434.69 USD | 0.00 USD | `+14.88%` | `535,000,000.00` |
| `Live` | `Short` | `814.50` | 5,340,000.00 USD | 692.32 USD | 0.00 USD | `+15.17%` | `850,000,000.00` |
| `Live` | `Short` | `815.50` | 5,350,000.00 USD | 8,150.00 USD | 0.00 USD | `+15.31%` | `9,992,000,000.00` |
| `Live` | `Short` | `816.50` | 5,370,000.00 USD | 15,410.00 USD | 0.00 USD | `+15.45%` | `18,879,000,000.00` |
| `Live` | `Short` | `817.50` | 5,370,000.00 USD | 325.37 USD | 0.00 USD | `+15.59%` | `398,000,000.00` |
| `Live` | `Short` | `818.50` | 5,370,000.00 USD | 7,720.00 USD | 0.00 USD | `+15.73%` | `9,432,000,000.00` |
| `Live` | `Short` | `821.50` | 5,400,000.00 USD | 27,280.00 USD | 0.00 USD | `+16.16%` | `33,213,000,000.00` |
| `Live` | `Short` | `822.50` | 5,410,000.00 USD | 10,870.00 USD | 0.00 USD | `+16.30%` | `13,210,000,000.00` |
| `Live` | `Short` | `826.50` | 6,030,000.00 USD | 618,360.00 USD | 0.00 USD | `+16.86%` | `748,168,000,000.00` |
| `Live` | `Short` | `828.50` | 6,030,000.00 USD | 2,230.00 USD | 0.00 USD | `+17.15%` | `2,689,000,000.00` |
| `Live` | `Short` | `833.50` | 6,040,000.00 USD | 2,920.00 USD | 0.00 USD | `+17.85%` | `3,500,000,000.00` |
| `Live` | `Short` | `834.50` | 6,040,000.00 USD | 1,010.00 USD | 0.00 USD | `+18.00%` | `1,206,000,000.00` |
| `Live` | `Short` | `837.50` | 6,040,000.00 USD | 3,570.00 USD | 0.00 USD | `+18.42%` | `4,257,000,000.00` |
| `Live` | `Short` | `838.50` | 6,060,000.00 USD | 21,840.00 USD | 0.00 USD | `+18.56%` | `26,046,000,000.00` |
| `Live` | `Short` | `840.50` | 6,060,000.00 USD | 1,150.00 USD | 0.00 USD | `+18.84%` | `1,371,000,000.00` |
| `Live` | `Short` | `841.50` | 6,070,000.00 USD | 2,830.00 USD | 0.00 USD | `+18.99%` | `3,364,000,000.00` |
| `Live` | `Short` | `842.50` | 6,100,000.00 USD | 35,770.00 USD | 0.00 USD | `+19.13%` | `42,452,000,000.00` |
| `Live` | `Short` | `845.50` | 6,110,000.00 USD | 10,760.00 USD | 0.00 USD | `+19.55%` | `12,723,000,000.00` |
| `Live` | `Short` | `848.50` | 6,110,000.00 USD | 289.34 USD | 0.00 USD | `+19.98%` | `341,000,000.00` |
| `Live` | `Short` | `850.50` | 6,110,000.00 USD | 108.86 USD | 0.00 USD | `+20.26%` | `128,000,000.00` |
| `Live` | `Short` | `851.50` | 6,110,000.00 USD | 285.25 USD | 0.00 USD | `+20.40%` | `335,000,000.00` |
| `Live` | `Short` | `855.50` | 6,120,000.00 USD | 7,140.00 USD | 0.00 USD | `+20.96%` | `8,346,000,000.00` |
| `Live` | `Short` | `856.50` | 6,150,000.00 USD | 29,740.00 USD | 0.00 USD | `+21.11%` | `34,722,000,000.00` |
| `Live` | `Short` | `857.50` | 6,220,000.00 USD | 68,600.00 USD | 0.00 USD | `+21.25%` | `80,000,000,000.00` |
| `Live` | `Short` | `858.50` | 6,740,000.00 USD | 523,680.00 USD | 0.00 USD | `+21.39%` | `610,000,000,000.00` |
| `Live` | `Short` | `859.50` | 6,760,000.00 USD | 16,380.00 USD | 0.00 USD | `+21.53%` | `19,059,000,000.00` |
| `Live` | `Short` | `865.50` | 6,780,000.00 USD | 18,900.00 USD | 0.00 USD | `+22.38%` | `21,832,000,000.00` |
| `Live` | `Short` | `868.50` | 7,070,000.00 USD | 290,990.00 USD | 0.00 USD | `+22.80%` | `335,051,000,000.00` |
| `Live` | `Short` | `871.50` | 7,070,000.00 USD | 499.37 USD | 0.00 USD | `+23.23%` | `573,000,000.00` |
| `Live` | `Short` | `873.50` | 7,070,000.00 USD | 326.69 USD | 0.00 USD | `+23.51%` | `374,000,000.00` |
| `Live` | `Short` | `877.50` | 7,680,000.00 USD | 614,250.00 USD | 0.00 USD | `+24.08%` | `700,000,000,000.00` |
| `Live` | `Short` | `878.50` | 7,780,000.00 USD | 92,600.00 USD | 0.00 USD | `+24.22%` | `105,403,000,000.00` |
| `Live` | `Short` | `879.50` | 7,790,000.00 USD | 14,060.00 USD | 0.00 USD | `+24.36%` | `15,992,000,000.00` |
| `Live` | `Short` | `880.50` | 7,790,000.00 USD | 663.02 USD | 0.00 USD | `+24.50%` | `753,000,000.00` |
| `Live` | `Short` | `881.50` | 7,810,000.00 USD | 22,280.00 USD | 0.00 USD | `+24.64%` | `25,275,000,000.00` |
| `Live` | `Short` | `885.50` | 7,810,000.00 USD | 1,770.00 USD | 0.00 USD | `+25.21%` | `2,000,000,000.00` |
| `Live` | `Short` | `886.50` | 7,820,000.00 USD | 812.92 USD | 0.00 USD | `+25.35%` | `917,000,000.00` |
| `Live` | `Short` | `887.50` | 7,820,000.00 USD | 385.18 USD | 0.00 USD | `+25.49%` | `434,000,000.00` |
| `Live` | `Short` | `888.50` | 7,900,000.00 USD | 88,850.00 USD | 0.00 USD | `+25.63%` | `100,000,000,000.00` |
| `Live` | `Short` | `891.50` | 7,910,000.00 USD | 4,330.00 USD | 0.00 USD | `+26.06%` | `4,856,000,000.00` |
| `Live` | `Short` | `893.50` | 7,910,000.00 USD | 173.34 USD | 0.00 USD | `+26.34%` | `194,000,000.00` |
| `Live` | `Short` | `894.50` | 7,940,000.00 USD | 26,840.00 USD | 0.00 USD | `+26.48%` | `30,000,000,000.00` |
| `Live` | `Short` | `895.50` | 8,160,000.00 USD | 223,880.00 USD | 0.00 USD | `+26.62%` | `250,000,000,000.00` |
| `Live` | `Short` | `896.50` | 8,240,000.00 USD | 79,560.00 USD | 0.00 USD | `+26.76%` | `88,749,000,000.00` |
| `Live` | `Short` | `898.50` | 8,240,000.00 USD | 127.59 USD | 0.00 USD | `+27.04%` | `142,000,000.00` |
| `Live` | `Short` | `899.50` | 8,250,000.00 USD | 5,400.00 USD | 0.00 USD | `+27.19%` | `6,000,000,000.00` |
| `Live` | `Short` | `901.50` | 8,300,000.00 USD | 50,030.00 USD | 0.00 USD | `+27.47%` | `55,495,000,000.00` |
| `Live` | `Short` | `902.50` | 8,300,000.00 USD | 305.05 USD | 0.00 USD | `+27.61%` | `338,000,000.00` |
| `Live` | `Short` | `903.50` | 8,300,000.00 USD | 9,270.00 USD | 0.00 USD | `+27.75%` | `10,264,000,000.00` |
| `Live` | `Short` | `904.50` | 8,370,000.00 USD | 63,930.00 USD | 0.00 USD | `+27.89%` | `70,678,000,000.00` |
| `Live` | `Short` | `906.50` | 8,410,000.00 USD | 37,400.00 USD | 0.00 USD | `+28.18%` | `41,255,000,000.00` |
| `Live` | `Short` | `907.50` | 8,410,000.00 USD | 6,470.00 USD | 0.00 USD | `+28.32%` | `7,130,000,000.00` |
| `Live` | `Short` | `908.50` | 8,420,000.00 USD | 9,280.00 USD | 0.00 USD | `+28.46%` | `10,215,000,000.00` |
| `Live` | `Short` | `909.50` | 8,420,000.00 USD | 634.83 USD | 0.00 USD | `+28.60%` | `698,000,000.00` |
| `Live` | `Short` | `910.50` | 8,440,000.00 USD | 16,510.00 USD | 0.00 USD | `+28.74%` | `18,131,000,000.00` |
| `Live` | `Short` | `911.50` | 8,470,000.00 USD | 35,180.00 USD | 0.00 USD | `+28.88%` | `38,595,000,000.00` |
| `Live` | `Short` | `913.50` | 8,470,000.00 USD | 116.93 USD | 0.00 USD | `+29.17%` | `128,000,000.00` |
| `Live` | `Short` | `914.50` | 8,500,000.00 USD | 30,060.00 USD | 0.00 USD | `+29.31%` | `32,872,000,000.00` |
| `Live` | `Short` | `918.50` | 8,640,000.00 USD | 133,350.00 USD | 0.00 USD | `+29.87%` | `145,183,000,000.00` |
| `Live` | `Short` | `925.50` | 8,650,000.00 USD | 9,260.00 USD | 0.00 USD | `+30.86%` | `10,000,000,000.00` |
| `Live` | `Short` | `928.50` | 8,650,000.00 USD | 651.81 USD | 0.00 USD | `+31.29%` | `702,000,000.00` |
| `Live` | `Short` | `933.50` | 8,650,000.00 USD | 954.04 USD | 0.00 USD | `+31.99%` | `1,022,000,000.00` |
| `Live` | `Short` | `934.50` | 8,710,000.00 USD | 65,420.00 USD | 0.00 USD | `+32.14%` | `70,000,000,000.00` |
| `Live` | `Short` | `939.50` | 8,720,000.00 USD | 3,140.00 USD | 0.00 USD | `+32.84%` | `3,344,000,000.00` |
| `Live` | `Short` | `940.50` | 8,720,000.00 USD | 2,680.00 USD | 0.00 USD | `+32.98%` | `2,846,000,000.00` |
| `Live` | `Short` | `952.50` | 8,720,000.00 USD | 202.88 USD | 0.00 USD | `+34.68%` | `213,000,000.00` |
| `Live` | `Short` | `955.50` | 8,740,000.00 USD | 19,020.00 USD | 0.00 USD | `+35.10%` | `19,907,000,000.00` |
| `Live` | `Short` | `964.50` | 8,750,000.00 USD | 6,940.00 USD | 0.00 USD | `+36.38%` | `7,199,000,000.00` |
| `Live` | `Short` | `965.50` | 8,750,000.00 USD | 1,360.00 USD | 0.00 USD | `+36.52%` | `1,413,000,000.00` |
| `Live` | `Short` | `969.50` | 8,750,000.00 USD | 5,780.00 USD | 0.00 USD | `+37.08%` | `5,960,000,000.00` |
| `Live` | `Short` | `970.50` | 8,760,000.00 USD | 1,940.00 USD | 0.00 USD | `+37.23%` | `2,000,000,000.00` |
| `Live` | `Short` | `977.50` | 8,820,000.00 USD | 60,020.00 USD | 0.00 USD | `+38.22%` | `61,406,000,000.00` |
| `Live` | `Short` | `981.50` | 8,830,000.00 USD | 14,480.00 USD | 0.00 USD | `+38.78%` | `14,758,000,000.00` |
| `Live` | `Short` | `983.50` | 8,840,000.00 USD | 14,300.00 USD | 0.00 USD | `+39.06%` | `14,541,000,000.00` |
| `Live` | `Short` | `985.50` | 8,850,000.00 USD | 2,560.00 USD | 0.00 USD | `+39.35%` | `2,594,000,000.00` |
| `Live` | `Short` | `990.50` | 8,870,000.00 USD | 28,300.00 USD | 0.00 USD | `+40.05%` | `28,570,000,000.00` |
| `Live` | `Short` | `992.50` | 8,880,000.00 USD | 2,140.00 USD | 0.00 USD | `+40.34%` | `2,154,000,000.00` |
| `Live` | `Short` | `993.50` | 8,880,000.00 USD | 975.62 USD | 0.00 USD | `+40.48%` | `982,000,000.00` |
| `Live` | `Short` | `994.50` | 9,160,000.00 USD | 285,750.00 USD | 0.00 USD | `+40.62%` | `287,331,000,000.00` |
| `Live` | `Short` | `995.50` | 9,160,000.00 USD | 313.58 USD | 0.00 USD | `+40.76%` | `315,000,000.00` |
| `Live` | `Short` | `996.50` | 9,190,000.00 USD | 22,470.00 USD | 0.00 USD | `+40.90%` | `22,545,000,000.00` |
| `Live` | `Short` | `997.50` | 9,820,000.00 USD | 632,460.00 USD | 0.00 USD | `+41.04%` | `634,044,000,000.00` |
| `Live` | `Short` | `998.50` | 9,830,000.00 USD | 9,550.00 USD | 0.00 USD | `+41.18%` | `9,569,000,000.00` |
| `Live` | `Short` | `999.50` | 9,870,000.00 USD | 36,850.00 USD | 0.00 USD | `+41.33%` | `36,870,000,000.00` |
| `Live` | `Short` | `1003.50` | 9,870,000.00 USD | 838.93 USD | 0.00 USD | `+41.89%` | `836,000,000.00` |
| `Live` | `Short` | `1005.50` | 10,160,000.00 USD | 297,210.00 USD | 0.00 USD | `+42.17%` | `295,587,000,000.00` |
| `Live` | `Short` | `1008.50` | 10,190,000.00 USD | 29,110.00 USD | 0.00 USD | `+42.60%` | `28,860,000,000.00` |
| `Live` | `Short` | `1009.50` | 10,240,000.00 USD | 51,370.00 USD | 0.00 USD | `+42.74%` | `50,889,000,000.00` |
| `Live` | `Short` | `1011.50` | 10,240,000.00 USD | 302.44 USD | 0.00 USD | `+43.02%` | `299,000,000.00` |
| `Live` | `Short` | `1014.50` | 11,010,000.00 USD | 761,510.00 USD | 0.00 USD | `+43.45%` | `750,621,000,000.00` |
| `Live` | `Short` | `1024.50` | 11,010,000.00 USD | 2,850.00 USD | 0.00 USD | `+44.86%` | `2,777,000,000.00` |
| `Live` | `Short` | `1026.50` | 11,010,000.00 USD | 494.77 USD | 0.00 USD | `+45.14%` | `482,000,000.00` |
| `Live` | `Short` | `1032.50` | 11,730,000.00 USD | 720,280.00 USD | 0.00 USD | `+45.99%` | `697,611,000,000.00` |
| `Live` | `Short` | `1048.50` | 11,790,000.00 USD | 65,530.00 USD | 0.00 USD | `+48.25%` | `62,500,000,000.00` |
| `Live` | `Short` | `1050.50` | 11,800,000.00 USD | 500.04 USD | 0.00 USD | `+48.54%` | `476,000,000.00` |
| `Live` | `Short` | `1058.50` | 11,810,000.00 USD | 15,250.00 USD | 0.00 USD | `+49.67%` | `14,403,000,000.00` |
| `Live` | `Short` | `1060.50` | 11,810,000.00 USD | 909.91 USD | 0.00 USD | `+49.95%` | `858,000,000.00` |
| `Live` | `Short` | `1062.50` | 11,810,000.00 USD | 635.38 USD | 0.00 USD | `+50.23%` | `598,000,000.00` |
| `Live` | `Short` | `1064.50` | 11,810,000.00 USD | 1,760.00 USD | 0.00 USD | `+50.52%` | `1,657,000,000.00` |
| `Live` | `Short` | `1066.50` | 11,820,000.00 USD | 7,810.00 USD | 0.00 USD | `+50.80%` | `7,321,000,000.00` |
| `Live` | `Short` | `1072.50` | 11,820,000.00 USD | 120.12 USD | 0.00 USD | `+51.65%` | `112,000,000.00` |
| `Live` | `Short` | `1073.50` | 11,820,000.00 USD | 1,610.00 USD | 0.00 USD | `+51.79%` | `1,500,000,000.00` |
| `Live` | `Short` | `1083.50` | 11,890,000.00 USD | 69,250.00 USD | 0.00 USD | `+53.20%` | `63,916,000,000.00` |
| `Live` | `Short` | `1087.50` | 11,900,000.00 USD | 5,770.00 USD | 0.00 USD | `+53.77%` | `5,310,000,000.00` |
| `Live` | `Short` | `1088.50` | 11,910,000.00 USD | 15,780.00 USD | 0.00 USD | `+53.91%` | `14,495,000,000.00` |
| `Live` | `Short` | `1093.50` | 12,030,000.00 USD | 120,790.00 USD | 0.00 USD | `+54.62%` | `110,460,000,000.00` |
| `Live` | `Short` | `1096.50` | 12,040,000.00 USD | 810.31 USD | 0.00 USD | `+55.04%` | `739,000,000.00` |
| `Live` | `Short` | `1109.50` | 12,110,000.00 USD | 75,720.00 USD | 0.00 USD | `+56.88%` | `68,249,000,000.00` |
| `Live` | `Short` | `1116.50` | 12,170,000.00 USD | 60,360.00 USD | 0.00 USD | `+57.87%` | `54,065,000,000.00` |
| `Live` | `Short` | `1119.50` | 12,310,000.00 USD | 136,380.00 USD | 0.00 USD | `+58.29%` | `121,826,000,000.00` |
| `Live` | `Short` | `1125.50` | 12,310,000.00 USD | 150.82 USD | 0.00 USD | `+59.14%` | `134,000,000.00` |
| `Live` | `Short` | `1134.50` | 12,310,000.00 USD | 1,520.00 USD | 0.00 USD | `+60.41%` | `1,337,000,000.00` |
| `Live` | `Short` | `1137.50` | 12,650,000.00 USD | 341,250.00 USD | 0.00 USD | `+60.84%` | `300,000,000,000.00` |
| `Live` | `Short` | `1143.50` | 12,670,000.00 USD | 23,170.00 USD | 0.00 USD | `+61.69%` | `20,265,000,000.00` |
| `Live` | `Short` | `1145.50` | 12,670,000.00 USD | 359.69 USD | 0.00 USD | `+61.97%` | `314,000,000.00` |
| `Live` | `Short` | `1146.50` | 12,670,000.00 USD | 119.24 USD | 0.00 USD | `+62.11%` | `104,000,000.00` |
| `Live` | `Short` | `1154.50` | 12,690,000.00 USD | 11,720.00 USD | 0.00 USD | `+63.24%` | `10,154,000,000.00` |
| `Live` | `Short` | `1155.50` | 12,690,000.00 USD | 154.84 USD | 0.00 USD | `+63.38%` | `134,000,000.00` |
| `Live` | `Short` | `1166.50` | 12,690,000.00 USD | 249.63 USD | 0.00 USD | `+64.94%` | `214,000,000.00` |
| `Live` | `Short` | `1172.50` | 12,690,000.00 USD | 1,690.00 USD | 0.00 USD | `+65.79%` | `1,445,000,000.00` |
| `Live` | `Short` | `1178.50` | 12,750,000.00 USD | 66,060.00 USD | 0.00 USD | `+66.64%` | `56,055,000,000.00` |
| `Live` | `Short` | `1183.50` | 12,750,000.00 USD | 166.87 USD | 0.00 USD | `+67.34%` | `141,000,000.00` |
| `Live` | `Short` | `1191.50` | 12,810,000.00 USD | 57,560.00 USD | 0.00 USD | `+68.47%` | `48,311,000,000.00` |
| `Live` | `Short` | `1197.50` | 12,810,000.00 USD | 463.43 USD | 0.00 USD | `+69.32%` | `387,000,000.00` |
| `Live` | `Short` | `1203.50` | 12,930,000.00 USD | 118,860.00 USD | 0.00 USD | `+70.17%` | `98,764,000,000.00` |
| `Live` | `Short` | `1207.50` | 12,930,000.00 USD | 385.19 USD | 0.00 USD | `+70.74%` | `319,000,000.00` |
| `Live` | `Short` | `1213.50` | 12,970,000.00 USD | 42,470.00 USD | 0.00 USD | `+71.58%` | `35,000,000,000.00` |
| `Live` | `Short` | `1215.50` | 13,000,000.00 USD | 30,370.00 USD | 0.00 USD | `+71.87%` | `24,982,000,000.00` |
| `Live` | `Short` | `1222.50` | 13,030,000.00 USD | 21,230.00 USD | 0.00 USD | `+72.86%` | `17,363,000,000.00` |
| `Live` | `Short` | `1224.50` | 13,030,000.00 USD | 1,030.00 USD | 0.00 USD | `+73.14%` | `841,000,000.00` |
| `Live` | `Short` | `1226.50` | 13,030,000.00 USD | 3,720.00 USD | 0.00 USD | `+73.42%` | `3,035,000,000.00` |
| `Live` | `Short` | `1238.50` | 14,780,000.00 USD | 1,750,000.00 USD | 0.00 USD | `+75.12%` | `1,412,868,000,000.00` |
| `Live` | `Short` | `1246.50` | 14,780,000.00 USD | 199.44 USD | 0.00 USD | `+76.25%` | `160,000,000.00` |
| `Live` | `Short` | `1249.50` | 14,790,000.00 USD | 4,720.00 USD | 0.00 USD | `+76.68%` | `3,778,000,000.00` |
| `Live` | `Short` | `1251.50` | 14,790,000.00 USD | 100.12 USD | 0.00 USD | `+76.96%` | `80,000,000.00` |
| `Live` | `Short` | `1254.50` | 14,790,000.00 USD | 6,630.00 USD | 0.00 USD | `+77.38%` | `5,284,000,000.00` |
| `Live` | `Short` | `1259.50` | 14,800,000.00 USD | 5,030.00 USD | 0.00 USD | `+78.09%` | `3,994,000,000.00` |
| `Live` | `Short` | `1263.50` | 14,910,000.00 USD | 113,720.00 USD | 0.00 USD | `+78.65%` | `90,000,000,000.00` |
| `Live` | `Short` | `1268.50` | 14,920,000.00 USD | 6,870.00 USD | 0.00 USD | `+79.36%` | `5,419,000,000.00` |
| `Live` | `Short` | `1272.50` | 14,940,000.00 USD | 24,700.00 USD | 0.00 USD | `+79.93%` | `19,414,000,000.00` |
| `Live` | `Short` | `1282.50` | 15,000,000.00 USD | 61,720.00 USD | 0.00 USD | `+81.34%` | `48,123,000,000.00` |
| `Live` | `Short` | `1284.50` | 15,000,000.00 USD | 348.10 USD | 0.00 USD | `+81.62%` | `271,000,000.00` |
| `Live` | `Short` | `1288.50` | 15,110,000.00 USD | 109,920.00 USD | 0.00 USD | `+82.19%` | `85,305,000,000.00` |
| `Live` | `Short` | `1292.50` | 15,130,000.00 USD | 19,310.00 USD | 0.00 USD | `+82.76%` | `14,939,000,000.00` |
| `Live` | `Short` | `1295.50` | 15,130,000.00 USD | 181.37 USD | 0.00 USD | `+83.18%` | `140,000,000.00` |
| `Live` | `Short` | `1299.50` | 15,140,000.00 USD | 4,020.00 USD | 0.00 USD | `+83.75%` | `3,092,000,000.00` |
| `Live` | `Short` | `1307.50` | 15,300,000.00 USD | 165,900.00 USD | 0.00 USD | `+84.88%` | `126,881,000,000.00` |
| `Live` | `Short` | `1309.50` | 15,300,000.00 USD | 206.90 USD | 0.00 USD | `+85.16%` | `158,000,000.00` |
| `Live` | `Short` | `1312.50` | 15,300,000.00 USD | 227.06 USD | 0.00 USD | `+85.58%` | `173,000,000.00` |
| `Live` | `Short` | `1313.50` | 15,310,000.00 USD | 1,850.00 USD | 0.00 USD | `+85.72%` | `1,409,000,000.00` |
| `Live` | `Short` | `1315.50` | 15,400,000.00 USD | 92,080.00 USD | 0.00 USD | `+86.01%` | `70,000,000,000.00` |
| `Live` | `Short` | `1317.50` | 15,410,000.00 USD | 7,590.00 USD | 0.00 USD | `+86.29%` | `5,758,000,000.00` |
| `Live` | `Short` | `1319.50` | 15,420,000.00 USD | 14,130.00 USD | 0.00 USD | `+86.57%` | `10,710,000,000.00` |
| `Live` | `Short` | `1321.50` | 15,420,000.00 USD | 2,640.00 USD | 0.00 USD | `+86.86%` | `2,000,000,000.00` |
| `Live` | `Short` | `1324.50` | 15,570,000.00 USD | 151,090.00 USD | 0.00 USD | `+87.28%` | `114,070,000,000.00` |
| `Live` | `Short` | `1327.50` | 15,570,000.00 USD | 138.06 USD | 0.00 USD | `+87.70%` | `104,000,000.00` |
| `Live` | `Short` | `1328.50` | 15,570,000.00 USD | 289.61 USD | 0.00 USD | `+87.85%` | `218,000,000.00` |
| `Live` | `Short` | `1330.50` | 15,600,000.00 USD | 23,470.00 USD | 0.00 USD | `+88.13%` | `17,640,000,000.00` |
| `Live` | `Short` | `1341.50` | 15,630,000.00 USD | 30,850.00 USD | 0.00 USD | `+89.68%` | `23,000,000,000.00` |
| `Live` | `Short` | `1344.50` | 15,670,000.00 USD | 40,620.00 USD | 0.00 USD | `+90.11%` | `30,209,000,000.00` |
| `Live` | `Short` | `1359.50` | 15,670,000.00 USD | 121.00 USD | 0.00 USD | `+92.23%` | `89,000,000.00` |
| `Live` | `Short` | `1367.50` | 15,670,000.00 USD | 761.70 USD | 0.00 USD | `+93.36%` | `557,000,000.00` |
| `Live` | `Short` | `1368.50` | 15,670,000.00 USD | 4,110.00 USD | 0.00 USD | `+93.50%` | `3,000,000,000.00` |
| `Live` | `Short` | `1369.50` | 15,720,000.00 USD | 46,880.00 USD | 0.00 USD | `+93.64%` | `34,232,000,000.00` |
| `Live` | `Short` | `1380.50` | 15,780,000.00 USD | 60,040.00 USD | 0.00 USD | `+95.20%` | `43,490,000,000.00` |
| `Live` | `Short` | `1386.50` | 15,780,000.00 USD | 2,520.00 USD | 0.00 USD | `+96.05%` | `1,818,000,000.00` |
| `Live` | `Short` | `1390.50` | 15,780,000.00 USD | 510.31 USD | 0.00 USD | `+96.61%` | `367,000,000.00` |
| `Live` | `Short` | `1392.50` | 15,850,000.00 USD | 69,620.00 USD | 0.00 USD | `+96.89%` | `50,000,000,000.00` |
| `Live` | `Short` | `1398.50` | 15,860,000.00 USD | 4,830.00 USD | 0.00 USD | `+97.74%` | `3,457,000,000.00` |
| `Live` | `Short` | `1401.50` | 16,110,000.00 USD | 252,270.00 USD | 0.00 USD | `+98.17%` | `180,000,000,000.00` |
| `Live` | `Short` | `1405.50` | 16,120,000.00 USD | 4,770.00 USD | 0.00 USD | `+98.73%` | `3,392,000,000.00` |
| `Live` | `Short` | `1407.50` | 16,120,000.00 USD | 4,010.00 USD | 0.00 USD | `+99.02%` | `2,846,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `150.50` | 2,990,000.00 USD | 0.00 USD | 475.73 USD | `-78.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `300.50` | 2,990,000.00 USD | 0.00 USD | 2,400.00 USD | `-57.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `333.50` | 2,990,000.00 USD | 0.00 USD | 333.50 USD | `-52.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `360.50` | 2,990,000.00 USD | 0.00 USD | 8,140.00 USD | `-49.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `369.50` | 2,980,000.00 USD | 0.00 USD | 5,170.00 USD | `-47.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `400.50` | 2,970,000.00 USD | 0.00 USD | 17,290.00 USD | `-43.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `410.50` | 2,960,000.00 USD | 0.00 USD | 25,210.00 USD | `-41.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `412.50` | 2,930,000.00 USD | 0.00 USD | 4,550.00 USD | `-41.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `424.50` | 2,930,000.00 USD | 0.00 USD | 8,180.00 USD | `-39.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `433.50` | 2,920,000.00 USD | 0.00 USD | 173.83 USD | `-38.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `445.50` | 2,920,000.00 USD | 0.00 USD | 2,210.00 USD | `-37.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `455.50` | 2,920,000.00 USD | 0.00 USD | 698.74 USD | `-35.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `456.50` | 2,920,000.00 USD | 0.00 USD | 2,270.00 USD | `-35.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `457.50` | 2,910,000.00 USD | 0.00 USD | 2,270.00 USD | `-35.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `458.50` | 2,910,000.00 USD | 0.00 USD | 1,750.00 USD | `-35.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `469.50` | 2,910,000.00 USD | 0.00 USD | 3,550.00 USD | `-33.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `485.50` | 2,910,000.00 USD | 0.00 USD | 100.50 USD | `-31.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `486.50` | 2,910,000.00 USD | 0.00 USD | 100.71 USD | `-31.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `487.50` | 2,900,000.00 USD | 0.00 USD | 6,600.00 USD | `-31.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `488.50` | 2,900,000.00 USD | 0.00 USD | 125.06 USD | `-30.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `490.50` | 2,900,000.00 USD | 0.00 USD | 101.53 USD | `-30.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `492.50` | 2,900,000.00 USD | 0.00 USD | 2,450.00 USD | `-30.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `495.50` | 2,900,000.00 USD | 0.00 USD | 102.57 USD | `-29.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `498.50` | 2,900,000.00 USD | 0.00 USD | 163.01 USD | `-29.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `499.50` | 2,900,000.00 USD | 0.00 USD | 214.78 USD | `-29.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `500.50` | 2,900,000.00 USD | 0.00 USD | 12,610.00 USD | `-29.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `503.50` | 2,880,000.00 USD | 0.00 USD | 42,390.00 USD | `-28.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `506.50` | 2,840,000.00 USD | 0.00 USD | 138.78 USD | `-28.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `509.50` | 2,840,000.00 USD | 0.00 USD | 185.97 USD | `-27.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `515.50` | 2,840,000.00 USD | 0.00 USD | 1,030.00 USD | `-27.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `516.50` | 2,840,000.00 USD | 0.00 USD | 125.51 USD | `-26.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `517.50` | 2,840,000.00 USD | 0.00 USD | 280.49 USD | `-26.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `521.50` | 2,840,000.00 USD | 0.00 USD | 258.14 USD | `-26.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `524.50` | 2,840,000.00 USD | 0.00 USD | 8,170.00 USD | `-25.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `528.50` | 2,830,000.00 USD | 0.00 USD | 485.16 USD | `-25.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `534.50` | 2,830,000.00 USD | 0.00 USD | 4,650.00 USD | `-24.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `538.50` | 2,820,000.00 USD | 0.00 USD | 1,680.00 USD | `-23.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `540.50` | 2,820,000.00 USD | 0.00 USD | 864.80 USD | `-23.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `547.50` | 2,820,000.00 USD | 0.00 USD | 248.56 USD | `-22.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `550.50` | 2,820,000.00 USD | 0.00 USD | 4,130.00 USD | `-22.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `552.50` | 2,820,000.00 USD | 0.00 USD | 366,230.00 USD | `-21.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `554.50` | 2,450,000.00 USD | 0.00 USD | 1,190.00 USD | `-21.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `555.50` | 2,450,000.00 USD | 0.00 USD | 611.05 USD | `-21.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `557.50` | 2,450,000.00 USD | 0.00 USD | 213.52 USD | `-21.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `558.50` | 2,450,000.00 USD | 0.00 USD | 51,260.00 USD | `-21.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `560.50` | 2,400,000.00 USD | 0.00 USD | 292.02 USD | `-20.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `561.50` | 2,400,000.00 USD | 0.00 USD | 748.48 USD | `-20.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `562.50` | 2,400,000.00 USD | 0.00 USD | 199.12 USD | `-20.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `563.50` | 2,400,000.00 USD | 0.00 USD | 808.06 USD | `-20.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `566.50` | 2,400,000.00 USD | 0.00 USD | 566.50 USD | `-19.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `567.50` | 2,400,000.00 USD | 0.00 USD | 330.85 USD | `-19.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `568.50` | 2,400,000.00 USD | 0.00 USD | 5,680.00 USD | `-19.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `569.50` | 2,390,000.00 USD | 0.00 USD | 569.50 USD | `-19.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `570.50` | 2,390,000.00 USD | 0.00 USD | 774.17 USD | `-19.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `571.50` | 2,390,000.00 USD | 0.00 USD | 1,700.00 USD | `-19.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `573.50` | 2,390,000.00 USD | 0.00 USD | 291.91 USD | `-18.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `575.50` | 2,390,000.00 USD | 0.00 USD | 469.61 USD | `-18.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `576.50` | 2,390,000.00 USD | 0.00 USD | 289.98 USD | `-18.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `577.50` | 2,390,000.00 USD | 0.00 USD | 285.86 USD | `-18.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `579.50` | 2,390,000.00 USD | 0.00 USD | 289.17 USD | `-18.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `580.50` | 2,390,000.00 USD | 0.00 USD | 6,750.00 USD | `-17.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `581.50` | 2,380,000.00 USD | 0.00 USD | 1,240.00 USD | `-17.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `582.50` | 2,380,000.00 USD | 0.00 USD | 6,980.00 USD | `-17.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `583.50` | 2,370,000.00 USD | 0.00 USD | 287.67 USD | `-17.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `584.50` | 2,370,000.00 USD | 0.00 USD | 763.94 USD | `-17.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `585.50` | 2,370,000.00 USD | 0.00 USD | 542.76 USD | `-17.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `586.50` | 2,370,000.00 USD | 0.00 USD | 34,020.00 USD | `-17.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `587.50` | 2,330,000.00 USD | 0.00 USD | 830,190.00 USD | `-16.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `589.50` | 1,500,000.00 USD | 0.00 USD | 252.31 USD | `-16.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `590.50` | 1,500,000.00 USD | 0.00 USD | 540.31 USD | `-16.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `592.50` | 1,500,000.00 USD | 0.00 USD | 698.56 USD | `-16.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `593.50` | 1,500,000.00 USD | 0.00 USD | 1,160.00 USD | `-16.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `596.50` | 1,500,000.00 USD | 0.00 USD | 119.30 USD | `-15.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `597.50` | 1,500,000.00 USD | 0.00 USD | 222.87 USD | `-15.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `598.50` | 1,500,000.00 USD | 0.00 USD | 244.79 USD | `-15.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `600.50` | 1,500,000.00 USD | 0.00 USD | 56,310.00 USD | `-15.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `601.50` | 1,440,000.00 USD | 0.00 USD | 1,590.00 USD | `-14.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `602.50` | 1,440,000.00 USD | 0.00 USD | 46,760.00 USD | `-14.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `603.50` | 1,400,000.00 USD | 0.00 USD | 937.84 USD | `-14.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `604.50` | 1,400,000.00 USD | 0.00 USD | 1,870.00 USD | `-14.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `605.50` | 1,390,000.00 USD | 0.00 USD | 2,610.00 USD | `-14.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `608.50` | 1,390,000.00 USD | 0.00 USD | 18,380.00 USD | `-13.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `609.50` | 1,370,000.00 USD | 0.00 USD | 30,480.00 USD | `-13.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `610.50` | 1,340,000.00 USD | 0.00 USD | 12,220.00 USD | `-13.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `611.50` | 1,330,000.00 USD | 0.00 USD | 4,470.00 USD | `-13.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `614.50` | 1,330,000.00 USD | 0.00 USD | 269.15 USD | `-13.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `615.50` | 1,330,000.00 USD | 0.00 USD | 1,740.00 USD | `-12.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `616.50` | 1,320,000.00 USD | 0.00 USD | 120.83 USD | `-12.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `620.50` | 1,320,000.00 USD | 0.00 USD | 13,170.00 USD | `-12.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `621.50` | 1,310,000.00 USD | 0.00 USD | 2,150.00 USD | `-12.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `623.50` | 1,310,000.00 USD | 0.00 USD | 219.47 USD | `-11.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `624.50` | 1,310,000.00 USD | 0.00 USD | 445.27 USD | `-11.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `625.50` | 1,310,000.00 USD | 0.00 USD | 445.98 USD | `-11.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `626.50` | 1,310,000.00 USD | 0.00 USD | 694.79 USD | `-11.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `627.50` | 1,310,000.00 USD | 0.00 USD | 916.15 USD | `-11.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `628.50` | 1,310,000.00 USD | 0.00 USD | 746.03 USD | `-11.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `629.50` | 1,300,000.00 USD | 0.00 USD | 2,740.00 USD | `-10.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `630.50` | 1,300,000.00 USD | 0.00 USD | 861.26 USD | `-10.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `631.50` | 1,300,000.00 USD | 0.00 USD | 179.98 USD | `-10.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `632.50` | 1,300,000.00 USD | 0.00 USD | 4,900.00 USD | `-10.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `633.50` | 1,300,000.00 USD | 0.00 USD | 164.08 USD | `-10.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `634.50` | 1,300,000.00 USD | 0.00 USD | 2,550.00 USD | `-10.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `636.50` | 1,290,000.00 USD | 0.00 USD | 7,140.00 USD | `-10.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `637.50` | 1,290,000.00 USD | 0.00 USD | 2,730.00 USD | `-9.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `638.50` | 1,280,000.00 USD | 0.00 USD | 3,640.00 USD | `-9.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `639.50` | 1,280,000.00 USD | 0.00 USD | 384.98 USD | `-9.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `640.50` | 1,280,000.00 USD | 0.00 USD | 429.78 USD | `-9.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `641.50` | 1,280,000.00 USD | 0.00 USD | 352.18 USD | `-9.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `642.50` | 1,280,000.00 USD | 0.00 USD | 357.87 USD | `-9.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `643.50` | 1,280,000.00 USD | 0.00 USD | 1,980.00 USD | `-9.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `644.50` | 1,280,000.00 USD | 0.00 USD | 3,790.00 USD | `-8.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `645.50` | 1,270,000.00 USD | 0.00 USD | 10,640.00 USD | `-8.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `646.50` | 1,260,000.00 USD | 0.00 USD | 971.04 USD | `-8.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `648.50` | 1,260,000.00 USD | 0.00 USD | 1,800.00 USD | `-8.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `649.50` | 1,260,000.00 USD | 0.00 USD | 107.17 USD | `-8.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `650.50` | 1,260,000.00 USD | 0.00 USD | 32,070.00 USD | `-8.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `651.50` | 1,230,000.00 USD | 0.00 USD | 5,890.00 USD | `-7.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `653.50` | 1,220,000.00 USD | 0.00 USD | 2,020.00 USD | `-7.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `654.50` | 1,220,000.00 USD | 0.00 USD | 308.92 USD | `-7.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `655.50` | 1,220,000.00 USD | 0.00 USD | 165.84 USD | `-7.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `656.50` | 1,220,000.00 USD | 0.00 USD | 456.27 USD | `-7.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `657.50` | 1,220,000.00 USD | 0.00 USD | 110.46 USD | `-7.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `658.50` | 1,220,000.00 USD | 0.00 USD | 1,320.00 USD | `-6.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `659.50` | 1,220,000.00 USD | 0.00 USD | 13,060.00 USD | `-6.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `660.50` | 1,200,000.00 USD | 0.00 USD | 6,470.00 USD | `-6.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `661.50` | 1,200,000.00 USD | 0.00 USD | 11,310.00 USD | `-6.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `662.50` | 1,190,000.00 USD | 0.00 USD | 7,780.00 USD | `-6.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `663.50` | 1,180,000.00 USD | 0.00 USD | 4,040.00 USD | `-6.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `664.50` | 1,170,000.00 USD | 0.00 USD | 713.01 USD | `-6.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `665.50` | 1,170,000.00 USD | 0.00 USD | 576.32 USD | `-5.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `666.50` | 1,170,000.00 USD | 0.00 USD | 24,530.00 USD | `-5.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `667.50` | 1,150,000.00 USD | 0.00 USD | 10,740.00 USD | `-5.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `668.50` | 1,140,000.00 USD | 0.00 USD | 719.97 USD | `-5.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `669.50` | 1,140,000.00 USD | 0.00 USD | 2,390.00 USD | `-5.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `670.50` | 1,130,000.00 USD | 0.00 USD | 132,230.00 USD | `-5.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `671.50` | 1,000,000.00 USD | 0.00 USD | 5,280.00 USD | `-5.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `672.50` | 996,700.00 USD | 0.00 USD | 1,500.00 USD | `-4.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `673.50` | 995,200.00 USD | 0.00 USD | 3,460.00 USD | `-4.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `674.50` | 991,740.00 USD | 0.00 USD | 1,470.00 USD | `-4.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `675.50` | 990,270.00 USD | 0.00 USD | 8,350.00 USD | `-4.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `676.50` | 981,920.00 USD | 0.00 USD | 56,170.00 USD | `-4.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `677.50` | 925,750.00 USD | 0.00 USD | 39,650.00 USD | `-4.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `678.50` | 886,100.00 USD | 0.00 USD | 825.73 USD | `-4.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `679.50` | 885,270.00 USD | 0.00 USD | 254.13 USD | `-3.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `680.50` | 885,020.00 USD | 0.00 USD | 3,200.00 USD | `-3.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `681.50` | 881,820.00 USD | 0.00 USD | 146.52 USD | `-3.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `682.50` | 881,670.00 USD | 0.00 USD | 4,740.00 USD | `-3.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `683.50` | 876,930.00 USD | 0.00 USD | 171,850.00 USD | `-3.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `684.50` | 705,080.00 USD | 0.00 USD | 171,120.00 USD | `-3.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `685.50` | 533,960.00 USD | 0.00 USD | 11,030.00 USD | `-3.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `686.50` | 522,930.00 USD | 0.00 USD | 530.66 USD | `-2.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `687.50` | 522,400.00 USD | 0.00 USD | 323.12 USD | `-2.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `688.50` | 522,080.00 USD | 0.00 USD | 262.32 USD | `-2.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `689.50` | 521,810.00 USD | 0.00 USD | 532.98 USD | `-2.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `690.50` | 521,280.00 USD | 0.00 USD | 91,630.00 USD | `-2.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `691.50` | 429,650.00 USD | 0.00 USD | 174,840.00 USD | `-2.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `692.50` | 254,810.00 USD | 0.00 USD | 4,450.00 USD | `-2.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `693.50` | 250,360.00 USD | 0.00 USD | 990.32 USD | `-1.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `694.50` | 249,370.00 USD | 0.00 USD | 1,540.00 USD | `-1.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `695.50` | 247,840.00 USD | 0.00 USD | 166.92 USD | `-1.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `696.50` | 247,670.00 USD | 0.00 USD | 136.51 USD | `-1.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `697.50` | 247,530.00 USD | 0.00 USD | 47,550.00 USD | `-1.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `698.50` | 199,980.00 USD | 0.00 USD | 15,500.00 USD | `-1.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `699.50` | 184,490.00 USD | 0.00 USD | 38,470.00 USD | `-1.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `700.50` | 146,020.00 USD | 0.00 USD | 42,530.00 USD | `-0.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `701.50` | 103,490.00 USD | 0.00 USD | 329.71 USD | `-0.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `702.50` | 103,160.00 USD | 0.00 USD | 380.05 USD | `-0.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `703.50` | 102,780.00 USD | 0.00 USD | 3,850.00 USD | `-0.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `704.50` | 98,930.00 USD | 0.00 USD | 86,660.00 USD | `-0.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `705.50` | 12,270.00 USD | 0.00 USD | 640.59 USD | `-0.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `706.50` | 11,630.00 USD | 0.00 USD | 11,630.00 USD | `-0.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `707.50` | 13,270.00 USD | 13,270.00 USD | 0.00 USD | `+0.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `708.50` | 15,400.00 USD | 2,130.00 USD | 0.00 USD | `+0.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `709.50` | 16,210.00 USD | 813.80 USD | 0.00 USD | `+0.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `710.50` | 22,400.00 USD | 6,190.00 USD | 0.00 USD | `+0.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `711.50` | 24,320.00 USD | 1,910.00 USD | 0.00 USD | `+0.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `712.50` | 24,960.00 USD | 646.95 USD | 0.00 USD | `+0.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `713.50` | 42,960.00 USD | 18,000.00 USD | 0.00 USD | `+0.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `714.50` | 44,620.00 USD | 1,660.00 USD | 0.00 USD | `+1.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `715.50` | 47,720.00 USD | 3,100.00 USD | 0.00 USD | `+1.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `716.50` | 216,420.00 USD | 168,690.00 USD | 0.00 USD | `+1.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `717.50` | 218,430.00 USD | 2,010.00 USD | 0.00 USD | `+1.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `718.50` | 277,520.00 USD | 59,090.00 USD | 0.00 USD | `+1.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `719.50` | 347,750.00 USD | 70,240.00 USD | 0.00 USD | `+1.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `720.50` | 348,110.00 USD | 357.37 USD | 0.00 USD | `+1.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `721.50` | 401,680.00 USD | 53,570.00 USD | 0.00 USD | `+2.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `722.50` | 408,660.00 USD | 6,980.00 USD | 0.00 USD | `+2.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `723.50` | 416,910.00 USD | 8,250.00 USD | 0.00 USD | `+2.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `724.50` | 452,880.00 USD | 35,970.00 USD | 0.00 USD | `+2.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `725.50` | 547,470.00 USD | 94,580.00 USD | 0.00 USD | `+2.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `726.50` | 547,970.00 USD | 501.28 USD | 0.00 USD | `+2.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `727.50` | 567,170.00 USD | 19,200.00 USD | 0.00 USD | `+2.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `728.50` | 620,340.00 USD | 53,170.00 USD | 0.00 USD | `+3.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `729.50` | 761,150.00 USD | 140,810.00 USD | 0.00 USD | `+3.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `730.50` | 765,570.00 USD | 4,430.00 USD | 0.00 USD | `+3.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `731.50` | 964,560.00 USD | 198,990.00 USD | 0.00 USD | `+3.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `732.50` | 965,970.00 USD | 1,410.00 USD | 0.00 USD | `+3.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `733.50` | 1,450,000.00 USD | 487,680.00 USD | 0.00 USD | `+3.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `734.50` | 1,460,000.00 USD | 7,480.00 USD | 0.00 USD | `+3.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `735.50` | 1,480,000.00 USD | 23,100.00 USD | 0.00 USD | `+4.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `736.50` | 1,490,000.00 USD | 5,460.00 USD | 0.00 USD | `+4.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `737.50` | 1,490,000.00 USD | 3,970.00 USD | 0.00 USD | `+4.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `738.50` | 1,510,000.00 USD | 13,270.00 USD | 0.00 USD | `+4.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `739.50` | 1,510,000.00 USD | 790.53 USD | 0.00 USD | `+4.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `740.50` | 1,510,000.00 USD | 2,110.00 USD | 0.00 USD | `+4.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `741.50` | 1,510,000.00 USD | 3,840.00 USD | 0.00 USD | `+4.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `742.50` | 1,530,000.00 USD | 13,140.00 USD | 0.00 USD | `+4.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `743.50` | 1,540,000.00 USD | 11,530.00 USD | 0.00 USD | `+5.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `744.50` | 1,740,000.00 USD | 203,810.00 USD | 0.00 USD | `+5.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `745.50` | 1,750,000.00 USD | 4,750.00 USD | 0.00 USD | `+5.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `746.50` | 1,820,000.00 USD | 76,650.00 USD | 0.00 USD | `+5.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `747.50` | 1,820,000.00 USD | 219.76 USD | 0.00 USD | `+5.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `748.50` | 1,820,000.00 USD | 279.19 USD | 0.00 USD | `+5.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `749.50` | 1,820,000.00 USD | 704.53 USD | 0.00 USD | `+5.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `750.50` | 1,820,000.00 USD | 123.83 USD | 0.00 USD | `+6.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `751.50` | 1,830,000.00 USD | 8,720.00 USD | 0.00 USD | `+6.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `752.50` | 1,840,000.00 USD | 2,730.00 USD | 0.00 USD | `+6.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `753.50` | 1,840,000.00 USD | 629.17 USD | 0.00 USD | `+6.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `754.50` | 1,880,000.00 USD | 47,160.00 USD | 0.00 USD | `+6.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `755.50` | 1,890,000.00 USD | 4,420.00 USD | 0.00 USD | `+6.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `756.50` | 1,900,000.00 USD | 10,340.00 USD | 0.00 USD | `+6.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `757.50` | 2,040,000.00 USD | 142,940.00 USD | 0.00 USD | `+7.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `758.50` | 2,040,000.00 USD | 2,790.00 USD | 0.00 USD | `+7.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `759.50` | 2,040,000.00 USD | 325.07 USD | 0.00 USD | `+7.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `760.50` | 2,330,000.00 USD | 287,930.00 USD | 0.00 USD | `+7.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `761.50` | 2,340,000.00 USD | 11,460.00 USD | 0.00 USD | `+7.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `762.50` | 2,340,000.00 USD | 274.50 USD | 0.00 USD | `+7.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `763.50` | 2,390,000.00 USD | 44,150.00 USD | 0.00 USD | `+7.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `764.50` | 2,390,000.00 USD | 323.38 USD | 0.00 USD | `+8.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `765.50` | 2,450,000.00 USD | 60,710.00 USD | 0.00 USD | `+8.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `766.50` | 2,450,000.00 USD | 571.81 USD | 0.00 USD | `+8.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `767.50` | 2,920,000.00 USD | 468,310.00 USD | 0.00 USD | `+8.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `768.50` | 2,920,000.00 USD | 180.60 USD | 0.00 USD | `+8.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `769.50` | 2,920,000.00 USD | 171.60 USD | 0.00 USD | `+8.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `770.50` | 2,920,000.00 USD | 1,540.00 USD | 0.00 USD | `+8.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `771.50` | 2,920,000.00 USD | 242.25 USD | 0.00 USD | `+9.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `772.50` | 2,930,000.00 USD | 12,400.00 USD | 0.00 USD | `+9.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `773.50` | 2,930,000.00 USD | 656.70 USD | 0.00 USD | `+9.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `774.50` | 2,940,000.00 USD | 9,680.00 USD | 0.00 USD | `+9.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `775.50` | 2,950,000.00 USD | 4,570.00 USD | 0.00 USD | `+9.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `776.50` | 2,960,000.00 USD | 14,230.00 USD | 0.00 USD | `+9.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `777.50` | 2,980,000.00 USD | 15,690.00 USD | 0.00 USD | `+9.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `778.50` | 2,990,000.00 USD | 9,990.00 USD | 0.00 USD | `+10.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `779.50` | 2,990,000.00 USD | 132.52 USD | 0.00 USD | `+10.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `780.50` | 3,010,000.00 USD | 24,280.00 USD | 0.00 USD | `+10.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `781.50` | 3,010,000.00 USD | 2,050.00 USD | 0.00 USD | `+10.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `782.50` | 3,020,000.00 USD | 1,900.00 USD | 0.00 USD | `+10.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `783.50` | 3,020,000.00 USD | 101.07 USD | 0.00 USD | `+10.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `784.50` | 3,020,000.00 USD | 102.77 USD | 0.00 USD | `+10.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `785.50` | 3,020,000.00 USD | 559.28 USD | 0.00 USD | `+11.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `786.50` | 3,020,000.00 USD | 5,610.00 USD | 0.00 USD | `+11.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `787.50` | 3,030,000.00 USD | 2,260.00 USD | 0.00 USD | `+11.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `788.50` | 3,030,000.00 USD | 133.26 USD | 0.00 USD | `+11.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `790.50` | 3,030,000.00 USD | 4,190.00 USD | 0.00 USD | `+11.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `791.50` | 3,030,000.00 USD | 704.44 USD | 0.00 USD | `+11.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `792.50` | 3,030,000.00 USD | 4,360.00 USD | 0.00 USD | `+12.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `793.50` | 3,040,000.00 USD | 1,450.00 USD | 0.00 USD | `+12.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `794.50` | 3,040,000.00 USD | 3,630.00 USD | 0.00 USD | `+12.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `795.50` | 3,040,000.00 USD | 3,390.00 USD | 0.00 USD | `+12.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `796.50` | 3,040,000.00 USD | 154.52 USD | 0.00 USD | `+12.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `798.50` | 3,050,000.00 USD | 7,140.00 USD | 0.00 USD | `+12.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `799.50` | 3,050,000.00 USD | 1,260.00 USD | 0.00 USD | `+13.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `800.50` | 3,070,000.00 USD | 14,370.00 USD | 0.00 USD | `+13.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `801.50` | 3,070,000.00 USD | 120.22 USD | 0.00 USD | `+13.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `803.50` | 3,070,000.00 USD | 803.50 USD | 0.00 USD | `+13.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `805.50` | 3,070,000.00 USD | 120.02 USD | 0.00 USD | `+13.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `806.50` | 3,070,000.00 USD | 1,300.00 USD | 0.00 USD | `+14.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `808.50` | 3,070,000.00 USD | 5,010.00 USD | 0.00 USD | `+14.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `809.50` | 3,070,000.00 USD | 242.04 USD | 0.00 USD | `+14.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `810.50` | 3,090,000.00 USD | 15,790.00 USD | 0.00 USD | `+14.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `811.50` | 3,090,000.00 USD | 374.10 USD | 0.00 USD | `+14.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `812.50` | 3,090,000.00 USD | 844.19 USD | 0.00 USD | `+14.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `813.50` | 3,090,000.00 USD | 109.82 USD | 0.00 USD | `+15.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `814.50` | 3,090,000.00 USD | 3,390.00 USD | 0.00 USD | `+15.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `816.50` | 3,090,000.00 USD | 984.70 USD | 0.00 USD | `+15.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `817.50` | 3,100,000.00 USD | 162.68 USD | 0.00 USD | `+15.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `818.50` | 3,100,000.00 USD | 5,990.00 USD | 0.00 USD | `+15.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `820.50` | 3,110,000.00 USD | 7,820.00 USD | 0.00 USD | `+16.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `824.50` | 3,110,000.00 USD | 408.13 USD | 0.00 USD | `+16.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `826.50` | 3,110,000.00 USD | 672.77 USD | 0.00 USD | `+16.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `827.50` | 3,110,000.00 USD | 276.38 USD | 0.00 USD | `+17.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `828.50` | 3,110,000.00 USD | 1,800.00 USD | 0.00 USD | `+17.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `830.50` | 3,150,000.00 USD | 35,850.00 USD | 0.00 USD | `+17.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `833.50` | 3,150,000.00 USD | 1,170.00 USD | 0.00 USD | `+17.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `835.50` | 3,150,000.00 USD | 187.15 USD | 0.00 USD | `+18.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `836.50` | 3,150,000.00 USD | 372.24 USD | 0.00 USD | `+18.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `837.50` | 3,150,000.00 USD | 326.62 USD | 0.00 USD | `+18.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `839.50` | 3,150,000.00 USD | 296.34 USD | 0.00 USD | `+18.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `840.50` | 3,160,000.00 USD | 5,040.00 USD | 0.00 USD | `+18.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `841.50` | 3,160,000.00 USD | 329.87 USD | 0.00 USD | `+18.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `843.50` | 3,160,000.00 USD | 425.97 USD | 0.00 USD | `+19.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `844.50` | 3,160,000.00 USD | 1,770.00 USD | 0.00 USD | `+19.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `850.50` | 3,160,000.00 USD | 2,550.00 USD | 0.00 USD | `+20.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `851.50` | 3,170,000.00 USD | 11,650.00 USD | 0.00 USD | `+20.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `852.50` | 3,170,000.00 USD | 102.30 USD | 0.00 USD | `+20.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `854.50` | 3,170,000.00 USD | 137.57 USD | 0.00 USD | `+20.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `857.50` | 3,170,000.00 USD | 1,200.00 USD | 0.00 USD | `+21.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `860.50` | 3,170,000.00 USD | 1,160.00 USD | 0.00 USD | `+21.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `862.50` | 3,180,000.00 USD | 1,200.00 USD | 0.00 USD | `+21.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `863.50` | 3,180,000.00 USD | 874.73 USD | 0.00 USD | `+22.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `864.50` | 3,180,000.00 USD | 2,970.00 USD | 0.00 USD | `+22.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `865.50` | 3,180,000.00 USD | 3,460.00 USD | 0.00 USD | `+22.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `868.50` | 3,190,000.00 USD | 2,610.00 USD | 0.00 USD | `+22.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `870.50` | 3,190,000.00 USD | 228.07 USD | 0.00 USD | `+23.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `872.50` | 3,190,000.00 USD | 1,110.00 USD | 0.00 USD | `+23.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `884.50` | 3,240,000.00 USD | 54,820.00 USD | 0.00 USD | `+25.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `888.50` | 3,240,000.00 USD | 266.55 USD | 0.00 USD | `+25.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `890.50` | 3,240,000.00 USD | 690.14 USD | 0.00 USD | `+25.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `891.50` | 3,240,000.00 USD | 605.33 USD | 0.00 USD | `+26.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `895.50` | 3,240,000.00 USD | 130.74 USD | 0.00 USD | `+26.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `898.50` | 3,240,000.00 USD | 101.53 USD | 0.00 USD | `+27.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `900.50` | 3,370,000.00 USD | 126,250.00 USD | 0.00 USD | `+27.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `904.50` | 3,370,000.00 USD | 167.33 USD | 0.00 USD | `+27.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `907.50` | 3,370,000.00 USD | 1,640.00 USD | 0.00 USD | `+28.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `913.50` | 3,370,000.00 USD | 908.02 USD | 0.00 USD | `+29.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `914.50` | 3,380,000.00 USD | 4,150.00 USD | 0.00 USD | `+29.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `917.50` | 3,380,000.00 USD | 533.99 USD | 0.00 USD | `+29.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `919.50` | 3,380,000.00 USD | 166.43 USD | 0.00 USD | `+30.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `920.50` | 3,380,000.00 USD | 463.01 USD | 0.00 USD | `+30.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `926.50` | 3,380,000.00 USD | 320.57 USD | 0.00 USD | `+31.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `930.50` | 3,380,000.00 USD | 552.72 USD | 0.00 USD | `+31.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `933.50` | 3,380,000.00 USD | 196.03 USD | 0.00 USD | `+31.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `935.50` | 3,380,000.00 USD | 287.20 USD | 0.00 USD | `+32.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `958.50` | 3,380,000.00 USD | 782.14 USD | 0.00 USD | `+35.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `959.50` | 3,380,000.00 USD | 498.94 USD | 0.00 USD | `+35.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `964.50` | 3,380,000.00 USD | 964.50 USD | 0.00 USD | `+36.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `965.50` | 3,380,000.00 USD | 1,930.00 USD | 0.00 USD | `+36.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `977.50` | 3,380,000.00 USD | 293.25 USD | 0.00 USD | `+38.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `980.50` | 3,390,000.00 USD | 1,300.00 USD | 0.00 USD | `+38.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `981.50` | 3,390,000.00 USD | 109.93 USD | 0.00 USD | `+38.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `984.50` | 3,390,000.00 USD | 439.09 USD | 0.00 USD | `+39.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `987.50` | 3,390,000.00 USD | 2,590.00 USD | 0.00 USD | `+39.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `995.50` | 3,390,000.00 USD | 145.34 USD | 0.00 USD | `+40.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `997.50` | 3,390,000.00 USD | 1,760.00 USD | 0.00 USD | `+41.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `998.50` | 3,390,000.00 USD | 3,990.00 USD | 0.00 USD | `+41.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `999.50` | 3,400,000.00 USD | 938.53 USD | 0.00 USD | `+41.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1000.50` | 3,410,000.00 USD | 11,810.00 USD | 0.00 USD | `+41.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1017.50` | 3,410,000.00 USD | 203.50 USD | 0.00 USD | `+43.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1020.50` | 3,410,000.00 USD | 148.99 USD | 0.00 USD | `+44.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1026.50` | 3,410,000.00 USD | 149.87 USD | 0.00 USD | `+45.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1030.50` | 3,410,000.00 USD | 150.45 USD | 0.00 USD | `+45.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1045.50` | 3,410,000.00 USD | 195.51 USD | 0.00 USD | `+47.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1053.50` | 3,410,000.00 USD | 149.60 USD | 0.00 USD | `+48.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1072.50` | 3,410,000.00 USD | 156.58 USD | 0.00 USD | `+51.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1100.50` | 3,410,000.00 USD | 278.43 USD | 0.00 USD | `+55.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1111.50` | 3,410,000.00 USD | 555.75 USD | 0.00 USD | `+57.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1136.50` | 3,410,000.00 USD | 165.93 USD | 0.00 USD | `+60.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1146.50` | 3,410,000.00 USD | 167.39 USD | 0.00 USD | `+62.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1200.50` | 3,470,000.00 USD | 62,330.00 USD | 0.00 USD | `+69.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1202.50` | 3,470,000.00 USD | 1,250.00 USD | 0.00 USD | `+70.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1226.50` | 3,470,000.00 USD | 235.49 USD | 0.00 USD | `+73.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1230.50` | 3,480,000.00 USD | 3,580.00 USD | 0.00 USD | `+73.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1250.50` | 3,480,000.00 USD | 421.42 USD | 0.00 USD | `+76.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1280.50` | 3,480,000.00 USD | 3,750.00 USD | 0.00 USD | `+81.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1297.50` | 3,480,000.00 USD | 133.64 USD | 0.00 USD | `+83.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1300.50` | 3,480,000.00 USD | 685.36 USD | 0.00 USD | `+83.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1330.50` | 3,540,000.00 USD | 58,230.00 USD | 0.00 USD | `+88.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1340.50` | 3,620,000.00 USD | 80,850.00 USD | 0.00 USD | `+89.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1360.50` | 3,630,000.00 USD | 6,210.00 USD | 0.00 USD | `+92.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1363.50` | 3,630,000.00 USD | 349.06 USD | 0.00 USD | `+92.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1370.50` | 3,630,000.00 USD | 1,060.00 USD | 0.00 USD | `+93.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1372.50` | 3,650,000.00 USD | 19,210.00 USD | 0.00 USD | `+94.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1389.50` | 3,650,000.00 USD | 425.19 USD | 0.00 USD | `+96.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1400.50` | 3,650,000.00 USD | 3,850.00 USD | 0.00 USD | `+98.03%` | `TACTICAL (Retail Cluster)` |

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
| `7D` | `633.90` | 37,630,000.00 USD | 0.00 USD | 37,630,000.00 USD | 70,320.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `634.30` | 48,740,000.00 USD | 0.00 USD | 48,740,000.00 USD | 28,010.00 USD | 47,460.00 USD | 80,500.00 USD |
| `7D` | `634.90` | 37,560,000.00 USD | 0.00 USD | 37,560,000.00 USD | 0.00 USD | 51,290.00 USD | 0.00 USD |
| `1D` | `635.10` | 48,590,000.00 USD | 0.00 USD | 48,590,000.00 USD | 0.00 USD | 9,540.00 USD | 82,800.00 USD |
| `1D` | `635.90` | 48,500,000.00 USD | 0.00 USD | 48,500,000.00 USD | 140,670.00 USD | 40,910.00 USD | 12,850.00 USD |
| `7D` | `635.90` | 37,510,000.00 USD | 0.00 USD | 37,510,000.00 USD | 90,060.00 USD | 17,990.00 USD | 0.00 USD |
| `1D` | `636.70` | 48,300,000.00 USD | 0.00 USD | 48,300,000.00 USD | 120,680.00 USD | 25,980.00 USD | 240,130.00 USD |
| `1D` | `637.50` | 47,910,000.00 USD | 0.00 USD | 47,910,000.00 USD | 69,730.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `638.30` | 47,840,000.00 USD | 0.00 USD | 47,840,000.00 USD | 24,710.00 USD | 37,610.00 USD | 0.00 USD |
| `1D` | `639.10` | 47,780,000.00 USD | 0.00 USD | 47,780,000.00 USD | 225,300.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `639.90` | 47,560,000.00 USD | 0.00 USD | 47,560,000.00 USD | 21,450.00 USD | 0.00 USD | 184,710.00 USD |
| `7D` | `640.90` | 37,400,000.00 USD | 0.00 USD | 37,400,000.00 USD | 0.00 USD | 0.00 USD | 224,770.00 USD |
| `1D` | `641.50` | 47,350,000.00 USD | 0.00 USD | 47,350,000.00 USD | 59,370.00 USD | 0.00 USD | 4,880.00 USD |
| `7D` | `641.90` | 37,170,000.00 USD | 0.00 USD | 37,170,000.00 USD | 0.00 USD | 40,220.00 USD | 0.00 USD |
| `1D` | `642.30` | 47,290,000.00 USD | 0.00 USD | 47,290,000.00 USD | 177,370.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `642.90` | 37,130,000.00 USD | 0.00 USD | 37,130,000.00 USD | 171,810.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `643.10` | 47,110,000.00 USD | 0.00 USD | 47,110,000.00 USD | 86,980.00 USD | 6,260.00 USD | 0.00 USD |
| `1D` | `643.90` | 47,020,000.00 USD | 0.00 USD | 47,020,000.00 USD | 29,750.00 USD | 13,880.00 USD | 0.00 USD |
| `7D` | `643.90` | 36,960,000.00 USD | 0.00 USD | 36,960,000.00 USD | 35,270.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `644.70` | 46,970,000.00 USD | 0.00 USD | 46,970,000.00 USD | 423,260.00 USD | 27,730.00 USD | 341,610.00 USD |
| `7D` | `644.90` | 36,930,000.00 USD | 0.00 USD | 36,930,000.00 USD | 0.00 USD | 24,160.00 USD | 0.00 USD |
| `1D` | `645.50` | 46,180,000.00 USD | 0.00 USD | 46,180,000.00 USD | 61,450.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `645.90` | 36,900,000.00 USD | 0.00 USD | 36,900,000.00 USD | 0.00 USD | 0.00 USD | 73,770.00 USD |
| `1D` | `646.30` | 46,120,000.00 USD | 0.00 USD | 46,120,000.00 USD | 156,000.00 USD | 11,780.00 USD | 184,540.00 USD |
| `7D` | `646.90` | 36,830,000.00 USD | 0.00 USD | 36,830,000.00 USD | 45,640.00 USD | 18,000.00 USD | 105,680.00 USD |
| `1D` | `647.10` | 45,770,000.00 USD | 0.00 USD | 45,770,000.00 USD | 204,530.00 USD | 31,640.00 USD | 33,810.00 USD |
| `1D` | `647.90` | 45,500,000.00 USD | 0.00 USD | 45,500,000.00 USD | 136,750.00 USD | 4,630.00 USD | 7,150.00 USD |
| `7D` | `647.90` | 36,660,000.00 USD | 0.00 USD | 36,660,000.00 USD | 122,600.00 USD | 16,830.00 USD | 14,870.00 USD |
| `1D` | `648.70` | 45,350,000.00 USD | 0.00 USD | 45,350,000.00 USD | 92,180.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `648.90` | 36,510,000.00 USD | 0.00 USD | 36,510,000.00 USD | 0.00 USD | 0.00 USD | 14,670.00 USD |
| `1D` | `649.50` | 45,260,000.00 USD | 0.00 USD | 45,260,000.00 USD | 96,580.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `649.90` | 36,490,000.00 USD | 0.00 USD | 36,490,000.00 USD | 162,040.00 USD | 15,690.00 USD | 0.00 USD |
| `1D` | `650.30` | 45,160,000.00 USD | 0.00 USD | 45,160,000.00 USD | 17,370.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `650.90` | 36,310,000.00 USD | 0.00 USD | 36,310,000.00 USD | 23,920.00 USD | 14,650.00 USD | 14,200.00 USD |
| `1D` | `651.10` | 45,140,000.00 USD | 0.00 USD | 45,140,000.00 USD | 184,040.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `651.90` | 44,960,000.00 USD | 0.00 USD | 44,960,000.00 USD | 0.00 USD | 0.00 USD | 94,590.00 USD |
| `7D` | `651.90` | 36,260,000.00 USD | 0.00 USD | 36,260,000.00 USD | 92,240.00 USD | 33,210.00 USD | 140,720.00 USD |
| `1D` | `652.70` | 44,860,000.00 USD | 0.00 USD | 44,860,000.00 USD | 30,730.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `652.90` | 35,990,000.00 USD | 0.00 USD | 35,990,000.00 USD | 213,140.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `653.50` | 44,830,000.00 USD | 0.00 USD | 44,830,000.00 USD | 43,630.00 USD | 26,830.00 USD | 0.00 USD |
| `1D` | `654.30` | 44,760,000.00 USD | 0.00 USD | 44,760,000.00 USD | 73,900.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `654.90` | 35,780,000.00 USD | 0.00 USD | 35,780,000.00 USD | 163,670.00 USD | 8,370.00 USD | 21,920.00 USD |
| `1D` | `655.10` | 44,690,000.00 USD | 0.00 USD | 44,690,000.00 USD | 88,130.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `655.90` | 44,600,000.00 USD | 0.00 USD | 44,600,000.00 USD | 209,270.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `655.90` | 35,590,000.00 USD | 0.00 USD | 35,590,000.00 USD | 47,200.00 USD | 16,330.00 USD | 0.00 USD |
| `1D` | `656.70` | 44,390,000.00 USD | 0.00 USD | 44,390,000.00 USD | 113,920.00 USD | 40,970.00 USD | 825,700.00 USD |
| `7D` | `656.90` | 35,520,000.00 USD | 0.00 USD | 35,520,000.00 USD | 105,420.00 USD | 0.00 USD | 10,970.00 USD |
| `1D` | `657.50` | 43,410,000.00 USD | 0.00 USD | 43,410,000.00 USD | 248,110.00 USD | 0.00 USD | 21,320.00 USD |
| `7D` | `657.90` | 35,410,000.00 USD | 0.00 USD | 35,410,000.00 USD | 0.00 USD | 7,610.00 USD | 19,000.00 USD |
| `1D` | `658.30` | 43,140,000.00 USD | 0.00 USD | 43,140,000.00 USD | 795,080.00 USD | 14,920.00 USD | 0.00 USD |
| `7D` | `658.90` | 35,380,000.00 USD | 0.00 USD | 35,380,000.00 USD | 0.00 USD | 18,790.00 USD | 13,980.00 USD |
| `1D` | `659.10` | 42,330,000.00 USD | 0.00 USD | 42,330,000.00 USD | 119,820.00 USD | 7,460.00 USD | 81,440.00 USD |
| `1D` | `659.90` | 42,120,000.00 USD | 0.00 USD | 42,120,000.00 USD | 111,490.00 USD | 0.00 USD | 14,670.00 USD |
| `7D` | `659.90` | 35,350,000.00 USD | 0.00 USD | 35,350,000.00 USD | 38,970.00 USD | 12,000.00 USD | 98,990.00 USD |
| `1D` | `660.70` | 42,000,000.00 USD | 0.00 USD | 42,000,000.00 USD | 90,670.00 USD | 83,170.00 USD | 0.00 USD |
| `7D` | `660.90` | 35,200,000.00 USD | 0.00 USD | 35,200,000.00 USD | 277,360.00 USD | 17,690.00 USD | 14,570.00 USD |
| `1D` | `661.50` | 41,820,000.00 USD | 0.00 USD | 41,820,000.00 USD | 468,220.00 USD | 19,460.00 USD | 0.00 USD |
| `7D` | `661.90` | 34,890,000.00 USD | 0.00 USD | 34,890,000.00 USD | 123,210.00 USD | 13,120.00 USD | 692,280.00 USD |
| `1D` | `662.30` | 41,330,000.00 USD | 0.00 USD | 41,330,000.00 USD | 165,160.00 USD | 136,330.00 USD | 0.00 USD |
| `7D` | `662.90` | 34,060,000.00 USD | 0.00 USD | 34,060,000.00 USD | 166,320.00 USD | 144,590.00 USD | 36,490.00 USD |
| `1D` | `663.10` | 41,030,000.00 USD | 0.00 USD | 41,030,000.00 USD | 259,470.00 USD | 5,000.00 USD | 44,630.00 USD |
| `1D` | `663.90` | 40,720,000.00 USD | 0.00 USD | 40,720,000.00 USD | 45,960.00 USD | 64,390.00 USD | 64,090.00 USD |
| `7D` | `663.90` | 33,710,000.00 USD | 0.00 USD | 33,710,000.00 USD | 943,280.00 USD | 18,740.00 USD | 22,460.00 USD |
| `1D` | `664.70` | 40,550,000.00 USD | 0.00 USD | 40,550,000.00 USD | 1,330,000.00 USD | 0.00 USD | 61,580.00 USD |
| `7D` | `664.90` | 32,730,000.00 USD | 0.00 USD | 32,730,000.00 USD | 237,720.00 USD | 22,990.00 USD | 50,380.00 USD |
| `1D` | `665.50` | 39,160,000.00 USD | 0.00 USD | 39,160,000.00 USD | 702,330.00 USD | 4,540.00 USD | 11,460.00 USD |
| `7D` | `665.90` | 32,420,000.00 USD | 0.00 USD | 32,420,000.00 USD | 398,250.00 USD | 60,610.00 USD | 63,410.00 USD |
| `1D` | `666.30` | 38,440,000.00 USD | 0.00 USD | 38,440,000.00 USD | 315,600.00 USD | 93,680.00 USD | 750,630.00 USD |
| `7D` | `666.90` | 31,890,000.00 USD | 0.00 USD | 31,890,000.00 USD | 425,290.00 USD | 33,320.00 USD | 53,950.00 USD |
| `1D` | `667.10` | 37,280,000.00 USD | 0.00 USD | 37,280,000.00 USD | 902,750.00 USD | 25,280.00 USD | 40,700.00 USD |
| `1D` | `667.90` | 36,310,000.00 USD | 0.00 USD | 36,310,000.00 USD | 385,370.00 USD | 150,850.00 USD | 0.00 USD |
| `7D` | `667.90` | 31,380,000.00 USD | 0.00 USD | 31,380,000.00 USD | 1,050,000.00 USD | 67,080.00 USD | 67,320.00 USD |
| `1D` | `668.70` | 35,770,000.00 USD | 0.00 USD | 35,770,000.00 USD | 771,830.00 USD | 39,300.00 USD | 3,620.00 USD |
| `7D` | `668.90` | 30,200,000.00 USD | 0.00 USD | 30,200,000.00 USD | 738,400.00 USD | 70,910.00 USD | 72,340.00 USD |
| `1D` | `669.50` | 34,960,000.00 USD | 0.00 USD | 34,960,000.00 USD | 481,670.00 USD | 61,020.00 USD | 29,910.00 USD |
| `7D` | `669.90` | 29,320,000.00 USD | 0.00 USD | 29,320,000.00 USD | 240,000.00 USD | 38,130.00 USD | 71,700.00 USD |
| `1D` | `670.30` | 34,390,000.00 USD | 0.00 USD | 34,390,000.00 USD | 661,320.00 USD | 50,060.00 USD | 1,500,000.00 USD |
| `7D` | `670.90` | 28,970,000.00 USD | 0.00 USD | 28,970,000.00 USD | 760,980.00 USD | 135,260.00 USD | 102,340.00 USD |
| `1D` | `671.10` | 32,180,000.00 USD | 0.00 USD | 32,180,000.00 USD | 557,780.00 USD | 13,720.00 USD | 45,290.00 USD |
| `1D` | `671.90` | 31,560,000.00 USD | 0.00 USD | 31,560,000.00 USD | 2,030,000.00 USD | 18,180.00 USD | 6,520.00 USD |
| `7D` | `671.90` | 27,970,000.00 USD | 0.00 USD | 27,970,000.00 USD | 255,560.00 USD | 26,430.00 USD | 684,860.00 USD |
| `1D` | `672.70` | 29,510,000.00 USD | 0.00 USD | 29,510,000.00 USD | 136,910.00 USD | 63,880.00 USD | 857,540.00 USD |
| `7D` | `672.90` | 27,000,000.00 USD | 0.00 USD | 27,000,000.00 USD | 1,010,000.00 USD | 159,740.00 USD | 31,670.00 USD |
| `1D` | `673.50` | 28,450,000.00 USD | 0.00 USD | 28,450,000.00 USD | 329,360.00 USD | 298,210.00 USD | 1,560,000.00 USD |
| `7D` | `673.90` | 25,800,000.00 USD | 0.00 USD | 25,800,000.00 USD | 335,670.00 USD | 268,790.00 USD | 60,640.00 USD |
| `1D` | `674.30` | 26,260,000.00 USD | 0.00 USD | 26,260,000.00 USD | 328,930.00 USD | 407,150.00 USD | 94,370.00 USD |
| `7D` | `674.90` | 25,130,000.00 USD | 0.00 USD | 25,130,000.00 USD | 143,690.00 USD | 129,800.00 USD | 860,540.00 USD |
| `1D` | `675.10` | 25,430,000.00 USD | 0.00 USD | 25,430,000.00 USD | 2,050,000.00 USD | 72,240.00 USD | 392,190.00 USD |
| `1D` | `675.90` | 22,920,000.00 USD | 0.00 USD | 22,920,000.00 USD | 621,390.00 USD | 348,940.00 USD | 210,740.00 USD |
| `7D` | `675.90` | 24,000,000.00 USD | 0.00 USD | 24,000,000.00 USD | 394,120.00 USD | 131,610.00 USD | 1,840,000.00 USD |
| `1D` | `676.70` | 21,740,000.00 USD | 0.00 USD | 21,740,000.00 USD | 218,210.00 USD | 174,670.00 USD | 281,250.00 USD |
| `7D` | `676.90` | 21,640,000.00 USD | 0.00 USD | 21,640,000.00 USD | 2,140,000.00 USD | 428,700.00 USD | 502,410.00 USD |
| `1D` | `677.50` | 21,060,000.00 USD | 0.00 USD | 21,060,000.00 USD | 214,450.00 USD | 157,160.00 USD | 276,660.00 USD |
| `7D` | `677.90` | 18,560,000.00 USD | 0.00 USD | 18,560,000.00 USD | 752,200.00 USD | 28,030.00 USD | 484,840.00 USD |
| `1D` | `678.30` | 20,420,000.00 USD | 0.00 USD | 20,420,000.00 USD | 1,700,000.00 USD | 157,380.00 USD | 269,680.00 USD |
| `7D` | `678.90` | 17,300,000.00 USD | 0.00 USD | 17,300,000.00 USD | 244,010.00 USD | 98,010.00 USD | 43,880.00 USD |
| `1D` | `679.10` | 18,290,000.00 USD | 0.00 USD | 18,290,000.00 USD | 246,070.00 USD | 81,100.00 USD | 34,680.00 USD |
| `1D` | `679.90` | 17,920,000.00 USD | 0.00 USD | 17,920,000.00 USD | 1,550,000.00 USD | 246,160.00 USD | 298,080.00 USD |
| `7D` | `679.90` | 16,910,000.00 USD | 0.00 USD | 16,910,000.00 USD | 89,860.00 USD | 65,770.00 USD | 321,910.00 USD |
| `1D` | `680.70` | 15,830,000.00 USD | 0.00 USD | 15,830,000.00 USD | 202,340.00 USD | 126,150.00 USD | 187,330.00 USD |
| `7D` | `680.90` | 16,430,000.00 USD | 0.00 USD | 16,430,000.00 USD | 10,590.00 USD | 64,440.00 USD | 167,870.00 USD |
| `1D` | `681.50` | 15,310,000.00 USD | 0.00 USD | 15,310,000.00 USD | 565,710.00 USD | 414,700.00 USD | 0.00 USD |
| `7D` | `681.90` | 16,190,000.00 USD | 0.00 USD | 16,190,000.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `682.30` | 14,330,000.00 USD | 0.00 USD | 14,330,000.00 USD | 323,390.00 USD | 16,030.00 USD | 0.00 USD |
| `7D` | `682.90` | 14,430,000.00 USD | 0.00 USD | 14,430,000.00 USD | 39,810.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `683.10` | 13,990,000.00 USD | 0.00 USD | 13,990,000.00 USD | 662,310.00 USD | 59,430.00 USD | 37,900.00 USD |
| `1D` | `683.90` | 13,230,000.00 USD | 0.00 USD | 13,230,000.00 USD | 405,890.00 USD | 0.00 USD | 50,970.00 USD |
| `7D` | `683.90` | 14,390,000.00 USD | 0.00 USD | 14,390,000.00 USD | 77,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `684.70` | 12,780,000.00 USD | 0.00 USD | 12,780,000.00 USD | 138,250.00 USD | 58,650.00 USD | 0.00 USD |
| `7D` | `684.90` | 14,320,000.00 USD | 0.00 USD | 14,320,000.00 USD | 1,490,000.00 USD | 116,310.00 USD | 0.00 USD |
| `1D` | `685.50` | 12,580,000.00 USD | 0.00 USD | 12,580,000.00 USD | 589,300.00 USD | 32,890.00 USD | 0.00 USD |
| `7D` | `685.90` | 12,710,000.00 USD | 0.00 USD | 12,710,000.00 USD | 122,630.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `686.30` | 11,960,000.00 USD | 0.00 USD | 11,960,000.00 USD | 937,160.00 USD | 21,120.00 USD | 0.00 USD |
| `7D` | `686.90` | 12,590,000.00 USD | 0.00 USD | 12,590,000.00 USD | 53,070.00 USD | 71,560.00 USD | 0.00 USD |
| `1D` | `687.10` | 11,000,000.00 USD | 0.00 USD | 11,000,000.00 USD | 1,010,000.00 USD | 181,980.00 USD | 98,790.00 USD |
| `1D` | `687.90` | 9,710,000.00 USD | 0.00 USD | 9,710,000.00 USD | 192,040.00 USD | 75,530.00 USD | 215,930.00 USD |
| `7D` | `687.90` | 12,460,000.00 USD | 0.00 USD | 12,460,000.00 USD | 142,930.00 USD | 504,150.00 USD | 0.00 USD |
| `1D` | `688.70` | 9,230,000.00 USD | 0.00 USD | 9,230,000.00 USD | 459,070.00 USD | 107,080.00 USD | 490,120.00 USD |
| `7D` | `688.90` | 11,820,000.00 USD | 0.00 USD | 11,820,000.00 USD | 70,480.00 USD | 253,790.00 USD | 1,940,000.00 USD |
| `1D` | `689.50` | 8,170,000.00 USD | 0.00 USD | 8,170,000.00 USD | 77,980.00 USD | 37,360.00 USD | 760,670.00 USD |
| `7D` | `689.90` | 9,550,000.00 USD | 0.00 USD | 9,550,000.00 USD | 170,280.00 USD | 0.00 USD | 1,040,000.00 USD |
| `1D` | `690.30` | 7,300,000.00 USD | 0.00 USD | 7,300,000.00 USD | 31,110.00 USD | 63,780.00 USD | 212,990.00 USD |
| `7D` | `690.90` | 8,340,000.00 USD | 0.00 USD | 8,340,000.00 USD | 109,680.00 USD | 186,610.00 USD | 0.00 USD |
| `1D` | `691.10` | 6,990,000.00 USD | 0.00 USD | 6,990,000.00 USD | 0.00 USD | 129,500.00 USD | 75,210.00 USD |
| `1D` | `691.90` | 6,790,000.00 USD | 0.00 USD | 6,790,000.00 USD | 184,180.00 USD | 86,780.00 USD | 116,720.00 USD |
| `7D` | `691.90` | 8,050,000.00 USD | 0.00 USD | 8,050,000.00 USD | 67,140.00 USD | 256,450.00 USD | 1,810,000.00 USD |
| `1D` | `692.70` | 6,400,000.00 USD | 0.00 USD | 6,400,000.00 USD | 673,080.00 USD | 45,970.00 USD | 50,290.00 USD |
| `7D` | `692.90` | 5,920,000.00 USD | 0.00 USD | 5,920,000.00 USD | 803,940.00 USD | 252,070.00 USD | 87,760.00 USD |
| `1D` | `693.50` | 5,630,000.00 USD | 0.00 USD | 5,630,000.00 USD | 145,470.00 USD | 207,190.00 USD | 328,870.00 USD |
| `7D` | `693.90` | 4,770,000.00 USD | 0.00 USD | 4,770,000.00 USD | 0.00 USD | 131,550.00 USD | 317,780.00 USD |
| `1D` | `694.30` | 4,950,000.00 USD | 0.00 USD | 4,950,000.00 USD | 174,860.00 USD | 117,630.00 USD | 180,380.00 USD |
| `7D` | `694.90` | 4,320,000.00 USD | 0.00 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 661,790.00 USD |
| `1D` | `695.10` | 4,470,000.00 USD | 0.00 USD | 4,470,000.00 USD | 306,060.00 USD | 64,240.00 USD | 175,000.00 USD |
| `1D` | `695.90` | 3,930,000.00 USD | 0.00 USD | 3,930,000.00 USD | 153,900.00 USD | 34,140.00 USD | 0.00 USD |
| `7D` | `695.90` | 3,660,000.00 USD | 0.00 USD | 3,660,000.00 USD | 0.00 USD | 128,880.00 USD | 0.00 USD |
| `1D` | `696.70` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 0.00 USD | 95,780.00 USD | 0.00 USD |
| `1D` | `698.30` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 479,860.00 USD | 0.00 USD | 24,380.00 USD |
| `7D` | `698.90` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 575,930.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `699.10` | 3,140,000.00 USD | 0.00 USD | 3,140,000.00 USD | 0.00 USD | 31,670.00 USD | 42,650.00 USD |
| `1D` | `699.90` | 3,070,000.00 USD | 0.00 USD | 3,070,000.00 USD | 134,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `700.70` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 190,120.00 USD | 42,240.00 USD | 0.00 USD |
| `7D` | `700.90` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 0.00 USD | 72,960.00 USD | 0.00 USD |
| `1D` | `701.50` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 207,370.00 USD | 222,670.00 USD | 0.00 USD |
| `7D` | `701.90` | 2,880,000.00 USD | 0.00 USD | 2,880,000.00 USD | 0.00 USD | 190,950.00 USD | 0.00 USD |
| `1D` | `702.30` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 384,090.00 USD | 98,960.00 USD | 138,960.00 USD |
| `7D` | `702.90` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 0.00 USD | 114,370.00 USD | 0.00 USD |
| `1D` | `703.10` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 512,150.00 USD | 58,910.00 USD | 298,770.00 USD |
| `1D` | `703.90` | 778,100.00 USD | 0.00 USD | 778,100.00 USD | 155,960.00 USD | 12,800.00 USD | 376,910.00 USD |
| `7D` | `703.90` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 1,030,000.00 USD |
| `1D` | `704.70` | 232,430.00 USD | 0.00 USD | 232,430.00 USD | 62,230.00 USD | 23,130.00 USD | 147,070.00 USD |
| `7D` | `704.90` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `705.20` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `705.50` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `706.30` | 121,180.00 USD | 121,180.00 USD | 0.00 USD | 121,180.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `709.90` | 677,910.00 USD | 677,910.00 USD | 0.00 USD | 677,910.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `711.10` | 560,620.00 USD | 560,620.00 USD | 0.00 USD | 401,530.00 USD | 0.00 USD | 37,900.00 USD |
| `1D` | `711.90` | 850,080.00 USD | 850,080.00 USD | 0.00 USD | 250,690.00 USD | 0.00 USD | 38,770.00 USD |
| `7D` | `712.90` | 794,220.00 USD | 794,220.00 USD | 0.00 USD | 0.00 USD | 116,310.00 USD | 0.00 USD |
| `1D` | `715.10` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 415,380.00 USD |
| `1D` | `715.90` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 917,170.00 USD |
| `7D` | `718.90` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 775,390.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `719.10` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 82,030.00 USD | 36,390.00 USD |
| `1D` | `719.90` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 244,770.00 USD | 71,280.00 USD | 104,480.00 USD |
| `7D` | `719.90` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 0.00 USD | 256,450.00 USD | 1,810,000.00 USD |
| `1D` | `720.70` | 3,920,000.00 USD | 3,920,000.00 USD | 0.00 USD | 881,010.00 USD | 250,840.00 USD | 69,760.00 USD |
| `7D` | `720.90` | 4,670,000.00 USD | 4,670,000.00 USD | 0.00 USD | 803,940.00 USD | 146,010.00 USD | 87,760.00 USD |
| `1D` | `721.50` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 174,820.00 USD | 240,840.00 USD | 127,470.00 USD |
| `7D` | `721.90` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 0.00 USD | 106,060.00 USD | 317,780.00 USD |
| `1D` | `722.30` | 5,260,000.00 USD | 5,260,000.00 USD | 0.00 USD | 274,310.00 USD | 123,420.00 USD | 391,200.00 USD |
| `7D` | `722.90` | 5,550,000.00 USD | 5,550,000.00 USD | 0.00 USD | 0.00 USD | 131,550.00 USD | 326,040.00 USD |
| `1D` | `723.10` | 5,970,000.00 USD | 5,970,000.00 USD | 0.00 USD | 257,560.00 USD | 283,040.00 USD | 176,360.00 USD |
| `1D` | `723.90` | 6,800,000.00 USD | 6,800,000.00 USD | 0.00 USD | 380,140.00 USD | 359,630.00 USD | 88,480.00 USD |
| `7D` | `723.90` | 6,820,000.00 USD | 6,820,000.00 USD | 0.00 USD | 806,150.00 USD | 128,880.00 USD | 335,740.00 USD |
| `1D` | `724.70` | 7,350,000.00 USD | 7,350,000.00 USD | 0.00 USD | 498,970.00 USD | 45,850.00 USD | 0.00 USD |
| `1D` | `725.50` | 7,790,000.00 USD | 7,790,000.00 USD | 0.00 USD | 289,330.00 USD | 120,790.00 USD | 38,340.00 USD |
| `7D` | `725.90` | 7,950,000.00 USD | 7,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,120,000.00 USD |
| `1D` | `726.30` | 8,060,000.00 USD | 8,060,000.00 USD | 0.00 USD | 256,420.00 USD | 10,760.00 USD | 0.00 USD |
| `7D` | `726.90` | 8,560,000.00 USD | 8,560,000.00 USD | 0.00 USD | 552,080.00 USD | 58,160.00 USD | 0.00 USD |
| `1D` | `727.10` | 8,660,000.00 USD | 8,660,000.00 USD | 0.00 USD | 502,440.00 USD | 75,120.00 USD | 24,380.00 USD |
| `1D` | `727.90` | 8,850,000.00 USD | 8,850,000.00 USD | 0.00 USD | 136,640.00 USD | 48,110.00 USD | 0.00 USD |
| `7D` | `727.90` | 9,970,000.00 USD | 9,970,000.00 USD | 0.00 USD | 575,930.00 USD | 201,080.00 USD | 639,380.00 USD |
| `1D` | `728.70` | 9,470,000.00 USD | 9,470,000.00 USD | 0.00 USD | 369,860.00 USD | 48,340.00 USD | 207,690.00 USD |
| `7D` | `728.90` | 11,450,000.00 USD | 11,450,000.00 USD | 0.00 USD | 1,360,000.00 USD | 125,070.00 USD | 0.00 USD |
| `1D` | `729.50` | 10,400,000.00 USD | 10,400,000.00 USD | 0.00 USD | 171,580.00 USD | 295,150.00 USD | 458,580.00 USD |
| `7D` | `729.90` | 11,820,000.00 USD | 11,820,000.00 USD | 0.00 USD | 0.00 USD | 365,010.00 USD | 0.00 USD |
| `1D` | `730.30` | 12,980,000.00 USD | 12,980,000.00 USD | 0.00 USD | 1,950,000.00 USD | 459,490.00 USD | 176,680.00 USD |
| `7D` | `730.90` | 12,480,000.00 USD | 12,480,000.00 USD | 0.00 USD | 127,820.00 USD | 219,090.00 USD | 313,360.00 USD |
| `1D` | `731.10` | 16,940,000.00 USD | 16,940,000.00 USD | 0.00 USD | 1,600,000.00 USD | 156,290.00 USD | 2,200,000.00 USD |
| `1D` | `731.90` | 17,800,000.00 USD | 17,800,000.00 USD | 0.00 USD | 206,640.00 USD | 152,280.00 USD | 502,920.00 USD |
| `7D` | `731.90` | 14,180,000.00 USD | 14,180,000.00 USD | 0.00 USD | 0.00 USD | 114,370.00 USD | 1,580,000.00 USD |
| `1D` | `732.70` | 20,780,000.00 USD | 20,780,000.00 USD | 0.00 USD | 1,610,000.00 USD | 119,840.00 USD | 1,250,000.00 USD |
| `7D` | `732.90` | 14,630,000.00 USD | 14,630,000.00 USD | 0.00 USD | 0.00 USD | 93,300.00 USD | 363,490.00 USD |
| `1D` | `733.50` | 21,520,000.00 USD | 21,520,000.00 USD | 0.00 USD | 62,230.00 USD | 317,290.00 USD | 363,600.00 USD |
| `7D` | `733.90` | 15,790,000.00 USD | 15,790,000.00 USD | 0.00 USD | 123,040.00 USD | 128,230.00 USD | 903,260.00 USD |
| `1D` | `734.30` | 22,500,000.00 USD | 22,500,000.00 USD | 0.00 USD | 735,390.00 USD | 43,390.00 USD | 200,410.00 USD |
| `7D` | `734.90` | 16,320,000.00 USD | 16,320,000.00 USD | 0.00 USD | 456,850.00 USD | 73,000.00 USD | 0.00 USD |
| `1D` | `735.10` | 23,370,000.00 USD | 23,370,000.00 USD | 0.00 USD | 656,080.00 USD | 197,510.00 USD | 16,020.00 USD |
| `1D` | `735.90` | 24,900,000.00 USD | 24,900,000.00 USD | 0.00 USD | 642,960.00 USD | 131,120.00 USD | 755,360.00 USD |
| `7D` | `735.90` | 16,660,000.00 USD | 16,660,000.00 USD | 0.00 USD | 90,800.00 USD | 53,030.00 USD | 202,770.00 USD |
| `1D` | `736.70` | 25,410,000.00 USD | 25,410,000.00 USD | 0.00 USD | 366,260.00 USD | 58,820.00 USD | 90,190.00 USD |
| `7D` | `736.90` | 17,070,000.00 USD | 17,070,000.00 USD | 0.00 USD | 176,450.00 USD | 65,770.00 USD | 163,020.00 USD |
| `1D` | `737.50` | 26,040,000.00 USD | 26,040,000.00 USD | 0.00 USD | 409,970.00 USD | 126,150.00 USD | 87,500.00 USD |
| `7D` | `737.90` | 17,300,000.00 USD | 17,300,000.00 USD | 0.00 USD | 0.00 USD | 64,440.00 USD | 167,870.00 USD |
| `1D` | `738.30` | 26,590,000.00 USD | 26,590,000.00 USD | 0.00 USD | 466,620.00 USD | 85,790.00 USD | 0.00 USD |
| `7D` | `738.90` | 18,170,000.00 USD | 18,170,000.00 USD | 0.00 USD | 0.00 USD | 166,070.00 USD | 703,580.00 USD |
| `1D` | `739.10` | 27,700,000.00 USD | 27,700,000.00 USD | 0.00 USD | 157,860.00 USD | 16,030.00 USD | 934,700.00 USD |
| `1D` | `739.90` | 27,920,000.00 USD | 27,920,000.00 USD | 0.00 USD | 187,730.00 USD | 31,860.00 USD | 0.00 USD |
| `7D` | `739.90` | 19,980,000.00 USD | 19,980,000.00 USD | 0.00 USD | 1,180,000.00 USD | 0.00 USD | 626,320.00 USD |
| `1D` | `740.70` | 28,340,000.00 USD | 28,340,000.00 USD | 0.00 USD | 246,020.00 USD | 166,390.00 USD | 12,190.00 USD |
| `7D` | `740.90` | 21,190,000.00 USD | 21,190,000.00 USD | 0.00 USD | 1,180,000.00 USD | 0.00 USD | 33,390.00 USD |
| `1D` | `741.50` | 28,970,000.00 USD | 28,970,000.00 USD | 0.00 USD | 622,710.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `741.90` | 21,810,000.00 USD | 21,810,000.00 USD | 0.00 USD | 287,970.00 USD | 100,540.00 USD | 230,050.00 USD |
| `1D` | `742.30` | 29,040,000.00 USD | 29,040,000.00 USD | 0.00 USD | 56,310.00 USD | 15,840.00 USD | 0.00 USD |
| `7D` | `742.90` | 22,460,000.00 USD | 22,460,000.00 USD | 0.00 USD | 485,340.00 USD | 0.00 USD | 162,460.00 USD |
| `1D` | `743.10` | 29,370,000.00 USD | 29,370,000.00 USD | 0.00 USD | 317,640.00 USD | 15,660.00 USD | 0.00 USD |
| `1D` | `743.90` | 29,950,000.00 USD | 29,950,000.00 USD | 0.00 USD | 16,710.00 USD | 129,570.00 USD | 436,560.00 USD |
| `7D` | `743.90` | 23,010,000.00 USD | 23,010,000.00 USD | 0.00 USD | 160,880.00 USD | 194,060.00 USD | 199,370.00 USD |
| `1D` | `744.70` | 31,970,000.00 USD | 31,970,000.00 USD | 0.00 USD | 1,040,000.00 USD | 111,890.00 USD | 871,710.00 USD |
| `7D` | `744.90` | 23,260,000.00 USD | 23,260,000.00 USD | 0.00 USD | 0.00 USD | 244,460.00 USD | 0.00 USD |
| `1D` | `745.50` | 32,870,000.00 USD | 32,870,000.00 USD | 0.00 USD | 713,060.00 USD | 106,000.00 USD | 78,560.00 USD |
| `7D` | `745.90` | 23,710,000.00 USD | 23,710,000.00 USD | 0.00 USD | 396,930.00 USD | 57,190.00 USD | 0.00 USD |
| `1D` | `746.30` | 33,600,000.00 USD | 33,600,000.00 USD | 0.00 USD | 451,300.00 USD | 61,130.00 USD | 219,610.00 USD |
| `7D` | `746.90` | 24,980,000.00 USD | 24,980,000.00 USD | 0.00 USD | 324,750.00 USD | 0.00 USD | 948,960.00 USD |
| `1D` | `747.10` | 35,080,000.00 USD | 35,080,000.00 USD | 0.00 USD | 521,800.00 USD | 74,380.00 USD | 881,280.00 USD |
| `1D` | `747.90` | 35,460,000.00 USD | 35,460,000.00 USD | 0.00 USD | 163,850.00 USD | 84,260.00 USD | 133,250.00 USD |
| `1D` | `748.70` | 35,880,000.00 USD | 35,880,000.00 USD | 0.00 USD | 404,050.00 USD | 0.00 USD | 17,880.00 USD |
| `7D` | `748.90` | 25,380,000.00 USD | 25,380,000.00 USD | 0.00 USD | 337,680.00 USD | 61,650.00 USD | 0.00 USD |
| `1D` | `749.50` | 36,290,000.00 USD | 36,290,000.00 USD | 0.00 USD | 406,170.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `749.90` | 25,790,000.00 USD | 25,790,000.00 USD | 0.00 USD | 404,760.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `750.30` | 36,380,000.00 USD | 36,380,000.00 USD | 0.00 USD | 92,750.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `750.90` | 25,860,000.00 USD | 25,860,000.00 USD | 0.00 USD | 70,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `751.10` | 36,470,000.00 USD | 36,470,000.00 USD | 0.00 USD | 88,760.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `751.90` | 37,020,000.00 USD | 37,020,000.00 USD | 0.00 USD | 86,270.00 USD | 25,010.00 USD | 433,820.00 USD |
| `7D` | `751.90` | 25,960,000.00 USD | 25,960,000.00 USD | 0.00 USD | 105,420.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `752.70` | 37,470,000.00 USD | 37,470,000.00 USD | 0.00 USD | 349,490.00 USD | 0.00 USD | 105,800.00 USD |
| `7D` | `752.90` | 26,320,000.00 USD | 26,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 351,790.00 USD |
| `1D` | `753.50` | 37,900,000.00 USD | 37,900,000.00 USD | 0.00 USD | 158,100.00 USD | 3,810.00 USD | 262,160.00 USD |
| `7D` | `753.90` | 26,840,000.00 USD | 26,840,000.00 USD | 0.00 USD | 406,900.00 USD | 83,030.00 USD | 33,430.00 USD |
| `1D` | `754.30` | 38,450,000.00 USD | 38,450,000.00 USD | 0.00 USD | 438,760.00 USD | 70,850.00 USD | 43,990.00 USD |
| `7D` | `754.90` | 26,900,000.00 USD | 26,900,000.00 USD | 0.00 USD | 0.00 USD | 59,560.00 USD | 0.00 USD |
| `1D` | `755.10` | 38,840,000.00 USD | 38,840,000.00 USD | 0.00 USD | 157,340.00 USD | 192,190.00 USD | 37,120.00 USD |
| `1D` | `755.90` | 39,540,000.00 USD | 39,540,000.00 USD | 0.00 USD | 576,050.00 USD | 62,280.00 USD | 66,220.00 USD |
| `7D` | `755.90` | 27,020,000.00 USD | 27,020,000.00 USD | 0.00 USD | 120,600.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `756.70` | 39,700,000.00 USD | 39,700,000.00 USD | 0.00 USD | 87,170.00 USD | 24,970.00 USD | 49,060.00 USD |
| `7D` | `756.90` | 27,180,000.00 USD | 27,180,000.00 USD | 0.00 USD | 0.00 USD | 160,580.00 USD | 0.00 USD |
| `1D` | `757.50` | 40,110,000.00 USD | 40,110,000.00 USD | 0.00 USD | 198,850.00 USD | 179,910.00 USD | 32,720.00 USD |
| `7D` | `757.90` | 27,660,000.00 USD | 27,660,000.00 USD | 0.00 USD | 475,510.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `758.30` | 41,120,000.00 USD | 41,120,000.00 USD | 0.00 USD | 757,140.00 USD | 34,450.00 USD | 218,280.00 USD |
| `7D` | `758.90` | 29,160,000.00 USD | 29,160,000.00 USD | 0.00 USD | 1,190,000.00 USD | 55,460.00 USD | 265,620.00 USD |
| `1D` | `759.10` | 42,160,000.00 USD | 42,160,000.00 USD | 0.00 USD | 861,530.00 USD | 117,910.00 USD | 54,810.00 USD |
| `1D` | `759.90` | 42,530,000.00 USD | 42,530,000.00 USD | 0.00 USD | 335,910.00 USD | 21,070.00 USD | 15,370.00 USD |
| `7D` | `759.90` | 29,520,000.00 USD | 29,520,000.00 USD | 0.00 USD | 310,160.00 USD | 0.00 USD | 42,540.00 USD |
| `1D` | `760.70` | 42,940,000.00 USD | 42,940,000.00 USD | 0.00 USD | 308,190.00 USD | 52,630.00 USD | 53,580.00 USD |
| `7D` | `760.90` | 29,870,000.00 USD | 29,870,000.00 USD | 0.00 USD | 264,540.00 USD | 27,650.00 USD | 61,350.00 USD |
| `1D` | `761.50` | 43,910,000.00 USD | 43,910,000.00 USD | 0.00 USD | 720,170.00 USD | 8,690.00 USD | 232,870.00 USD |
| `7D` | `761.90` | 30,490,000.00 USD | 30,490,000.00 USD | 0.00 USD | 46,720.00 USD | 282,090.00 USD | 288,600.00 USD |
| `1D` | `762.30` | 44,260,000.00 USD | 44,260,000.00 USD | 0.00 USD | 128,330.00 USD | 124,370.00 USD | 98,750.00 USD |
| `7D` | `762.90` | 32,530,000.00 USD | 32,530,000.00 USD | 0.00 USD | 1,290,000.00 USD | 427,600.00 USD | 324,830.00 USD |
| `1D` | `763.10` | 46,870,000.00 USD | 46,870,000.00 USD | 0.00 USD | 1,940,000.00 USD | 142,770.00 USD | 523,900.00 USD |
| `1D` | `763.90` | 47,960,000.00 USD | 47,960,000.00 USD | 0.00 USD | 890,720.00 USD | 68,590.00 USD | 131,440.00 USD |
| `7D` | `763.90` | 35,570,000.00 USD | 35,570,000.00 USD | 0.00 USD | 2,260,000.00 USD | 329,860.00 USD | 450,710.00 USD |
| `1D` | `764.70` | 48,940,000.00 USD | 48,940,000.00 USD | 0.00 USD | 687,580.00 USD | 147,600.00 USD | 146,710.00 USD |
| `7D` | `764.90` | 37,480,000.00 USD | 37,480,000.00 USD | 0.00 USD | 1,250,000.00 USD | 308,520.00 USD | 346,190.00 USD |
| `1D` | `765.50` | 49,340,000.00 USD | 49,340,000.00 USD | 0.00 USD | 217,860.00 USD | 62,870.00 USD | 118,800.00 USD |
| `7D` | `765.90` | 40,850,000.00 USD | 40,850,000.00 USD | 0.00 USD | 2,560,000.00 USD | 228,800.00 USD | 585,320.00 USD |
| `1D` | `766.30` | 50,360,000.00 USD | 50,360,000.00 USD | 0.00 USD | 652,360.00 USD | 146,240.00 USD | 220,700.00 USD |
| `7D` | `766.90` | 45,470,000.00 USD | 45,470,000.00 USD | 0.00 USD | 3,530,000.00 USD | 285,740.00 USD | 801,480.00 USD |
| `1D` | `767.10` | 51,780,000.00 USD | 51,780,000.00 USD | 0.00 USD | 1,230,000.00 USD | 21,380.00 USD | 166,180.00 USD |
| `1D` | `767.90` | 52,880,000.00 USD | 52,880,000.00 USD | 0.00 USD | 851,190.00 USD | 39,510.00 USD | 207,920.00 USD |
| `7D` | `767.90` | 49,710,000.00 USD | 49,710,000.00 USD | 0.00 USD | 3,510,000.00 USD | 173,810.00 USD | 557,450.00 USD |
| `1D` | `768.70` | 53,300,000.00 USD | 53,300,000.00 USD | 0.00 USD | 380,150.00 USD | 25,300.00 USD | 20,190.00 USD |
| `7D` | `768.90` | 51,290,000.00 USD | 51,290,000.00 USD | 0.00 USD | 1,050,000.00 USD | 92,840.00 USD | 436,370.00 USD |
| `1D` | `769.50` | 53,640,000.00 USD | 53,640,000.00 USD | 0.00 USD | 285,410.00 USD | 44,280.00 USD | 8,460.00 USD |
| `7D` | `769.90` | 53,330,000.00 USD | 53,330,000.00 USD | 0.00 USD | 1,240,000.00 USD | 322,290.00 USD | 486,170.00 USD |
| `1D` | `770.30` | 53,820,000.00 USD | 53,820,000.00 USD | 0.00 USD | 82,200.00 USD | 66,110.00 USD | 28,450.00 USD |
| `7D` | `770.90` | 55,620,000.00 USD | 55,620,000.00 USD | 0.00 USD | 1,860,000.00 USD | 259,380.00 USD | 170,990.00 USD |
| `1D` | `771.10` | 54,390,000.00 USD | 54,390,000.00 USD | 0.00 USD | 156,280.00 USD | 56,560.00 USD | 361,060.00 USD |
| `1D` | `771.90` | 55,180,000.00 USD | 55,180,000.00 USD | 0.00 USD | 140,150.00 USD | 70,310.00 USD | 582,120.00 USD |
| `7D` | `771.90` | 58,460,000.00 USD | 58,460,000.00 USD | 0.00 USD | 2,000,000.00 USD | 431,660.00 USD | 411,300.00 USD |
| `1D` | `772.70` | 55,550,000.00 USD | 55,550,000.00 USD | 0.00 USD | 221,230.00 USD | 134,200.00 USD | 16,360.00 USD |
| `7D` | `772.90` | 61,480,000.00 USD | 61,480,000.00 USD | 0.00 USD | 2,310,000.00 USD | 316,340.00 USD | 397,820.00 USD |
| `1D` | `773.50` | 56,250,000.00 USD | 56,250,000.00 USD | 0.00 USD | 618,270.00 USD | 12,950.00 USD | 68,320.00 USD |
| `7D` | `773.90` | 63,280,000.00 USD | 63,280,000.00 USD | 0.00 USD | 1,220,000.00 USD | 270,430.00 USD | 304,680.00 USD |
| `1D` | `774.30` | 56,850,000.00 USD | 56,850,000.00 USD | 0.00 USD | 583,550.00 USD | 11,780.00 USD | 1,360.00 USD |
| `7D` | `774.90` | 65,430,000.00 USD | 65,430,000.00 USD | 0.00 USD | 1,140,000.00 USD | 515,010.00 USD | 490,500.00 USD |
| `1D` | `775.10` | 57,040,000.00 USD | 57,040,000.00 USD | 0.00 USD | 67,380.00 USD | 34,120.00 USD | 86,160.00 USD |
| `1D` | `775.90` | 57,220,000.00 USD | 57,220,000.00 USD | 0.00 USD | 98,960.00 USD | 24,070.00 USD | 56,400.00 USD |
| `7D` | `775.90` | 67,690,000.00 USD | 67,690,000.00 USD | 0.00 USD | 1,670,000.00 USD | 274,120.00 USD | 316,370.00 USD |
| `1D` | `776.70` | 57,580,000.00 USD | 57,580,000.00 USD | 0.00 USD | 253,970.00 USD | 13,880.00 USD | 92,290.00 USD |
| `7D` | `776.90` | 69,280,000.00 USD | 69,280,000.00 USD | 0.00 USD | 1,370,000.00 USD | 106,550.00 USD | 115,990.00 USD |
| `1D` | `777.50` | 58,240,000.00 USD | 58,240,000.00 USD | 0.00 USD | 510,620.00 USD | 112,090.00 USD | 36,270.00 USD |
| `7D` | `777.90` | 71,190,000.00 USD | 71,190,000.00 USD | 0.00 USD | 1,470,000.00 USD | 240,260.00 USD | 196,170.00 USD |
| `1D` | `778.30` | 59,340,000.00 USD | 59,340,000.00 USD | 0.00 USD | 683,420.00 USD | 72,880.00 USD | 346,050.00 USD |
| `7D` | `778.90` | 72,450,000.00 USD | 72,450,000.00 USD | 0.00 USD | 994,320.00 USD | 117,290.00 USD | 152,370.00 USD |
| `1D` | `779.10` | 60,070,000.00 USD | 60,070,000.00 USD | 0.00 USD | 620,220.00 USD | 33,020.00 USD | 77,130.00 USD |
| `1D` | `779.90` | 60,260,000.00 USD | 60,260,000.00 USD | 0.00 USD | 75,250.00 USD | 75,710.00 USD | 37,410.00 USD |
| `7D` | `779.90` | 73,470,000.00 USD | 73,470,000.00 USD | 0.00 USD | 758,640.00 USD | 125,670.00 USD | 135,630.00 USD |
| `1D` | `780.70` | 60,570,000.00 USD | 60,570,000.00 USD | 0.00 USD | 203,640.00 USD | 32,870.00 USD | 70,080.00 USD |
| `7D` | `780.90` | 75,020,000.00 USD | 75,020,000.00 USD | 0.00 USD | 1,220,000.00 USD | 93,770.00 USD | 240,340.00 USD |
| `1D` | `781.50` | 61,040,000.00 USD | 61,040,000.00 USD | 0.00 USD | 286,730.00 USD | 66,560.00 USD | 121,700.00 USD |
| `7D` | `781.90` | 77,320,000.00 USD | 77,320,000.00 USD | 0.00 USD | 1,790,000.00 USD | 118,390.00 USD | 386,440.00 USD |
| `1D` | `782.30` | 61,830,000.00 USD | 61,830,000.00 USD | 0.00 USD | 562,770.00 USD | 6,820.00 USD | 224,210.00 USD |
| `7D` | `782.90` | 79,620,000.00 USD | 79,620,000.00 USD | 0.00 USD | 1,840,000.00 USD | 36,140.00 USD | 427,460.00 USD |
| `1D` | `783.10` | 62,350,000.00 USD | 62,350,000.00 USD | 0.00 USD | 438,920.00 USD | 18,800.00 USD | 61,360.00 USD |
| `1D` | `783.90` | 62,470,000.00 USD | 62,470,000.00 USD | 0.00 USD | 115,530.00 USD | 0.00 USD | 4,880.00 USD |
| `7D` | `783.90` | 80,120,000.00 USD | 80,120,000.00 USD | 0.00 USD | 437,000.00 USD | 10,100.00 USD | 54,380.00 USD |
| `1D` | `784.70` | 62,790,000.00 USD | 62,790,000.00 USD | 0.00 USD | 315,460.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `784.90` | 80,720,000.00 USD | 80,720,000.00 USD | 0.00 USD | 424,680.00 USD | 81,720.00 USD | 92,590.00 USD |
| `1D` | `785.50` | 62,890,000.00 USD | 62,890,000.00 USD | 0.00 USD | 96,290.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `785.90` | 81,760,000.00 USD | 81,760,000.00 USD | 0.00 USD | 932,150.00 USD | 60,930.00 USD | 48,900.00 USD |
| `1D` | `786.30` | 62,980,000.00 USD | 62,980,000.00 USD | 0.00 USD | 85,400.00 USD | 6,260.00 USD | 0.00 USD |
| `7D` | `786.90` | 82,500,000.00 USD | 82,500,000.00 USD | 0.00 USD | 601,980.00 USD | 28,250.00 USD | 104,290.00 USD |
| `1D` | `787.10` | 63,030,000.00 USD | 63,030,000.00 USD | 0.00 USD | 39,820.00 USD | 16,940.00 USD | 0.00 USD |
| `1D` | `787.90` | 63,770,000.00 USD | 63,770,000.00 USD | 0.00 USD | 373,310.00 USD | 24,670.00 USD | 341,610.00 USD |
| `7D` | `787.90` | 82,910,000.00 USD | 82,910,000.00 USD | 0.00 USD | 261,000.00 USD | 56,730.00 USD | 91,960.00 USD |
| `1D` | `788.60` | 63,810,000.00 USD | 63,810,000.00 USD | 0.00 USD | 38,270.00 USD | 0.00 USD | 0.00 USD |
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
  * Total Open Interest: `1.29B` | Total OI Tokens: `1,828,435.5 BNB`
  * 1h OI Change: `-0.73%` | 4h OI Change: `-2.33%` | 24h OI Change: `+1.83%`
  * Exchange Breakdown: Binance=`563.00M` | Bybit=`134.81M` | OKX=`64.62M` | Hyperliquid=`68.50M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-93.46K` | Last 24h: `-160.49K` | Last 3d: `35.49K` | Last 7d: `220.92K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0000%` | **USDT OKX** | `-0.0407%` |
| **USDT Bybit** | `-0.0518%` | **USDT KuCoin** | `-0.0070%` |
| **USDT MEXC** | `0.0000%` | **USDT BingX** | `-0.0458%` |
| **USDT Gate** | `-0.0036%` | **USDT Bitget** | `-0.0211%` |
| **CoinM Binance** | `0.0509%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `BNB` | `50.04%` | `49.96%` | `1.00` | 48,520,000.00 USD |
| `15M` | `Binance` | `45.35%` | `54.65%` | `0.83` | 11,230,000.00 USD |
| `15M` | `OKX` | `62.65%` | `37.35%` | `1.68` | 8,530,000.00 USD |
| `15M` | `Bybit` | `43.72%` | `56.28%` | `0.78` | 2,740,000.00 USD |
| `15M` | `KuCoin` | `46.94%` | `53.06%` | `0.88` | 239,880.00 USD |
| `15M` | `Gate` | `55.49%` | `44.51%` | `1.25` | 3,170,000.00 USD |
| `15M` | `Bitget` | `35.47%` | `64.53%` | `0.55` | 1,550,000.00 USD |
| `15M` | `BingX` | `46.67%` | `53.33%` | `0.88` | 1,990,000.00 USD |
| `15M` | `MEXC` | `54.88%` | `45.12%` | `1.22` | 9,330,000.00 USD |
| `15M` | `Bitunix` | `45.44%` | `54.56%` | `0.83` | 1,910,000.00 USD |
| `15M` | `Hyperliquid` | `41.41%` | `58.59%` | `0.71` | 3,000,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `48.83%` | `51.17%` | `0.95` | 3,150,000.00 USD |
| `15M` | `Crypto.com` | `39.58%` | `60.42%` | `0.66` | 141,110.00 USD |
| `15M` | `WhiteBIT` | `26.31%` | `73.69%` | `0.36` | 384,680.00 USD |
| `15M` | `HTX` | `23.79%` | `76.21%` | `0.31` | 76,400.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `20.35%` | `79.65%` | `0.26` | 564,640.00 USD |
| `15M` | `Aster` | `42.96%` | `57.04%` | `0.75` | 300,540.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `50.64%` | `49.36%` | `1.03` | 211,630.00 USD |
| `15M` | `Whale Positions` | `45.35%` | `54.65%` | `0.83` | 11,230,000.00 USD |
| `15M` | `Global Accounts` | `50.04%` | `49.96%` | `1.00` | 48,520,000.00 USD |
| `1H` | `BNB` | `48.48%` | `51.52%` | `0.94` | 2,220,000,000.00 USD |
| `1H` | `Binance` | `47.9%` | `52.1%` | `0.92` | 702,760,000.00 USD |
| `1H` | `OKX` | `49.68%` | `50.32%` | `0.99` | 372,530,000.00 USD |
| `1H` | `Bybit` | `40.12%` | `59.88%` | `0.67` | 128,780,000.00 USD |
| `1H` | `KuCoin` | `43.79%` | `56.21%` | `0.78` | 8,090,000.00 USD |
| `1H` | `Gate` | `48.44%` | `51.56%` | `0.94` | 336,570,000.00 USD |
| `1H` | `Bitget` | `47.76%` | `52.24%` | `0.91` | 72,240,000.00 USD |
| `1H` | `BingX` | `47.74%` | `52.26%` | `0.91` | 19,600,000.00 USD |
| `1H` | `MEXC` | `48.62%` | `51.38%` | `0.95` | 77,050,000.00 USD |
| `1H` | `Bitunix` | `51.78%` | `48.22%` | `1.07` | 68,610,000.00 USD |
| `1H` | `Hyperliquid` | `27.69%` | `72.31%` | `0.38` | 142,320,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `48.06%` | `51.94%` | `0.93` | 20,270,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `71.9%` | `28.1%` | `2.56` | 171,030,000.00 USD |
| `1H` | `HTX` | `35.49%` | `64.51%` | `0.55` | 23,510,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `47.54%` | `52.46%` | `0.91` | 28,500,000.00 USD |
| `1H` | `Bitfinex` | `43.23%` | `56.77%` | `0.76` | 790,130.00 USD |
| `1H` | `Kraken` | `53.95%` | `46.05%` | `1.17` | 5,750,000.00 USD |
| `1H` | `Aster` | `48.59%` | `51.41%` | `0.95` | 16,790,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `55.25%` | `44.75%` | `1.23` | 26,460,000.00 USD |
| `1H` | `Whale Positions` | `47.9%` | `52.1%` | `0.92` | 702,760,000.00 USD |
| `1H` | `Global Accounts` | `48.48%` | `51.52%` | `0.94` | 2,220,000,000.00 USD |
| `4H` | `BNB` | `46.75%` | `53.25%` | `0.88` | 9,880,000,000.00 USD |
| `4H` | `Binance` | `45.01%` | `54.99%` | `0.82` | 3,060,000,000.00 USD |
| `4H` | `OKX` | `47.44%` | `52.56%` | `0.90` | 1,430,000,000.00 USD |
| `4H` | `Bybit` | `46.52%` | `53.48%` | `0.87` | 843,140,000.00 USD |
| `4H` | `KuCoin` | `52.64%` | `47.36%` | `1.11` | 23,160,000.00 USD |
| `4H` | `Gate` | `49.3%` | `50.7%` | `0.97` | 1,000,000,000.00 USD |
| `4H` | `Bitget` | `46.52%` | `53.48%` | `0.87` | 481,090,000.00 USD |
| `4H` | `BingX` | `40.1%` | `59.9%` | `0.67` | 177,090,000.00 USD |
| `4H` | `MEXC` | `44.11%` | `55.89%` | `0.79` | 411,190,000.00 USD |
| `4H` | `Bitunix` | `44.47%` | `55.53%` | `0.80` | 363,720,000.00 USD |
| `4H` | `Hyperliquid` | `36.31%` | `63.69%` | `0.57` | 495,420,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.76%` | `49.24%` | `1.03` | 677,380,000.00 USD |
| `4H` | `Crypto.com` | `46.55%` | `53.45%` | `0.87` | 27,930,000.00 USD |
| `4H` | `WhiteBIT` | `66.55%` | `33.45%` | `1.99` | 197,780,000.00 USD |
| `4H` | `HTX` | `46.68%` | `53.32%` | `0.88` | 35,640,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `51.63%` | `48.37%` | `1.07` | 423,770,000.00 USD |
| `4H` | `Bitfinex` | `35.27%` | `64.73%` | `0.54` | 5,490,000.00 USD |
| `4H` | `Kraken` | `63.02%` | `36.98%` | `1.70` | 9,950,000.00 USD |
| `4H` | `Aster` | `54.36%` | `45.64%` | `1.19` | 94,090,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `53.18%` | `46.82%` | `1.14` | 115,480,000.00 USD |
| `4H` | `Whale Positions` | `45.01%` | `54.99%` | `0.82` | 3,060,000,000.00 USD |
| `4H` | `Global Accounts` | `46.75%` | `53.25%` | `0.88` | 9,880,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `714.75` | `715.73` | `714.75` | `717.45` | `714.45` | 5,381,694.04 USD | 1,484,466.15 USD | 3,897,227.89 USD | -2,412,761.74 USD | `-44.83%` | `0B / 2S` |
| `5:00 UTC` | `714.45` | `714.97` | `714.45` | `715.95` | `714.15` | 4,744,759.02 USD | 1,432,065.49 USD | 3,312,693.53 USD | -1,880,628.03 USD | `-39.64%` | `0B / 3S` |
| `0:00 UTC` | `715.65` | `715.06` | `715.65` | `715.95` | `714.15` | 8,426,556.65 USD | 1,415,418.26 USD | 7,011,138.39 USD | -5,595,720.13 USD | `-66.41%` | `0B / 4S` |
| `5:00 UTC` | `714.15` | `713.37` | `714.15` | `714.45` | `711.75` | 6,200,853.08 USD | 1,812,683.15 USD | 4,388,169.93 USD | -2,575,486.78 USD | `-41.53%` | `0B / 5S` |
| `0:00 UTC` | `707.55` | `709.41` | `707.55` | `712.65` | `707.25` | 17,460,360.59 USD | 7,319,853.16 USD | 10,140,507.43 USD | -2,820,654.27 USD | `-16.15%` | `0B / 5S` |
| `5:00 UTC` | `706.65` | `707.24` | `706.65` | `708.75` | `705.75` | 12,869,917.05 USD | 6,444,555.70 USD | 6,425,361.36 USD | 19,194.34 USD | `+0.15%` | `1B / 1S` |
| `0:00 UTC` | `706.95` | `706.86` | `706.95` | `708.45` | `705.75` | 8,952,126.09 USD | 3,169,282.84 USD | 5,782,843.25 USD | -2,613,560.41 USD | `-29.19%` | `0B / 2S` |
| `5:00 UTC` | `707.85` | `707.46` | `707.85` | `708.45` | `706.05` | 5,397,479.08 USD | 2,137,235.04 USD | 3,260,244.05 USD | -1,123,009.01 USD | `-20.81%` | `0B / 3S` |
| `0:00 UTC` | `706.05` | `706.04` | `706.05` | `706.95` | `705.15` | 8,644,432.66 USD | 3,111,233.15 USD | 5,533,199.52 USD | -2,421,966.37 USD | `-28.02%` | `0B / 2S` |
| `5:00 UTC` | `705.15` | `705.00` | `705.15` | `705.75` | `704.55` | 1,736,502.81 USD | 454,158.28 USD | 1,282,344.53 USD | -828,186.24 USD | `-47.69%` | `0B / 2S` |

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
| `5m` | -773,580.00 USD | -872,140.00 USD | **`DISTRIBUTION`** |
| `15m` | -1,490,000.00 USD | -2,860,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -1,960,000.00 USD | -7,210,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -941,090.00 USD | -9,720,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -9,030,000.00 USD | -27,010,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -10,110,000.00 USD | -35,280,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -6,070,000.00 USD | -34,220,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -14,290,000.00 USD | -56,320,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -22,410,000.00 USD | -28,850,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -50,340,000.00 USD | -107,340,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -65,550,000.00 USD | -138,930,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -164,390,000.00 USD | -469,780,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-773.58K` | 15m=`-1.49M` | 1h=`-941.09K` | 24h=`-50.34M`
* Futures Capital Netflows: 5m=`-872.14K` | 15m=`-2.86M` | 1h=`-9.72M` | 24h=`-107.34M`
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
  * `2026-10-30 14:10:12 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:52:12 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:51:12 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:32:12 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 13:24:12 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:24:12 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 13:22:12 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 13:21:12 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:16:12 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:16:12 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `690.08` (Risk Distance: `9.18` pts)
  * +2.5R Take Profit: `722.21`
  * Mathematical Lot Sizing: **`1.08 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `715.24` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `724.42` (Risk Distance: `9.18` pts)
  * +2.5R Take Profit: `692.29`
  * Mathematical Lot Sizing: **`1.08 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`710.14`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
