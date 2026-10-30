# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BNB
**Canonical Key**: `BNB` | **Broker Instrument**: `BNBUSD.p` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 09:01:01 IST` (`2026-10-30 03:31:01 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `704.90` | **Live Ask Quote**: `708.10` | **Mid Price**: `706.50`
- **Spread Points**: `320.00` | **Spread BPS**: `45.29 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `696.30` | VWAP Z-Score: `+1.04` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `7.43` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `48.71` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `721.04` | Lower -3.00σ Band: `671.57`
  * Upper +2.51σ Band: `717.00` | Lower -2.51σ Band: `675.61`
  * Upper +2.01σ Band: `712.87` | Lower -2.01σ Band: `679.73`
  * Upper +2.00σ Band: `712.79` | Lower -2.00σ Band: `679.81`
  * Upper +1.28σ Band: `706.86` | Lower -1.28σ Band: `685.75`
  * Upper +1.00σ Band: `704.55` | Lower -1.00σ Band: `688.06`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`703.51` | EMA-20=`703.83` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`715.33` (Slope: `+0.0000`) | EMA-100=`727.01`
  * Institutional Anchors: EMA-144=`731.90` | EMA-200=`734.87` (Slope: `-0.6156`) | EMA-233=`736.07`
- **Range Boundaries**: 24H High=`758.10` | 24H Low=`677.20` | Weekly High=`760.90` | Weekly Low=`677.20`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `714.01` (Distance: `-1.05%`)
  * Point of Control (POC) = `706.94` (Distance: `-0.06%`)
  * Value Area Low (VAL) = `697.42` (Distance: `+1.30%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`754.57` | POC=`744.11` | VAL=`738.60`
  * Prior Day Extremes: PDH=`759.80` | PDL=`677.20` | PDC=`696.20`
  * Monday Range Blueprint: High=`746.00` | Mid=`738.45` | Low=`730.90`
  * Developing Weekly Value Area: Weekly VAH=`751.69` | Weekly POC=`740.53` | Weekly VAL=`734.95`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`724.00` | Low=`677.90`
  * London Session (08:00-16:00 UTC): High=`709.33` | Low=`703.67`
  * New York Session (13:00-21:00 UTC): High=`710.74` | Low=`702.26`
  * Initial Balance (First Hour): IB High=`708.62` | IB Low=`704.38`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `703.67` - `709.33`
  * Optimal Trade Entry (OTE 0.705): `707.91`
  * Structural Invalidation Anchor (0.786): `712.15`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `711.17` | `711.49` | `710.34` | `710.56` | `3,254` | 2,313,224.83 USD | -46,056.73 USD | `-1.99%` | -41,002,446.46 USD | `+0.64` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `710.57` | `712.91` | `710.34` | `711.30` | `6,624` | 4,714,007.43 USD | 1,489,893.85 USD | `+31.61%` | -39,512,552.61 USD | `+1.61` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `711.30` | `712.20` | `710.43` | `712.00` | `4,759` | 3,385,510.50 USD | -378,488.61 USD | `-11.18%` | -39,891,041.22 USD | `+0.20` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `714.41` | `715.85` | `712.91` | `714.34` | `28,523` | 20,381,456.18 USD | -2,148,483.82 USD | `-10.54%` | -38,896,384.20 USD | `-0.42` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `714.33` | `714.34` | `710.00` | `710.56` | `19,541` | 13,903,836.91 USD | -1,198,131.24 USD | `-8.62%` | -40,094,515.44 USD | `-0.01` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `710.57` | `712.91` | `710.34` | `712.00` | `11,383` | 8,099,517.93 USD | 1,111,405.25 USD | `+13.72%` | -38,983,110.19 USD | `+0.77` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `696.33` | `704.02` | `691.00` | `702.98` | `140,981` | 98,470,359.76 USD | -8,456,832.77 USD | `-8.59%` | -29,398,036.53 USD | `-0.74` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `702.99` | `715.85` | `701.01` | `710.56` | `127,490` | 90,521,702.76 USD | -9,774,555.27 USD | `-10.80%` | -39,172,591.80 USD | `-0.84` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `710.57` | `712.91` | `710.34` | `712.02` | `11,403` | 8,113,380.57 USD | 1,125,225.17 USD | `+13.87%` | -38,047,366.63 USD | `+0.27` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `750.62` | `754.90` | `743.07` | `745.33` | `88,414` | 66,199,547.89 USD | 232,195.88 USD | `+0.35%` | -10,302,756.17 USD | `+0.38` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `745.34` | `745.53` | `677.76` | `697.96` | `1,556,116` | 1,101,338,590.19 USD | -7,502,511.31 USD | `-0.68%` | -17,805,267.48 USD | `-0.58` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `697.96` | `715.85` | `681.03` | `712.20` | `461,007` | 322,229,413.72 USD | -20,229,615.71 USD | `-6.28%` | -38,034,883.19 USD | `-1.58` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `748.51` | `753.57` | `738.70` | `740.45` | `333,019` | 248,636,999.78 USD | -10,340,292.49 USD | `-4.16%` | -18,580,450.49 USD | `-1.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `740.45` | `753.64` | `739.55` | `750.62` | `148,938` | 111,099,080.67 USD | 8,045,498.44 USD | `+7.24%` | -10,534,952.05 USD | `+1.41` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `750.62` | `754.90` | `743.07` | `745.33` | `88,414` | 66,199,547.89 USD | 232,195.88 USD | `+0.35%` | -10,302,756.17 USD | `+0.38` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `745.34` | `745.53` | `677.76` | `697.96` | `1,556,116` | 1,101,338,590.19 USD | -7,502,511.31 USD | `-0.68%` | -17,805,267.48 USD | `-0.58` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `697.96` | `715.85` | `681.03` | `712.20` | `461,007` | 322,229,413.72 USD | -20,229,615.71 USD | `-6.28%` | -38,034,883.19 USD | `-1.58` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| --- | **`706.50`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `707.66` | `3209000000.0000` | 2,270.88 USD | 94,603.76 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `707.68` | `25495000000.0000` | 18,042.30 USD | 92,332.88 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `707.69` | `18840000000.0000` | 13,332.88 USD | 74,290.58 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `707.70` | `699000000.0000` | 494.68 USD | 60,957.70 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `707.72` | `15699000000.0000` | 11,110.50 USD | 60,463.02 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `707.73` | `2356000000.0000` | 1,667.41 USD | 49,352.52 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `707.75` | `25492000000.0000` | 18,041.96 USD | 47,685.11 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `707.77` | `699000000.0000` | 494.73 USD | 29,643.14 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `707.78` | `699000000.0000` | 494.74 USD | 29,148.41 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `707.79` | `338000000.0000` | 239.23 USD | 28,653.67 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `707.80` | `4618000000.0000` | 3,268.62 USD | 28,414.44 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `707.82` | `2832000000.0000` | 2,004.55 USD | 25,145.82 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `707.85` | `2356000000.0000` | 1,667.69 USD | 23,141.27 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `707.86` | `12557000000.0000` | 8,888.60 USD | 21,473.58 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `707.87` | `702000000.0000` | 496.92 USD | 12,584.98 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `707.88` | `698000000.0000` | 494.10 USD | 12,088.06 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `707.93` | `4489000000.0000` | 3,177.90 USD | 11,593.96 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `707.94` | `9417000000.0000` | 6,666.67 USD | 8,416.06 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `707.95` | `1000000000.0000` | 707.95 USD | 1,749.39 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `707.98` | `1471000000.0000` | 1,041.44 USD | 1,041.44 USD | `2 orders` | `-0.00%` | `-` |
| `ASK` | `707.99` | `2845000000.0000` | 2,014.23 USD | 2,014.23 USD | `3 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `707.99` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 707.99` | `0.00%` | `-` |
| `ASK` | `708.04` | `4348000000.0000` | 3,078.56 USD | 5,092.79 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `708.05` | `699000000.0000` | 494.93 USD | 5,587.72 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `708.12` | `526000000.0000` | 372.47 USD | 5,960.19 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `708.16` | `450000000.0000` | 318.67 USD | 6,278.86 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `708.17` | `7027000000.0000` | 4,976.31 USD | 11,255.17 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `708.18` | `710000000.0000` | 502.81 USD | 11,757.98 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `708.21` | `5328000000.0000` | 3,773.34 USD | 15,531.32 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `708.22` | `150000000.0000` | 106.23 USD | 15,637.55 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `708.23` | `1707000000.0000` | 1,208.95 USD | 16,846.50 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `708.24` | `300000000.0000` | 212.47 USD | 17,058.97 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `708.28` | `4355000000.0000` | 3,084.56 USD | 20,143.53 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `708.29` | `297000000.0000` | 210.36 USD | 20,353.90 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `708.30` | `581000000.0000` | 411.52 USD | 20,765.42 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `708.31` | `150000000.0000` | 106.25 USD | 20,871.66 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `708.32` | `7721000000.0000` | 5,468.94 USD | 26,340.60 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `708.33` | `702000000.0000` | 497.25 USD | 26,837.85 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `708.34` | `851000000.0000` | 602.80 USD | 27,440.65 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `708.37` | `300000000.0000` | 212.51 USD | 27,653.16 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `708.38` | `1793000000.0000` | 1,270.13 USD | 28,923.28 USD | `1 orders` | `+0.06%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 08:53:31 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `780` | `0xea00...a918` | `LONG` | 2,907,560.78 USD | `4,098,429,000,000.00` | `787.24` | `709.11` | `0.000000` | -318,866.00 USD | `-10.97%` | `5X Cross` |
| `867` | `0x7d0c...1b28` | `LONG` | 2,610,890.74 USD | `3,680,473,000,000.00` | `703.37` | `709.11` | `0.000000` | 22,141.76 USD | `+0.85%` | `10X Cross` |
| `901` | `0xfe7c...b7ae` | `LONG` | 2,477,038.53 USD | `3,491,575,000,000.00` | `686.05` | `709.11` | `0.000000` | 81,627.67 USD | `+3.30%` | `10X Cross` |
| `1064` | `0x27c9...d65d` | `LONG` | 2,023,339.05 USD | `2,851,862,000,000.00` | `700.84` | `709.11` | `166.33` | 24,631.30 USD | `+1.22%` | `10X Cross` |
| `1166` | `0x7737...bf66` | `SHORT` | 1,874,420.89 USD | `2,646,179,000,000.00` | `752.73` | `709.11` | `6687.14` | 117,449.69 USD | `+6.27%` | `10X Cross` |
| `1350` | `0x51f6...2b39` | `LONG` | 1,589,348.13 USD | `2,241,992,000,000.00` | `703.00` | `709.11` | `87.53` | 13,237.95 USD | `+0.83%` | `10X Cross` |
| `1421` | `0x325e...9564` | `LONG` | 1,517,937.64 USD | `2,140,352,000,000.00` | `707.43` | `709.11` | `0.000000` | 3,781.59 USD | `+0.25%` | `10X Cross` |
| `1453` | `0xab04...8b69` | `SHORT` | 1,477,478.96 USD | `2,087,100,000,000.00` | `699.81` | `709.11` | `1104.44` | -16,907.95 USD | `-1.14%` | `10X Cross` |
| `1477` | `0xc675...795d` | `LONG` | 1,455,810.84 USD | `2,055,214,000,000.00` | `706.91` | `709.11` | `640.94` | 2,966.17 USD | `+0.20%` | `10X Cross` |
| `1501` | `0x2edd...8179` | `LONG` | 1,429,661.35 USD | `2,019,367,000,000.00` | `714.56` | `709.11` | `0.000000` | -13,300.04 USD | `-0.93%` | `10X Cross` |
| `1683` | `0x07fd...689d` | `LONG` | 1,237,051.89 USD | `1,744,292,000,000.00` | `714.40` | `709.11` | `0.000000` | -9,080.14 USD | `-0.73%` | `10X Cross` |
| `1690` | `0x4420...4c4b` | `LONG` | 1,227,622.47 USD | `1,730,313,000,000.00` | `704.02` | `709.11` | `269.89` | 9,448.09 USD | `+0.77%` | `10X Cross` |
| `1698` | `0x645b...87b8` | `LONG` | 1,221,622.76 USD | `1,721,990,000,000.00` | `747.34` | `709.11` | `0.000000` | -65,284.66 USD | `-5.34%` | `10X Cross` |
| `1819` | `0xfc27...9d9d` | `LONG` | 1,118,797.17 USD | `1,578,149,000,000.00` | `700.69` | `709.11` | `0.000000` | 13,004.05 USD | `+1.16%` | `10X Cross` |
| `1826` | `0xa4a6...46cf` | `SHORT` | 1,110,911.07 USD | `1,565,914,000,000.00` | `711.66` | `709.11` | `1765.08` | 3,492.20 USD | `+0.31%` | `10X Cross` |
| `1877` | `0x14c6...b280` | `SHORT` | 1,064,080.50 USD | `1,500,000,000,000.00` | `712.51` | `709.11` | `1462.48` | 4,681.20 USD | `+0.44%` | `10X Cross` |
| `1944` | `0xbf5a...88ba` | `SHORT` | 1,018,670.47 USD | `1,439,105,000,000.00` | `718.16` | `709.11` | `1942.64` | 14,836.47 USD | `+1.46%` | `10X Cross` |
| `1981` | `0x646b...01dc` | `SHORT` | 1,001,624.51 USD | `1,412,868,000,000.00` | `699.26` | `709.11` | `1300.05` | -13,655.51 USD | `-1.36%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`758.29` (Vol: 2,900,000.00 USD, Dist: `+7.08%`) | Long MP=`677.19` (Vol: 3,100,000.00 USD, Dist: `--4.37%`)
  * 48H Horizon: Short MP=`767.93` (Vol: 3,000,000.00 USD, Dist: `+8.44%`) | Long MP=`677.29` (Vol: 3,100,000.00 USD, Dist: `--4.36%`)
  * 3D Horizon: Short MP=`767.93` (Vol: 3,400,000.00 USD, Dist: `+8.44%`) | Long MP=`677.29` (Vol: 3,100,000.00 USD, Dist: `--4.36%`)
  * 7D Horizon: Short MP=`767.93` (Vol: 3,500,000.00 USD, Dist: `+8.44%`) | Long MP=`677.29` (Vol: 3,100,000.00 USD, Dist: `--4.36%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `141.50` | 5,520.00 USD | 6,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Long` | `141.50` | 6,120,000.00 USD | 0.00 USD | 5,520.00 USD | `-80.06%` | `38,980,000,000.00` |
| `Live` | `Long` | `143.50` | 6,120,000.00 USD | 0.00 USD | 2,870.00 USD | `-79.78%` | `20,000,000,000.00` |
| `Live` | `Long` | `149.50` | 6,110,000.00 USD | 0.00 USD | 5,100.00 USD | `-78.93%` | `34,129,000,000.00` |
| `Live` | `Long` | `153.50` | 6,110,000.00 USD | 0.00 USD | 294.11 USD | `-78.37%` | `1,916,000,000.00` |
| `Live` | `Long` | `158.50` | 6,110,000.00 USD | 0.00 USD | 2,220.00 USD | `-77.67%` | `14,000,000,000.00` |
| `Live` | `Long` | `163.50` | 6,110,000.00 USD | 0.00 USD | 468,590.00 USD | `-76.96%` | `2,865,992,000,000.00` |
| `Live` | `Long` | `168.50` | 5,640,000.00 USD | 0.00 USD | 101,100.00 USD | `-76.26%` | `600,000,000,000.00` |
| `Live` | `Long` | `178.50` | 5,540,000.00 USD | 0.00 USD | 1,320.00 USD | `-74.85%` | `7,394,000,000.00` |
| `Live` | `Long` | `183.50` | 5,540,000.00 USD | 0.00 USD | 6,220.00 USD | `-74.14%` | `33,907,000,000.00` |
| `Live` | `Long` | `190.50` | 5,530,000.00 USD | 0.00 USD | 759.71 USD | `-73.16%` | `3,988,000,000.00` |
| `Live` | `Long` | `200.50` | 5,530,000.00 USD | 0.00 USD | 608.52 USD | `-71.75%` | `3,035,000,000.00` |
| `Live` | `Long` | `207.50` | 5,530,000.00 USD | 0.00 USD | 102.09 USD | `-70.76%` | `492,000,000.00` |
| `Live` | `Long` | `208.50` | 5,530,000.00 USD | 0.00 USD | 20,850.00 USD | `-70.62%` | `100,000,000,000.00` |
| `Live` | `Long` | `213.50` | 5,510,000.00 USD | 0.00 USD | 108.24 USD | `-69.92%` | `507,000,000.00` |
| `Live` | `Long` | `214.50` | 5,510,000.00 USD | 0.00 USD | 388.03 USD | `-69.78%` | `1,809,000,000.00` |
| `Live` | `Long` | `219.50` | 5,510,000.00 USD | 0.00 USD | 191.18 USD | `-69.07%` | `871,000,000.00` |
| `Live` | `Long` | `228.50` | 5,510,000.00 USD | 0.00 USD | 17,450.00 USD | `-67.80%` | `76,375,000,000.00` |
| `Live` | `Long` | `244.50` | 5,490,000.00 USD | 0.00 USD | 1,290.00 USD | `-65.55%` | `5,281,000,000.00` |
| `Live` | `Long` | `258.50` | 5,490,000.00 USD | 0.00 USD | 7,010.00 USD | `-63.58%` | `27,108,000,000.00` |
| `Live` | `Long` | `259.50` | 5,480,000.00 USD | 0.00 USD | 738.80 USD | `-63.43%` | `2,847,000,000.00` |
| `Live` | `Long` | `267.50` | 5,480,000.00 USD | 0.00 USD | 462,860.00 USD | `-62.31%` | `1,730,313,000,000.00` |
| `Live` | `Long` | `269.50` | 5,020,000.00 USD | 0.00 USD | 21,360.00 USD | `-62.03%` | `79,269,000,000.00` |
| `Live` | `Long` | `283.50` | 5,000,000.00 USD | 0.00 USD | 283,500.00 USD | `-60.05%` | `1,000,000,000,000.00` |
| `Live` | `Long` | `292.50` | 4,710,000.00 USD | 0.00 USD | 9,350.00 USD | `-58.78%` | `31,975,000,000.00` |
| `Live` | `Long` | `298.50` | 4,700,000.00 USD | 0.00 USD | 148,320.00 USD | `-57.94%` | `496,876,000,000.00` |
| `Live` | `Long` | `300.50` | 4,550,000.00 USD | 0.00 USD | 457.06 USD | `-57.66%` | `1,521,000,000.00` |
| `Live` | `Long` | `312.50` | 4,550,000.00 USD | 0.00 USD | 500.00 USD | `-55.97%` | `1,600,000,000.00` |
| `Live` | `Long` | `326.50` | 4,550,000.00 USD | 0.00 USD | 500.85 USD | `-53.99%` | `1,534,000,000.00` |
| `Live` | `Long` | `327.50` | 4,550,000.00 USD | 0.00 USD | 314.07 USD | `-53.85%` | `959,000,000.00` |
| `Live` | `Long` | `328.50` | 4,550,000.00 USD | 0.00 USD | 133.70 USD | `-53.71%` | `407,000,000.00` |
| `Live` | `Long` | `332.50` | 4,550,000.00 USD | 0.00 USD | 150.29 USD | `-53.15%` | `452,000,000.00` |
| `Live` | `Long` | `333.50` | 4,550,000.00 USD | 0.00 USD | 226.45 USD | `-53.01%` | `679,000,000.00` |
| `Live` | `Long` | `337.50` | 4,550,000.00 USD | 0.00 USD | 135,000.00 USD | `-52.44%` | `400,000,000,000.00` |
| `Live` | `Long` | `339.50` | 4,420,000.00 USD | 0.00 USD | 417.25 USD | `-52.16%` | `1,229,000,000.00` |
| `Live` | `Long` | `342.50` | 4,420,000.00 USD | 0.00 USD | 650.75 USD | `-51.74%` | `1,900,000,000.00` |
| `Live` | `Long` | `347.50` | 4,420,000.00 USD | 0.00 USD | 9,580.00 USD | `-51.03%` | `27,554,000,000.00` |
| `Live` | `Long` | `349.50` | 4,410,000.00 USD | 0.00 USD | 6,840.00 USD | `-50.75%` | `19,558,000,000.00` |
| `Live` | `Long` | `350.50` | 4,400,000.00 USD | 0.00 USD | 14,990.00 USD | `-50.61%` | `42,767,000,000.00` |
| `Live` | `Long` | `351.50` | 4,380,000.00 USD | 0.00 USD | 124.08 USD | `-50.47%` | `353,000,000.00` |
| `Live` | `Long` | `352.50` | 4,380,000.00 USD | 0.00 USD | 24,480.00 USD | `-50.33%` | `69,447,000,000.00` |
| `Live` | `Long` | `354.50` | 4,360,000.00 USD | 0.00 USD | 11,800.00 USD | `-50.05%` | `33,296,000,000.00` |
| `Live` | `Long` | `355.50` | 4,350,000.00 USD | 0.00 USD | 529.34 USD | `-49.91%` | `1,489,000,000.00` |
| `Live` | `Long` | `356.50` | 4,350,000.00 USD | 0.00 USD | 3,570.00 USD | `-49.77%` | `10,019,000,000.00` |
| `Live` | `Long` | `359.50` | 4,340,000.00 USD | 0.00 USD | 212.10 USD | `-49.34%` | `590,000,000.00` |
| `Live` | `Long` | `363.50` | 4,340,000.00 USD | 0.00 USD | 340.60 USD | `-48.78%` | `937,000,000.00` |
| `Live` | `Long` | `366.50` | 4,340,000.00 USD | 0.00 USD | 549.75 USD | `-48.36%` | `1,500,000,000.00` |
| `Live` | `Long` | `367.50` | 4,340,000.00 USD | 0.00 USD | 146.63 USD | `-48.22%` | `399,000,000.00` |
| `Live` | `Long` | `368.50` | 4,340,000.00 USD | 0.00 USD | 15,810.00 USD | `-48.08%` | `42,904,000,000.00` |
| `Live` | `Long` | `369.50` | 4,330,000.00 USD | 0.00 USD | 1,660.00 USD | `-47.94%` | `4,504,000,000.00` |
| `Live` | `Long` | `371.50` | 4,330,000.00 USD | 0.00 USD | 146.37 USD | `-47.65%` | `394,000,000.00` |
| `Live` | `Long` | `372.50` | 4,330,000.00 USD | 0.00 USD | 11,560.00 USD | `-47.51%` | `31,029,000,000.00` |
| `Live` | `Long` | `374.50` | 4,310,000.00 USD | 0.00 USD | 1,820.00 USD | `-47.23%` | `4,868,000,000.00` |
| `Live` | `Long` | `377.50` | 4,310,000.00 USD | 0.00 USD | 1,400.00 USD | `-46.81%` | `3,716,000,000.00` |
| `Live` | `Long` | `378.50` | 4,310,000.00 USD | 0.00 USD | 643.45 USD | `-46.67%` | `1,700,000,000.00` |
| `Live` | `Long` | `381.50` | 4,310,000.00 USD | 0.00 USD | 1,910.00 USD | `-46.24%` | `5,000,000,000.00` |
| `Live` | `Long` | `382.50` | 4,310,000.00 USD | 0.00 USD | 12,070.00 USD | `-46.10%` | `31,561,000,000.00` |
| `Live` | `Long` | `383.50` | 4,300,000.00 USD | 0.00 USD | 7,290.00 USD | `-45.96%` | `19,000,000,000.00` |
| `Live` | `Long` | `384.50` | 4,290,000.00 USD | 0.00 USD | 1,060.00 USD | `-45.82%` | `2,746,000,000.00` |
| `Live` | `Long` | `385.50` | 4,290,000.00 USD | 0.00 USD | 19,150.00 USD | `-45.68%` | `49,675,000,000.00` |
| `Live` | `Long` | `386.50` | 4,270,000.00 USD | 0.00 USD | 531.44 USD | `-45.54%` | `1,375,000,000.00` |
| `Live` | `Long` | `387.50` | 4,270,000.00 USD | 0.00 USD | 392.54 USD | `-45.40%` | `1,013,000,000.00` |
| `Live` | `Long` | `393.50` | 4,270,000.00 USD | 0.00 USD | 536.73 USD | `-44.55%` | `1,364,000,000.00` |
| `Live` | `Long` | `394.50` | 4,270,000.00 USD | 0.00 USD | 168.06 USD | `-44.41%` | `426,000,000.00` |
| `Live` | `Long` | `395.50` | 4,270,000.00 USD | 0.00 USD | 2,110.00 USD | `-44.27%` | `5,347,000,000.00` |
| `Live` | `Long` | `396.50` | 4,260,000.00 USD | 0.00 USD | 317.20 USD | `-44.13%` | `800,000,000.00` |
| `Live` | `Long` | `398.50` | 4,260,000.00 USD | 0.00 USD | 626.84 USD | `-43.85%` | `1,573,000,000.00` |
| `Live` | `Long` | `399.50` | 4,260,000.00 USD | 0.00 USD | 603.64 USD | `-43.71%` | `1,511,000,000.00` |
| `Live` | `Long` | `404.50` | 4,260,000.00 USD | 0.00 USD | 102.34 USD | `-43.00%` | `253,000,000.00` |
| `Live` | `Long` | `409.50` | 4,260,000.00 USD | 0.00 USD | 613.02 USD | `-42.30%` | `1,497,000,000.00` |
| `Live` | `Long` | `410.50` | 4,260,000.00 USD | 0.00 USD | 105.91 USD | `-42.16%` | `258,000,000.00` |
| `Live` | `Long` | `412.50` | 4,260,000.00 USD | 0.00 USD | 1,750.00 USD | `-41.88%` | `4,250,000,000.00` |
| `Live` | `Long` | `413.50` | 4,260,000.00 USD | 0.00 USD | 14,890.00 USD | `-41.74%` | `36,017,000,000.00` |
| `Live` | `Long` | `414.50` | 4,250,000.00 USD | 0.00 USD | 1,890.00 USD | `-41.59%` | `4,566,000,000.00` |
| `Live` | `Long` | `415.50` | 4,240,000.00 USD | 0.00 USD | 1,810.00 USD | `-41.45%` | `4,368,000,000.00` |
| `Live` | `Long` | `417.50` | 4,240,000.00 USD | 0.00 USD | 7,140.00 USD | `-41.17%` | `17,092,000,000.00` |
| `Live` | `Long` | `418.50` | 4,230,000.00 USD | 0.00 USD | 318.06 USD | `-41.03%` | `760,000,000.00` |
| `Live` | `Long` | `419.50` | 4,230,000.00 USD | 0.00 USD | 2,650.00 USD | `-40.89%` | `6,316,000,000.00` |
| `Live` | `Long` | `421.50` | 4,230,000.00 USD | 0.00 USD | 2,320.00 USD | `-40.61%` | `5,496,000,000.00` |
| `Live` | `Long` | `422.50` | 4,230,000.00 USD | 0.00 USD | 62,760.00 USD | `-40.47%` | `148,556,000,000.00` |
| `Live` | `Long` | `428.50` | 4,170,000.00 USD | 0.00 USD | 30,660.00 USD | `-39.62%` | `71,547,000,000.00` |
| `Live` | `Long` | `429.50` | 4,140,000.00 USD | 0.00 USD | 846.12 USD | `-39.48%` | `1,970,000,000.00` |
| `Live` | `Long` | `431.50` | 4,140,000.00 USD | 0.00 USD | 612.73 USD | `-39.20%` | `1,420,000,000.00` |
| `Live` | `Long` | `436.50` | 4,130,000.00 USD | 0.00 USD | 133.13 USD | `-38.49%` | `305,000,000.00` |
| `Live` | `Long` | `437.50` | 4,130,000.00 USD | 0.00 USD | 2,380.00 USD | `-38.35%` | `5,431,000,000.00` |
| `Live` | `Long` | `438.50` | 4,130,000.00 USD | 0.00 USD | 1,790.00 USD | `-38.21%` | `4,087,000,000.00` |
| `Live` | `Long` | `442.50` | 4,130,000.00 USD | 0.00 USD | 33,410.00 USD | `-37.65%` | `75,511,000,000.00` |
| `Live` | `Long` | `444.50` | 4,100,000.00 USD | 0.00 USD | 4,510.00 USD | `-37.37%` | `10,149,000,000.00` |
| `Live` | `Long` | `448.50` | 4,090,000.00 USD | 0.00 USD | 3,350.00 USD | `-36.80%` | `7,470,000,000.00` |
| `Live` | `Long` | `452.50` | 4,090,000.00 USD | 0.00 USD | 957.04 USD | `-36.24%` | `2,115,000,000.00` |
| `Live` | `Long` | `456.50` | 4,090,000.00 USD | 0.00 USD | 4,730.00 USD | `-35.68%` | `10,359,000,000.00` |
| `Live` | `Long` | `459.50` | 4,080,000.00 USD | 0.00 USD | 38,210.00 USD | `-35.25%` | `83,150,000,000.00` |
| `Live` | `Long` | `463.50` | 4,050,000.00 USD | 0.00 USD | 199.31 USD | `-34.69%` | `430,000,000.00` |
| `Live` | `Long` | `464.50` | 4,040,000.00 USD | 0.00 USD | 396.68 USD | `-34.55%` | `854,000,000.00` |
| `Live` | `Long` | `469.50` | 4,040,000.00 USD | 0.00 USD | 4,370.00 USD | `-33.84%` | `9,301,000,000.00` |
| `Live` | `Long` | `470.50` | 4,040,000.00 USD | 0.00 USD | 674.23 USD | `-33.70%` | `1,433,000,000.00` |
| `Live` | `Long` | `475.50` | 4,040,000.00 USD | 0.00 USD | 5,320.00 USD | `-33.00%` | `11,182,000,000.00` |
| `Live` | `Long` | `477.50` | 4,030,000.00 USD | 0.00 USD | 1,560.00 USD | `-32.72%` | `3,259,000,000.00` |
| `Live` | `Long` | `481.50` | 4,030,000.00 USD | 0.00 USD | 615.36 USD | `-32.15%` | `1,278,000,000.00` |
| `Live` | `Long` | `482.50` | 4,030,000.00 USD | 0.00 USD | 6,840.00 USD | `-32.01%` | `14,184,000,000.00` |
| `Live` | `Long` | `483.50` | 4,030,000.00 USD | 0.00 USD | 8,500.00 USD | `-31.87%` | `17,576,000,000.00` |
| `Live` | `Long` | `484.50` | 4,020,000.00 USD | 0.00 USD | 2,840.00 USD | `-31.73%` | `5,864,000,000.00` |
| `Live` | `Long` | `485.50` | 4,010,000.00 USD | 0.00 USD | 2,400.00 USD | `-31.59%` | `4,947,000,000.00` |
| `Live` | `Long` | `487.50` | 4,010,000.00 USD | 0.00 USD | 464.59 USD | `-31.31%` | `953,000,000.00` |
| `Live` | `Long` | `488.50` | 4,010,000.00 USD | 0.00 USD | 2,300.00 USD | `-31.17%` | `4,712,000,000.00` |
| `Live` | `Long` | `491.50` | 4,010,000.00 USD | 0.00 USD | 1,080.00 USD | `-30.74%` | `2,197,000,000.00` |
| `Live` | `Long` | `493.50` | 4,010,000.00 USD | 0.00 USD | 3,940.00 USD | `-30.46%` | `7,988,000,000.00` |
| `Live` | `Long` | `498.50` | 4,000,000.00 USD | 0.00 USD | 1,820.00 USD | `-29.76%` | `3,656,000,000.00` |
| `Live` | `Long` | `499.50` | 4,000,000.00 USD | 0.00 USD | 13,310.00 USD | `-29.62%` | `26,644,000,000.00` |
| `Live` | `Long` | `501.50` | 3,990,000.00 USD | 0.00 USD | 7,760.00 USD | `-29.34%` | `15,482,000,000.00` |
| `Live` | `Long` | `502.50` | 3,980,000.00 USD | 0.00 USD | 109.04 USD | `-29.19%` | `217,000,000.00` |
| `Live` | `Long` | `504.50` | 3,980,000.00 USD | 0.00 USD | 288.07 USD | `-28.91%` | `571,000,000.00` |
| `Live` | `Long` | `505.50` | 3,980,000.00 USD | 0.00 USD | 5,760.00 USD | `-28.77%` | `11,387,000,000.00` |
| `Live` | `Long` | `508.50` | 3,970,000.00 USD | 0.00 USD | 992.08 USD | `-28.35%` | `1,951,000,000.00` |
| `Live` | `Long` | `509.50` | 3,970,000.00 USD | 0.00 USD | 44,080.00 USD | `-28.21%` | `86,523,000,000.00` |
| `Live` | `Long` | `510.50` | 3,930,000.00 USD | 0.00 USD | 4,080.00 USD | `-28.07%` | `8,000,000,000.00` |
| `Live` | `Long` | `511.50` | 3,930,000.00 USD | 0.00 USD | 5,180.00 USD | `-27.93%` | `10,118,000,000.00` |
| `Live` | `Long` | `513.50` | 3,920,000.00 USD | 0.00 USD | 2,520.00 USD | `-27.64%` | `4,914,000,000.00` |
| `Live` | `Long` | `514.50` | 3,920,000.00 USD | 0.00 USD | 701.78 USD | `-27.50%` | `1,364,000,000.00` |
| `Live` | `Long` | `515.50` | 3,920,000.00 USD | 0.00 USD | 81,170.00 USD | `-27.36%` | `157,465,000,000.00` |
| `Live` | `Long` | `516.50` | 3,840,000.00 USD | 0.00 USD | 481.89 USD | `-27.22%` | `933,000,000.00` |
| `Live` | `Long` | `517.50` | 3,840,000.00 USD | 0.00 USD | 22,650.00 USD | `-27.08%` | `43,765,000,000.00` |
| `Live` | `Long` | `519.50` | 3,810,000.00 USD | 0.00 USD | 968.35 USD | `-26.80%` | `1,864,000,000.00` |
| `Live` | `Long` | `520.50` | 3,810,000.00 USD | 0.00 USD | 272.22 USD | `-26.66%` | `523,000,000.00` |
| `Live` | `Long` | `521.50` | 3,810,000.00 USD | 0.00 USD | 838.05 USD | `-26.52%` | `1,607,000,000.00` |
| `Live` | `Long` | `522.50` | 3,810,000.00 USD | 0.00 USD | 2,090.00 USD | `-26.38%` | `3,993,000,000.00` |
| `Live` | `Long` | `524.50` | 3,810,000.00 USD | 0.00 USD | 833.43 USD | `-26.09%` | `1,589,000,000.00` |
| `Live` | `Long` | `526.50` | 3,810,000.00 USD | 0.00 USD | 1,700.00 USD | `-25.81%` | `3,234,000,000.00` |
| `Live` | `Long` | `529.50` | 3,810,000.00 USD | 0.00 USD | 42,820.00 USD | `-25.39%` | `80,869,000,000.00` |
| `Live` | `Long` | `530.50` | 3,760,000.00 USD | 0.00 USD | 18,050.00 USD | `-25.25%` | `34,028,000,000.00` |
| `Live` | `Long` | `531.50` | 3,750,000.00 USD | 0.00 USD | 484.73 USD | `-25.11%` | `912,000,000.00` |
| `Live` | `Long` | `532.50` | 3,740,000.00 USD | 0.00 USD | 422.81 USD | `-24.97%` | `794,000,000.00` |
| `Live` | `Long` | `534.50` | 3,740,000.00 USD | 0.00 USD | 555.35 USD | `-24.69%` | `1,039,000,000.00` |
| `Live` | `Long` | `535.50` | 3,740,000.00 USD | 0.00 USD | 100.14 USD | `-24.54%` | `187,000,000.00` |
| `Live` | `Long` | `536.50` | 3,740,000.00 USD | 0.00 USD | 183,580.00 USD | `-24.40%` | `342,188,000,000.00` |
| `Live` | `Long` | `537.50` | 3,560,000.00 USD | 0.00 USD | 769.70 USD | `-24.26%` | `1,432,000,000.00` |
| `Live` | `Long` | `539.50` | 3,560,000.00 USD | 0.00 USD | 490.94 USD | `-23.98%` | `910,000,000.00` |
| `Live` | `Long` | `540.50` | 3,560,000.00 USD | 0.00 USD | 2,130.00 USD | `-23.84%` | `3,944,000,000.00` |
| `Live` | `Long` | `541.50` | 3,560,000.00 USD | 0.00 USD | 65,690.00 USD | `-23.70%` | `121,304,000,000.00` |
| `Live` | `Long` | `543.50` | 3,490,000.00 USD | 0.00 USD | 2,680.00 USD | `-23.42%` | `4,927,000,000.00` |
| `Live` | `Long` | `544.50` | 3,490,000.00 USD | 0.00 USD | 210,830.00 USD | `-23.28%` | `387,204,000,000.00` |
| `Live` | `Long` | `545.50` | 3,280,000.00 USD | 0.00 USD | 1,580.00 USD | `-23.14%` | `2,900,000,000.00` |
| `Live` | `Long` | `546.50` | 3,280,000.00 USD | 0.00 USD | 874.40 USD | `-22.99%` | `1,600,000,000.00` |
| `Live` | `Long` | `548.50` | 3,270,000.00 USD | 0.00 USD | 1,980.00 USD | `-22.71%` | `3,611,000,000.00` |
| `Live` | `Long` | `549.50` | 3,270,000.00 USD | 0.00 USD | 1,370.00 USD | `-22.57%` | `2,496,000,000.00` |
| `Live` | `Long` | `550.50` | 3,270,000.00 USD | 0.00 USD | 633.63 USD | `-22.43%` | `1,151,000,000.00` |
| `Live` | `Long` | `551.50` | 3,270,000.00 USD | 0.00 USD | 1,250.00 USD | `-22.29%` | `2,271,000,000.00` |
| `Live` | `Long` | `552.50` | 3,270,000.00 USD | 0.00 USD | 24,120.00 USD | `-22.15%` | `43,665,000,000.00` |
| `Live` | `Long` | `553.50` | 3,250,000.00 USD | 0.00 USD | 3,080.00 USD | `-22.01%` | `5,565,000,000.00` |
| `Live` | `Long` | `556.50` | 3,240,000.00 USD | 0.00 USD | 5,670.00 USD | `-21.59%` | `10,193,000,000.00` |
| `Live` | `Long` | `557.50` | 3,240,000.00 USD | 0.00 USD | 10,020.00 USD | `-21.44%` | `17,967,000,000.00` |
| `Live` | `Long` | `558.50` | 3,230,000.00 USD | 0.00 USD | 212.23 USD | `-21.30%` | `380,000,000.00` |
| `Live` | `Long` | `560.50` | 3,230,000.00 USD | 0.00 USD | 582.36 USD | `-21.02%` | `1,039,000,000.00` |
| `Live` | `Long` | `562.50` | 3,230,000.00 USD | 0.00 USD | 67,470.00 USD | `-20.74%` | `119,940,000,000.00` |
| `Live` | `Long` | `564.50` | 3,160,000.00 USD | 0.00 USD | 33,490.00 USD | `-20.46%` | `59,330,000,000.00` |
| `Live` | `Long` | `568.50` | 3,120,000.00 USD | 0.00 USD | 454.80 USD | `-19.89%` | `800,000,000.00` |
| `Live` | `Long` | `569.50` | 3,120,000.00 USD | 0.00 USD | 144.08 USD | `-19.75%` | `253,000,000.00` |
| `Live` | `Long` | `571.50` | 3,120,000.00 USD | 0.00 USD | 712,450.00 USD | `-19.47%` | `1,246,635,000,000.00` |
| `Live` | `Long` | `572.50` | 2,410,000.00 USD | 0.00 USD | 8,800.00 USD | `-19.33%` | `15,374,000,000.00` |
| `Live` | `Long` | `574.50` | 2,400,000.00 USD | 0.00 USD | 767.53 USD | `-19.05%` | `1,336,000,000.00` |
| `Live` | `Long` | `575.50` | 2,400,000.00 USD | 0.00 USD | 1,540.00 USD | `-18.91%` | `2,682,000,000.00` |
| `Live` | `Long` | `576.50` | 2,400,000.00 USD | 0.00 USD | 4,810.00 USD | `-18.77%` | `8,349,000,000.00` |
| `Live` | `Long` | `577.50` | 2,400,000.00 USD | 0.00 USD | 225,800.00 USD | `-18.63%` | `391,000,000,000.00` |
| `Live` | `Long` | `578.50` | 2,170,000.00 USD | 0.00 USD | 7,640.00 USD | `-18.49%` | `13,202,000,000.00` |
| `Live` | `Long` | `580.50` | 2,160,000.00 USD | 0.00 USD | 35,850.00 USD | `-18.20%` | `61,765,000,000.00` |
| `Live` | `Long` | `581.50` | 2,130,000.00 USD | 0.00 USD | 580.34 USD | `-18.06%` | `998,000,000.00` |
| `Live` | `Long` | `582.50` | 2,130,000.00 USD | 0.00 USD | 1,540.00 USD | `-17.92%` | `2,646,000,000.00` |
| `Live` | `Long` | `583.50` | 2,120,000.00 USD | 0.00 USD | 3,470.00 USD | `-17.78%` | `5,952,000,000.00` |
| `Live` | `Long` | `584.50` | 2,120,000.00 USD | 0.00 USD | 292.25 USD | `-17.64%` | `500,000,000.00` |
| `Live` | `Long` | `585.50` | 2,120,000.00 USD | 0.00 USD | 210.19 USD | `-17.50%` | `359,000,000.00` |
| `Live` | `Long` | `586.50` | 2,120,000.00 USD | 0.00 USD | 2,360.00 USD | `-17.36%` | `4,022,000,000.00` |
| `Live` | `Long` | `587.50` | 2,120,000.00 USD | 0.00 USD | 179,500.00 USD | `-17.22%` | `305,530,000,000.00` |
| `Live` | `Long` | `588.50` | 1,940,000.00 USD | 0.00 USD | 397.24 USD | `-17.08%` | `675,000,000.00` |
| `Live` | `Long` | `589.50` | 1,940,000.00 USD | 0.00 USD | 14,950.00 USD | `-16.94%` | `25,352,000,000.00` |
| `Live` | `Long` | `590.50` | 1,920,000.00 USD | 0.00 USD | 2,560.00 USD | `-16.79%` | `4,334,000,000.00` |
| `Live` | `Long` | `591.50` | 1,920,000.00 USD | 0.00 USD | 619.30 USD | `-16.65%` | `1,047,000,000.00` |
| `Live` | `Long` | `592.50` | 1,920,000.00 USD | 0.00 USD | 840.76 USD | `-16.51%` | `1,419,000,000.00` |
| `Live` | `Long` | `593.50` | 1,920,000.00 USD | 0.00 USD | 36,050.00 USD | `-16.37%` | `60,735,000,000.00` |
| `Live` | `Long` | `594.50` | 1,880,000.00 USD | 0.00 USD | 9,370.00 USD | `-16.23%` | `15,765,000,000.00` |
| `Live` | `Long` | `595.50` | 1,870,000.00 USD | 0.00 USD | 3,000.00 USD | `-16.09%` | `5,043,000,000.00` |
| `Live` | `Long` | `596.50` | 1,870,000.00 USD | 0.00 USD | 100.81 USD | `-15.95%` | `169,000,000.00` |
| `Live` | `Long` | `597.50` | 1,870,000.00 USD | 0.00 USD | 2,390.00 USD | `-15.81%` | `3,998,000,000.00` |
| `Live` | `Long` | `598.50` | 1,870,000.00 USD | 0.00 USD | 892.96 USD | `-15.67%` | `1,492,000,000.00` |
| `Live` | `Long` | `600.50` | 1,870,000.00 USD | 0.00 USD | 945.19 USD | `-15.39%` | `1,574,000,000.00` |
| `Live` | `Long` | `601.50` | 1,870,000.00 USD | 0.00 USD | 16,880.00 USD | `-15.24%` | `28,061,000,000.00` |
| `Live` | `Long` | `602.50` | 1,850,000.00 USD | 0.00 USD | 418.13 USD | `-15.10%` | `694,000,000.00` |
| `Live` | `Long` | `603.50` | 1,850,000.00 USD | 0.00 USD | 1,610.00 USD | `-14.96%` | `2,671,000,000.00` |
| `Live` | `Long` | `606.50` | 1,850,000.00 USD | 0.00 USD | 60,390.00 USD | `-14.54%` | `99,569,000,000.00` |
| `Live` | `Long` | `609.50` | 1,790,000.00 USD | 0.00 USD | 213.32 USD | `-14.12%` | `350,000,000.00` |
| `Live` | `Long` | `611.50` | 1,790,000.00 USD | 0.00 USD | 1,580.00 USD | `-13.84%` | `2,584,000,000.00` |
| `Live` | `Long` | `612.50` | 1,790,000.00 USD | 0.00 USD | 15,850.00 USD | `-13.69%` | `25,877,000,000.00` |
| `Live` | `Long` | `613.50` | 1,770,000.00 USD | 0.00 USD | 120.25 USD | `-13.55%` | `196,000,000.00` |
| `Live` | `Long` | `614.50` | 1,770,000.00 USD | 0.00 USD | 8,590.00 USD | `-13.41%` | `13,975,000,000.00` |
| `Live` | `Long` | `616.50` | 1,760,000.00 USD | 0.00 USD | 1,540.00 USD | `-13.13%` | `2,500,000,000.00` |
| `Live` | `Long` | `617.50` | 1,760,000.00 USD | 0.00 USD | 156.23 USD | `-12.99%` | `253,000,000.00` |
| `Live` | `Long` | `618.50` | 1,760,000.00 USD | 0.00 USD | 932.70 USD | `-12.85%` | `1,508,000,000.00` |
| `Live` | `Long` | `619.50` | 1,760,000.00 USD | 0.00 USD | 1,410.00 USD | `-12.71%` | `2,279,000,000.00` |
| `Live` | `Long` | `620.50` | 1,760,000.00 USD | 0.00 USD | 24,930.00 USD | `-12.57%` | `40,181,000,000.00` |
| `Live` | `Long` | `621.50` | 1,730,000.00 USD | 0.00 USD | 696.70 USD | `-12.43%` | `1,121,000,000.00` |
| `Live` | `Long` | `622.50` | 1,730,000.00 USD | 0.00 USD | 137.57 USD | `-12.29%` | `221,000,000.00` |
| `Live` | `Long` | `624.50` | 1,730,000.00 USD | 0.00 USD | 3,460.00 USD | `-12.00%` | `5,547,000,000.00` |
| `Live` | `Long` | `625.50` | 1,730,000.00 USD | 0.00 USD | 25,330.00 USD | `-11.86%` | `40,495,000,000.00` |
| `Live` | `Long` | `626.50` | 1,700,000.00 USD | 0.00 USD | 964.81 USD | `-11.72%` | `1,540,000,000.00` |
| `Live` | `Long` | `630.50` | 1,700,000.00 USD | 0.00 USD | 153.21 USD | `-11.16%` | `243,000,000.00` |
| `Live` | `Long` | `631.50` | 1,700,000.00 USD | 0.00 USD | 2,900.00 USD | `-11.02%` | `4,587,000,000.00` |
| `Live` | `Long` | `632.50` | 1,700,000.00 USD | 0.00 USD | 3,560.00 USD | `-10.88%` | `5,633,000,000.00` |
| `Live` | `Long` | `634.50` | 1,690,000.00 USD | 0.00 USD | 6,660.00 USD | `-10.59%` | `10,489,000,000.00` |
| `Live` | `Long` | `635.50` | 1,690,000.00 USD | 0.00 USD | 155.06 USD | `-10.45%` | `244,000,000.00` |
| `Live` | `Long` | `636.50` | 1,690,000.00 USD | 0.00 USD | 1,110.00 USD | `-10.31%` | `1,743,000,000.00` |
| `Live` | `Long` | `637.50` | 1,690,000.00 USD | 0.00 USD | 305.36 USD | `-10.17%` | `479,000,000.00` |
| `Live` | `Long` | `638.50` | 1,690,000.00 USD | 0.00 USD | 328.83 USD | `-10.03%` | `515,000,000.00` |
| `Live` | `Long` | `639.50` | 1,690,000.00 USD | 0.00 USD | 455.96 USD | `-9.89%` | `713,000,000.00` |
| `Live` | `Long` | `640.50` | 1,690,000.00 USD | 0.00 USD | 1,320,000.00 USD | `-9.75%` | `2,059,440,000,000.00` |
| `Live` | `Long` | `642.50` | 366,710.00 USD | 0.00 USD | 8,480.00 USD | `-9.47%` | `13,199,000,000.00` |
| `Live` | `Long` | `644.50` | 358,230.00 USD | 0.00 USD | 9,660.00 USD | `-9.19%` | `14,982,000,000.00` |
| `Live` | `Long` | `646.50` | 348,570.00 USD | 0.00 USD | 804.25 USD | `-8.90%` | `1,244,000,000.00` |
| `Live` | `Long` | `647.50` | 347,770.00 USD | 0.00 USD | 156.05 USD | `-8.76%` | `241,000,000.00` |
| `Live` | `Long` | `648.50` | 347,610.00 USD | 0.00 USD | 1,940.00 USD | `-8.62%` | `2,988,000,000.00` |
| `Live` | `Long` | `649.50` | 345,680.00 USD | 0.00 USD | 6,640.00 USD | `-8.48%` | `10,224,000,000.00` |
| `Live` | `Long` | `650.50` | 339,040.00 USD | 0.00 USD | 1,760.00 USD | `-8.34%` | `2,703,000,000.00` |
| `Live` | `Long` | `651.50` | 337,280.00 USD | 0.00 USD | 9,650.00 USD | `-8.20%` | `14,806,000,000.00` |
| `Live` | `Long` | `652.50` | 327,630.00 USD | 0.00 USD | 652.50 USD | `-8.06%` | `1,000,000,000.00` |
| `Live` | `Long` | `653.50` | 326,980.00 USD | 0.00 USD | 97,380.00 USD | `-7.92%` | `149,014,000,000.00` |
| `Live` | `Long` | `654.50` | 229,600.00 USD | 0.00 USD | 100.14 USD | `-7.78%` | `153,000,000.00` |
| `Live` | `Long` | `655.50` | 229,500.00 USD | 0.00 USD | 437.87 USD | `-7.64%` | `668,000,000.00` |
| `Live` | `Long` | `658.50` | 229,060.00 USD | 0.00 USD | 15,090.00 USD | `-7.21%` | `22,916,000,000.00` |
| `Live` | `Long` | `659.50` | 213,970.00 USD | 0.00 USD | 46,450.00 USD | `-7.07%` | `70,433,000,000.00` |
| `Live` | `Long` | `660.50` | 167,520.00 USD | 0.00 USD | 3,410.00 USD | `-6.93%` | `5,167,000,000.00` |
| `Live` | `Long` | `661.50` | 164,110.00 USD | 0.00 USD | 20,140.00 USD | `-6.79%` | `30,450,000,000.00` |
| `Live` | `Long` | `662.50` | 143,960.00 USD | 0.00 USD | 2,850.00 USD | `-6.65%` | `4,297,000,000.00` |
| `Live` | `Long` | `663.50` | 141,120.00 USD | 0.00 USD | 9,230.00 USD | `-6.51%` | `13,911,000,000.00` |
| `Live` | `Long` | `664.50` | 131,890.00 USD | 0.00 USD | 24,600.00 USD | `-6.37%` | `37,027,000,000.00` |
| `Live` | `Long` | `665.50` | 107,280.00 USD | 0.00 USD | 11,290.00 USD | `-6.23%` | `16,962,000,000.00` |
| `Live` | `Long` | `666.50` | 95,990.00 USD | 0.00 USD | 2,270.00 USD | `-6.09%` | `3,406,000,000.00` |
| `Live` | `Long` | `667.50` | 93,720.00 USD | 0.00 USD | 1,380.00 USD | `-5.94%` | `2,067,000,000.00` |
| `Live` | `Long` | `668.50` | 92,340.00 USD | 0.00 USD | 1,880.00 USD | `-5.80%` | `2,813,000,000.00` |
| `Live` | `Long` | `669.50` | 90,460.00 USD | 0.00 USD | 2,930.00 USD | `-5.66%` | `4,371,000,000.00` |
| `Live` | `Long` | `670.50` | 87,540.00 USD | 0.00 USD | 6,110.00 USD | `-5.52%` | `9,113,000,000.00` |
| `Live` | `Long` | `671.50` | 81,430.00 USD | 0.00 USD | 641.28 USD | `-5.38%` | `955,000,000.00` |
| `Live` | `Long` | `672.50` | 80,790.00 USD | 0.00 USD | 8,680.00 USD | `-5.24%` | `12,907,000,000.00` |
| `Live` | `Long` | `673.50` | 72,110.00 USD | 0.00 USD | 31,510.00 USD | `-5.10%` | `46,782,000,000.00` |
| `Live` | `Long` | `674.50` | 40,600.00 USD | 0.00 USD | 4,470.00 USD | `-4.96%` | `6,625,000,000.00` |
| `Live` | `Long` | `675.50` | 36,130.00 USD | 0.00 USD | 9,230.00 USD | `-4.82%` | `13,659,000,000.00` |
| `Live` | `Long` | `676.50` | 26,900.00 USD | 0.00 USD | 1,910.00 USD | `-4.68%` | `2,820,000,000.00` |
| `Live` | `Long` | `677.50` | 25,000.00 USD | 0.00 USD | 10,400.00 USD | `-4.54%` | `15,354,000,000.00` |
| `Live` | `Long` | `679.50` | 14,590.00 USD | 0.00 USD | 3,100.00 USD | `-4.25%` | `4,569,000,000.00` |
| `Live` | `Long` | `680.50` | 11,490.00 USD | 0.00 USD | 11,490.00 USD | `-4.11%` | `16,883,000,000.00` |
| `Live` | `Short` | `715.50` | 349.16 USD | 349.16 USD | 0.00 USD | `+0.82%` | `488,000,000.00` |
| `Live` | `Short` | `716.50` | 49,530.00 USD | 49,180.00 USD | 0.00 USD | `+0.96%` | `68,640,000,000.00` |
| `Live` | `Short` | `720.50` | 49,690.00 USD | 161.39 USD | 0.00 USD | `+1.52%` | `224,000,000.00` |
| `Live` | `Short` | `721.50` | 83,400.00 USD | 33,710.00 USD | 0.00 USD | `+1.66%` | `46,724,000,000.00` |
| `Live` | `Short` | `722.50` | 101,710.00 USD | 18,310.00 USD | 0.00 USD | `+1.81%` | `25,346,000,000.00` |
| `Live` | `Short` | `723.50` | 113,140.00 USD | 11,430.00 USD | 0.00 USD | `+1.95%` | `15,797,000,000.00` |
| `Live` | `Short` | `724.50` | 113,670.00 USD | 525.26 USD | 0.00 USD | `+2.09%` | `725,000,000.00` |
| `Live` | `Short` | `725.50` | 115,590.00 USD | 1,920.00 USD | 0.00 USD | `+2.23%` | `2,643,000,000.00` |
| `Live` | `Short` | `726.50` | 122,440.00 USD | 6,860.00 USD | 0.00 USD | `+2.37%` | `9,436,000,000.00` |
| `Live` | `Short` | `727.50` | 123,470.00 USD | 1,030.00 USD | 0.00 USD | `+2.51%` | `1,418,000,000.00` |
| `Live` | `Short` | `728.50` | 166,100.00 USD | 42,630.00 USD | 0.00 USD | `+2.65%` | `58,517,000,000.00` |
| `Live` | `Short` | `729.50` | 338,890.00 USD | 172,780.00 USD | 0.00 USD | `+2.79%` | `236,850,000,000.00` |
| `Live` | `Short` | `730.50` | 397,890.00 USD | 59,010.00 USD | 0.00 USD | `+2.93%` | `80,776,000,000.00` |
| `Live` | `Short` | `731.50` | 443,990.00 USD | 46,090.00 USD | 0.00 USD | `+3.07%` | `63,013,000,000.00` |
| `Live` | `Short` | `732.50` | 577,100.00 USD | 133,110.00 USD | 0.00 USD | `+3.21%` | `181,724,000,000.00` |
| `Live` | `Short` | `733.50` | 605,670.00 USD | 28,570.00 USD | 0.00 USD | `+3.35%` | `38,954,000,000.00` |
| `Live` | `Short` | `734.50` | 810,200.00 USD | 204,530.00 USD | 0.00 USD | `+3.50%` | `278,462,000,000.00` |
| `Live` | `Short` | `735.50` | 833,990.00 USD | 23,790.00 USD | 0.00 USD | `+3.64%` | `32,341,000,000.00` |
| `Live` | `Short` | `736.50` | 846,160.00 USD | 12,170.00 USD | 0.00 USD | `+3.78%` | `16,520,000,000.00` |
| `Live` | `Short` | `737.50` | 850,220.00 USD | 4,060.00 USD | 0.00 USD | `+3.92%` | `5,507,000,000.00` |
| `Live` | `Short` | `738.50` | 1,900,000.00 USD | 1,050,000.00 USD | 0.00 USD | `+4.06%` | `1,427,797,000,000.00` |
| `Live` | `Short` | `739.50` | 1,910,000.00 USD | 8,400.00 USD | 0.00 USD | `+4.20%` | `11,363,000,000.00` |
| `Live` | `Short` | `740.50` | 1,910,000.00 USD | 810.11 USD | 0.00 USD | `+4.34%` | `1,094,000,000.00` |
| `Live` | `Short` | `741.50` | 1,920,000.00 USD | 8,440.00 USD | 0.00 USD | `+4.48%` | `11,381,000,000.00` |
| `Live` | `Short` | `742.50` | 1,940,000.00 USD | 14,070.00 USD | 0.00 USD | `+4.62%` | `18,950,000,000.00` |
| `Live` | `Short` | `743.50` | 2,040,000.00 USD | 102,990.00 USD | 0.00 USD | `+4.76%` | `138,520,000,000.00` |
| `Live` | `Short` | `744.50` | 2,160,000.00 USD | 118,750.00 USD | 0.00 USD | `+4.90%` | `159,505,000,000.00` |
| `Live` | `Short` | `745.50` | 2,240,000.00 USD | 78,410.00 USD | 0.00 USD | `+5.05%` | `105,181,000,000.00` |
| `Live` | `Short` | `746.50` | 2,420,000.00 USD | 185,150.00 USD | 0.00 USD | `+5.19%` | `248,023,000,000.00` |
| `Live` | `Short` | `747.50` | 2,460,000.00 USD | 40,240.00 USD | 0.00 USD | `+5.33%` | `53,835,000,000.00` |
| `Live` | `Short` | `748.50` | 2,460,000.00 USD | 2,970.00 USD | 0.00 USD | `+5.47%` | `3,974,000,000.00` |
| `Live` | `Short` | `749.50` | 2,640,000.00 USD | 170,970.00 USD | 0.00 USD | `+5.61%` | `228,106,000,000.00` |
| `Live` | `Short` | `750.50` | 2,640,000.00 USD | 6,610.00 USD | 0.00 USD | `+5.75%` | `8,811,000,000.00` |
| `Live` | `Short` | `751.50` | 3,360,000.00 USD | 714,780.00 USD | 0.00 USD | `+5.89%` | `951,134,000,000.00` |
| `Live` | `Short` | `752.50` | 3,400,000.00 USD | 47,580.00 USD | 0.00 USD | `+6.03%` | `63,225,000,000.00` |
| `Live` | `Short` | `754.50` | 4,270,000.00 USD | 863,250.00 USD | 0.00 USD | `+6.31%` | `1,144,139,000,000.00` |
| `Live` | `Short` | `755.50` | 4,270,000.00 USD | 2,340.00 USD | 0.00 USD | `+6.45%` | `3,103,000,000.00` |
| `Live` | `Short` | `756.50` | 4,270,000.00 USD | 3,750.00 USD | 0.00 USD | `+6.60%` | `4,960,000,000.00` |
| `Live` | `Short` | `758.50` | 4,300,000.00 USD | 25,140.00 USD | 0.00 USD | `+6.88%` | `33,143,000,000.00` |
| `Live` | `Short` | `759.50` | 4,300,000.00 USD | 838.49 USD | 0.00 USD | `+7.02%` | `1,104,000,000.00` |
| `Live` | `Short` | `760.50` | 4,300,000.00 USD | 540.72 USD | 0.00 USD | `+7.16%` | `711,000,000.00` |
| `Live` | `Short` | `762.50` | 4,310,000.00 USD | 12,760.00 USD | 0.00 USD | `+7.44%` | `16,729,000,000.00` |
| `Live` | `Short` | `763.50` | 4,760,000.00 USD | 447,010.00 USD | 0.00 USD | `+7.58%` | `585,469,000,000.00` |
| `Live` | `Short` | `766.50` | 4,760,000.00 USD | 3,130.00 USD | 0.00 USD | `+8.00%` | `4,084,000,000.00` |
| `Live` | `Short` | `767.50` | 4,770,000.00 USD | 2,450.00 USD | 0.00 USD | `+8.15%` | `3,190,000,000.00` |
| `Live` | `Short` | `768.50` | 4,770,000.00 USD | 156.77 USD | 0.00 USD | `+8.29%` | `204,000,000.00` |
| `Live` | `Short` | `770.50` | 4,770,000.00 USD | 2,250.00 USD | 0.00 USD | `+8.57%` | `2,920,000,000.00` |
| `Live` | `Short` | `771.50` | 4,780,000.00 USD | 10,020.00 USD | 0.00 USD | `+8.71%` | `12,992,000,000.00` |
| `Live` | `Short` | `772.50` | 4,790,000.00 USD | 9,490.00 USD | 0.00 USD | `+8.85%` | `12,284,000,000.00` |
| `Live` | `Short` | `773.50` | 4,800,000.00 USD | 8,230.00 USD | 0.00 USD | `+8.99%` | `10,646,000,000.00` |
| `Live` | `Short` | `776.50` | 4,890,000.00 USD | 97,260.00 USD | 0.00 USD | `+9.41%` | `125,252,000,000.00` |
| `Live` | `Short` | `777.50` | 4,890,000.00 USD | 209.15 USD | 0.00 USD | `+9.55%` | `269,000,000.00` |
| `Live` | `Short` | `778.50` | 4,900,000.00 USD | 3,200.00 USD | 0.00 USD | `+9.70%` | `4,107,000,000.00` |
| `Live` | `Short` | `780.50` | 4,900,000.00 USD | 5,240.00 USD | 0.00 USD | `+9.98%` | `6,714,000,000.00` |
| `Live` | `Short` | `781.50` | 4,900,000.00 USD | 1,830.00 USD | 0.00 USD | `+10.12%` | `2,337,000,000.00` |
| `Live` | `Short` | `785.50` | 4,900,000.00 USD | 129.61 USD | 0.00 USD | `+10.68%` | `165,000,000.00` |
| `Live` | `Short` | `786.50` | 5,030,000.00 USD | 126,920.00 USD | 0.00 USD | `+10.82%` | `161,372,000,000.00` |
| `Live` | `Short` | `787.50` | 5,030,000.00 USD | 3,150.00 USD | 0.00 USD | `+10.96%` | `4,000,000,000.00` |
| `Live` | `Short` | `788.50` | 5,040,000.00 USD | 1,580.00 USD | 0.00 USD | `+11.10%` | `2,000,000,000.00` |
| `Live` | `Short` | `789.50` | 5,040,000.00 USD | 1,250.00 USD | 0.00 USD | `+11.25%` | `1,580,000,000.00` |
| `Live` | `Short` | `793.50` | 5,040,000.00 USD | 1,280.00 USD | 0.00 USD | `+11.81%` | `1,616,000,000.00` |
| `Live` | `Short` | `794.50` | 5,050,000.00 USD | 8,780.00 USD | 0.00 USD | `+11.95%` | `11,046,000,000.00` |
| `Live` | `Short` | `795.50` | 5,050,000.00 USD | 518.67 USD | 0.00 USD | `+12.09%` | `652,000,000.00` |
| `Live` | `Short` | `796.50` | 5,050,000.00 USD | 3,240.00 USD | 0.00 USD | `+12.23%` | `4,062,000,000.00` |
| `Live` | `Short` | `797.50` | 5,050,000.00 USD | 1,090.00 USD | 0.00 USD | `+12.37%` | `1,367,000,000.00` |
| `Live` | `Short` | `798.50` | 5,060,000.00 USD | 4,300.00 USD | 0.00 USD | `+12.51%` | `5,381,000,000.00` |
| `Live` | `Short` | `799.50` | 5,060,000.00 USD | 610.02 USD | 0.00 USD | `+12.65%` | `763,000,000.00` |
| `Live` | `Short` | `800.50` | 5,060,000.00 USD | 1,130.00 USD | 0.00 USD | `+12.80%` | `1,410,000,000.00` |
| `Live` | `Short` | `801.50` | 5,060,000.00 USD | 6,110.00 USD | 0.00 USD | `+12.94%` | `7,623,000,000.00` |
| `Live` | `Short` | `802.50` | 5,840,000.00 USD | 778,380.00 USD | 0.00 USD | `+13.08%` | `969,946,000,000.00` |
| `Live` | `Short` | `803.50` | 5,960,000.00 USD | 121,930.00 USD | 0.00 USD | `+13.22%` | `151,749,000,000.00` |
| `Live` | `Short` | `804.50` | 5,960,000.00 USD | 105.39 USD | 0.00 USD | `+13.36%` | `131,000,000.00` |
| `Live` | `Short` | `805.50` | 6,010,000.00 USD | 47,420.00 USD | 0.00 USD | `+13.50%` | `58,872,000,000.00` |
| `Live` | `Short` | `806.50` | 6,010,000.00 USD | 2,890.00 USD | 0.00 USD | `+13.64%` | `3,580,000,000.00` |
| `Live` | `Short` | `807.50` | 6,020,000.00 USD | 738.06 USD | 0.00 USD | `+13.78%` | `914,000,000.00` |
| `Live` | `Short` | `808.50` | 6,030,000.00 USD | 11,780.00 USD | 0.00 USD | `+13.92%` | `14,574,000,000.00` |
| `Live` | `Short` | `809.50` | 6,030,000.00 USD | 342.42 USD | 0.00 USD | `+14.06%` | `423,000,000.00` |
| `Live` | `Short` | `810.50` | 6,030,000.00 USD | 568.16 USD | 0.00 USD | `+14.20%` | `701,000,000.00` |
| `Live` | `Short` | `814.50` | 6,030,000.00 USD | 692.32 USD | 0.00 USD | `+14.77%` | `850,000,000.00` |
| `Live` | `Short` | `815.50` | 6,030,000.00 USD | 6,020.00 USD | 0.00 USD | `+14.91%` | `7,383,000,000.00` |
| `Live` | `Short` | `816.50` | 6,050,000.00 USD | 15,410.00 USD | 0.00 USD | `+15.05%` | `18,879,000,000.00` |
| `Live` | `Short` | `817.50` | 6,050,000.00 USD | 325.37 USD | 0.00 USD | `+15.19%` | `398,000,000.00` |
| `Live` | `Short` | `820.50` | 6,060,000.00 USD | 8,340.00 USD | 0.00 USD | `+15.61%` | `10,166,000,000.00` |
| `Live` | `Short` | `821.50` | 6,070,000.00 USD | 11,710.00 USD | 0.00 USD | `+15.75%` | `14,252,000,000.00` |
| `Live` | `Short` | `822.50` | 6,070,000.00 USD | 3,540.00 USD | 0.00 USD | `+15.90%` | `4,302,000,000.00` |
| `Live` | `Short` | `824.50` | 6,070,000.00 USD | 425.44 USD | 0.00 USD | `+16.18%` | `516,000,000.00` |
| `Live` | `Short` | `826.50` | 6,080,000.00 USD | 7,510.00 USD | 0.00 USD | `+16.46%` | `9,084,000,000.00` |
| `Live` | `Short` | `827.50` | 6,560,000.00 USD | 480,240.00 USD | 0.00 USD | `+16.60%` | `580,352,000,000.00` |
| `Live` | `Short` | `828.50` | 6,580,000.00 USD | 12,770.00 USD | 0.00 USD | `+16.74%` | `15,412,000,000.00` |
| `Live` | `Short` | `834.50` | 6,660,000.00 USD | 83,370.00 USD | 0.00 USD | `+17.59%` | `99,901,000,000.00` |
| `Live` | `Short` | `835.50` | 6,740,000.00 USD | 85,260.00 USD | 0.00 USD | `+17.73%` | `102,047,000,000.00` |
| `Live` | `Short` | `836.50` | 6,750,000.00 USD | 8,370.00 USD | 0.00 USD | `+17.87%` | `10,000,000,000.00` |
| `Live` | `Short` | `837.50` | 6,760,000.00 USD | 3,570.00 USD | 0.00 USD | `+18.01%` | `4,257,000,000.00` |
| `Live` | `Short` | `838.50` | 6,780,000.00 USD | 21,840.00 USD | 0.00 USD | `+18.15%` | `26,046,000,000.00` |
| `Live` | `Short` | `839.50` | 6,780,000.00 USD | 167.90 USD | 0.00 USD | `+18.29%` | `200,000,000.00` |
| `Live` | `Short` | `841.50` | 6,780,000.00 USD | 2,830.00 USD | 0.00 USD | `+18.57%` | `3,364,000,000.00` |
| `Live` | `Short` | `842.50` | 6,780,000.00 USD | 1,750.00 USD | 0.00 USD | `+18.71%` | `2,074,000,000.00` |
| `Live` | `Short` | `843.50` | 6,780,000.00 USD | 227.75 USD | 0.00 USD | `+18.85%` | `270,000,000.00` |
| `Live` | `Short` | `848.50` | 6,780,000.00 USD | 289.34 USD | 0.00 USD | `+19.56%` | `341,000,000.00` |
| `Live` | `Short` | `849.50` | 6,820,000.00 USD | 34,300.00 USD | 0.00 USD | `+19.70%` | `40,378,000,000.00` |
| `Live` | `Short` | `850.50` | 6,820,000.00 USD | 108.86 USD | 0.00 USD | `+19.84%` | `128,000,000.00` |
| `Live` | `Short` | `856.50` | 6,820,000.00 USD | 256.09 USD | 0.00 USD | `+20.69%` | `299,000,000.00` |
| `Live` | `Short` | `858.50` | 7,350,000.00 USD | 528,740.00 USD | 0.00 USD | `+20.97%` | `615,884,000,000.00` |
| `Live` | `Short` | `859.50` | 7,350,000.00 USD | 1,180.00 USD | 0.00 USD | `+21.11%` | `1,371,000,000.00` |
| `Live` | `Short` | `865.50` | 7,370,000.00 USD | 18,900.00 USD | 0.00 USD | `+21.95%` | `21,832,000,000.00` |
| `Live` | `Short` | `870.50` | 7,370,000.00 USD | 6,090.00 USD | 0.00 USD | `+22.66%` | `7,000,000,000.00` |
| `Live` | `Short` | `872.50` | 7,670,000.00 USD | 292,870.00 USD | 0.00 USD | `+22.94%` | `335,668,000,000.00` |
| `Live` | `Short` | `875.50` | 7,680,000.00 USD | 14,000.00 USD | 0.00 USD | `+23.36%` | `15,992,000,000.00` |
| `Live` | `Short` | `877.50` | 8,290,000.00 USD | 614,250.00 USD | 0.00 USD | `+23.65%` | `700,000,000,000.00` |
| `Live` | `Short` | `878.50` | 8,390,000.00 USD | 92,600.00 USD | 0.00 USD | `+23.79%` | `105,403,000,000.00` |
| `Live` | `Short` | `880.50` | 8,390,000.00 USD | 663.02 USD | 0.00 USD | `+24.07%` | `753,000,000.00` |
| `Live` | `Short` | `885.50` | 8,390,000.00 USD | 3,200.00 USD | 0.00 USD | `+24.77%` | `3,611,000,000.00` |
| `Live` | `Short` | `886.50` | 8,390,000.00 USD | 812.92 USD | 0.00 USD | `+24.91%` | `917,000,000.00` |
| `Live` | `Short` | `887.50` | 8,400,000.00 USD | 13,920.00 USD | 0.00 USD | `+25.05%` | `15,681,000,000.00` |
| `Live` | `Short` | `888.50` | 8,580,000.00 USD | 178,210.00 USD | 0.00 USD | `+25.20%` | `200,573,000,000.00` |
| `Live` | `Short` | `891.50` | 8,590,000.00 USD | 11,300.00 USD | 0.00 USD | `+25.62%` | `12,673,000,000.00` |
| `Live` | `Short` | `893.50` | 8,590,000.00 USD | 173.34 USD | 0.00 USD | `+25.90%` | `194,000,000.00` |
| `Live` | `Short` | `894.50` | 8,620,000.00 USD | 26,840.00 USD | 0.00 USD | `+26.04%` | `30,000,000,000.00` |
| `Live` | `Short` | `896.50` | 8,850,000.00 USD | 228,220.00 USD | 0.00 USD | `+26.32%` | `254,573,000,000.00` |
| `Live` | `Short` | `898.50` | 8,850,000.00 USD | 127.59 USD | 0.00 USD | `+26.60%` | `142,000,000.00` |
| `Live` | `Short` | `902.50` | 8,850,000.00 USD | 305.05 USD | 0.00 USD | `+27.17%` | `338,000,000.00` |
| `Live` | `Short` | `904.50` | 8,910,000.00 USD | 63,930.00 USD | 0.00 USD | `+27.45%` | `70,678,000,000.00` |
| `Live` | `Short` | `906.50` | 8,910,000.00 USD | 313.65 USD | 0.00 USD | `+27.73%` | `346,000,000.00` |
| `Live` | `Short` | `908.50` | 8,920,000.00 USD | 1,790.00 USD | 0.00 USD | `+28.01%` | `1,971,000,000.00` |
| `Live` | `Short` | `909.50` | 8,950,000.00 USD | 29,900.00 USD | 0.00 USD | `+28.15%` | `32,872,000,000.00` |
| `Live` | `Short` | `910.50` | 9,030,000.00 USD | 83,430.00 USD | 0.00 USD | `+28.30%` | `91,633,000,000.00` |
| `Live` | `Short` | `911.50` | 9,060,000.00 USD | 34,670.00 USD | 0.00 USD | `+28.44%` | `38,036,000,000.00` |
| `Live` | `Short` | `912.50` | 9,100,000.00 USD | 37,330.00 USD | 0.00 USD | `+28.58%` | `40,909,000,000.00` |
| `Live` | `Short` | `913.50` | 9,100,000.00 USD | 116.93 USD | 0.00 USD | `+28.72%` | `128,000,000.00` |
| `Live` | `Short` | `917.50` | 9,100,000.00 USD | 390.86 USD | 0.00 USD | `+29.28%` | `426,000,000.00` |
| `Live` | `Short` | `918.50` | 9,120,000.00 USD | 17,510.00 USD | 0.00 USD | `+29.42%` | `19,059,000,000.00` |
| `Live` | `Short` | `920.50` | 9,210,000.00 USD | 92,050.00 USD | 0.00 USD | `+29.70%` | `100,000,000,000.00` |
| `Live` | `Short` | `925.50` | 9,220,000.00 USD | 9,260.00 USD | 0.00 USD | `+30.41%` | `10,000,000,000.00` |
| `Live` | `Short` | `934.50` | 9,220,000.00 USD | 656.02 USD | 0.00 USD | `+31.68%` | `702,000,000.00` |
| `Live` | `Short` | `935.50` | 9,290,000.00 USD | 65,480.00 USD | 0.00 USD | `+31.82%` | `70,000,000,000.00` |
| `Live` | `Short` | `937.50` | 9,300,000.00 USD | 13,130.00 USD | 0.00 USD | `+32.10%` | `14,008,000,000.00` |
| `Live` | `Short` | `945.50` | 9,360,000.00 USD | 58,060.00 USD | 0.00 USD | `+33.23%` | `61,406,000,000.00` |
| `Live` | `Short` | `950.50` | 9,360,000.00 USD | 2,380.00 USD | 0.00 USD | `+33.93%` | `2,504,000,000.00` |
| `Live` | `Short` | `951.50` | 9,360,000.00 USD | 397.73 USD | 0.00 USD | `+34.07%` | `418,000,000.00` |
| `Live` | `Short` | `954.50` | 9,380,000.00 USD | 18,890.00 USD | 0.00 USD | `+34.50%` | `19,788,000,000.00` |
| `Live` | `Short` | `960.50` | 9,380,000.00 USD | 114.30 USD | 0.00 USD | `+35.34%` | `119,000,000.00` |
| `Live` | `Short` | `963.50` | 9,380,000.00 USD | 205.23 USD | 0.00 USD | `+35.76%` | `213,000,000.00` |
| `Live` | `Short` | `966.50` | 9,390,000.00 USD | 6,960.00 USD | 0.00 USD | `+36.19%` | `7,199,000,000.00` |
| `Live` | `Short` | `969.50` | 9,390,000.00 USD | 5,780.00 USD | 0.00 USD | `+36.61%` | `5,960,000,000.00` |
| `Live` | `Short` | `971.50` | 10,240,000.00 USD | 847,970.00 USD | 0.00 USD | `+36.89%` | `872,846,000,000.00` |
| `Live` | `Short` | `972.50` | 10,240,000.00 USD | 1,950.00 USD | 0.00 USD | `+37.03%` | `2,000,000,000.00` |
| `Live` | `Short` | `976.50` | 10,260,000.00 USD | 14,200.00 USD | 0.00 USD | `+37.60%` | `14,541,000,000.00` |
| `Live` | `Short` | `977.50` | 10,260,000.00 USD | 3,270.00 USD | 0.00 USD | `+37.74%` | `3,344,000,000.00` |
| `Live` | `Short` | `981.50` | 10,270,000.00 USD | 14,480.00 USD | 0.00 USD | `+38.30%` | `14,758,000,000.00` |
| `Live` | `Short` | `986.50` | 10,280,000.00 USD | 1,100.00 USD | 0.00 USD | `+39.00%` | `1,112,000,000.00` |
| `Live` | `Short` | `990.50` | 10,300,000.00 USD | 28,300.00 USD | 0.00 USD | `+39.57%` | `28,570,000,000.00` |
| `Live` | `Short` | `992.50` | 10,310,000.00 USD | 2,140.00 USD | 0.00 USD | `+39.85%` | `2,154,000,000.00` |
| `Live` | `Short` | `993.50` | 10,310,000.00 USD | 975.62 USD | 0.00 USD | `+39.99%` | `982,000,000.00` |
| `Live` | `Short` | `994.50` | 10,590,000.00 USD | 285,520.00 USD | 0.00 USD | `+40.13%` | `287,098,000,000.00` |
| `Live` | `Short` | `995.50` | 11,070,000.00 USD | 481,020.00 USD | 0.00 USD | `+40.27%` | `483,195,000,000.00` |
| `Live` | `Short` | `996.50` | 11,070,000.00 USD | 989.52 USD | 0.00 USD | `+40.41%` | `993,000,000.00` |
| `Live` | `Short` | `997.50` | 11,080,000.00 USD | 7,300.00 USD | 0.00 USD | `+40.55%` | `7,316,000,000.00` |
| `Live` | `Short` | `998.50` | 11,090,000.00 USD | 9,550.00 USD | 0.00 USD | `+40.70%` | `9,569,000,000.00` |
| `Live` | `Short` | `999.50` | 11,230,000.00 USD | 136,800.00 USD | 0.00 USD | `+40.84%` | `136,868,000,000.00` |
| `Live` | `Short` | `1003.50` | 11,230,000.00 USD | 1,620.00 USD | 0.00 USD | `+41.40%` | `1,617,000,000.00` |
| `Live` | `Short` | `1005.50` | 11,230,000.00 USD | 4,050.00 USD | 0.00 USD | `+41.68%` | `4,024,000,000.00` |
| `Live` | `Short` | `1008.50` | 11,260,000.00 USD | 28,800.00 USD | 0.00 USD | `+42.10%` | `28,558,000,000.00` |
| `Live` | `Short` | `1009.50` | 11,310,000.00 USD | 51,680.00 USD | 0.00 USD | `+42.25%` | `51,191,000,000.00` |
| `Live` | `Short` | `1010.50` | 11,420,000.00 USD | 101,810.00 USD | 0.00 USD | `+42.39%` | `100,755,000,000.00` |
| `Live` | `Short` | `1011.50` | 11,420,000.00 USD | 3,160.00 USD | 0.00 USD | `+42.53%` | `3,125,000,000.00` |
| `Live` | `Short` | `1014.50` | 11,420,000.00 USD | 1,450.00 USD | 0.00 USD | `+42.95%` | `1,434,000,000.00` |
| `Live` | `Short` | `1024.50` | 11,420,000.00 USD | 2,850.00 USD | 0.00 USD | `+44.36%` | `2,777,000,000.00` |
| `Live` | `Short` | `1037.50` | 11,730,000.00 USD | 302,500.00 USD | 0.00 USD | `+46.19%` | `291,563,000,000.00` |
| `Live` | `Short` | `1038.50` | 12,450,000.00 USD | 724,470.00 USD | 0.00 USD | `+46.33%` | `697,611,000,000.00` |
| `Live` | `Short` | `1039.50` | 12,550,000.00 USD | 96,150.00 USD | 0.00 USD | `+46.47%` | `92,500,000,000.00` |
| `Live` | `Short` | `1047.50` | 12,550,000.00 USD | 504.89 USD | 0.00 USD | `+47.60%` | `482,000,000.00` |
| `Live` | `Short` | `1050.50` | 12,550,000.00 USD | 500.04 USD | 0.00 USD | `+48.02%` | `476,000,000.00` |
| `Live` | `Short` | `1064.50` | 12,550,000.00 USD | 1,600.00 USD | 0.00 USD | `+50.00%` | `1,500,000,000.00` |
| `Live` | `Short` | `1067.50` | 12,560,000.00 USD | 15,380.00 USD | 0.00 USD | `+50.42%` | `14,403,000,000.00` |
| `Live` | `Short` | `1073.50` | 12,570,000.00 USD | 1,610.00 USD | 0.00 USD | `+51.26%` | `1,500,000,000.00` |
| `Live` | `Short` | `1074.50` | 12,630,000.00 USD | 68,680.00 USD | 0.00 USD | `+51.40%` | `63,916,000,000.00` |
| `Live` | `Short` | `1081.50` | 12,640,000.00 USD | 121.13 USD | 0.00 USD | `+52.39%` | `112,000,000.00` |
| `Live` | `Short` | `1085.50` | 12,640,000.00 USD | 4,330.00 USD | 0.00 USD | `+52.95%` | `3,985,000,000.00` |
| `Live` | `Short` | `1087.50` | 12,650,000.00 USD | 5,770.00 USD | 0.00 USD | `+53.24%` | `5,310,000,000.00` |
| `Live` | `Short` | `1088.50` | 12,660,000.00 USD | 15,780.00 USD | 0.00 USD | `+53.38%` | `14,495,000,000.00` |
| `Live` | `Short` | `1093.50` | 12,780,000.00 USD | 120,790.00 USD | 0.00 USD | `+54.08%` | `110,460,000,000.00` |
| `Live` | `Short` | `1096.50` | 12,940,000.00 USD | 162,020.00 USD | 0.00 USD | `+54.50%` | `147,759,000,000.00` |
| `Live` | `Short` | `1103.50` | 15,250,000.00 USD | 2,300,000.00 USD | 0.00 USD | `+55.49%` | `2,087,100,000,000.00` |
| `Live` | `Short` | `1106.50` | 15,360,000.00 USD | 115,080.00 USD | 0.00 USD | `+55.91%` | `104,000,000,000.00` |
| `Live` | `Short` | `1137.50` | 15,700,000.00 USD | 341,250.00 USD | 0.00 USD | `+60.28%` | `300,000,000,000.00` |
| `Live` | `Short` | `1139.50` | 15,760,000.00 USD | 61,760.00 USD | 0.00 USD | `+60.56%` | `54,199,000,000.00` |
| `Live` | `Short` | `1144.50` | 15,840,000.00 USD | 78,470.00 USD | 0.00 USD | `+61.27%` | `68,563,000,000.00` |
| `Live` | `Short` | `1147.50` | 15,860,000.00 USD | 20,460.00 USD | 0.00 USD | `+61.69%` | `17,826,000,000.00` |
| `Live` | `Short` | `1150.50` | 15,880,000.00 USD | 19,980.00 USD | 0.00 USD | `+62.11%` | `17,363,000,000.00` |
| `Live` | `Short` | `1161.50` | 15,890,000.00 USD | 1,550.00 USD | 0.00 USD | `+63.66%` | `1,337,000,000.00` |
| `Live` | `Short` | `1163.50` | 15,900,000.00 USD | 11,810.00 USD | 0.00 USD | `+63.94%` | `10,154,000,000.00` |
| `Live` | `Short` | `1170.50` | 15,900,000.00 USD | 156.85 USD | 0.00 USD | `+64.93%` | `134,000,000.00` |
| `Live` | `Short` | `1178.50` | 15,960,000.00 USD | 66,060.00 USD | 0.00 USD | `+66.06%` | `56,055,000,000.00` |
| `Live` | `Short` | `1181.50` | 16,020,000.00 USD | 57,080.00 USD | 0.00 USD | `+66.48%` | `48,311,000,000.00` |
| `Live` | `Short` | `1196.50` | 16,020,000.00 USD | 206.99 USD | 0.00 USD | `+68.59%` | `173,000,000.00` |
| `Live` | `Short` | `1197.50` | 16,020,000.00 USD | 463.43 USD | 0.00 USD | `+68.74%` | `387,000,000.00` |
| `Live` | `Short` | `1202.50` | 16,140,000.00 USD | 118,760.00 USD | 0.00 USD | `+69.44%` | `98,764,000,000.00` |
| `Live` | `Short` | `1207.50` | 16,140,000.00 USD | 385.19 USD | 0.00 USD | `+70.14%` | `319,000,000.00` |
| `Live` | `Short` | `1213.50` | 16,140,000.00 USD | 126.20 USD | 0.00 USD | `+70.99%` | `104,000,000.00` |
| `Live` | `Short` | `1218.50` | 16,140,000.00 USD | 704.29 USD | 0.00 USD | `+71.69%` | `578,000,000.00` |
| `Live` | `Short` | `1220.50` | 16,170,000.00 USD | 30,490.00 USD | 0.00 USD | `+71.98%` | `24,982,000,000.00` |
| `Live` | `Short` | `1221.50` | 16,210,000.00 USD | 42,750.00 USD | 0.00 USD | `+72.12%` | `35,000,000,000.00` |
| `Live` | `Short` | `1224.50` | 16,220,000.00 USD | 1,030.00 USD | 0.00 USD | `+72.54%` | `841,000,000.00` |
| `Live` | `Short` | `1227.50` | 16,220,000.00 USD | 4,900.00 USD | 0.00 USD | `+72.96%` | `3,994,000,000.00` |
| `Live` | `Short` | `1231.50` | 16,220,000.00 USD | 3,740.00 USD | 0.00 USD | `+73.53%` | `3,035,000,000.00` |
| `Live` | `Short` | `1239.50` | 16,340,000.00 USD | 111,560.00 USD | 0.00 USD | `+74.65%` | `90,000,000,000.00` |
| `Live` | `Short` | `1241.50` | 16,360,000.00 USD | 26,600.00 USD | 0.00 USD | `+74.94%` | `21,429,000,000.00` |
| `Live` | `Short` | `1245.50` | 16,400,000.00 USD | 37,630.00 USD | 0.00 USD | `+75.50%` | `30,209,000,000.00` |
| `Live` | `Short` | `1247.50` | 16,530,000.00 USD | 134,380.00 USD | 0.00 USD | `+75.78%` | `107,716,000,000.00` |
| `Live` | `Short` | `1249.50` | 16,560,000.00 USD | 20,870.00 USD | 0.00 USD | `+76.06%` | `16,706,000,000.00` |
| `Live` | `Short` | `1251.50` | 16,560,000.00 USD | 100.12 USD | 0.00 USD | `+76.34%` | `80,000,000.00` |
| `Live` | `Short` | `1256.50` | 16,670,000.00 USD | 113,080.00 USD | 0.00 USD | `+77.05%` | `90,000,000,000.00` |
| `Live` | `Short` | `1259.50` | 16,670,000.00 USD | 201.52 USD | 0.00 USD | `+77.47%` | `160,000,000.00` |
| `Live` | `Short` | `1268.50` | 18,250,000.00 USD | 1,580,000.00 USD | 0.00 USD | `+78.74%` | `1,244,857,000,000.00` |
| `Live` | `Short` | `1278.50` | 18,360,000.00 USD | 109,060.00 USD | 0.00 USD | `+80.15%` | `85,305,000,000.00` |
| `Live` | `Short` | `1290.50` | 18,420,000.00 USD | 62,100.00 USD | 0.00 USD | `+81.84%` | `48,123,000,000.00` |
| `Live` | `Short` | `1293.50` | 18,440,000.00 USD | 25,460.00 USD | 0.00 USD | `+82.26%` | `19,685,000,000.00` |
| `Live` | `Short` | `1294.50` | 18,480,000.00 USD | 32,170.00 USD | 0.00 USD | `+82.40%` | `24,853,000,000.00` |
| `Live` | `Short` | `1295.50` | 18,480,000.00 USD | 7,200.00 USD | 0.00 USD | `+82.54%` | `5,559,000,000.00` |
| `Live` | `Short` | `1299.50` | 18,490,000.00 USD | 4,020.00 USD | 0.00 USD | `+83.11%` | `3,092,000,000.00` |
| `Live` | `Short` | `1300.50` | 18,490,000.00 USD | 5,800.00 USD | 0.00 USD | `+83.25%` | `4,463,000,000.00` |
| `Live` | `Short` | `1304.50` | 20,340,000.00 USD | 1,840,000.00 USD | 0.00 USD | `+83.81%` | `1,412,868,000,000.00` |
| `Live` | `Short` | `1312.50` | 20,340,000.00 USD | 645.75 USD | 0.00 USD | `+84.94%` | `492,000,000.00` |
| `Live` | `Short` | `1314.50` | 20,340,000.00 USD | 1,850.00 USD | 0.00 USD | `+85.22%` | `1,409,000,000.00` |
| `Live` | `Short` | `1316.50` | 20,350,000.00 USD | 7,580.00 USD | 0.00 USD | `+85.50%` | `5,758,000,000.00` |
| `Live` | `Short` | `1317.50` | 20,350,000.00 USD | 2,810.00 USD | 0.00 USD | `+85.64%` | `2,134,000,000.00` |
| `Live` | `Short` | `1319.50` | 20,360,000.00 USD | 14,130.00 USD | 0.00 USD | `+85.93%` | `10,710,000,000.00` |
| `Live` | `Short` | `1323.50` | 20,360,000.00 USD | 115.14 USD | 0.00 USD | `+86.49%` | `87,000,000.00` |
| `Live` | `Short` | `1327.50` | 20,360,000.00 USD | 138.06 USD | 0.00 USD | `+87.05%` | `104,000,000.00` |
| `Live` | `Short` | `1328.50` | 20,530,000.00 USD | 168,850.00 USD | 0.00 USD | `+87.19%` | `127,099,000,000.00` |
| `Live` | `Short` | `1330.50` | 20,560,000.00 USD | 23,470.00 USD | 0.00 USD | `+87.48%` | `17,640,000,000.00` |
| `Live` | `Short` | `1339.50` | 20,640,000.00 USD | 87,070.00 USD | 0.00 USD | `+88.74%` | `65,000,000,000.00` |
| `Live` | `Short` | `1346.50` | 20,670,000.00 USD | 26,930.00 USD | 0.00 USD | `+89.73%` | `20,000,000,000.00` |
| `Live` | `Short` | `1350.50` | 20,670,000.00 USD | 1,350.00 USD | 0.00 USD | `+90.29%` | `1,000,000,000.00` |
| `Live` | `Short` | `1365.50` | 20,740,000.00 USD | 71,280.00 USD | 0.00 USD | `+92.41%` | `52,204,000,000.00` |
| `Live` | `Short` | `1366.50` | 20,750,000.00 USD | 2,930.00 USD | 0.00 USD | `+92.55%` | `2,142,000,000.00` |
| `Live` | `Short` | `1367.50` | 20,750,000.00 USD | 4,100.00 USD | 0.00 USD | `+92.69%` | `3,000,000,000.00` |
| `Live` | `Short` | `1369.50` | 20,800,000.00 USD | 46,880.00 USD | 0.00 USD | `+92.97%` | `34,232,000,000.00` |
| `Live` | `Short` | `1401.50` | 20,800,000.00 USD | 177.99 USD | 0.00 USD | `+97.48%` | `127,000,000.00` |
| `Live` | `Short` | `1405.50` | 20,800,000.00 USD | 4,770.00 USD | 0.00 USD | `+98.04%` | `3,392,000,000.00` |
| `Live` | `Short` | `1407.50` | 20,830,000.00 USD | 32,370.00 USD | 0.00 USD | `+98.33%` | `23,000,000,000.00` |
| `Live` | `Short` | `1417.50` | 20,840,000.00 USD | 4,900.00 USD | 0.00 USD | `+99.74%` | `3,457,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `150.50` | 4,650,000.00 USD | 0.00 USD | 475.73 USD | `-78.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `300.50` | 4,650,000.00 USD | 0.00 USD | 2,400.00 USD | `-57.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `333.50` | 4,650,000.00 USD | 0.00 USD | 333.50 USD | `-53.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `360.50` | 4,640,000.00 USD | 0.00 USD | 8,140.00 USD | `-49.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `369.50` | 4,640,000.00 USD | 0.00 USD | 5,170.00 USD | `-47.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `400.50` | 4,630,000.00 USD | 0.00 USD | 17,290.00 USD | `-43.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `410.50` | 4,610,000.00 USD | 0.00 USD | 25,210.00 USD | `-42.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `412.50` | 4,590,000.00 USD | 0.00 USD | 4,550.00 USD | `-41.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `424.50` | 4,580,000.00 USD | 0.00 USD | 8,180.00 USD | `-40.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `433.50` | 4,580,000.00 USD | 0.00 USD | 173.83 USD | `-38.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `445.50` | 4,580,000.00 USD | 0.00 USD | 2,210.00 USD | `-37.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `455.50` | 4,570,000.00 USD | 0.00 USD | 698.74 USD | `-35.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `456.50` | 4,570,000.00 USD | 0.00 USD | 2,270.00 USD | `-35.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `458.50` | 4,570,000.00 USD | 0.00 USD | 1,750.00 USD | `-35.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `469.50` | 4,570,000.00 USD | 0.00 USD | 3,550.00 USD | `-33.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `486.50` | 4,570,000.00 USD | 0.00 USD | 100.71 USD | `-31.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `487.50` | 4,570,000.00 USD | 0.00 USD | 6,600.00 USD | `-31.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `488.50` | 4,560,000.00 USD | 0.00 USD | 125.06 USD | `-31.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `492.50` | 4,560,000.00 USD | 0.00 USD | 2,450.00 USD | `-30.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `498.50` | 4,560,000.00 USD | 0.00 USD | 163.01 USD | `-29.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `499.50` | 4,560,000.00 USD | 0.00 USD | 214.78 USD | `-29.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `500.50` | 4,560,000.00 USD | 0.00 USD | 39,500.00 USD | `-29.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `503.50` | 4,520,000.00 USD | 0.00 USD | 42,600.00 USD | `-29.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `506.50` | 4,470,000.00 USD | 0.00 USD | 138.78 USD | `-28.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `509.50` | 4,470,000.00 USD | 0.00 USD | 185.97 USD | `-28.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `515.50` | 4,470,000.00 USD | 0.00 USD | 1,030.00 USD | `-27.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `516.50` | 4,470,000.00 USD | 0.00 USD | 125.51 USD | `-27.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `517.50` | 4,470,000.00 USD | 0.00 USD | 280.49 USD | `-27.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `521.50` | 4,470,000.00 USD | 0.00 USD | 258.14 USD | `-26.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `524.50` | 4,470,000.00 USD | 0.00 USD | 8,170.00 USD | `-26.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `528.50` | 4,460,000.00 USD | 0.00 USD | 485.16 USD | `-25.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `534.50` | 4,460,000.00 USD | 0.00 USD | 4,650.00 USD | `-24.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `538.50` | 4,460,000.00 USD | 0.00 USD | 1,680.00 USD | `-24.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `540.50` | 4,460,000.00 USD | 0.00 USD | 864.80 USD | `-23.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `550.50` | 4,460,000.00 USD | 0.00 USD | 4,130.00 USD | `-22.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `552.50` | 4,450,000.00 USD | 0.00 USD | 366,230.00 USD | `-22.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `554.50` | 4,090,000.00 USD | 0.00 USD | 1,190.00 USD | `-21.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `555.50` | 4,080,000.00 USD | 0.00 USD | 611.05 USD | `-21.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `557.50` | 4,080,000.00 USD | 0.00 USD | 213.52 USD | `-21.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `558.50` | 4,080,000.00 USD | 0.00 USD | 51,260.00 USD | `-21.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `560.50` | 4,030,000.00 USD | 0.00 USD | 292.02 USD | `-21.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `561.50` | 4,030,000.00 USD | 0.00 USD | 748.48 USD | `-20.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `562.50` | 4,030,000.00 USD | 0.00 USD | 199.12 USD | `-20.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `563.50` | 4,030,000.00 USD | 0.00 USD | 808.06 USD | `-20.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `566.50` | 4,030,000.00 USD | 0.00 USD | 566.50 USD | `-20.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `567.50` | 4,030,000.00 USD | 0.00 USD | 330.85 USD | `-20.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `568.50` | 4,030,000.00 USD | 0.00 USD | 5,680.00 USD | `-19.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `569.50` | 4,020,000.00 USD | 0.00 USD | 569.50 USD | `-19.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `570.50` | 4,020,000.00 USD | 0.00 USD | 774.17 USD | `-19.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `571.50` | 4,020,000.00 USD | 0.00 USD | 1,700.00 USD | `-19.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `573.50` | 4,020,000.00 USD | 0.00 USD | 291.91 USD | `-19.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `575.50` | 4,020,000.00 USD | 0.00 USD | 469.61 USD | `-18.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `576.50` | 4,020,000.00 USD | 0.00 USD | 289.98 USD | `-18.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `577.50` | 4,020,000.00 USD | 0.00 USD | 285.86 USD | `-18.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `579.50` | 4,020,000.00 USD | 0.00 USD | 289.17 USD | `-18.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `580.50` | 4,020,000.00 USD | 0.00 USD | 6,750.00 USD | `-18.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `581.50` | 4,010,000.00 USD | 0.00 USD | 1,240.00 USD | `-18.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `582.50` | 4,010,000.00 USD | 0.00 USD | 6,980.00 USD | `-17.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `583.50` | 4,000,000.00 USD | 0.00 USD | 287.67 USD | `-17.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `584.50` | 4,000,000.00 USD | 0.00 USD | 763.94 USD | `-17.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `585.50` | 4,000,000.00 USD | 0.00 USD | 542.76 USD | `-17.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `586.50` | 4,000,000.00 USD | 0.00 USD | 34,020.00 USD | `-17.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `587.50` | 3,970,000.00 USD | 0.00 USD | 830,190.00 USD | `-17.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `588.50` | 3,140,000.00 USD | 0.00 USD | 287.78 USD | `-17.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `589.50` | 3,140,000.00 USD | 0.00 USD | 1,820.00 USD | `-16.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `590.50` | 3,140,000.00 USD | 0.00 USD | 540.31 USD | `-16.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `592.50` | 3,140,000.00 USD | 0.00 USD | 698.56 USD | `-16.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `593.50` | 3,140,000.00 USD | 0.00 USD | 1,160.00 USD | `-16.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `596.50` | 3,130,000.00 USD | 0.00 USD | 119.30 USD | `-15.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `597.50` | 3,130,000.00 USD | 0.00 USD | 222.87 USD | `-15.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `598.50` | 3,130,000.00 USD | 0.00 USD | 244.79 USD | `-15.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `600.50` | 3,130,000.00 USD | 0.00 USD | 43,310.00 USD | `-15.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `601.50` | 3,090,000.00 USD | 0.00 USD | 1,590.00 USD | `-15.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `602.50` | 3,090,000.00 USD | 0.00 USD | 46,760.00 USD | `-15.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `603.50` | 3,040,000.00 USD | 0.00 USD | 123,870.00 USD | `-14.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `604.50` | 2,920,000.00 USD | 0.00 USD | 1,870.00 USD | `-14.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `605.50` | 2,920,000.00 USD | 0.00 USD | 2,610.00 USD | `-14.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `608.50` | 2,910,000.00 USD | 0.00 USD | 18,380.00 USD | `-14.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `610.50` | 2,890,000.00 USD | 0.00 USD | 11,650.00 USD | `-13.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `611.50` | 2,880,000.00 USD | 0.00 USD | 4,470.00 USD | `-13.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `612.50` | 2,880,000.00 USD | 0.00 USD | 1,380.00 USD | `-13.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `614.50` | 2,880,000.00 USD | 0.00 USD | 269.15 USD | `-13.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `615.50` | 2,880,000.00 USD | 0.00 USD | 1,740.00 USD | `-13.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `616.50` | 2,880,000.00 USD | 0.00 USD | 120.83 USD | `-13.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `620.50` | 2,880,000.00 USD | 0.00 USD | 13,170.00 USD | `-12.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `621.50` | 2,860,000.00 USD | 0.00 USD | 2,150.00 USD | `-12.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `623.50` | 2,860,000.00 USD | 0.00 USD | 219.47 USD | `-12.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `624.50` | 2,860,000.00 USD | 0.00 USD | 445.27 USD | `-12.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `625.50` | 2,860,000.00 USD | 0.00 USD | 445.98 USD | `-11.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `626.50` | 2,860,000.00 USD | 0.00 USD | 694.79 USD | `-11.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `627.50` | 2,860,000.00 USD | 0.00 USD | 916.15 USD | `-11.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `628.50` | 2,860,000.00 USD | 0.00 USD | 34,040.00 USD | `-11.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `629.50` | 2,820,000.00 USD | 0.00 USD | 2,740.00 USD | `-11.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `630.50` | 2,820,000.00 USD | 0.00 USD | 861.26 USD | `-11.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `631.50` | 2,820,000.00 USD | 0.00 USD | 179.98 USD | `-11.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `632.50` | 2,820,000.00 USD | 0.00 USD | 1,100.00 USD | `-10.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `633.50` | 2,820,000.00 USD | 0.00 USD | 164.08 USD | `-10.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `634.50` | 2,820,000.00 USD | 0.00 USD | 2,550.00 USD | `-10.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `636.50` | 2,820,000.00 USD | 0.00 USD | 6,460.00 USD | `-10.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `638.50` | 2,810,000.00 USD | 0.00 USD | 3,640.00 USD | `-10.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `639.50` | 2,810,000.00 USD | 0.00 USD | 384.98 USD | `-9.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `640.50` | 2,810,000.00 USD | 0.00 USD | 429.78 USD | `-9.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `641.50` | 2,800,000.00 USD | 0.00 USD | 352.18 USD | `-9.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `642.50` | 2,800,000.00 USD | 0.00 USD | 1,280.00 USD | `-9.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `643.50` | 2,800,000.00 USD | 0.00 USD | 1,830.00 USD | `-9.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `644.50` | 2,800,000.00 USD | 0.00 USD | 3,790.00 USD | `-9.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `645.50` | 2,800,000.00 USD | 0.00 USD | 1,950.00 USD | `-9.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `646.50` | 2,800,000.00 USD | 0.00 USD | 971.04 USD | `-8.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `648.50` | 2,790,000.00 USD | 0.00 USD | 1,800.00 USD | `-8.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `649.50` | 2,790,000.00 USD | 0.00 USD | 107.17 USD | `-8.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `650.50` | 2,790,000.00 USD | 0.00 USD | 30,840.00 USD | `-8.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `651.50` | 2,760,000.00 USD | 0.00 USD | 201.31 USD | `-8.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `653.50` | 2,760,000.00 USD | 0.00 USD | 2,020.00 USD | `-7.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `654.50` | 2,760,000.00 USD | 0.00 USD | 308.92 USD | `-7.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `655.50` | 2,760,000.00 USD | 0.00 USD | 165.84 USD | `-7.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `656.50` | 2,760,000.00 USD | 0.00 USD | 2,330.00 USD | `-7.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `657.50` | 2,760,000.00 USD | 0.00 USD | 110.46 USD | `-7.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `658.50` | 2,760,000.00 USD | 0.00 USD | 1,320.00 USD | `-7.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `659.50` | 2,760,000.00 USD | 0.00 USD | 13,060.00 USD | `-7.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `660.50` | 2,740,000.00 USD | 0.00 USD | 11,090.00 USD | `-6.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `661.50` | 2,730,000.00 USD | 0.00 USD | 11,310.00 USD | `-6.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `662.50` | 2,720,000.00 USD | 0.00 USD | 7,780.00 USD | `-6.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `663.50` | 2,710,000.00 USD | 0.00 USD | 2,840.00 USD | `-6.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `664.50` | 2,710,000.00 USD | 0.00 USD | 864.51 USD | `-6.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `665.50` | 2,710,000.00 USD | 0.00 USD | 12,180.00 USD | `-6.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `666.50` | 2,700,000.00 USD | 0.00 USD | 24,530.00 USD | `-6.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `667.50` | 2,670,000.00 USD | 0.00 USD | 10,740.00 USD | `-5.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `668.50` | 2,660,000.00 USD | 0.00 USD | 760.75 USD | `-5.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `669.50` | 2,660,000.00 USD | 0.00 USD | 2,390.00 USD | `-5.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `670.50` | 2,660,000.00 USD | 0.00 USD | 129,550.00 USD | `-5.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `671.50` | 2,530,000.00 USD | 0.00 USD | 19,160.00 USD | `-5.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `672.50` | 2,510,000.00 USD | 0.00 USD | 1,500.00 USD | `-5.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `673.50` | 2,510,000.00 USD | 0.00 USD | 7,790.00 USD | `-5.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `674.50` | 2,500,000.00 USD | 0.00 USD | 1,470.00 USD | `-4.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `675.50` | 2,500,000.00 USD | 0.00 USD | 10,640.00 USD | `-4.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `676.50` | 2,490,000.00 USD | 0.00 USD | 56,290.00 USD | `-4.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `677.50` | 2,430,000.00 USD | 0.00 USD | 39,650.00 USD | `-4.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `678.50` | 2,390,000.00 USD | 0.00 USD | 825.73 USD | `-4.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `679.50` | 2,390,000.00 USD | 0.00 USD | 5,250.00 USD | `-4.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `680.50` | 2,390,000.00 USD | 0.00 USD | 296,190.00 USD | `-4.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `681.50` | 2,090,000.00 USD | 0.00 USD | 146.52 USD | `-3.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `682.50` | 2,090,000.00 USD | 0.00 USD | 1,160,000.00 USD | `-3.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `683.50` | 930,030.00 USD | 0.00 USD | 171,850.00 USD | `-3.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `684.50` | 758,180.00 USD | 0.00 USD | 171,120.00 USD | `-3.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `685.50` | 587,050.00 USD | 0.00 USD | 12,470.00 USD | `-3.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `686.50` | 574,580.00 USD | 0.00 USD | 530.66 USD | `-3.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `687.50` | 574,050.00 USD | 0.00 USD | 330.69 USD | `-3.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `688.50` | 573,720.00 USD | 0.00 USD | 364.22 USD | `-2.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `689.50` | 573,360.00 USD | 0.00 USD | 532.98 USD | `-2.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `690.50` | 572,830.00 USD | 0.00 USD | 3,860.00 USD | `-2.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `691.50` | 568,960.00 USD | 0.00 USD | 173,590.00 USD | `-2.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `692.50` | 395,370.00 USD | 0.00 USD | 2,420.00 USD | `-2.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `693.50` | 392,950.00 USD | 0.00 USD | 7,180.00 USD | `-2.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `694.50` | 385,770.00 USD | 0.00 USD | 589.63 USD | `-2.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `695.50` | 385,180.00 USD | 0.00 USD | 166.92 USD | `-2.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `696.50` | 385,020.00 USD | 0.00 USD | 2,200.00 USD | `-1.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `697.50` | 382,810.00 USD | 0.00 USD | 47,550.00 USD | `-1.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `698.50` | 335,260.00 USD | 0.00 USD | 15,500.00 USD | `-1.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `699.50` | 319,770.00 USD | 0.00 USD | 116,570.00 USD | `-1.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `700.50` | 203,190.00 USD | 0.00 USD | 41,530.00 USD | `-1.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `701.50` | 161,660.00 USD | 0.00 USD | 633.45 USD | `-1.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `702.50` | 161,030.00 USD | 0.00 USD | 29,960.00 USD | `-1.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `703.50` | 131,060.00 USD | 0.00 USD | 3,850.00 USD | `-0.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `704.50` | 127,220.00 USD | 0.00 USD | 86,660.00 USD | `-0.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `705.50` | 40,560.00 USD | 0.00 USD | 6,830.00 USD | `-0.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `706.50` | 33,730.00 USD | 0.00 USD | 21,300.00 USD | `-0.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `707.50` | 12,430.00 USD | 0.00 USD | 182.53 USD | `-0.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `708.50` | 12,240.00 USD | 0.00 USD | 10,760.00 USD | `-0.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `709.50` | 1,490.00 USD | 0.00 USD | 1,490.00 USD | `-0.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `710.50` | 7,940.00 USD | 7,940.00 USD | 0.00 USD | `+0.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `711.50` | 14,650.00 USD | 6,700.00 USD | 0.00 USD | `+0.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `712.50` | 29,140.00 USD | 14,490.00 USD | 0.00 USD | `+0.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `713.50` | 29,290.00 USD | 150.55 USD | 0.00 USD | `+0.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `714.50` | 30,950.00 USD | 1,660.00 USD | 0.00 USD | `+0.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `715.50` | 37,380.00 USD | 6,420.00 USD | 0.00 USD | `+0.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `716.50` | 206,070.00 USD | 168,690.00 USD | 0.00 USD | `+0.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `717.50` | 207,120.00 USD | 1,050.00 USD | 0.00 USD | `+1.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `718.50` | 287,990.00 USD | 80,870.00 USD | 0.00 USD | `+1.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `719.50` | 357,870.00 USD | 69,880.00 USD | 0.00 USD | `+1.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `720.50` | 378,330.00 USD | 20,460.00 USD | 0.00 USD | `+1.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `721.50` | 381,320.00 USD | 2,990.00 USD | 0.00 USD | `+1.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `722.50` | 383,200.00 USD | 1,880.00 USD | 0.00 USD | `+1.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `723.50` | 390,130.00 USD | 6,930.00 USD | 0.00 USD | `+1.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `724.50` | 415,830.00 USD | 25,700.00 USD | 0.00 USD | `+2.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `725.50` | 507,260.00 USD | 91,430.00 USD | 0.00 USD | `+2.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `726.50` | 511,370.00 USD | 4,110.00 USD | 0.00 USD | `+2.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `727.50` | 528,170.00 USD | 16,790.00 USD | 0.00 USD | `+2.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `728.50` | 569,070.00 USD | 40,910.00 USD | 0.00 USD | `+2.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `729.50` | 707,850.00 USD | 138,780.00 USD | 0.00 USD | `+2.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `730.50` | 761,100.00 USD | 53,250.00 USD | 0.00 USD | `+2.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `731.50` | 985,510.00 USD | 224,410.00 USD | 0.00 USD | `+3.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `732.50` | 986,820.00 USD | 1,310.00 USD | 0.00 USD | `+3.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `733.50` | 1,470,000.00 USD | 486,210.00 USD | 0.00 USD | `+3.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `734.50` | 1,480,000.00 USD | 7,480.00 USD | 0.00 USD | `+3.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `735.50` | 1,490,000.00 USD | 12,850.00 USD | 0.00 USD | `+3.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `736.50` | 1,500,000.00 USD | 6,860.00 USD | 0.00 USD | `+3.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `737.50` | 1,500,000.00 USD | 3,970.00 USD | 0.00 USD | `+3.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `738.50` | 1,520,000.00 USD | 12,620.00 USD | 0.00 USD | `+4.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `739.50` | 1,520,000.00 USD | 790.53 USD | 0.00 USD | `+4.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `740.50` | 1,520,000.00 USD | 4,170.00 USD | 0.00 USD | `+4.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `741.50` | 1,520,000.00 USD | 2,370.00 USD | 0.00 USD | `+4.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `742.50` | 1,530,000.00 USD | 4,540.00 USD | 0.00 USD | `+4.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `743.50` | 1,540,000.00 USD | 8,880.00 USD | 0.00 USD | `+4.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `744.50` | 1,740,000.00 USD | 203,810.00 USD | 0.00 USD | `+4.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `745.50` | 1,760,000.00 USD | 14,430.00 USD | 0.00 USD | `+5.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `746.50` | 1,760,000.00 USD | 672.60 USD | 0.00 USD | `+5.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `747.50` | 1,760,000.00 USD | 1,070.00 USD | 0.00 USD | `+5.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `748.50` | 1,760,000.00 USD | 558.38 USD | 0.00 USD | `+5.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `749.50` | 1,760,000.00 USD | 704.53 USD | 0.00 USD | `+5.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `750.50` | 1,760,000.00 USD | 123.83 USD | 0.00 USD | `+5.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `751.50` | 1,770,000.00 USD | 6,850.00 USD | 0.00 USD | `+5.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `752.50` | 1,770,000.00 USD | 2,730.00 USD | 0.00 USD | `+6.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `753.50` | 1,770,000.00 USD | 105.49 USD | 0.00 USD | `+6.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `754.50` | 1,820,000.00 USD | 47,160.00 USD | 0.00 USD | `+6.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `755.50` | 1,820,000.00 USD | 4,420.00 USD | 0.00 USD | `+6.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `756.50` | 1,830,000.00 USD | 12,340.00 USD | 0.00 USD | `+6.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `757.50` | 1,980,000.00 USD | 142,940.00 USD | 0.00 USD | `+6.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `758.50` | 1,980,000.00 USD | 2,920.00 USD | 0.00 USD | `+6.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `759.50` | 2,000,000.00 USD | 21,350.00 USD | 0.00 USD | `+7.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `760.50` | 2,290,000.00 USD | 288,360.00 USD | 0.00 USD | `+7.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `761.50` | 2,300,000.00 USD | 11,460.00 USD | 0.00 USD | `+7.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `762.50` | 2,300,000.00 USD | 274.50 USD | 0.00 USD | `+7.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `763.50` | 2,350,000.00 USD | 45,960.00 USD | 0.00 USD | `+7.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `764.50` | 2,350,000.00 USD | 323.38 USD | 0.00 USD | `+7.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `765.50` | 2,390,000.00 USD | 41,050.00 USD | 0.00 USD | `+7.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `766.50` | 2,390,000.00 USD | 600.94 USD | 0.00 USD | `+8.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `767.50` | 2,860,000.00 USD | 468,310.00 USD | 0.00 USD | `+8.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `768.50` | 2,860,000.00 USD | 180.60 USD | 0.00 USD | `+8.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `769.50` | 2,860,000.00 USD | 171.60 USD | 0.00 USD | `+8.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `770.50` | 2,860,000.00 USD | 1,540.00 USD | 0.00 USD | `+8.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `771.50` | 2,860,000.00 USD | 242.25 USD | 0.00 USD | `+8.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `772.50` | 2,860,000.00 USD | 273.46 USD | 0.00 USD | `+8.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `773.50` | 2,860,000.00 USD | 656.70 USD | 0.00 USD | `+8.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `774.50` | 2,870,000.00 USD | 9,680.00 USD | 0.00 USD | `+9.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `775.50` | 2,870,000.00 USD | 4,570.00 USD | 0.00 USD | `+9.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `776.50` | 2,890,000.00 USD | 14,230.00 USD | 0.00 USD | `+9.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `777.50` | 2,900,000.00 USD | 15,690.00 USD | 0.00 USD | `+9.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `778.50` | 2,910,000.00 USD | 4,580.00 USD | 0.00 USD | `+9.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `779.50` | 2,910,000.00 USD | 132.52 USD | 0.00 USD | `+9.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `780.50` | 2,930,000.00 USD | 24,280.00 USD | 0.00 USD | `+9.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `781.50` | 2,930,000.00 USD | 2,050.00 USD | 0.00 USD | `+10.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `782.50` | 2,940,000.00 USD | 1,900.00 USD | 0.00 USD | `+10.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `783.50` | 2,940,000.00 USD | 101.07 USD | 0.00 USD | `+10.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `784.50` | 2,940,000.00 USD | 102.77 USD | 0.00 USD | `+10.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `785.50` | 2,940,000.00 USD | 559.28 USD | 0.00 USD | `+10.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `786.50` | 2,950,000.00 USD | 11,990.00 USD | 0.00 USD | `+10.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `787.50` | 2,950,000.00 USD | 2,260.00 USD | 0.00 USD | `+10.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `788.50` | 2,950,000.00 USD | 133.26 USD | 0.00 USD | `+11.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `790.50` | 2,960,000.00 USD | 4,190.00 USD | 0.00 USD | `+11.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `791.50` | 2,960,000.00 USD | 704.44 USD | 0.00 USD | `+11.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `792.50` | 2,960,000.00 USD | 4,360.00 USD | 0.00 USD | `+11.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `793.50` | 2,960,000.00 USD | 1,450.00 USD | 0.00 USD | `+11.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `794.50` | 2,970,000.00 USD | 3,630.00 USD | 0.00 USD | `+11.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `795.50` | 2,970,000.00 USD | 3,040.00 USD | 0.00 USD | `+12.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `796.50` | 2,970,000.00 USD | 154.52 USD | 0.00 USD | `+12.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `799.50` | 2,970,000.00 USD | 1,450.00 USD | 0.00 USD | `+12.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `800.50` | 2,980,000.00 USD | 12,890.00 USD | 0.00 USD | `+12.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `801.50` | 2,980,000.00 USD | 120.22 USD | 0.00 USD | `+12.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `803.50` | 2,980,000.00 USD | 803.50 USD | 0.00 USD | `+13.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `805.50` | 2,980,000.00 USD | 120.02 USD | 0.00 USD | `+13.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `806.50` | 2,990,000.00 USD | 1,300.00 USD | 0.00 USD | `+13.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `808.50` | 2,990,000.00 USD | 5,010.00 USD | 0.00 USD | `+13.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `809.50` | 2,990,000.00 USD | 242.04 USD | 0.00 USD | `+14.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `810.50` | 3,010,000.00 USD | 15,790.00 USD | 0.00 USD | `+14.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `811.50` | 3,010,000.00 USD | 6,050.00 USD | 0.00 USD | `+14.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `812.50` | 3,010,000.00 USD | 844.19 USD | 0.00 USD | `+14.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `813.50` | 3,010,000.00 USD | 109.82 USD | 0.00 USD | `+14.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `814.50` | 3,020,000.00 USD | 3,390.00 USD | 0.00 USD | `+14.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `816.50` | 3,020,000.00 USD | 984.70 USD | 0.00 USD | `+15.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `817.50` | 3,020,000.00 USD | 162.68 USD | 0.00 USD | `+15.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `818.50` | 3,020,000.00 USD | 5,990.00 USD | 0.00 USD | `+15.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `820.50` | 3,030,000.00 USD | 8,230.00 USD | 0.00 USD | `+15.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `824.50` | 3,030,000.00 USD | 408.13 USD | 0.00 USD | `+16.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `826.50` | 3,030,000.00 USD | 672.77 USD | 0.00 USD | `+16.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `827.50` | 3,030,000.00 USD | 276.38 USD | 0.00 USD | `+16.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `828.50` | 3,040,000.00 USD | 1,800.00 USD | 0.00 USD | `+16.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `830.50` | 3,070,000.00 USD | 35,850.00 USD | 0.00 USD | `+17.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `833.50` | 3,070,000.00 USD | 1,050.00 USD | 0.00 USD | `+17.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `835.50` | 3,070,000.00 USD | 187.15 USD | 0.00 USD | `+17.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `836.50` | 3,070,000.00 USD | 372.24 USD | 0.00 USD | `+17.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `837.50` | 3,070,000.00 USD | 326.62 USD | 0.00 USD | `+18.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `839.50` | 3,070,000.00 USD | 296.34 USD | 0.00 USD | `+18.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `840.50` | 3,070,000.00 USD | 441.26 USD | 0.00 USD | `+18.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `841.50` | 3,070,000.00 USD | 329.87 USD | 0.00 USD | `+18.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `843.50` | 3,070,000.00 USD | 425.97 USD | 0.00 USD | `+18.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `844.50` | 3,080,000.00 USD | 1,770.00 USD | 0.00 USD | `+19.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `850.50` | 3,080,000.00 USD | 2,550.00 USD | 0.00 USD | `+19.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `851.50` | 3,090,000.00 USD | 11,650.00 USD | 0.00 USD | `+19.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `852.50` | 3,090,000.00 USD | 102.30 USD | 0.00 USD | `+20.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `854.50` | 3,090,000.00 USD | 137.57 USD | 0.00 USD | `+20.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `857.50` | 3,090,000.00 USD | 1,200.00 USD | 0.00 USD | `+20.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `860.50` | 3,090,000.00 USD | 1,160.00 USD | 0.00 USD | `+21.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `862.50` | 3,090,000.00 USD | 1,200.00 USD | 0.00 USD | `+21.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `863.50` | 3,100,000.00 USD | 874.73 USD | 0.00 USD | `+21.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `864.50` | 3,100,000.00 USD | 2,970.00 USD | 0.00 USD | `+21.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `865.50` | 3,100,000.00 USD | 3,460.00 USD | 0.00 USD | `+21.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `868.50` | 3,100,000.00 USD | 2,610.00 USD | 0.00 USD | `+22.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `870.50` | 3,100,000.00 USD | 228.07 USD | 0.00 USD | `+22.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `872.50` | 3,110,000.00 USD | 1,110.00 USD | 0.00 USD | `+22.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `884.50` | 3,160,000.00 USD | 54,820.00 USD | 0.00 USD | `+24.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `888.50` | 3,160,000.00 USD | 266.55 USD | 0.00 USD | `+25.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `890.50` | 3,160,000.00 USD | 690.14 USD | 0.00 USD | `+25.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `891.50` | 3,160,000.00 USD | 605.33 USD | 0.00 USD | `+25.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `900.50` | 3,290,000.00 USD | 132,720.00 USD | 0.00 USD | `+26.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `904.50` | 3,300,000.00 USD | 167.33 USD | 0.00 USD | `+27.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `907.50` | 3,300,000.00 USD | 1,640.00 USD | 0.00 USD | `+27.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `913.50` | 3,300,000.00 USD | 908.02 USD | 0.00 USD | `+28.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `914.50` | 3,300,000.00 USD | 4,150.00 USD | 0.00 USD | `+28.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `917.50` | 3,300,000.00 USD | 533.99 USD | 0.00 USD | `+29.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `919.50` | 3,300,000.00 USD | 166.43 USD | 0.00 USD | `+29.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `920.50` | 3,300,000.00 USD | 463.01 USD | 0.00 USD | `+29.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `926.50` | 3,300,000.00 USD | 320.57 USD | 0.00 USD | `+30.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `930.50` | 3,300,000.00 USD | 552.72 USD | 0.00 USD | `+31.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `933.50` | 3,300,000.00 USD | 196.03 USD | 0.00 USD | `+31.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `935.50` | 3,300,000.00 USD | 287.20 USD | 0.00 USD | `+31.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `958.50` | 3,310,000.00 USD | 782.14 USD | 0.00 USD | `+35.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `959.50` | 3,310,000.00 USD | 498.94 USD | 0.00 USD | `+35.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `965.50` | 3,310,000.00 USD | 1,930.00 USD | 0.00 USD | `+36.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `977.50` | 3,310,000.00 USD | 293.25 USD | 0.00 USD | `+37.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `980.50` | 3,310,000.00 USD | 1,300.00 USD | 0.00 USD | `+38.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `981.50` | 3,310,000.00 USD | 109.93 USD | 0.00 USD | `+38.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `984.50` | 3,310,000.00 USD | 439.09 USD | 0.00 USD | `+38.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `987.50` | 3,310,000.00 USD | 2,590.00 USD | 0.00 USD | `+39.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `997.50` | 3,310,000.00 USD | 1,840.00 USD | 0.00 USD | `+40.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `998.50` | 3,320,000.00 USD | 3,990.00 USD | 0.00 USD | `+40.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `999.50` | 3,320,000.00 USD | 938.53 USD | 0.00 USD | `+40.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1000.50` | 3,330,000.00 USD | 11,810.00 USD | 0.00 USD | `+40.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1017.50` | 3,330,000.00 USD | 203.50 USD | 0.00 USD | `+43.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1020.50` | 3,330,000.00 USD | 148.99 USD | 0.00 USD | `+43.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1026.50` | 3,330,000.00 USD | 149.87 USD | 0.00 USD | `+44.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1030.50` | 3,330,000.00 USD | 150.45 USD | 0.00 USD | `+45.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1045.50` | 3,330,000.00 USD | 195.51 USD | 0.00 USD | `+47.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1053.50` | 3,330,000.00 USD | 149.60 USD | 0.00 USD | `+48.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1072.50` | 3,330,000.00 USD | 156.58 USD | 0.00 USD | `+51.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1100.50` | 3,330,000.00 USD | 278.43 USD | 0.00 USD | `+55.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1111.50` | 3,330,000.00 USD | 555.75 USD | 0.00 USD | `+56.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1136.50` | 3,330,000.00 USD | 165.93 USD | 0.00 USD | `+60.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1146.50` | 3,330,000.00 USD | 167.39 USD | 0.00 USD | `+61.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1200.50` | 3,400,000.00 USD | 62,330.00 USD | 0.00 USD | `+69.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1202.50` | 3,400,000.00 USD | 1,250.00 USD | 0.00 USD | `+69.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1226.50` | 3,400,000.00 USD | 235.49 USD | 0.00 USD | `+72.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1230.50` | 3,400,000.00 USD | 3,580.00 USD | 0.00 USD | `+73.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1250.50` | 3,400,000.00 USD | 421.42 USD | 0.00 USD | `+76.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1280.50` | 3,400,000.00 USD | 3,750.00 USD | 0.00 USD | `+80.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1297.50` | 3,400,000.00 USD | 133.64 USD | 0.00 USD | `+82.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1300.50` | 3,410,000.00 USD | 685.36 USD | 0.00 USD | `+83.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1330.50` | 3,460,000.00 USD | 58,230.00 USD | 0.00 USD | `+87.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1340.50` | 3,540,000.00 USD | 80,850.00 USD | 0.00 USD | `+88.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1360.50` | 3,550,000.00 USD | 6,210.00 USD | 0.00 USD | `+91.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1363.50` | 3,550,000.00 USD | 349.06 USD | 0.00 USD | `+92.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1370.50` | 3,550,000.00 USD | 1,060.00 USD | 0.00 USD | `+93.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1372.50` | 3,570,000.00 USD | 19,210.00 USD | 0.00 USD | `+93.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1389.50` | 3,570,000.00 USD | 425.19 USD | 0.00 USD | `+95.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1400.50` | 3,580,000.00 USD | 3,850.00 USD | 0.00 USD | `+97.34%` | `TACTICAL (Retail Cluster)` |

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
  * Total Open Interest: `1.31B` | Total OI Tokens: `1,850,503.8 BNB`
  * 1h OI Change: `-1.62%` | 4h OI Change: `-3.94%` | 24h OI Change: `+6.61%`
  * Exchange Breakdown: Binance=`571.46M` | Bybit=`131.49M` | OKX=`64.38M` | Hyperliquid=`75.56M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-124.96K` | Last 24h: `-51.15K` | Last 3d: `142.23K` | Last 7d: `346.08K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0000%` | **USDT OKX** | `-0.0588%` |
| **USDT Bybit** | `-0.0663%` | **USDT KuCoin** | `-0.0209%` |
| **USDT MEXC** | `0.0000%` | **USDT BingX** | `0.0050%` |
| **USDT Gate** | `0.0012%` | **USDT Bitget** | `-0.0023%` |
| **CoinM Binance** | `0.1038%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `BNB` | `55.23%` | `44.77%` | `1.23` | 59,570,000.00 USD |
| `15M` | `Binance` | `54.12%` | `45.88%` | `1.18` | 21,580,000.00 USD |
| `15M` | `OKX` | `64.67%` | `35.33%` | `1.83` | 9,670,000.00 USD |
| `15M` | `Bybit` | `46.77%` | `53.23%` | `0.88` | 5,390,000.00 USD |
| `15M` | `KuCoin` | `50.07%` | `49.93%` | `1.00` | 603,240.00 USD |
| `15M` | `Gate` | `57.78%` | `42.22%` | `1.37` | 4,600,000.00 USD |
| `15M` | `Bitget` | `50.57%` | `49.43%` | `1.02` | 1,980,000.00 USD |
| `15M` | `BingX` | `58.1%` | `41.9%` | `1.39` | 2,480,000.00 USD |
| `15M` | `MEXC` | `52.88%` | `47.12%` | `1.12` | 2,910,000.00 USD |
| `15M` | `Bitunix` | `50.22%` | `49.78%` | `1.01` | 5,480,000.00 USD |
| `15M` | `Hyperliquid` | `47.98%` | `52.02%` | `0.92` | 1,290,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `46.77%` | `53.23%` | `0.88` | 450,150.00 USD |
| `15M` | `Crypto.com` | `53.2%` | `46.8%` | `1.14` | 128,530.00 USD |
| `15M` | `WhiteBIT` | `99.99%` | `0.01%` | `9999.00` | 855,780.00 USD |
| `15M` | `HTX` | `41.05%` | `58.95%` | `0.70` | 39,930.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `41.65%` | `58.35%` | `0.71` | 1,190,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `52.93%` | `47.07%` | `1.12` | 896,870.00 USD |
| `15M` | `Whale Positions` | `54.12%` | `45.88%` | `1.18` | 21,580,000.00 USD |
| `15M` | `Global Accounts` | `55.23%` | `44.77%` | `1.23` | 59,570,000.00 USD |
| `1H` | `BNB` | `54.27%` | `45.73%` | `1.19` | 274,580,000.00 USD |
| `1H` | `Binance` | `53.91%` | `46.09%` | `1.17` | 98,010,000.00 USD |
| `1H` | `OKX` | `63.55%` | `36.45%` | `1.74` | 45,760,000.00 USD |
| `1H` | `Bybit` | `52.89%` | `47.11%` | `1.12` | 24,830,000.00 USD |
| `1H` | `KuCoin` | `61.44%` | `38.56%` | `1.59` | 3,240,000.00 USD |
| `1H` | `Gate` | `52.69%` | `47.31%` | `1.11` | 19,530,000.00 USD |
| `1H` | `Bitget` | `55.64%` | `44.36%` | `1.25` | 9,170,000.00 USD |
| `1H` | `BingX` | `44.16%` | `55.84%` | `0.79` | 11,320,000.00 USD |
| `1H` | `MEXC` | `52.48%` | `47.52%` | `1.10` | 15,280,000.00 USD |
| `1H` | `Bitunix` | `53.54%` | `46.46%` | `1.15` | 17,150,000.00 USD |
| `1H` | `Hyperliquid` | `45.5%` | `54.5%` | `0.83` | 15,450,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `48.42%` | `51.58%` | `0.94` | 2,110,000.00 USD |
| `1H` | `Crypto.com` | `56.62%` | `43.38%` | `1.31` | 461,020.00 USD |
| `1H` | `WhiteBIT` | `59.44%` | `40.56%` | `1.47` | 2,460,000.00 USD |
| `1H` | `HTX` | `70.49%` | `29.51%` | `2.39` | 253,500.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `84.19%` | `15.81%` | `5.33` | 19,160.00 USD |
| `1H` | `Aster` | `57.5%` | `42.5%` | `1.35` | 3,180,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `40.49%` | `59.51%` | `0.68` | 6,400,000.00 USD |
| `1H` | `Whale Positions` | `53.91%` | `46.09%` | `1.17` | 98,010,000.00 USD |
| `1H` | `Global Accounts` | `54.27%` | `45.73%` | `1.19` | 274,580,000.00 USD |
| `4H` | `BNB` | `48.22%` | `51.78%` | `0.93` | 1,150,000,000.00 USD |
| `4H` | `Binance` | `49.51%` | `50.49%` | `0.98` | 430,310,000.00 USD |
| `4H` | `OKX` | `45.4%` | `54.6%` | `0.83` | 155,880,000.00 USD |
| `4H` | `Bybit` | `47.2%` | `52.8%` | `0.89` | 199,060,000.00 USD |
| `4H` | `KuCoin` | `48.25%` | `51.75%` | `0.93` | 16,250,000.00 USD |
| `4H` | `Gate` | `48.08%` | `51.92%` | `0.93` | 25,100,000.00 USD |
| `4H` | `Bitget` | `49.16%` | `50.84%` | `0.97` | 74,510,000.00 USD |
| `4H` | `BingX` | `46.52%` | `53.48%` | `0.87` | 13,540,000.00 USD |
| `4H` | `MEXC` | `49.04%` | `50.96%` | `0.96` | 104,450,000.00 USD |
| `4H` | `Bitunix` | `50.38%` | `49.62%` | `1.02` | 41,100,000.00 USD |
| `4H` | `Hyperliquid` | `33.63%` | `66.37%` | `0.51` | 48,420,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `58.31%` | `41.69%` | `1.40` | 4,870,000.00 USD |
| `4H` | `Crypto.com` | `44.17%` | `55.83%` | `0.79` | 1,550,000.00 USD |
| `4H` | `WhiteBIT` | `84.86%` | `15.14%` | `5.61` | 14,180,000.00 USD |
| `4H` | `HTX` | `49.71%` | `50.29%` | `0.99` | 1,210,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `41.97%` | `58.03%` | `0.72` | 5,130,000.00 USD |
| `4H` | `Aster` | `49.85%` | `50.15%` | `0.99` | 8,380,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `55.76%` | `44.24%` | `1.26` | 4,220,000.00 USD |
| `4H` | `Whale Positions` | `49.51%` | `50.49%` | `0.98` | 430,310,000.00 USD |
| `4H` | `Global Accounts` | `48.22%` | `51.78%` | `0.93` | 1,150,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `703.35` | `698.37` | `703.35` | `703.95` | `693.15` | 25,441,600.08 USD | 13,471,074.68 USD | 11,970,525.40 USD | 1,500,549.29 USD | `+5.90%` | `5B / 0S` |
| `5:00 UTC` | `697.65` | `698.85` | `697.65` | `702.75` | `694.95` | 18,975,470.10 USD | 6,730,952.35 USD | 12,244,517.75 USD | -5,513,565.40 USD | `-29.06%` | `0B / 6S` |
| `0:00 UTC` | `696.15` | `697.09` | `696.15` | `701.25` | `691.05` | 27,922,556.67 USD | 13,351,945.23 USD | 14,570,611.45 USD | -1,218,666.22 USD | `-4.36%` | `3B / 2S` |
| `5:00 UTC` | `698.25` | `699.83` | `698.25` | `703.95` | `696.75` | 26,130,732.92 USD | 11,452,791.24 USD | 14,677,941.68 USD | -3,225,150.44 USD | `-12.34%` | `1B / 0S` |
| `0:00 UTC` | `702.15` | `705.20` | `702.15` | `709.95` | `700.95` | 29,227,520.74 USD | 13,415,473.28 USD | 15,812,047.46 USD | -2,396,574.18 USD | `-8.20%` | `2B / 1S` |
| `5:00 UTC` | `709.05` | `711.18` | `709.05` | `715.35` | `708.15` | 27,008,888.92 USD | 11,488,761.44 USD | 15,520,127.48 USD | -4,031,366.04 USD | `-14.93%` | `0B / 1S` |
| `0:00 UTC` | `714.45` | `714.56` | `714.45` | `715.95` | `712.95` | 20,381,456.18 USD | 9,116,486.18 USD | 11,264,970.00 USD | -2,148,483.82 USD | `-10.54%` | `0B / 1S` |
| `5:00 UTC` | `711.15` | `711.54` | `711.15` | `714.45` | `709.95` | 13,903,836.91 USD | 6,352,852.84 USD | 7,550,984.08 USD | -1,198,131.24 USD | `-8.62%` | `1B / 4S` |
| `0:00 UTC` | `711.75` | `711.23` | `711.75` | `712.95` | `708.45` | 13,559,921.70 USD | 6,659,796.80 USD | 6,900,124.90 USD | -240,328.10 USD | `-1.77%` | `1B / 4S` |
| `5:00 UTC` | `708.45` | `708.49` | `708.45` | `709.05` | `708.15` | 2,711,908.85 USD | 1,397,979.15 USD | 1,313,929.70 USD | 84,049.44 USD | `+3.10%` | `0B / 0S` |

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
| `5m` | 580,000.00 USD | 143,260.00 USD | **`ACCUMULATION`** |
| `15m` | -734,740.00 USD | -1,890,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -442,770.00 USD | 1,050,000.00 USD | **`ACCUMULATION`** |
| `1h` | -3,590,000.00 USD | -2,190,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -6,460,000.00 USD | -14,870,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -20,660,000.00 USD | -22,990,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -14,310,000.00 USD | -21,190,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -31,470,000.00 USD | -62,540,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -33,940,000.00 USD | -69,600,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -32,060,000.00 USD | -84,570,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -61,030,000.00 USD | -113,700,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -159,080,000.00 USD | -435,750,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+580.00K` | 15m=`-734.74K` | 1h=`-3.59M` | 24h=`-32.06M`
* Futures Capital Netflows: 5m=`+143.26K` | 15m=`-1.89M` | 1h=`-2.19M` | 24h=`-84.57M`
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
  * `2026-10-30 08:33:58 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:32:58 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:00:58 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:48:58 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:47:58 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:47:58 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 08:47:58 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:58 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:58 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:58 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:58 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:58 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:58 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:49:58 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:49:58 IST`: [investinglive.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `697.42` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `683.71` (Risk Distance: `13.71` pts)
  * +2.5R Take Profit: `731.71`
  * Mathematical Lot Sizing: **`0.72 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `714.01` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `727.72` (Risk Distance: `13.71` pts)
  * +2.5R Take Profit: `679.72`
  * Mathematical Lot Sizing: **`0.72 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`712.15`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
