# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BNB
**Canonical Key**: `BNB` | **Broker Instrument**: `BNBUSD.p` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 09:34:18 IST` (`2026-10-30 04:04:18 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
  * Session VWAP: `715.50` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.79` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `720.51` | Lower -3.00σ Band: `710.49`
  * Upper +2.51σ Band: `719.44` | Lower -2.51σ Band: `711.56`
  * Upper +2.01σ Band: `718.51` | Lower -2.01σ Band: `712.49`
  * Upper +2.00σ Band: `718.36` | Lower -2.00σ Band: `712.64`
  * Upper +1.28σ Band: `717.50` | Lower -1.28σ Band: `713.50`
  * Upper +1.00σ Band: `716.93` | Lower -1.00σ Band: `714.07`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`715.50` | EMA-20=`715.50` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`715.50` (Slope: `+0.0000`) | EMA-100=`715.50`
  * Institutional Anchors: EMA-144=`715.50` | EMA-200=`715.50` (Slope: `+0.0000`) | EMA-233=`715.50`
- **Range Boundaries**: 24H High=`722.65` | 24H Low=`708.35` | Weekly High=`729.81` | Weekly Low=`701.19`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `714.32` (Distance: `+0.10%`)
  * Point of Control (POC) = `706.94` (Distance: `+1.14%`)
  * Value Area Low (VAL) = `698.03` (Distance: `+2.43%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`754.57` | POC=`744.11` | VAL=`738.60`
  * Prior Day Extremes: PDH=`759.80` | PDL=`677.20` | PDC=`696.20`
  * Monday Range Blueprint: High=`746.00` | Mid=`738.45` | Low=`730.90`
  * Developing Weekly Value Area: Weekly VAH=`751.69` | Weekly POC=`740.53` | Weekly VAL=`734.95`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`724.00` | Low=`677.90`
  * London Session (08:00-16:00 UTC): High=`718.36` | Low=`712.64`
  * New York Session (13:00-21:00 UTC): High=`719.79` | Low=`711.21`
  * Initial Balance (First Hour): IB High=`717.65` | IB Low=`713.35`
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
| `5m` | `717.23` | `717.54` | `716.20` | `717.24` | `4,032` | 2,891,438.15 USD | 102,418.49 USD | `+3.54%` | -36,239,130.50 USD | `+0.26` | **`BULLISH`** | `NEUTRAL CHOP` |
| `5m` | `717.23` | `719.84` | `716.84` | `719.04` | `8,368` | 6,007,216.10 USD | 790,434.60 USD | `+13.16%` | -35,448,695.89 USD | `+0.77` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `719.04` | `719.13` | `719.04` | `719.13` | `12` | 8,758.04 USD | 8,714.90 USD | `+99.51%` | -35,439,980.99 USD | `+0.18` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `708.49` | `710.53` | `708.09` | `710.12` | `10,879` | 7,713,838.94 USD | -128,948.88 USD | `-1.67%` | -39,541,868.78 USD | `+0.36` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `710.11` | `717.54` | `709.32` | `717.24` | `25,176` | 18,001,107.25 USD | 3,180,478.62 USD | `+17.67%` | -36,361,390.16 USD | `+1.54` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `717.23` | `719.84` | `716.84` | `719.31` | `8,436` | 6,055,965.51 USD | 815,763.29 USD | `+13.47%` | -35,545,626.87 USD | `+0.71` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `696.33` | `704.02` | `691.00` | `702.98` | `140,981` | 98,470,359.76 USD | -8,456,832.77 USD | `-8.59%` | -29,398,036.53 USD | `-0.74` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `702.99` | `715.85` | `701.01` | `710.56` | `127,490` | 90,521,702.76 USD | -9,774,555.27 USD | `-10.80%` | -39,172,591.80 USD | `-0.84` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `710.57` | `719.84` | `708.09` | `719.30` | `63,528` | 45,310,562.42 USD | 3,623,454.93 USD | `+8.00%` | -35,549,136.88 USD | `+0.52` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `750.62` | `754.90` | `743.07` | `745.33` | `88,414` | 66,199,547.89 USD | 232,195.88 USD | `+0.35%` | -10,302,756.17 USD | `+0.38` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `745.34` | `745.53` | `677.76` | `697.96` | `1,556,116` | 1,101,338,590.19 USD | -7,502,511.31 USD | `-0.68%` | -17,805,267.48 USD | `-0.58` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `697.96` | `719.84` | `681.03` | `719.31` | `513,142` | 359,433,770.73 USD | -17,740,359.40 USD | `-4.94%` | -35,545,626.87 USD | `-1.45` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `748.51` | `753.57` | `738.70` | `740.45` | `333,019` | 248,636,999.78 USD | -10,340,292.49 USD | `-4.16%` | -18,580,450.49 USD | `-1.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `740.45` | `753.64` | `739.55` | `750.62` | `148,938` | 111,099,080.67 USD | 8,045,498.44 USD | `+7.24%` | -10,534,952.05 USD | `+1.41` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `750.62` | `754.90` | `743.07` | `745.33` | `88,414` | 66,199,547.89 USD | 232,195.88 USD | `+0.35%` | -10,302,756.17 USD | `+0.38` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `745.34` | `745.53` | `677.76` | `697.96` | `1,556,116` | 1,101,338,590.19 USD | -7,502,511.31 USD | `-0.68%` | -17,805,267.48 USD | `-0.58` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `697.96` | `719.84` | `681.03` | `719.31` | `513,142` | 359,433,770.73 USD | -17,740,359.40 USD | `-4.94%` | -35,545,626.87 USD | `-1.45` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| `BID` | `715.66` | `363000000.0000` | 259.78 USD | 37,262.67 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `715.67` | `13953000000.0000` | 9,985.74 USD | 37,002.89 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `715.68` | `273000000.0000` | 195.38 USD | 27,017.15 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `715.69` | `15000000.0000` | 10.74 USD | 26,821.76 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `715.71` | `461000000.0000` | 329.94 USD | 26,811.03 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `715.72` | `380000000.0000` | 271.97 USD | 26,481.09 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `715.73` | `187000000.0000` | 133.84 USD | 26,209.11 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `715.76` | `381000000.0000` | 272.70 USD | 26,075.27 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `715.78` | `2296000000.0000` | 1,643.43 USD | 25,802.57 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `715.80` | `1397000000.0000` | 999.97 USD | 24,159.14 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `715.81` | `4968000000.0000` | 3,556.14 USD | 23,159.16 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `715.82` | `5299000000.0000` | 3,793.13 USD | 19,603.02 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `715.83` | `1000000000.0000` | 715.83 USD | 15,809.89 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `715.84` | `14207000000.0000` | 10,169.94 USD | 15,094.06 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `715.85` | `272000000.0000` | 194.71 USD | 4,924.12 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `715.88` | `363000000.0000` | 259.86 USD | 4,729.41 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `715.90` | `2661000000.0000` | 1,905.01 USD | 4,469.54 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `715.92` | `579000000.0000` | 414.52 USD | 2,564.53 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `715.94` | `1766000000.0000` | 1,264.35 USD | 2,150.02 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `715.98` | `1237000000.0000` | 885.67 USD | 885.67 USD | `2 orders` | `-0.00%` | `-` |
| `ASK` | `715.99` | `17534000000.0000` | 12,554.17 USD | 12,554.17 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `715.99` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 715.99` | `0.00%` | `-` |
| `ASK` | `716.03` | `285000000.0000` | 204.07 USD | 12,758.24 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `716.07` | `665000000.0000` | 476.19 USD | 13,234.42 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `716.11` | `380000000.0000` | 272.12 USD | 13,506.55 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `716.13` | `380000000.0000` | 272.13 USD | 13,778.67 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `716.14` | `1052000000.0000` | 753.38 USD | 14,532.05 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `716.16` | `381000000.0000` | 272.86 USD | 14,804.91 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `716.20` | `363000000.0000` | 259.98 USD | 15,064.89 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `716.21` | `1399000000.0000` | 1,001.98 USD | 16,066.87 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `716.22` | `363000000.0000` | 259.99 USD | 16,326.86 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `716.27` | `380000000.0000` | 272.18 USD | 16,599.04 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `716.28` | `381000000.0000` | 272.90 USD | 16,871.94 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `716.32` | `381000000.0000` | 272.92 USD | 17,144.86 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `716.36` | `1381000000.0000` | 989.29 USD | 18,134.15 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `716.37` | `2797000000.0000` | 2,003.69 USD | 20,137.84 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `716.40` | `2174000000.0000` | 1,557.45 USD | 21,695.29 USD | `2 orders` | `+0.06%` | `-` |
| `ASK` | `716.41` | `299000000.0000` | 214.21 USD | 21,909.50 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `716.45` | `362000000.0000` | 259.35 USD | 22,168.86 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `716.46` | `1478000000.0000` | 1,058.93 USD | 23,227.78 USD | `2 orders` | `+0.07%` | `-` |
| `ASK` | `716.47` | `560000000.0000` | 401.22 USD | 23,629.01 USD | `4 orders` | `+0.07%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 09:33:32 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `776` | `0xea00...a918` | `LONG` | 2,940,876.91 USD | `4,098,429,000,000.00` | `787.24` | `717.88` | `0.000000` | -285,549.87 USD | `-9.71%` | `5X Cross` |
| `902` | `0xfe7c...b7ae` | `LONG` | 2,506,881.02 USD | `3,491,575,000,000.00` | `686.05` | `717.88` | `0.000000` | 111,470.16 USD | `+4.45%` | `10X Cross` |
| `932` | `0x7d0c...1b28` | `LONG` | 2,420,774.70 USD | `3,372,304,000,000.00` | `703.55` | `717.88` | `0.000000` | 48,178.18 USD | `+1.99%` | `10X Cross` |
| `1084` | `0x27c9...d65d` | `LONG` | 2,020,629.06 USD | `2,814,325,000,000.00` | `700.84` | `717.88` | `203.03` | 48,228.86 USD | `+2.39%` | `10X Cross` |
| `1172` | `0x7737...bf66` | `SHORT` | 1,896,622.34 USD | `2,646,179,000,000.00` | `752.73` | `717.88` | `6771.45` | 95,248.25 USD | `+5.02%` | `10X Cross` |
| `1343` | `0x51f6...2b39` | `LONG` | 1,609,369.12 USD | `2,241,992,000,000.00` | `703.00` | `717.88` | `117.28` | 33,258.93 USD | `+2.07%` | `10X Cross` |
| `1465` | `0xc675...795d` | `LONG` | 1,473,752.86 USD | `2,055,214,000,000.00` | `706.91` | `717.88` | `640.94` | 20,908.19 USD | `+1.42%` | `10X Cross` |
| `1490` | `0x2edd...8179` | `LONG` | 1,449,804.54 USD | `2,019,367,000,000.00` | `714.56` | `717.88` | `0.000000` | 6,843.15 USD | `+0.47%` | `10X Cross` |
| `1540` | `0x325e...9564` | `LONG` | 1,398,736.04 USD | `1,948,236,000,000.00` | `707.43` | `717.88` | `0.000000` | 20,489.22 USD | `+1.46%` | `10X Cross` |
| `1682` | `0x07fd...689d` | `LONG` | 1,252,183.62 USD | `1,744,292,000,000.00` | `714.40` | `717.88` | `0.000000` | 6,051.59 USD | `+0.48%` | `10X Cross` |
| `1701` | `0x645b...87b8` | `LONG` | 1,236,438.76 USD | `1,721,990,000,000.00` | `747.34` | `717.88` | `0.000000` | -50,468.66 USD | `-4.08%` | `10X Cross` |
| `1733` | `0x4420...4c4b` | `LONG` | 1,201,046.28 USD | `1,672,813,000,000.00` | `704.02` | `717.88` | `257.49` | 23,353.03 USD | `+1.94%` | `10X Cross` |
| `1795` | `0xa4a6...46cf` | `SHORT` | 1,150,230.53 USD | `1,602,037,000,000.00` | `711.76` | `717.88` | `1753.98` | -9,960.96 USD | `-0.87%` | `10X Cross` |
| `1822` | `0xfc27...9d9d` | `LONG` | 1,133,079.42 USD | `1,578,149,000,000.00` | `700.69` | `717.88` | `0.000000` | 27,286.30 USD | `+2.41%` | `10X Cross` |
| `1888` | `0x14c6...b280` | `SHORT` | 1,076,985.00 USD | `1,500,000,000,000.00` | `712.51` | `717.88` | `1464.75` | -8,223.30 USD | `-0.76%` | `10X Cross` |
| `1946` | `0xbf5a...88ba` | `SHORT` | 1,033,319.12 USD | `1,439,105,000,000.00` | `718.16` | `717.88` | `1961.80` | 187.82 USD | `+0.02%` | `10X Cross` |
| `1985` | `0xecb6...2b00` | `SHORT` | 1,015,035.93 USD | `1,413,640,000,000.00` | `713.16` | `717.88` | `19074.63` | -6,887.15 USD | `-0.68%` | `5X Cross` |
| `1987` | `0x646b...01dc` | `SHORT` | 1,014,241.42 USD | `1,412,868,000,000.00` | `699.26` | `717.88` | `1291.64` | -26,272.42 USD | `-2.59%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`758.29` (Vol: 2,900,000.00 USD, Dist: `+5.69%`) | Long MP=`677.19` (Vol: 3,100,000.00 USD, Dist: `--5.62%`)
  * 48H Horizon: Short MP=`767.93` (Vol: 3,000,000.00 USD, Dist: `+7.03%`) | Long MP=`677.29` (Vol: 3,100,000.00 USD, Dist: `--5.60%`)
  * 3D Horizon: Short MP=`767.93` (Vol: 3,400,000.00 USD, Dist: `+7.03%`) | Long MP=`677.29` (Vol: 3,100,000.00 USD, Dist: `--5.60%`)
  * 7D Horizon: Short MP=`767.93` (Vol: 3,500,000.00 USD, Dist: `+7.03%`) | Long MP=`677.29` (Vol: 3,100,000.00 USD, Dist: `--5.60%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `143.50` | 2,870.00 USD | 6,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `149.50` | 5,100.00 USD | 6,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `153.50` | 294.11 USD | 6,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `158.50` | 2,220.00 USD | 6,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `163.50` | 468,590.00 USD | 6,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `168.50` | 101,100.00 USD | 5,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `178.50` | 1,320.00 USD | 5,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `183.50` | 6,220.00 USD | 5,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `190.50` | 759.71 USD | 5,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `200.50` | 608.52 USD | 5,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `207.50` | 102.09 USD | 5,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `208.50` | 20,850.00 USD | 5,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `213.50` | 108.24 USD | 5,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `214.50` | 388.03 USD | 5,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `219.50` | 191.18 USD | 5,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `228.50` | 17,450.00 USD | 5,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `244.50` | 1,290.00 USD | 5,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `258.50` | 7,010.00 USD | 5,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `259.50` | 738.80 USD | 5,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `267.50` | 462,860.00 USD | 5,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `269.50` | 21,360.00 USD | 5,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `283.50` | 283,500.00 USD | 5,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `292.50` | 9,350.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `298.50` | 148,320.00 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `300.50` | 457.06 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `312.50` | 500.00 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `326.50` | 500.85 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `327.50` | 314.07 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `328.50` | 133.70 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `332.50` | 150.29 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `333.50` | 226.45 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `337.50` | 135,000.00 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `339.50` | 417.25 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `342.50` | 650.75 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `347.50` | 9,580.00 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `349.50` | 6,840.00 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `350.50` | 14,990.00 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `351.50` | 124.08 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `352.50` | 24,480.00 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `354.50` | 11,800.00 USD | 4,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `355.50` | 529.34 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `356.50` | 3,570.00 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `359.50` | 212.10 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `363.50` | 340.60 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `366.50` | 549.75 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `367.50` | 146.63 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `368.50` | 15,810.00 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `369.50` | 1,660.00 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `371.50` | 146.37 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `372.50` | 11,560.00 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `374.50` | 1,820.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `377.50` | 1,400.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `378.50` | 643.45 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `381.50` | 1,910.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `382.50` | 12,070.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `383.50` | 7,290.00 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `384.50` | 1,060.00 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `385.50` | 19,150.00 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `386.50` | 531.44 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `387.50` | 392.54 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `393.50` | 536.73 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `394.50` | 168.06 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `395.50` | 2,110.00 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `396.50` | 317.20 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `398.50` | 626.84 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `399.50` | 603.64 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `404.50` | 102.34 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `409.50` | 613.02 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `410.50` | 105.91 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `412.50` | 1,750.00 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `413.50` | 14,890.00 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `414.50` | 1,890.00 USD | 4,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `415.50` | 1,810.00 USD | 4,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `417.50` | 7,140.00 USD | 4,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `418.50` | 318.06 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `419.50` | 2,650.00 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `421.50` | 2,320.00 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `422.50` | 62,760.00 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `428.50` | 30,660.00 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `429.50` | 846.12 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `431.50` | 612.73 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `436.50` | 133.13 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `437.50` | 2,380.00 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `438.50` | 1,790.00 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `442.50` | 33,410.00 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `444.50` | 4,510.00 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `448.50` | 3,350.00 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `452.50` | 957.04 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `456.50` | 4,730.00 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `459.50` | 38,210.00 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `463.50` | 199.31 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `464.50` | 396.68 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `469.50` | 4,370.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `470.50` | 674.23 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `475.50` | 5,320.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `477.50` | 1,560.00 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `481.50` | 615.36 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `482.50` | 6,840.00 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `483.50` | 8,500.00 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `484.50` | 2,840.00 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `485.50` | 2,400.00 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `487.50` | 464.59 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `488.50` | 2,300.00 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `491.50` | 1,080.00 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `493.50` | 3,940.00 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `498.50` | 1,820.00 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `499.50` | 13,310.00 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `501.50` | 7,760.00 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `502.50` | 109.04 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `504.50` | 288.07 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `505.50` | 5,760.00 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `508.50` | 992.08 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `509.50` | 44,080.00 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `510.50` | 4,080.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `511.50` | 5,180.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `513.50` | 2,520.00 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `514.50` | 701.78 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `515.50` | 81,170.00 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `516.50` | 481.89 USD | 3,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `517.50` | 22,650.00 USD | 3,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `519.50` | 968.35 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `520.50` | 272.22 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `521.50` | 838.05 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `522.50` | 2,090.00 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `524.50` | 833.43 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `526.50` | 1,700.00 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `529.50` | 42,820.00 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `530.50` | 18,050.00 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `531.50` | 484.73 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `532.50` | 422.81 USD | 3,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `534.50` | 555.35 USD | 3,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `535.50` | 100.14 USD | 3,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `536.50` | 183,580.00 USD | 3,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `537.50` | 769.70 USD | 3,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `539.50` | 490.94 USD | 3,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `540.50` | 2,130.00 USD | 3,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `541.50` | 65,690.00 USD | 3,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `543.50` | 2,680.00 USD | 3,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `544.50` | 210,830.00 USD | 3,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `545.50` | 1,580.00 USD | 3,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `546.50` | 874.40 USD | 3,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `548.50` | 1,980.00 USD | 3,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `549.50` | 1,370.00 USD | 3,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `550.50` | 633.63 USD | 3,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `551.50` | 1,250.00 USD | 3,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `552.50` | 24,120.00 USD | 3,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `553.50` | 3,080.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `556.50` | 5,670.00 USD | 3,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `557.50` | 10,020.00 USD | 3,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `558.50` | 212.23 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `560.50` | 582.36 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `562.50` | 67,470.00 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `564.50` | 33,490.00 USD | 3,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `568.50` | 454.80 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `569.50` | 144.08 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `571.50` | 712,450.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `572.50` | 8,800.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `574.50` | 767.53 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `575.50` | 1,540.00 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `576.50` | 4,810.00 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `577.50` | 225,800.00 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `578.50` | 7,640.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `580.50` | 35,850.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `581.50` | 580.34 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `582.50` | 1,540.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `583.50` | 3,470.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `584.50` | 292.25 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `585.50` | 210.19 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `586.50` | 2,360.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `587.50` | 179,500.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `588.50` | 397.24 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `589.50` | 14,950.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `590.50` | 2,560.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `591.50` | 619.30 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `592.50` | 840.76 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `593.50` | 36,050.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `594.50` | 9,370.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `595.50` | 3,000.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `596.50` | 100.81 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `597.50` | 2,390.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `598.50` | 892.96 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `600.50` | 945.19 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `601.50` | 16,880.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `602.50` | 418.13 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `603.50` | 1,610.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `606.50` | 60,390.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `609.50` | 213.32 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `611.50` | 1,580.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `612.50` | 15,850.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `613.50` | 120.25 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `614.50` | 8,590.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `616.50` | 1,540.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `617.50` | 156.23 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `618.50` | 932.70 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `619.50` | 1,410.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `620.50` | 24,930.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `621.50` | 696.70 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `622.50` | 137.57 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `624.50` | 3,460.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `625.50` | 25,330.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `626.50` | 964.81 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `630.50` | 153.21 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `631.10` | 39,810,000.00 USD | 39,810,000.00 USD | 0.00 USD | 93,570.00 USD | 875,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `631.50` | 2,900.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `632.00` | 38,840,000.00 USD | 38,840,000.00 USD | 88,900.00 USD | 42,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `632.50` | 3,560.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `632.90` | 38,710,000.00 USD | 38,710,000.00 USD | 514,860.00 USD | 11,420.00 USD | 40,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `633.80` | 38,140,000.00 USD | 38,140,000.00 USD | 16,720.00 USD | 0.00 USD | 73,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `634.50` | 6,660.00 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `634.70` | 38,050,000.00 USD | 38,050,000.00 USD | 11,290.00 USD | 39,990.00 USD | 37,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `635.50` | 155.06 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `635.60` | 37,960,000.00 USD | 37,960,000.00 USD | 0.00 USD | 0.00 USD | 38,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `636.50` | 37,920,000.00 USD | 37,920,000.00 USD | 101,910.00 USD | 40,910.00 USD | 236,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `636.50` | 1,110.00 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `637.50` | 305.36 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `638.30` | 37,540,000.00 USD | 37,540,000.00 USD | 0.00 USD | 37,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `638.50` | 328.83 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `639.20` | 37,510,000.00 USD | 37,510,000.00 USD | 184,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `639.50` | 455.96 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `640.10` | 37,320,000.00 USD | 37,320,000.00 USD | 0.00 USD | 0.00 USD | 184,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `640.50` | 1,320,000.00 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `641.90` | 37,140,000.00 USD | 37,140,000.00 USD | 150,090.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `642.50` | 8,480.00 USD | 366,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `644.50` | 9,660.00 USD | 358,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `644.60` | 36,990,000.00 USD | 36,990,000.00 USD | 308,550.00 USD | 0.00 USD | 341,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `646.40` | 36,340,000.00 USD | 36,340,000.00 USD | 87,020.00 USD | 0.00 USD | 140,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `646.50` | 804.25 USD | 348,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `647.30` | 36,110,000.00 USD | 36,110,000.00 USD | 227,570.00 USD | 29,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `647.50` | 156.05 USD | 347,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `648.20` | 35,850,000.00 USD | 35,850,000.00 USD | 101,870.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `648.50` | 1,940.00 USD | 347,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `649.50` | 6,640.00 USD | 345,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `650.50` | 1,760.00 USD | 339,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `651.50` | 9,650.00 USD | 337,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `651.80` | 35,750,000.00 USD | 35,750,000.00 USD | 106,810.00 USD | 0.00 USD | 94,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `652.50` | 652.50 USD | 327,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `653.50` | 97,380.00 USD | 326,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `653.60` | 35,550,000.00 USD | 35,550,000.00 USD | 0.00 USD | 26,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `654.50` | 35,520,000.00 USD | 35,520,000.00 USD | 108,090.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `654.50` | 100.14 USD | 229,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `655.40` | 35,410,000.00 USD | 35,410,000.00 USD | 192,610.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `655.50` | 437.87 USD | 229,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `656.30` | 35,220,000.00 USD | 35,220,000.00 USD | 35,490.00 USD | 0.00 USD | 825,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `657.20` | 34,360,000.00 USD | 34,360,000.00 USD | 76,470.00 USD | 21,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `658.10` | 34,260,000.00 USD | 34,260,000.00 USD | 853,340.00 USD | 14,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `658.50` | 15,090.00 USD | 229,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `659.00` | 33,390,000.00 USD | 33,390,000.00 USD | 81,060.00 USD | 0.00 USD | 81,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `659.50` | 46,450.00 USD | 213,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `659.90` | 33,230,000.00 USD | 33,230,000.00 USD | 0.00 USD | 7,460.00 USD | 14,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `660.50` | 3,410.00 USD | 167,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `660.80` | 33,210,000.00 USD | 33,210,000.00 USD | 90,670.00 USD | 83,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `661.50` | 20,140.00 USD | 164,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `661.70` | 33,040,000.00 USD | 33,040,000.00 USD | 445,210.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `662.50` | 2,850.00 USD | 143,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `662.60` | 32,590,000.00 USD | 32,590,000.00 USD | 57,440.00 USD | 87,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `663.50` | 32,440,000.00 USD | 32,440,000.00 USD | 145,120.00 USD | 5,000.00 USD | 19,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `663.50` | 9,230.00 USD | 141,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `664.10` | 87,050,000.00 USD | 87,050,000.00 USD | 78,740.00 USD | 18,740.00 USD | 39,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `664.40` | 32,280,000.00 USD | 32,280,000.00 USD | 1,200,000.00 USD | 48,410.00 USD | 21,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `664.50` | 24,600.00 USD | 131,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `665.00` | 86,910,000.00 USD | 86,910,000.00 USD | 92,030.00 USD | 22,990.00 USD | 37,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `665.30` | 31,010,000.00 USD | 31,010,000.00 USD | 70,400.00 USD | 4,540.00 USD | 11,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `665.50` | 11,290.00 USD | 107,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `665.90` | 86,760,000.00 USD | 86,760,000.00 USD | 264,020.00 USD | 71,380.00 USD | 63,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `666.20` | 30,920,000.00 USD | 30,920,000.00 USD | 720,400.00 USD | 88,780.00 USD | 692,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `666.50` | 2,270.00 USD | 95,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `666.80` | 86,360,000.00 USD | 86,360,000.00 USD | 198,550.00 USD | 33,320.00 USD | 61,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `667.10` | 29,420,000.00 USD | 29,420,000.00 USD | 709,250.00 USD | 16,560.00 USD | 13,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `667.50` | 1,380.00 USD | 93,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `667.70` | 86,070,000.00 USD | 86,070,000.00 USD | 199,690.00 USD | 45,130.00 USD | 51,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `668.00` | 28,680,000.00 USD | 28,680,000.00 USD | 265,780.00 USD | 120,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `668.50` | 1,880.00 USD | 92,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `668.60` | 85,770,000.00 USD | 85,770,000.00 USD | 387,530.00 USD | 92,860.00 USD | 51,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `668.90` | 28,300,000.00 USD | 28,300,000.00 USD | 603,810.00 USD | 17,190.00 USD | 3,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `669.50` | 85,240,000.00 USD | 85,240,000.00 USD | 341,150.00 USD | 38,130.00 USD | 108,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `669.50` | 2,930.00 USD | 90,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `669.80` | 27,670,000.00 USD | 27,670,000.00 USD | 237,120.00 USD | 61,020.00 USD | 1,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `670.40` | 84,750,000.00 USD | 84,750,000.00 USD | 319,660.00 USD | 93,800.00 USD | 77,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `670.50` | 6,110.00 USD | 87,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `670.70` | 25,890,000.00 USD | 25,890,000.00 USD | 193,670.00 USD | 4,460.00 USD | 7,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `671.30` | 84,260,000.00 USD | 84,260,000.00 USD | 335,750.00 USD | 57,500.00 USD | 42,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `671.50` | 641.28 USD | 81,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `671.60` | 25,680,000.00 USD | 25,680,000.00 USD | 1,850,000.00 USD | 13,640.00 USD | 11,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `672.20` | 83,830,000.00 USD | 83,830,000.00 USD | 180,230.00 USD | 62,620.00 USD | 74,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `672.50` | 23,800,000.00 USD | 23,800,000.00 USD | 214,460.00 USD | 15,830.00 USD | 670,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `672.50` | 8,680.00 USD | 80,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `673.10` | 83,510,000.00 USD | 83,510,000.00 USD | 394,120.00 USD | 64,970.00 USD | 42,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `673.40` | 22,900,000.00 USD | 22,900,000.00 USD | 345,840.00 USD | 296,640.00 USD | 1,650,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `673.50` | 31,510.00 USD | 72,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `674.00` | 83,010,000.00 USD | 83,010,000.00 USD | 335,670.00 USD | 105,910.00 USD | 80,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `674.30` | 20,600,000.00 USD | 20,600,000.00 USD | 359,530.00 USD | 351,220.00 USD | 178,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `674.50` | 4,470.00 USD | 40,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `674.90` | 82,490,000.00 USD | 82,490,000.00 USD | 247,070.00 USD | 31,490.00 USD | 44,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `675.20` | 19,720,000.00 USD | 19,720,000.00 USD | 2,080,000.00 USD | 63,140.00 USD | 397,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `675.50` | 9,230.00 USD | 36,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `675.80` | 82,160,000.00 USD | 82,160,000.00 USD | 387,400.00 USD | 26,020.00 USD | 79,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `676.10` | 17,180,000.00 USD | 17,180,000.00 USD | 207,530.00 USD | 284,040.00 USD | 422,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `676.50` | 1,910.00 USD | 26,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `676.70` | 81,670,000.00 USD | 81,670,000.00 USD | 509,100.00 USD | 35,490.00 USD | 126,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `677.00` | 16,260,000.00 USD | 16,260,000.00 USD | 417,680.00 USD | 82,460.00 USD | 185,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `677.50` | 10,400.00 USD | 25,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `677.60` | 81,000,000.00 USD | 81,000,000.00 USD | 409,810.00 USD | 0.00 USD | 63,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `677.90` | 15,580,000.00 USD | 15,580,000.00 USD | 215,410.00 USD | 109,020.00 USD | 97,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `678.50` | 80,530,000.00 USD | 80,530,000.00 USD | 120,190.00 USD | 0.00 USD | 26,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `678.80` | 15,150,000.00 USD | 15,150,000.00 USD | 1,030,000.00 USD | 111,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `679.40` | 80,380,000.00 USD | 80,380,000.00 USD | 116,510.00 USD | 10,480.00 USD | 40,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `679.50` | 3,100.00 USD | 14,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `679.70` | 14,020,000.00 USD | 14,020,000.00 USD | 1,200,000.00 USD | 164,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `680.30` | 80,210,000.00 USD | 80,210,000.00 USD | 166,780.00 USD | 13,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `680.50` | 11,490.00 USD | 11,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `680.60` | 12,650,000.00 USD | 12,650,000.00 USD | 2,190.00 USD | 98,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `681.20` | 80,030,000.00 USD | 80,030,000.00 USD | 106,280.00 USD | 7,050.00 USD | 35,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `681.50` | 12,550,000.00 USD | 12,550,000.00 USD | 11,460.00 USD | 293,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `682.10` | 79,880,000.00 USD | 79,880,000.00 USD | 0.00 USD | 23,360.00 USD | 27,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `682.40` | 12,250,000.00 USD | 12,250,000.00 USD | 35,000.00 USD | 10,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `683.00` | 79,830,000.00 USD | 79,830,000.00 USD | 175,930.00 USD | 28,470.00 USD | 11,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `683.30` | 12,200,000.00 USD | 12,200,000.00 USD | 118,750.00 USD | 125,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `683.90` | 79,620,000.00 USD | 79,620,000.00 USD | 77,000.00 USD | 29,510.00 USD | 17,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `684.20` | 11,960,000.00 USD | 11,960,000.00 USD | 19,390.00 USD | 38,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `684.80` | 79,490,000.00 USD | 79,490,000.00 USD | 246,080.00 USD | 9,850.00 USD | 39,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `685.70` | 79,200,000.00 USD | 79,200,000.00 USD | 197,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `686.00` | 11,900,000.00 USD | 11,900,000.00 USD | 694,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `686.60` | 79,000,000.00 USD | 79,000,000.00 USD | 62,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `686.90` | 11,210,000.00 USD | 11,210,000.00 USD | 0.00 USD | 266,430.00 USD | 316,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `687.50` | 78,940,000.00 USD | 78,940,000.00 USD | 148,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `687.80` | 10,620,000.00 USD | 10,620,000.00 USD | 775,320.00 USD | 295,490.00 USD | 3,930,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `688.40` | 78,790,000.00 USD | 78,790,000.00 USD | 67,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `688.70` | 5,620,000.00 USD | 5,620,000.00 USD | 2,210,000.00 USD | 91,030.00 USD | 340,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `689.30` | 78,720,000.00 USD | 78,720,000.00 USD | 84,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `689.60` | 2,980,000.00 USD | 2,980,000.00 USD | 306,820.00 USD | 38,440.00 USD | 694,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `690.20` | 78,640,000.00 USD | 78,640,000.00 USD | 283,920.00 USD | 63,230.00 USD | 82,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `690.50` | 1,940,000.00 USD | 1,940,000.00 USD | 367,190.00 USD | 146,030.00 USD | 625,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `691.10` | 78,210,000.00 USD | 78,210,000.00 USD | 362,020.00 USD | 61,370.00 USD | 81,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `691.40` | 800,560.00 USD | 800,560.00 USD | 33,240.00 USD | 129,500.00 USD | 306,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `692.00` | 77,700,000.00 USD | 77,700,000.00 USD | 322,430.00 USD | 18,850.00 USD | 58,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `692.30` | 331,790.00 USD | 331,790.00 USD | 0.00 USD | 0.00 USD | 194,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `692.90` | 77,300,000.00 USD | 77,300,000.00 USD | 280,830.00 USD | 19,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `693.80` | 77,000,000.00 USD | 77,000,000.00 USD | 305,720.00 USD | 39,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `694.70` | 76,660,000.00 USD | 76,660,000.00 USD | 279,840.00 USD | 36,640.00 USD | 35,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `695.60` | 76,300,000.00 USD | 76,300,000.00 USD | 120,440.00 USD | 0.00 USD | 21,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `695.90` | 137,440.00 USD | 137,440.00 USD | 0.00 USD | 137,440.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `696.50` | 76,160,000.00 USD | 76,160,000.00 USD | 140,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `697.40` | 76,020,000.00 USD | 76,020,000.00 USD | 189,100.00 USD | 19,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `698.30` | 75,810,000.00 USD | 75,810,000.00 USD | 273,520.00 USD | 33,120.00 USD | 54,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `699.20` | 75,450,000.00 USD | 75,450,000.00 USD | 274,810.00 USD | 12,670.00 USD | 11,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `700.10` | 75,150,000.00 USD | 75,150,000.00 USD | 225,450.00 USD | 40,820.00 USD | 27,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `701.00` | 74,860,000.00 USD | 74,860,000.00 USD | 237,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `701.90` | 74,620,000.00 USD | 74,620,000.00 USD | 135,260.00 USD | 41,260.00 USD | 89,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `702.80` | 74,360,000.00 USD | 74,360,000.00 USD | 416,820.00 USD | 57,470.00 USD | 36,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `703.70` | 73,840,000.00 USD | 73,840,000.00 USD | 311,800.00 USD | 44,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `704.60` | 73,490,000.00 USD | 73,490,000.00 USD | 537,050.00 USD | 136,550.00 USD | 194,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `705.50` | 72,620,000.00 USD | 72,620,000.00 USD | 920,340.00 USD | 162,820.00 USD | 236,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `706.40` | 71,300,000.00 USD | 71,300,000.00 USD | 523,540.00 USD | 104,380.00 USD | 231,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `707.30` | 70,440,000.00 USD | 70,440,000.00 USD | 604,060.00 USD | 90,200.00 USD | 53,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `708.20` | 69,690,000.00 USD | 69,690,000.00 USD | 796,640.00 USD | 138,200.00 USD | 42,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `709.10` | 68,710,000.00 USD | 68,710,000.00 USD | 392,150.00 USD | 156,040.00 USD | 195,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `710.00` | 67,970,000.00 USD | 67,970,000.00 USD | 450,480.00 USD | 167,090.00 USD | 176,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `710.90` | 67,180,000.00 USD | 67,180,000.00 USD | 922,450.00 USD | 160,040.00 USD | 236,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `711.80` | 65,860,000.00 USD | 65,860,000.00 USD | 608,910.00 USD | 232,130.00 USD | 114,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `712.70` | 64,900,000.00 USD | 64,900,000.00 USD | 1,190,000.00 USD | 217,390.00 USD | 236,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `713.60` | 63,260,000.00 USD | 63,260,000.00 USD | 2,250,000.00 USD | 279,180.00 USD | 308,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `714.50` | 60,410,000.00 USD | 60,410,000.00 USD | 508,400.00 USD | 209,320.00 USD | 292,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `714.80` | 463,510.00 USD | 463,510.00 USD | 0.00 USD | 146,930.00 USD | 316,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `715.40` | 59,400,000.00 USD | 59,400,000.00 USD | 1,050,000.00 USD | 419,310.00 USD | 329,730.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `715.50` | 349.16 USD | 349.16 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `715.70` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 498,160.00 USD | 1,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `716.30` | 57,600,000.00 USD | 57,600,000.00 USD | 1,080,000.00 USD | 324,540.00 USD | 233,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `716.50` | 49,180.00 USD | 49,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `716.60` | 2,980,000.00 USD | 2,980,000.00 USD | 303,890.00 USD | 305,750.00 USD | 340,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `717.20` | 55,960,000.00 USD | 55,960,000.00 USD | 581,610.00 USD | 398,030.00 USD | 387,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `717.50` | 3,950,000.00 USD | 3,950,000.00 USD | 268,080.00 USD | 126,170.00 USD | 579,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `718.10` | 54,590,000.00 USD | 54,590,000.00 USD | 1,690,000.00 USD | 246,320.00 USD | 151,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `718.40` | 4,980,000.00 USD | 4,980,000.00 USD | 145,050.00 USD | 146,030.00 USD | 739,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `719.00` | 52,510,000.00 USD | 52,510,000.00 USD | 670,390.00 USD | 137,460.00 USD | 211,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `719.30` | 5,590,000.00 USD | 5,590,000.00 USD | 126,360.00 USD | 177,910.00 USD | 306,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `719.90` | 51,490,000.00 USD | 51,490,000.00 USD | 618,020.00 USD | 173,240.00 USD | 186,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `720.20` | 5,790,000.00 USD | 5,790,000.00 USD | 0.00 USD | 0.00 USD | 194,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `720.50` | 161.39 USD | 49,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `720.80` | 50,510,000.00 USD | 50,510,000.00 USD | 1,010,000.00 USD | 52,490.00 USD | 180,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `721.10` | 5,990,000.00 USD | 5,990,000.00 USD | 0.00 USD | 204,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `721.50` | 33,710.00 USD | 83,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `721.70` | 49,260,000.00 USD | 49,260,000.00 USD | 1,950,000.00 USD | 237,690.00 USD | 653,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `722.00` | 6,070,000.00 USD | 6,070,000.00 USD | 0.00 USD | 78,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `722.50` | 18,310.00 USD | 101,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `722.60` | 46,430,000.00 USD | 46,430,000.00 USD | 1,930,000.00 USD | 108,200.00 USD | 229,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `723.50` | 44,160,000.00 USD | 44,160,000.00 USD | 640,550.00 USD | 140,550.00 USD | 293,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `723.50` | 11,430.00 USD | 113,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `723.80` | 6,510,000.00 USD | 6,510,000.00 USD | 0.00 USD | 437,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `724.40` | 43,080,000.00 USD | 43,080,000.00 USD | 663,550.00 USD | 186,780.00 USD | 130,770.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `724.50` | 525.26 USD | 113,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `725.30` | 42,100,000.00 USD | 42,100,000.00 USD | 1,760,000.00 USD | 418,390.00 USD | 396,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `725.50` | 1,920.00 USD | 115,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `725.60` | 6,560,000.00 USD | 6,560,000.00 USD | 0.00 USD | 57,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `726.20` | 39,520,000.00 USD | 39,520,000.00 USD | 1,060,000.00 USD | 311,550.00 USD | 460,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `726.50` | 6,630,000.00 USD | 6,630,000.00 USD | 0.00 USD | 64,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `726.50` | 6,860.00 USD | 122,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `727.10` | 37,690,000.00 USD | 37,690,000.00 USD | 1,230,000.00 USD | 331,980.00 USD | 241,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `727.50` | 1,030.00 USD | 123,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `728.00` | 35,890,000.00 USD | 35,890,000.00 USD | 3,110,000.00 USD | 778,750.00 USD | 388,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `728.50` | 42,630.00 USD | 166,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `728.90` | 31,610,000.00 USD | 31,610,000.00 USD | 2,330,000.00 USD | 317,590.00 USD | 644,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `729.20` | 7,500,000.00 USD | 7,500,000.00 USD | 0.00 USD | 256,940.00 USD | 616,880.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `729.50` | 172,780.00 USD | 338,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `729.80` | 28,320,000.00 USD | 28,320,000.00 USD | 1,320,000.00 USD | 430,010.00 USD | 339,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `730.10` | 9,290,000.00 USD | 9,290,000.00 USD | 1,690,000.00 USD | 24,020.00 USD | 73,220.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `730.50` | 59,010.00 USD | 397,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `730.70` | 26,230,000.00 USD | 26,230,000.00 USD | 2,760,000.00 USD | 351,520.00 USD | 587,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `731.00` | 12,410,000.00 USD | 12,410,000.00 USD | 1,090,000.00 USD | 152,870.00 USD | 1,880,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `731.50` | 46,090.00 USD | 443,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `731.60` | 22,530,000.00 USD | 22,530,000.00 USD | 1,530,000.00 USD | 133,980.00 USD | 261,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `731.90` | 12,840,000.00 USD | 12,840,000.00 USD | 0.00 USD | 82,570.00 USD | 347,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `732.50` | 20,610,000.00 USD | 20,610,000.00 USD | 465,880.00 USD | 221,510.00 USD | 96,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `732.50` | 133,110.00 USD | 577,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `732.80` | 15,130,000.00 USD | 15,130,000.00 USD | 1,130,000.00 USD | 134,420.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `733.40` | 19,820,000.00 USD | 19,820,000.00 USD | 1,910,000.00 USD | 158,310.00 USD | 338,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `733.50` | 28,570.00 USD | 605,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `733.70` | 15,830,000.00 USD | 15,830,000.00 USD | 344,230.00 USD | 210,140.00 USD | 153,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `734.30` | 17,420,000.00 USD | 17,420,000.00 USD | 1,580,000.00 USD | 288,470.00 USD | 244,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `734.50` | 204,530.00 USD | 810,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `734.60` | 16,430,000.00 USD | 16,430,000.00 USD | 460,890.00 USD | 42,070.00 USD | 97,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `735.20` | 15,310,000.00 USD | 15,310,000.00 USD | 1,330,000.00 USD | 172,940.00 USD | 437,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `735.50` | 18,070,000.00 USD | 18,070,000.00 USD | 813,660.00 USD | 227,070.00 USD | 590,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `735.50` | 23,790.00 USD | 833,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `736.10` | 13,370,000.00 USD | 13,370,000.00 USD | 2,130,000.00 USD | 181,990.00 USD | 484,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `736.40` | 18,800,000.00 USD | 18,800,000.00 USD | 736,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `736.50` | 12,170.00 USD | 846,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `737.00` | 10,570,000.00 USD | 10,570,000.00 USD | 2,360,000.00 USD | 175,330.00 USD | 633,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `737.30` | 18,920,000.00 USD | 18,920,000.00 USD | 117,570.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `737.50` | 4,060.00 USD | 850,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `737.90` | 7,400,000.00 USD | 7,400,000.00 USD | 3,420,000.00 USD | 72,280.00 USD | 374,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `738.20` | 19,290,000.00 USD | 19,290,000.00 USD | 210,200.00 USD | 162,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `738.50` | 1,050,000.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `738.80` | 3,530,000.00 USD | 3,530,000.00 USD | 522,950.00 USD | 20,210.00 USD | 155,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `739.10` | 20,950,000.00 USD | 20,950,000.00 USD | 726,150.00 USD | 0.00 USD | 934,700.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `739.50` | 8,400.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `739.70` | 2,830,000.00 USD | 2,830,000.00 USD | 352,500.00 USD | 0.00 USD | 203,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `740.00` | 21,670,000.00 USD | 21,670,000.00 USD | 697,550.00 USD | 0.00 USD | 15,020.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `740.50` | 810.11 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `740.60` | 2,280,000.00 USD | 2,280,000.00 USD | 1,090,000.00 USD | 0.00 USD | 33,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `740.90` | 22,380,000.00 USD | 22,380,000.00 USD | 546,620.00 USD | 166,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `741.50` | 1,160,000.00 USD | 1,160,000.00 USD | 257,630.00 USD | 0.00 USD | 208,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `741.50` | 8,440.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `741.80` | 22,690,000.00 USD | 22,690,000.00 USD | 313,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `742.40` | 689,850.00 USD | 689,850.00 USD | 0.00 USD | 0.00 USD | 183,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `742.50` | 14,070.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `743.30` | 505,930.00 USD | 505,930.00 USD | 0.00 USD | 0.00 USD | 57,580.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `743.50` | 102,990.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `743.60` | 23,250,000.00 USD | 23,250,000.00 USD | 120,950.00 USD | 0.00 USD | 436,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `744.20` | 448,350.00 USD | 448,350.00 USD | 0.00 USD | 257,580.00 USD | 141,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `744.50` | 24,130,000.00 USD | 24,130,000.00 USD | 771,380.00 USD | 106,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `744.50` | 118,750.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `745.10` | 48,980.00 USD | 48,980.00 USD | 0.00 USD | 48,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `745.40` | 25,460,000.00 USD | 25,460,000.00 USD | 473,600.00 USD | 0.00 USD | 854,020.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `745.50` | 78,410.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `746.00` | 999,320.00 USD | 999,320.00 USD | 999,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `746.30` | 26,000,000.00 USD | 26,000,000.00 USD | 435,700.00 USD | 106,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `746.50` | 185,150.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `746.90` | 1,210,000.00 USD | 1,210,000.00 USD | 215,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `747.20` | 27,250,000.00 USD | 27,250,000.00 USD | 428,210.00 USD | 67,980.00 USD | 758,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `747.50` | 40,240.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `748.10` | 27,740,000.00 USD | 27,740,000.00 USD | 341,720.00 USD | 72,690.00 USD | 73,330.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `748.50` | 2,970.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `749.00` | 28,150,000.00 USD | 28,150,000.00 USD | 404,680.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `749.50` | 170,970.00 USD | 2,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `749.90` | 28,300,000.00 USD | 28,300,000.00 USD | 157,570.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `750.50` | 6,610.00 USD | 2,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `750.80` | 28,340,000.00 USD | 28,340,000.00 USD | 33,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `751.50` | 714,780.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `751.70` | 28,810,000.00 USD | 28,810,000.00 USD | 53,980.00 USD | 25,010.00 USD | 393,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `752.50` | 47,580.00 USD | 3,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `752.60` | 29,240,000.00 USD | 29,240,000.00 USD | 284,000.00 USD | 0.00 USD | 146,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `753.50` | 29,550,000.00 USD | 29,550,000.00 USD | 47,700.00 USD | 3,810.00 USD | 262,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `754.40` | 30,020,000.00 USD | 30,020,000.00 USD | 352,780.00 USD | 70,850.00 USD | 43,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `754.50` | 863,250.00 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `755.00` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 59,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `755.30` | 30,610,000.00 USD | 30,610,000.00 USD | 289,960.00 USD | 243,600.00 USD | 56,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `755.50` | 2,340.00 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `756.20` | 31,100,000.00 USD | 31,100,000.00 USD | 406,880.00 USD | 35,830.00 USD | 46,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `756.50` | 3,750.00 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `756.80` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 47,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `757.10` | 31,510,000.00 USD | 31,510,000.00 USD | 223,780.00 USD | 122,240.00 USD | 63,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `757.70` | 1,910,000.00 USD | 1,910,000.00 USD | 475,510.00 USD | 113,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `758.00` | 31,970,000.00 USD | 31,970,000.00 USD | 369,420.00 USD | 67,700.00 USD | 18,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `758.50` | 25,140.00 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `758.60` | 3,100,000.00 USD | 3,100,000.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `758.90` | 33,510,000.00 USD | 33,510,000.00 USD | 1,150,000.00 USD | 122,880.00 USD | 273,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `759.50` | 838.49 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `759.80` | 33,930,000.00 USD | 33,930,000.00 USD | 371,250.00 USD | 21,070.00 USD | 22,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `760.40` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 27,650.00 USD | 42,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `760.50` | 540.72 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `760.70` | 34,490,000.00 USD | 34,490,000.00 USD | 354,030.00 USD | 94,530.00 USD | 113,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `761.30` | 3,490,000.00 USD | 3,490,000.00 USD | 10,750.00 USD | 211,960.00 USD | 100,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `761.60` | 35,710,000.00 USD | 35,710,000.00 USD | 778,030.00 USD | 87,560.00 USD | 353,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `762.20` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 699,820.00 USD | 179,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `762.50` | 36,660,000.00 USD | 36,660,000.00 USD | 650,310.00 USD | 184,600.00 USD | 117,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `762.50` | 12,760.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `763.10` | 7,830,000.00 USD | 7,830,000.00 USD | 2,460,000.00 USD | 590,460.00 USD | 404,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `763.40` | 39,720,000.00 USD | 39,720,000.00 USD | 2,300,000.00 USD | 203,280.00 USD | 554,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `763.50` | 447,010.00 USD | 4,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `764.00` | 10,270,000.00 USD | 10,270,000.00 USD | 1,590,000.00 USD | 441,980.00 USD | 402,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `764.30` | 41,790,000.00 USD | 41,790,000.00 USD | 1,610,000.00 USD | 153,350.00 USD | 304,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `764.90` | 12,470,000.00 USD | 12,470,000.00 USD | 1,450,000.00 USD | 352,570.00 USD | 395,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `765.20` | 42,720,000.00 USD | 42,720,000.00 USD | 609,290.00 USD | 223,440.00 USD | 95,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `765.80` | 15,460,000.00 USD | 15,460,000.00 USD | 2,470,000.00 USD | 107,550.00 USD | 416,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `766.10` | 44,360,000.00 USD | 44,360,000.00 USD | 1,030,000.00 USD | 216,550.00 USD | 399,250.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `766.50` | 3,130.00 USD | 4,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `766.70` | 20,050,000.00 USD | 20,050,000.00 USD | 3,330,000.00 USD | 416,530.00 USD | 842,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `767.00` | 46,790,000.00 USD | 46,790,000.00 USD | 2,020,000.00 USD | 104,660.00 USD | 306,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `767.50` | 2,450.00 USD | 4,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `767.60` | 23,430,000.00 USD | 23,430,000.00 USD | 2,790,000.00 USD | 123,530.00 USD | 467,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `767.90` | 48,750,000.00 USD | 48,750,000.00 USD | 1,530,000.00 USD | 124,080.00 USD | 308,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `768.50` | 25,660,000.00 USD | 25,660,000.00 USD | 1,840,000.00 USD | 95,830.00 USD | 281,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `768.50` | 156.77 USD | 4,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `768.80` | 49,670,000.00 USD | 49,670,000.00 USD | 782,650.00 USD | 54,840.00 USD | 76,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `769.40` | 26,810,000.00 USD | 26,810,000.00 USD | 565,780.00 USD | 249,950.00 USD | 333,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `769.70` | 50,440,000.00 USD | 50,440,000.00 USD | 591,420.00 USD | 111,680.00 USD | 69,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `770.30` | 29,310,000.00 USD | 29,310,000.00 USD | 1,900,000.00 USD | 240,530.00 USD | 364,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `770.50` | 2,250.00 USD | 4,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `770.60` | 51,150,000.00 USD | 51,150,000.00 USD | 295,710.00 USD | 95,060.00 USD | 316,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `771.20` | 30,770,000.00 USD | 30,770,000.00 USD | 1,050,000.00 USD | 242,570.00 USD | 162,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `771.50` | 52,600,000.00 USD | 52,600,000.00 USD | 604,710.00 USD | 144,120.00 USD | 705,810.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `771.50` | 10,020.00 USD | 4,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `772.10` | 33,190,000.00 USD | 33,190,000.00 USD | 1,750,000.00 USD | 252,650.00 USD | 419,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `772.40` | 53,200,000.00 USD | 53,200,000.00 USD | 418,600.00 USD | 148,190.00 USD | 33,620.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `772.50` | 9,490.00 USD | 4,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `773.00` | 35,800,000.00 USD | 35,800,000.00 USD | 1,950,000.00 USD | 325,680.00 USD | 338,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `773.30` | 54,450,000.00 USD | 54,450,000.00 USD | 976,860.00 USD | 92,850.00 USD | 181,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `773.50` | 8,230.00 USD | 4,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `773.90` | 37,600,000.00 USD | 37,600,000.00 USD | 1,220,000.00 USD | 276,760.00 USD | 293,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `774.20` | 55,520,000.00 USD | 55,520,000.00 USD | 983,640.00 USD | 62,410.00 USD | 22,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `774.80` | 39,980,000.00 USD | 39,980,000.00 USD | 1,310,000.00 USD | 568,930.00 USD | 502,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `775.10` | 56,080,000.00 USD | 56,080,000.00 USD | 290,910.00 USD | 122,640.00 USD | 141,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `775.70` | 42,470,000.00 USD | 42,470,000.00 USD | 1,830,000.00 USD | 470,960.00 USD | 187,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `776.00` | 56,720,000.00 USD | 56,720,000.00 USD | 430,680.00 USD | 109,470.00 USD | 103,300.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `776.50` | 97,260.00 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `776.60` | 44,740,000.00 USD | 44,740,000.00 USD | 1,630,000.00 USD | 269,050.00 USD | 378,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `776.90` | 57,290,000.00 USD | 57,290,000.00 USD | 412,420.00 USD | 30,600.00 USD | 120,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `777.50` | 46,480,000.00 USD | 46,480,000.00 USD | 1,350,000.00 USD | 243,990.00 USD | 148,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `777.50` | 209.15 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `777.80` | 58,890,000.00 USD | 58,890,000.00 USD | 1,080,000.00 USD | 159,720.00 USD | 366,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `778.40` | 48,170,000.00 USD | 48,170,000.00 USD | 1,180,000.00 USD | 307,370.00 USD | 206,530.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `778.50` | 3,200.00 USD | 4,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `778.70` | 59,520,000.00 USD | 59,520,000.00 USD | 493,740.00 USD | 61,580.00 USD | 76,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `779.30` | 49,730,000.00 USD | 49,730,000.00 USD | 1,240,000.00 USD | 188,170.00 USD | 123,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `779.60` | 60,580,000.00 USD | 60,580,000.00 USD | 814,150.00 USD | 96,550.00 USD | 141,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `780.20` | 51,100,000.00 USD | 51,100,000.00 USD | 1,070,000.00 USD | 86,470.00 USD | 218,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `780.50` | 61,140,000.00 USD | 61,140,000.00 USD | 388,410.00 USD | 100,010.00 USD | 79,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `780.50` | 5,240.00 USD | 4,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `781.10` | 52,710,000.00 USD | 52,710,000.00 USD | 1,270,000.00 USD | 90,990.00 USD | 242,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `781.40` | 61,920,000.00 USD | 61,920,000.00 USD | 511,520.00 USD | 113,520.00 USD | 154,660.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `781.50` | 1,830.00 USD | 4,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `782.00` | 54,610,000.00 USD | 54,610,000.00 USD | 1,510,000.00 USD | 87,670.00 USD | 301,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `782.30` | 63,450,000.00 USD | 63,450,000.00 USD | 1,150,000.00 USD | 49,090.00 USD | 325,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `782.90` | 56,600,000.00 USD | 56,600,000.00 USD | 1,750,000.00 USD | 36,140.00 USD | 202,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `783.20` | 64,250,000.00 USD | 64,250,000.00 USD | 655,850.00 USD | 47,470.00 USD | 100,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `783.80` | 57,170,000.00 USD | 57,170,000.00 USD | 508,000.00 USD | 10,100.00 USD | 54,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `784.10` | 64,610,000.00 USD | 64,610,000.00 USD | 314,540.00 USD | 23,200.00 USD | 18,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `784.70` | 57,480,000.00 USD | 57,480,000.00 USD | 208,380.00 USD | 28,260.00 USD | 70,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `785.00` | 65,160,000.00 USD | 65,160,000.00 USD | 502,530.00 USD | 32,830.00 USD | 19,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `785.50` | 129.61 USD | 4,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `785.60` | 58,610,000.00 USD | 58,610,000.00 USD | 1,010,000.00 USD | 54,140.00 USD | 71,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `785.90` | 65,370,000.00 USD | 65,370,000.00 USD | 179,190.00 USD | 4,490.00 USD | 30,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `786.50` | 59,000,000.00 USD | 59,000,000.00 USD | 329,230.00 USD | 30,660.00 USD | 23,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `786.50` | 126,920.00 USD | 5,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `786.80` | 65,610,000.00 USD | 65,610,000.00 USD | 201,790.00 USD | 23,920.00 USD | 14,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `787.40` | 59,580,000.00 USD | 59,580,000.00 USD | 470,050.00 USD | 17,630.00 USD | 91,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `787.50` | 3,150.00 USD | 5,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `787.70` | 66,460,000.00 USD | 66,460,000.00 USD | 482,920.00 USD | 15,430.00 USD | 350,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `788.30` | 59,940,000.00 USD | 59,940,000.00 USD | 202,630.00 USD | 82,380.00 USD | 81,230.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `788.50` | 1,580.00 USD | 5,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `788.60` | 66,610,000.00 USD | 66,610,000.00 USD | 80,180.00 USD | 0.00 USD | 65,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `789.00` | 66,830,000.00 USD | 66,830,000.00 USD | 220,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `789.20` | 60,780,000.00 USD | 60,780,000.00 USD | 698,830.00 USD | 81,250.00 USD | 55,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `789.50` | 1,250.00 USD | 5,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `790.10` | 61,270,000.00 USD | 61,270,000.00 USD | 299,250.00 USD | 104,360.00 USD | 88,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `791.00` | 62,150,000.00 USD | 62,150,000.00 USD | 693,290.00 USD | 82,870.00 USD | 100,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `791.90` | 63,030,000.00 USD | 63,030,000.00 USD | 816,380.00 USD | 16,830.00 USD | 46,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `792.80` | 63,250,000.00 USD | 63,250,000.00 USD | 205,450.00 USD | 0.00 USD | 14,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `793.50` | 1,280.00 USD | 5,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `793.70` | 63,430,000.00 USD | 63,430,000.00 USD | 184,960.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `794.50` | 8,780.00 USD | 5,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `794.60` | 63,750,000.00 USD | 63,750,000.00 USD | 302,280.00 USD | 15,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `795.50` | 63,890,000.00 USD | 63,890,000.00 USD | 109,640.00 USD | 14,650.00 USD | 14,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `795.50` | 518.67 USD | 5,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `796.40` | 64,030,000.00 USD | 64,030,000.00 USD | 139,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `796.50` | 3,240.00 USD | 5,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `797.30` | 64,090,000.00 USD | 64,090,000.00 USD | 64,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `797.50` | 1,090.00 USD | 5,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `798.20` | 64,250,000.00 USD | 64,250,000.00 USD | 155,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `798.50` | 4,300.00 USD | 5,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `799.10` | 64,290,000.00 USD | 64,290,000.00 USD | 42,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `799.50` | 610.02 USD | 5,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `800.00` | 64,400,000.00 USD | 64,400,000.00 USD | 113,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `800.50` | 1,130.00 USD | 5,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `800.90` | 64,510,000.00 USD | 64,510,000.00 USD | 77,580.00 USD | 8,370.00 USD | 21,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `801.50` | 6,110.00 USD | 5,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `801.80` | 64,720,000.00 USD | 64,720,000.00 USD | 179,900.00 USD | 16,330.00 USD | 10,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `802.50` | 778,380.00 USD | 5,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `802.70` | 64,730,000.00 USD | 64,730,000.00 USD | 11,220.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `803.50` | 121,930.00 USD | 5,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `803.60` | 64,760,000.00 USD | 64,760,000.00 USD | 27,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `804.50` | 64,840,000.00 USD | 64,840,000.00 USD | 32,340.00 USD | 18,260.00 USD | 32,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `804.50` | 105.39 USD | 5,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `805.40` | 64,910,000.00 USD | 64,910,000.00 USD | 56,700.00 USD | 8,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `805.50` | 47,420.00 USD | 6,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `806.30` | 64,920,000.00 USD | 64,920,000.00 USD | 3,270.00 USD | 12,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `806.50` | 2,890.00 USD | 6,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `807.20` | 64,970,000.00 USD | 64,970,000.00 USD | 39,190.00 USD | 0.00 USD | 11,830.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `807.50` | 738.06 USD | 6,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `808.10` | 65,030,000.00 USD | 65,030,000.00 USD | 17,980.00 USD | 5,360.00 USD | 29,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `808.50` | 11,780.00 USD | 6,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `809.00` | 65,110,000.00 USD | 65,110,000.00 USD | 58,620.00 USD | 13,120.00 USD | 13,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `809.50` | 342.42 USD | 6,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `809.90` | 65,330,000.00 USD | 65,330,000.00 USD | 178,130.00 USD | 9,760.00 USD | 36,490.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `810.50` | 568.16 USD | 6,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `810.80` | 65,420,000.00 USD | 65,420,000.00 USD | 78,030.00 USD | 6,630.00 USD | 5,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `811.70` | 65,480,000.00 USD | 65,480,000.00 USD | 19,210.00 USD | 12,110.00 USD | 29,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `812.60` | 65,600,000.00 USD | 65,600,000.00 USD | 68,390.00 USD | 17,450.00 USD | 31,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `813.50` | 65,860,000.00 USD | 65,860,000.00 USD | 147,480.00 USD | 59,640.00 USD | 45,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `814.40` | 66,180,000.00 USD | 66,180,000.00 USD | 218,130.00 USD | 32,770.00 USD | 74,730.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `814.50` | 692.32 USD | 6,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `815.30` | 66,390,000.00 USD | 66,390,000.00 USD | 171,100.00 USD | 24,290.00 USD | 10,150.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `815.50` | 6,020.00 USD | 6,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `816.20` | 66,690,000.00 USD | 66,690,000.00 USD | 203,680.00 USD | 44,470.00 USD | 59,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `816.50` | 15,410.00 USD | 6,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `817.10` | 67,090,000.00 USD | 67,090,000.00 USD | 278,420.00 USD | 76,830.00 USD | 42,530.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `817.50` | 325.37 USD | 6,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `818.00` | 67,550,000.00 USD | 67,550,000.00 USD | 346,550.00 USD | 48,360.00 USD | 67,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `818.90` | 67,790,000.00 USD | 67,790,000.00 USD | 180,470.00 USD | 8,160.00 USD | 47,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `819.80` | 68,300,000.00 USD | 68,300,000.00 USD | 295,510.00 USD | 101,950.00 USD | 107,190.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `820.50` | 8,340.00 USD | 6,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `820.70` | 68,600,000.00 USD | 68,600,000.00 USD | 235,990.00 USD | 41,190.00 USD | 24,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `821.50` | 11,710.00 USD | 6,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `821.60` | 68,800,000.00 USD | 68,800,000.00 USD | 86,380.00 USD | 62,620.00 USD | 55,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `822.50` | 69,300,000.00 USD | 69,300,000.00 USD | 394,120.00 USD | 64,970.00 USD | 42,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `822.50` | 3,540.00 USD | 6,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `823.40` | 69,630,000.00 USD | 69,630,000.00 USD | 213,450.00 USD | 68,530.00 USD | 45,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `824.30` | 69,980,000.00 USD | 69,980,000.00 USD | 248,860.00 USD | 58,170.00 USD | 43,880.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `824.50` | 425.44 USD | 6,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `825.20` | 70,340,000.00 USD | 70,340,000.00 USD | 277,990.00 USD | 21,630.00 USD | 61,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `826.10` | 70,650,000.00 USD | 70,650,000.00 USD | 223,810.00 USD | 27,390.00 USD | 53,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `826.50` | 7,510.00 USD | 6,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `827.00` | 71,290,000.00 USD | 71,290,000.00 USD | 494,310.00 USD | 23,200.00 USD | 126,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `827.50` | 480,240.00 USD | 6,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `827.90` | 71,650,000.00 USD | 71,650,000.00 USD | 297,880.00 USD | 0.00 USD | 63,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `828.50` | 12,770.00 USD | 6,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `828.80` | 71,840,000.00 USD | 71,840,000.00 USD | 184,280.00 USD | 0.00 USD | 5,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `829.70` | 71,930,000.00 USD | 71,930,000.00 USD | 43,760.00 USD | 5,190.00 USD | 33,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `830.60` | 72,180,000.00 USD | 72,180,000.00 USD | 221,150.00 USD | 5,300.00 USD | 28,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `831.50` | 72,220,000.00 USD | 72,220,000.00 USD | 37,200.00 USD | 5,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `834.50` | 83,370.00 USD | 6,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `835.50` | 85,260.00 USD | 6,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `836.50` | 8,370.00 USD | 6,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `837.50` | 3,570.00 USD | 6,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `838.50` | 21,840.00 USD | 6,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `839.50` | 167.90 USD | 6,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `841.50` | 2,830.00 USD | 6,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `842.50` | 1,750.00 USD | 6,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `843.50` | 227.75 USD | 6,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `848.50` | 289.34 USD | 6,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `849.50` | 34,300.00 USD | 6,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `850.50` | 108.86 USD | 6,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `856.50` | 256.09 USD | 6,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `858.50` | 528,740.00 USD | 7,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `859.50` | 1,180.00 USD | 7,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `865.50` | 18,900.00 USD | 7,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `870.50` | 6,090.00 USD | 7,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `872.50` | 292,870.00 USD | 7,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `875.50` | 14,000.00 USD | 7,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `877.50` | 614,250.00 USD | 8,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `878.50` | 92,600.00 USD | 8,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `880.50` | 663.02 USD | 8,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `885.50` | 3,200.00 USD | 8,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `886.50` | 812.92 USD | 8,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `887.50` | 13,920.00 USD | 8,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `888.50` | 178,210.00 USD | 8,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `891.50` | 11,300.00 USD | 8,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `893.50` | 173.34 USD | 8,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `894.50` | 26,840.00 USD | 8,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `896.50` | 228,220.00 USD | 8,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `898.50` | 127.59 USD | 8,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `902.50` | 305.05 USD | 8,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `904.50` | 63,930.00 USD | 8,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `906.50` | 313.65 USD | 8,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `908.50` | 1,790.00 USD | 8,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `909.50` | 29,900.00 USD | 8,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `910.50` | 83,430.00 USD | 9,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `911.50` | 34,670.00 USD | 9,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `912.50` | 37,330.00 USD | 9,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `913.50` | 116.93 USD | 9,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `917.50` | 390.86 USD | 9,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `918.50` | 17,510.00 USD | 9,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `920.50` | 92,050.00 USD | 9,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `925.50` | 9,260.00 USD | 9,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `934.50` | 656.02 USD | 9,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `935.50` | 65,480.00 USD | 9,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `937.50` | 13,130.00 USD | 9,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `945.50` | 58,060.00 USD | 9,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `950.50` | 2,380.00 USD | 9,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `951.50` | 397.73 USD | 9,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `954.50` | 18,890.00 USD | 9,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `960.50` | 114.30 USD | 9,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `963.50` | 205.23 USD | 9,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `966.50` | 6,960.00 USD | 9,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `969.50` | 5,780.00 USD | 9,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `971.50` | 847,970.00 USD | 10,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `972.50` | 1,950.00 USD | 10,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `976.50` | 14,200.00 USD | 10,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `977.50` | 3,270.00 USD | 10,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `981.50` | 14,480.00 USD | 10,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `986.50` | 1,100.00 USD | 10,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `990.50` | 28,300.00 USD | 10,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `992.50` | 2,140.00 USD | 10,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `993.50` | 975.62 USD | 10,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `994.50` | 285,520.00 USD | 10,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `995.50` | 481,020.00 USD | 11,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `996.50` | 989.52 USD | 11,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `997.50` | 7,300.00 USD | 11,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `998.50` | 9,550.00 USD | 11,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `999.50` | 136,800.00 USD | 11,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1003.50` | 1,620.00 USD | 11,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1005.50` | 4,050.00 USD | 11,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1008.50` | 28,800.00 USD | 11,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1009.50` | 51,680.00 USD | 11,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1010.50` | 101,810.00 USD | 11,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1011.50` | 3,160.00 USD | 11,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1014.50` | 1,450.00 USD | 11,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1024.50` | 2,850.00 USD | 11,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1037.50` | 302,500.00 USD | 11,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1038.50` | 724,470.00 USD | 12,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1039.50` | 96,150.00 USD | 12,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1047.50` | 504.89 USD | 12,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1050.50` | 500.04 USD | 12,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1064.50` | 1,600.00 USD | 12,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1067.50` | 15,380.00 USD | 12,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1073.50` | 1,610.00 USD | 12,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1074.50` | 68,680.00 USD | 12,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1081.50` | 121.13 USD | 12,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1085.50` | 4,330.00 USD | 12,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1087.50` | 5,770.00 USD | 12,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1088.50` | 15,780.00 USD | 12,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1093.50` | 120,790.00 USD | 12,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1096.50` | 162,020.00 USD | 12,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1103.50` | 2,300,000.00 USD | 15,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1106.50` | 115,080.00 USD | 15,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1137.50` | 341,250.00 USD | 15,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1139.50` | 61,760.00 USD | 15,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1144.50` | 78,470.00 USD | 15,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1147.50` | 20,460.00 USD | 15,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1150.50` | 19,980.00 USD | 15,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1161.50` | 1,550.00 USD | 15,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1163.50` | 11,810.00 USD | 15,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1170.50` | 156.85 USD | 15,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1178.50` | 66,060.00 USD | 15,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1181.50` | 57,080.00 USD | 16,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1196.50` | 206.99 USD | 16,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1197.50` | 463.43 USD | 16,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1202.50` | 118,760.00 USD | 16,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1207.50` | 385.19 USD | 16,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1213.50` | 126.20 USD | 16,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1218.50` | 704.29 USD | 16,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1220.50` | 30,490.00 USD | 16,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1221.50` | 42,750.00 USD | 16,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1224.50` | 1,030.00 USD | 16,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1227.50` | 4,900.00 USD | 16,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1231.50` | 3,740.00 USD | 16,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1239.50` | 111,560.00 USD | 16,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1241.50` | 26,600.00 USD | 16,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1245.50` | 37,630.00 USD | 16,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1247.50` | 134,380.00 USD | 16,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1249.50` | 20,870.00 USD | 16,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1251.50` | 100.12 USD | 16,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1256.50` | 113,080.00 USD | 16,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1259.50` | 201.52 USD | 16,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1268.50` | 1,580,000.00 USD | 18,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1278.50` | 109,060.00 USD | 18,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1290.50` | 62,100.00 USD | 18,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1293.50` | 25,460.00 USD | 18,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1294.50` | 32,170.00 USD | 18,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1295.50` | 7,200.00 USD | 18,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1299.50` | 4,020.00 USD | 18,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1300.50` | 5,800.00 USD | 18,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1304.50` | 1,840,000.00 USD | 20,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1312.50` | 645.75 USD | 20,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1314.50` | 1,850.00 USD | 20,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1316.50` | 7,580.00 USD | 20,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1317.50` | 2,810.00 USD | 20,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1319.50` | 14,130.00 USD | 20,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1323.50` | 115.14 USD | 20,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1327.50` | 138.06 USD | 20,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1328.50` | 168,850.00 USD | 20,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1330.50` | 23,470.00 USD | 20,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1339.50` | 87,070.00 USD | 20,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1346.50` | 26,930.00 USD | 20,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1350.50` | 1,350.00 USD | 20,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1365.50` | 71,280.00 USD | 20,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1366.50` | 2,930.00 USD | 20,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1367.50` | 4,100.00 USD | 20,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1369.50` | 46,880.00 USD | 20,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1401.50` | 177.99 USD | 20,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1405.50` | 4,770.00 USD | 20,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1407.50` | 32,370.00 USD | 20,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1417.50` | 4,900.00 USD | 20,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `143.50` | 5,900,000.00 USD | 0.00 USD | 2,870.00 USD | `-80.03%` | `20,000,000,000.00` |
| `Live` | `Long` | `145.50` | 5,900,000.00 USD | 0.00 USD | 2,040.00 USD | `-79.75%` | `14,000,000,000.00` |
| `Live` | `Long` | `146.50` | 5,890,000.00 USD | 0.00 USD | 886.32 USD | `-79.61%` | `6,050,000,000.00` |
| `Live` | `Long` | `150.50` | 5,890,000.00 USD | 0.00 USD | 288.36 USD | `-79.05%` | `1,916,000,000.00` |
| `Live` | `Long` | `155.50` | 5,890,000.00 USD | 0.00 USD | 2,890.00 USD | `-78.35%` | `18,565,000,000.00` |
| `Live` | `Long` | `157.50` | 5,890,000.00 USD | 0.00 USD | 94,500.00 USD | `-78.08%` | `600,000,000,000.00` |
| `Live` | `Long` | `164.50` | 5,800,000.00 USD | 0.00 USD | 468.33 USD | `-77.10%` | `2,847,000,000.00` |
| `Live` | `Long` | `178.50` | 5,790,000.00 USD | 0.00 USD | 239.90 USD | `-75.15%` | `1,344,000,000.00` |
| `Live` | `Long` | `179.50` | 5,790,000.00 USD | 0.00 USD | 6,090.00 USD | `-75.01%` | `33,907,000,000.00` |
| `Live` | `Long` | `195.50` | 5,790,000.00 USD | 0.00 USD | 1,840.00 USD | `-72.79%` | `9,406,000,000.00` |
| `Live` | `Long` | `202.50` | 5,790,000.00 USD | 0.00 USD | 6,910.00 USD | `-71.81%` | `34,129,000,000.00` |
| `Live` | `Long` | `203.50` | 5,780,000.00 USD | 0.00 USD | 572,960.00 USD | `-71.67%` | `2,815,552,000,000.00` |
| `Live` | `Long` | `209.50` | 5,210,000.00 USD | 0.00 USD | 20,950.00 USD | `-70.84%` | `100,000,000,000.00` |
| `Live` | `Long` | `212.50` | 5,190,000.00 USD | 0.00 USD | 212,500.00 USD | `-70.42%` | `1,000,000,000,000.00` |
| `Live` | `Long` | `213.50` | 4,970,000.00 USD | 0.00 USD | 1,530.00 USD | `-70.28%` | `7,186,000,000.00` |
| `Live` | `Long` | `219.50` | 4,970,000.00 USD | 0.00 USD | 191.18 USD | `-69.45%` | `871,000,000.00` |
| `Live` | `Long` | `231.50` | 4,970,000.00 USD | 0.00 USD | 284.51 USD | `-67.78%` | `1,229,000,000.00` |
| `Live` | `Long` | `249.50` | 4,970,000.00 USD | 0.00 USD | 1,100.00 USD | `-65.27%` | `4,407,000,000.00` |
| `Live` | `Long` | `251.50` | 4,970,000.00 USD | 0.00 USD | 18,730.00 USD | `-64.99%` | `74,470,000,000.00` |
| `Live` | `Long` | `257.50` | 4,950,000.00 USD | 0.00 USD | 430,750.00 USD | `-64.16%` | `1,672,813,000,000.00` |
| `Live` | `Long` | `267.50` | 4,520,000.00 USD | 0.00 USD | 21,200.00 USD | `-62.76%` | `79,269,000,000.00` |
| `Live` | `Long` | `269.50` | 4,500,000.00 USD | 0.00 USD | 4,790.00 USD | `-62.49%` | `17,770,000,000.00` |
| `Live` | `Long` | `280.50` | 4,490,000.00 USD | 0.00 USD | 426.64 USD | `-60.95%` | `1,521,000,000.00` |
| `Live` | `Long` | `283.50` | 4,490,000.00 USD | 0.00 USD | 567.00 USD | `-60.54%` | `2,000,000,000.00` |
| `Live` | `Long` | `287.50` | 4,490,000.00 USD | 0.00 USD | 19,970.00 USD | `-59.98%` | `69,447,000,000.00` |
| `Live` | `Long` | `291.50` | 4,470,000.00 USD | 0.00 USD | 434.04 USD | `-59.42%` | `1,489,000,000.00` |
| `Live` | `Long` | `292.50` | 4,470,000.00 USD | 0.00 USD | 9,350.00 USD | `-59.28%` | `31,975,000,000.00` |
| `Live` | `Long` | `302.50` | 4,460,000.00 USD | 0.00 USD | 150,300.00 USD | `-57.89%` | `496,876,000,000.00` |
| `Live` | `Long` | `312.50` | 4,310,000.00 USD | 0.00 USD | 500.00 USD | `-56.50%` | `1,600,000,000.00` |
| `Live` | `Long` | `316.50` | 4,310,000.00 USD | 0.00 USD | 12,660.00 USD | `-55.94%` | `40,000,000,000.00` |
| `Live` | `Long` | `326.50` | 4,300,000.00 USD | 0.00 USD | 500.85 USD | `-54.55%` | `1,534,000,000.00` |
| `Live` | `Long` | `327.50` | 4,300,000.00 USD | 0.00 USD | 314.07 USD | `-54.41%` | `959,000,000.00` |
| `Live` | `Long` | `332.50` | 4,300,000.00 USD | 0.00 USD | 150.29 USD | `-53.72%` | `452,000,000.00` |
| `Live` | `Long` | `333.50` | 4,300,000.00 USD | 0.00 USD | 226.45 USD | `-53.58%` | `679,000,000.00` |
| `Live` | `Long` | `339.50` | 4,300,000.00 USD | 0.00 USD | 9,350.00 USD | `-52.74%` | `27,554,000,000.00` |
| `Live` | `Long` | `342.50` | 4,290,000.00 USD | 0.00 USD | 1,730.00 USD | `-52.32%` | `5,047,000,000.00` |
| `Live` | `Long` | `343.50` | 4,290,000.00 USD | 0.00 USD | 137,520.00 USD | `-52.19%` | `400,353,000,000.00` |
| `Live` | `Long` | `344.50` | 4,150,000.00 USD | 0.00 USD | 953.23 USD | `-52.05%` | `2,767,000,000.00` |
| `Live` | `Long` | `356.50` | 4,150,000.00 USD | 0.00 USD | 3,570.00 USD | `-50.38%` | `10,019,000,000.00` |
| `Live` | `Long` | `359.50` | 4,150,000.00 USD | 0.00 USD | 212.10 USD | `-49.96%` | `590,000,000.00` |
| `Live` | `Long` | `363.50` | 4,150,000.00 USD | 0.00 USD | 340.60 USD | `-49.40%` | `937,000,000.00` |
| `Live` | `Long` | `365.50` | 4,150,000.00 USD | 0.00 USD | 1,650.00 USD | `-49.12%` | `4,504,000,000.00` |
| `Live` | `Long` | `366.50` | 4,140,000.00 USD | 0.00 USD | 6,990.00 USD | `-48.98%` | `19,076,000,000.00` |
| `Live` | `Long` | `367.50` | 4,140,000.00 USD | 0.00 USD | 146.63 USD | `-48.84%` | `399,000,000.00` |
| `Live` | `Long` | `368.50` | 4,140,000.00 USD | 0.00 USD | 15,810.00 USD | `-48.71%` | `42,904,000,000.00` |
| `Live` | `Long` | `371.50` | 4,120,000.00 USD | 0.00 USD | 146.37 USD | `-48.29%` | `394,000,000.00` |
| `Live` | `Long` | `372.50` | 4,120,000.00 USD | 0.00 USD | 27,270.00 USD | `-48.15%` | `73,204,000,000.00` |
| `Live` | `Long` | `373.50` | 4,090,000.00 USD | 0.00 USD | 15,910.00 USD | `-48.01%` | `42,597,000,000.00` |
| `Live` | `Long` | `374.50` | 4,080,000.00 USD | 0.00 USD | 1,820.00 USD | `-47.87%` | `4,868,000,000.00` |
| `Live` | `Long` | `377.50` | 4,080,000.00 USD | 0.00 USD | 1,400.00 USD | `-47.45%` | `3,716,000,000.00` |
| `Live` | `Long` | `378.50` | 4,070,000.00 USD | 0.00 USD | 643.45 USD | `-47.31%` | `1,700,000,000.00` |
| `Live` | `Long` | `381.50` | 4,070,000.00 USD | 0.00 USD | 1,910.00 USD | `-46.90%` | `5,000,000,000.00` |
| `Live` | `Long` | `383.50` | 4,070,000.00 USD | 0.00 USD | 10,900.00 USD | `-46.62%` | `28,414,000,000.00` |
| `Live` | `Long` | `384.50` | 4,060,000.00 USD | 0.00 USD | 1,060.00 USD | `-46.48%` | `2,746,000,000.00` |
| `Live` | `Long` | `385.50` | 4,060,000.00 USD | 0.00 USD | 1,800.00 USD | `-46.34%` | `4,675,000,000.00` |
| `Live` | `Long` | `386.50` | 4,060,000.00 USD | 0.00 USD | 531.44 USD | `-46.20%` | `1,375,000,000.00` |
| `Live` | `Long` | `387.50` | 4,060,000.00 USD | 0.00 USD | 392.54 USD | `-46.06%` | `1,013,000,000.00` |
| `Live` | `Long` | `389.50` | 4,060,000.00 USD | 0.00 USD | 5,500.00 USD | `-45.78%` | `14,117,000,000.00` |
| `Live` | `Long` | `390.50` | 4,050,000.00 USD | 0.00 USD | 1,660.00 USD | `-45.64%` | `4,250,000,000.00` |
| `Live` | `Long` | `393.50` | 4,050,000.00 USD | 0.00 USD | 536.73 USD | `-45.23%` | `1,364,000,000.00` |
| `Live` | `Long` | `394.50` | 4,050,000.00 USD | 0.00 USD | 168.06 USD | `-45.09%` | `426,000,000.00` |
| `Live` | `Long` | `395.50` | 4,050,000.00 USD | 0.00 USD | 2,110.00 USD | `-44.95%` | `5,347,000,000.00` |
| `Live` | `Long` | `396.50` | 4,050,000.00 USD | 0.00 USD | 317.20 USD | `-44.81%` | `800,000,000.00` |
| `Live` | `Long` | `398.50` | 4,050,000.00 USD | 0.00 USD | 523.63 USD | `-44.53%` | `1,314,000,000.00` |
| `Live` | `Long` | `399.50` | 4,050,000.00 USD | 0.00 USD | 603.64 USD | `-44.39%` | `1,511,000,000.00` |
| `Live` | `Long` | `400.50` | 4,050,000.00 USD | 0.00 USD | 7,610.00 USD | `-44.25%` | `19,000,000,000.00` |
| `Live` | `Long` | `402.50` | 4,040,000.00 USD | 0.00 USD | 29,880.00 USD | `-43.97%` | `74,245,000,000.00` |
| `Live` | `Long` | `404.50` | 4,010,000.00 USD | 0.00 USD | 102.34 USD | `-43.69%` | `253,000,000.00` |
| `Live` | `Long` | `409.50` | 4,010,000.00 USD | 0.00 USD | 613.02 USD | `-43.00%` | `1,497,000,000.00` |
| `Live` | `Long` | `410.50` | 4,010,000.00 USD | 0.00 USD | 105.91 USD | `-42.86%` | `258,000,000.00` |
| `Live` | `Long` | `412.50` | 4,010,000.00 USD | 0.00 USD | 3,490.00 USD | `-42.58%` | `8,455,000,000.00` |
| `Live` | `Long` | `413.50` | 4,000,000.00 USD | 0.00 USD | 11,400.00 USD | `-42.44%` | `27,562,000,000.00` |
| `Live` | `Long` | `414.50` | 3,990,000.00 USD | 0.00 USD | 1,890.00 USD | `-42.30%` | `4,566,000,000.00` |
| `Live` | `Long` | `415.50` | 3,990,000.00 USD | 0.00 USD | 1,810.00 USD | `-42.16%` | `4,368,000,000.00` |
| `Live` | `Long` | `417.50` | 3,990,000.00 USD | 0.00 USD | 7,140.00 USD | `-41.88%` | `17,092,000,000.00` |
| `Live` | `Long` | `418.50` | 3,980,000.00 USD | 0.00 USD | 318.06 USD | `-41.75%` | `760,000,000.00` |
| `Live` | `Long` | `419.50` | 3,980,000.00 USD | 0.00 USD | 2,650.00 USD | `-41.61%` | `6,316,000,000.00` |
| `Live` | `Long` | `421.50` | 3,980,000.00 USD | 0.00 USD | 2,320.00 USD | `-41.33%` | `5,496,000,000.00` |
| `Live` | `Long` | `422.50` | 3,980,000.00 USD | 0.00 USD | 92,990.00 USD | `-41.19%` | `220,103,000,000.00` |
| `Live` | `Long` | `426.50` | 3,880,000.00 USD | 0.00 USD | 3,330.00 USD | `-40.63%` | `7,799,000,000.00` |
| `Live` | `Long` | `429.50` | 3,880,000.00 USD | 0.00 USD | 846.12 USD | `-40.21%` | `1,970,000,000.00` |
| `Live` | `Long` | `430.50` | 3,880,000.00 USD | 0.00 USD | 185.12 USD | `-40.08%` | `430,000,000.00` |
| `Live` | `Long` | `431.50` | 3,880,000.00 USD | 0.00 USD | 612.73 USD | `-39.94%` | `1,420,000,000.00` |
| `Live` | `Long` | `434.50` | 3,880,000.00 USD | 0.00 USD | 1,470.00 USD | `-39.52%` | `3,381,000,000.00` |
| `Live` | `Long` | `436.50` | 3,880,000.00 USD | 0.00 USD | 133.13 USD | `-39.24%` | `305,000,000.00` |
| `Live` | `Long` | `438.50` | 3,880,000.00 USD | 0.00 USD | 1,790.00 USD | `-38.96%` | `4,087,000,000.00` |
| `Live` | `Long` | `445.50` | 3,880,000.00 USD | 0.00 USD | 1,450.00 USD | `-37.99%` | `3,259,000,000.00` |
| `Live` | `Long` | `446.50` | 3,870,000.00 USD | 0.00 USD | 639.39 USD | `-37.85%` | `1,432,000,000.00` |
| `Live` | `Long` | `448.50` | 3,870,000.00 USD | 0.00 USD | 3,350.00 USD | `-37.57%` | `7,470,000,000.00` |
| `Live` | `Long` | `456.50` | 3,870,000.00 USD | 0.00 USD | 4,730.00 USD | `-36.46%` | `10,359,000,000.00` |
| `Live` | `Long` | `459.50` | 3,870,000.00 USD | 0.00 USD | 107,060.00 USD | `-36.04%` | `233,000,000,000.00` |
| `Live` | `Long` | `464.50` | 3,760,000.00 USD | 0.00 USD | 3,590.00 USD | `-35.34%` | `7,718,000,000.00` |
| `Live` | `Long` | `469.50` | 3,750,000.00 USD | 0.00 USD | 4,370.00 USD | `-34.65%` | `9,301,000,000.00` |
| `Live` | `Long` | `475.50` | 3,750,000.00 USD | 0.00 USD | 5,320.00 USD | `-33.81%` | `11,182,000,000.00` |
| `Live` | `Long` | `481.50` | 3,740,000.00 USD | 0.00 USD | 615.36 USD | `-32.98%` | `1,278,000,000.00` |
| `Live` | `Long` | `482.50` | 3,740,000.00 USD | 0.00 USD | 6,840.00 USD | `-32.84%` | `14,184,000,000.00` |
| `Live` | `Long` | `484.50` | 3,740,000.00 USD | 0.00 USD | 3,330.00 USD | `-32.56%` | `6,864,000,000.00` |
| `Live` | `Long` | `485.50` | 3,730,000.00 USD | 0.00 USD | 2,400.00 USD | `-32.42%` | `4,947,000,000.00` |
| `Live` | `Long` | `487.50` | 3,730,000.00 USD | 0.00 USD | 464.59 USD | `-32.14%` | `953,000,000.00` |
| `Live` | `Long` | `488.50` | 3,730,000.00 USD | 0.00 USD | 2,300.00 USD | `-32.00%` | `4,712,000,000.00` |
| `Live` | `Long` | `493.50` | 3,730,000.00 USD | 0.00 USD | 1,840.00 USD | `-31.31%` | `3,720,000,000.00` |
| `Live` | `Long` | `495.50` | 3,730,000.00 USD | 0.00 USD | 282.93 USD | `-31.03%` | `571,000,000.00` |
| `Live` | `Long` | `498.50` | 3,730,000.00 USD | 0.00 USD | 1,820.00 USD | `-30.61%` | `3,656,000,000.00` |
| `Live` | `Long` | `499.50` | 3,720,000.00 USD | 0.00 USD | 16,240.00 USD | `-30.47%` | `32,507,000,000.00` |
| `Live` | `Long` | `501.50` | 3,710,000.00 USD | 0.00 USD | 7,760.00 USD | `-30.19%` | `15,482,000,000.00` |
| `Live` | `Long` | `502.50` | 3,700,000.00 USD | 0.00 USD | 7,070.00 USD | `-30.05%` | `14,078,000,000.00` |
| `Live` | `Long` | `505.50` | 3,690,000.00 USD | 0.00 USD | 5,760.00 USD | `-29.64%` | `11,387,000,000.00` |
| `Live` | `Long` | `508.50` | 3,690,000.00 USD | 0.00 USD | 41,890.00 USD | `-29.22%` | `82,383,000,000.00` |
| `Live` | `Long` | `509.50` | 3,650,000.00 USD | 0.00 USD | 4,780.00 USD | `-29.08%` | `9,390,000,000.00` |
| `Live` | `Long` | `510.50` | 3,640,000.00 USD | 0.00 USD | 4,080.00 USD | `-28.94%` | `8,000,000,000.00` |
| `Live` | `Long` | `511.50` | 3,640,000.00 USD | 0.00 USD | 5,870.00 USD | `-28.80%` | `11,467,000,000.00` |
| `Live` | `Long` | `513.50` | 3,630,000.00 USD | 0.00 USD | 2,520.00 USD | `-28.52%` | `4,914,000,000.00` |
| `Live` | `Long` | `514.50` | 3,630,000.00 USD | 0.00 USD | 701.78 USD | `-28.38%` | `1,364,000,000.00` |
| `Live` | `Long` | `515.50` | 3,630,000.00 USD | 0.00 USD | 5,990.00 USD | `-28.24%` | `11,621,000,000.00` |
| `Live` | `Long` | `516.50` | 3,620,000.00 USD | 0.00 USD | 115,530.00 USD | `-28.10%` | `223,684,000,000.00` |
| `Live` | `Long` | `517.50` | 3,510,000.00 USD | 0.00 USD | 22,650.00 USD | `-27.96%` | `43,765,000,000.00` |
| `Live` | `Long` | `519.50` | 3,480,000.00 USD | 0.00 USD | 968.35 USD | `-27.69%` | `1,864,000,000.00` |
| `Live` | `Long` | `520.50` | 3,480,000.00 USD | 0.00 USD | 272.22 USD | `-27.55%` | `523,000,000.00` |
| `Live` | `Long` | `521.50` | 3,480,000.00 USD | 0.00 USD | 838.05 USD | `-27.41%` | `1,607,000,000.00` |
| `Live` | `Long` | `522.50` | 3,480,000.00 USD | 0.00 USD | 2,090.00 USD | `-27.27%` | `3,993,000,000.00` |
| `Live` | `Long` | `523.50` | 3,480,000.00 USD | 0.00 USD | 178,430.00 USD | `-27.13%` | `340,839,000,000.00` |
| `Live` | `Long` | `524.50` | 3,300,000.00 USD | 0.00 USD | 833.43 USD | `-26.99%` | `1,589,000,000.00` |
| `Live` | `Long` | `526.50` | 3,300,000.00 USD | 0.00 USD | 1,700.00 USD | `-26.71%` | `3,234,000,000.00` |
| `Live` | `Long` | `528.50` | 3,300,000.00 USD | 0.00 USD | 76,160.00 USD | `-26.43%` | `144,110,000,000.00` |
| `Live` | `Long` | `529.50` | 3,220,000.00 USD | 0.00 USD | 42,820.00 USD | `-26.29%` | `80,869,000,000.00` |
| `Live` | `Long` | `530.50` | 3,180,000.00 USD | 0.00 USD | 18,050.00 USD | `-26.16%` | `34,028,000,000.00` |
| `Live` | `Long` | `531.50` | 3,160,000.00 USD | 0.00 USD | 484.73 USD | `-26.02%` | `912,000,000.00` |
| `Live` | `Long` | `532.50` | 3,160,000.00 USD | 0.00 USD | 422.81 USD | `-25.88%` | `794,000,000.00` |
| `Live` | `Long` | `534.50` | 3,160,000.00 USD | 0.00 USD | 555.35 USD | `-25.60%` | `1,039,000,000.00` |
| `Live` | `Long` | `535.50` | 3,160,000.00 USD | 0.00 USD | 1,750.00 USD | `-25.46%` | `3,259,000,000.00` |
| `Live` | `Long` | `539.50` | 3,160,000.00 USD | 0.00 USD | 490.94 USD | `-24.90%` | `910,000,000.00` |
| `Live` | `Long` | `540.50` | 3,160,000.00 USD | 0.00 USD | 471.32 USD | `-24.76%` | `872,000,000.00` |
| `Live` | `Long` | `543.50` | 3,160,000.00 USD | 0.00 USD | 2,680.00 USD | `-24.35%` | `4,927,000,000.00` |
| `Live` | `Long` | `544.50` | 3,160,000.00 USD | 0.00 USD | 210,830.00 USD | `-24.21%` | `387,204,000,000.00` |
| `Live` | `Long` | `545.50` | 2,940,000.00 USD | 0.00 USD | 1,580.00 USD | `-24.07%` | `2,900,000,000.00` |
| `Live` | `Long` | `546.50` | 2,940,000.00 USD | 0.00 USD | 530.11 USD | `-23.93%` | `970,000,000.00` |
| `Live` | `Long` | `548.50` | 2,940,000.00 USD | 0.00 USD | 1,980.00 USD | `-23.65%` | `3,611,000,000.00` |
| `Live` | `Long` | `549.50` | 2,940,000.00 USD | 0.00 USD | 1,370.00 USD | `-23.51%` | `2,496,000,000.00` |
| `Live` | `Long` | `550.50` | 2,940,000.00 USD | 0.00 USD | 633.63 USD | `-23.37%` | `1,151,000,000.00` |
| `Live` | `Long` | `551.50` | 2,940,000.00 USD | 0.00 USD | 1,250.00 USD | `-23.23%` | `2,271,000,000.00` |
| `Live` | `Long` | `552.50` | 2,940,000.00 USD | 0.00 USD | 24,120.00 USD | `-23.09%` | `43,665,000,000.00` |
| `Live` | `Long` | `553.50` | 2,910,000.00 USD | 0.00 USD | 3,080.00 USD | `-22.95%` | `5,565,000,000.00` |
| `Live` | `Long` | `556.50` | 2,910,000.00 USD | 0.00 USD | 5,670.00 USD | `-22.54%` | `10,193,000,000.00` |
| `Live` | `Long` | `557.50` | 2,900,000.00 USD | 0.00 USD | 10,020.00 USD | `-22.40%` | `17,967,000,000.00` |
| `Live` | `Long` | `558.50` | 2,890,000.00 USD | 0.00 USD | 212.23 USD | `-22.26%` | `380,000,000.00` |
| `Live` | `Long` | `560.50` | 2,890,000.00 USD | 0.00 USD | 582.36 USD | `-21.98%` | `1,039,000,000.00` |
| `Live` | `Long` | `568.50` | 2,890,000.00 USD | 0.00 USD | 454.80 USD | `-20.87%` | `800,000,000.00` |
| `Live` | `Long` | `569.50` | 2,890,000.00 USD | 0.00 USD | 144.08 USD | `-20.73%` | `253,000,000.00` |
| `Live` | `Long` | `571.50` | 2,890,000.00 USD | 0.00 USD | 712,450.00 USD | `-20.45%` | `1,246,635,000,000.00` |
| `Live` | `Long` | `572.50` | 2,180,000.00 USD | 0.00 USD | 8,800.00 USD | `-20.31%` | `15,374,000,000.00` |
| `Live` | `Long` | `573.50` | 2,170,000.00 USD | 0.00 USD | 286.75 USD | `-20.17%` | `500,000,000.00` |
| `Live` | `Long` | `574.50` | 2,170,000.00 USD | 0.00 USD | 323.44 USD | `-20.03%` | `563,000,000.00` |
| `Live` | `Long` | `576.50` | 2,170,000.00 USD | 0.00 USD | 4,810.00 USD | `-19.75%` | `8,349,000,000.00` |
| `Live` | `Long` | `577.50` | 2,170,000.00 USD | 0.00 USD | 163,840.00 USD | `-19.61%` | `283,700,000,000.00` |
| `Live` | `Long` | `578.50` | 2,000,000.00 USD | 0.00 USD | 7,640.00 USD | `-19.47%` | `13,202,000,000.00` |
| `Live` | `Long` | `580.50` | 1,990,000.00 USD | 0.00 USD | 35,850.00 USD | `-19.20%` | `61,765,000,000.00` |
| `Live` | `Long` | `581.50` | 1,960,000.00 USD | 0.00 USD | 580.34 USD | `-19.06%` | `998,000,000.00` |
| `Live` | `Long` | `582.50` | 1,960,000.00 USD | 0.00 USD | 1,540.00 USD | `-18.92%` | `2,646,000,000.00` |
| `Live` | `Long` | `583.50` | 1,960,000.00 USD | 0.00 USD | 3,470.00 USD | `-18.78%` | `5,952,000,000.00` |
| `Live` | `Long` | `585.50` | 1,950,000.00 USD | 0.00 USD | 210.19 USD | `-18.50%` | `359,000,000.00` |
| `Live` | `Long` | `586.50` | 1,950,000.00 USD | 0.00 USD | 2,360.00 USD | `-18.36%` | `4,022,000,000.00` |
| `Live` | `Long` | `587.50` | 1,950,000.00 USD | 0.00 USD | 5,340.00 USD | `-18.22%` | `9,096,000,000.00` |
| `Live` | `Long` | `588.50` | 1,950,000.00 USD | 0.00 USD | 397.24 USD | `-18.08%` | `675,000,000.00` |
| `Live` | `Long` | `589.50` | 1,940,000.00 USD | 0.00 USD | 10,820.00 USD | `-17.94%` | `18,352,000,000.00` |
| `Live` | `Long` | `590.50` | 1,930,000.00 USD | 0.00 USD | 2,560.00 USD | `-17.80%` | `4,334,000,000.00` |
| `Live` | `Long` | `591.50` | 1,930,000.00 USD | 0.00 USD | 619.30 USD | `-17.66%` | `1,047,000,000.00` |
| `Live` | `Long` | `592.50` | 1,930,000.00 USD | 0.00 USD | 840.76 USD | `-17.53%` | `1,419,000,000.00` |
| `Live` | `Long` | `593.50` | 1,930,000.00 USD | 0.00 USD | 36,050.00 USD | `-17.39%` | `60,735,000,000.00` |
| `Live` | `Long` | `594.50` | 1,890,000.00 USD | 0.00 USD | 8,860.00 USD | `-17.25%` | `14,906,000,000.00` |
| `Live` | `Long` | `595.50` | 1,880,000.00 USD | 0.00 USD | 3,000.00 USD | `-17.11%` | `5,043,000,000.00` |
| `Live` | `Long` | `596.50` | 1,880,000.00 USD | 0.00 USD | 8,910.00 USD | `-16.97%` | `14,934,000,000.00` |
| `Live` | `Long` | `597.50` | 1,870,000.00 USD | 0.00 USD | 2,390.00 USD | `-16.83%` | `3,998,000,000.00` |
| `Live` | `Long` | `598.50` | 1,870,000.00 USD | 0.00 USD | 1,100.00 USD | `-16.69%` | `1,832,000,000.00` |
| `Live` | `Long` | `600.50` | 1,870,000.00 USD | 0.00 USD | 945.19 USD | `-16.41%` | `1,574,000,000.00` |
| `Live` | `Long` | `601.50` | 1,870,000.00 USD | 0.00 USD | 16,880.00 USD | `-16.27%` | `28,061,000,000.00` |
| `Live` | `Long` | `602.50` | 1,850,000.00 USD | 0.00 USD | 418.13 USD | `-16.13%` | `694,000,000.00` |
| `Live` | `Long` | `603.50` | 1,850,000.00 USD | 0.00 USD | 2,160.00 USD | `-15.99%` | `3,579,000,000.00` |
| `Live` | `Long` | `605.50` | 1,850,000.00 USD | 0.00 USD | 17,970.00 USD | `-15.72%` | `29,675,000,000.00` |
| `Live` | `Long` | `606.50` | 1,830,000.00 USD | 0.00 USD | 1,880.00 USD | `-15.58%` | `3,092,000,000.00` |
| `Live` | `Long` | `607.50` | 1,830,000.00 USD | 0.00 USD | 58,610.00 USD | `-15.44%` | `96,477,000,000.00` |
| `Live` | `Long` | `608.50` | 1,770,000.00 USD | 0.00 USD | 4,260.00 USD | `-15.30%` | `7,002,000,000.00` |
| `Live` | `Long` | `609.50` | 1,770,000.00 USD | 0.00 USD | 213.32 USD | `-15.16%` | `350,000,000.00` |
| `Live` | `Long` | `611.50` | 1,770,000.00 USD | 0.00 USD | 1,580.00 USD | `-14.88%` | `2,584,000,000.00` |
| `Live` | `Long` | `612.50` | 1,760,000.00 USD | 0.00 USD | 12,250.00 USD | `-14.74%` | `20,000,000,000.00` |
| `Live` | `Long` | `613.50` | 1,750,000.00 USD | 0.00 USD | 120.25 USD | `-14.60%` | `196,000,000.00` |
| `Live` | `Long` | `614.50` | 1,750,000.00 USD | 0.00 USD | 4,280.00 USD | `-14.46%` | `6,973,000,000.00` |
| `Live` | `Long` | `616.50` | 1,750,000.00 USD | 0.00 USD | 1,540.00 USD | `-14.18%` | `2,500,000,000.00` |
| `Live` | `Long` | `617.50` | 1,750,000.00 USD | 0.00 USD | 156.23 USD | `-14.05%` | `253,000,000.00` |
| `Live` | `Long` | `618.50` | 1,750,000.00 USD | 0.00 USD | 932.70 USD | `-13.91%` | `1,508,000,000.00` |
| `Live` | `Long` | `619.50` | 1,750,000.00 USD | 0.00 USD | 1,410.00 USD | `-13.77%` | `2,279,000,000.00` |
| `Live` | `Long` | `620.50` | 1,740,000.00 USD | 0.00 USD | 6,520.00 USD | `-13.63%` | `10,506,000,000.00` |
| `Live` | `Long` | `621.50` | 1,740,000.00 USD | 0.00 USD | 13,930.00 USD | `-13.49%` | `22,412,000,000.00` |
| `Live` | `Long` | `624.50` | 1,720,000.00 USD | 0.00 USD | 3,690.00 USD | `-13.07%` | `5,905,000,000.00` |
| `Live` | `Long` | `625.50` | 1,720,000.00 USD | 0.00 USD | 14,200.00 USD | `-12.93%` | `22,702,000,000.00` |
| `Live` | `Long` | `626.50` | 1,710,000.00 USD | 0.00 USD | 964.81 USD | `-12.79%` | `1,540,000,000.00` |
| `Live` | `Long` | `630.50` | 1,700,000.00 USD | 0.00 USD | 9,600.00 USD | `-12.24%` | `15,225,000,000.00` |
| `Live` | `Long` | `631.50` | 1,700,000.00 USD | 0.00 USD | 2,900.00 USD | `-12.10%` | `4,587,000,000.00` |
| `Live` | `Long` | `632.50` | 1,690,000.00 USD | 0.00 USD | 3,560.00 USD | `-11.96%` | `5,633,000,000.00` |
| `Live` | `Long` | `634.50` | 1,690,000.00 USD | 0.00 USD | 6,660.00 USD | `-11.68%` | `10,489,000,000.00` |
| `Live` | `Long` | `635.50` | 1,680,000.00 USD | 0.00 USD | 155.06 USD | `-11.54%` | `244,000,000.00` |
| `Live` | `Long` | `636.50` | 1,680,000.00 USD | 0.00 USD | 1,110.00 USD | `-11.40%` | `1,743,000,000.00` |
| `Live` | `Long` | `637.50` | 1,680,000.00 USD | 0.00 USD | 305.36 USD | `-11.26%` | `479,000,000.00` |
| `Live` | `Long` | `638.50` | 1,680,000.00 USD | 0.00 USD | 6,710.00 USD | `-11.12%` | `10,515,000,000.00` |
| `Live` | `Long` | `639.50` | 1,670,000.00 USD | 0.00 USD | 3,490.00 USD | `-10.98%` | `5,458,000,000.00` |
| `Live` | `Long` | `640.50` | 1,670,000.00 USD | 0.00 USD | 1,320,000.00 USD | `-10.84%` | `2,059,440,000,000.00` |
| `Live` | `Long` | `642.50` | 351,060.00 USD | 0.00 USD | 8,480.00 USD | `-10.57%` | `13,199,000,000.00` |
| `Live` | `Long` | `645.50` | 342,580.00 USD | 0.00 USD | 340.18 USD | `-10.15%` | `527,000,000.00` |
| `Live` | `Long` | `646.50` | 342,240.00 USD | 0.00 USD | 463.54 USD | `-10.01%` | `717,000,000.00` |
| `Live` | `Long` | `648.50` | 341,770.00 USD | 0.00 USD | 1,940.00 USD | `-9.73%` | `2,988,000,000.00` |
| `Live` | `Long` | `649.50` | 339,840.00 USD | 0.00 USD | 1,620.00 USD | `-9.59%` | `2,501,000,000.00` |
| `Live` | `Long` | `650.50` | 338,210.00 USD | 0.00 USD | 1,760.00 USD | `-9.45%` | `2,703,000,000.00` |
| `Live` | `Long` | `651.50` | 336,450.00 USD | 0.00 USD | 9,650.00 USD | `-9.31%` | `14,806,000,000.00` |
| `Live` | `Long` | `652.50` | 326,810.00 USD | 0.00 USD | 652.50 USD | `-9.17%` | `1,000,000,000.00` |
| `Live` | `Long` | `653.50` | 326,150.00 USD | 0.00 USD | 97,380.00 USD | `-9.03%` | `149,014,000,000.00` |
| `Live` | `Long` | `654.50` | 228,770.00 USD | 0.00 USD | 437.21 USD | `-8.89%` | `668,000,000.00` |
| `Live` | `Long` | `655.50` | 228,340.00 USD | 0.00 USD | 437.87 USD | `-8.76%` | `668,000,000.00` |
| `Live` | `Long` | `658.50` | 227,900.00 USD | 0.00 USD | 15,090.00 USD | `-8.34%` | `22,916,000,000.00` |
| `Live` | `Long` | `659.50` | 212,810.00 USD | 0.00 USD | 46,450.00 USD | `-8.20%` | `70,433,000,000.00` |
| `Live` | `Long` | `660.50` | 166,360.00 USD | 0.00 USD | 3,410.00 USD | `-8.06%` | `5,167,000,000.00` |
| `Live` | `Long` | `661.50` | 162,940.00 USD | 0.00 USD | 20,140.00 USD | `-7.92%` | `30,450,000,000.00` |
| `Live` | `Long` | `662.50` | 142,800.00 USD | 0.00 USD | 2,850.00 USD | `-7.78%` | `4,297,000,000.00` |
| `Live` | `Long` | `663.50` | 139,960.00 USD | 0.00 USD | 9,230.00 USD | `-7.64%` | `13,911,000,000.00` |
| `Live` | `Long` | `664.50` | 130,730.00 USD | 0.00 USD | 24,100.00 USD | `-7.50%` | `36,261,000,000.00` |
| `Live` | `Long` | `665.50` | 106,630.00 USD | 0.00 USD | 11,380.00 USD | `-7.36%` | `17,096,000,000.00` |
| `Live` | `Long` | `666.50` | 95,250.00 USD | 0.00 USD | 2,550.00 USD | `-7.22%` | `3,824,000,000.00` |
| `Live` | `Long` | `667.50` | 92,700.00 USD | 0.00 USD | 1,380.00 USD | `-7.09%` | `2,067,000,000.00` |
| `Live` | `Long` | `668.50` | 91,320.00 USD | 0.00 USD | 1,450.00 USD | `-6.95%` | `2,164,000,000.00` |
| `Live` | `Long` | `669.50` | 89,880.00 USD | 0.00 USD | 2,930.00 USD | `-6.81%` | `4,371,000,000.00` |
| `Live` | `Long` | `670.50` | 86,950.00 USD | 0.00 USD | 6,110.00 USD | `-6.67%` | `9,113,000,000.00` |
| `Live` | `Long` | `671.50` | 80,840.00 USD | 0.00 USD | 832.66 USD | `-6.53%` | `1,240,000,000.00` |
| `Live` | `Long` | `672.50` | 80,010.00 USD | 0.00 USD | 7,590.00 USD | `-6.39%` | `11,279,000,000.00` |
| `Live` | `Long` | `673.50` | 72,420.00 USD | 0.00 USD | 41,620.00 USD | `-6.25%` | `61,797,000,000.00` |
| `Live` | `Long` | `674.50` | 30,800.00 USD | 0.00 USD | 4,310.00 USD | `-6.11%` | `6,384,000,000.00` |
| `Live` | `Long` | `675.50` | 26,500.00 USD | 0.00 USD | 9,430.00 USD | `-5.97%` | `13,967,000,000.00` |
| `Live` | `Long` | `676.50` | 17,060.00 USD | 0.00 USD | 1,660.00 USD | `-5.83%` | `2,453,000,000.00` |
| `Live` | `Long` | `677.50` | 15,400.00 USD | 0.00 USD | 674.79 USD | `-5.69%` | `996,000,000.00` |
| `Live` | `Long` | `678.50` | 14,730.00 USD | 0.00 USD | 134.34 USD | `-5.55%` | `198,000,000.00` |
| `Live` | `Long` | `679.50` | 14,590.00 USD | 0.00 USD | 3,100.00 USD | `-5.41%` | `4,569,000,000.00` |
| `Live` | `Long` | `680.50` | 11,490.00 USD | 0.00 USD | 11,490.00 USD | `-5.28%` | `16,883,000,000.00` |
| `Live` | `Short` | `681.50` | 4,790.00 USD | 4,790.00 USD | 0.00 USD | `-5.14%` | `7,026,000,000.00` |
| `Live` | `Short` | `689.50` | 6,650.00 USD | 1,860.00 USD | 0.00 USD | `-4.02%` | `2,694,000,000.00` |
| `Live` | `Short` | `695.50` | 7,020.00 USD | 376.96 USD | 0.00 USD | `-3.19%` | `542,000,000.00` |
| `Live` | `Short` | `720.50` | 7,180.00 USD | 161.39 USD | 0.00 USD | `+0.29%` | `224,000,000.00` |
| `Live` | `Short` | `721.50` | 40,440.00 USD | 33,260.00 USD | 0.00 USD | `+0.43%` | `46,099,000,000.00` |
| `Live` | `Short` | `722.50` | 41,010.00 USD | 566.44 USD | 0.00 USD | `+0.57%` | `784,000,000.00` |
| `Live` | `Short` | `723.50` | 44,570.00 USD | 3,560.00 USD | 0.00 USD | `+0.71%` | `4,914,000,000.00` |
| `Live` | `Short` | `724.50` | 109,060.00 USD | 64,500.00 USD | 0.00 USD | `+0.85%` | `89,021,000,000.00` |
| `Live` | `Short` | `725.50` | 110,980.00 USD | 1,920.00 USD | 0.00 USD | `+0.99%` | `2,643,000,000.00` |
| `Live` | `Short` | `726.50` | 117,830.00 USD | 6,860.00 USD | 0.00 USD | `+1.13%` | `9,436,000,000.00` |
| `Live` | `Short` | `727.50` | 118,870.00 USD | 1,030.00 USD | 0.00 USD | `+1.27%` | `1,418,000,000.00` |
| `Live` | `Short` | `728.50` | 200,900.00 USD | 82,030.00 USD | 0.00 USD | `+1.41%` | `112,608,000,000.00` |
| `Live` | `Short` | `729.50` | 375,930.00 USD | 175,030.00 USD | 0.00 USD | `+1.55%` | `239,931,000,000.00` |
| `Live` | `Short` | `730.50` | 434,830.00 USD | 58,900.00 USD | 0.00 USD | `+1.68%` | `80,633,000,000.00` |
| `Live` | `Short` | `731.50` | 442,170.00 USD | 7,340.00 USD | 0.00 USD | `+1.82%` | `10,036,000,000.00` |
| `Live` | `Short` | `732.50` | 579,090.00 USD | 136,920.00 USD | 0.00 USD | `+1.96%` | `186,920,000,000.00` |
| `Live` | `Short` | `733.50` | 607,670.00 USD | 28,570.00 USD | 0.00 USD | `+2.10%` | `38,954,000,000.00` |
| `Live` | `Short` | `734.50` | 760,140.00 USD | 152,470.00 USD | 0.00 USD | `+2.24%` | `207,590,000,000.00` |
| `Live` | `Short` | `735.50` | 783,130.00 USD | 22,990.00 USD | 0.00 USD | `+2.38%` | `31,262,000,000.00` |
| `Live` | `Short` | `736.50` | 795,300.00 USD | 12,170.00 USD | 0.00 USD | `+2.52%` | `16,520,000,000.00` |
| `Live` | `Short` | `737.50` | 799,360.00 USD | 4,060.00 USD | 0.00 USD | `+2.66%` | `5,507,000,000.00` |
| `Live` | `Short` | `738.50` | 805,570.00 USD | 6,210.00 USD | 0.00 USD | `+2.80%` | `8,405,000,000.00` |
| `Live` | `Short` | `739.50` | 813,970.00 USD | 8,400.00 USD | 0.00 USD | `+2.94%` | `11,363,000,000.00` |
| `Live` | `Short` | `740.50` | 817,950.00 USD | 3,980.00 USD | 0.00 USD | `+3.08%` | `5,376,000,000.00` |
| `Live` | `Short` | `741.50` | 826,740.00 USD | 8,790.00 USD | 0.00 USD | `+3.22%` | `11,850,000,000.00` |
| `Live` | `Short` | `742.50` | 838,350.00 USD | 11,610.00 USD | 0.00 USD | `+3.35%` | `15,634,000,000.00` |
| `Live` | `Short` | `743.50` | 942,760.00 USD | 104,410.00 USD | 0.00 USD | `+3.49%` | `140,437,000,000.00` |
| `Live` | `Short` | `744.50` | 1,060,000.00 USD | 119,040.00 USD | 0.00 USD | `+3.63%` | `159,893,000,000.00` |
| `Live` | `Short` | `745.50` | 1,130,000.00 USD | 67,820.00 USD | 0.00 USD | `+3.77%` | `90,974,000,000.00` |
| `Live` | `Short` | `746.50` | 1,310,000.00 USD | 182,880.00 USD | 0.00 USD | `+3.91%` | `244,988,000,000.00` |
| `Live` | `Short` | `747.50` | 1,310,000.00 USD | 131.56 USD | 0.00 USD | `+4.05%` | `176,000,000.00` |
| `Live` | `Short` | `748.50` | 1,320,000.00 USD | 2,970.00 USD | 0.00 USD | `+4.19%` | `3,974,000,000.00` |
| `Live` | `Short` | `749.50` | 1,320,000.00 USD | 3,080.00 USD | 0.00 USD | `+4.33%` | `4,103,000,000.00` |
| `Live` | `Short` | `750.50` | 1,340,000.00 USD | 19,160.00 USD | 0.00 USD | `+4.47%` | `25,529,000,000.00` |
| `Live` | `Short` | `751.50` | 1,920,000.00 USD | 579,320.00 USD | 0.00 USD | `+4.61%` | `770,883,000,000.00` |
| `Live` | `Short` | `752.50` | 1,960,000.00 USD | 47,580.00 USD | 0.00 USD | `+4.75%` | `63,225,000,000.00` |
| `Live` | `Short` | `754.50` | 2,830,000.00 USD | 862,640.00 USD | 0.00 USD | `+5.03%` | `1,143,331,000,000.00` |
| `Live` | `Short` | `756.50` | 2,830,000.00 USD | 3,750.00 USD | 0.00 USD | `+5.30%` | `4,960,000,000.00` |
| `Live` | `Short` | `758.50` | 2,860,000.00 USD | 27,490.00 USD | 0.00 USD | `+5.58%` | `36,246,000,000.00` |
| `Live` | `Short` | `759.50` | 2,860,000.00 USD | 704.82 USD | 0.00 USD | `+5.72%` | `928,000,000.00` |
| `Live` | `Short` | `760.50` | 2,950,000.00 USD | 94,660.00 USD | 0.00 USD | `+5.86%` | `124,473,000,000.00` |
| `Live` | `Short` | `762.50` | 2,950,000.00 USD | 367.52 USD | 0.00 USD | `+6.14%` | `482,000,000.00` |
| `Live` | `Short` | `763.50` | 3,400,000.00 USD | 445,300.00 USD | 0.00 USD | `+6.28%` | `583,234,000,000.00` |
| `Live` | `Short` | `764.50` | 3,480,000.00 USD | 76,450.00 USD | 0.00 USD | `+6.42%` | `100,000,000,000.00` |
| `Live` | `Short` | `765.50` | 3,480,000.00 USD | 5,230.00 USD | 0.00 USD | `+6.56%` | `6,828,000,000.00` |
| `Live` | `Short` | `766.50` | 3,480,000.00 USD | 2,850.00 USD | 0.00 USD | `+6.70%` | `3,719,000,000.00` |
| `Live` | `Short` | `768.50` | 3,480,000.00 USD | 156.77 USD | 0.00 USD | `+6.97%` | `204,000,000.00` |
| `Live` | `Short` | `769.50` | 3,480,000.00 USD | 280.87 USD | 0.00 USD | `+7.11%` | `365,000,000.00` |
| `Live` | `Short` | `770.50` | 3,490,000.00 USD | 881.45 USD | 0.00 USD | `+7.25%` | `1,144,000,000.00` |
| `Live` | `Short` | `771.50` | 3,500,000.00 USD | 10,380.00 USD | 0.00 USD | `+7.39%` | `13,458,000,000.00` |
| `Live` | `Short` | `772.50` | 3,500,000.00 USD | 4,210.00 USD | 0.00 USD | `+7.53%` | `5,456,000,000.00` |
| `Live` | `Short` | `773.50` | 3,510,000.00 USD | 8,230.00 USD | 0.00 USD | `+7.67%` | `10,646,000,000.00` |
| `Live` | `Short` | `774.50` | 3,520,000.00 USD | 12,580.00 USD | 0.00 USD | `+7.81%` | `16,247,000,000.00` |
| `Live` | `Short` | `776.50` | 3,620,000.00 USD | 97,260.00 USD | 0.00 USD | `+8.09%` | `125,252,000,000.00` |
| `Live` | `Short` | `777.50` | 3,620,000.00 USD | 209.15 USD | 0.00 USD | `+8.23%` | `269,000,000.00` |
| `Live` | `Short` | `778.50` | 3,620,000.00 USD | 3,200.00 USD | 0.00 USD | `+8.37%` | `4,107,000,000.00` |
| `Live` | `Short` | `779.50` | 3,620,000.00 USD | 2,490.00 USD | 0.00 USD | `+8.51%` | `3,190,000,000.00` |
| `Live` | `Short` | `780.50` | 3,630,000.00 USD | 5,240.00 USD | 0.00 USD | `+8.64%` | `6,714,000,000.00` |
| `Live` | `Short` | `781.50` | 3,630,000.00 USD | 1,600.00 USD | 0.00 USD | `+8.78%` | `2,045,000,000.00` |
| `Live` | `Short` | `785.50` | 3,630,000.00 USD | 758.01 USD | 0.00 USD | `+9.34%` | `965,000,000.00` |
| `Live` | `Short` | `786.50` | 3,760,000.00 USD | 127,660.00 USD | 0.00 USD | `+9.48%` | `162,308,000,000.00` |
| `Live` | `Short` | `787.50` | 3,760,000.00 USD | 3,150.00 USD | 0.00 USD | `+9.62%` | `4,000,000,000.00` |
| `Live` | `Short` | `788.50` | 3,760,000.00 USD | 1,580.00 USD | 0.00 USD | `+9.76%` | `2,000,000,000.00` |
| `Live` | `Short` | `789.50` | 3,770,000.00 USD | 1,250.00 USD | 0.00 USD | `+9.90%` | `1,580,000,000.00` |
| `Live` | `Short` | `793.50` | 3,770,000.00 USD | 1,280.00 USD | 0.00 USD | `+10.45%` | `1,616,000,000.00` |
| `Live` | `Short` | `794.50` | 3,770,000.00 USD | 7,090.00 USD | 0.00 USD | `+10.59%` | `8,926,000,000.00` |
| `Live` | `Short` | `795.50` | 3,780,000.00 USD | 2,930.00 USD | 0.00 USD | `+10.73%` | `3,681,000,000.00` |
| `Live` | `Short` | `796.50` | 3,780,000.00 USD | 3,240.00 USD | 0.00 USD | `+10.87%` | `4,062,000,000.00` |
| `Live` | `Short` | `797.50` | 3,780,000.00 USD | 1,090.00 USD | 0.00 USD | `+11.01%` | `1,367,000,000.00` |
| `Live` | `Short` | `798.50` | 3,790,000.00 USD | 4,140.00 USD | 0.00 USD | `+11.15%` | `5,181,000,000.00` |
| `Live` | `Short` | `799.50` | 3,790,000.00 USD | 610.02 USD | 0.00 USD | `+11.29%` | `763,000,000.00` |
| `Live` | `Short` | `800.50` | 3,790,000.00 USD | 379.44 USD | 0.00 USD | `+11.43%` | `474,000,000.00` |
| `Live` | `Short` | `801.50` | 3,790,000.00 USD | 3,680.00 USD | 0.00 USD | `+11.57%` | `4,594,000,000.00` |
| `Live` | `Short` | `802.50` | 4,570,000.00 USD | 778,380.00 USD | 0.00 USD | `+11.71%` | `969,946,000,000.00` |
| `Live` | `Short` | `803.50` | 4,570,000.00 USD | 4,560.00 USD | 0.00 USD | `+11.85%` | `5,679,000,000.00` |
| `Live` | `Short` | `804.50` | 4,570,000.00 USD | 105.39 USD | 0.00 USD | `+11.98%` | `131,000,000.00` |
| `Live` | `Short` | `805.50` | 4,620,000.00 USD | 47,420.00 USD | 0.00 USD | `+12.12%` | `58,872,000,000.00` |
| `Live` | `Short` | `806.50` | 4,620,000.00 USD | 2,890.00 USD | 0.00 USD | `+12.26%` | `3,580,000,000.00` |
| `Live` | `Short` | `807.50` | 4,620,000.00 USD | 738.06 USD | 0.00 USD | `+12.40%` | `914,000,000.00` |
| `Live` | `Short` | `808.50` | 4,640,000.00 USD | 12,200.00 USD | 0.00 USD | `+12.54%` | `15,090,000,000.00` |
| `Live` | `Short` | `809.50` | 4,640,000.00 USD | 342.42 USD | 0.00 USD | `+12.68%` | `423,000,000.00` |
| `Live` | `Short` | `812.50` | 4,640,000.00 USD | 434.69 USD | 0.00 USD | `+13.10%` | `535,000,000.00` |
| `Live` | `Short` | `814.50` | 4,640,000.00 USD | 692.32 USD | 0.00 USD | `+13.38%` | `850,000,000.00` |
| `Live` | `Short` | `815.50` | 4,640,000.00 USD | 6,020.00 USD | 0.00 USD | `+13.52%` | `7,383,000,000.00` |
| `Live` | `Short` | `816.50` | 4,660,000.00 USD | 15,410.00 USD | 0.00 USD | `+13.66%` | `18,879,000,000.00` |
| `Live` | `Short` | `817.50` | 4,660,000.00 USD | 325.37 USD | 0.00 USD | `+13.79%` | `398,000,000.00` |
| `Live` | `Short` | `820.50` | 4,670,000.00 USD | 8,340.00 USD | 0.00 USD | `+14.21%` | `10,166,000,000.00` |
| `Live` | `Short` | `821.50` | 4,680,000.00 USD | 11,710.00 USD | 0.00 USD | `+14.35%` | `14,252,000,000.00` |
| `Live` | `Short` | `822.50` | 4,680,000.00 USD | 3,540.00 USD | 0.00 USD | `+14.49%` | `4,302,000,000.00` |
| `Live` | `Short` | `824.50` | 4,930,000.00 USD | 247,350.00 USD | 0.00 USD | `+14.77%` | `300,000,000,000.00` |
| `Live` | `Short` | `826.50` | 4,940,000.00 USD | 7,510.00 USD | 0.00 USD | `+15.05%` | `9,084,000,000.00` |
| `Live` | `Short` | `827.50` | 5,420,000.00 USD | 480,240.00 USD | 0.00 USD | `+15.19%` | `580,352,000,000.00` |
| `Live` | `Short` | `828.50` | 5,420,000.00 USD | 2,230.00 USD | 0.00 USD | `+15.33%` | `2,689,000,000.00` |
| `Live` | `Short` | `830.50` | 5,500,000.00 USD | 81,970.00 USD | 0.00 USD | `+15.60%` | `98,695,000,000.00` |
| `Live` | `Short` | `834.50` | 5,500,000.00 USD | 1,010.00 USD | 0.00 USD | `+16.16%` | `1,206,000,000.00` |
| `Live` | `Short` | `836.50` | 5,580,000.00 USD | 79,430.00 USD | 0.00 USD | `+16.44%` | `94,960,000,000.00` |
| `Live` | `Short` | `837.50` | 5,590,000.00 USD | 11,450.00 USD | 0.00 USD | `+16.58%` | `13,676,000,000.00` |
| `Live` | `Short` | `838.50` | 5,620,000.00 USD | 21,840.00 USD | 0.00 USD | `+16.72%` | `26,046,000,000.00` |
| `Live` | `Short` | `841.50` | 5,620,000.00 USD | 2,830.00 USD | 0.00 USD | `+17.14%` | `3,364,000,000.00` |
| `Live` | `Short` | `842.50` | 5,620,000.00 USD | 1,750.00 USD | 0.00 USD | `+17.27%` | `2,074,000,000.00` |
| `Live` | `Short` | `843.50` | 5,620,000.00 USD | 1,380.00 USD | 0.00 USD | `+17.41%` | `1,641,000,000.00` |
| `Live` | `Short` | `844.50` | 5,630,000.00 USD | 9,490.00 USD | 0.00 USD | `+17.55%` | `11,241,000,000.00` |
| `Live` | `Short` | `848.50` | 5,640,000.00 USD | 11,080.00 USD | 0.00 USD | `+18.11%` | `13,064,000,000.00` |
| `Live` | `Short` | `850.50` | 5,680,000.00 USD | 34,450.00 USD | 0.00 USD | `+18.39%` | `40,506,000,000.00` |
| `Live` | `Short` | `853.50` | 5,680,000.00 USD | 5,020.00 USD | 0.00 USD | `+18.81%` | `5,884,000,000.00` |
| `Live` | `Short` | `858.50` | 6,210,000.00 USD | 523,680.00 USD | 0.00 USD | `+19.50%` | `610,000,000,000.00` |
| `Live` | `Short` | `859.50` | 6,220,000.00 USD | 16,380.00 USD | 0.00 USD | `+19.64%` | `19,059,000,000.00` |
| `Live` | `Short` | `865.50` | 6,240,000.00 USD | 18,900.00 USD | 0.00 USD | `+20.48%` | `21,832,000,000.00` |
| `Live` | `Short` | `870.50` | 6,250,000.00 USD | 6,090.00 USD | 0.00 USD | `+21.17%` | `7,000,000,000.00` |
| `Live` | `Short` | `872.50` | 6,540,000.00 USD | 292,330.00 USD | 0.00 USD | `+21.45%` | `335,051,000,000.00` |
| `Live` | `Short` | `877.50` | 7,150,000.00 USD | 614,250.00 USD | 0.00 USD | `+22.15%` | `700,000,000,000.00` |
| `Live` | `Short` | `878.50` | 7,250,000.00 USD | 92,600.00 USD | 0.00 USD | `+22.29%` | `105,403,000,000.00` |
| `Live` | `Short` | `880.50` | 7,250,000.00 USD | 663.02 USD | 0.00 USD | `+22.56%` | `753,000,000.00` |
| `Live` | `Short` | `881.50` | 7,250,000.00 USD | 505.10 USD | 0.00 USD | `+22.70%` | `573,000,000.00` |
| `Live` | `Short` | `883.50` | 7,260,000.00 USD | 14,130.00 USD | 0.00 USD | `+22.98%` | `15,992,000,000.00` |
| `Live` | `Short` | `885.50` | 7,260,000.00 USD | 1,770.00 USD | 0.00 USD | `+23.26%` | `2,000,000,000.00` |
| `Live` | `Short` | `886.50` | 7,260,000.00 USD | 812.92 USD | 0.00 USD | `+23.40%` | `917,000,000.00` |
| `Live` | `Short` | `887.50` | 7,260,000.00 USD | 385.18 USD | 0.00 USD | `+23.54%` | `434,000,000.00` |
| `Live` | `Short` | `891.50` | 7,270,000.00 USD | 3,950.00 USD | 0.00 USD | `+24.10%` | `4,429,000,000.00` |
| `Live` | `Short` | `893.50` | 7,270,000.00 USD | 173.34 USD | 0.00 USD | `+24.37%` | `194,000,000.00` |
| `Live` | `Short` | `894.50` | 7,300,000.00 USD | 26,840.00 USD | 0.00 USD | `+24.51%` | `30,000,000,000.00` |
| `Live` | `Short` | `896.50` | 7,520,000.00 USD | 224,120.00 USD | 0.00 USD | `+24.79%` | `250,000,000,000.00` |
| `Live` | `Short` | `897.50` | 7,560,000.00 USD | 36,720.00 USD | 0.00 USD | `+24.93%` | `40,909,000,000.00` |
| `Live` | `Short` | `898.50` | 7,820,000.00 USD | 259,570.00 USD | 0.00 USD | `+25.07%` | `288,891,000,000.00` |
| `Live` | `Short` | `900.50` | 7,910,000.00 USD | 90,050.00 USD | 0.00 USD | `+25.35%` | `100,000,000,000.00` |
| `Live` | `Short` | `902.50` | 7,910,000.00 USD | 305.05 USD | 0.00 USD | `+25.63%` | `338,000,000.00` |
| `Live` | `Short` | `904.50` | 7,970,000.00 USD | 63,930.00 USD | 0.00 USD | `+25.90%` | `70,678,000,000.00` |
| `Live` | `Short` | `906.50` | 7,970,000.00 USD | 2,130.00 USD | 0.00 USD | `+26.18%` | `2,346,000,000.00` |
| `Live` | `Short` | `908.50` | 7,970,000.00 USD | 901.23 USD | 0.00 USD | `+26.46%` | `992,000,000.00` |
| `Live` | `Short` | `909.50` | 7,970,000.00 USD | 890.40 USD | 0.00 USD | `+26.60%` | `979,000,000.00` |
| `Live` | `Short` | `910.50` | 7,980,000.00 USD | 2,630.00 USD | 0.00 USD | `+26.74%` | `2,884,000,000.00` |
| `Live` | `Short` | `911.50` | 8,010,000.00 USD | 34,670.00 USD | 0.00 USD | `+26.88%` | `38,036,000,000.00` |
| `Live` | `Short` | `912.50` | 8,010,000.00 USD | 388.72 USD | 0.00 USD | `+27.02%` | `426,000,000.00` |
| `Live` | `Short` | `913.50` | 8,010,000.00 USD | 116.93 USD | 0.00 USD | `+27.16%` | `128,000,000.00` |
| `Live` | `Short` | `917.50` | 8,010,000.00 USD | 989.98 USD | 0.00 USD | `+27.71%` | `1,079,000,000.00` |
| `Live` | `Short` | `918.50` | 8,150,000.00 USD | 132,360.00 USD | 0.00 USD | `+27.85%` | `144,104,000,000.00` |
| `Live` | `Short` | `922.50` | 8,180,000.00 USD | 30,320.00 USD | 0.00 USD | `+28.41%` | `32,872,000,000.00` |
| `Live` | `Short` | `925.50` | 8,180,000.00 USD | 9,260.00 USD | 0.00 USD | `+28.83%` | `10,000,000,000.00` |
| `Live` | `Short` | `927.50` | 8,640,000.00 USD | 455,520.00 USD | 0.00 USD | `+29.11%` | `491,124,000,000.00` |
| `Live` | `Short` | `931.50` | 8,650,000.00 USD | 14,200.00 USD | 0.00 USD | `+29.66%` | `15,247,000,000.00` |
| `Live` | `Short` | `932.50` | 8,660,000.00 USD | 3,120.00 USD | 0.00 USD | `+29.80%` | `3,344,000,000.00` |
| `Live` | `Short` | `934.50` | 8,660,000.00 USD | 656.02 USD | 0.00 USD | `+30.08%` | `702,000,000.00` |
| `Live` | `Short` | `935.50` | 8,720,000.00 USD | 65,480.00 USD | 0.00 USD | `+30.22%` | `70,000,000,000.00` |
| `Live` | `Short` | `936.50` | 8,720,000.00 USD | 1,240.00 USD | 0.00 USD | `+30.36%` | `1,321,000,000.00` |
| `Live` | `Short` | `942.50` | 8,780,000.00 USD | 57,880.00 USD | 0.00 USD | `+31.19%` | `61,406,000,000.00` |
| `Live` | `Short` | `947.50` | 8,780,000.00 USD | 405.53 USD | 0.00 USD | `+31.89%` | `428,000,000.00` |
| `Live` | `Short` | `948.50` | 8,790,000.00 USD | 2,700.00 USD | 0.00 USD | `+32.03%` | `2,846,000,000.00` |
| `Live` | `Short` | `949.50` | 8,790,000.00 USD | 112.99 USD | 0.00 USD | `+32.17%` | `119,000,000.00` |
| `Live` | `Short` | `951.50` | 8,790,000.00 USD | 397.73 USD | 0.00 USD | `+32.45%` | `418,000,000.00` |
| `Live` | `Short` | `954.50` | 8,790,000.00 USD | 203.31 USD | 0.00 USD | `+32.86%` | `213,000,000.00` |
| `Live` | `Short` | `955.50` | 8,810,000.00 USD | 18,910.00 USD | 0.00 USD | `+33.00%` | `19,788,000,000.00` |
| `Live` | `Short` | `956.50` | 8,820,000.00 USD | 13,400.00 USD | 0.00 USD | `+33.14%` | `14,008,000,000.00` |
| `Live` | `Short` | `965.50` | 8,830,000.00 USD | 6,950.00 USD | 0.00 USD | `+34.40%` | `7,199,000,000.00` |
| `Live` | `Short` | `969.50` | 9,680,000.00 USD | 851,180.00 USD | 0.00 USD | `+34.95%` | `877,960,000,000.00` |
| `Live` | `Short` | `970.50` | 9,680,000.00 USD | 1,390.00 USD | 0.00 USD | `+35.09%` | `1,434,000,000.00` |
| `Live` | `Short` | `979.50` | 9,680,000.00 USD | 228.22 USD | 0.00 USD | `+36.34%` | `233,000,000.00` |
| `Live` | `Short` | `980.50` | 9,690,000.00 USD | 14,260.00 USD | 0.00 USD | `+36.48%` | `14,541,000,000.00` |
| `Live` | `Short` | `981.50` | 9,710,000.00 USD | 15,940.00 USD | 0.00 USD | `+36.62%` | `16,240,000,000.00` |
| `Live` | `Short` | `986.50` | 9,710,000.00 USD | 1,100.00 USD | 0.00 USD | `+37.32%` | `1,112,000,000.00` |
| `Live` | `Short` | `990.50` | 9,740,000.00 USD | 28,300.00 USD | 0.00 USD | `+37.88%` | `28,570,000,000.00` |
| `Live` | `Short` | `992.50` | 9,840,000.00 USD | 101,390.00 USD | 0.00 USD | `+38.15%` | `102,152,000,000.00` |
| `Live` | `Short` | `993.50` | 9,840,000.00 USD | 975.62 USD | 0.00 USD | `+38.29%` | `982,000,000.00` |
| `Live` | `Short` | `994.50` | 10,130,000.00 USD | 285,520.00 USD | 0.00 USD | `+38.43%` | `287,098,000,000.00` |
| `Live` | `Short` | `995.50` | 10,130,000.00 USD | 313.58 USD | 0.00 USD | `+38.57%` | `315,000,000.00` |
| `Live` | `Short` | `996.50` | 10,130,000.00 USD | 989.52 USD | 0.00 USD | `+38.71%` | `993,000,000.00` |
| `Live` | `Short` | `997.50` | 10,130,000.00 USD | 7,300.00 USD | 0.00 USD | `+38.85%` | `7,316,000,000.00` |
| `Live` | `Short` | `998.50` | 10,140,000.00 USD | 9,550.00 USD | 0.00 USD | `+38.99%` | `9,569,000,000.00` |
| `Live` | `Short` | `999.50` | 10,180,000.00 USD | 36,850.00 USD | 0.00 USD | `+39.13%` | `36,870,000,000.00` |
| `Live` | `Short` | `1003.50` | 10,180,000.00 USD | 838.93 USD | 0.00 USD | `+39.69%` | `836,000,000.00` |
| `Live` | `Short` | `1005.50` | 10,190,000.00 USD | 4,050.00 USD | 0.00 USD | `+39.96%` | `4,024,000,000.00` |
| `Live` | `Short` | `1008.50` | 10,210,000.00 USD | 28,800.00 USD | 0.00 USD | `+40.38%` | `28,558,000,000.00` |
| `Live` | `Short` | `1009.50` | 10,270,000.00 USD | 60,010.00 USD | 0.00 USD | `+40.52%` | `59,446,000,000.00` |
| `Live` | `Short` | `1018.50` | 10,570,000.00 USD | 296,960.00 USD | 0.00 USD | `+41.77%` | `291,563,000,000.00` |
| `Live` | `Short` | `1024.50` | 10,570,000.00 USD | 2,850.00 USD | 0.00 USD | `+42.61%` | `2,777,000,000.00` |
| `Live` | `Short` | `1025.50` | 10,570,000.00 USD | 126.14 USD | 0.00 USD | `+42.75%` | `123,000,000.00` |
| `Live` | `Short` | `1030.50` | 10,580,000.00 USD | 496.70 USD | 0.00 USD | `+43.44%` | `482,000,000.00` |
| `Live` | `Short` | `1033.50` | 10,580,000.00 USD | 115.75 USD | 0.00 USD | `+43.86%` | `112,000,000.00` |
| `Live` | `Short` | `1035.50` | 11,300,000.00 USD | 722,380.00 USD | 0.00 USD | `+44.14%` | `697,611,000,000.00` |
| `Live` | `Short` | `1039.50` | 11,330,000.00 USD | 31,180.00 USD | 0.00 USD | `+44.70%` | `30,000,000,000.00` |
| `Live` | `Short` | `1050.50` | 11,330,000.00 USD | 500.04 USD | 0.00 USD | `+46.23%` | `476,000,000.00` |
| `Live` | `Short` | `1056.50` | 11,400,000.00 USD | 66,030.00 USD | 0.00 USD | `+47.06%` | `62,500,000,000.00` |
| `Live` | `Short` | `1064.50` | 11,400,000.00 USD | 1,600.00 USD | 0.00 USD | `+48.18%` | `1,500,000,000.00` |
| `Live` | `Short` | `1065.50` | 11,410,000.00 USD | 15,350.00 USD | 0.00 USD | `+48.32%` | `14,403,000,000.00` |
| `Live` | `Short` | `1073.50` | 11,410,000.00 USD | 1,610.00 USD | 0.00 USD | `+49.43%` | `1,500,000,000.00` |
| `Live` | `Short` | `1077.50` | 11,460,000.00 USD | 44,740.00 USD | 0.00 USD | `+49.99%` | `41,524,000,000.00` |
| `Live` | `Short` | `1087.50` | 11,460,000.00 USD | 5,770.00 USD | 0.00 USD | `+51.38%` | `5,310,000,000.00` |
| `Live` | `Short` | `1088.50` | 11,480,000.00 USD | 15,780.00 USD | 0.00 USD | `+51.52%` | `14,495,000,000.00` |
| `Live` | `Short` | `1092.50` | 11,550,000.00 USD | 69,830.00 USD | 0.00 USD | `+52.07%` | `63,916,000,000.00` |
| `Live` | `Short` | `1093.50` | 11,670,000.00 USD | 120,790.00 USD | 0.00 USD | `+52.21%` | `110,460,000,000.00` |
| `Live` | `Short` | `1095.50` | 11,670,000.00 USD | 809.57 USD | 0.00 USD | `+52.49%` | `739,000,000.00` |
| `Live` | `Short` | `1102.50` | 11,690,000.00 USD | 19,650.00 USD | 0.00 USD | `+53.47%` | `17,826,000,000.00` |
| `Live` | `Short` | `1108.50` | 11,770,000.00 USD | 75,650.00 USD | 0.00 USD | `+54.30%` | `68,249,000,000.00` |
| `Live` | `Short` | `1109.50` | 11,930,000.00 USD | 163,940.00 USD | 0.00 USD | `+54.44%` | `147,759,000,000.00` |
| `Live` | `Short` | `1117.50` | 12,050,000.00 USD | 116,220.00 USD | 0.00 USD | `+55.55%` | `104,000,000,000.00` |
| `Live` | `Short` | `1122.50` | 12,110,000.00 USD | 60,690.00 USD | 0.00 USD | `+56.25%` | `54,065,000,000.00` |
| `Live` | `Short` | `1123.50` | 12,110,000.00 USD | 150.55 USD | 0.00 USD | `+56.39%` | `134,000,000.00` |
| `Live` | `Short` | `1137.50` | 12,450,000.00 USD | 341,250.00 USD | 0.00 USD | `+58.34%` | `300,000,000,000.00` |
| `Live` | `Short` | `1138.50` | 12,450,000.00 USD | 357.49 USD | 0.00 USD | `+58.48%` | `314,000,000.00` |
| `Live` | `Short` | `1140.50` | 12,450,000.00 USD | 1,520.00 USD | 0.00 USD | `+58.76%` | `1,337,000,000.00` |
| `Live` | `Short` | `1153.50` | 12,450,000.00 USD | 154.57 USD | 0.00 USD | `+60.57%` | `134,000,000.00` |
| `Live` | `Short` | `1155.50` | 12,460,000.00 USD | 11,730.00 USD | 0.00 USD | `+60.84%` | `10,154,000,000.00` |
| `Live` | `Short` | `1159.50` | 12,460,000.00 USD | 120.59 USD | 0.00 USD | `+61.40%` | `104,000,000.00` |
| `Live` | `Short` | `1177.50` | 12,460,000.00 USD | 166.03 USD | 0.00 USD | `+63.91%` | `141,000,000.00` |
| `Live` | `Short` | `1178.50` | 12,530,000.00 USD | 66,060.00 USD | 0.00 USD | `+64.05%` | `56,055,000,000.00` |
| `Live` | `Short` | `1180.50` | 12,550,000.00 USD | 20,500.00 USD | 0.00 USD | `+64.32%` | `17,363,000,000.00` |
| `Live` | `Short` | `1182.50` | 12,610,000.00 USD | 57,130.00 USD | 0.00 USD | `+64.60%` | `48,311,000,000.00` |
| `Live` | `Short` | `1197.50` | 12,610,000.00 USD | 463.43 USD | 0.00 USD | `+66.69%` | `387,000,000.00` |
| `Live` | `Short` | `1203.50` | 12,730,000.00 USD | 118,860.00 USD | 0.00 USD | `+67.53%` | `98,764,000,000.00` |
| `Live` | `Short` | `1207.50` | 12,730,000.00 USD | 385.19 USD | 0.00 USD | `+68.08%` | `319,000,000.00` |
| `Live` | `Short` | `1210.50` | 12,840,000.00 USD | 108,940.00 USD | 0.00 USD | `+68.50%` | `90,000,000,000.00` |
| `Live` | `Short` | `1211.50` | 12,870,000.00 USD | 30,270.00 USD | 0.00 USD | `+68.64%` | `24,982,000,000.00` |
| `Live` | `Short` | `1214.50` | 12,910,000.00 USD | 42,510.00 USD | 0.00 USD | `+69.06%` | `35,000,000,000.00` |
| `Live` | `Short` | `1218.50` | 12,910,000.00 USD | 704.29 USD | 0.00 USD | `+69.61%` | `578,000,000.00` |
| `Live` | `Short` | `1224.50` | 12,910,000.00 USD | 1,030.00 USD | 0.00 USD | `+70.45%` | `841,000,000.00` |
| `Live` | `Short` | `1227.50` | 12,910,000.00 USD | 3,730.00 USD | 0.00 USD | `+70.87%` | `3,035,000,000.00` |
| `Live` | `Short` | `1241.50` | 12,940,000.00 USD | 26,600.00 USD | 0.00 USD | `+72.81%` | `21,429,000,000.00` |
| `Live` | `Short` | `1244.50` | 12,950,000.00 USD | 5,170.00 USD | 0.00 USD | `+73.23%` | `4,154,000,000.00` |
| `Live` | `Short` | `1249.50` | 12,950,000.00 USD | 2,050.00 USD | 0.00 USD | `+73.93%` | `1,644,000,000.00` |
| `Live` | `Short` | `1251.50` | 12,950,000.00 USD | 100.12 USD | 0.00 USD | `+74.21%` | `80,000,000.00` |
| `Live` | `Short` | `1259.50` | 12,970,000.00 USD | 24,450.00 USD | 0.00 USD | `+75.32%` | `19,414,000,000.00` |
| `Live` | `Short` | `1261.50` | 13,090,000.00 USD | 113,750.00 USD | 0.00 USD | `+75.60%` | `90,173,000,000.00` |
| `Live` | `Short` | `1275.50` | 13,120,000.00 USD | 38,530.00 USD | 0.00 USD | `+77.55%` | `30,209,000,000.00` |
| `Live` | `Short` | `1276.50` | 13,130,000.00 USD | 6,920.00 USD | 0.00 USD | `+77.69%` | `5,419,000,000.00` |
| `Live` | `Short` | `1281.50` | 13,260,000.00 USD | 128,150.00 USD | 0.00 USD | `+78.38%` | `100,000,000,000.00` |
| `Live` | `Short` | `1282.50` | 13,260,000.00 USD | 2,740.00 USD | 0.00 USD | `+78.52%` | `2,134,000,000.00` |
| `Live` | `Short` | `1283.50` | 13,330,000.00 USD | 63,050.00 USD | 0.00 USD | `+78.66%` | `49,123,000,000.00` |
| `Live` | `Short` | `1285.50` | 13,330,000.00 USD | 348.37 USD | 0.00 USD | `+78.94%` | `271,000,000.00` |
| `Live` | `Short` | `1286.50` | 13,350,000.00 USD | 19,220.00 USD | 0.00 USD | `+79.08%` | `14,939,000,000.00` |
| `Live` | `Short` | `1289.50` | 13,350,000.00 USD | 3,990.00 USD | 0.00 USD | `+79.50%` | `3,092,000,000.00` |
| `Live` | `Short` | `1291.50` | 15,170,000.00 USD | 1,820,000.00 USD | 0.00 USD | `+79.77%` | `1,412,868,000,000.00` |
| `Live` | `Short` | `1295.50` | 15,170,000.00 USD | 181.37 USD | 0.00 USD | `+80.33%` | `140,000,000.00` |
| `Live` | `Short` | `1298.50` | 15,280,000.00 USD | 110,770.00 USD | 0.00 USD | `+80.75%` | `85,305,000,000.00` |
| `Live` | `Short` | `1310.50` | 15,450,000.00 USD | 166,280.00 USD | 0.00 USD | `+82.42%` | `126,881,000,000.00` |
| `Live` | `Short` | `1316.50` | 15,460,000.00 USD | 7,580.00 USD | 0.00 USD | `+83.25%` | `5,758,000,000.00` |
| `Live` | `Short` | `1319.50` | 15,470,000.00 USD | 14,130.00 USD | 0.00 USD | `+83.67%` | `10,710,000,000.00` |
| `Live` | `Short` | `1323.50` | 15,520,000.00 USD | 51,510.00 USD | 0.00 USD | `+84.23%` | `38,923,000,000.00` |
| `Live` | `Short` | `1327.50` | 15,520,000.00 USD | 138.06 USD | 0.00 USD | `+84.79%` | `104,000,000.00` |
| `Live` | `Short` | `1328.50` | 15,520,000.00 USD | 289.61 USD | 0.00 USD | `+84.92%` | `218,000,000.00` |
| `Live` | `Short` | `1330.50` | 15,550,000.00 USD | 23,470.00 USD | 0.00 USD | `+85.20%` | `17,640,000,000.00` |
| `Live` | `Short` | `1352.50` | 15,550,000.00 USD | 347.59 USD | 0.00 USD | `+88.27%` | `257,000,000.00` |
| `Live` | `Short` | `1358.50` | 17,310,000.00 USD | 1,770,000.00 USD | 0.00 USD | `+89.10%` | `1,299,244,000,000.00` |
| `Live` | `Short` | `1359.50` | 17,340,000.00 USD | 31,270.00 USD | 0.00 USD | `+89.24%` | `23,000,000,000.00` |
| `Live` | `Short` | `1365.50` | 17,440,000.00 USD | 92,850.00 USD | 0.00 USD | `+90.08%` | `68,000,000,000.00` |
| `Live` | `Short` | `1366.50` | 17,440,000.00 USD | 194.04 USD | 0.00 USD | `+90.21%` | `142,000,000.00` |
| `Live` | `Short` | `1369.50` | 17,480,000.00 USD | 46,880.00 USD | 0.00 USD | `+90.63%` | `34,232,000,000.00` |
| `Live` | `Short` | `1371.50` | 17,490,000.00 USD | 3,900.00 USD | 0.00 USD | `+90.91%` | `2,846,000,000.00` |
| `Live` | `Short` | `1373.50` | 17,560,000.00 USD | 71,700.00 USD | 0.00 USD | `+91.19%` | `52,204,000,000.00` |
| `Live` | `Short` | `1374.50` | 17,560,000.00 USD | 2,750.00 USD | 0.00 USD | `+91.33%` | `2,000,000,000.00` |
| `Live` | `Short` | `1379.50` | 17,570,000.00 USD | 6,710.00 USD | 0.00 USD | `+92.02%` | `4,866,000,000.00` |
| `Live` | `Short` | `1400.50` | 19,060,000.00 USD | 1,490,000.00 USD | 0.00 USD | `+94.95%` | `1,066,971,000,000.00` |
| `Live` | `Short` | `1401.50` | 19,060,000.00 USD | 692.34 USD | 0.00 USD | `+95.09%` | `494,000,000.00` |
| `Live` | `Short` | `1404.50` | 19,320,000.00 USD | 252,810.00 USD | 0.00 USD | `+95.50%` | `180,000,000,000.00` |
| `Live` | `Short` | `1405.50` | 19,320,000.00 USD | 4,770.00 USD | 0.00 USD | `+95.64%` | `3,392,000,000.00` |
| `Live` | `Short` | `1431.50` | 19,320,000.00 USD | 360.74 USD | 0.00 USD | `+99.26%` | `252,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `150.50` | 4,860,000.00 USD | 0.00 USD | 475.73 USD | `-79.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `300.50` | 4,850,000.00 USD | 0.00 USD | 2,400.00 USD | `-58.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `333.50` | 4,850,000.00 USD | 0.00 USD | 333.50 USD | `-53.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `360.50` | 4,850,000.00 USD | 0.00 USD | 8,140.00 USD | `-49.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `369.50` | 4,840,000.00 USD | 0.00 USD | 5,170.00 USD | `-48.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `400.50` | 4,840,000.00 USD | 0.00 USD | 17,290.00 USD | `-44.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `410.50` | 4,820,000.00 USD | 0.00 USD | 25,210.00 USD | `-42.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `412.50` | 4,800,000.00 USD | 0.00 USD | 4,550.00 USD | `-42.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `424.50` | 4,790,000.00 USD | 0.00 USD | 8,180.00 USD | `-40.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `433.50` | 4,780,000.00 USD | 0.00 USD | 173.83 USD | `-39.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `445.50` | 4,780,000.00 USD | 0.00 USD | 2,210.00 USD | `-37.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `455.50` | 4,780,000.00 USD | 0.00 USD | 698.74 USD | `-36.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `456.50` | 4,780,000.00 USD | 0.00 USD | 2,270.00 USD | `-36.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `458.50` | 4,780,000.00 USD | 0.00 USD | 1,750.00 USD | `-36.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `469.50` | 4,780,000.00 USD | 0.00 USD | 3,550.00 USD | `-34.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `486.50` | 4,770,000.00 USD | 0.00 USD | 100.71 USD | `-32.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `487.50` | 4,770,000.00 USD | 0.00 USD | 6,600.00 USD | `-32.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `488.50` | 4,770,000.00 USD | 0.00 USD | 125.06 USD | `-32.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `492.50` | 4,770,000.00 USD | 0.00 USD | 2,450.00 USD | `-31.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `498.50` | 4,760,000.00 USD | 0.00 USD | 163.01 USD | `-30.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `499.50` | 4,760,000.00 USD | 0.00 USD | 214.78 USD | `-30.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `500.50` | 4,760,000.00 USD | 0.00 USD | 39,500.00 USD | `-30.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `503.50` | 4,720,000.00 USD | 0.00 USD | 42,600.00 USD | `-29.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `506.50` | 4,680,000.00 USD | 0.00 USD | 138.78 USD | `-29.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `509.50` | 4,680,000.00 USD | 0.00 USD | 185.97 USD | `-29.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `515.50` | 4,680,000.00 USD | 0.00 USD | 1,030.00 USD | `-28.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `516.50` | 4,680,000.00 USD | 0.00 USD | 125.51 USD | `-28.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `517.50` | 4,680,000.00 USD | 0.00 USD | 280.49 USD | `-27.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `521.50` | 4,680,000.00 USD | 0.00 USD | 258.14 USD | `-27.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `524.50` | 4,680,000.00 USD | 0.00 USD | 8,170.00 USD | `-26.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `528.50` | 4,670,000.00 USD | 0.00 USD | 485.16 USD | `-26.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `534.50` | 4,670,000.00 USD | 0.00 USD | 4,650.00 USD | `-25.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `538.50` | 4,670,000.00 USD | 0.00 USD | 1,680.00 USD | `-25.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `540.50` | 4,660,000.00 USD | 0.00 USD | 864.80 USD | `-24.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `550.50` | 4,660,000.00 USD | 0.00 USD | 4,130.00 USD | `-23.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `552.50` | 4,660,000.00 USD | 0.00 USD | 366,230.00 USD | `-23.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `554.50` | 4,290,000.00 USD | 0.00 USD | 1,190.00 USD | `-22.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `555.50` | 4,290,000.00 USD | 0.00 USD | 611.05 USD | `-22.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `557.50` | 4,290,000.00 USD | 0.00 USD | 213.52 USD | `-22.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `558.50` | 4,290,000.00 USD | 0.00 USD | 51,260.00 USD | `-22.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `560.50` | 4,240,000.00 USD | 0.00 USD | 292.02 USD | `-21.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `561.50` | 4,240,000.00 USD | 0.00 USD | 748.48 USD | `-21.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `562.50` | 4,240,000.00 USD | 0.00 USD | 199.12 USD | `-21.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `563.50` | 4,240,000.00 USD | 0.00 USD | 808.06 USD | `-21.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `566.50` | 4,240,000.00 USD | 0.00 USD | 566.50 USD | `-21.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `567.50` | 4,240,000.00 USD | 0.00 USD | 330.85 USD | `-21.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `568.50` | 4,240,000.00 USD | 0.00 USD | 5,680.00 USD | `-20.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `569.50` | 4,230,000.00 USD | 0.00 USD | 569.50 USD | `-20.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `570.50` | 4,230,000.00 USD | 0.00 USD | 774.17 USD | `-20.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `571.50` | 4,230,000.00 USD | 0.00 USD | 1,700.00 USD | `-20.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `573.50` | 4,230,000.00 USD | 0.00 USD | 291.91 USD | `-20.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `575.50` | 4,230,000.00 USD | 0.00 USD | 469.61 USD | `-19.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `576.50` | 4,230,000.00 USD | 0.00 USD | 289.98 USD | `-19.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `577.50` | 4,230,000.00 USD | 0.00 USD | 285.86 USD | `-19.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `579.50` | 4,230,000.00 USD | 0.00 USD | 289.17 USD | `-19.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `580.50` | 4,230,000.00 USD | 0.00 USD | 6,750.00 USD | `-19.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `581.50` | 4,220,000.00 USD | 0.00 USD | 1,240.00 USD | `-19.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `582.50` | 4,220,000.00 USD | 0.00 USD | 6,980.00 USD | `-18.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `583.50` | 4,210,000.00 USD | 0.00 USD | 287.67 USD | `-18.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `584.50` | 4,210,000.00 USD | 0.00 USD | 763.94 USD | `-18.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `585.50` | 4,210,000.00 USD | 0.00 USD | 542.76 USD | `-18.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `586.50` | 4,210,000.00 USD | 0.00 USD | 34,020.00 USD | `-18.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `587.50` | 4,180,000.00 USD | 0.00 USD | 830,190.00 USD | `-18.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `588.50` | 3,350,000.00 USD | 0.00 USD | 287.78 USD | `-18.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `589.50` | 3,350,000.00 USD | 0.00 USD | 1,820.00 USD | `-17.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `590.50` | 3,340,000.00 USD | 0.00 USD | 540.31 USD | `-17.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `592.50` | 3,340,000.00 USD | 0.00 USD | 698.56 USD | `-17.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `593.50` | 3,340,000.00 USD | 0.00 USD | 1,160.00 USD | `-17.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `596.50` | 3,340,000.00 USD | 0.00 USD | 119.30 USD | `-16.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `597.50` | 3,340,000.00 USD | 0.00 USD | 222.87 USD | `-16.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `598.50` | 3,340,000.00 USD | 0.00 USD | 244.79 USD | `-16.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `600.50` | 3,340,000.00 USD | 0.00 USD | 43,310.00 USD | `-16.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `601.50` | 3,300,000.00 USD | 0.00 USD | 1,590.00 USD | `-16.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `602.50` | 3,300,000.00 USD | 0.00 USD | 46,760.00 USD | `-16.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `603.50` | 3,250,000.00 USD | 0.00 USD | 123,870.00 USD | `-15.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `604.50` | 3,120,000.00 USD | 0.00 USD | 1,870.00 USD | `-15.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `605.50` | 3,120,000.00 USD | 0.00 USD | 2,610.00 USD | `-15.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `608.50` | 3,120,000.00 USD | 0.00 USD | 18,380.00 USD | `-15.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `610.50` | 3,100,000.00 USD | 0.00 USD | 11,650.00 USD | `-15.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `611.50` | 3,090,000.00 USD | 0.00 USD | 4,470.00 USD | `-14.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `612.50` | 3,090,000.00 USD | 0.00 USD | 1,380.00 USD | `-14.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `614.50` | 3,080,000.00 USD | 0.00 USD | 269.15 USD | `-14.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `615.50` | 3,080,000.00 USD | 0.00 USD | 1,740.00 USD | `-14.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `616.50` | 3,080,000.00 USD | 0.00 USD | 120.83 USD | `-14.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `620.50` | 3,080,000.00 USD | 0.00 USD | 13,170.00 USD | `-13.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `621.50` | 3,070,000.00 USD | 0.00 USD | 2,150.00 USD | `-13.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `623.50` | 3,070,000.00 USD | 0.00 USD | 219.47 USD | `-13.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `624.50` | 3,070,000.00 USD | 0.00 USD | 445.27 USD | `-13.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `625.50` | 3,070,000.00 USD | 0.00 USD | 445.98 USD | `-12.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `626.50` | 3,070,000.00 USD | 0.00 USD | 694.79 USD | `-12.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `627.50` | 3,070,000.00 USD | 0.00 USD | 916.15 USD | `-12.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `628.50` | 3,060,000.00 USD | 0.00 USD | 34,040.00 USD | `-12.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `629.50` | 3,030,000.00 USD | 0.00 USD | 2,740.00 USD | `-12.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `630.50` | 3,030,000.00 USD | 0.00 USD | 861.26 USD | `-12.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `631.50` | 3,030,000.00 USD | 0.00 USD | 179.98 USD | `-12.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `632.50` | 3,030,000.00 USD | 0.00 USD | 1,100.00 USD | `-11.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `633.50` | 3,030,000.00 USD | 0.00 USD | 164.08 USD | `-11.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `634.50` | 3,030,000.00 USD | 0.00 USD | 2,550.00 USD | `-11.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `636.50` | 3,020,000.00 USD | 0.00 USD | 6,460.00 USD | `-11.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `638.50` | 3,020,000.00 USD | 0.00 USD | 3,640.00 USD | `-11.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `639.50` | 3,010,000.00 USD | 0.00 USD | 384.98 USD | `-10.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `640.50` | 3,010,000.00 USD | 0.00 USD | 429.78 USD | `-10.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `641.50` | 3,010,000.00 USD | 0.00 USD | 352.18 USD | `-10.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `642.50` | 3,010,000.00 USD | 0.00 USD | 1,280.00 USD | `-10.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `643.50` | 3,010,000.00 USD | 0.00 USD | 1,830.00 USD | `-10.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `644.50` | 3,010,000.00 USD | 0.00 USD | 3,790.00 USD | `-10.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `645.50` | 3,000,000.00 USD | 0.00 USD | 1,950.00 USD | `-10.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `646.50` | 3,000,000.00 USD | 0.00 USD | 971.04 USD | `-10.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `648.50` | 3,000,000.00 USD | 0.00 USD | 1,800.00 USD | `-9.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `649.50` | 3,000,000.00 USD | 0.00 USD | 107.17 USD | `-9.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `650.50` | 3,000,000.00 USD | 0.00 USD | 30,840.00 USD | `-9.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `651.50` | 2,970,000.00 USD | 0.00 USD | 201.31 USD | `-9.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `653.50` | 2,970,000.00 USD | 0.00 USD | 2,020.00 USD | `-9.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `654.50` | 2,970,000.00 USD | 0.00 USD | 308.92 USD | `-8.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `655.50` | 2,970,000.00 USD | 0.00 USD | 165.84 USD | `-8.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `656.50` | 2,970,000.00 USD | 0.00 USD | 2,330.00 USD | `-8.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `657.50` | 2,960,000.00 USD | 0.00 USD | 110.46 USD | `-8.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `658.50` | 2,960,000.00 USD | 0.00 USD | 1,320.00 USD | `-8.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `659.50` | 2,960,000.00 USD | 0.00 USD | 13,060.00 USD | `-8.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `660.50` | 2,950,000.00 USD | 0.00 USD | 11,090.00 USD | `-8.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `661.50` | 2,940,000.00 USD | 0.00 USD | 11,310.00 USD | `-7.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `662.50` | 2,930,000.00 USD | 0.00 USD | 7,780.00 USD | `-7.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `663.50` | 2,920,000.00 USD | 0.00 USD | 2,840.00 USD | `-7.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `664.50` | 2,920,000.00 USD | 0.00 USD | 864.51 USD | `-7.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `665.50` | 2,920,000.00 USD | 0.00 USD | 12,180.00 USD | `-7.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `666.50` | 2,900,000.00 USD | 0.00 USD | 24,530.00 USD | `-7.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `667.50` | 2,880,000.00 USD | 0.00 USD | 10,740.00 USD | `-7.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `668.50` | 2,870,000.00 USD | 0.00 USD | 760.75 USD | `-6.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `669.50` | 2,870,000.00 USD | 0.00 USD | 2,390.00 USD | `-6.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `670.50` | 2,860,000.00 USD | 0.00 USD | 129,550.00 USD | `-6.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `671.50` | 2,740,000.00 USD | 0.00 USD | 19,160.00 USD | `-6.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `672.50` | 2,720,000.00 USD | 0.00 USD | 1,500.00 USD | `-6.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `673.50` | 2,710,000.00 USD | 0.00 USD | 7,790.00 USD | `-6.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `674.50` | 2,710,000.00 USD | 0.00 USD | 1,470.00 USD | `-6.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `675.50` | 2,710,000.00 USD | 0.00 USD | 10,640.00 USD | `-5.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `676.50` | 2,690,000.00 USD | 0.00 USD | 56,290.00 USD | `-5.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `677.50` | 2,640,000.00 USD | 0.00 USD | 39,650.00 USD | `-5.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `678.50` | 2,600,000.00 USD | 0.00 USD | 825.73 USD | `-5.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `679.50` | 2,600,000.00 USD | 0.00 USD | 5,250.00 USD | `-5.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `680.50` | 2,590,000.00 USD | 0.00 USD | 296,190.00 USD | `-5.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `681.50` | 2,300,000.00 USD | 0.00 USD | 146.52 USD | `-5.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `682.50` | 2,300,000.00 USD | 0.00 USD | 1,160,000.00 USD | `-5.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `683.50` | 1,140,000.00 USD | 0.00 USD | 171,850.00 USD | `-4.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `684.50` | 965,300.00 USD | 0.00 USD | 171,120.00 USD | `-4.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `685.50` | 794,170.00 USD | 0.00 USD | 12,470.00 USD | `-4.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `686.50` | 781,700.00 USD | 0.00 USD | 530.66 USD | `-4.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `687.50` | 781,170.00 USD | 0.00 USD | 330.69 USD | `-4.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `688.50` | 780,840.00 USD | 0.00 USD | 364.22 USD | `-4.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `689.50` | 780,480.00 USD | 0.00 USD | 532.98 USD | `-4.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `690.50` | 779,940.00 USD | 0.00 USD | 3,860.00 USD | `-3.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `691.50` | 776,080.00 USD | 0.00 USD | 173,590.00 USD | `-3.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `692.50` | 602,490.00 USD | 0.00 USD | 2,420.00 USD | `-3.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `693.50` | 600,070.00 USD | 0.00 USD | 7,180.00 USD | `-3.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `694.50` | 592,890.00 USD | 0.00 USD | 589.63 USD | `-3.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `695.50` | 592,300.00 USD | 0.00 USD | 166.92 USD | `-3.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `696.50` | 592,130.00 USD | 0.00 USD | 2,200.00 USD | `-3.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `697.50` | 589,930.00 USD | 0.00 USD | 47,550.00 USD | `-2.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `698.50` | 542,380.00 USD | 0.00 USD | 15,500.00 USD | `-2.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `699.50` | 526,880.00 USD | 0.00 USD | 116,570.00 USD | `-2.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `700.50` | 410,310.00 USD | 0.00 USD | 41,530.00 USD | `-2.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `701.50` | 368,780.00 USD | 0.00 USD | 633.45 USD | `-2.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `702.50` | 368,150.00 USD | 0.00 USD | 29,960.00 USD | `-2.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `703.50` | 338,180.00 USD | 0.00 USD | 3,850.00 USD | `-2.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `704.50` | 334,330.00 USD | 0.00 USD | 86,660.00 USD | `-1.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `705.50` | 247,680.00 USD | 0.00 USD | 6,830.00 USD | `-1.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `706.50` | 240,850.00 USD | 0.00 USD | 21,300.00 USD | `-1.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `707.50` | 219,540.00 USD | 0.00 USD | 182.53 USD | `-1.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `708.50` | 219,360.00 USD | 0.00 USD | 10,760.00 USD | `-1.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `709.50` | 208,600.00 USD | 0.00 USD | 1,490.00 USD | `-1.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `710.50` | 207,120.00 USD | 0.00 USD | 7,940.00 USD | `-1.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `711.50` | 199,170.00 USD | 0.00 USD | 6,700.00 USD | `-0.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `712.50` | 192,470.00 USD | 0.00 USD | 14,490.00 USD | `-0.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `713.50` | 177,980.00 USD | 0.00 USD | 150.55 USD | `-0.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `714.50` | 177,830.00 USD | 0.00 USD | 1,660.00 USD | `-0.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `715.50` | 176,160.00 USD | 0.00 USD | 6,420.00 USD | `-0.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `716.50` | 169,740.00 USD | 0.00 USD | 168,690.00 USD | `-0.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `717.50` | 1,050.00 USD | 0.00 USD | 1,050.00 USD | `-0.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `718.50` | 80,870.00 USD | 80,870.00 USD | 0.00 USD | `+0.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `719.50` | 150,750.00 USD | 69,880.00 USD | 0.00 USD | `+0.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `720.50` | 171,210.00 USD | 20,460.00 USD | 0.00 USD | `+0.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `721.50` | 174,200.00 USD | 2,990.00 USD | 0.00 USD | `+0.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `722.50` | 176,080.00 USD | 1,880.00 USD | 0.00 USD | `+0.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `723.50` | 183,010.00 USD | 6,930.00 USD | 0.00 USD | `+0.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `724.50` | 208,710.00 USD | 25,700.00 USD | 0.00 USD | `+0.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `725.50` | 300,140.00 USD | 91,430.00 USD | 0.00 USD | `+0.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `726.50` | 304,260.00 USD | 4,110.00 USD | 0.00 USD | `+1.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `727.50` | 321,050.00 USD | 16,790.00 USD | 0.00 USD | `+1.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `728.50` | 361,960.00 USD | 40,910.00 USD | 0.00 USD | `+1.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `729.50` | 500,730.00 USD | 138,780.00 USD | 0.00 USD | `+1.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `730.50` | 553,980.00 USD | 53,250.00 USD | 0.00 USD | `+1.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `731.50` | 778,390.00 USD | 224,410.00 USD | 0.00 USD | `+1.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `732.50` | 779,700.00 USD | 1,310.00 USD | 0.00 USD | `+1.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `733.50` | 1,270,000.00 USD | 486,210.00 USD | 0.00 USD | `+2.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `734.50` | 1,270,000.00 USD | 7,480.00 USD | 0.00 USD | `+2.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `735.50` | 1,290,000.00 USD | 12,850.00 USD | 0.00 USD | `+2.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `736.50` | 1,290,000.00 USD | 6,860.00 USD | 0.00 USD | `+2.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `737.50` | 1,300,000.00 USD | 3,970.00 USD | 0.00 USD | `+2.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `738.50` | 1,310,000.00 USD | 12,620.00 USD | 0.00 USD | `+2.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `739.50` | 1,310,000.00 USD | 790.53 USD | 0.00 USD | `+2.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `740.50` | 1,310,000.00 USD | 4,170.00 USD | 0.00 USD | `+3.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `741.50` | 1,320,000.00 USD | 2,370.00 USD | 0.00 USD | `+3.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `742.50` | 1,320,000.00 USD | 4,540.00 USD | 0.00 USD | `+3.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `743.50` | 1,330,000.00 USD | 8,880.00 USD | 0.00 USD | `+3.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `744.50` | 1,530,000.00 USD | 203,810.00 USD | 0.00 USD | `+3.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `745.50` | 1,550,000.00 USD | 14,430.00 USD | 0.00 USD | `+3.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `746.50` | 1,550,000.00 USD | 672.60 USD | 0.00 USD | `+3.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `747.50` | 1,550,000.00 USD | 1,070.00 USD | 0.00 USD | `+4.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `748.50` | 1,550,000.00 USD | 558.38 USD | 0.00 USD | `+4.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `749.50` | 1,550,000.00 USD | 704.53 USD | 0.00 USD | `+4.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `750.50` | 1,550,000.00 USD | 123.83 USD | 0.00 USD | `+4.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `751.50` | 1,560,000.00 USD | 6,850.00 USD | 0.00 USD | `+4.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `752.50` | 1,560,000.00 USD | 2,730.00 USD | 0.00 USD | `+4.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `753.50` | 1,560,000.00 USD | 105.49 USD | 0.00 USD | `+4.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `754.50` | 1,610,000.00 USD | 47,160.00 USD | 0.00 USD | `+5.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `755.50` | 1,610,000.00 USD | 4,420.00 USD | 0.00 USD | `+5.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `756.50` | 1,630,000.00 USD | 12,340.00 USD | 0.00 USD | `+5.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `757.50` | 1,770,000.00 USD | 142,940.00 USD | 0.00 USD | `+5.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `758.50` | 1,770,000.00 USD | 2,920.00 USD | 0.00 USD | `+5.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `759.50` | 1,790,000.00 USD | 21,350.00 USD | 0.00 USD | `+5.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `760.50` | 2,080,000.00 USD | 288,360.00 USD | 0.00 USD | `+5.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `761.50` | 2,090,000.00 USD | 11,460.00 USD | 0.00 USD | `+6.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `762.50` | 2,090,000.00 USD | 274.50 USD | 0.00 USD | `+6.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `763.50` | 2,140,000.00 USD | 45,960.00 USD | 0.00 USD | `+6.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `764.50` | 2,140,000.00 USD | 323.38 USD | 0.00 USD | `+6.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `765.50` | 2,180,000.00 USD | 41,050.00 USD | 0.00 USD | `+6.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `766.50` | 2,180,000.00 USD | 600.94 USD | 0.00 USD | `+6.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `767.50` | 2,650,000.00 USD | 468,310.00 USD | 0.00 USD | `+6.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `768.50` | 2,650,000.00 USD | 180.60 USD | 0.00 USD | `+6.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `769.50` | 2,650,000.00 USD | 171.60 USD | 0.00 USD | `+7.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `770.50` | 2,650,000.00 USD | 1,540.00 USD | 0.00 USD | `+7.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `771.50` | 2,650,000.00 USD | 242.25 USD | 0.00 USD | `+7.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `772.50` | 2,650,000.00 USD | 273.46 USD | 0.00 USD | `+7.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `773.50` | 2,650,000.00 USD | 656.70 USD | 0.00 USD | `+7.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `774.50` | 2,660,000.00 USD | 9,680.00 USD | 0.00 USD | `+7.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `775.50` | 2,670,000.00 USD | 4,570.00 USD | 0.00 USD | `+7.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `776.50` | 2,680,000.00 USD | 14,230.00 USD | 0.00 USD | `+8.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `777.50` | 2,700,000.00 USD | 15,690.00 USD | 0.00 USD | `+8.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `778.50` | 2,700,000.00 USD | 4,580.00 USD | 0.00 USD | `+8.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `779.50` | 2,700,000.00 USD | 132.52 USD | 0.00 USD | `+8.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `780.50` | 2,730,000.00 USD | 24,280.00 USD | 0.00 USD | `+8.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `781.50` | 2,730,000.00 USD | 2,050.00 USD | 0.00 USD | `+8.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `782.50` | 2,730,000.00 USD | 1,900.00 USD | 0.00 USD | `+8.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `783.50` | 2,730,000.00 USD | 101.07 USD | 0.00 USD | `+9.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `784.50` | 2,730,000.00 USD | 102.77 USD | 0.00 USD | `+9.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `785.50` | 2,730,000.00 USD | 559.28 USD | 0.00 USD | `+9.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `786.50` | 2,740,000.00 USD | 11,990.00 USD | 0.00 USD | `+9.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `787.50` | 2,740,000.00 USD | 2,260.00 USD | 0.00 USD | `+9.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `788.50` | 2,740,000.00 USD | 133.26 USD | 0.00 USD | `+9.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `790.50` | 2,750,000.00 USD | 4,190.00 USD | 0.00 USD | `+10.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `791.50` | 2,750,000.00 USD | 704.44 USD | 0.00 USD | `+10.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `792.50` | 2,750,000.00 USD | 4,360.00 USD | 0.00 USD | `+10.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `793.50` | 2,760,000.00 USD | 1,450.00 USD | 0.00 USD | `+10.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `794.50` | 2,760,000.00 USD | 3,630.00 USD | 0.00 USD | `+10.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `795.50` | 2,760,000.00 USD | 3,040.00 USD | 0.00 USD | `+10.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `796.50` | 2,760,000.00 USD | 154.52 USD | 0.00 USD | `+10.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `799.50` | 2,760,000.00 USD | 1,450.00 USD | 0.00 USD | `+11.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `800.50` | 2,780,000.00 USD | 12,890.00 USD | 0.00 USD | `+11.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `801.50` | 2,780,000.00 USD | 120.22 USD | 0.00 USD | `+11.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `803.50` | 2,780,000.00 USD | 803.50 USD | 0.00 USD | `+11.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `805.50` | 2,780,000.00 USD | 120.02 USD | 0.00 USD | `+12.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `806.50` | 2,780,000.00 USD | 1,300.00 USD | 0.00 USD | `+12.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `808.50` | 2,780,000.00 USD | 5,010.00 USD | 0.00 USD | `+12.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `809.50` | 2,780,000.00 USD | 242.04 USD | 0.00 USD | `+12.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `810.50` | 2,800,000.00 USD | 15,790.00 USD | 0.00 USD | `+12.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `811.50` | 2,810,000.00 USD | 6,050.00 USD | 0.00 USD | `+12.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `812.50` | 2,810,000.00 USD | 844.19 USD | 0.00 USD | `+13.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `813.50` | 2,810,000.00 USD | 109.82 USD | 0.00 USD | `+13.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `814.50` | 2,810,000.00 USD | 3,390.00 USD | 0.00 USD | `+13.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `816.50` | 2,810,000.00 USD | 984.70 USD | 0.00 USD | `+13.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `817.50` | 2,810,000.00 USD | 162.68 USD | 0.00 USD | `+13.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `818.50` | 2,820,000.00 USD | 5,990.00 USD | 0.00 USD | `+13.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `820.50` | 2,830,000.00 USD | 8,230.00 USD | 0.00 USD | `+14.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `824.50` | 2,830,000.00 USD | 408.13 USD | 0.00 USD | `+14.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `826.50` | 2,830,000.00 USD | 672.77 USD | 0.00 USD | `+15.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `827.50` | 2,830,000.00 USD | 276.38 USD | 0.00 USD | `+15.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `828.50` | 2,830,000.00 USD | 1,800.00 USD | 0.00 USD | `+15.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `830.50` | 2,860,000.00 USD | 35,850.00 USD | 0.00 USD | `+15.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `833.50` | 2,870,000.00 USD | 1,050.00 USD | 0.00 USD | `+16.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `835.50` | 2,870,000.00 USD | 187.15 USD | 0.00 USD | `+16.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `836.50` | 2,870,000.00 USD | 372.24 USD | 0.00 USD | `+16.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `837.50` | 2,870,000.00 USD | 326.62 USD | 0.00 USD | `+16.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `839.50` | 2,870,000.00 USD | 296.34 USD | 0.00 USD | `+16.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `840.50` | 2,870,000.00 USD | 441.26 USD | 0.00 USD | `+17.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `841.50` | 2,870,000.00 USD | 329.87 USD | 0.00 USD | `+17.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `843.50` | 2,870,000.00 USD | 425.97 USD | 0.00 USD | `+17.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `844.50` | 2,870,000.00 USD | 1,770.00 USD | 0.00 USD | `+17.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `850.50` | 2,870,000.00 USD | 2,550.00 USD | 0.00 USD | `+18.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `851.50` | 2,880,000.00 USD | 11,650.00 USD | 0.00 USD | `+18.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `852.50` | 2,880,000.00 USD | 102.30 USD | 0.00 USD | `+18.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `854.50` | 2,880,000.00 USD | 137.57 USD | 0.00 USD | `+18.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `857.50` | 2,890,000.00 USD | 1,200.00 USD | 0.00 USD | `+19.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `860.50` | 2,890,000.00 USD | 1,160.00 USD | 0.00 USD | `+19.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `862.50` | 2,890,000.00 USD | 1,200.00 USD | 0.00 USD | `+20.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `863.50` | 2,890,000.00 USD | 874.73 USD | 0.00 USD | `+20.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `864.50` | 2,890,000.00 USD | 2,970.00 USD | 0.00 USD | `+20.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `865.50` | 2,890,000.00 USD | 3,460.00 USD | 0.00 USD | `+20.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `868.50` | 2,900,000.00 USD | 2,610.00 USD | 0.00 USD | `+20.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `870.50` | 2,900,000.00 USD | 228.07 USD | 0.00 USD | `+21.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `872.50` | 2,900,000.00 USD | 1,110.00 USD | 0.00 USD | `+21.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `884.50` | 2,950,000.00 USD | 54,820.00 USD | 0.00 USD | `+23.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `888.50` | 2,950,000.00 USD | 266.55 USD | 0.00 USD | `+23.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `890.50` | 2,950,000.00 USD | 690.14 USD | 0.00 USD | `+23.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `891.50` | 2,960,000.00 USD | 605.33 USD | 0.00 USD | `+24.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `900.50` | 3,090,000.00 USD | 132,720.00 USD | 0.00 USD | `+25.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `904.50` | 3,090,000.00 USD | 167.33 USD | 0.00 USD | `+25.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `907.50` | 3,090,000.00 USD | 1,640.00 USD | 0.00 USD | `+26.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `913.50` | 3,090,000.00 USD | 908.02 USD | 0.00 USD | `+27.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `914.50` | 3,090,000.00 USD | 4,150.00 USD | 0.00 USD | `+27.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `917.50` | 3,100,000.00 USD | 533.99 USD | 0.00 USD | `+27.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `919.50` | 3,100,000.00 USD | 166.43 USD | 0.00 USD | `+27.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `920.50` | 3,100,000.00 USD | 463.01 USD | 0.00 USD | `+28.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `926.50` | 3,100,000.00 USD | 320.57 USD | 0.00 USD | `+28.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `930.50` | 3,100,000.00 USD | 552.72 USD | 0.00 USD | `+29.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `933.50` | 3,100,000.00 USD | 196.03 USD | 0.00 USD | `+29.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `935.50` | 3,100,000.00 USD | 287.20 USD | 0.00 USD | `+30.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `958.50` | 3,100,000.00 USD | 782.14 USD | 0.00 USD | `+33.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `959.50` | 3,100,000.00 USD | 498.94 USD | 0.00 USD | `+33.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `965.50` | 3,100,000.00 USD | 1,930.00 USD | 0.00 USD | `+34.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `977.50` | 3,100,000.00 USD | 293.25 USD | 0.00 USD | `+36.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `980.50` | 3,100,000.00 USD | 1,300.00 USD | 0.00 USD | `+36.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `981.50` | 3,100,000.00 USD | 109.93 USD | 0.00 USD | `+36.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `984.50` | 3,100,000.00 USD | 439.09 USD | 0.00 USD | `+37.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `987.50` | 3,110,000.00 USD | 2,590.00 USD | 0.00 USD | `+37.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `997.50` | 3,110,000.00 USD | 1,840.00 USD | 0.00 USD | `+38.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `998.50` | 3,110,000.00 USD | 3,990.00 USD | 0.00 USD | `+38.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `999.50` | 3,110,000.00 USD | 938.53 USD | 0.00 USD | `+39.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1000.50` | 3,120,000.00 USD | 11,810.00 USD | 0.00 USD | `+39.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1017.50` | 3,120,000.00 USD | 203.50 USD | 0.00 USD | `+41.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1020.50` | 3,120,000.00 USD | 148.99 USD | 0.00 USD | `+42.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1026.50` | 3,120,000.00 USD | 149.87 USD | 0.00 USD | `+42.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1030.50` | 3,120,000.00 USD | 150.45 USD | 0.00 USD | `+43.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1045.50` | 3,120,000.00 USD | 195.51 USD | 0.00 USD | `+45.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1053.50` | 3,120,000.00 USD | 149.60 USD | 0.00 USD | `+46.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1072.50` | 3,120,000.00 USD | 156.58 USD | 0.00 USD | `+49.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1100.50` | 3,130,000.00 USD | 278.43 USD | 0.00 USD | `+53.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1111.50` | 3,130,000.00 USD | 555.75 USD | 0.00 USD | `+54.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1136.50` | 3,130,000.00 USD | 165.93 USD | 0.00 USD | `+58.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1146.50` | 3,130,000.00 USD | 167.39 USD | 0.00 USD | `+59.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1200.50` | 3,190,000.00 USD | 62,330.00 USD | 0.00 USD | `+67.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1202.50` | 3,190,000.00 USD | 1,250.00 USD | 0.00 USD | `+67.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1226.50` | 3,190,000.00 USD | 235.49 USD | 0.00 USD | `+70.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1230.50` | 3,190,000.00 USD | 3,580.00 USD | 0.00 USD | `+71.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1250.50` | 3,190,000.00 USD | 421.42 USD | 0.00 USD | `+74.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1280.50` | 3,200,000.00 USD | 3,750.00 USD | 0.00 USD | `+78.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1297.50` | 3,200,000.00 USD | 133.64 USD | 0.00 USD | `+80.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1300.50` | 3,200,000.00 USD | 685.36 USD | 0.00 USD | `+81.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1330.50` | 3,260,000.00 USD | 58,230.00 USD | 0.00 USD | `+85.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1340.50` | 3,340,000.00 USD | 80,850.00 USD | 0.00 USD | `+86.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1360.50` | 3,340,000.00 USD | 6,210.00 USD | 0.00 USD | `+89.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1363.50` | 3,340,000.00 USD | 349.06 USD | 0.00 USD | `+89.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1370.50` | 3,350,000.00 USD | 1,060.00 USD | 0.00 USD | `+90.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1372.50` | 3,360,000.00 USD | 19,210.00 USD | 0.00 USD | `+91.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1389.50` | 3,360,000.00 USD | 425.19 USD | 0.00 USD | `+93.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1400.50` | 3,370,000.00 USD | 3,850.00 USD | 0.00 USD | `+94.95%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `631.10` | 39,810,000.00 USD | 0.00 USD | 39,810,000.00 USD | 0.00 USD | 93,570.00 USD | 875,670.00 USD |
| `1D` | `632.00` | 38,840,000.00 USD | 0.00 USD | 38,840,000.00 USD | 88,900.00 USD | 42,940.00 USD | 0.00 USD |
| `1D` | `632.90` | 38,710,000.00 USD | 0.00 USD | 38,710,000.00 USD | 514,860.00 USD | 11,420.00 USD | 40,920.00 USD |
| `1D` | `633.80` | 38,140,000.00 USD | 0.00 USD | 38,140,000.00 USD | 16,720.00 USD | 0.00 USD | 73,220.00 USD |
| `1D` | `634.70` | 38,050,000.00 USD | 0.00 USD | 38,050,000.00 USD | 11,290.00 USD | 39,990.00 USD | 37,540.00 USD |
| `1D` | `635.60` | 37,960,000.00 USD | 0.00 USD | 37,960,000.00 USD | 0.00 USD | 0.00 USD | 38,870.00 USD |
| `1D` | `636.50` | 37,920,000.00 USD | 0.00 USD | 37,920,000.00 USD | 101,910.00 USD | 40,910.00 USD | 236,370.00 USD |
| `1D` | `638.30` | 37,540,000.00 USD | 0.00 USD | 37,540,000.00 USD | 0.00 USD | 37,610.00 USD | 0.00 USD |
| `1D` | `639.20` | 37,510,000.00 USD | 0.00 USD | 37,510,000.00 USD | 184,100.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `640.10` | 37,320,000.00 USD | 0.00 USD | 37,320,000.00 USD | 0.00 USD | 0.00 USD | 184,710.00 USD |
| `1D` | `641.90` | 37,140,000.00 USD | 0.00 USD | 37,140,000.00 USD | 150,090.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `644.60` | 36,990,000.00 USD | 0.00 USD | 36,990,000.00 USD | 308,550.00 USD | 0.00 USD | 341,610.00 USD |
| `1D` | `646.40` | 36,340,000.00 USD | 0.00 USD | 36,340,000.00 USD | 87,020.00 USD | 0.00 USD | 140,640.00 USD |
| `1D` | `647.30` | 36,110,000.00 USD | 0.00 USD | 36,110,000.00 USD | 227,570.00 USD | 29,080.00 USD | 0.00 USD |
| `1D` | `648.20` | 35,850,000.00 USD | 0.00 USD | 35,850,000.00 USD | 101,870.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `651.80` | 35,750,000.00 USD | 0.00 USD | 35,750,000.00 USD | 106,810.00 USD | 0.00 USD | 94,590.00 USD |
| `1D` | `653.60` | 35,550,000.00 USD | 0.00 USD | 35,550,000.00 USD | 0.00 USD | 26,830.00 USD | 0.00 USD |
| `1D` | `654.50` | 35,520,000.00 USD | 0.00 USD | 35,520,000.00 USD | 108,090.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `655.40` | 35,410,000.00 USD | 0.00 USD | 35,410,000.00 USD | 192,610.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `656.30` | 35,220,000.00 USD | 0.00 USD | 35,220,000.00 USD | 35,490.00 USD | 0.00 USD | 825,700.00 USD |
| `1D` | `657.20` | 34,360,000.00 USD | 0.00 USD | 34,360,000.00 USD | 76,470.00 USD | 21,320.00 USD | 0.00 USD |
| `1D` | `658.10` | 34,260,000.00 USD | 0.00 USD | 34,260,000.00 USD | 853,340.00 USD | 14,920.00 USD | 0.00 USD |
| `1D` | `659.00` | 33,390,000.00 USD | 0.00 USD | 33,390,000.00 USD | 81,060.00 USD | 0.00 USD | 81,440.00 USD |
| `1D` | `659.90` | 33,230,000.00 USD | 0.00 USD | 33,230,000.00 USD | 0.00 USD | 7,460.00 USD | 14,670.00 USD |
| `1D` | `660.80` | 33,210,000.00 USD | 0.00 USD | 33,210,000.00 USD | 90,670.00 USD | 83,170.00 USD | 0.00 USD |
| `1D` | `661.70` | 33,040,000.00 USD | 0.00 USD | 33,040,000.00 USD | 445,210.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `662.60` | 32,590,000.00 USD | 0.00 USD | 32,590,000.00 USD | 57,440.00 USD | 87,740.00 USD | 0.00 USD |
| `1D` | `663.50` | 32,440,000.00 USD | 0.00 USD | 32,440,000.00 USD | 145,120.00 USD | 5,000.00 USD | 19,650.00 USD |
| `7D` | `664.10` | 87,050,000.00 USD | 0.00 USD | 87,050,000.00 USD | 78,740.00 USD | 18,740.00 USD | 39,340.00 USD |
| `1D` | `664.40` | 32,280,000.00 USD | 0.00 USD | 32,280,000.00 USD | 1,200,000.00 USD | 48,410.00 USD | 21,160.00 USD |
| `7D` | `665.00` | 86,910,000.00 USD | 0.00 USD | 86,910,000.00 USD | 92,030.00 USD | 22,990.00 USD | 37,000.00 USD |
| `1D` | `665.30` | 31,010,000.00 USD | 0.00 USD | 31,010,000.00 USD | 70,400.00 USD | 4,540.00 USD | 11,460.00 USD |
| `7D` | `665.90` | 86,760,000.00 USD | 0.00 USD | 86,760,000.00 USD | 264,020.00 USD | 71,380.00 USD | 63,410.00 USD |
| `1D` | `666.20` | 30,920,000.00 USD | 0.00 USD | 30,920,000.00 USD | 720,400.00 USD | 88,780.00 USD | 692,530.00 USD |
| `7D` | `666.80` | 86,360,000.00 USD | 0.00 USD | 86,360,000.00 USD | 198,550.00 USD | 33,320.00 USD | 61,710.00 USD |
| `1D` | `667.10` | 29,420,000.00 USD | 0.00 USD | 29,420,000.00 USD | 709,250.00 USD | 16,560.00 USD | 13,240.00 USD |
| `7D` | `667.70` | 86,070,000.00 USD | 0.00 USD | 86,070,000.00 USD | 199,690.00 USD | 45,130.00 USD | 51,340.00 USD |
| `1D` | `668.00` | 28,680,000.00 USD | 0.00 USD | 28,680,000.00 USD | 265,780.00 USD | 120,730.00 USD | 0.00 USD |
| `7D` | `668.60` | 85,770,000.00 USD | 0.00 USD | 85,770,000.00 USD | 387,530.00 USD | 92,860.00 USD | 51,060.00 USD |
| `1D` | `668.90` | 28,300,000.00 USD | 0.00 USD | 28,300,000.00 USD | 603,810.00 USD | 17,190.00 USD | 3,620.00 USD |
| `7D` | `669.50` | 85,240,000.00 USD | 0.00 USD | 85,240,000.00 USD | 341,150.00 USD | 38,130.00 USD | 108,970.00 USD |
| `1D` | `669.80` | 27,670,000.00 USD | 0.00 USD | 27,670,000.00 USD | 237,120.00 USD | 61,020.00 USD | 1,490,000.00 USD |
| `7D` | `670.40` | 84,750,000.00 USD | 0.00 USD | 84,750,000.00 USD | 319,660.00 USD | 93,800.00 USD | 77,380.00 USD |
| `1D` | `670.70` | 25,890,000.00 USD | 0.00 USD | 25,890,000.00 USD | 193,670.00 USD | 4,460.00 USD | 7,950.00 USD |
| `7D` | `671.30` | 84,260,000.00 USD | 0.00 USD | 84,260,000.00 USD | 335,750.00 USD | 57,500.00 USD | 42,050.00 USD |
| `1D` | `671.60` | 25,680,000.00 USD | 0.00 USD | 25,680,000.00 USD | 1,850,000.00 USD | 13,640.00 USD | 11,320.00 USD |
| `7D` | `672.20` | 83,830,000.00 USD | 0.00 USD | 83,830,000.00 USD | 180,230.00 USD | 62,620.00 USD | 74,250.00 USD |
| `1D` | `672.50` | 23,800,000.00 USD | 0.00 USD | 23,800,000.00 USD | 214,460.00 USD | 15,830.00 USD | 670,660.00 USD |
| `7D` | `673.10` | 83,510,000.00 USD | 0.00 USD | 83,510,000.00 USD | 394,120.00 USD | 64,970.00 USD | 42,710.00 USD |
| `1D` | `673.40` | 22,900,000.00 USD | 0.00 USD | 22,900,000.00 USD | 345,840.00 USD | 296,640.00 USD | 1,650,000.00 USD |
| `7D` | `674.00` | 83,010,000.00 USD | 0.00 USD | 83,010,000.00 USD | 335,670.00 USD | 105,910.00 USD | 80,360.00 USD |
| `1D` | `674.30` | 20,600,000.00 USD | 0.00 USD | 20,600,000.00 USD | 359,530.00 USD | 351,220.00 USD | 178,030.00 USD |
| `7D` | `674.90` | 82,490,000.00 USD | 0.00 USD | 82,490,000.00 USD | 247,070.00 USD | 31,490.00 USD | 44,420.00 USD |
| `1D` | `675.20` | 19,720,000.00 USD | 0.00 USD | 19,720,000.00 USD | 2,080,000.00 USD | 63,140.00 USD | 397,490.00 USD |
| `7D` | `675.80` | 82,160,000.00 USD | 0.00 USD | 82,160,000.00 USD | 387,400.00 USD | 26,020.00 USD | 79,190.00 USD |
| `1D` | `676.10` | 17,180,000.00 USD | 0.00 USD | 17,180,000.00 USD | 207,530.00 USD | 284,040.00 USD | 422,620.00 USD |
| `7D` | `676.70` | 81,670,000.00 USD | 0.00 USD | 81,670,000.00 USD | 509,100.00 USD | 35,490.00 USD | 126,570.00 USD |
| `1D` | `677.00` | 16,260,000.00 USD | 0.00 USD | 16,260,000.00 USD | 417,680.00 USD | 82,460.00 USD | 185,760.00 USD |
| `7D` | `677.60` | 81,000,000.00 USD | 0.00 USD | 81,000,000.00 USD | 409,810.00 USD | 0.00 USD | 63,990.00 USD |
| `1D` | `677.90` | 15,580,000.00 USD | 0.00 USD | 15,580,000.00 USD | 215,410.00 USD | 109,020.00 USD | 97,180.00 USD |
| `7D` | `678.50` | 80,530,000.00 USD | 0.00 USD | 80,530,000.00 USD | 120,190.00 USD | 0.00 USD | 26,990.00 USD |
| `1D` | `678.80` | 15,150,000.00 USD | 0.00 USD | 15,150,000.00 USD | 1,030,000.00 USD | 111,360.00 USD | 0.00 USD |
| `7D` | `679.40` | 80,380,000.00 USD | 0.00 USD | 80,380,000.00 USD | 116,510.00 USD | 10,480.00 USD | 40,610.00 USD |
| `1D` | `679.70` | 14,020,000.00 USD | 0.00 USD | 14,020,000.00 USD | 1,200,000.00 USD | 164,850.00 USD | 0.00 USD |
| `7D` | `680.30` | 80,210,000.00 USD | 0.00 USD | 80,210,000.00 USD | 166,780.00 USD | 13,510.00 USD | 0.00 USD |
| `1D` | `680.60` | 12,650,000.00 USD | 0.00 USD | 12,650,000.00 USD | 2,190.00 USD | 98,700.00 USD | 0.00 USD |
| `7D` | `681.20` | 80,030,000.00 USD | 0.00 USD | 80,030,000.00 USD | 106,280.00 USD | 7,050.00 USD | 35,170.00 USD |
| `1D` | `681.50` | 12,550,000.00 USD | 0.00 USD | 12,550,000.00 USD | 11,460.00 USD | 293,520.00 USD | 0.00 USD |
| `7D` | `682.10` | 79,880,000.00 USD | 0.00 USD | 79,880,000.00 USD | 0.00 USD | 23,360.00 USD | 27,620.00 USD |
| `1D` | `682.40` | 12,250,000.00 USD | 0.00 USD | 12,250,000.00 USD | 35,000.00 USD | 10,250.00 USD | 0.00 USD |
| `7D` | `683.00` | 79,830,000.00 USD | 0.00 USD | 79,830,000.00 USD | 175,930.00 USD | 28,470.00 USD | 11,520.00 USD |
| `1D` | `683.30` | 12,200,000.00 USD | 0.00 USD | 12,200,000.00 USD | 118,750.00 USD | 125,590.00 USD | 0.00 USD |
| `7D` | `683.90` | 79,620,000.00 USD | 0.00 USD | 79,620,000.00 USD | 77,000.00 USD | 29,510.00 USD | 17,480.00 USD |
| `1D` | `684.20` | 11,960,000.00 USD | 0.00 USD | 11,960,000.00 USD | 19,390.00 USD | 38,160.00 USD | 0.00 USD |
| `7D` | `684.80` | 79,490,000.00 USD | 0.00 USD | 79,490,000.00 USD | 246,080.00 USD | 9,850.00 USD | 39,550.00 USD |
| `7D` | `685.70` | 79,200,000.00 USD | 0.00 USD | 79,200,000.00 USD | 197,040.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `686.00` | 11,900,000.00 USD | 0.00 USD | 11,900,000.00 USD | 694,060.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `686.60` | 79,000,000.00 USD | 0.00 USD | 79,000,000.00 USD | 62,990.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `686.90` | 11,210,000.00 USD | 0.00 USD | 11,210,000.00 USD | 0.00 USD | 266,430.00 USD | 316,590.00 USD |
| `7D` | `687.50` | 78,940,000.00 USD | 0.00 USD | 78,940,000.00 USD | 148,480.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `687.80` | 10,620,000.00 USD | 0.00 USD | 10,620,000.00 USD | 775,320.00 USD | 295,490.00 USD | 3,930,000.00 USD |
| `7D` | `688.40` | 78,790,000.00 USD | 0.00 USD | 78,790,000.00 USD | 67,880.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `688.70` | 5,620,000.00 USD | 0.00 USD | 5,620,000.00 USD | 2,210,000.00 USD | 91,030.00 USD | 340,730.00 USD |
| `7D` | `689.30` | 78,720,000.00 USD | 0.00 USD | 78,720,000.00 USD | 84,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `689.60` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 306,820.00 USD | 38,440.00 USD | 694,240.00 USD |
| `7D` | `690.20` | 78,640,000.00 USD | 0.00 USD | 78,640,000.00 USD | 283,920.00 USD | 63,230.00 USD | 82,450.00 USD |
| `1D` | `690.50` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 367,190.00 USD | 146,030.00 USD | 625,470.00 USD |
| `7D` | `691.10` | 78,210,000.00 USD | 0.00 USD | 78,210,000.00 USD | 362,020.00 USD | 61,370.00 USD | 81,090.00 USD |
| `1D` | `691.40` | 800,560.00 USD | 0.00 USD | 800,560.00 USD | 33,240.00 USD | 129,500.00 USD | 306,040.00 USD |
| `7D` | `692.00` | 77,700,000.00 USD | 0.00 USD | 77,700,000.00 USD | 322,430.00 USD | 18,850.00 USD | 58,910.00 USD |
| `1D` | `692.30` | 331,790.00 USD | 0.00 USD | 331,790.00 USD | 0.00 USD | 0.00 USD | 194,350.00 USD |
| `7D` | `692.90` | 77,300,000.00 USD | 0.00 USD | 77,300,000.00 USD | 280,830.00 USD | 19,470.00 USD | 0.00 USD |
| `7D` | `693.80` | 77,000,000.00 USD | 0.00 USD | 77,000,000.00 USD | 305,720.00 USD | 39,210.00 USD | 0.00 USD |
| `7D` | `694.70` | 76,660,000.00 USD | 0.00 USD | 76,660,000.00 USD | 279,840.00 USD | 36,640.00 USD | 35,490.00 USD |
| `7D` | `695.60` | 76,300,000.00 USD | 0.00 USD | 76,300,000.00 USD | 120,440.00 USD | 0.00 USD | 21,670.00 USD |
| `1D` | `695.90` | 137,440.00 USD | 0.00 USD | 137,440.00 USD | 0.00 USD | 137,440.00 USD | 0.00 USD |
| `7D` | `696.50` | 76,160,000.00 USD | 0.00 USD | 76,160,000.00 USD | 140,370.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `697.40` | 76,020,000.00 USD | 0.00 USD | 76,020,000.00 USD | 189,100.00 USD | 19,230.00 USD | 0.00 USD |
| `7D` | `698.30` | 75,810,000.00 USD | 0.00 USD | 75,810,000.00 USD | 273,520.00 USD | 33,120.00 USD | 54,800.00 USD |
| `7D` | `699.20` | 75,450,000.00 USD | 0.00 USD | 75,450,000.00 USD | 274,810.00 USD | 12,670.00 USD | 11,820.00 USD |
| `7D` | `700.10` | 75,150,000.00 USD | 0.00 USD | 75,150,000.00 USD | 225,450.00 USD | 40,820.00 USD | 27,440.00 USD |
| `7D` | `701.00` | 74,860,000.00 USD | 0.00 USD | 74,860,000.00 USD | 237,800.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `701.90` | 74,620,000.00 USD | 0.00 USD | 74,620,000.00 USD | 135,260.00 USD | 41,260.00 USD | 89,700.00 USD |
| `7D` | `702.80` | 74,360,000.00 USD | 0.00 USD | 74,360,000.00 USD | 416,820.00 USD | 57,470.00 USD | 36,720.00 USD |
| `7D` | `703.70` | 73,840,000.00 USD | 0.00 USD | 73,840,000.00 USD | 311,800.00 USD | 44,990.00 USD | 0.00 USD |
| `7D` | `704.60` | 73,490,000.00 USD | 0.00 USD | 73,490,000.00 USD | 537,050.00 USD | 136,550.00 USD | 194,460.00 USD |
| `7D` | `705.50` | 72,620,000.00 USD | 0.00 USD | 72,620,000.00 USD | 920,340.00 USD | 162,820.00 USD | 236,670.00 USD |
| `7D` | `706.40` | 71,300,000.00 USD | 0.00 USD | 71,300,000.00 USD | 523,540.00 USD | 104,380.00 USD | 231,200.00 USD |
| `1D` | `706.50` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `707.30` | 70,440,000.00 USD | 0.00 USD | 70,440,000.00 USD | 604,060.00 USD | 90,200.00 USD | 53,960.00 USD |
| `7D` | `708.20` | 69,690,000.00 USD | 0.00 USD | 69,690,000.00 USD | 796,640.00 USD | 138,200.00 USD | 42,800.00 USD |
| `7D` | `709.10` | 68,710,000.00 USD | 0.00 USD | 68,710,000.00 USD | 392,150.00 USD | 156,040.00 USD | 195,500.00 USD |
| `7D` | `710.00` | 67,970,000.00 USD | 0.00 USD | 67,970,000.00 USD | 450,480.00 USD | 167,090.00 USD | 176,960.00 USD |
| `7D` | `710.90` | 67,180,000.00 USD | 0.00 USD | 67,180,000.00 USD | 922,450.00 USD | 160,040.00 USD | 236,990.00 USD |
| `7D` | `711.80` | 65,860,000.00 USD | 0.00 USD | 65,860,000.00 USD | 608,910.00 USD | 232,130.00 USD | 114,740.00 USD |
| `7D` | `712.70` | 64,900,000.00 USD | 0.00 USD | 64,900,000.00 USD | 1,190,000.00 USD | 217,390.00 USD | 236,970.00 USD |
| `7D` | `713.60` | 63,260,000.00 USD | 0.00 USD | 63,260,000.00 USD | 2,250,000.00 USD | 279,180.00 USD | 308,960.00 USD |
| `7D` | `714.50` | 60,410,000.00 USD | 0.00 USD | 60,410,000.00 USD | 508,400.00 USD | 209,320.00 USD | 292,980.00 USD |
| `1D` | `714.80` | 463,510.00 USD | 463,510.00 USD | 0.00 USD | 0.00 USD | 146,930.00 USD | 316,590.00 USD |
| `7D` | `715.40` | 59,400,000.00 USD | 0.00 USD | 59,400,000.00 USD | 1,050,000.00 USD | 419,310.00 USD | 329,730.00 USD |
| `1D` | `715.70` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 498,160.00 USD | 1,060,000.00 USD |
| `7D` | `716.30` | 57,600,000.00 USD | 0.00 USD | 57,600,000.00 USD | 1,080,000.00 USD | 324,540.00 USD | 233,140.00 USD |
| `1D` | `716.60` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 303,890.00 USD | 305,750.00 USD | 340,730.00 USD |
| `7D` | `717.20` | 55,960,000.00 USD | 0.00 USD | 55,960,000.00 USD | 581,610.00 USD | 398,030.00 USD | 387,120.00 USD |
| `1D` | `717.50` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 268,080.00 USD | 126,170.00 USD | 579,800.00 USD |
| `7D` | `718.10` | 54,590,000.00 USD | 0.00 USD | 54,590,000.00 USD | 1,690,000.00 USD | 246,320.00 USD | 151,880.00 USD |
| `1D` | `718.40` | 4,980,000.00 USD | 4,980,000.00 USD | 0.00 USD | 145,050.00 USD | 146,030.00 USD | 739,910.00 USD |
| `7D` | `719.00` | 52,510,000.00 USD | 0.00 USD | 52,510,000.00 USD | 670,390.00 USD | 137,460.00 USD | 211,490.00 USD |
| `1D` | `719.30` | 5,590,000.00 USD | 5,590,000.00 USD | 0.00 USD | 126,360.00 USD | 177,910.00 USD | 306,040.00 USD |
| `7D` | `719.90` | 51,490,000.00 USD | 0.00 USD | 51,490,000.00 USD | 618,020.00 USD | 173,240.00 USD | 186,780.00 USD |
| `1D` | `720.20` | 5,790,000.00 USD | 5,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 194,350.00 USD |
| `7D` | `720.80` | 50,510,000.00 USD | 0.00 USD | 50,510,000.00 USD | 1,010,000.00 USD | 52,490.00 USD | 180,370.00 USD |
| `1D` | `721.10` | 5,990,000.00 USD | 5,990,000.00 USD | 0.00 USD | 0.00 USD | 204,540.00 USD | 0.00 USD |
| `7D` | `721.70` | 49,260,000.00 USD | 0.00 USD | 49,260,000.00 USD | 1,950,000.00 USD | 237,690.00 USD | 653,400.00 USD |
| `1D` | `722.00` | 6,070,000.00 USD | 6,070,000.00 USD | 0.00 USD | 0.00 USD | 78,640.00 USD | 0.00 USD |
| `7D` | `722.60` | 46,430,000.00 USD | 0.00 USD | 46,430,000.00 USD | 1,930,000.00 USD | 108,200.00 USD | 229,380.00 USD |
| `7D` | `723.50` | 44,160,000.00 USD | 0.00 USD | 44,160,000.00 USD | 640,550.00 USD | 140,550.00 USD | 293,670.00 USD |
| `1D` | `723.80` | 6,510,000.00 USD | 6,510,000.00 USD | 0.00 USD | 0.00 USD | 437,890.00 USD | 0.00 USD |
| `7D` | `724.40` | 43,080,000.00 USD | 0.00 USD | 43,080,000.00 USD | 663,550.00 USD | 186,780.00 USD | 130,770.00 USD |
| `7D` | `725.30` | 42,100,000.00 USD | 0.00 USD | 42,100,000.00 USD | 1,760,000.00 USD | 418,390.00 USD | 396,690.00 USD |
| `1D` | `725.60` | 6,560,000.00 USD | 6,560,000.00 USD | 0.00 USD | 0.00 USD | 57,080.00 USD | 0.00 USD |
| `7D` | `726.20` | 39,520,000.00 USD | 0.00 USD | 39,520,000.00 USD | 1,060,000.00 USD | 311,550.00 USD | 460,020.00 USD |
| `1D` | `726.50` | 6,630,000.00 USD | 6,630,000.00 USD | 0.00 USD | 0.00 USD | 64,470.00 USD | 0.00 USD |
| `7D` | `727.10` | 37,690,000.00 USD | 0.00 USD | 37,690,000.00 USD | 1,230,000.00 USD | 331,980.00 USD | 241,010.00 USD |
| `7D` | `728.00` | 35,890,000.00 USD | 0.00 USD | 35,890,000.00 USD | 3,110,000.00 USD | 778,750.00 USD | 388,930.00 USD |
| `7D` | `728.90` | 31,610,000.00 USD | 0.00 USD | 31,610,000.00 USD | 2,330,000.00 USD | 317,590.00 USD | 644,150.00 USD |
| `1D` | `729.20` | 7,500,000.00 USD | 7,500,000.00 USD | 0.00 USD | 0.00 USD | 256,940.00 USD | 616,880.00 USD |
| `7D` | `729.80` | 28,320,000.00 USD | 0.00 USD | 28,320,000.00 USD | 1,320,000.00 USD | 430,010.00 USD | 339,140.00 USD |
| `1D` | `730.10` | 9,290,000.00 USD | 9,290,000.00 USD | 0.00 USD | 1,690,000.00 USD | 24,020.00 USD | 73,220.00 USD |
| `7D` | `730.70` | 26,230,000.00 USD | 0.00 USD | 26,230,000.00 USD | 2,760,000.00 USD | 351,520.00 USD | 587,010.00 USD |
| `1D` | `731.00` | 12,410,000.00 USD | 12,410,000.00 USD | 0.00 USD | 1,090,000.00 USD | 152,870.00 USD | 1,880,000.00 USD |
| `7D` | `731.60` | 22,530,000.00 USD | 0.00 USD | 22,530,000.00 USD | 1,530,000.00 USD | 133,980.00 USD | 261,910.00 USD |
| `1D` | `731.90` | 12,840,000.00 USD | 12,840,000.00 USD | 0.00 USD | 0.00 USD | 82,570.00 USD | 347,120.00 USD |
| `7D` | `732.50` | 20,610,000.00 USD | 0.00 USD | 20,610,000.00 USD | 465,880.00 USD | 221,510.00 USD | 96,400.00 USD |
| `1D` | `732.80` | 15,130,000.00 USD | 15,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 134,420.00 USD | 1,020,000.00 USD |
| `7D` | `733.40` | 19,820,000.00 USD | 0.00 USD | 19,820,000.00 USD | 1,910,000.00 USD | 158,310.00 USD | 338,540.00 USD |
| `1D` | `733.70` | 15,830,000.00 USD | 15,830,000.00 USD | 0.00 USD | 344,230.00 USD | 210,140.00 USD | 153,020.00 USD |
| `7D` | `734.30` | 17,420,000.00 USD | 0.00 USD | 17,420,000.00 USD | 1,580,000.00 USD | 288,470.00 USD | 244,940.00 USD |
| `1D` | `734.60` | 16,430,000.00 USD | 16,430,000.00 USD | 0.00 USD | 460,890.00 USD | 42,070.00 USD | 97,180.00 USD |
| `7D` | `735.20` | 15,310,000.00 USD | 0.00 USD | 15,310,000.00 USD | 1,330,000.00 USD | 172,940.00 USD | 437,510.00 USD |
| `1D` | `735.50` | 18,070,000.00 USD | 18,070,000.00 USD | 0.00 USD | 813,660.00 USD | 227,070.00 USD | 590,930.00 USD |
| `7D` | `736.10` | 13,370,000.00 USD | 0.00 USD | 13,370,000.00 USD | 2,130,000.00 USD | 181,990.00 USD | 484,910.00 USD |
| `1D` | `736.40` | 18,800,000.00 USD | 18,800,000.00 USD | 0.00 USD | 736,640.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `737.00` | 10,570,000.00 USD | 0.00 USD | 10,570,000.00 USD | 2,360,000.00 USD | 175,330.00 USD | 633,690.00 USD |
| `1D` | `737.30` | 18,920,000.00 USD | 18,920,000.00 USD | 0.00 USD | 117,570.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `737.90` | 7,400,000.00 USD | 0.00 USD | 7,400,000.00 USD | 3,420,000.00 USD | 72,280.00 USD | 374,090.00 USD |
| `1D` | `738.20` | 19,290,000.00 USD | 19,290,000.00 USD | 0.00 USD | 210,200.00 USD | 162,750.00 USD | 0.00 USD |
| `7D` | `738.80` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 522,950.00 USD | 20,210.00 USD | 155,300.00 USD |
| `1D` | `739.10` | 20,950,000.00 USD | 20,950,000.00 USD | 0.00 USD | 726,150.00 USD | 0.00 USD | 934,700.00 USD |
| `7D` | `739.70` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 352,500.00 USD | 0.00 USD | 203,030.00 USD |
| `1D` | `740.00` | 21,670,000.00 USD | 21,670,000.00 USD | 0.00 USD | 697,550.00 USD | 0.00 USD | 15,020.00 USD |
| `7D` | `740.60` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 1,090,000.00 USD | 0.00 USD | 33,390.00 USD |
| `1D` | `740.90` | 22,380,000.00 USD | 22,380,000.00 USD | 0.00 USD | 546,620.00 USD | 166,390.00 USD | 0.00 USD |
| `7D` | `741.50` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 257,630.00 USD | 0.00 USD | 208,590.00 USD |
| `1D` | `741.80` | 22,690,000.00 USD | 22,690,000.00 USD | 0.00 USD | 313,800.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `742.40` | 689,850.00 USD | 0.00 USD | 689,850.00 USD | 0.00 USD | 0.00 USD | 183,920.00 USD |
| `7D` | `743.30` | 505,930.00 USD | 0.00 USD | 505,930.00 USD | 0.00 USD | 0.00 USD | 57,580.00 USD |
| `1D` | `743.60` | 23,250,000.00 USD | 23,250,000.00 USD | 0.00 USD | 120,950.00 USD | 0.00 USD | 436,560.00 USD |
| `7D` | `744.20` | 448,350.00 USD | 0.00 USD | 448,350.00 USD | 0.00 USD | 257,580.00 USD | 141,790.00 USD |
| `1D` | `744.50` | 24,130,000.00 USD | 24,130,000.00 USD | 0.00 USD | 771,380.00 USD | 106,580.00 USD | 0.00 USD |
| `7D` | `745.10` | 48,980.00 USD | 0.00 USD | 48,980.00 USD | 0.00 USD | 48,980.00 USD | 0.00 USD |
| `7D` | `745.20` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `745.40` | 25,460,000.00 USD | 25,460,000.00 USD | 0.00 USD | 473,600.00 USD | 0.00 USD | 854,020.00 USD |
| `7D` | `746.00` | 999,320.00 USD | 999,320.00 USD | 0.00 USD | 999,320.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `746.30` | 26,000,000.00 USD | 26,000,000.00 USD | 0.00 USD | 435,700.00 USD | 106,280.00 USD | 0.00 USD |
| `7D` | `746.90` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 215,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `747.20` | 27,250,000.00 USD | 27,250,000.00 USD | 0.00 USD | 428,210.00 USD | 67,980.00 USD | 758,780.00 USD |
| `1D` | `748.10` | 27,740,000.00 USD | 27,740,000.00 USD | 0.00 USD | 341,720.00 USD | 72,690.00 USD | 73,330.00 USD |
| `1D` | `749.00` | 28,150,000.00 USD | 28,150,000.00 USD | 0.00 USD | 404,680.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `749.90` | 28,300,000.00 USD | 28,300,000.00 USD | 0.00 USD | 157,570.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `750.80` | 28,340,000.00 USD | 28,340,000.00 USD | 0.00 USD | 33,990.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `751.70` | 28,810,000.00 USD | 28,810,000.00 USD | 0.00 USD | 53,980.00 USD | 25,010.00 USD | 393,600.00 USD |
| `1D` | `752.60` | 29,240,000.00 USD | 29,240,000.00 USD | 0.00 USD | 284,000.00 USD | 0.00 USD | 146,020.00 USD |
| `1D` | `753.50` | 29,550,000.00 USD | 29,550,000.00 USD | 0.00 USD | 47,700.00 USD | 3,810.00 USD | 262,160.00 USD |
| `1D` | `754.40` | 30,020,000.00 USD | 30,020,000.00 USD | 0.00 USD | 352,780.00 USD | 70,850.00 USD | 43,990.00 USD |
| `7D` | `755.00` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 59,560.00 USD | 0.00 USD |
| `1D` | `755.30` | 30,610,000.00 USD | 30,610,000.00 USD | 0.00 USD | 289,960.00 USD | 243,600.00 USD | 56,900.00 USD |
| `1D` | `756.20` | 31,100,000.00 USD | 31,100,000.00 USD | 0.00 USD | 406,880.00 USD | 35,830.00 USD | 46,440.00 USD |
| `7D` | `756.80` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 47,340.00 USD | 0.00 USD |
| `1D` | `757.10` | 31,510,000.00 USD | 31,510,000.00 USD | 0.00 USD | 223,780.00 USD | 122,240.00 USD | 63,690.00 USD |
| `7D` | `757.70` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 475,510.00 USD | 113,240.00 USD | 0.00 USD |
| `1D` | `758.00` | 31,970,000.00 USD | 31,970,000.00 USD | 0.00 USD | 369,420.00 USD | 67,700.00 USD | 18,080.00 USD |
| `7D` | `758.60` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `758.90` | 33,510,000.00 USD | 33,510,000.00 USD | 0.00 USD | 1,150,000.00 USD | 122,880.00 USD | 273,090.00 USD |
| `1D` | `759.80` | 33,930,000.00 USD | 33,930,000.00 USD | 0.00 USD | 371,250.00 USD | 21,070.00 USD | 22,840.00 USD |
| `7D` | `760.40` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 0.00 USD | 27,650.00 USD | 42,540.00 USD |
| `1D` | `760.70` | 34,490,000.00 USD | 34,490,000.00 USD | 0.00 USD | 354,030.00 USD | 94,530.00 USD | 113,560.00 USD |
| `7D` | `761.30` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 10,750.00 USD | 211,960.00 USD | 100,630.00 USD |
| `1D` | `761.60` | 35,710,000.00 USD | 35,710,000.00 USD | 0.00 USD | 778,030.00 USD | 87,560.00 USD | 353,890.00 USD |
| `7D` | `762.20` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 699,820.00 USD | 179,270.00 USD |
| `1D` | `762.50` | 36,660,000.00 USD | 36,660,000.00 USD | 0.00 USD | 650,310.00 USD | 184,600.00 USD | 117,630.00 USD |
| `7D` | `763.10` | 7,830,000.00 USD | 7,830,000.00 USD | 0.00 USD | 2,460,000.00 USD | 590,460.00 USD | 404,720.00 USD |
| `1D` | `763.40` | 39,720,000.00 USD | 39,720,000.00 USD | 0.00 USD | 2,300,000.00 USD | 203,280.00 USD | 554,280.00 USD |
| `7D` | `764.00` | 10,270,000.00 USD | 10,270,000.00 USD | 0.00 USD | 1,590,000.00 USD | 441,980.00 USD | 402,300.00 USD |
| `1D` | `764.30` | 41,790,000.00 USD | 41,790,000.00 USD | 0.00 USD | 1,610,000.00 USD | 153,350.00 USD | 304,950.00 USD |
| `7D` | `764.90` | 12,470,000.00 USD | 12,470,000.00 USD | 0.00 USD | 1,450,000.00 USD | 352,570.00 USD | 395,630.00 USD |
| `1D` | `765.20` | 42,720,000.00 USD | 42,720,000.00 USD | 0.00 USD | 609,290.00 USD | 223,440.00 USD | 95,370.00 USD |
| `7D` | `765.80` | 15,460,000.00 USD | 15,460,000.00 USD | 0.00 USD | 2,470,000.00 USD | 107,550.00 USD | 416,290.00 USD |
| `1D` | `766.10` | 44,360,000.00 USD | 44,360,000.00 USD | 0.00 USD | 1,030,000.00 USD | 216,550.00 USD | 399,250.00 USD |
| `7D` | `766.70` | 20,050,000.00 USD | 20,050,000.00 USD | 0.00 USD | 3,330,000.00 USD | 416,530.00 USD | 842,330.00 USD |
| `1D` | `767.00` | 46,790,000.00 USD | 46,790,000.00 USD | 0.00 USD | 2,020,000.00 USD | 104,660.00 USD | 306,540.00 USD |
| `7D` | `767.60` | 23,430,000.00 USD | 23,430,000.00 USD | 0.00 USD | 2,790,000.00 USD | 123,530.00 USD | 467,840.00 USD |
| `1D` | `767.90` | 48,750,000.00 USD | 48,750,000.00 USD | 0.00 USD | 1,530,000.00 USD | 124,080.00 USD | 308,200.00 USD |
| `7D` | `768.50` | 25,660,000.00 USD | 25,660,000.00 USD | 0.00 USD | 1,840,000.00 USD | 95,830.00 USD | 281,920.00 USD |
| `1D` | `768.80` | 49,670,000.00 USD | 49,670,000.00 USD | 0.00 USD | 782,650.00 USD | 54,840.00 USD | 76,340.00 USD |
| `7D` | `769.40` | 26,810,000.00 USD | 26,810,000.00 USD | 0.00 USD | 565,780.00 USD | 249,950.00 USD | 333,550.00 USD |
| `1D` | `769.70` | 50,440,000.00 USD | 50,440,000.00 USD | 0.00 USD | 591,420.00 USD | 111,680.00 USD | 69,960.00 USD |
| `7D` | `770.30` | 29,310,000.00 USD | 29,310,000.00 USD | 0.00 USD | 1,900,000.00 USD | 240,530.00 USD | 364,650.00 USD |
| `1D` | `770.60` | 51,150,000.00 USD | 51,150,000.00 USD | 0.00 USD | 295,710.00 USD | 95,060.00 USD | 316,530.00 USD |
| `7D` | `771.20` | 30,770,000.00 USD | 30,770,000.00 USD | 0.00 USD | 1,050,000.00 USD | 242,570.00 USD | 162,680.00 USD |
| `1D` | `771.50` | 52,600,000.00 USD | 52,600,000.00 USD | 0.00 USD | 604,710.00 USD | 144,120.00 USD | 705,810.00 USD |
| `7D` | `772.10` | 33,190,000.00 USD | 33,190,000.00 USD | 0.00 USD | 1,750,000.00 USD | 252,650.00 USD | 419,070.00 USD |
| `1D` | `772.40` | 53,200,000.00 USD | 53,200,000.00 USD | 0.00 USD | 418,600.00 USD | 148,190.00 USD | 33,620.00 USD |
| `7D` | `773.00` | 35,800,000.00 USD | 35,800,000.00 USD | 0.00 USD | 1,950,000.00 USD | 325,680.00 USD | 338,170.00 USD |
| `1D` | `773.30` | 54,450,000.00 USD | 54,450,000.00 USD | 0.00 USD | 976,860.00 USD | 92,850.00 USD | 181,550.00 USD |
| `7D` | `773.90` | 37,600,000.00 USD | 37,600,000.00 USD | 0.00 USD | 1,220,000.00 USD | 276,760.00 USD | 293,960.00 USD |
| `1D` | `774.20` | 55,520,000.00 USD | 55,520,000.00 USD | 0.00 USD | 983,640.00 USD | 62,410.00 USD | 22,850.00 USD |
| `7D` | `774.80` | 39,980,000.00 USD | 39,980,000.00 USD | 0.00 USD | 1,310,000.00 USD | 568,930.00 USD | 502,710.00 USD |
| `1D` | `775.10` | 56,080,000.00 USD | 56,080,000.00 USD | 0.00 USD | 290,910.00 USD | 122,640.00 USD | 141,550.00 USD |
| `7D` | `775.70` | 42,470,000.00 USD | 42,470,000.00 USD | 0.00 USD | 1,830,000.00 USD | 470,960.00 USD | 187,170.00 USD |
| `1D` | `776.00` | 56,720,000.00 USD | 56,720,000.00 USD | 0.00 USD | 430,680.00 USD | 109,470.00 USD | 103,300.00 USD |
| `7D` | `776.60` | 44,740,000.00 USD | 44,740,000.00 USD | 0.00 USD | 1,630,000.00 USD | 269,050.00 USD | 378,590.00 USD |
| `1D` | `776.90` | 57,290,000.00 USD | 57,290,000.00 USD | 0.00 USD | 412,420.00 USD | 30,600.00 USD | 120,910.00 USD |
| `7D` | `777.50` | 46,480,000.00 USD | 46,480,000.00 USD | 0.00 USD | 1,350,000.00 USD | 243,990.00 USD | 148,450.00 USD |
| `1D` | `777.80` | 58,890,000.00 USD | 58,890,000.00 USD | 0.00 USD | 1,080,000.00 USD | 159,720.00 USD | 366,320.00 USD |
| `7D` | `778.40` | 48,170,000.00 USD | 48,170,000.00 USD | 0.00 USD | 1,180,000.00 USD | 307,370.00 USD | 206,530.00 USD |
| `1D` | `778.70` | 59,520,000.00 USD | 59,520,000.00 USD | 0.00 USD | 493,740.00 USD | 61,580.00 USD | 76,320.00 USD |
| `7D` | `779.30` | 49,730,000.00 USD | 49,730,000.00 USD | 0.00 USD | 1,240,000.00 USD | 188,170.00 USD | 123,650.00 USD |
| `1D` | `779.60` | 60,580,000.00 USD | 60,580,000.00 USD | 0.00 USD | 814,150.00 USD | 96,550.00 USD | 141,140.00 USD |
| `7D` | `780.20` | 51,100,000.00 USD | 51,100,000.00 USD | 0.00 USD | 1,070,000.00 USD | 86,470.00 USD | 218,750.00 USD |
| `1D` | `780.50` | 61,140,000.00 USD | 61,140,000.00 USD | 0.00 USD | 388,410.00 USD | 100,010.00 USD | 79,670.00 USD |
| `7D` | `781.10` | 52,710,000.00 USD | 52,710,000.00 USD | 0.00 USD | 1,270,000.00 USD | 90,990.00 USD | 242,450.00 USD |
| `1D` | `781.40` | 61,920,000.00 USD | 61,920,000.00 USD | 0.00 USD | 511,520.00 USD | 113,520.00 USD | 154,660.00 USD |
| `7D` | `782.00` | 54,610,000.00 USD | 54,610,000.00 USD | 0.00 USD | 1,510,000.00 USD | 87,670.00 USD | 301,190.00 USD |
| `1D` | `782.30` | 63,450,000.00 USD | 63,450,000.00 USD | 0.00 USD | 1,150,000.00 USD | 49,090.00 USD | 325,500.00 USD |
| `7D` | `782.90` | 56,600,000.00 USD | 56,600,000.00 USD | 0.00 USD | 1,750,000.00 USD | 36,140.00 USD | 202,700.00 USD |
| `1D` | `783.20` | 64,250,000.00 USD | 64,250,000.00 USD | 0.00 USD | 655,850.00 USD | 47,470.00 USD | 100,590.00 USD |
| `7D` | `783.80` | 57,170,000.00 USD | 57,170,000.00 USD | 0.00 USD | 508,000.00 USD | 10,100.00 USD | 54,380.00 USD |
| `1D` | `784.10` | 64,610,000.00 USD | 64,610,000.00 USD | 0.00 USD | 314,540.00 USD | 23,200.00 USD | 18,280.00 USD |
| `7D` | `784.70` | 57,480,000.00 USD | 57,480,000.00 USD | 0.00 USD | 208,380.00 USD | 28,260.00 USD | 70,300.00 USD |
| `1D` | `785.00` | 65,160,000.00 USD | 65,160,000.00 USD | 0.00 USD | 502,530.00 USD | 32,830.00 USD | 19,600.00 USD |
| `7D` | `785.60` | 58,610,000.00 USD | 58,610,000.00 USD | 0.00 USD | 1,010,000.00 USD | 54,140.00 USD | 71,180.00 USD |
| `1D` | `785.90` | 65,370,000.00 USD | 65,370,000.00 USD | 0.00 USD | 179,190.00 USD | 4,490.00 USD | 30,250.00 USD |
| `7D` | `786.50` | 59,000,000.00 USD | 59,000,000.00 USD | 0.00 USD | 329,230.00 USD | 30,660.00 USD | 23,970.00 USD |
| `1D` | `786.80` | 65,610,000.00 USD | 65,610,000.00 USD | 0.00 USD | 201,790.00 USD | 23,920.00 USD | 14,270.00 USD |
| `7D` | `787.40` | 59,580,000.00 USD | 59,580,000.00 USD | 0.00 USD | 470,050.00 USD | 17,630.00 USD | 91,050.00 USD |
| `1D` | `787.70` | 66,460,000.00 USD | 66,460,000.00 USD | 0.00 USD | 482,920.00 USD | 15,430.00 USD | 350,240.00 USD |
| `7D` | `788.30` | 59,940,000.00 USD | 59,940,000.00 USD | 0.00 USD | 202,630.00 USD | 82,380.00 USD | 81,230.00 USD |
| `1D` | `788.60` | 66,610,000.00 USD | 66,610,000.00 USD | 0.00 USD | 80,180.00 USD | 0.00 USD | 65,290.00 USD |
| `1D` | `789.00` | 66,830,000.00 USD | 66,830,000.00 USD | 0.00 USD | 220,550.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `789.20` | 60,780,000.00 USD | 60,780,000.00 USD | 0.00 USD | 698,830.00 USD | 81,250.00 USD | 55,990.00 USD |
| `7D` | `790.10` | 61,270,000.00 USD | 61,270,000.00 USD | 0.00 USD | 299,250.00 USD | 104,360.00 USD | 88,890.00 USD |
| `7D` | `791.00` | 62,150,000.00 USD | 62,150,000.00 USD | 0.00 USD | 693,290.00 USD | 82,870.00 USD | 100,420.00 USD |
| `7D` | `791.90` | 63,030,000.00 USD | 63,030,000.00 USD | 0.00 USD | 816,380.00 USD | 16,830.00 USD | 46,300.00 USD |
| `7D` | `792.80` | 63,250,000.00 USD | 63,250,000.00 USD | 0.00 USD | 205,450.00 USD | 0.00 USD | 14,670.00 USD |
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
  * Total Open Interest: `1.33B` | Total OI Tokens: `1,850,428.8 BNB`
  * 1h OI Change: `+1.33%` | 4h OI Change: `-2.26%` | 24h OI Change: `+8.05%`
  * Exchange Breakdown: Binance=`578.10M` | Bybit=`135.22M` | OKX=`66.11M` | Hyperliquid=`74.05M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-140.78K` | Last 24h: `-51.15K` | Last 3d: `142.23K` | Last 7d: `346.08K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0000%` | **USDT OKX** | `-0.0609%` |
| **USDT Bybit** | `-0.0758%` | **USDT KuCoin** | `-0.0168%` |
| **USDT MEXC** | `0.0000%` | **USDT BingX** | `0.0050%` |
| **USDT Gate** | `0.0023%` | **USDT Bitget** | `-0.0035%` |
| **CoinM Binance** | `0.1217%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `BNB` | `58.00%` | `42.00%` | `1.38` | 51,500,000.00 USD |
| `15M` | `Binance` | `53.59%` | `46.41%` | `1.15` | 17,110,000.00 USD |
| `15M` | `OKX` | `58.89%` | `41.11%` | `1.43` | 5,010,000.00 USD |
| `15M` | `Bybit` | `61.84%` | `38.16%` | `1.62` | 8,810,000.00 USD |
| `15M` | `KuCoin` | `28.44%` | `71.56%` | `0.40` | 605,280.00 USD |
| `15M` | `Gate` | `57.47%` | `42.53%` | `1.35` | 3,200,000.00 USD |
| `15M` | `Bitget` | `58.23%` | `41.77%` | `1.39` | 3,090,000.00 USD |
| `15M` | `BingX` | `63.42%` | `36.58%` | `1.73` | 666,250.00 USD |
| `15M` | `MEXC` | `56.37%` | `43.63%` | `1.29` | 8,830,000.00 USD |
| `15M` | `Bitunix` | `56.05%` | `43.95%` | `1.28` | 1,330,000.00 USD |
| `15M` | `Hyperliquid` | `82.54%` | `17.46%` | `4.73` | 1,470,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `70.41%` | `29.59%` | `2.38` | 190,640.00 USD |
| `15M` | `Crypto.com` | `53.06%` | `46.94%` | `1.13` | 100,690.00 USD |
| `15M` | `WhiteBIT` | `99.32%` | `0.68%` | `146.06` | 805,530.00 USD |
| `15M` | `HTX` | `67.97%` | `32.03%` | `2.12` | 41,870.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `52.82%` | `47.18%` | `1.12` | 177,140.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `41.4%` | `58.6%` | `0.71` | 70,090.00 USD |
| `15M` | `Whale Positions` | `53.59%` | `46.41%` | `1.15` | 17,110,000.00 USD |
| `15M` | `Global Accounts` | `58.00%` | `42.00%` | `1.38` | 51,500,000.00 USD |
| `1H` | `BNB` | `54.11%` | `45.89%` | `1.18` | 345,650,000.00 USD |
| `1H` | `Binance` | `54.3%` | `45.7%` | `1.19` | 112,000,000.00 USD |
| `1H` | `OKX` | `55.15%` | `44.85%` | `1.23` | 71,400,000.00 USD |
| `1H` | `Bybit` | `53.25%` | `46.75%` | `1.14` | 33,040,000.00 USD |
| `1H` | `KuCoin` | `51.49%` | `48.51%` | `1.06` | 3,060,000.00 USD |
| `1H` | `Gate` | `51.74%` | `48.26%` | `1.07` | 20,640,000.00 USD |
| `1H` | `Bitget` | `48.57%` | `51.43%` | `0.94` | 13,030,000.00 USD |
| `1H` | `BingX` | `38.65%` | `61.35%` | `0.63` | 13,100,000.00 USD |
| `1H` | `MEXC` | `56.16%` | `43.84%` | `1.28` | 26,450,000.00 USD |
| `1H` | `Bitunix` | `54.65%` | `45.35%` | `1.21` | 18,580,000.00 USD |
| `1H` | `Hyperliquid` | `62.84%` | `37.16%` | `1.69` | 18,920,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `48.72%` | `51.28%` | `0.95` | 3,160,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 530,170.00 USD |
| `1H` | `WhiteBIT` | `21.55%` | `78.45%` | `0.27` | 3,240,000.00 USD |
| `1H` | `HTX` | `38.76%` | `61.24%` | `0.63` | 653,740.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `100%` | `0.00` | 19,020.00 USD |
| `1H` | `Aster` | `50.68%` | `49.32%` | `1.03` | 4,310,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `57.08%` | `42.92%` | `1.33` | 3,500,000.00 USD |
| `1H` | `Whale Positions` | `54.3%` | `45.7%` | `1.19` | 112,000,000.00 USD |
| `1H` | `Global Accounts` | `54.11%` | `45.89%` | `1.18` | 345,650,000.00 USD |
| `4H` | `BNB` | `49.06%` | `50.94%` | `0.96` | 2,540,000,000.00 USD |
| `4H` | `Binance` | `49.16%` | `50.84%` | `0.97` | 889,450,000.00 USD |
| `4H` | `OKX` | `46.57%` | `53.43%` | `0.87` | 465,780,000.00 USD |
| `4H` | `Bybit` | `53.4%` | `46.6%` | `1.15` | 231,760,000.00 USD |
| `4H` | `KuCoin` | `55.79%` | `44.21%` | `1.26` | 38,730,000.00 USD |
| `4H` | `Gate` | `47.4%` | `52.6%` | `0.90` | 124,560,000.00 USD |
| `4H` | `Bitget` | `49.98%` | `50.02%` | `1.00` | 105,670,000.00 USD |
| `4H` | `BingX` | `39.15%` | `60.85%` | `0.64` | 118,780,000.00 USD |
| `4H` | `MEXC` | `52.19%` | `47.81%` | `1.09` | 225,610,000.00 USD |
| `4H` | `Bitunix` | `51.78%` | `48.22%` | `1.07` | 106,260,000.00 USD |
| `4H` | `Hyperliquid` | `49.94%` | `50.06%` | `1.00` | 127,650,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.47%` | `50.53%` | `0.98` | 26,990,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 5,620,000.00 USD |
| `4H` | `WhiteBIT` | `29.71%` | `70.29%` | `0.42` | 15,370,000.00 USD |
| `4H` | `HTX` | `47%` | `53%` | `0.89` | 5,200,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `64.27%` | `35.73%` | `1.80` | 10,200,000.00 USD |
| `4H` | `Aster` | `49.05%` | `50.95%` | `0.96` | 20,150,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `30.5%` | `69.5%` | `0.44` | 25,960,000.00 USD |
| `4H` | `Whale Positions` | `49.16%` | `50.84%` | `0.97` | 889,450,000.00 USD |
| `4H` | `Global Accounts` | `49.06%` | `50.94%` | `0.96` | 2,540,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `698.25` | `699.83` | `698.25` | `703.95` | `696.75` | 26,130,732.92 USD | 11,452,791.24 USD | 14,677,941.68 USD | -3,225,150.44 USD | `-12.34%` | `1B / 0S` |
| `0:00 UTC` | `702.15` | `705.20` | `702.15` | `709.95` | `700.95` | 29,227,520.74 USD | 13,415,473.28 USD | 15,812,047.46 USD | -2,396,574.18 USD | `-8.20%` | `2B / 1S` |
| `5:00 UTC` | `709.05` | `711.18` | `709.05` | `715.35` | `708.15` | 27,008,888.92 USD | 11,488,761.44 USD | 15,520,127.48 USD | -4,031,366.04 USD | `-14.93%` | `0B / 1S` |
| `0:00 UTC` | `714.45` | `714.56` | `714.45` | `715.95` | `712.95` | 20,381,456.18 USD | 9,116,486.18 USD | 11,264,970.00 USD | -2,148,483.82 USD | `-10.54%` | `0B / 1S` |
| `5:00 UTC` | `711.15` | `711.54` | `711.15` | `714.45` | `709.95` | 13,903,836.91 USD | 6,352,852.84 USD | 7,550,984.08 USD | -1,198,131.24 USD | `-8.62%` | `1B / 4S` |
| `0:00 UTC` | `711.75` | `711.23` | `711.75` | `712.95` | `708.45` | 13,559,921.70 USD | 6,659,796.80 USD | 6,900,124.90 USD | -240,328.10 USD | `-1.77%` | `1B / 4S` |
| `5:00 UTC` | `708.45` | `709.07` | `708.45` | `710.55` | `708.15` | 7,713,838.94 USD | 3,792,445.03 USD | 3,921,393.91 USD | -128,948.88 USD | `-1.67%` | `0B / 0S` |
| `0:00 UTC` | `717.15` | `715.03` | `717.15` | `717.45` | `709.35` | 18,001,107.25 USD | 10,590,792.94 USD | 7,410,314.32 USD | 3,180,478.62 USD | `+17.67%` | `10B / 0S` |
| `5:00 UTC` | `718.65` | `718.30` | `718.65` | `719.85` | `716.85` | 14,406,892.83 USD | 6,892,738.14 USD | 7,514,154.69 USD | -621,416.55 USD | `-4.31%` | `1B / 0S` |
| `0:00 UTC` | `718.95` | `719.22` | `718.95` | `719.55` | `718.95` | 244,740.52 USD | 126,726.54 USD | 118,013.97 USD | 8,712.57 USD | `+3.56%` | `1B / 1S` |

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
| `5m` | -28,480.00 USD | 310,830.00 USD | **`ACCUMULATION`** |
| `15m` | -91,330.00 USD | 5,670,000.00 USD | **`ACCUMULATION`** |
| `30m` | 836,430.00 USD | 5,970,000.00 USD | **`ACCUMULATION`** |
| `1h` | 2,230,000.00 USD | 6,880,000.00 USD | **`ACCUMULATION`** |
| `2h` | -1,520,000.00 USD | -4,780,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -8,630,000.00 USD | -13,680,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -12,110,000.00 USD | -14,370,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -27,160,000.00 USD | -56,920,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -29,740,000.00 USD | -61,980,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -29,440,000.00 USD | -77,050,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -58,400,000.00 USD | -107,790,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -156,140,000.00 USD | -429,840,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-28.48K` | 15m=`-91.33K` | 1h=`+2.23M` | 24h=`-29.44M`
* Futures Capital Netflows: 5m=`+310.83K` | 15m=`+5.67M` | 1h=`+6.88M` | 24h=`-77.05M`
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
  * `2026-10-30 09:09:56 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:33:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:32:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:28:56 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:27:56 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:27:56 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:29:56 IST`: [economics.td.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `691.08` (Risk Distance: `6.95` pts)
  * +2.5R Take Profit: `715.40`
  * Mathematical Lot Sizing: **`1.43 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `714.32` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `721.27` (Risk Distance: `6.95` pts)
  * +2.5R Take Profit: `696.95`
  * Mathematical Lot Sizing: **`1.43 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`721.22`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
