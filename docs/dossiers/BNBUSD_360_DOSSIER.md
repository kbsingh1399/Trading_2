# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BNB
**Canonical Key**: `BNB` | **Broker Instrument**: `BNBUSD.p` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 10:43:53 IST` (`2026-10-30 05:13:53 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `716.90` | **Live Ask Quote**: `720.10` | **Mid Price**: `718.50`
- **Spread Points**: `320.00` | **Spread BPS**: `44.54 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `718.50` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.80` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `723.53` | Lower -3.00σ Band: `713.47`
  * Upper +2.51σ Band: `722.45` | Lower -2.51σ Band: `714.55`
  * Upper +2.01σ Band: `721.52` | Lower -2.01σ Band: `715.48`
  * Upper +2.00σ Band: `721.37` | Lower -2.00σ Band: `715.63`
  * Upper +1.28σ Band: `720.51` | Lower -1.28σ Band: `716.49`
  * Upper +1.00σ Band: `719.94` | Lower -1.00σ Band: `717.06`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`718.50` | EMA-20=`718.50` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`718.50` (Slope: `+0.0000`) | EMA-100=`718.50`
  * Institutional Anchors: EMA-144=`718.50` | EMA-200=`718.50` (Slope: `+0.0000`) | EMA-233=`718.50`
- **Range Boundaries**: 24H High=`725.69` | 24H Low=`711.31` | Weekly High=`732.87` | Weekly Low=`704.13`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `714.63` (Distance: `+0.47%`)
  * Point of Control (POC) = `706.94` (Distance: `+1.56%`)
  * Value Area Low (VAL) = `698.03` (Distance: `+2.86%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`754.57` | POC=`744.11` | VAL=`738.60`
  * Prior Day Extremes: PDH=`759.80` | PDL=`677.20` | PDC=`696.20`
  * Monday Range Blueprint: High=`746.00` | Mid=`738.45` | Low=`730.90`
  * Developing Weekly Value Area: Weekly VAH=`751.69` | Weekly POC=`740.53` | Weekly VAL=`734.95`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`724.00` | Low=`677.90`
  * London Session (08:00-16:00 UTC): High=`717.90` | Low=`712.90`
  * New York Session (13:00-21:00 UTC): High=`722.81` | Low=`714.19`
  * Initial Balance (First Hour): IB High=`717.90` | IB Low=`712.90`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `715.63` - `721.37`
  * Optimal Trade Entry (OTE 0.705): `719.94`
  * Structural Invalidation Anchor (0.786): `724.25`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `717.32` | `720.37` | `716.64` | `719.95` | `5,417` | 3,896,179.39 USD | 899,015.06 USD | `+23.07%` | -45,496,563.18 USD | `+0.94` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `719.95` | `720.96` | `719.70` | `720.07` | `2,806` | 2,020,945.71 USD | 429,406.37 USD | `+21.25%` | -45,067,156.82 USD | `+0.41` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `720.06` | `721.67` | `719.75` | `719.93` | `3,091` | 2,227,565.64 USD | 341,435.23 USD | `+15.33%` | -44,725,721.59 USD | `+0.65` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `718.29` | `719.43` | `716.59` | `716.90` | `7,462` | 5,355,538.86 USD | 367,216.51 USD | `+6.86%` | -46,076,028.42 USD | `+0.66` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `716.90` | `717.99` | `716.63` | `717.32` | `6,895` | 4,945,586.67 USD | -319,549.83 USD | `-6.46%` | -46,395,578.25 USD | `+0.32` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `717.32` | `721.67` | `716.64` | `719.93` | `11,313` | 8,144,690.75 USD | 1,669,856.66 USD | `+20.50%` | -44,725,721.59 USD | `+1.02` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `710.57` | `719.84` | `708.09` | `719.55` | `75,178` | 53,681,760.72 USD | 2,189,785.10 USD | `+4.08%` | -37,453,136.79 USD | `+0.38` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `719.56` | `719.60` | `715.13` | `717.32` | `39,263` | 28,162,402.44 USD | -3,149,012.91 USD | `-11.18%` | -40,602,149.70 USD | `-0.18` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `717.32` | `721.67` | `716.64` | `719.93` | `11,276` | 8,117,859.01 USD | 1,659,122.44 USD | `+20.44%` | -38,943,027.25 USD | `+0.26` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `745.34` | `745.53` | `677.76` | `697.96` | `1,556,116` | 1,101,338,590.19 USD | -7,502,511.31 USD | `-0.68%` | -9,565,109.48 USD | `-0.71` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `697.96` | `719.84` | `681.03` | `719.55` | `524,764` | 367,784,698.06 USD | -19,177,539.23 USD | `-5.21%` | -28,742,648.71 USD | `-1.45` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `719.56` | `721.67` | `715.13` | `719.93` | `50,576` | 36,307,093.18 USD | -1,479,156.25 USD | `-4.07%` | -30,221,804.96 USD | `+0.41` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `740.45` | `753.64` | `739.55` | `750.62` | `148,938` | 111,099,080.67 USD | 8,045,498.44 USD | `+7.24%` | -2,294,794.05 USD | `+1.00` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `750.62` | `754.90` | `743.07` | `745.33` | `88,414` | 66,199,547.89 USD | 232,195.88 USD | `+0.35%` | -2,062,598.17 USD | `+0.12` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `745.34` | `745.53` | `677.76` | `697.96` | `1,556,116` | 1,101,338,590.19 USD | -7,502,511.31 USD | `-0.68%` | -9,565,109.48 USD | `-0.71` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `697.96` | `719.84` | `681.03` | `719.55` | `524,764` | 367,784,698.06 USD | -19,177,539.23 USD | `-5.21%` | -28,742,648.71 USD | `-1.45` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `719.56` | `721.67` | `715.13` | `719.93` | `50,576` | 36,307,093.18 USD | -1,479,156.25 USD | `-4.07%` | -30,221,804.96 USD | `+0.41` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| --- | **`718.50`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `718.99` | `827000000.0000` | 594.60 USD | 119,488.46 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `719.00` | `5226000000.0000` | 3,757.49 USD | 118,893.85 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `719.02` | `14369000000.0000` | 10,331.60 USD | 115,136.36 USD | `3 orders` | `-0.06%` | `-` |
| `BID` | `719.06` | `46579000000.0000` | 33,493.10 USD | 104,804.76 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `719.07` | `4743000000.0000` | 3,410.55 USD | 71,311.66 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `719.08` | `24570000000.0000` | 17,667.80 USD | 67,901.11 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `719.10` | `2827000000.0000` | 2,032.90 USD | 50,233.32 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `719.11` | `3186000000.0000` | 2,291.08 USD | 48,200.42 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `719.16` | `827000000.0000` | 594.75 USD | 45,909.34 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `719.17` | `1000000000.0000` | 719.17 USD | 45,314.59 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `719.20` | `2296000000.0000` | 1,651.28 USD | 44,595.42 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `719.21` | `208000000.0000` | 149.60 USD | 42,944.14 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `719.22` | `242000000.0000` | 174.05 USD | 42,794.54 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `719.23` | `827000000.0000` | 594.80 USD | 42,620.49 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `719.27` | `41272000000.0000` | 29,685.71 USD | 42,025.69 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `719.29` | `620000000.0000` | 445.96 USD | 12,339.98 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `719.32` | `3572000000.0000` | 2,569.41 USD | 11,894.02 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `719.33` | `822000000.0000` | 591.29 USD | 9,324.61 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `719.41` | `2139000000.0000` | 1,538.82 USD | 8,733.32 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `719.45` | `10000000000.0000` | 7,194.50 USD | 7,194.50 USD | `1 orders` | `-0.00%` | `-` |
| `ASK` | `719.46` | `16629000000.0000` | 11,963.90 USD | 11,963.90 USD | `6 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `719.46` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 719.46` | `0.00%` | `-` |
| `ASK` | `719.52` | `827000000.0000` | 595.04 USD | 12,558.94 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `719.53` | `3867000000.0000` | 2,782.42 USD | 15,341.37 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `719.56` | `12353000000.0000` | 8,888.72 USD | 24,230.09 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `719.57` | `2779000000.0000` | 1,999.69 USD | 26,229.78 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `719.60` | `827000000.0000` | 595.11 USD | 26,824.88 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `719.66` | `15440000000.0000` | 11,111.55 USD | 37,936.44 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `719.67` | `279000000.0000` | 200.79 USD | 38,137.22 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `719.69` | `18526000000.0000` | 13,332.98 USD | 51,470.20 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `719.70` | `1953000000.0000` | 1,405.57 USD | 52,875.77 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `719.71` | `25067000000.0000` | 18,040.97 USD | 70,916.74 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `719.72` | `1933000000.0000` | 1,391.22 USD | 72,307.96 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `719.74` | `140000000.0000` | 100.76 USD | 72,408.73 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `719.75` | `827000000.0000` | 595.23 USD | 73,003.96 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `719.78` | `25625000000.0000` | 18,444.36 USD | 91,448.32 USD | `5 orders` | `+0.05%` | `-` |
| `ASK` | `719.81` | `2500000000.0000` | 1,799.52 USD | 93,247.85 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `719.82` | `1831000000.0000` | 1,317.99 USD | 94,565.84 USD | `3 orders` | `+0.05%` | `-` |
| `ASK` | `719.83` | `827000000.0000` | 595.30 USD | 95,161.14 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `719.84` | `1439000000.0000` | 1,035.85 USD | 96,196.99 USD | `3 orders` | `+0.05%` | `-` |
| `ASK` | `719.85` | `2622000000.0000` | 1,887.45 USD | 98,084.43 USD | `1 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:43:23 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `780` | `0xea00...a918` | `LONG` | 2,950,581.99 USD | `4,098,429,000,000.00` | `787.24` | `719.70` | `0.000000` | -275,844.79 USD | `-9.35%` | `5X Cross` |
| `902` | `0xfe7c...b7ae` | `LONG` | 2,513,689.59 USD | `3,491,575,000,000.00` | `686.05` | `719.70` | `0.000000` | 118,278.73 USD | `+4.71%` | `10X Cross` |
| `1028` | `0x7d0c...1b28` | `LONG` | 2,115,045.86 USD | `2,938,135,000,000.00` | `703.65` | `719.70` | `0.000000` | 47,619.92 USD | `+2.25%` | `10X Cross` |
| `1079` | `0x27c9...d65d` | `LONG` | 2,023,117.05 USD | `2,810,158,000,000.00` | `700.84` | `719.70` | `186.17` | 53,637.26 USD | `+2.65%` | `10X Cross` |
| `1170` | `0x7737...bf66` | `SHORT` | 1,904,746.11 USD | `2,646,179,000,000.00` | `752.73` | `719.70` | `6894.01` | 87,124.48 USD | `+4.57%` | `10X Cross` |
| `1344` | `0x51f6...2b39` | `LONG` | 1,613,920.36 USD | `2,241,992,000,000.00` | `703.00` | `719.70` | `111.84` | 37,810.18 USD | `+2.34%` | `10X Cross` |
| `1470` | `0xc675...795d` | `LONG` | 1,479,363.59 USD | `2,055,214,000,000.00` | `706.91` | `719.70` | `640.91` | 26,518.92 USD | `+1.79%` | `10X Cross` |
| `1494` | `0x2edd...8179` | `LONG` | 1,453,802.88 USD | `2,019,367,000,000.00` | `714.56` | `719.70` | `0.000000` | 10,841.50 USD | `+0.75%` | `10X Cross` |
| `1548` | `0x325e...9564` | `LONG` | 1,392,497.25 USD | `1,934,212,000,000.00` | `707.43` | `719.70` | `0.000000` | 24,171.48 USD | `+1.74%` | `10X Cross` |
| `1609` | `0xecb6...2b00` | `SHORT` | 1,326,203.86 USD | `1,842,564,000,000.00` | `715.28` | `719.70` | `15367.79` | -8,260.64 USD | `-0.62%` | `5X Cross` |
| `1696` | `0x07fd...689d` | `LONG` | 1,244,331.33 USD | `1,728,406,000,000.00` | `714.40` | `719.70` | `0.000000` | 9,548.35 USD | `+0.77%` | `10X Cross` |
| `1702` | `0x645b...87b8` | `LONG` | 1,239,419.52 USD | `1,721,990,000,000.00` | `747.34` | `719.70` | `0.000000` | -47,487.90 USD | `-3.83%` | `10X Cross` |
| `1781` | `0xa4a6...46cf` | `SHORT` | 1,170,204.46 USD | `1,625,442,000,000.00` | `711.86` | `719.70` | `1726.66` | -13,112.08 USD | `-1.12%` | `10X Cross` |
| `1859` | `0xfc27...9d9d` | `LONG` | 1,110,722.12 USD | `1,543,184,000,000.00` | `700.97` | `719.70` | `0.000000` | 28,996.57 USD | `+2.61%` | `10X Cross` |
| `1874` | `0x4420...4c4b` | `LONG` | 1,094,350.95 USD | `1,520,143,000,000.00` | `704.02` | `719.70` | `212.61` | 24,140.38 USD | `+2.21%` | `10X Cross` |
| `1891` | `0x14c6...b280` | `SHORT` | 1,078,830.00 USD | `1,500,000,000,000.00` | `712.51` | `719.70` | `1466.99` | -10,068.30 USD | `-0.93%` | `10X Cross` |
| `1995` | `0x646b...01dc` | `SHORT` | 1,014,495.74 USD | `1,412,868,000,000.00` | `699.26` | `719.70` | `1289.64` | -26,526.74 USD | `-2.61%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`758.29` (Vol: 2,900,000.00 USD, Dist: `+5.67%`) | Long MP=`677.19` (Vol: 3,100,000.00 USD, Dist: `--5.63%`)
  * 48H Horizon: Short MP=`767.93` (Vol: 3,000,000.00 USD, Dist: `+7.01%`) | Long MP=`677.29` (Vol: 3,100,000.00 USD, Dist: `--5.62%`)
  * 3D Horizon: Short MP=`767.93` (Vol: 3,400,000.00 USD, Dist: `+7.01%`) | Long MP=`677.29` (Vol: 3,100,000.00 USD, Dist: `--5.62%`)
  * 7D Horizon: Short MP=`767.93` (Vol: 3,500,000.00 USD, Dist: `+7.01%`) | Long MP=`677.29` (Vol: 3,100,000.00 USD, Dist: `--5.62%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
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
| `1D` | `Long Liquidation` | `636.80` | 47,610,000.00 USD | 47,610,000.00 USD | 101,910.00 USD | 40,910.00 USD | 275,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `637.50` | 305.36 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `637.60` | 47,190,000.00 USD | 47,190,000.00 USD | 34,750.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `638.40` | 47,160,000.00 USD | 47,160,000.00 USD | 24,710.00 USD | 37,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `638.50` | 6,710.00 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `639.20` | 47,100,000.00 USD | 47,100,000.00 USD | 194,520.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `639.50` | 127.26 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `640.00` | 46,900,000.00 USD | 46,900,000.00 USD | 21,450.00 USD | 0.00 USD | 184,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `640.50` | 1,320,000.00 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `641.60` | 46,700,000.00 USD | 46,700,000.00 USD | 113,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `642.40` | 46,580,000.00 USD | 46,580,000.00 USD | 122,750.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `642.50` | 8,480.00 USD | 360,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `643.20` | 46,460,000.00 USD | 46,460,000.00 USD | 48,750.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `643.50` | 339.12 USD | 351,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `644.00` | 46,410,000.00 USD | 46,410,000.00 USD | 34,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `644.80` | 46,380,000.00 USD | 46,380,000.00 USD | 354,850.00 USD | 10,420.00 USD | 341,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `645.60` | 45,670,000.00 USD | 45,670,000.00 USD | 64,260.00 USD | 0.00 USD | 17,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `646.40` | 45,590,000.00 USD | 45,590,000.00 USD | 87,020.00 USD | 9,200.00 USD | 140,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `646.50` | 463.54 USD | 351,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `647.20` | 45,350,000.00 USD | 45,350,000.00 USD | 187,370.00 USD | 33,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `648.00` | 45,130,000.00 USD | 45,130,000.00 USD | 222,650.00 USD | 0.00 USD | 7,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `648.50` | 1,940.00 USD | 351,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `649.50` | 1,620.00 USD | 349,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `649.60` | 44,900,000.00 USD | 44,900,000.00 USD | 96,580.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `650.40` | 44,800,000.00 USD | 44,800,000.00 USD | 17,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `650.50` | 2,090.00 USD | 347,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `651.20` | 44,790,000.00 USD | 44,790,000.00 USD | 184,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `651.50` | 9,650.00 USD | 345,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `652.00` | 44,600,000.00 USD | 44,600,000.00 USD | 0.00 USD | 0.00 USD | 94,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `652.50` | 652.50 USD | 335,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `652.80` | 44,510,000.00 USD | 44,510,000.00 USD | 30,730.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `653.50` | 97,380.00 USD | 335,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `653.60` | 44,480,000.00 USD | 44,480,000.00 USD | 43,630.00 USD | 26,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `654.40` | 44,410,000.00 USD | 44,410,000.00 USD | 108,090.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `654.50` | 100.14 USD | 237,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `655.20` | 44,300,000.00 USD | 44,300,000.00 USD | 72,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `655.50` | 437.87 USD | 237,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `656.00` | 44,230,000.00 USD | 44,230,000.00 USD | 190,750.00 USD | 19,650.00 USD | 87,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `656.80` | 43,930,000.00 USD | 43,930,000.00 USD | 134,130.00 USD | 21,320.00 USD | 738,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `657.60` | 43,040,000.00 USD | 43,040,000.00 USD | 227,900.00 USD | 0.00 USD | 21,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `658.40` | 42,790,000.00 USD | 42,790,000.00 USD | 859,170.00 USD | 14,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `658.50` | 15,090.00 USD | 237,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `659.20` | 41,910,000.00 USD | 41,910,000.00 USD | 55,730.00 USD | 7,460.00 USD | 81,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `659.50` | 46,450.00 USD | 222,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `660.00` | 41,770,000.00 USD | 41,770,000.00 USD | 159,940.00 USD | 0.00 USD | 14,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `660.50` | 3,410.00 USD | 175,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `660.80` | 41,590,000.00 USD | 41,590,000.00 USD | 0.00 USD | 83,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `661.50` | 20,140.00 USD | 172,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `661.60` | 41,510,000.00 USD | 41,510,000.00 USD | 491,390.00 USD | 19,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `662.40` | 41,000,000.00 USD | 41,000,000.00 USD | 199,440.00 USD | 136,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `662.50` | 2,850.00 USD | 152,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `663.20` | 40,660,000.00 USD | 40,660,000.00 USD | 202,030.00 USD | 5,000.00 USD | 44,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `663.50` | 9,230.00 USD | 149,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `664.00` | 40,410,000.00 USD | 40,410,000.00 USD | 45,960.00 USD | 64,390.00 USD | 64,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `664.10` | 87,050,000.00 USD | 87,050,000.00 USD | 78,740.00 USD | 18,740.00 USD | 39,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `664.50` | 24,100.00 USD | 140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `664.80` | 40,240,000.00 USD | 40,240,000.00 USD | 1,340,000.00 USD | 0.00 USD | 64,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `665.00` | 86,910,000.00 USD | 86,910,000.00 USD | 92,030.00 USD | 22,990.00 USD | 37,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `665.50` | 10,950.00 USD | 115,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `665.60` | 38,830,000.00 USD | 38,830,000.00 USD | 695,710.00 USD | 5,880.00 USD | 8,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `665.90` | 86,760,000.00 USD | 86,760,000.00 USD | 264,020.00 USD | 71,380.00 USD | 63,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `666.40` | 38,120,000.00 USD | 38,120,000.00 USD | 306,600.00 USD | 92,350.00 USD | 778,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `666.50` | 1,930.00 USD | 104,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `666.80` | 86,360,000.00 USD | 86,360,000.00 USD | 198,550.00 USD | 33,320.00 USD | 61,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `667.20` | 36,950,000.00 USD | 36,950,000.00 USD | 902,780.00 USD | 25,280.00 USD | 13,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `667.50` | 1,380.00 USD | 103,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `667.70` | 86,070,000.00 USD | 86,070,000.00 USD | 199,690.00 USD | 45,130.00 USD | 51,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `668.00` | 36,010,000.00 USD | 36,010,000.00 USD | 394,550.00 USD | 159,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `668.50` | 1,450.00 USD | 101,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `668.60` | 85,770,000.00 USD | 85,770,000.00 USD | 387,530.00 USD | 92,860.00 USD | 51,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `668.80` | 35,450,000.00 USD | 35,450,000.00 USD | 769,660.00 USD | 30,970.00 USD | 3,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `669.50` | 85,240,000.00 USD | 85,240,000.00 USD | 341,150.00 USD | 38,130.00 USD | 108,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `669.50` | 2,930.00 USD | 100,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `669.60` | 34,650,000.00 USD | 34,650,000.00 USD | 708,560.00 USD | 100,330.00 USD | 49,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `670.40` | 33,790,000.00 USD | 33,790,000.00 USD | 354,100.00 USD | 10,760.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `670.40` | 84,750,000.00 USD | 84,750,000.00 USD | 319,660.00 USD | 93,800.00 USD | 77,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `670.50` | 6,110.00 USD | 97,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `671.20` | 31,950,000.00 USD | 31,950,000.00 USD | 548,370.00 USD | 13,720.00 USD | 48,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `671.30` | 84,260,000.00 USD | 84,260,000.00 USD | 335,750.00 USD | 57,500.00 USD | 42,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `671.50` | 832.66 USD | 91,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `672.00` | 31,340,000.00 USD | 31,340,000.00 USD | 2,080,000.00 USD | 18,180.00 USD | 13,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `672.20` | 83,830,000.00 USD | 83,830,000.00 USD | 180,230.00 USD | 62,620.00 USD | 74,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `672.50` | 6,920.00 USD | 90,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `672.80` | 29,220,000.00 USD | 29,220,000.00 USD | 192,130.00 USD | 118,570.00 USD | 846,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `673.10` | 83,510,000.00 USD | 83,510,000.00 USD | 394,120.00 USD | 64,970.00 USD | 42,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `673.50` | 41,240.00 USD | 83,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `673.60` | 28,060,000.00 USD | 28,060,000.00 USD | 201,420.00 USD | 245,910.00 USD | 1,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `674.00` | 83,010,000.00 USD | 83,010,000.00 USD | 335,670.00 USD | 105,910.00 USD | 80,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `674.40` | 26,050,000.00 USD | 26,050,000.00 USD | 1,280,000.00 USD | 438,780.00 USD | 207,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `674.50` | 4,310.00 USD | 42,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `674.90` | 82,490,000.00 USD | 82,490,000.00 USD | 247,070.00 USD | 31,490.00 USD | 44,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `675.20` | 24,130,000.00 USD | 24,130,000.00 USD | 1,140,000.00 USD | 61,020.00 USD | 289,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `675.50` | 9,430.00 USD | 37,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `675.80` | 82,160,000.00 USD | 82,160,000.00 USD | 387,400.00 USD | 26,020.00 USD | 79,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `676.00` | 22,630,000.00 USD | 22,630,000.00 USD | 626,400.00 USD | 372,550.00 USD | 422,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `676.50` | 1,660.00 USD | 28,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `676.70` | 81,670,000.00 USD | 81,670,000.00 USD | 509,100.00 USD | 35,490.00 USD | 126,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `676.80` | 21,210,000.00 USD | 21,210,000.00 USD | 340,220.00 USD | 163,630.00 USD | 176,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `677.50` | 438.34 USD | 26,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `677.60` | 20,530,000.00 USD | 20,530,000.00 USD | 295,270.00 USD | 177,920.00 USD | 242,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `677.60` | 81,000,000.00 USD | 81,000,000.00 USD | 409,810.00 USD | 0.00 USD | 63,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `678.40` | 19,820,000.00 USD | 19,820,000.00 USD | 1,240,000.00 USD | 108,180.00 USD | 123,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `678.50` | 80,530,000.00 USD | 80,530,000.00 USD | 120,190.00 USD | 0.00 USD | 26,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `678.50` | 417.96 USD | 26,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `679.20` | 18,350,000.00 USD | 18,350,000.00 USD | 1,360,000.00 USD | 30,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `679.40` | 80,380,000.00 USD | 80,380,000.00 USD | 116,510.00 USD | 10,480.00 USD | 40,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `679.50` | 3,510.00 USD | 25,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `680.00` | 16,960,000.00 USD | 16,960,000.00 USD | 233,510.00 USD | 217,890.00 USD | 298,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `680.30` | 80,210,000.00 USD | 80,210,000.00 USD | 166,780.00 USD | 13,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `680.50` | 21,460.00 USD | 22,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `680.80` | 16,210,000.00 USD | 16,210,000.00 USD | 265,940.00 USD | 126,150.00 USD | 187,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `681.20` | 80,030,000.00 USD | 80,030,000.00 USD | 106,280.00 USD | 7,050.00 USD | 35,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `681.50` | 939.79 USD | 939.79 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `681.60` | 15,630,000.00 USD | 15,630,000.00 USD | 647,060.00 USD | 414,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `682.10` | 79,880,000.00 USD | 79,880,000.00 USD | 0.00 USD | 23,360.00 USD | 27,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `682.40` | 14,570,000.00 USD | 14,570,000.00 USD | 14,340.00 USD | 75,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `682.50` | 345.35 USD | 345.35 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `683.00` | 79,830,000.00 USD | 79,830,000.00 USD | 175,930.00 USD | 28,470.00 USD | 11,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `683.20` | 14,480,000.00 USD | 14,480,000.00 USD | 662,310.00 USD | 0.00 USD | 37,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `683.90` | 79,620,000.00 USD | 79,620,000.00 USD | 77,000.00 USD | 29,510.00 USD | 17,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `684.00` | 13,780,000.00 USD | 13,780,000.00 USD | 380,290.00 USD | 0.00 USD | 38,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `684.80` | 13,360,000.00 USD | 13,360,000.00 USD | 138,250.00 USD | 58,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `684.80` | 79,490,000.00 USD | 79,490,000.00 USD | 246,080.00 USD | 9,850.00 USD | 39,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `685.60` | 13,160,000.00 USD | 13,160,000.00 USD | 1,360,000.00 USD | 32,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `685.70` | 79,200,000.00 USD | 79,200,000.00 USD | 197,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `686.40` | 11,760,000.00 USD | 11,760,000.00 USD | 95,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `686.60` | 79,000,000.00 USD | 79,000,000.00 USD | 62,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `687.20` | 11,670,000.00 USD | 11,670,000.00 USD | 902,200.00 USD | 152,370.00 USD | 98,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `687.50` | 78,940,000.00 USD | 78,940,000.00 USD | 148,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `688.00` | 10,510,000.00 USD | 10,510,000.00 USD | 373,380.00 USD | 19,580.00 USD | 180,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `688.40` | 78,790,000.00 USD | 78,790,000.00 USD | 67,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `688.80` | 9,940,000.00 USD | 9,940,000.00 USD | 116,110.00 USD | 100,620.00 USD | 492,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `689.30` | 78,720,000.00 USD | 78,720,000.00 USD | 84,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `689.60` | 9,230,000.00 USD | 9,230,000.00 USD | 0.00 USD | 60,040.00 USD | 773,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `690.20` | 78,640,000.00 USD | 78,640,000.00 USD | 283,920.00 USD | 63,230.00 USD | 82,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `690.40` | 8,400,000.00 USD | 8,400,000.00 USD | 0.00 USD | 34,700.00 USD | 6,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `691.10` | 78,210,000.00 USD | 78,210,000.00 USD | 362,020.00 USD | 61,370.00 USD | 81,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `691.20` | 8,360,000.00 USD | 8,360,000.00 USD | 0.00 USD | 129,500.00 USD | 17,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `692.00` | 8,210,000.00 USD | 8,210,000.00 USD | 0.00 USD | 23,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `692.00` | 77,700,000.00 USD | 77,700,000.00 USD | 322,430.00 USD | 18,850.00 USD | 58,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `692.90` | 77,300,000.00 USD | 77,300,000.00 USD | 280,830.00 USD | 19,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `693.60` | 8,180,000.00 USD | 8,180,000.00 USD | 0.00 USD | 92,970.00 USD | 273,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `693.80` | 77,000,000.00 USD | 77,000,000.00 USD | 305,720.00 USD | 39,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `694.40` | 7,820,000.00 USD | 7,820,000.00 USD | 0.00 USD | 116,660.00 USD | 180,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `694.70` | 76,660,000.00 USD | 76,660,000.00 USD | 279,840.00 USD | 36,640.00 USD | 35,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `695.20` | 7,520,000.00 USD | 7,520,000.00 USD | 239,550.00 USD | 32,370.00 USD | 175,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `695.60` | 76,300,000.00 USD | 76,300,000.00 USD | 120,440.00 USD | 0.00 USD | 21,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `696.00` | 7,070,000.00 USD | 7,070,000.00 USD | 0.00 USD | 66,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `696.50` | 76,160,000.00 USD | 76,160,000.00 USD | 140,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `696.80` | 7,010,000.00 USD | 7,010,000.00 USD | 0.00 USD | 63,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `697.40` | 76,020,000.00 USD | 76,020,000.00 USD | 189,100.00 USD | 19,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `698.30` | 75,810,000.00 USD | 75,810,000.00 USD | 273,520.00 USD | 33,120.00 USD | 54,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `698.40` | 6,940,000.00 USD | 6,940,000.00 USD | 479,860.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `699.20` | 6,460,000.00 USD | 6,460,000.00 USD | 0.00 USD | 31,670.00 USD | 42,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `699.20` | 75,450,000.00 USD | 75,450,000.00 USD | 274,810.00 USD | 12,670.00 USD | 11,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `700.10` | 75,150,000.00 USD | 75,150,000.00 USD | 225,450.00 USD | 40,820.00 USD | 27,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `700.80` | 6,390,000.00 USD | 6,390,000.00 USD | 190,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `701.00` | 74,860,000.00 USD | 74,860,000.00 USD | 237,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `701.60` | 6,200,000.00 USD | 6,200,000.00 USD | 0.00 USD | 111,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `701.90` | 74,620,000.00 USD | 74,620,000.00 USD | 135,260.00 USD | 41,260.00 USD | 89,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `702.40` | 6,090,000.00 USD | 6,090,000.00 USD | 138,970.00 USD | 39,170.00 USD | 67,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `702.80` | 74,360,000.00 USD | 74,360,000.00 USD | 416,820.00 USD | 57,470.00 USD | 36,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `703.20` | 5,840,000.00 USD | 5,840,000.00 USD | 434,010.00 USD | 45,990.00 USD | 353,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `703.70` | 73,840,000.00 USD | 73,840,000.00 USD | 311,800.00 USD | 44,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `704.00` | 5,010,000.00 USD | 5,010,000.00 USD | 0.00 USD | 0.00 USD | 159,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `704.60` | 73,490,000.00 USD | 73,490,000.00 USD | 537,050.00 USD | 136,550.00 USD | 194,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `704.80` | 4,850,000.00 USD | 4,850,000.00 USD | 0.00 USD | 23,130.00 USD | 12,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `705.50` | 72,620,000.00 USD | 72,620,000.00 USD | 920,340.00 USD | 162,820.00 USD | 236,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `705.60` | 4,810,000.00 USD | 4,810,000.00 USD | 121,180.00 USD | 0.00 USD | 173,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `706.40` | 4,520,000.00 USD | 4,520,000.00 USD | 116,270.00 USD | 0.00 USD | 71,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `706.40` | 71,300,000.00 USD | 71,300,000.00 USD | 523,540.00 USD | 104,380.00 USD | 231,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `707.30` | 70,440,000.00 USD | 70,440,000.00 USD | 604,060.00 USD | 90,200.00 USD | 53,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `708.00` | 4,330,000.00 USD | 4,330,000.00 USD | 201,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `708.20` | 69,690,000.00 USD | 69,690,000.00 USD | 796,640.00 USD | 138,200.00 USD | 42,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `708.80` | 4,130,000.00 USD | 4,130,000.00 USD | 382,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `709.10` | 68,710,000.00 USD | 68,710,000.00 USD | 392,150.00 USD | 156,040.00 USD | 195,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `709.50` | 1,400.00 USD | 1,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `710.00` | 67,970,000.00 USD | 67,970,000.00 USD | 450,480.00 USD | 167,090.00 USD | 176,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `710.40` | 3,750,000.00 USD | 3,750,000.00 USD | 292,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `710.90` | 67,180,000.00 USD | 67,180,000.00 USD | 922,450.00 USD | 160,040.00 USD | 236,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `711.20` | 3,460,000.00 USD | 3,460,000.00 USD | 652,220.00 USD | 0.00 USD | 37,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `711.80` | 65,860,000.00 USD | 65,860,000.00 USD | 608,910.00 USD | 232,130.00 USD | 114,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `712.00` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 0.00 USD | 38,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `712.70` | 64,900,000.00 USD | 64,900,000.00 USD | 1,190,000.00 USD | 217,390.00 USD | 236,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `712.80` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 0.00 USD | 21,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `713.60` | 63,260,000.00 USD | 63,260,000.00 USD | 2,250,000.00 USD | 279,180.00 USD | 308,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `714.50` | 60,410,000.00 USD | 60,410,000.00 USD | 508,400.00 USD | 209,320.00 USD | 292,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `715.20` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 317,060.00 USD | 1,330,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `715.40` | 59,400,000.00 USD | 59,400,000.00 USD | 1,050,000.00 USD | 419,310.00 USD | 329,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `716.00` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 146,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `716.30` | 57,600,000.00 USD | 57,600,000.00 USD | 1,080,000.00 USD | 324,540.00 USD | 233,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `717.20` | 55,960,000.00 USD | 55,960,000.00 USD | 581,610.00 USD | 398,030.00 USD | 387,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `718.10` | 54,590,000.00 USD | 54,590,000.00 USD | 1,690,000.00 USD | 246,320.00 USD | 151,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `718.40` | 909,530.00 USD | 909,530.00 USD | 656,220.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `719.00` | 52,510,000.00 USD | 52,510,000.00 USD | 670,390.00 USD | 137,460.00 USD | 211,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `719.20` | 253,300.00 USD | 253,300.00 USD | 126,360.00 USD | 126,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `719.90` | 51,490,000.00 USD | 51,490,000.00 USD | 618,020.00 USD | 173,240.00 USD | 186,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `720.00` | 170,940.00 USD | 170,940.00 USD | 147,340.00 USD | 23,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `720.50` | 161.39 USD | 1,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `720.80` | 525,280.00 USD | 525,280.00 USD | 149,800.00 USD | 204,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `720.80` | 50,510,000.00 USD | 50,510,000.00 USD | 1,010,000.00 USD | 52,490.00 USD | 180,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `721.50` | 33,260.00 USD | 35,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `721.60` | 762,810.00 USD | 762,810.00 USD | 100,790.00 USD | 78,640.00 USD | 58,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `721.70` | 49,260,000.00 USD | 49,260,000.00 USD | 1,950,000.00 USD | 237,690.00 USD | 653,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `722.40` | 1,360,000.00 USD | 1,360,000.00 USD | 28,010.00 USD | 177,770.00 USD | 391,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `722.50` | 566.44 USD | 35,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `722.60` | 46,430,000.00 USD | 46,430,000.00 USD | 1,930,000.00 USD | 108,200.00 USD | 229,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `723.20` | 2,140,000.00 USD | 2,140,000.00 USD | 191,050.00 USD | 416,750.00 USD | 176,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `723.50` | 44,160,000.00 USD | 44,160,000.00 USD | 640,550.00 USD | 140,550.00 USD | 293,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `723.50` | 3,560.00 USD | 39,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `724.00` | 2,780,000.00 USD | 2,780,000.00 USD | 380,140.00 USD | 171,580.00 USD | 88,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `724.40` | 43,080,000.00 USD | 43,080,000.00 USD | 663,550.00 USD | 186,780.00 USD | 130,770.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `724.50` | 525.26 USD | 39,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `724.80` | 3,190,000.00 USD | 3,190,000.00 USD | 345,070.00 USD | 45,850.00 USD | 18,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `725.30` | 42,100,000.00 USD | 42,100,000.00 USD | 1,760,000.00 USD | 418,390.00 USD | 396,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `725.50` | 1,530.00 USD | 41,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `725.60` | 3,620,000.00 USD | 3,620,000.00 USD | 289,330.00 USD | 120,790.00 USD | 19,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `726.20` | 39,520,000.00 USD | 39,520,000.00 USD | 1,060,000.00 USD | 311,550.00 USD | 460,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `726.40` | 3,960,000.00 USD | 3,960,000.00 USD | 256,420.00 USD | 75,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `726.50` | 3,840.00 USD | 45,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `727.10` | 37,690,000.00 USD | 37,690,000.00 USD | 1,230,000.00 USD | 331,980.00 USD | 241,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `727.20` | 4,470,000.00 USD | 4,470,000.00 USD | 502,440.00 USD | 10,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `727.50` | 1,030.00 USD | 46,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `728.00` | 4,680,000.00 USD | 4,680,000.00 USD | 159,800.00 USD | 48,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `728.00` | 35,890,000.00 USD | 35,890,000.00 USD | 3,110,000.00 USD | 778,750.00 USD | 388,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `728.50` | 41,940.00 USD | 88,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `728.80` | 5,260,000.00 USD | 5,260,000.00 USD | 278,100.00 USD | 98,780.00 USD | 207,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `728.90` | 31,610,000.00 USD | 31,610,000.00 USD | 2,330,000.00 USD | 317,590.00 USD | 644,150.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `729.50` | 174,370.00 USD | 262,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `729.60` | 6,030,000.00 USD | 6,030,000.00 USD | 106,170.00 USD | 205,910.00 USD | 458,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `729.80` | 28,320,000.00 USD | 28,320,000.00 USD | 1,320,000.00 USD | 430,010.00 USD | 339,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `730.40` | 9,900,000.00 USD | 9,900,000.00 USD | 1,690,000.00 USD | 327,540.00 USD | 1,850,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `730.50` | 24,090.00 USD | 286,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `730.70` | 26,230,000.00 USD | 26,230,000.00 USD | 2,760,000.00 USD | 351,520.00 USD | 587,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `731.20` | 11,890,000.00 USD | 11,890,000.00 USD | 1,360,000.00 USD | 113,710.00 USD | 513,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `731.50` | 7,340.00 USD | 293,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `731.60` | 22,530,000.00 USD | 22,530,000.00 USD | 1,530,000.00 USD | 133,980.00 USD | 261,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `732.00` | 12,810,000.00 USD | 12,810,000.00 USD | 417,600.00 USD | 139,360.00 USD | 357,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `732.50` | 20,610,000.00 USD | 20,610,000.00 USD | 465,880.00 USD | 221,510.00 USD | 96,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `732.50` | 136,920.00 USD | 430,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `732.80` | 15,300,000.00 USD | 15,300,000.00 USD | 1,200,000.00 USD | 168,450.00 USD | 1,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `733.40` | 19,820,000.00 USD | 19,820,000.00 USD | 1,910,000.00 USD | 158,310.00 USD | 338,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `733.50` | 86,060.00 USD | 516,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `733.60` | 16,070,000.00 USD | 16,070,000.00 USD | 344,230.00 USD | 255,890.00 USD | 165,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `734.30` | 17,420,000.00 USD | 17,420,000.00 USD | 1,580,000.00 USD | 288,470.00 USD | 244,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `734.40` | 16,810,000.00 USD | 16,810,000.00 USD | 597,780.00 USD | 11,800.00 USD | 132,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `734.50` | 152,470.00 USD | 669,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `735.20` | 17,200,000.00 USD | 17,200,000.00 USD | 173,750.00 USD | 215,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `735.20` | 15,310,000.00 USD | 15,310,000.00 USD | 1,330,000.00 USD | 172,940.00 USD | 437,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `735.50` | 22,990.00 USD | 692,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `736.00` | 18,680,000.00 USD | 18,680,000.00 USD | 702,000.00 USD | 52,260.00 USD | 727,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `736.10` | 13,370,000.00 USD | 13,370,000.00 USD | 2,130,000.00 USD | 181,990.00 USD | 484,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `736.50` | 13,550.00 USD | 705,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `736.80` | 19,370,000.00 USD | 19,370,000.00 USD | 542,490.00 USD | 58,820.00 USD | 90,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `737.00` | 10,570,000.00 USD | 10,570,000.00 USD | 2,360,000.00 USD | 175,330.00 USD | 633,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `737.50` | 3,010.00 USD | 708,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `737.60` | 19,920,000.00 USD | 19,920,000.00 USD | 329,040.00 USD | 126,150.00 USD | 87,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `737.90` | 7,400,000.00 USD | 7,400,000.00 USD | 3,420,000.00 USD | 72,280.00 USD | 374,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `738.40` | 20,630,000.00 USD | 20,630,000.00 USD | 627,690.00 USD | 85,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `738.50` | 6,210.00 USD | 715,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `738.80` | 3,530,000.00 USD | 3,530,000.00 USD | 522,950.00 USD | 20,210.00 USD | 155,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `739.20` | 21,910,000.00 USD | 21,910,000.00 USD | 294,170.00 USD | 47,890.00 USD | 934,700.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `739.50` | 8,000.00 USD | 723,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `739.70` | 2,830,000.00 USD | 2,830,000.00 USD | 352,500.00 USD | 0.00 USD | 203,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `740.00` | 22,150,000.00 USD | 22,150,000.00 USD | 245,960.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `740.50` | 3,980.00 USD | 727,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `740.60` | 2,280,000.00 USD | 2,280,000.00 USD | 1,090,000.00 USD | 0.00 USD | 33,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `740.80` | 22,560,000.00 USD | 22,560,000.00 USD | 246,020.00 USD | 166,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `741.50` | 1,160,000.00 USD | 1,160,000.00 USD | 257,630.00 USD | 0.00 USD | 208,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `741.50` | 8,790.00 USD | 735,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `741.60` | 23,290,000.00 USD | 23,290,000.00 USD | 707,380.00 USD | 15,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `742.40` | 689,850.00 USD | 689,850.00 USD | 0.00 USD | 0.00 USD | 183,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `742.50` | 11,610.00 USD | 747,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `743.20` | 23,540,000.00 USD | 23,540,000.00 USD | 250,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `743.30` | 505,930.00 USD | 505,930.00 USD | 0.00 USD | 0.00 USD | 57,580.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `743.50` | 103,120.00 USD | 850,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `744.00` | 24,100,000.00 USD | 24,100,000.00 USD | 16,710.00 USD | 106,580.00 USD | 436,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `744.20` | 448,350.00 USD | 448,350.00 USD | 0.00 USD | 257,580.00 USD | 141,790.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `744.50` | 117,700.00 USD | 968,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `744.80` | 26,010,000.00 USD | 26,010,000.00 USD | 979,590.00 USD | 55,680.00 USD | 880,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `745.10` | 48,980.00 USD | 48,980.00 USD | 0.00 USD | 48,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `745.50` | 67,820.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `745.60` | 26,650,000.00 USD | 26,650,000.00 USD | 503,610.00 USD | 94,190.00 USD | 34,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `746.00` | 999,320.00 USD | 999,320.00 USD | 999,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `746.40` | 27,710,000.00 USD | 27,710,000.00 USD | 451,300.00 USD | 54,670.00 USD | 557,330.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `746.50` | 182,880.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `746.90` | 1,210,000.00 USD | 1,210,000.00 USD | 215,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `747.20` | 28,630,000.00 USD | 28,630,000.00 USD | 443,820.00 USD | 67,980.00 USD | 406,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `748.00` | 29,130,000.00 USD | 29,130,000.00 USD | 342,940.00 USD | 84,260.00 USD | 79,770.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `748.50` | 44,170.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `748.80` | 29,570,000.00 USD | 29,570,000.00 USD | 415,650.00 USD | 0.00 USD | 17,880.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `749.50` | 3,230.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `749.60` | 29,740,000.00 USD | 29,740,000.00 USD | 175,730.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `750.40` | 29,790,000.00 USD | 29,790,000.00 USD | 51,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `750.50` | 9,570.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `751.20` | 30,000,000.00 USD | 30,000,000.00 USD | 108,960.00 USD | 0.00 USD | 98,240.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `751.50` | 593,520.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `752.00` | 30,530,000.00 USD | 30,530,000.00 USD | 66,060.00 USD | 25,010.00 USD | 441,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `752.50` | 57,710.00 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `752.80` | 30,870,000.00 USD | 30,870,000.00 USD | 334,780.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `753.60` | 31,610,000.00 USD | 31,610,000.00 USD | 421,210.00 USD | 31,700.00 USD | 289,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `754.40` | 31,760,000.00 USD | 31,760,000.00 USD | 92,070.00 USD | 42,960.00 USD | 16,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `754.50` | 863,250.00 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `755.00` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 59,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `755.20` | 32,300,000.00 USD | 32,300,000.00 USD | 300,910.00 USD | 201,730.00 USD | 37,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `755.50` | 336.20 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `756.00` | 32,840,000.00 USD | 32,840,000.00 USD | 406,880.00 USD | 69,210.00 USD | 66,220.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `756.50` | 3,750.00 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `756.80` | 33,020,000.00 USD | 33,020,000.00 USD | 119,600.00 USD | 8,490.00 USD | 49,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `756.80` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 47,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `757.50` | 3,050.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `757.60` | 33,460,000.00 USD | 33,460,000.00 USD | 223,870.00 USD | 179,910.00 USD | 32,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `757.70` | 1,910,000.00 USD | 1,910,000.00 USD | 475,510.00 USD | 113,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `758.40` | 34,410,000.00 USD | 34,410,000.00 USD | 699,690.00 USD | 34,450.00 USD | 218,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `758.50` | 180,270.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `758.60` | 3,100,000.00 USD | 3,100,000.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `759.20` | 35,490,000.00 USD | 35,490,000.00 USD | 905,380.00 USD | 117,910.00 USD | 54,810.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `759.50` | 3,830.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `760.00` | 35,840,000.00 USD | 35,840,000.00 USD | 305,690.00 USD | 21,070.00 USD | 28,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `760.40` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 27,650.00 USD | 42,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `760.50` | 540.72 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `760.80` | 36,380,000.00 USD | 36,380,000.00 USD | 448,300.00 USD | 52,630.00 USD | 40,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `761.30` | 3,490,000.00 USD | 3,490,000.00 USD | 10,750.00 USD | 211,960.00 USD | 100,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `761.60` | 37,260,000.00 USD | 37,260,000.00 USD | 559,960.00 USD | 27,330.00 USD | 286,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `762.20` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 699,820.00 USD | 179,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `762.40` | 37,780,000.00 USD | 37,780,000.00 USD | 335,720.00 USD | 105,730.00 USD | 82,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `762.50` | 367.52 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `763.10` | 7,830,000.00 USD | 7,830,000.00 USD | 2,460,000.00 USD | 590,460.00 USD | 404,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `763.20` | 40,180,000.00 USD | 40,180,000.00 USD | 1,710,000.00 USD | 168,160.00 USD | 522,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `763.50` | 445,300.00 USD | 3,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `764.00` | 41,840,000.00 USD | 41,840,000.00 USD | 1,310,000.00 USD | 152,200.00 USD | 198,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `764.00` | 10,270,000.00 USD | 10,270,000.00 USD | 1,590,000.00 USD | 441,980.00 USD | 402,300.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `764.50` | 76,450.00 USD | 3,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `764.80` | 43,030,000.00 USD | 43,030,000.00 USD | 884,970.00 USD | 155,100.00 USD | 155,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `764.90` | 12,470,000.00 USD | 12,470,000.00 USD | 1,450,000.00 USD | 352,570.00 USD | 395,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `765.60` | 44,230,000.00 USD | 44,230,000.00 USD | 948,980.00 USD | 81,400.00 USD | 169,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `765.80` | 15,460,000.00 USD | 15,460,000.00 USD | 2,470,000.00 USD | 107,550.00 USD | 416,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `766.40` | 45,350,000.00 USD | 45,350,000.00 USD | 427,170.00 USD | 240,890.00 USD | 443,770.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `766.50` | 2,850.00 USD | 3,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `766.70` | 20,050,000.00 USD | 20,050,000.00 USD | 3,330,000.00 USD | 416,530.00 USD | 842,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `767.20` | 48,090,000.00 USD | 48,090,000.00 USD | 2,470,000.00 USD | 47,060.00 USD | 221,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `767.60` | 23,430,000.00 USD | 23,430,000.00 USD | 2,790,000.00 USD | 123,530.00 USD | 467,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `768.00` | 49,430,000.00 USD | 49,430,000.00 USD | 1,080,000.00 USD | 78,680.00 USD | 184,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `768.50` | 25,660,000.00 USD | 25,660,000.00 USD | 1,840,000.00 USD | 95,830.00 USD | 281,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `768.50` | 156.77 USD | 3,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `768.80` | 50,000,000.00 USD | 50,000,000.00 USD | 467,860.00 USD | 54,840.00 USD | 45,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `769.40` | 26,810,000.00 USD | 26,810,000.00 USD | 565,780.00 USD | 249,950.00 USD | 333,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `769.60` | 50,560,000.00 USD | 50,560,000.00 USD | 497,030.00 USD | 49,670.00 USD | 18,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `770.30` | 29,310,000.00 USD | 29,310,000.00 USD | 1,900,000.00 USD | 240,530.00 USD | 364,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `770.40` | 50,730,000.00 USD | 50,730,000.00 USD | 82,200.00 USD | 75,090.00 USD | 9,890.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `770.50` | 881.45 USD | 3,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `771.20` | 51,510,000.00 USD | 51,510,000.00 USD | 279,870.00 USD | 97,820.00 USD | 397,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `771.20` | 30,770,000.00 USD | 30,770,000.00 USD | 1,050,000.00 USD | 242,570.00 USD | 162,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `771.50` | 10,380.00 USD | 3,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `772.00` | 52,480,000.00 USD | 52,480,000.00 USD | 272,790.00 USD | 77,190.00 USD | 617,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `772.10` | 33,190,000.00 USD | 33,190,000.00 USD | 1,750,000.00 USD | 252,650.00 USD | 419,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `772.50` | 849.75 USD | 3,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `772.80` | 53,430,000.00 USD | 53,430,000.00 USD | 693,530.00 USD | 110,530.00 USD | 146,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `773.00` | 35,800,000.00 USD | 35,800,000.00 USD | 1,950,000.00 USD | 325,680.00 USD | 338,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `773.50` | 3,800.00 USD | 3,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `773.60` | 53,750,000.00 USD | 53,750,000.00 USD | 242,430.00 USD | 52,380.00 USD | 27,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `773.90` | 37,600,000.00 USD | 37,600,000.00 USD | 1,220,000.00 USD | 276,760.00 USD | 293,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `774.40` | 54,560,000.00 USD | 54,560,000.00 USD | 791,090.00 USD | 16,900.00 USD | 4,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `774.80` | 39,980,000.00 USD | 39,980,000.00 USD | 1,310,000.00 USD | 568,930.00 USD | 502,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `775.20` | 54,980,000.00 USD | 54,980,000.00 USD | 290,110.00 USD | 49,290.00 USD | 83,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `775.70` | 42,470,000.00 USD | 42,470,000.00 USD | 1,830,000.00 USD | 470,960.00 USD | 187,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `776.00` | 55,080,000.00 USD | 55,080,000.00 USD | 45,110.00 USD | 7,660.00 USD | 49,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `776.50` | 100,020.00 USD | 3,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `776.60` | 44,740,000.00 USD | 44,740,000.00 USD | 1,630,000.00 USD | 269,050.00 USD | 378,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `776.80` | 55,320,000.00 USD | 55,320,000.00 USD | 152,810.00 USD | 4,350.00 USD | 78,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `777.50` | 46,480,000.00 USD | 46,480,000.00 USD | 1,350,000.00 USD | 243,990.00 USD | 148,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `777.50` | 209.15 USD | 3,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `777.60` | 55,950,000.00 USD | 55,950,000.00 USD | 454,390.00 USD | 112,090.00 USD | 67,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `778.40` | 57,070,000.00 USD | 57,070,000.00 USD | 744,850.00 USD | 52,880.00 USD | 315,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `778.40` | 48,170,000.00 USD | 48,170,000.00 USD | 1,180,000.00 USD | 307,370.00 USD | 206,530.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `778.50` | 3,200.00 USD | 3,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `779.20` | 57,910,000.00 USD | 57,910,000.00 USD | 636,170.00 USD | 73,260.00 USD | 138,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `779.30` | 49,730,000.00 USD | 49,730,000.00 USD | 1,240,000.00 USD | 188,170.00 USD | 123,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `780.00` | 58,340,000.00 USD | 58,340,000.00 USD | 293,030.00 USD | 98,680.00 USD | 32,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `780.20` | 51,100,000.00 USD | 51,100,000.00 USD | 1,070,000.00 USD | 86,470.00 USD | 218,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `780.50` | 6,200.00 USD | 3,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `780.80` | 58,840,000.00 USD | 58,840,000.00 USD | 346,180.00 USD | 50,860.00 USD | 103,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `781.10` | 52,710,000.00 USD | 52,710,000.00 USD | 1,270,000.00 USD | 90,990.00 USD | 242,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `781.50` | 1,830.00 USD | 3,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `781.60` | 59,840,000.00 USD | 59,840,000.00 USD | 553,070.00 USD | 90,340.00 USD | 352,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `782.00` | 54,610,000.00 USD | 54,610,000.00 USD | 1,510,000.00 USD | 87,670.00 USD | 301,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `782.40` | 60,840,000.00 USD | 60,840,000.00 USD | 892,310.00 USD | 31,410.00 USD | 82,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `782.90` | 56,600,000.00 USD | 56,600,000.00 USD | 1,750,000.00 USD | 36,140.00 USD | 202,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `783.20` | 61,570,000.00 USD | 61,570,000.00 USD | 600,530.00 USD | 36,240.00 USD | 89,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `783.80` | 57,170,000.00 USD | 57,170,000.00 USD | 508,000.00 USD | 10,100.00 USD | 54,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `784.00` | 61,830,000.00 USD | 61,830,000.00 USD | 253,320.00 USD | 9,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `784.70` | 57,480,000.00 USD | 57,480,000.00 USD | 208,380.00 USD | 28,260.00 USD | 70,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `784.80` | 62,220,000.00 USD | 62,220,000.00 USD | 389,330.00 USD | 2,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `785.50` | 129.61 USD | 3,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `785.60` | 62,300,000.00 USD | 62,300,000.00 USD | 75,370.00 USD | 4,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `785.60` | 58,610,000.00 USD | 58,610,000.00 USD | 1,010,000.00 USD | 54,140.00 USD | 71,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `786.40` | 62,520,000.00 USD | 62,520,000.00 USD | 195,580.00 USD | 3,730.00 USD | 18,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `786.50` | 59,000,000.00 USD | 59,000,000.00 USD | 329,230.00 USD | 30,660.00 USD | 23,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `786.50` | 126,920.00 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `787.20` | 62,560,000.00 USD | 62,560,000.00 USD | 17,590.00 USD | 8,510.00 USD | 14,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `787.40` | 59,580,000.00 USD | 59,580,000.00 USD | 470,050.00 USD | 17,630.00 USD | 91,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `788.00` | 63,360,000.00 USD | 63,360,000.00 USD | 402,300.00 USD | 10,420.00 USD | 389,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `788.30` | 59,940,000.00 USD | 59,940,000.00 USD | 202,630.00 USD | 82,380.00 USD | 81,230.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `788.50` | 2,320.00 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `788.80` | 63,470,000.00 USD | 63,470,000.00 USD | 86,980.00 USD | 21,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `789.20` | 60,780,000.00 USD | 60,780,000.00 USD | 698,830.00 USD | 81,250.00 USD | 55,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `789.60` | 63,940,000.00 USD | 63,940,000.00 USD | 303,290.00 USD | 9,200.00 USD | 158,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `790.10` | 61,270,000.00 USD | 61,270,000.00 USD | 299,250.00 USD | 104,360.00 USD | 88,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `790.40` | 64,210,000.00 USD | 64,210,000.00 USD | 266,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `791.00` | 62,150,000.00 USD | 62,150,000.00 USD | 693,290.00 USD | 82,870.00 USD | 100,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `791.20` | 64,410,000.00 USD | 64,410,000.00 USD | 164,490.00 USD | 33,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `791.90` | 63,030,000.00 USD | 63,030,000.00 USD | 816,380.00 USD | 16,830.00 USD | 46,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `792.00` | 64,570,000.00 USD | 64,570,000.00 USD | 155,970.00 USD | 0.00 USD | 7,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `792.80` | 64,590,000.00 USD | 64,590,000.00 USD | 19,440.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `792.80` | 63,250,000.00 USD | 63,250,000.00 USD | 205,450.00 USD | 0.00 USD | 14,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `793.50` | 3,690.00 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `793.60` | 64,620,000.00 USD | 64,620,000.00 USD | 27,830.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
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
| `1D` | `636.80` | 47,610,000.00 USD | 0.00 USD | 47,610,000.00 USD | 101,910.00 USD | 40,910.00 USD | 275,240.00 USD |
| `1D` | `637.60` | 47,190,000.00 USD | 0.00 USD | 47,190,000.00 USD | 34,750.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `638.40` | 47,160,000.00 USD | 0.00 USD | 47,160,000.00 USD | 24,710.00 USD | 37,610.00 USD | 0.00 USD |
| `1D` | `639.20` | 47,100,000.00 USD | 0.00 USD | 47,100,000.00 USD | 194,520.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `640.00` | 46,900,000.00 USD | 0.00 USD | 46,900,000.00 USD | 21,450.00 USD | 0.00 USD | 184,710.00 USD |
| `1D` | `641.60` | 46,700,000.00 USD | 0.00 USD | 46,700,000.00 USD | 113,990.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `642.40` | 46,580,000.00 USD | 0.00 USD | 46,580,000.00 USD | 122,750.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `643.20` | 46,460,000.00 USD | 0.00 USD | 46,460,000.00 USD | 48,750.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `644.00` | 46,410,000.00 USD | 0.00 USD | 46,410,000.00 USD | 34,060.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `644.80` | 46,380,000.00 USD | 0.00 USD | 46,380,000.00 USD | 354,850.00 USD | 10,420.00 USD | 341,610.00 USD |
| `1D` | `645.60` | 45,670,000.00 USD | 0.00 USD | 45,670,000.00 USD | 64,260.00 USD | 0.00 USD | 17,450.00 USD |
| `1D` | `646.40` | 45,590,000.00 USD | 0.00 USD | 45,590,000.00 USD | 87,020.00 USD | 9,200.00 USD | 140,640.00 USD |
| `1D` | `647.20` | 45,350,000.00 USD | 0.00 USD | 45,350,000.00 USD | 187,370.00 USD | 33,700.00 USD | 0.00 USD |
| `1D` | `648.00` | 45,130,000.00 USD | 0.00 USD | 45,130,000.00 USD | 222,650.00 USD | 0.00 USD | 7,150.00 USD |
| `1D` | `649.60` | 44,900,000.00 USD | 0.00 USD | 44,900,000.00 USD | 96,580.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `650.40` | 44,800,000.00 USD | 0.00 USD | 44,800,000.00 USD | 17,370.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `651.20` | 44,790,000.00 USD | 0.00 USD | 44,790,000.00 USD | 184,040.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `652.00` | 44,600,000.00 USD | 0.00 USD | 44,600,000.00 USD | 0.00 USD | 0.00 USD | 94,590.00 USD |
| `1D` | `652.80` | 44,510,000.00 USD | 0.00 USD | 44,510,000.00 USD | 30,730.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `653.60` | 44,480,000.00 USD | 0.00 USD | 44,480,000.00 USD | 43,630.00 USD | 26,830.00 USD | 0.00 USD |
| `1D` | `654.40` | 44,410,000.00 USD | 0.00 USD | 44,410,000.00 USD | 108,090.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `655.20` | 44,300,000.00 USD | 0.00 USD | 44,300,000.00 USD | 72,460.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `656.00` | 44,230,000.00 USD | 0.00 USD | 44,230,000.00 USD | 190,750.00 USD | 19,650.00 USD | 87,310.00 USD |
| `1D` | `656.80` | 43,930,000.00 USD | 0.00 USD | 43,930,000.00 USD | 134,130.00 USD | 21,320.00 USD | 738,390.00 USD |
| `1D` | `657.60` | 43,040,000.00 USD | 0.00 USD | 43,040,000.00 USD | 227,900.00 USD | 0.00 USD | 21,320.00 USD |
| `1D` | `658.40` | 42,790,000.00 USD | 0.00 USD | 42,790,000.00 USD | 859,170.00 USD | 14,920.00 USD | 0.00 USD |
| `1D` | `659.20` | 41,910,000.00 USD | 0.00 USD | 41,910,000.00 USD | 55,730.00 USD | 7,460.00 USD | 81,440.00 USD |
| `1D` | `660.00` | 41,770,000.00 USD | 0.00 USD | 41,770,000.00 USD | 159,940.00 USD | 0.00 USD | 14,670.00 USD |
| `1D` | `660.80` | 41,590,000.00 USD | 0.00 USD | 41,590,000.00 USD | 0.00 USD | 83,170.00 USD | 0.00 USD |
| `1D` | `661.60` | 41,510,000.00 USD | 0.00 USD | 41,510,000.00 USD | 491,390.00 USD | 19,460.00 USD | 0.00 USD |
| `1D` | `662.40` | 41,000,000.00 USD | 0.00 USD | 41,000,000.00 USD | 199,440.00 USD | 136,330.00 USD | 0.00 USD |
| `1D` | `663.20` | 40,660,000.00 USD | 0.00 USD | 40,660,000.00 USD | 202,030.00 USD | 5,000.00 USD | 44,630.00 USD |
| `1D` | `664.00` | 40,410,000.00 USD | 0.00 USD | 40,410,000.00 USD | 45,960.00 USD | 64,390.00 USD | 64,090.00 USD |
| `7D` | `664.10` | 87,050,000.00 USD | 0.00 USD | 87,050,000.00 USD | 78,740.00 USD | 18,740.00 USD | 39,340.00 USD |
| `1D` | `664.80` | 40,240,000.00 USD | 0.00 USD | 40,240,000.00 USD | 1,340,000.00 USD | 0.00 USD | 64,240.00 USD |
| `7D` | `665.00` | 86,910,000.00 USD | 0.00 USD | 86,910,000.00 USD | 92,030.00 USD | 22,990.00 USD | 37,000.00 USD |
| `1D` | `665.60` | 38,830,000.00 USD | 0.00 USD | 38,830,000.00 USD | 695,710.00 USD | 5,880.00 USD | 8,800.00 USD |
| `7D` | `665.90` | 86,760,000.00 USD | 0.00 USD | 86,760,000.00 USD | 264,020.00 USD | 71,380.00 USD | 63,410.00 USD |
| `1D` | `666.40` | 38,120,000.00 USD | 0.00 USD | 38,120,000.00 USD | 306,600.00 USD | 92,350.00 USD | 778,080.00 USD |
| `7D` | `666.80` | 86,360,000.00 USD | 0.00 USD | 86,360,000.00 USD | 198,550.00 USD | 33,320.00 USD | 61,710.00 USD |
| `1D` | `667.20` | 36,950,000.00 USD | 0.00 USD | 36,950,000.00 USD | 902,780.00 USD | 25,280.00 USD | 13,240.00 USD |
| `7D` | `667.70` | 86,070,000.00 USD | 0.00 USD | 86,070,000.00 USD | 199,690.00 USD | 45,130.00 USD | 51,340.00 USD |
| `1D` | `668.00` | 36,010,000.00 USD | 0.00 USD | 36,010,000.00 USD | 394,550.00 USD | 159,170.00 USD | 0.00 USD |
| `7D` | `668.60` | 85,770,000.00 USD | 0.00 USD | 85,770,000.00 USD | 387,530.00 USD | 92,860.00 USD | 51,060.00 USD |
| `1D` | `668.80` | 35,450,000.00 USD | 0.00 USD | 35,450,000.00 USD | 769,660.00 USD | 30,970.00 USD | 3,620.00 USD |
| `7D` | `669.50` | 85,240,000.00 USD | 0.00 USD | 85,240,000.00 USD | 341,150.00 USD | 38,130.00 USD | 108,970.00 USD |
| `1D` | `669.60` | 34,650,000.00 USD | 0.00 USD | 34,650,000.00 USD | 708,560.00 USD | 100,330.00 USD | 49,300.00 USD |
| `1D` | `670.40` | 33,790,000.00 USD | 0.00 USD | 33,790,000.00 USD | 354,100.00 USD | 10,760.00 USD | 1,480,000.00 USD |
| `7D` | `670.40` | 84,750,000.00 USD | 0.00 USD | 84,750,000.00 USD | 319,660.00 USD | 93,800.00 USD | 77,380.00 USD |
| `1D` | `671.20` | 31,950,000.00 USD | 0.00 USD | 31,950,000.00 USD | 548,370.00 USD | 13,720.00 USD | 48,820.00 USD |
| `7D` | `671.30` | 84,260,000.00 USD | 0.00 USD | 84,260,000.00 USD | 335,750.00 USD | 57,500.00 USD | 42,050.00 USD |
| `1D` | `672.00` | 31,340,000.00 USD | 0.00 USD | 31,340,000.00 USD | 2,080,000.00 USD | 18,180.00 USD | 13,670.00 USD |
| `7D` | `672.20` | 83,830,000.00 USD | 0.00 USD | 83,830,000.00 USD | 180,230.00 USD | 62,620.00 USD | 74,250.00 USD |
| `1D` | `672.80` | 29,220,000.00 USD | 0.00 USD | 29,220,000.00 USD | 192,130.00 USD | 118,570.00 USD | 846,870.00 USD |
| `7D` | `673.10` | 83,510,000.00 USD | 0.00 USD | 83,510,000.00 USD | 394,120.00 USD | 64,970.00 USD | 42,710.00 USD |
| `1D` | `673.60` | 28,060,000.00 USD | 0.00 USD | 28,060,000.00 USD | 201,420.00 USD | 245,910.00 USD | 1,560,000.00 USD |
| `7D` | `674.00` | 83,010,000.00 USD | 0.00 USD | 83,010,000.00 USD | 335,670.00 USD | 105,910.00 USD | 80,360.00 USD |
| `1D` | `674.40` | 26,050,000.00 USD | 0.00 USD | 26,050,000.00 USD | 1,280,000.00 USD | 438,780.00 USD | 207,090.00 USD |
| `7D` | `674.90` | 82,490,000.00 USD | 0.00 USD | 82,490,000.00 USD | 247,070.00 USD | 31,490.00 USD | 44,420.00 USD |
| `1D` | `675.20` | 24,130,000.00 USD | 0.00 USD | 24,130,000.00 USD | 1,140,000.00 USD | 61,020.00 USD | 289,900.00 USD |
| `7D` | `675.80` | 82,160,000.00 USD | 0.00 USD | 82,160,000.00 USD | 387,400.00 USD | 26,020.00 USD | 79,190.00 USD |
| `1D` | `676.00` | 22,630,000.00 USD | 0.00 USD | 22,630,000.00 USD | 626,400.00 USD | 372,550.00 USD | 422,620.00 USD |
| `7D` | `676.70` | 81,670,000.00 USD | 0.00 USD | 81,670,000.00 USD | 509,100.00 USD | 35,490.00 USD | 126,570.00 USD |
| `1D` | `676.80` | 21,210,000.00 USD | 0.00 USD | 21,210,000.00 USD | 340,220.00 USD | 163,630.00 USD | 176,550.00 USD |
| `1D` | `677.60` | 20,530,000.00 USD | 0.00 USD | 20,530,000.00 USD | 295,270.00 USD | 177,920.00 USD | 242,210.00 USD |
| `7D` | `677.60` | 81,000,000.00 USD | 0.00 USD | 81,000,000.00 USD | 409,810.00 USD | 0.00 USD | 63,990.00 USD |
| `1D` | `678.40` | 19,820,000.00 USD | 0.00 USD | 19,820,000.00 USD | 1,240,000.00 USD | 108,180.00 USD | 123,170.00 USD |
| `7D` | `678.50` | 80,530,000.00 USD | 0.00 USD | 80,530,000.00 USD | 120,190.00 USD | 0.00 USD | 26,990.00 USD |
| `1D` | `679.20` | 18,350,000.00 USD | 0.00 USD | 18,350,000.00 USD | 1,360,000.00 USD | 30,070.00 USD | 0.00 USD |
| `7D` | `679.40` | 80,380,000.00 USD | 0.00 USD | 80,380,000.00 USD | 116,510.00 USD | 10,480.00 USD | 40,610.00 USD |
| `1D` | `680.00` | 16,960,000.00 USD | 0.00 USD | 16,960,000.00 USD | 233,510.00 USD | 217,890.00 USD | 298,080.00 USD |
| `7D` | `680.30` | 80,210,000.00 USD | 0.00 USD | 80,210,000.00 USD | 166,780.00 USD | 13,510.00 USD | 0.00 USD |
| `1D` | `680.80` | 16,210,000.00 USD | 0.00 USD | 16,210,000.00 USD | 265,940.00 USD | 126,150.00 USD | 187,330.00 USD |
| `7D` | `681.20` | 80,030,000.00 USD | 0.00 USD | 80,030,000.00 USD | 106,280.00 USD | 7,050.00 USD | 35,170.00 USD |
| `1D` | `681.60` | 15,630,000.00 USD | 0.00 USD | 15,630,000.00 USD | 647,060.00 USD | 414,700.00 USD | 0.00 USD |
| `7D` | `682.10` | 79,880,000.00 USD | 0.00 USD | 79,880,000.00 USD | 0.00 USD | 23,360.00 USD | 27,620.00 USD |
| `1D` | `682.40` | 14,570,000.00 USD | 0.00 USD | 14,570,000.00 USD | 14,340.00 USD | 75,460.00 USD | 0.00 USD |
| `7D` | `683.00` | 79,830,000.00 USD | 0.00 USD | 79,830,000.00 USD | 175,930.00 USD | 28,470.00 USD | 11,520.00 USD |
| `1D` | `683.20` | 14,480,000.00 USD | 0.00 USD | 14,480,000.00 USD | 662,310.00 USD | 0.00 USD | 37,900.00 USD |
| `7D` | `683.90` | 79,620,000.00 USD | 0.00 USD | 79,620,000.00 USD | 77,000.00 USD | 29,510.00 USD | 17,480.00 USD |
| `1D` | `684.00` | 13,780,000.00 USD | 0.00 USD | 13,780,000.00 USD | 380,290.00 USD | 0.00 USD | 38,770.00 USD |
| `1D` | `684.80` | 13,360,000.00 USD | 0.00 USD | 13,360,000.00 USD | 138,250.00 USD | 58,650.00 USD | 0.00 USD |
| `7D` | `684.80` | 79,490,000.00 USD | 0.00 USD | 79,490,000.00 USD | 246,080.00 USD | 9,850.00 USD | 39,550.00 USD |
| `1D` | `685.60` | 13,160,000.00 USD | 0.00 USD | 13,160,000.00 USD | 1,360,000.00 USD | 32,890.00 USD | 0.00 USD |
| `7D` | `685.70` | 79,200,000.00 USD | 0.00 USD | 79,200,000.00 USD | 197,040.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `686.40` | 11,760,000.00 USD | 0.00 USD | 11,760,000.00 USD | 95,060.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `686.60` | 79,000,000.00 USD | 0.00 USD | 79,000,000.00 USD | 62,990.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `687.20` | 11,670,000.00 USD | 0.00 USD | 11,670,000.00 USD | 902,200.00 USD | 152,370.00 USD | 98,790.00 USD |
| `7D` | `687.50` | 78,940,000.00 USD | 0.00 USD | 78,940,000.00 USD | 148,480.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `688.00` | 10,510,000.00 USD | 0.00 USD | 10,510,000.00 USD | 373,380.00 USD | 19,580.00 USD | 180,340.00 USD |
| `7D` | `688.40` | 78,790,000.00 USD | 0.00 USD | 78,790,000.00 USD | 67,880.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `688.80` | 9,940,000.00 USD | 0.00 USD | 9,940,000.00 USD | 116,110.00 USD | 100,620.00 USD | 492,440.00 USD |
| `7D` | `689.30` | 78,720,000.00 USD | 0.00 USD | 78,720,000.00 USD | 84,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `689.60` | 9,230,000.00 USD | 0.00 USD | 9,230,000.00 USD | 0.00 USD | 60,040.00 USD | 773,970.00 USD |
| `7D` | `690.20` | 78,640,000.00 USD | 0.00 USD | 78,640,000.00 USD | 283,920.00 USD | 63,230.00 USD | 82,450.00 USD |
| `1D` | `690.40` | 8,400,000.00 USD | 0.00 USD | 8,400,000.00 USD | 0.00 USD | 34,700.00 USD | 6,440.00 USD |
| `7D` | `691.10` | 78,210,000.00 USD | 0.00 USD | 78,210,000.00 USD | 362,020.00 USD | 61,370.00 USD | 81,090.00 USD |
| `1D` | `691.20` | 8,360,000.00 USD | 0.00 USD | 8,360,000.00 USD | 0.00 USD | 129,500.00 USD | 17,880.00 USD |
| `1D` | `692.00` | 8,210,000.00 USD | 0.00 USD | 8,210,000.00 USD | 0.00 USD | 23,600.00 USD | 0.00 USD |
| `7D` | `692.00` | 77,700,000.00 USD | 0.00 USD | 77,700,000.00 USD | 322,430.00 USD | 18,850.00 USD | 58,910.00 USD |
| `7D` | `692.90` | 77,300,000.00 USD | 0.00 USD | 77,300,000.00 USD | 280,830.00 USD | 19,470.00 USD | 0.00 USD |
| `1D` | `693.60` | 8,180,000.00 USD | 0.00 USD | 8,180,000.00 USD | 0.00 USD | 92,970.00 USD | 273,200.00 USD |
| `7D` | `693.80` | 77,000,000.00 USD | 0.00 USD | 77,000,000.00 USD | 305,720.00 USD | 39,210.00 USD | 0.00 USD |
| `1D` | `694.40` | 7,820,000.00 USD | 0.00 USD | 7,820,000.00 USD | 0.00 USD | 116,660.00 USD | 180,380.00 USD |
| `7D` | `694.70` | 76,660,000.00 USD | 0.00 USD | 76,660,000.00 USD | 279,840.00 USD | 36,640.00 USD | 35,490.00 USD |
| `1D` | `695.20` | 7,520,000.00 USD | 0.00 USD | 7,520,000.00 USD | 239,550.00 USD | 32,370.00 USD | 175,000.00 USD |
| `7D` | `695.60` | 76,300,000.00 USD | 0.00 USD | 76,300,000.00 USD | 120,440.00 USD | 0.00 USD | 21,670.00 USD |
| `1D` | `696.00` | 7,070,000.00 USD | 0.00 USD | 7,070,000.00 USD | 0.00 USD | 66,210.00 USD | 0.00 USD |
| `7D` | `696.50` | 76,160,000.00 USD | 0.00 USD | 76,160,000.00 USD | 140,370.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `696.80` | 7,010,000.00 USD | 0.00 USD | 7,010,000.00 USD | 0.00 USD | 63,720.00 USD | 0.00 USD |
| `7D` | `697.40` | 76,020,000.00 USD | 0.00 USD | 76,020,000.00 USD | 189,100.00 USD | 19,230.00 USD | 0.00 USD |
| `7D` | `698.30` | 75,810,000.00 USD | 0.00 USD | 75,810,000.00 USD | 273,520.00 USD | 33,120.00 USD | 54,800.00 USD |
| `1D` | `698.40` | 6,940,000.00 USD | 0.00 USD | 6,940,000.00 USD | 479,860.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `699.20` | 6,460,000.00 USD | 0.00 USD | 6,460,000.00 USD | 0.00 USD | 31,670.00 USD | 42,650.00 USD |
| `7D` | `699.20` | 75,450,000.00 USD | 0.00 USD | 75,450,000.00 USD | 274,810.00 USD | 12,670.00 USD | 11,820.00 USD |
| `7D` | `700.10` | 75,150,000.00 USD | 0.00 USD | 75,150,000.00 USD | 225,450.00 USD | 40,820.00 USD | 27,440.00 USD |
| `1D` | `700.80` | 6,390,000.00 USD | 0.00 USD | 6,390,000.00 USD | 190,120.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `701.00` | 74,860,000.00 USD | 0.00 USD | 74,860,000.00 USD | 237,800.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `701.60` | 6,200,000.00 USD | 0.00 USD | 6,200,000.00 USD | 0.00 USD | 111,360.00 USD | 0.00 USD |
| `7D` | `701.90` | 74,620,000.00 USD | 0.00 USD | 74,620,000.00 USD | 135,260.00 USD | 41,260.00 USD | 89,700.00 USD |
| `1D` | `702.40` | 6,090,000.00 USD | 0.00 USD | 6,090,000.00 USD | 138,970.00 USD | 39,170.00 USD | 67,790.00 USD |
| `7D` | `702.80` | 74,360,000.00 USD | 0.00 USD | 74,360,000.00 USD | 416,820.00 USD | 57,470.00 USD | 36,720.00 USD |
| `1D` | `703.20` | 5,840,000.00 USD | 0.00 USD | 5,840,000.00 USD | 434,010.00 USD | 45,990.00 USD | 353,820.00 USD |
| `7D` | `703.70` | 73,840,000.00 USD | 0.00 USD | 73,840,000.00 USD | 311,800.00 USD | 44,990.00 USD | 0.00 USD |
| `1D` | `704.00` | 5,010,000.00 USD | 0.00 USD | 5,010,000.00 USD | 0.00 USD | 0.00 USD | 159,030.00 USD |
| `7D` | `704.60` | 73,490,000.00 USD | 0.00 USD | 73,490,000.00 USD | 537,050.00 USD | 136,550.00 USD | 194,460.00 USD |
| `1D` | `704.80` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 0.00 USD | 23,130.00 USD | 12,880.00 USD |
| `7D` | `705.50` | 72,620,000.00 USD | 0.00 USD | 72,620,000.00 USD | 920,340.00 USD | 162,820.00 USD | 236,670.00 USD |
| `1D` | `705.60` | 4,810,000.00 USD | 0.00 USD | 4,810,000.00 USD | 121,180.00 USD | 0.00 USD | 173,230.00 USD |
| `1D` | `706.40` | 4,520,000.00 USD | 0.00 USD | 4,520,000.00 USD | 116,270.00 USD | 0.00 USD | 71,540.00 USD |
| `7D` | `706.40` | 71,300,000.00 USD | 0.00 USD | 71,300,000.00 USD | 523,540.00 USD | 104,380.00 USD | 231,200.00 USD |
| `7D` | `707.30` | 70,440,000.00 USD | 0.00 USD | 70,440,000.00 USD | 604,060.00 USD | 90,200.00 USD | 53,960.00 USD |
| `1D` | `708.00` | 4,330,000.00 USD | 0.00 USD | 4,330,000.00 USD | 201,590.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `708.20` | 69,690,000.00 USD | 0.00 USD | 69,690,000.00 USD | 796,640.00 USD | 138,200.00 USD | 42,800.00 USD |
| `1D` | `708.80` | 4,130,000.00 USD | 0.00 USD | 4,130,000.00 USD | 382,110.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `709.10` | 68,710,000.00 USD | 0.00 USD | 68,710,000.00 USD | 392,150.00 USD | 156,040.00 USD | 195,500.00 USD |
| `7D` | `710.00` | 67,970,000.00 USD | 0.00 USD | 67,970,000.00 USD | 450,480.00 USD | 167,090.00 USD | 176,960.00 USD |
| `1D` | `710.40` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 292,560.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `710.90` | 67,180,000.00 USD | 0.00 USD | 67,180,000.00 USD | 922,450.00 USD | 160,040.00 USD | 236,990.00 USD |
| `1D` | `711.20` | 3,460,000.00 USD | 0.00 USD | 3,460,000.00 USD | 652,220.00 USD | 0.00 USD | 37,900.00 USD |
| `7D` | `711.80` | 65,860,000.00 USD | 0.00 USD | 65,860,000.00 USD | 608,910.00 USD | 232,130.00 USD | 114,740.00 USD |
| `1D` | `712.00` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 0.00 USD | 0.00 USD | 38,770.00 USD |
| `7D` | `712.70` | 64,900,000.00 USD | 0.00 USD | 64,900,000.00 USD | 1,190,000.00 USD | 217,390.00 USD | 236,970.00 USD |
| `1D` | `712.80` | 2,730,000.00 USD | 0.00 USD | 2,730,000.00 USD | 0.00 USD | 0.00 USD | 21,320.00 USD |
| `7D` | `713.60` | 63,260,000.00 USD | 0.00 USD | 63,260,000.00 USD | 2,250,000.00 USD | 279,180.00 USD | 308,960.00 USD |
| `7D` | `714.50` | 60,410,000.00 USD | 0.00 USD | 60,410,000.00 USD | 508,400.00 USD | 209,320.00 USD | 292,980.00 USD |
| `1D` | `715.20` | 2,710,000.00 USD | 0.00 USD | 2,710,000.00 USD | 0.00 USD | 317,060.00 USD | 1,330,000.00 USD |
| `7D` | `715.40` | 59,400,000.00 USD | 0.00 USD | 59,400,000.00 USD | 1,050,000.00 USD | 419,310.00 USD | 329,730.00 USD |
| `1D` | `716.00` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 146,450.00 USD |
| `7D` | `716.30` | 57,600,000.00 USD | 0.00 USD | 57,600,000.00 USD | 1,080,000.00 USD | 324,540.00 USD | 233,140.00 USD |
| `7D` | `717.20` | 55,960,000.00 USD | 0.00 USD | 55,960,000.00 USD | 581,610.00 USD | 398,030.00 USD | 387,120.00 USD |
| `7D` | `718.10` | 54,590,000.00 USD | 0.00 USD | 54,590,000.00 USD | 1,690,000.00 USD | 246,320.00 USD | 151,880.00 USD |
| `1D` | `718.40` | 909,530.00 USD | 0.00 USD | 909,530.00 USD | 656,220.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `719.00` | 52,510,000.00 USD | 0.00 USD | 52,510,000.00 USD | 670,390.00 USD | 137,460.00 USD | 211,490.00 USD |
| `1D` | `719.20` | 253,300.00 USD | 0.00 USD | 253,300.00 USD | 126,360.00 USD | 126,950.00 USD | 0.00 USD |
| `1D` | `719.80` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `719.90` | 51,490,000.00 USD | 0.00 USD | 51,490,000.00 USD | 618,020.00 USD | 173,240.00 USD | 186,780.00 USD |
| `1D` | `720.00` | 170,940.00 USD | 170,940.00 USD | 0.00 USD | 147,340.00 USD | 23,600.00 USD | 0.00 USD |
| `1D` | `720.80` | 525,280.00 USD | 525,280.00 USD | 0.00 USD | 149,800.00 USD | 204,540.00 USD | 0.00 USD |
| `7D` | `720.80` | 50,510,000.00 USD | 0.00 USD | 50,510,000.00 USD | 1,010,000.00 USD | 52,490.00 USD | 180,370.00 USD |
| `1D` | `721.60` | 762,810.00 USD | 762,810.00 USD | 0.00 USD | 100,790.00 USD | 78,640.00 USD | 58,100.00 USD |
| `7D` | `721.70` | 49,260,000.00 USD | 0.00 USD | 49,260,000.00 USD | 1,950,000.00 USD | 237,690.00 USD | 653,400.00 USD |
| `1D` | `722.40` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 28,010.00 USD | 177,770.00 USD | 391,200.00 USD |
| `7D` | `722.60` | 46,430,000.00 USD | 0.00 USD | 46,430,000.00 USD | 1,930,000.00 USD | 108,200.00 USD | 229,380.00 USD |
| `1D` | `723.20` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 191,050.00 USD | 416,750.00 USD | 176,360.00 USD |
| `7D` | `723.50` | 44,160,000.00 USD | 0.00 USD | 44,160,000.00 USD | 640,550.00 USD | 140,550.00 USD | 293,670.00 USD |
| `1D` | `724.00` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 380,140.00 USD | 171,580.00 USD | 88,480.00 USD |
| `7D` | `724.40` | 43,080,000.00 USD | 0.00 USD | 43,080,000.00 USD | 663,550.00 USD | 186,780.00 USD | 130,770.00 USD |
| `1D` | `724.80` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 345,070.00 USD | 45,850.00 USD | 18,950.00 USD |
| `7D` | `725.30` | 42,100,000.00 USD | 0.00 USD | 42,100,000.00 USD | 1,760,000.00 USD | 418,390.00 USD | 396,690.00 USD |
| `1D` | `725.60` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 289,330.00 USD | 120,790.00 USD | 19,390.00 USD |
| `7D` | `726.20` | 39,520,000.00 USD | 0.00 USD | 39,520,000.00 USD | 1,060,000.00 USD | 311,550.00 USD | 460,020.00 USD |
| `1D` | `726.40` | 3,960,000.00 USD | 3,960,000.00 USD | 0.00 USD | 256,420.00 USD | 75,230.00 USD | 0.00 USD |
| `7D` | `727.10` | 37,690,000.00 USD | 0.00 USD | 37,690,000.00 USD | 1,230,000.00 USD | 331,980.00 USD | 241,010.00 USD |
| `1D` | `727.20` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 502,440.00 USD | 10,650.00 USD | 0.00 USD |
| `1D` | `728.00` | 4,680,000.00 USD | 4,680,000.00 USD | 0.00 USD | 159,800.00 USD | 48,110.00 USD | 0.00 USD |
| `7D` | `728.00` | 35,890,000.00 USD | 0.00 USD | 35,890,000.00 USD | 3,110,000.00 USD | 778,750.00 USD | 388,930.00 USD |
| `1D` | `728.80` | 5,260,000.00 USD | 5,260,000.00 USD | 0.00 USD | 278,100.00 USD | 98,780.00 USD | 207,690.00 USD |
| `7D` | `728.90` | 31,610,000.00 USD | 0.00 USD | 31,610,000.00 USD | 2,330,000.00 USD | 317,590.00 USD | 644,150.00 USD |
| `1D` | `729.60` | 6,030,000.00 USD | 6,030,000.00 USD | 0.00 USD | 106,170.00 USD | 205,910.00 USD | 458,580.00 USD |
| `7D` | `729.80` | 28,320,000.00 USD | 0.00 USD | 28,320,000.00 USD | 1,320,000.00 USD | 430,010.00 USD | 339,140.00 USD |
| `1D` | `730.40` | 9,900,000.00 USD | 9,900,000.00 USD | 0.00 USD | 1,690,000.00 USD | 327,540.00 USD | 1,850,000.00 USD |
| `7D` | `730.70` | 26,230,000.00 USD | 0.00 USD | 26,230,000.00 USD | 2,760,000.00 USD | 351,520.00 USD | 587,010.00 USD |
| `1D` | `731.20` | 11,890,000.00 USD | 11,890,000.00 USD | 0.00 USD | 1,360,000.00 USD | 113,710.00 USD | 513,520.00 USD |
| `7D` | `731.60` | 22,530,000.00 USD | 0.00 USD | 22,530,000.00 USD | 1,530,000.00 USD | 133,980.00 USD | 261,910.00 USD |
| `1D` | `732.00` | 12,810,000.00 USD | 12,810,000.00 USD | 0.00 USD | 417,600.00 USD | 139,360.00 USD | 357,510.00 USD |
| `7D` | `732.50` | 20,610,000.00 USD | 0.00 USD | 20,610,000.00 USD | 465,880.00 USD | 221,510.00 USD | 96,400.00 USD |
| `1D` | `732.80` | 15,300,000.00 USD | 15,300,000.00 USD | 0.00 USD | 1,200,000.00 USD | 168,450.00 USD | 1,120,000.00 USD |
| `7D` | `733.40` | 19,820,000.00 USD | 0.00 USD | 19,820,000.00 USD | 1,910,000.00 USD | 158,310.00 USD | 338,540.00 USD |
| `1D` | `733.60` | 16,070,000.00 USD | 16,070,000.00 USD | 0.00 USD | 344,230.00 USD | 255,890.00 USD | 165,900.00 USD |
| `7D` | `734.30` | 17,420,000.00 USD | 0.00 USD | 17,420,000.00 USD | 1,580,000.00 USD | 288,470.00 USD | 244,940.00 USD |
| `1D` | `734.40` | 16,810,000.00 USD | 16,810,000.00 USD | 0.00 USD | 597,780.00 USD | 11,800.00 USD | 132,930.00 USD |
| `1D` | `735.20` | 17,200,000.00 USD | 17,200,000.00 USD | 0.00 USD | 173,750.00 USD | 215,600.00 USD | 0.00 USD |
| `7D` | `735.20` | 15,310,000.00 USD | 0.00 USD | 15,310,000.00 USD | 1,330,000.00 USD | 172,940.00 USD | 437,510.00 USD |
| `1D` | `736.00` | 18,680,000.00 USD | 18,680,000.00 USD | 0.00 USD | 702,000.00 USD | 52,260.00 USD | 727,530.00 USD |
| `7D` | `736.10` | 13,370,000.00 USD | 0.00 USD | 13,370,000.00 USD | 2,130,000.00 USD | 181,990.00 USD | 484,910.00 USD |
| `1D` | `736.80` | 19,370,000.00 USD | 19,370,000.00 USD | 0.00 USD | 542,490.00 USD | 58,820.00 USD | 90,190.00 USD |
| `7D` | `737.00` | 10,570,000.00 USD | 0.00 USD | 10,570,000.00 USD | 2,360,000.00 USD | 175,330.00 USD | 633,690.00 USD |
| `1D` | `737.60` | 19,920,000.00 USD | 19,920,000.00 USD | 0.00 USD | 329,040.00 USD | 126,150.00 USD | 87,500.00 USD |
| `7D` | `737.90` | 7,400,000.00 USD | 0.00 USD | 7,400,000.00 USD | 3,420,000.00 USD | 72,280.00 USD | 374,090.00 USD |
| `1D` | `738.40` | 20,630,000.00 USD | 20,630,000.00 USD | 0.00 USD | 627,690.00 USD | 85,790.00 USD | 0.00 USD |
| `7D` | `738.80` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 522,950.00 USD | 20,210.00 USD | 155,300.00 USD |
| `1D` | `739.20` | 21,910,000.00 USD | 21,910,000.00 USD | 0.00 USD | 294,170.00 USD | 47,890.00 USD | 934,700.00 USD |
| `7D` | `739.70` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 352,500.00 USD | 0.00 USD | 203,030.00 USD |
| `1D` | `740.00` | 22,150,000.00 USD | 22,150,000.00 USD | 0.00 USD | 245,960.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `740.60` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 1,090,000.00 USD | 0.00 USD | 33,390.00 USD |
| `1D` | `740.80` | 22,560,000.00 USD | 22,560,000.00 USD | 0.00 USD | 246,020.00 USD | 166,390.00 USD | 0.00 USD |
| `7D` | `741.50` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 257,630.00 USD | 0.00 USD | 208,590.00 USD |
| `1D` | `741.60` | 23,290,000.00 USD | 23,290,000.00 USD | 0.00 USD | 707,380.00 USD | 15,840.00 USD | 0.00 USD |
| `7D` | `742.40` | 689,850.00 USD | 0.00 USD | 689,850.00 USD | 0.00 USD | 0.00 USD | 183,920.00 USD |
| `1D` | `743.20` | 23,540,000.00 USD | 23,540,000.00 USD | 0.00 USD | 250,640.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `743.30` | 505,930.00 USD | 0.00 USD | 505,930.00 USD | 0.00 USD | 0.00 USD | 57,580.00 USD |
| `1D` | `744.00` | 24,100,000.00 USD | 24,100,000.00 USD | 0.00 USD | 16,710.00 USD | 106,580.00 USD | 436,560.00 USD |
| `7D` | `744.20` | 448,350.00 USD | 0.00 USD | 448,350.00 USD | 0.00 USD | 257,580.00 USD | 141,790.00 USD |
| `1D` | `744.80` | 26,010,000.00 USD | 26,010,000.00 USD | 0.00 USD | 979,590.00 USD | 55,680.00 USD | 880,130.00 USD |
| `7D` | `745.10` | 48,980.00 USD | 0.00 USD | 48,980.00 USD | 0.00 USD | 48,980.00 USD | 0.00 USD |
| `7D` | `745.20` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `745.60` | 26,650,000.00 USD | 26,650,000.00 USD | 0.00 USD | 503,610.00 USD | 94,190.00 USD | 34,550.00 USD |
| `7D` | `746.00` | 999,320.00 USD | 999,320.00 USD | 0.00 USD | 999,320.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `746.40` | 27,710,000.00 USD | 27,710,000.00 USD | 0.00 USD | 451,300.00 USD | 54,670.00 USD | 557,330.00 USD |
| `7D` | `746.90` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 215,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `747.20` | 28,630,000.00 USD | 28,630,000.00 USD | 0.00 USD | 443,820.00 USD | 67,980.00 USD | 406,120.00 USD |
| `1D` | `748.00` | 29,130,000.00 USD | 29,130,000.00 USD | 0.00 USD | 342,940.00 USD | 84,260.00 USD | 79,770.00 USD |
| `1D` | `748.80` | 29,570,000.00 USD | 29,570,000.00 USD | 0.00 USD | 415,650.00 USD | 0.00 USD | 17,880.00 USD |
| `1D` | `749.60` | 29,740,000.00 USD | 29,740,000.00 USD | 0.00 USD | 175,730.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `750.40` | 29,790,000.00 USD | 29,790,000.00 USD | 0.00 USD | 51,080.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `751.20` | 30,000,000.00 USD | 30,000,000.00 USD | 0.00 USD | 108,960.00 USD | 0.00 USD | 98,240.00 USD |
| `1D` | `752.00` | 30,530,000.00 USD | 30,530,000.00 USD | 0.00 USD | 66,060.00 USD | 25,010.00 USD | 441,380.00 USD |
| `1D` | `752.80` | 30,870,000.00 USD | 30,870,000.00 USD | 0.00 USD | 334,780.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `753.60` | 31,610,000.00 USD | 31,610,000.00 USD | 0.00 USD | 421,210.00 USD | 31,700.00 USD | 289,240.00 USD |
| `1D` | `754.40` | 31,760,000.00 USD | 31,760,000.00 USD | 0.00 USD | 92,070.00 USD | 42,960.00 USD | 16,910.00 USD |
| `7D` | `755.00` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 59,560.00 USD | 0.00 USD |
| `1D` | `755.20` | 32,300,000.00 USD | 32,300,000.00 USD | 0.00 USD | 300,910.00 USD | 201,730.00 USD | 37,120.00 USD |
| `1D` | `756.00` | 32,840,000.00 USD | 32,840,000.00 USD | 0.00 USD | 406,880.00 USD | 69,210.00 USD | 66,220.00 USD |
| `1D` | `756.80` | 33,020,000.00 USD | 33,020,000.00 USD | 0.00 USD | 119,600.00 USD | 8,490.00 USD | 49,060.00 USD |
| `7D` | `756.80` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 47,340.00 USD | 0.00 USD |
| `1D` | `757.60` | 33,460,000.00 USD | 33,460,000.00 USD | 0.00 USD | 223,870.00 USD | 179,910.00 USD | 32,720.00 USD |
| `7D` | `757.70` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 475,510.00 USD | 113,240.00 USD | 0.00 USD |
| `1D` | `758.40` | 34,410,000.00 USD | 34,410,000.00 USD | 0.00 USD | 699,690.00 USD | 34,450.00 USD | 218,280.00 USD |
| `7D` | `758.60` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `759.20` | 35,490,000.00 USD | 35,490,000.00 USD | 0.00 USD | 905,380.00 USD | 117,910.00 USD | 54,810.00 USD |
| `1D` | `760.00` | 35,840,000.00 USD | 35,840,000.00 USD | 0.00 USD | 305,690.00 USD | 21,070.00 USD | 28,610.00 USD |
| `7D` | `760.40` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 0.00 USD | 27,650.00 USD | 42,540.00 USD |
| `1D` | `760.80` | 36,380,000.00 USD | 36,380,000.00 USD | 0.00 USD | 448,300.00 USD | 52,630.00 USD | 40,340.00 USD |
| `7D` | `761.30` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 10,750.00 USD | 211,960.00 USD | 100,630.00 USD |
| `1D` | `761.60` | 37,260,000.00 USD | 37,260,000.00 USD | 0.00 USD | 559,960.00 USD | 27,330.00 USD | 286,260.00 USD |
| `7D` | `762.20` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 699,820.00 USD | 179,270.00 USD |
| `1D` | `762.40` | 37,780,000.00 USD | 37,780,000.00 USD | 0.00 USD | 335,720.00 USD | 105,730.00 USD | 82,030.00 USD |
| `7D` | `763.10` | 7,830,000.00 USD | 7,830,000.00 USD | 0.00 USD | 2,460,000.00 USD | 590,460.00 USD | 404,720.00 USD |
| `1D` | `763.20` | 40,180,000.00 USD | 40,180,000.00 USD | 0.00 USD | 1,710,000.00 USD | 168,160.00 USD | 522,470.00 USD |
| `1D` | `764.00` | 41,840,000.00 USD | 41,840,000.00 USD | 0.00 USD | 1,310,000.00 USD | 152,200.00 USD | 198,610.00 USD |
| `7D` | `764.00` | 10,270,000.00 USD | 10,270,000.00 USD | 0.00 USD | 1,590,000.00 USD | 441,980.00 USD | 402,300.00 USD |
| `1D` | `764.80` | 43,030,000.00 USD | 43,030,000.00 USD | 0.00 USD | 884,970.00 USD | 155,100.00 USD | 155,720.00 USD |
| `7D` | `764.90` | 12,470,000.00 USD | 12,470,000.00 USD | 0.00 USD | 1,450,000.00 USD | 352,570.00 USD | 395,630.00 USD |
| `1D` | `765.60` | 44,230,000.00 USD | 44,230,000.00 USD | 0.00 USD | 948,980.00 USD | 81,400.00 USD | 169,050.00 USD |
| `7D` | `765.80` | 15,460,000.00 USD | 15,460,000.00 USD | 0.00 USD | 2,470,000.00 USD | 107,550.00 USD | 416,290.00 USD |
| `1D` | `766.40` | 45,350,000.00 USD | 45,350,000.00 USD | 0.00 USD | 427,170.00 USD | 240,890.00 USD | 443,770.00 USD |
| `7D` | `766.70` | 20,050,000.00 USD | 20,050,000.00 USD | 0.00 USD | 3,330,000.00 USD | 416,530.00 USD | 842,330.00 USD |
| `1D` | `767.20` | 48,090,000.00 USD | 48,090,000.00 USD | 0.00 USD | 2,470,000.00 USD | 47,060.00 USD | 221,640.00 USD |
| `7D` | `767.60` | 23,430,000.00 USD | 23,430,000.00 USD | 0.00 USD | 2,790,000.00 USD | 123,530.00 USD | 467,840.00 USD |
| `1D` | `768.00` | 49,430,000.00 USD | 49,430,000.00 USD | 0.00 USD | 1,080,000.00 USD | 78,680.00 USD | 184,050.00 USD |
| `7D` | `768.50` | 25,660,000.00 USD | 25,660,000.00 USD | 0.00 USD | 1,840,000.00 USD | 95,830.00 USD | 281,920.00 USD |
| `1D` | `768.80` | 50,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 467,860.00 USD | 54,840.00 USD | 45,440.00 USD |
| `7D` | `769.40` | 26,810,000.00 USD | 26,810,000.00 USD | 0.00 USD | 565,780.00 USD | 249,950.00 USD | 333,550.00 USD |
| `1D` | `769.60` | 50,560,000.00 USD | 50,560,000.00 USD | 0.00 USD | 497,030.00 USD | 49,670.00 USD | 18,560.00 USD |
| `7D` | `770.30` | 29,310,000.00 USD | 29,310,000.00 USD | 0.00 USD | 1,900,000.00 USD | 240,530.00 USD | 364,650.00 USD |
| `1D` | `770.40` | 50,730,000.00 USD | 50,730,000.00 USD | 0.00 USD | 82,200.00 USD | 75,090.00 USD | 9,890.00 USD |
| `1D` | `771.20` | 51,510,000.00 USD | 51,510,000.00 USD | 0.00 USD | 279,870.00 USD | 97,820.00 USD | 397,910.00 USD |
| `7D` | `771.20` | 30,770,000.00 USD | 30,770,000.00 USD | 0.00 USD | 1,050,000.00 USD | 242,570.00 USD | 162,680.00 USD |
| `1D` | `772.00` | 52,480,000.00 USD | 52,480,000.00 USD | 0.00 USD | 272,790.00 USD | 77,190.00 USD | 617,970.00 USD |
| `7D` | `772.10` | 33,190,000.00 USD | 33,190,000.00 USD | 0.00 USD | 1,750,000.00 USD | 252,650.00 USD | 419,070.00 USD |
| `1D` | `772.80` | 53,430,000.00 USD | 53,430,000.00 USD | 0.00 USD | 693,530.00 USD | 110,530.00 USD | 146,010.00 USD |
| `7D` | `773.00` | 35,800,000.00 USD | 35,800,000.00 USD | 0.00 USD | 1,950,000.00 USD | 325,680.00 USD | 338,170.00 USD |
| `1D` | `773.60` | 53,750,000.00 USD | 53,750,000.00 USD | 0.00 USD | 242,430.00 USD | 52,380.00 USD | 27,410.00 USD |
| `7D` | `773.90` | 37,600,000.00 USD | 37,600,000.00 USD | 0.00 USD | 1,220,000.00 USD | 276,760.00 USD | 293,960.00 USD |
| `1D` | `774.40` | 54,560,000.00 USD | 54,560,000.00 USD | 0.00 USD | 791,090.00 USD | 16,900.00 USD | 4,180.00 USD |
| `7D` | `774.80` | 39,980,000.00 USD | 39,980,000.00 USD | 0.00 USD | 1,310,000.00 USD | 568,930.00 USD | 502,710.00 USD |
| `1D` | `775.20` | 54,980,000.00 USD | 54,980,000.00 USD | 0.00 USD | 290,110.00 USD | 49,290.00 USD | 83,340.00 USD |
| `7D` | `775.70` | 42,470,000.00 USD | 42,470,000.00 USD | 0.00 USD | 1,830,000.00 USD | 470,960.00 USD | 187,170.00 USD |
| `1D` | `776.00` | 55,080,000.00 USD | 55,080,000.00 USD | 0.00 USD | 45,110.00 USD | 7,660.00 USD | 49,120.00 USD |
| `7D` | `776.60` | 44,740,000.00 USD | 44,740,000.00 USD | 0.00 USD | 1,630,000.00 USD | 269,050.00 USD | 378,590.00 USD |
| `1D` | `776.80` | 55,320,000.00 USD | 55,320,000.00 USD | 0.00 USD | 152,810.00 USD | 4,350.00 USD | 78,730.00 USD |
| `7D` | `777.50` | 46,480,000.00 USD | 46,480,000.00 USD | 0.00 USD | 1,350,000.00 USD | 243,990.00 USD | 148,450.00 USD |
| `1D` | `777.60` | 55,950,000.00 USD | 55,950,000.00 USD | 0.00 USD | 454,390.00 USD | 112,090.00 USD | 67,060.00 USD |
| `1D` | `778.40` | 57,070,000.00 USD | 57,070,000.00 USD | 0.00 USD | 744,850.00 USD | 52,880.00 USD | 315,610.00 USD |
| `7D` | `778.40` | 48,170,000.00 USD | 48,170,000.00 USD | 0.00 USD | 1,180,000.00 USD | 307,370.00 USD | 206,530.00 USD |
| `1D` | `779.20` | 57,910,000.00 USD | 57,910,000.00 USD | 0.00 USD | 636,170.00 USD | 73,260.00 USD | 138,550.00 USD |
| `7D` | `779.30` | 49,730,000.00 USD | 49,730,000.00 USD | 0.00 USD | 1,240,000.00 USD | 188,170.00 USD | 123,650.00 USD |
| `1D` | `780.00` | 58,340,000.00 USD | 58,340,000.00 USD | 0.00 USD | 293,030.00 USD | 98,680.00 USD | 32,780.00 USD |
| `7D` | `780.20` | 51,100,000.00 USD | 51,100,000.00 USD | 0.00 USD | 1,070,000.00 USD | 86,470.00 USD | 218,750.00 USD |
| `1D` | `780.80` | 58,840,000.00 USD | 58,840,000.00 USD | 0.00 USD | 346,180.00 USD | 50,860.00 USD | 103,250.00 USD |
| `7D` | `781.10` | 52,710,000.00 USD | 52,710,000.00 USD | 0.00 USD | 1,270,000.00 USD | 90,990.00 USD | 242,450.00 USD |
| `1D` | `781.60` | 59,840,000.00 USD | 59,840,000.00 USD | 0.00 USD | 553,070.00 USD | 90,340.00 USD | 352,430.00 USD |
| `7D` | `782.00` | 54,610,000.00 USD | 54,610,000.00 USD | 0.00 USD | 1,510,000.00 USD | 87,670.00 USD | 301,190.00 USD |
| `1D` | `782.40` | 60,840,000.00 USD | 60,840,000.00 USD | 0.00 USD | 892,310.00 USD | 31,410.00 USD | 82,100.00 USD |
| `7D` | `782.90` | 56,600,000.00 USD | 56,600,000.00 USD | 0.00 USD | 1,750,000.00 USD | 36,140.00 USD | 202,700.00 USD |
| `1D` | `783.20` | 61,570,000.00 USD | 61,570,000.00 USD | 0.00 USD | 600,530.00 USD | 36,240.00 USD | 89,540.00 USD |
| `7D` | `783.80` | 57,170,000.00 USD | 57,170,000.00 USD | 0.00 USD | 508,000.00 USD | 10,100.00 USD | 54,380.00 USD |
| `1D` | `784.00` | 61,830,000.00 USD | 61,830,000.00 USD | 0.00 USD | 253,320.00 USD | 9,040.00 USD | 0.00 USD |
| `7D` | `784.70` | 57,480,000.00 USD | 57,480,000.00 USD | 0.00 USD | 208,380.00 USD | 28,260.00 USD | 70,300.00 USD |
| `1D` | `784.80` | 62,220,000.00 USD | 62,220,000.00 USD | 0.00 USD | 389,330.00 USD | 2,690.00 USD | 0.00 USD |
| `1D` | `785.60` | 62,300,000.00 USD | 62,300,000.00 USD | 0.00 USD | 75,370.00 USD | 4,490.00 USD | 0.00 USD |
| `7D` | `785.60` | 58,610,000.00 USD | 58,610,000.00 USD | 0.00 USD | 1,010,000.00 USD | 54,140.00 USD | 71,180.00 USD |
| `1D` | `786.40` | 62,520,000.00 USD | 62,520,000.00 USD | 0.00 USD | 195,580.00 USD | 3,730.00 USD | 18,430.00 USD |
| `7D` | `786.50` | 59,000,000.00 USD | 59,000,000.00 USD | 0.00 USD | 329,230.00 USD | 30,660.00 USD | 23,970.00 USD |
| `1D` | `787.20` | 62,560,000.00 USD | 62,560,000.00 USD | 0.00 USD | 17,590.00 USD | 8,510.00 USD | 14,270.00 USD |
| `7D` | `787.40` | 59,580,000.00 USD | 59,580,000.00 USD | 0.00 USD | 470,050.00 USD | 17,630.00 USD | 91,050.00 USD |
| `1D` | `788.00` | 63,360,000.00 USD | 63,360,000.00 USD | 0.00 USD | 402,300.00 USD | 10,420.00 USD | 389,640.00 USD |
| `7D` | `788.30` | 59,940,000.00 USD | 59,940,000.00 USD | 0.00 USD | 202,630.00 USD | 82,380.00 USD | 81,230.00 USD |
| `1D` | `788.80` | 63,470,000.00 USD | 63,470,000.00 USD | 0.00 USD | 86,980.00 USD | 21,660.00 USD | 0.00 USD |
| `7D` | `789.20` | 60,780,000.00 USD | 60,780,000.00 USD | 0.00 USD | 698,830.00 USD | 81,250.00 USD | 55,990.00 USD |
| `1D` | `789.60` | 63,940,000.00 USD | 63,940,000.00 USD | 0.00 USD | 303,290.00 USD | 9,200.00 USD | 158,090.00 USD |
| `7D` | `790.10` | 61,270,000.00 USD | 61,270,000.00 USD | 0.00 USD | 299,250.00 USD | 104,360.00 USD | 88,890.00 USD |
| `1D` | `790.40` | 64,210,000.00 USD | 64,210,000.00 USD | 0.00 USD | 266,490.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `791.00` | 62,150,000.00 USD | 62,150,000.00 USD | 0.00 USD | 693,290.00 USD | 82,870.00 USD | 100,420.00 USD |
| `1D` | `791.20` | 64,410,000.00 USD | 64,410,000.00 USD | 0.00 USD | 164,490.00 USD | 33,700.00 USD | 0.00 USD |
| `7D` | `791.90` | 63,030,000.00 USD | 63,030,000.00 USD | 0.00 USD | 816,380.00 USD | 16,830.00 USD | 46,300.00 USD |
| `1D` | `792.00` | 64,570,000.00 USD | 64,570,000.00 USD | 0.00 USD | 155,970.00 USD | 0.00 USD | 7,150.00 USD |
| `1D` | `792.80` | 64,590,000.00 USD | 64,590,000.00 USD | 0.00 USD | 19,440.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `792.80` | 63,250,000.00 USD | 63,250,000.00 USD | 0.00 USD | 205,450.00 USD | 0.00 USD | 14,670.00 USD |
| `1D` | `793.60` | 64,620,000.00 USD | 64,620,000.00 USD | 0.00 USD | 27,830.00 USD | 0.00 USD | 0.00 USD |
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
  * Total Open Interest: `1.33B` | Total OI Tokens: `1,844,197.0 BNB`
  * 1h OI Change: `+0.32%` | 4h OI Change: `-0.80%` | 24h OI Change: `+6.24%`
  * Exchange Breakdown: Binance=`576.32M` | Bybit=`136.53M` | OKX=`66.03M` | Hyperliquid=`71.93M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-150.85K` | Last 24h: `-51.15K` | Last 3d: `142.23K` | Last 7d: `346.08K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0000%` | **USDT OKX** | `-0.0648%` |
| **USDT Bybit** | `-0.0798%` | **USDT KuCoin** | `-0.0171%` |
| **USDT MEXC** | `0.0000%` | **USDT BingX** | `0.0050%` |
| **USDT Gate** | `-0.0117%` | **USDT Bitget** | `-0.0077%` |
| **CoinM Binance** | `0.1306%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `BNB` | `58.02%` | `41.98%` | `1.38` | 16,750,000.00 USD |
| `15M` | `Binance` | `52.5%` | `47.5%` | `1.11` | 9,770,000.00 USD |
| `15M` | `OKX` | `59.18%` | `40.82%` | `1.45` | 1,510,000.00 USD |
| `15M` | `Bybit` | `71.39%` | `28.61%` | `2.50` | 971,780.00 USD |
| `15M` | `KuCoin` | `51.06%` | `48.94%` | `1.04` | 191,970.00 USD |
| `15M` | `Gate` | `58.11%` | `41.89%` | `1.39` | 742,140.00 USD |
| `15M` | `Bitget` | `70.41%` | `29.59%` | `2.38` | 609,340.00 USD |
| `15M` | `BingX` | `60.71%` | `39.29%` | `1.55` | 409,230.00 USD |
| `15M` | `MEXC` | `62.67%` | `37.33%` | `1.68` | 239,800.00 USD |
| `15M` | `Bitunix` | `54.18%` | `45.82%` | `1.18` | 363,560.00 USD |
| `15M` | `Hyperliquid` | `85.22%` | `14.78%` | `5.77` | 1,420,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.26%` | `49.74%` | `1.01` | 75,690.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `21.44%` | `78.56%` | `0.27` | 32,690.00 USD |
| `15M` | `HTX` | `65.81%` | `34.19%` | `1.92` | 32,960.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `31.37%` | `68.63%` | `0.46` | 289,260.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `84.99%` | `15.01%` | `5.66` | 93,350.00 USD |
| `15M` | `Whale Positions` | `52.5%` | `47.5%` | `1.11` | 9,770,000.00 USD |
| `15M` | `Global Accounts` | `58.02%` | `41.98%` | `1.38` | 16,750,000.00 USD |
| `1H` | `BNB` | `51.01%` | `48.99%` | `1.04` | 60,900,000.00 USD |
| `1H` | `Binance` | `47.64%` | `52.36%` | `0.91` | 38,800,000.00 USD |
| `1H` | `OKX` | `52.37%` | `47.63%` | `1.10` | 5,230,000.00 USD |
| `1H` | `Bybit` | `60.74%` | `39.26%` | `1.55` | 3,540,000.00 USD |
| `1H` | `KuCoin` | `51.98%` | `48.02%` | `1.08` | 582,440.00 USD |
| `1H` | `Gate` | `56.18%` | `43.82%` | `1.28` | 2,560,000.00 USD |
| `1H` | `Bitget` | `59.78%` | `40.22%` | `1.49` | 1,600,000.00 USD |
| `1H` | `BingX` | `44.75%` | `55.25%` | `0.81` | 1,440,000.00 USD |
| `1H` | `MEXC` | `71.26%` | `28.74%` | `2.48` | 1,040,000.00 USD |
| `1H` | `Bitunix` | `52.47%` | `47.53%` | `1.10` | 1,310,000.00 USD |
| `1H` | `Hyperliquid` | `70.18%` | `29.82%` | `2.35` | 2,810,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.8%` | `49.2%` | `1.03` | 195,060.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `21.29%` | `78.71%` | `0.27` | 99,380.00 USD |
| `1H` | `HTX` | `48.77%` | `51.23%` | `0.95` | 129,130.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `48.46%` | `51.54%` | `0.94` | 1,160,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `51.28%` | `48.72%` | `1.05` | 407,480.00 USD |
| `1H` | `Whale Positions` | `47.64%` | `52.36%` | `0.91` | 38,800,000.00 USD |
| `1H` | `Global Accounts` | `51.01%` | `48.99%` | `1.04` | 60,900,000.00 USD |
| `4H` | `BNB` | `49.09%` | `50.91%` | `0.96` | 567,000,000.00 USD |
| `4H` | `Binance` | `47.86%` | `52.14%` | `0.92` | 359,460,000.00 USD |
| `4H` | `OKX` | `45.97%` | `54.03%` | `0.85` | 53,770,000.00 USD |
| `4H` | `Bybit` | `57.85%` | `42.15%` | `1.37` | 41,100,000.00 USD |
| `4H` | `KuCoin` | `53.84%` | `46.16%` | `1.17` | 3,420,000.00 USD |
| `4H` | `Gate` | `49.19%` | `50.81%` | `0.97` | 17,280,000.00 USD |
| `4H` | `Bitget` | `51.31%` | `48.69%` | `1.05` | 11,480,000.00 USD |
| `4H` | `BingX` | `37.45%` | `62.55%` | `0.60` | 10,630,000.00 USD |
| `4H` | `MEXC` | `56.05%` | `43.95%` | `1.28` | 5,390,000.00 USD |
| `4H` | `Bitunix` | `49.26%` | `50.74%` | `0.97` | 13,460,000.00 USD |
| `4H` | `Hyperliquid` | `58.89%` | `41.11%` | `1.43` | 26,680,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.83%` | `50.17%` | `0.99` | 3,510,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `30.58%` | `69.42%` | `0.44` | 455,960.00 USD |
| `4H` | `HTX` | `41.74%` | `58.26%` | `0.72` | 2,130,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `70.7%` | `29.3%` | `2.41` | 1,770,000.00 USD |
| `4H` | `Aster` | `52.01%` | `47.99%` | `1.08` | 12,380,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `43.93%` | `56.07%` | `0.78` | 4,110,000.00 USD |
| `4H` | `Whale Positions` | `47.86%` | `52.14%` | `0.92` | 359,460,000.00 USD |
| `4H` | `Global Accounts` | `49.09%` | `50.91%` | `0.96` | 567,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `711.15` | `711.54` | `711.15` | `714.45` | `709.95` | 13,903,836.91 USD | 6,352,852.84 USD | 7,550,984.08 USD | -1,198,131.24 USD | `-8.62%` | `1B / 4S` |
| `0:00 UTC` | `711.75` | `711.23` | `711.75` | `712.95` | `708.45` | 13,559,921.70 USD | 6,659,796.80 USD | 6,900,124.90 USD | -240,328.10 USD | `-1.77%` | `1B / 4S` |
| `5:00 UTC` | `708.45` | `709.07` | `708.45` | `710.55` | `708.15` | 7,713,838.94 USD | 3,792,445.03 USD | 3,921,393.91 USD | -128,948.88 USD | `-1.67%` | `0B / 0S` |
| `0:00 UTC` | `717.15` | `715.03` | `717.15` | `717.45` | `709.35` | 18,001,107.25 USD | 10,590,792.94 USD | 7,410,314.32 USD | 3,180,478.62 USD | `+17.67%` | `10B / 0S` |
| `5:00 UTC` | `718.65` | `718.30` | `718.65` | `719.85` | `716.85` | 14,406,892.83 USD | 6,892,738.14 USD | 7,514,154.69 USD | -621,416.55 USD | `-4.31%` | `1B / 0S` |
| `0:00 UTC` | `716.85` | `716.98` | `716.85` | `719.55` | `715.05` | 10,882,676.97 USD | 3,981,765.95 USD | 6,900,911.02 USD | -2,919,145.07 USD | `-26.82%` | `0B / 0S` |
| `5:00 UTC` | `717.15` | `717.39` | `717.15` | `718.65` | `716.25` | 6,978,599.94 USD | 3,350,532.71 USD | 3,628,067.23 USD | -277,534.53 USD | `-3.98%` | `0B / 0S` |
| `0:00 UTC` | `717.45` | `717.74` | `717.45` | `719.55` | `716.55` | 5,355,538.86 USD | 2,861,377.69 USD | 2,494,161.17 USD | 367,216.51 USD | `+6.86%` | `2B / 1S` |
| `5:00 UTC` | `717.45` | `717.28` | `717.45` | `718.05` | `716.55` | 4,945,586.67 USD | 2,313,018.42 USD | 2,632,568.25 USD | -319,549.83 USD | `-6.46%` | `0B / 2S` |
| `0:00 UTC` | `720.15` | `719.65` | `720.15` | `721.05` | `716.55` | 6,082,512.09 USD | 3,667,736.64 USD | 2,414,775.45 USD | 1,252,961.19 USD | `+20.60%` | `3B / 1S` |

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
| `5m` | 557,700.00 USD | 1,520,000.00 USD | **`ACCUMULATION`** |
| `15m` | 629,180.00 USD | 1,120,000.00 USD | **`ACCUMULATION`** |
| `30m` | 973,680.00 USD | 1,910,000.00 USD | **`ACCUMULATION`** |
| `1h` | 641,840.00 USD | -801,690.00 USD | **`DISTRIBUTION`** |
| `2h` | 3,400,000.00 USD | -104,480.00 USD | **`ACCUMULATION`** |
| `4h` | -3,830,000.00 USD | -12,750,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -13,930,000.00 USD | -20,070,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -10,940,000.00 USD | -63,510,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -28,530,000.00 USD | -64,390,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -30,360,000.00 USD | -82,250,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -56,570,000.00 USD | -107,490,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -155,610,000.00 USD | -437,030,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+557.70K` | 15m=`+629.18K` | 1h=`+641.84K` | 24h=`-30.36M`
* Futures Capital Netflows: 5m=`+1.52M` | 15m=`+1.12M` | 1h=`-801.69K` | 24h=`-82.25M`
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
  * `2026-10-30 09:51:14 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:39:14 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:38:14 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:38:14 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:38:14 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:40:14 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:40:14 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:40:14 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:40:14 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:40:14 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:40:14 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:40:14 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:40:14 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:40:14 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:40:14 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `698.03` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `691.07` (Risk Distance: `6.96` pts)
  * +2.5R Take Profit: `715.42`
  * Mathematical Lot Sizing: **`1.43 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `714.63` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `721.59` (Risk Distance: `6.96` pts)
  * +2.5R Take Profit: `697.24`
  * Mathematical Lot Sizing: **`1.43 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`724.25`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
