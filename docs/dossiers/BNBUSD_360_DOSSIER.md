# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BNB
**Canonical Key**: `BNB` | **Broker Instrument**: `BNBUSD.p` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 04:13:47 IST` (`2026-10-29 22:43:47 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `697.90` | **Live Ask Quote**: `701.10` | **Mid Price**: `699.50`
- **Spread Points**: `320.00` | **Spread BPS**: `45.75 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `732.65` | VWAP Z-Score: `-1.68` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `9.14` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `28.26` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `794.86` | Lower -3.00σ Band: `670.44`
  * Upper +2.51σ Band: `784.70` | Lower -2.51σ Band: `680.60`
  * Upper +2.01σ Band: `774.33` | Lower -2.01σ Band: `690.97`
  * Upper +2.00σ Band: `774.12` | Lower -2.00σ Band: `691.17`
  * Upper +1.28σ Band: `759.19` | Lower -1.28σ Band: `706.10`
  * Upper +1.00σ Band: `753.38` | Lower -1.00σ Band: `711.91`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`709.03` | EMA-20=`720.71` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`733.25` (Slope: `+0.0000`) | EMA-100=`739.86`
  * Institutional Anchors: EMA-144=`741.95` | EMA-200=`742.57` (Slope: `-0.4849`) | EMA-233=`742.53`
- **Range Boundaries**: 24H High=`759.80` | 24H Low=`677.20` | Weekly High=`760.90` | Weekly Low=`677.20`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `714.05` (Distance: `-2.04%`)
  * Point of Control (POC) = `706.96` (Distance: `-1.06%`)
  * Value Area Low (VAL) = `700.10` (Distance: `-0.09%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`754.57` | POC=`744.11` | VAL=`738.60`
  * Prior Day Extremes: PDH=`759.80` | PDL=`677.20` | PDC=`696.20`
  * Monday Range Blueprint: High=`746.00` | Mid=`738.45` | Low=`730.90`
  * Developing Weekly Value Area: Weekly VAH=`751.13` | Weekly POC=`740.53` | Weekly VAL=`734.95`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`724.00` | Low=`689.70`
  * London Session (08:00-16:00 UTC): High=`702.30` | Low=`696.70`
  * New York Session (13:00-21:00 UTC): High=`703.70` | Low=`695.30`
  * Initial Balance (First Hour): IB High=`701.60` | IB Low=`697.40`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `696.70` - `702.30`
  * Optimal Trade Entry (OTE 0.705): `700.90`
  * Structural Invalidation Anchor (0.786): `705.10`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `703.70` | `706.21` | `703.01` | `705.32` | `8,225` | 5,794,401.52 USD | 142,305.98 USD | `+2.46%` | -27,374,476.34 USD | `-0.30` | **`BULLISH`** | `NEUTRAL CHOP` |
| `5m` | `705.31` | `705.74` | `701.00` | `701.00` | `12,201` | 8,589,064.52 USD | 408,515.54 USD | `+4.76%` | -26,965,960.80 USD | `-0.18` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `701.01` | `703.59` | `700.00` | `701.29` | `14,241` | 9,989,047.44 USD | -316,639.10 USD | `-3.17%` | -27,282,599.90 USD | `-0.28` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `708.58` | `708.89` | `700.81` | `703.74` | `30,348` | 21,370,966.63 USD | -2,101,576.78 USD | `-9.83%` | -26,732,199.41 USD | `-0.22` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `703.71` | `706.21` | `701.00` | `701.00` | `26,877` | 18,920,983.07 USD | 253,731.35 USD | `+1.34%` | -26,478,468.06 USD | `+0.07` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `701.01` | `703.59` | `700.00` | `701.13` | `14,195` | 9,957,284.31 USD | -345,120.93 USD | `-3.47%` | -26,823,589.00 USD | `-0.01` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `745.34` | `745.53` | `677.76` | `697.34` | `772,178` | 547,049,922.28 USD | -28,994,090.87 USD | `-5.30%` | -47,816,369.31 USD | `-3.64` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `697.33` | `727.80` | `690.87` | `708.57` | `539,232` | 382,207,739.86 USD | 23,645,514.63 USD | `+6.19%` | -24,170,854.68 USD | `+2.64` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `708.58` | `708.89` | `700.00` | `701.29` | `71,465` | 50,280,997.15 USD | -2,164,484.53 USD | `-4.30%` | -26,335,339.21 USD | `-0.13` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `740.45` | `753.64` | `739.55` | `750.62` | `148,938` | 111,099,080.67 USD | 8,045,498.44 USD | `+7.24%` | -17,010,604.60 USD | `+1.70` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `750.62` | `754.90` | `743.07` | `745.33` | `88,414` | 66,199,547.89 USD | 232,195.88 USD | `+0.35%` | -16,778,408.72 USD | `+0.53` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `745.34` | `745.53` | `677.76` | `701.13` | `1,382,830` | 979,506,896.16 USD | -7,541,542.60 USD | `-0.77%` | -24,319,951.31 USD | `-0.55` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `747.26` | `759.90` | `745.75` | `748.51` | `156,800` | 118,182,602.62 USD | -8,240,157.99 USD | `-6.97%` | -14,715,810.54 USD | `-1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `748.51` | `753.57` | `738.70` | `740.45` | `333,019` | 248,636,999.78 USD | -10,340,292.49 USD | `-4.16%` | -25,056,103.04 USD | `-1.26` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `740.45` | `753.64` | `739.55` | `750.62` | `148,938` | 111,099,080.67 USD | 8,045,498.44 USD | `+7.24%` | -17,010,604.60 USD | `+1.70` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `750.62` | `754.90` | `743.07` | `745.33` | `88,414` | 66,199,547.89 USD | 232,195.88 USD | `+0.35%` | -16,778,408.72 USD | `+0.53` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `745.34` | `745.53` | `677.76` | `701.13` | `1,382,830` | 979,506,896.16 USD | -7,541,542.60 USD | `-0.77%` | -24,319,951.31 USD | `-0.55` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`699.50`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `699.73` | `7284000000.0000` | 5,096.83 USD | 85,056.71 USD | `2 orders` | `-0.09%` | `-` |
| `BID` | `699.75` | `6041000000.0000` | 4,227.19 USD | 79,959.88 USD | `1 orders` | `-0.08%` | `-` |
| `BID` | `699.76` | `150000000.0000` | 104.96 USD | 75,732.69 USD | `1 orders` | `-0.08%` | `-` |
| `BID` | `699.78` | `150000000.0000` | 104.97 USD | 75,627.73 USD | `1 orders` | `-0.08%` | `-` |
| `BID` | `699.80` | `150000000.0000` | 104.97 USD | 75,522.76 USD | `1 orders` | `-0.08%` | `-` |
| `BID` | `699.81` | `6299000000.0000` | 4,408.10 USD | 75,417.79 USD | `3 orders` | `-0.07%` | `-` |
| `BID` | `699.86` | `6061000000.0000` | 4,241.85 USD | 71,009.69 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `699.87` | `6033000000.0000` | 4,222.32 USD | 66,767.83 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `699.88` | `5942000000.0000` | 4,158.69 USD | 62,545.52 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `699.93` | `5939000000.0000` | 4,156.88 USD | 58,386.83 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `699.99` | `5958000000.0000` | 4,170.54 USD | 54,229.95 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `700.00` | `13687000000.0000` | 9,580.90 USD | 50,059.41 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `700.04` | `4461000000.0000` | 3,122.88 USD | 40,478.51 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `700.05` | `1000000000.0000` | 700.05 USD | 37,355.63 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `700.06` | `5930000000.0000` | 4,151.36 USD | 36,655.58 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `700.14` | `5944000000.0000` | 4,161.63 USD | 32,504.22 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `700.18` | `18236000000.0000` | 12,768.48 USD | 28,342.59 USD | `5 orders` | `-0.02%` | `-` |
| `BID` | `700.24` | `5932000000.0000` | 4,153.82 USD | 15,574.11 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `700.28` | `10378000000.0000` | 7,267.51 USD | 11,420.28 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `700.30` | `5930000000.0000` | 4,152.78 USD | 4,152.78 USD | `1 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `700.33` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 700.33` | `0.00%` | `-` |
| `ASK` | `700.36` | `2598000000.0000` | 1,819.54 USD | 1,819.54 USD | `2 orders` | `+0.00%` | `-` |
| `ASK` | `700.37` | `5929000000.0000` | 4,152.49 USD | 5,972.03 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `700.39` | `1000000000.0000` | 700.39 USD | 6,672.42 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `700.41` | `12690000000.0000` | 8,888.20 USD | 15,560.62 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `700.42` | `5935000000.0000` | 4,156.99 USD | 19,717.61 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `700.46` | `9517000000.0000` | 6,666.28 USD | 26,383.89 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `700.47` | `6040000000.0000` | 4,230.84 USD | 30,614.73 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `700.50` | `8286000000.0000` | 5,804.34 USD | 36,419.07 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `700.52` | `15000000.0000` | 10.51 USD | 36,429.58 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `700.53` | `6029000000.0000` | 4,223.50 USD | 40,653.08 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `700.54` | `15860000000.0000` | 11,110.56 USD | 51,763.64 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `700.55` | `1584000000.0000` | 1,109.67 USD | 52,873.31 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `700.56` | `713000000.0000` | 499.50 USD | 53,372.81 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `700.59` | `6108000000.0000` | 4,279.20 USD | 57,652.02 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `700.62` | `15235000000.0000` | 10,673.95 USD | 68,325.96 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `700.64` | `8285000000.0000` | 5,804.80 USD | 74,130.76 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `700.65` | `30500000000.0000` | 21,369.83 USD | 95,500.59 USD | `3 orders` | `+0.05%` | `-` |
| `ASK` | `700.66` | `5929000000.0000` | 4,154.21 USD | 99,654.80 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `700.67` | `43171000000.0000` | 30,248.62 USD | 129,903.43 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `700.68` | `150000000.0000` | 105.10 USD | 130,008.53 USD | `1 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:05:52 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `793` | `0xea00...a918` | `LONG` | 2,867,219.94 USD | `4,098,429,000,000.00` | `787.24` | `702.56` | `0.000000` | -359,206.84 USD | `-12.53%` | `5X Cross` |
| `867` | `0xb23b...4852` | `SHORT` | 2,593,975.41 USD | `3,703,087,000,000.00` | `702.34` | `702.56` | `3594.19` | 6,860.40 USD | `+0.26%` | `5X Cross` |
| `921` | `0xfe7c...b7ae` | `LONG` | 2,446,127.61 USD | `3,491,575,000,000.00` | `686.05` | `702.56` | `0.000000` | 50,716.75 USD | `+2.07%` | `10X Cross` |
| `1036` | `0x39b4...5c34` | `SHORT` | 2,117,819.50 USD | `3,025,007,000,000.00` | `707.72` | `702.56` | `834.41` | 23,023.70 USD | `+1.09%` | `10X Cross` |
| `1142` | `0xcac1...26b3` | `LONG` | 1,952,274.32 USD | `2,789,043,000,000.00` | `679.91` | `702.56` | `0.000000` | 55,963.16 USD | `+2.87%` | `10X Cross` |
| `1203` | `0x7737...bf66` | `SHORT` | 1,851,478.52 USD | `2,646,179,000,000.00` | `752.73` | `702.56` | `6719.03` | 140,392.06 USD | `+7.58%` | `10X Cross` |
| `1305` | `0x5b67...c66a` | `SHORT` | 1,702,065.75 USD | `2,429,891,000,000.00` | `691.70` | `702.56` | `946.92` | -21,307.32 USD | `-1.25%` | `10X Cross` |
| `1358` | `0xc675...795d` | `LONG` | 1,634,147.29 USD | `2,335,694,000,000.00` | `706.91` | `702.56` | `651.36` | -16,970.59 USD | `-1.04%` | `10X Cross` |
| `1381` | `0x7d0c...1b28` | `LONG` | 1,601,927.75 USD | `2,284,617,000,000.00` | `705.98` | `702.56` | `0.000000` | -10,958.73 USD | `-0.68%` | `10X Cross` |
| `1444` | `0xab04...8b69` | `SHORT` | 1,538,040.40 USD | `2,198,328,000,000.00` | `696.91` | `702.56` | `1041.21` | -5,998.22 USD | `-0.39%` | `10X Cross` |
| `1514` | `0x2edd...8179` | `LONG` | 1,444,471.73 USD | `2,063,590,000,000.00` | `714.56` | `702.56` | `0.000000` | -30,089.70 USD | `-2.08%` | `10X Cross` |
| `1559` | `0x325e...9564` | `LONG` | 1,399,960.00 USD | `2,000,000,000,000.00` | `713.23` | `702.56` | `0.000000` | -26,499.80 USD | `-1.89%` | `10X Cross` |
| `1560` | `0x4420...4c4b` | `LONG` | 1,399,899.59 USD | `1,998,606,000,000.00` | `704.51` | `702.56` | `321.40` | -8,132.66 USD | `-0.58%` | `10X Cross` |
| `1680` | `0xb69e...033a` | `LONG` | 1,262,390.36 USD | `1,795,655,000,000.00` | `772.94` | `702.56` | `619.50` | -125,541.36 USD | `-9.94%` | `10X Cross` |
| `1726` | `0x07fd...689d` | `LONG` | 1,221,824.22 USD | `1,744,292,000,000.00` | `714.81` | `702.56` | `0.000000` | -25,021.59 USD | `-2.05%` | `10X Cross` |
| `1737` | `0x645b...87b8` | `LONG` | 1,205,966.70 USD | `1,721,457,000,000.00` | `747.36` | `702.56` | `0.000000` | -80,577.06 USD | `-6.68%` | `10X Cross` |
| `1866` | `0x023a...2355` | `LONG` | 1,101,832.22 USD | `1,574,091,000,000.00` | `714.42` | `702.56` | `0.000000` | -22,729.84 USD | `-2.06%` | `10X Cross` |
| `1919` | `0xa4a6...46cf` | `SHORT` | 1,051,489.12 USD | `1,500,948,000,000.00` | `713.79` | `702.56` | `1904.17` | 19,868.59 USD | `+1.89%` | `10X Cross` |
| `1923` | `0x14c6...b280` | `SHORT` | 1,049,310.00 USD | `1,500,000,000,000.00` | `712.51` | `702.56` | `1463.07` | 19,451.70 USD | `+1.85%` | `10X Cross` |
| `1996` | `0xbf5a...88ba` | `SHORT` | 1,006,639.56 USD | `1,439,105,000,000.00` | `718.16` | `702.56` | `1969.39` | 26,867.39 USD | `+2.67%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`758.49` (Vol: 2,400,000.00 USD, Dist: `+7.79%`) | Long MP=`677.61` (Vol: 3,100,000.00 USD, Dist: `--3.70%`)
  * 48H Horizon: Short MP=`767.93` (Vol: 3,000,000.00 USD, Dist: `+9.13%`) | Long MP=`677.29` (Vol: 3,100,000.00 USD, Dist: `--3.75%`)
  * 3D Horizon: Short MP=`767.93` (Vol: 3,400,000.00 USD, Dist: `+9.13%`) | Long MP=`677.29` (Vol: 3,100,000.00 USD, Dist: `--3.75%`)
  * 7D Horizon: Short MP=`767.93` (Vol: 3,500,000.00 USD, Dist: `+9.13%`) | Long MP=`677.29` (Vol: 3,100,000.00 USD, Dist: `--3.75%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `141.50` | 5,340.00 USD | 7,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `142.50` | 174.28 USD | 7,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `143.50` | 88,970.00 USD | 7,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `144.50` | 2,020.00 USD | 7,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `147.50` | 2,830.00 USD | 7,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `160.50` | 971.02 USD | 7,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `162.50` | 812.50 USD | 7,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `178.50` | 239.90 USD | 7,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `182.50` | 23,210.00 USD | 7,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `190.50` | 20,420.00 USD | 6,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `193.50` | 1,380.00 USD | 6,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `197.50` | 242.73 USD | 6,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `204.50` | 250.92 USD | 6,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `210.50` | 7,180.00 USD | 6,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `212.50` | 170.00 USD | 6,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `219.50` | 191.18 USD | 6,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `221.50` | 221,500.00 USD | 6,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `240.50` | 16,700.00 USD | 6,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `246.50` | 17,060.00 USD | 6,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `247.50` | 368.53 USD | 6,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `262.50` | 27,880.00 USD | 6,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `264.50` | 1,400.00 USD | 6,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `267.50` | 535.00 USD | 6,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `268.50` | 21,690.00 USD | 6,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `278.50` | 1,950.00 USD | 6,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `287.50` | 20,120.00 USD | 6,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `288.50` | 383.42 USD | 6,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `292.50` | 12,410.00 USD | 6,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `299.50` | 1,890.00 USD | 6,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `309.50` | 317.86 USD | 6,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `313.50` | 501.60 USD | 6,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `314.50` | 5,100.00 USD | 6,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `322.50` | 129,000.00 USD | 6,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `323.50` | 3,190.00 USD | 6,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `324.50` | 1,020.00 USD | 6,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `326.50` | 500.85 USD | 6,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `328.50` | 315.03 USD | 6,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `330.50` | 308.36 USD | 6,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `331.50` | 9,130.00 USD | 6,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `332.50` | 175,560.00 USD | 6,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `333.50` | 377.19 USD | 6,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `334.50` | 118.08 USD | 6,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `335.50` | 14,260.00 USD | 6,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `337.50` | 933.86 USD | 6,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `342.50` | 490.80 USD | 6,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `343.50` | 652.65 USD | 6,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `357.50` | 1,490.00 USD | 6,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `359.50` | 212.10 USD | 6,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `360.50` | 1,620.00 USD | 6,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `364.50` | 1,890.00 USD | 6,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `366.50` | 549.75 USD | 6,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `370.50` | 1,220.00 USD | 6,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `374.50` | 1,820.00 USD | 6,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `377.50` | 451.87 USD | 6,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `378.50` | 7,760.00 USD | 6,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `379.50` | 645.15 USD | 6,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `380.50` | 163.62 USD | 6,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `382.50` | 1,910.00 USD | 6,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `383.50` | 10,900.00 USD | 6,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `385.50` | 2,860.00 USD | 6,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `386.50` | 531.44 USD | 6,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `388.50` | 602.95 USD | 6,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `393.50` | 103.88 USD | 6,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `394.50` | 168.06 USD | 6,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `395.50` | 2,110.00 USD | 6,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `396.50` | 396.50 USD | 6,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `397.50` | 318.00 USD | 6,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `398.50` | 523.63 USD | 6,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `400.50` | 605.16 USD | 6,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `404.50` | 102.34 USD | 6,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `405.50` | 1,280.00 USD | 6,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `410.50` | 614.52 USD | 6,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `411.50` | 106.17 USD | 6,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `412.50` | 12,360.00 USD | 6,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `414.50` | 13,320.00 USD | 6,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `415.50` | 1,810.00 USD | 6,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `417.50` | 8,500.00 USD | 6,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `418.50` | 5,680.00 USD | 6,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `420.50` | 10,650.00 USD | 6,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `421.50` | 2,320.00 USD | 6,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `423.50` | 1,450.00 USD | 6,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `427.50` | 29,930.00 USD | 6,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `429.50` | 615.04 USD | 6,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `430.50` | 638.00 USD | 6,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `432.50` | 3,340.00 USD | 6,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `438.50` | 1,790.00 USD | 6,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `444.50` | 949.90 USD | 6,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `452.50` | 1,210.00 USD | 6,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `453.50` | 7,610.00 USD | 6,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `456.50` | 4,730.00 USD | 6,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `460.50` | 37,040.00 USD | 6,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `470.50` | 4,510.00 USD | 6,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `472.50` | 131,830.00 USD | 6,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `476.50` | 5,330.00 USD | 5,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `478.50` | 2,170.00 USD | 5,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `482.50` | 7,330.00 USD | 5,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `484.50` | 58,270.00 USD | 5,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `485.50` | 52,350.00 USD | 5,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `487.50` | 204.75 USD | 5,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `488.50` | 257.44 USD | 5,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `489.50` | 6,030.00 USD | 5,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `493.50` | 41,030.00 USD | 5,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `494.50` | 1,410.00 USD | 5,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `496.50` | 1,320.00 USD | 5,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `498.50` | 1,420.00 USD | 5,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `501.50` | 7,760.00 USD | 5,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `502.50` | 109.04 USD | 5,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `505.50` | 5,760.00 USD | 5,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `508.50` | 992.08 USD | 5,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `509.50` | 3,100.00 USD | 5,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `511.50` | 4,090.00 USD | 5,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `512.50` | 5,190.00 USD | 5,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `513.50` | 3,090.00 USD | 5,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `514.50` | 4,120.00 USD | 5,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `515.50` | 3,930.00 USD | 5,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `516.50` | 2,550.00 USD | 5,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `517.50` | 22,650.00 USD | 5,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `518.50` | 7,540.00 USD | 5,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `519.50` | 968.35 USD | 5,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `520.50` | 532.47 USD | 5,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `521.50` | 838.05 USD | 5,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `522.50` | 2,350.00 USD | 5,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `523.50` | 2,090.00 USD | 5,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `525.50` | 835.02 USD | 5,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `526.50` | 1,700.00 USD | 5,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `529.50` | 43,700.00 USD | 5,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `530.50` | 17,770.00 USD | 5,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `531.50` | 1,070.00 USD | 5,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `532.50` | 632.08 USD | 5,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `533.50` | 1,320.00 USD | 5,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `534.50` | 1,630.00 USD | 5,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `535.50` | 3,250.00 USD | 5,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `536.50` | 100.33 USD | 5,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `539.50` | 2,150.00 USD | 5,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `540.50` | 1,760.00 USD | 5,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `541.50` | 472.19 USD | 5,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `543.50` | 334.25 USD | 5,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `545.50` | 212,310.00 USD | 5,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `546.50` | 491.85 USD | 5,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `547.50` | 531.07 USD | 5,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `548.50` | 1,580.00 USD | 5,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `549.50` | 1,770.00 USD | 5,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `550.50` | 1,700.00 USD | 5,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `552.50` | 959.69 USD | 5,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `553.50` | 2,730.00 USD | 5,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `554.50` | 2,010.00 USD | 5,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `555.50` | 274.97 USD | 5,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `557.50` | 5,680.00 USD | 5,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `559.50` | 15,990.00 USD | 5,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `560.50` | 3,450.00 USD | 5,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `561.50` | 583.40 USD | 5,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `562.50` | 10,240.00 USD | 5,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `565.50` | 160,430.00 USD | 5,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `566.50` | 453.20 USD | 5,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `567.50` | 24,450.00 USD | 5,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `568.50` | 20,310.00 USD | 5,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `569.50` | 144.08 USD | 5,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `570.50` | 296.09 USD | 5,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `571.50` | 1,030.00 USD | 5,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `572.50` | 722,500.00 USD | 5,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `574.50` | 610.69 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `576.50` | 416.23 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `578.50` | 5,790.00 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `579.50` | 1,860.00 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `581.50` | 35,070.00 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `582.50` | 274.94 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `583.50` | 313.34 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `584.50` | 3,060.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `586.50` | 826.96 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `587.50` | 3,560.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `588.50` | 271.89 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `589.50` | 203.38 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `590.50` | 5,360.00 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `591.50` | 4,670.00 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `592.50` | 840.76 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `593.50` | 255,210.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `594.50` | 45,110.00 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `595.50` | 12,660.00 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `596.50` | 15,090.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `597.50` | 311.30 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `598.50` | 217.26 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `599.50` | 116.90 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `600.50` | 5,150.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `601.50` | 58,030.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `602.50` | 16,910.00 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `604.50` | 1,610.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `606.10` | 37,790,000.00 USD | 37,790,000.00 USD | 42,510.00 USD | 3,960.00 USD | 13,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `606.50` | 169.82 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `607.20` | 37,730,000.00 USD | 37,730,000.00 USD | 49,710.00 USD | 7,560.00 USD | 5,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `607.50` | 1,880.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `608.30` | 37,670,000.00 USD | 37,670,000.00 USD | 11,850.00 USD | 4,880.00 USD | 3,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `609.40` | 37,650,000.00 USD | 37,650,000.00 USD | 11,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `610.50` | 213.67 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `613.50` | 12,270.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `614.50` | 1,440.00 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `615.50` | 8,870.00 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `616.00` | 37,640,000.00 USD | 37,640,000.00 USD | 0.00 USD | 0.00 USD | 295,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `616.50` | 1,540.00 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `617.10` | 37,340,000.00 USD | 37,340,000.00 USD | 290,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `617.50` | 156.23 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `618.50` | 9,040.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `619.30` | 37,050,000.00 USD | 37,050,000.00 USD | 0.00 USD | 33,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `620.40` | 37,020,000.00 USD | 37,020,000.00 USD | 175,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `620.50` | 5,410.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `621.50` | 36,840,000.00 USD | 36,840,000.00 USD | 0.00 USD | 35,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `621.50` | 3,230.00 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `623.50` | 1,050.00 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `623.70` | 36,810,000.00 USD | 36,810,000.00 USD | 460,160.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `624.50` | 16,600.00 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `624.80` | 36,350,000.00 USD | 36,350,000.00 USD | 238,630.00 USD | 31,450.00 USD | 274,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `625.50` | 25,330.00 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `625.90` | 35,810,000.00 USD | 35,810,000.00 USD | 224,870.00 USD | 44,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `627.00` | 35,540,000.00 USD | 35,540,000.00 USD | 186,500.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `627.50` | 326.30 USD | 3,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `628.50` | 9,420.00 USD | 3,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `629.50` | 1,150,000.00 USD | 3,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `630.50` | 252,440.00 USD | 2,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `631.40` | 35,350,000.00 USD | 35,350,000.00 USD | 0.00 USD | 10,840.00 USD | 812,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `632.50` | 34,530,000.00 USD | 34,530,000.00 USD | 473,380.00 USD | 42,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `632.50` | 125.87 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `633.50` | 4,540.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `633.60` | 34,010,000.00 USD | 34,010,000.00 USD | 7,730.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `634.70` | 34,000,000.00 USD | 34,000,000.00 USD | 11,290.00 USD | 23,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `635.50` | 5,910.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `636.50` | 155.31 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `636.90` | 33,970,000.00 USD | 33,970,000.00 USD | 101,910.00 USD | 40,910.00 USD | 236,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `637.50` | 1,110.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `638.50` | 432.90 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `639.10` | 33,590,000.00 USD | 33,590,000.00 USD | 184,100.00 USD | 37,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `639.50` | 746.30 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `640.20` | 33,370,000.00 USD | 33,370,000.00 USD | 0.00 USD | 0.00 USD | 184,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `640.50` | 97,540.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `641.50` | 1,670.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `642.40` | 33,180,000.00 USD | 33,180,000.00 USD | 150,090.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `642.50` | 8,970.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `644.50` | 3,470.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `644.60` | 33,030,000.00 USD | 33,030,000.00 USD | 308,550.00 USD | 0.00 USD | 341,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `645.50` | 2,070.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `646.50` | 463.54 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `646.80` | 32,380,000.00 USD | 32,380,000.00 USD | 217,880.00 USD | 0.00 USD | 140,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `647.90` | 32,020,000.00 USD | 32,020,000.00 USD | 106,400.00 USD | 29,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `648.50` | 5,190.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `649.00` | 31,890,000.00 USD | 31,890,000.00 USD | 92,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `649.50` | 1,120.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `650.50` | 2,930.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `651.20` | 31,790,000.00 USD | 31,790,000.00 USD | 106,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `651.50` | 1,520,000.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `652.30` | 31,690,000.00 USD | 31,690,000.00 USD | 0.00 USD | 0.00 USD | 94,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `652.50` | 1,420.00 USD | 803,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `653.40` | 31,590,000.00 USD | 31,590,000.00 USD | 0.00 USD | 26,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `653.50` | 298.00 USD | 802,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `654.50` | 31,570,000.00 USD | 31,570,000.00 USD | 56,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `654.50` | 97,530.00 USD | 801,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `655.60` | 31,510,000.00 USD | 31,510,000.00 USD | 138,350.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `656.50` | 122.77 USD | 704,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `656.70` | 31,370,000.00 USD | 31,370,000.00 USD | 22,490.00 USD | 21,320.00 USD | 825,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `657.80` | 30,500,000.00 USD | 30,500,000.00 USD | 833,200.00 USD | 14,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `658.50` | 1,540.00 USD | 704,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `658.90` | 29,650,000.00 USD | 29,650,000.00 USD | 64,090.00 USD | 0.00 USD | 81,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `659.50` | 313,710.00 USD | 702,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `660.00` | 29,510,000.00 USD | 29,510,000.00 USD | 90,670.00 USD | 7,460.00 USD | 14,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `660.50` | 46,960.00 USD | 388,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `661.10` | 29,400,000.00 USD | 29,400,000.00 USD | 0.00 USD | 83,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `661.50` | 1,070.00 USD | 341,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `662.20` | 29,310,000.00 USD | 29,310,000.00 USD | 445,210.00 USD | 87,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `662.50` | 111,140.00 USD | 340,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `663.30` | 28,780,000.00 USD | 28,780,000.00 USD | 202,560.00 USD | 5,000.00 USD | 19,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `663.50` | 2,590.00 USD | 229,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `664.10` | 87,050,000.00 USD | 87,050,000.00 USD | 78,740.00 USD | 18,740.00 USD | 39,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `664.40` | 28,550,000.00 USD | 28,550,000.00 USD | 1,200,000.00 USD | 48,410.00 USD | 21,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `664.50` | 37,920.00 USD | 227,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `665.00` | 86,910,000.00 USD | 86,910,000.00 USD | 92,030.00 USD | 22,990.00 USD | 37,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `665.50` | 27,290,000.00 USD | 27,290,000.00 USD | 671,470.00 USD | 4,540.00 USD | 11,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `665.50` | 131.10 USD | 189,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `665.90` | 86,760,000.00 USD | 86,760,000.00 USD | 264,020.00 USD | 71,380.00 USD | 63,410.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `666.50` | 794,320.00 USD | 794,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `666.60` | 26,600,000.00 USD | 26,600,000.00 USD | 686,090.00 USD | 102,050.00 USD | 696,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `666.80` | 86,360,000.00 USD | 86,360,000.00 USD | 198,550.00 USD | 33,320.00 USD | 61,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `667.50` | 2,550.00 USD | 796,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `667.70` | 25,110,000.00 USD | 25,110,000.00 USD | 205,320.00 USD | 115,700.00 USD | 9,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `667.70` | 86,070,000.00 USD | 86,070,000.00 USD | 199,690.00 USD | 45,130.00 USD | 51,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `668.50` | 1,770.00 USD | 798,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `668.60` | 85,770,000.00 USD | 85,770,000.00 USD | 387,530.00 USD | 92,860.00 USD | 51,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `668.80` | 24,780,000.00 USD | 24,780,000.00 USD | 562,170.00 USD | 25,520.00 USD | 3,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `669.50` | 85,240,000.00 USD | 85,240,000.00 USD | 341,150.00 USD | 38,130.00 USD | 108,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `669.50` | 70,020.00 USD | 868,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `669.90` | 24,190,000.00 USD | 24,190,000.00 USD | 253,070.00 USD | 61,020.00 USD | 1,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `670.40` | 84,750,000.00 USD | 84,750,000.00 USD | 319,660.00 USD | 93,800.00 USD | 77,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `670.50` | 8,260.00 USD | 876,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `671.00` | 22,390,000.00 USD | 22,390,000.00 USD | 143,770.00 USD | 8,380.00 USD | 10,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `671.30` | 84,260,000.00 USD | 84,260,000.00 USD | 335,750.00 USD | 57,500.00 USD | 42,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `671.50` | 115,780.00 USD | 189,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `672.10` | 22,230,000.00 USD | 22,230,000.00 USD | 2,020,000.00 USD | 11,460.00 USD | 35,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `672.20` | 83,830,000.00 USD | 83,830,000.00 USD | 180,230.00 USD | 62,620.00 USD | 74,250.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `672.50` | 11,590.00 USD | 888,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `673.10` | 83,510,000.00 USD | 83,510,000.00 USD | 394,120.00 USD | 64,970.00 USD | 42,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `673.20` | 20,160,000.00 USD | 20,160,000.00 USD | 348,680.00 USD | 73,200.00 USD | 2,140,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `673.50` | 18,880.00 USD | 73,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `674.00` | 83,010,000.00 USD | 83,010,000.00 USD | 335,670.00 USD | 105,910.00 USD | 80,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `674.30` | 17,610,000.00 USD | 17,610,000.00 USD | 225,430.00 USD | 306,330.00 USD | 111,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `674.50` | 8,680.00 USD | 54,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `674.90` | 82,490,000.00 USD | 82,490,000.00 USD | 247,070.00 USD | 31,490.00 USD | 44,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `675.40` | 16,960,000.00 USD | 16,960,000.00 USD | 2,030,000.00 USD | 46,170.00 USD | 249,580.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `675.50` | 14,390.00 USD | 45,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `675.80` | 82,160,000.00 USD | 82,160,000.00 USD | 387,400.00 USD | 26,020.00 USD | 79,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `676.50` | 14,640,000.00 USD | 14,640,000.00 USD | 385,420.00 USD | 289,950.00 USD | 74,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `676.50` | 1,940.00 USD | 31,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `676.70` | 81,670,000.00 USD | 81,670,000.00 USD | 509,100.00 USD | 35,490.00 USD | 126,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `677.50` | 983.73 USD | 29,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `677.60` | 13,890,000.00 USD | 13,890,000.00 USD | 374,010.00 USD | 118,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `677.60` | 81,000,000.00 USD | 81,000,000.00 USD | 409,810.00 USD | 0.00 USD | 63,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `678.50` | 80,530,000.00 USD | 80,530,000.00 USD | 120,190.00 USD | 0.00 USD | 26,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `678.50` | 14,770.00 USD | 28,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `678.70` | 13,400,000.00 USD | 13,400,000.00 USD | 1,030,000.00 USD | 111,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `679.40` | 80,380,000.00 USD | 80,380,000.00 USD | 116,510.00 USD | 10,480.00 USD | 40,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `679.50` | 1,260.00 USD | 889,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `679.80` | 12,260,000.00 USD | 12,260,000.00 USD | 1,200,000.00 USD | 167,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `680.30` | 80,210,000.00 USD | 80,210,000.00 USD | 166,780.00 USD | 13,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `680.50` | 2,010.00 USD | 13,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `680.90` | 10,900,000.00 USD | 10,900,000.00 USD | 13,920.00 USD | 99,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `681.20` | 80,030,000.00 USD | 80,030,000.00 USD | 106,280.00 USD | 7,050.00 USD | 35,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `681.50` | 11,580.00 USD | 11,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `682.00` | 10,780,000.00 USD | 10,780,000.00 USD | 34,310.00 USD | 305,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `682.10` | 79,880,000.00 USD | 79,880,000.00 USD | 0.00 USD | 23,360.00 USD | 27,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `683.00` | 79,830,000.00 USD | 79,830,000.00 USD | 175,930.00 USD | 28,470.00 USD | 11,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `683.10` | 10,440,000.00 USD | 10,440,000.00 USD | 120,530.00 USD | 128,350.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `683.90` | 79,620,000.00 USD | 79,620,000.00 USD | 77,000.00 USD | 29,510.00 USD | 17,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `684.20` | 10,190,000.00 USD | 10,190,000.00 USD | 19,970.00 USD | 41,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `684.80` | 79,490,000.00 USD | 79,490,000.00 USD | 246,080.00 USD | 9,850.00 USD | 39,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `685.70` | 79,200,000.00 USD | 79,200,000.00 USD | 197,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `686.40` | 10,130,000.00 USD | 10,130,000.00 USD | 694,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `686.60` | 79,000,000.00 USD | 79,000,000.00 USD | 62,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `687.50` | 9,440,000.00 USD | 9,440,000.00 USD | 775,320.00 USD | 54,180.00 USD | 3,790,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `687.50` | 78,940,000.00 USD | 78,940,000.00 USD | 148,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `687.50` | 124.44 USD | 889,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `688.40` | 78,790,000.00 USD | 78,790,000.00 USD | 67,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `688.60` | 4,820,000.00 USD | 4,820,000.00 USD | 1,910,000.00 USD | 0.00 USD | 146,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `689.30` | 78,720,000.00 USD | 78,720,000.00 USD | 84,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `689.70` | 2,770,000.00 USD | 2,770,000.00 USD | 50,420.00 USD | 38,440.00 USD | 466,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `690.20` | 78,640,000.00 USD | 78,640,000.00 USD | 283,920.00 USD | 63,230.00 USD | 82,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `690.80` | 2,210,000.00 USD | 2,210,000.00 USD | 361,400.00 USD | 146,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `691.10` | 78,210,000.00 USD | 78,210,000.00 USD | 362,020.00 USD | 61,370.00 USD | 81,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `691.90` | 1,710,000.00 USD | 1,710,000.00 USD | 27,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `692.00` | 77,700,000.00 USD | 77,700,000.00 USD | 322,430.00 USD | 18,850.00 USD | 58,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `692.90` | 77,300,000.00 USD | 77,300,000.00 USD | 280,830.00 USD | 19,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `693.80` | 77,000,000.00 USD | 77,000,000.00 USD | 305,720.00 USD | 39,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `694.70` | 76,660,000.00 USD | 76,660,000.00 USD | 279,840.00 USD | 36,640.00 USD | 35,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `695.60` | 76,300,000.00 USD | 76,300,000.00 USD | 120,440.00 USD | 0.00 USD | 21,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `696.30` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 137,440.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `696.50` | 76,160,000.00 USD | 76,160,000.00 USD | 140,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `697.40` | 76,020,000.00 USD | 76,020,000.00 USD | 189,100.00 USD | 19,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `698.30` | 75,810,000.00 USD | 75,810,000.00 USD | 273,520.00 USD | 33,120.00 USD | 54,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `699.20` | 75,450,000.00 USD | 75,450,000.00 USD | 274,810.00 USD | 12,670.00 USD | 11,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `700.10` | 75,150,000.00 USD | 75,150,000.00 USD | 225,450.00 USD | 40,820.00 USD | 27,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `701.00` | 74,860,000.00 USD | 74,860,000.00 USD | 237,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `701.80` | 1,540,000.00 USD | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `701.90` | 74,620,000.00 USD | 74,620,000.00 USD | 135,260.00 USD | 41,260.00 USD | 89,700.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `702.50` | 848,660.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `702.80` | 74,360,000.00 USD | 74,360,000.00 USD | 416,820.00 USD | 57,470.00 USD | 36,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `703.70` | 73,840,000.00 USD | 73,840,000.00 USD | 311,800.00 USD | 44,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `704.60` | 73,490,000.00 USD | 73,490,000.00 USD | 537,050.00 USD | 136,550.00 USD | 194,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `705.10` | 96,830.00 USD | 96,830.00 USD | 0.00 USD | 96,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `705.50` | 72,620,000.00 USD | 72,620,000.00 USD | 920,340.00 USD | 162,820.00 USD | 236,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `706.40` | 71,300,000.00 USD | 71,300,000.00 USD | 523,540.00 USD | 104,380.00 USD | 231,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `707.30` | 70,440,000.00 USD | 70,440,000.00 USD | 604,060.00 USD | 90,200.00 USD | 53,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `708.20` | 69,690,000.00 USD | 69,690,000.00 USD | 796,640.00 USD | 138,200.00 USD | 42,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `709.10` | 68,710,000.00 USD | 68,710,000.00 USD | 392,150.00 USD | 156,040.00 USD | 195,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `710.00` | 67,970,000.00 USD | 67,970,000.00 USD | 450,480.00 USD | 167,090.00 USD | 176,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `710.50` | 2,000.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `710.90` | 67,180,000.00 USD | 67,180,000.00 USD | 922,450.00 USD | 160,040.00 USD | 236,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `711.50` | 1,030.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `711.80` | 65,860,000.00 USD | 65,860,000.00 USD | 608,910.00 USD | 232,130.00 USD | 114,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `712.70` | 64,900,000.00 USD | 64,900,000.00 USD | 1,190,000.00 USD | 217,390.00 USD | 236,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `713.60` | 63,260,000.00 USD | 63,260,000.00 USD | 2,250,000.00 USD | 279,180.00 USD | 308,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `714.50` | 60,410,000.00 USD | 60,410,000.00 USD | 508,400.00 USD | 209,320.00 USD | 292,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `715.40` | 59,400,000.00 USD | 59,400,000.00 USD | 1,050,000.00 USD | 419,310.00 USD | 329,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `716.10` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 137,360.00 USD | 1,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `716.30` | 57,600,000.00 USD | 57,600,000.00 USD | 1,080,000.00 USD | 324,540.00 USD | 233,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `717.20` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 253,150.00 USD | 466,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `717.20` | 55,960,000.00 USD | 55,960,000.00 USD | 581,610.00 USD | 398,030.00 USD | 387,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `718.10` | 54,590,000.00 USD | 54,590,000.00 USD | 1,690,000.00 USD | 246,320.00 USD | 151,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `718.30` | 2,280,000.00 USD | 2,280,000.00 USD | 145,050.00 USD | 115,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `719.00` | 52,510,000.00 USD | 52,510,000.00 USD | 670,390.00 USD | 137,460.00 USD | 211,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `719.40` | 2,570,000.00 USD | 2,570,000.00 USD | 126,360.00 USD | 166,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `719.90` | 51,490,000.00 USD | 51,490,000.00 USD | 618,020.00 USD | 173,240.00 USD | 186,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `720.80` | 50,510,000.00 USD | 50,510,000.00 USD | 1,010,000.00 USD | 52,490.00 USD | 180,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `721.50` | 5,570.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `721.60` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 283,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `721.70` | 49,260,000.00 USD | 49,260,000.00 USD | 1,950,000.00 USD | 237,690.00 USD | 653,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `722.50` | 3,410.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `722.60` | 46,430,000.00 USD | 46,430,000.00 USD | 1,930,000.00 USD | 108,200.00 USD | 229,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `723.50` | 44,160,000.00 USD | 44,160,000.00 USD | 640,550.00 USD | 140,550.00 USD | 293,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `723.50` | 23,050.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `723.80` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 437,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `724.40` | 43,080,000.00 USD | 43,080,000.00 USD | 663,550.00 USD | 186,780.00 USD | 130,770.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `724.50` | 5,780.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `724.90` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 57,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `725.30` | 42,100,000.00 USD | 42,100,000.00 USD | 1,760,000.00 USD | 418,390.00 USD | 396,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `725.50` | 4,390.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `726.20` | 39,520,000.00 USD | 39,520,000.00 USD | 1,060,000.00 USD | 311,550.00 USD | 460,020.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `726.50` | 912.48 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `727.10` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 64,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `727.10` | 37,690,000.00 USD | 37,690,000.00 USD | 1,230,000.00 USD | 331,980.00 USD | 241,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `727.50` | 16,960.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `728.00` | 35,890,000.00 USD | 35,890,000.00 USD | 3,110,000.00 USD | 778,750.00 USD | 388,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `728.50` | 10,340.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `728.90` | 31,610,000.00 USD | 31,610,000.00 USD | 2,330,000.00 USD | 317,590.00 USD | 644,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `729.30` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 27,090.00 USD | 458,580.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `729.50` | 30,550.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `729.80` | 28,320,000.00 USD | 28,320,000.00 USD | 1,320,000.00 USD | 430,010.00 USD | 339,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `730.40` | 7,330,000.00 USD | 7,330,000.00 USD | 1,540,000.00 USD | 107,360.00 USD | 1,780,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `730.50` | 34,300.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `730.70` | 26,230,000.00 USD | 26,230,000.00 USD | 2,760,000.00 USD | 351,520.00 USD | 587,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `731.50` | 8,600,000.00 USD | 8,600,000.00 USD | 952,750.00 USD | 82,570.00 USD | 233,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `731.50` | 41,490.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `731.60` | 22,530,000.00 USD | 22,530,000.00 USD | 1,530,000.00 USD | 133,980.00 USD | 261,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `732.50` | 20,610,000.00 USD | 20,610,000.00 USD | 465,880.00 USD | 221,510.00 USD | 96,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `732.50` | 132,460.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `732.60` | 9,810,000.00 USD | 9,810,000.00 USD | 430,780.00 USD | 73,020.00 USD | 703,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `733.40` | 19,820,000.00 USD | 19,820,000.00 USD | 1,910,000.00 USD | 158,310.00 USD | 338,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `733.50` | 214,400.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `733.70` | 11,060,000.00 USD | 11,060,000.00 USD | 1,050,000.00 USD | 206,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `734.30` | 17,420,000.00 USD | 17,420,000.00 USD | 1,580,000.00 USD | 288,470.00 USD | 244,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `734.50` | 125,010.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `734.80` | 11,710,000.00 USD | 11,710,000.00 USD | 460,890.00 USD | 187,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `735.20` | 15,310,000.00 USD | 15,310,000.00 USD | 1,330,000.00 USD | 172,940.00 USD | 437,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `735.50` | 72,690.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `735.90` | 13,490,000.00 USD | 13,490,000.00 USD | 1,110,000.00 USD | 81,400.00 USD | 590,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `736.10` | 13,370,000.00 USD | 13,370,000.00 USD | 2,130,000.00 USD | 181,990.00 USD | 484,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `736.50` | 8,960.00 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `737.00` | 13,930,000.00 USD | 13,930,000.00 USD | 438,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `737.00` | 10,570,000.00 USD | 10,570,000.00 USD | 2,360,000.00 USD | 175,330.00 USD | 633,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `737.50` | 25,410.00 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `737.90` | 7,400,000.00 USD | 7,400,000.00 USD | 3,420,000.00 USD | 72,280.00 USD | 374,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `738.10` | 14,260,000.00 USD | 14,260,000.00 USD | 160,280.00 USD | 162,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `738.50` | 8,090.00 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `738.80` | 3,530,000.00 USD | 3,530,000.00 USD | 522,950.00 USD | 20,210.00 USD | 155,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `739.20` | 16,000,000.00 USD | 16,000,000.00 USD | 807,980.00 USD | 0.00 USD | 934,700.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `739.50` | 127,330.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `739.70` | 2,830,000.00 USD | 2,830,000.00 USD | 352,500.00 USD | 0.00 USD | 203,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `740.30` | 16,820,000.00 USD | 16,820,000.00 USD | 661,350.00 USD | 134,150.00 USD | 22,040.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `740.50` | 20,070.00 USD | 2,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `740.60` | 2,280,000.00 USD | 2,280,000.00 USD | 1,090,000.00 USD | 0.00 USD | 33,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `741.40` | 17,230,000.00 USD | 17,230,000.00 USD | 379,980.00 USD | 32,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `741.50` | 1,160,000.00 USD | 1,160,000.00 USD | 257,630.00 USD | 0.00 USD | 208,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `741.50` | 424.14 USD | 2,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `742.40` | 689,850.00 USD | 689,850.00 USD | 0.00 USD | 0.00 USD | 183,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `742.50` | 17,520,000.00 USD | 17,520,000.00 USD | 291,160.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `742.50` | 146,070.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `743.30` | 505,930.00 USD | 505,930.00 USD | 0.00 USD | 0.00 USD | 57,580.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `743.50` | 76,990.00 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `743.60` | 18,080,000.00 USD | 18,080,000.00 USD | 120,950.00 USD | 0.00 USD | 436,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `744.20` | 448,350.00 USD | 448,350.00 USD | 0.00 USD | 257,580.00 USD | 141,790.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `744.50` | 8,770.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `744.70` | 19,920,000.00 USD | 19,920,000.00 USD | 878,190.00 USD | 106,580.00 USD | 854,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `745.10` | 48,980.00 USD | 48,980.00 USD | 0.00 USD | 48,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `745.50` | 17,630.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `745.80` | 20,430,000.00 USD | 20,430,000.00 USD | 443,420.00 USD | 74,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `746.00` | 999,320.00 USD | 999,320.00 USD | 999,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `746.50` | 402,950.00 USD | 3,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `746.90` | 21,800,000.00 USD | 21,800,000.00 USD | 538,200.00 USD | 68,950.00 USD | 758,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `746.90` | 1,210,000.00 USD | 1,210,000.00 USD | 215,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `747.50` | 470.93 USD | 3,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `748.00` | 22,550,000.00 USD | 22,550,000.00 USD | 573,840.00 USD | 103,400.00 USD | 73,330.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `748.50` | 240,840.00 USD | 3,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `749.10` | 22,890,000.00 USD | 22,890,000.00 USD | 334,750.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `749.50` | 164,820.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `750.20` | 23,010,000.00 USD | 23,010,000.00 USD | 120,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `750.50` | 171,680.00 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `751.30` | 23,120,000.00 USD | 23,120,000.00 USD | 17,390.00 USD | 0.00 USD | 98,240.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `751.50` | 562,240.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `752.40` | 23,850,000.00 USD | 23,850,000.00 USD | 263,850.00 USD | 25,010.00 USD | 441,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `752.50` | 3,910.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `753.50` | 24,150,000.00 USD | 24,150,000.00 USD | 30,730.00 USD | 3,810.00 USD | 262,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `754.60` | 24,690,000.00 USD | 24,690,000.00 USD | 352,780.00 USD | 149,020.00 USD | 43,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `755.00` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 59,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `755.50` | 3,500.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `755.70` | 25,310,000.00 USD | 25,310,000.00 USD | 384,280.00 USD | 176,290.00 USD | 56,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `756.50` | 583.26 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `756.80` | 25,850,000.00 USD | 25,850,000.00 USD | 422,820.00 USD | 24,970.00 USD | 95,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `756.80` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 47,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `757.70` | 1,910,000.00 USD | 1,910,000.00 USD | 475,510.00 USD | 113,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `757.90` | 26,560,000.00 USD | 26,560,000.00 USD | 482,940.00 USD | 189,940.00 USD | 32,720.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `758.50` | 882,460.00 USD | 5,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `758.60` | 3,100,000.00 USD | 3,100,000.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `759.00` | 28,110,000.00 USD | 28,110,000.00 USD | 1,150,000.00 USD | 122,880.00 USD | 273,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `759.50` | 769,300.00 USD | 6,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `760.10` | 28,650,000.00 USD | 28,650,000.00 USD | 409,880.00 USD | 80,670.00 USD | 49,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `760.40` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 27,650.00 USD | 42,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `760.50` | 13,580.00 USD | 6,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `761.20` | 29,810,000.00 USD | 29,810,000.00 USD | 774,860.00 USD | 90,660.00 USD | 301,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `761.30` | 3,490,000.00 USD | 3,490,000.00 USD | 10,750.00 USD | 211,960.00 USD | 100,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `761.50` | 541.43 USD | 6,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `762.20` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 699,820.00 USD | 179,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `762.30` | 30,860,000.00 USD | 30,860,000.00 USD | 658,580.00 USD | 172,280.00 USD | 220,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `762.50` | 10,640.00 USD | 6,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `763.10` | 7,830,000.00 USD | 7,830,000.00 USD | 2,460,000.00 USD | 590,460.00 USD | 404,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `763.40` | 34,320,000.00 USD | 34,320,000.00 USD | 2,620,000.00 USD | 247,430.00 USD | 590,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `763.50` | 435,970.00 USD | 6,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `764.00` | 10,270,000.00 USD | 10,270,000.00 USD | 1,590,000.00 USD | 441,980.00 USD | 402,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `764.50` | 36,640,000.00 USD | 36,640,000.00 USD | 1,790,000.00 USD | 210,060.00 USD | 321,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `764.90` | 12,470,000.00 USD | 12,470,000.00 USD | 1,450,000.00 USD | 352,570.00 USD | 395,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `765.50` | 9,770.00 USD | 6,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `765.60` | 38,300,000.00 USD | 38,300,000.00 USD | 1,250,000.00 USD | 188,930.00 USD | 217,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `765.80` | 15,460,000.00 USD | 15,460,000.00 USD | 2,470,000.00 USD | 107,550.00 USD | 416,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `766.70` | 40,650,000.00 USD | 40,650,000.00 USD | 1,630,000.00 USD | 260,910.00 USD | 463,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `766.70` | 20,050,000.00 USD | 20,050,000.00 USD | 3,330,000.00 USD | 416,530.00 USD | 842,330.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `767.50` | 3,950.00 USD | 6,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `767.60` | 23,430,000.00 USD | 23,430,000.00 USD | 2,790,000.00 USD | 123,530.00 USD | 467,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `767.80` | 43,170,000.00 USD | 43,170,000.00 USD | 1,990,000.00 USD | 160,290.00 USD | 364,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `768.50` | 25,660,000.00 USD | 25,660,000.00 USD | 1,840,000.00 USD | 95,830.00 USD | 281,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `768.50` | 21,880.00 USD | 6,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `768.90` | 44,350,000.00 USD | 44,350,000.00 USD | 986,770.00 USD | 56,740.00 USD | 135,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `769.40` | 26,810,000.00 USD | 26,810,000.00 USD | 565,780.00 USD | 249,950.00 USD | 333,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `769.50` | 231,890.00 USD | 6,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `770.00` | 45,190,000.00 USD | 45,190,000.00 USD | 590,250.00 USD | 180,380.00 USD | 72,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `770.30` | 29,310,000.00 USD | 29,310,000.00 USD | 1,900,000.00 USD | 240,530.00 USD | 364,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `770.50` | 27,930.00 USD | 6,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `771.10` | 46,190,000.00 USD | 46,190,000.00 USD | 610,340.00 USD | 46,300.00 USD | 340,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `771.20` | 30,770,000.00 USD | 30,770,000.00 USD | 1,050,000.00 USD | 242,570.00 USD | 162,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `771.50` | 27,330.00 USD | 6,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `772.10` | 33,190,000.00 USD | 33,190,000.00 USD | 1,750,000.00 USD | 252,650.00 USD | 419,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `772.20` | 47,390,000.00 USD | 47,390,000.00 USD | 426,940.00 USD | 131,000.00 USD | 647,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `773.00` | 35,800,000.00 USD | 35,800,000.00 USD | 1,950,000.00 USD | 325,680.00 USD | 338,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `773.30` | 48,800,000.00 USD | 48,800,000.00 USD | 1,090,000.00 USD | 175,430.00 USD | 148,410.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `773.50` | 8,960.00 USD | 6,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `773.90` | 37,600,000.00 USD | 37,600,000.00 USD | 1,220,000.00 USD | 276,760.00 USD | 293,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `774.40` | 50,050,000.00 USD | 50,050,000.00 USD | 1,080,000.00 USD | 85,850.00 USD | 79,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `774.50` | 130.12 USD | 6,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `774.80` | 39,980,000.00 USD | 39,980,000.00 USD | 1,310,000.00 USD | 568,930.00 USD | 502,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `775.50` | 50,810,000.00 USD | 50,810,000.00 USD | 543,580.00 USD | 151,460.00 USD | 63,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `775.70` | 42,470,000.00 USD | 42,470,000.00 USD | 1,830,000.00 USD | 470,960.00 USD | 187,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `776.60` | 51,340,000.00 USD | 51,340,000.00 USD | 365,690.00 USD | 63,550.00 USD | 109,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `776.60` | 44,740,000.00 USD | 44,740,000.00 USD | 1,630,000.00 USD | 269,050.00 USD | 378,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `777.50` | 46,480,000.00 USD | 46,480,000.00 USD | 1,350,000.00 USD | 243,990.00 USD | 148,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `777.50` | 541.14 USD | 6,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `777.70` | 52,860,000.00 USD | 52,860,000.00 USD | 996,310.00 USD | 148,330.00 USD | 372,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `778.40` | 48,170,000.00 USD | 48,170,000.00 USD | 1,180,000.00 USD | 307,370.00 USD | 206,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `778.80` | 54,000,000.00 USD | 54,000,000.00 USD | 927,520.00 USD | 107,660.00 USD | 106,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `779.30` | 49,730,000.00 USD | 49,730,000.00 USD | 1,240,000.00 USD | 188,170.00 USD | 123,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `779.50` | 3,200.00 USD | 6,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `779.90` | 54,940,000.00 USD | 54,940,000.00 USD | 670,650.00 USD | 139,800.00 USD | 127,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `780.20` | 51,100,000.00 USD | 51,100,000.00 USD | 1,070,000.00 USD | 86,470.00 USD | 218,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `780.50` | 9,280.00 USD | 6,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `781.00` | 55,870,000.00 USD | 55,870,000.00 USD | 691,970.00 USD | 83,750.00 USD | 148,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `781.10` | 52,710,000.00 USD | 52,710,000.00 USD | 1,270,000.00 USD | 90,990.00 USD | 242,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `781.50` | 33,510.00 USD | 6,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `782.00` | 54,610,000.00 USD | 54,610,000.00 USD | 1,510,000.00 USD | 87,670.00 USD | 301,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `782.10` | 57,380,000.00 USD | 57,380,000.00 USD | 1,070,000.00 USD | 97,460.00 USD | 338,530.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `782.50` | 78,440.00 USD | 7,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `782.90` | 56,600,000.00 USD | 56,600,000.00 USD | 1,750,000.00 USD | 36,140.00 USD | 202,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `783.20` | 58,500,000.00 USD | 58,500,000.00 USD | 893,500.00 USD | 66,810.00 USD | 162,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `783.80` | 57,170,000.00 USD | 57,170,000.00 USD | 508,000.00 USD | 10,100.00 USD | 54,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `784.30` | 59,030,000.00 USD | 59,030,000.00 USD | 485,610.00 USD | 23,200.00 USD | 18,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `784.70` | 57,480,000.00 USD | 57,480,000.00 USD | 208,380.00 USD | 28,260.00 USD | 70,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `785.40` | 59,550,000.00 USD | 59,550,000.00 USD | 460,360.00 USD | 37,320.00 USD | 27,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `785.60` | 58,610,000.00 USD | 58,610,000.00 USD | 1,010,000.00 USD | 54,140.00 USD | 71,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `786.50` | 59,850,000.00 USD | 59,850,000.00 USD | 262,870.00 USD | 15,410.00 USD | 26,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `786.50` | 59,000,000.00 USD | 59,000,000.00 USD | 329,230.00 USD | 30,660.00 USD | 23,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `786.50` | 4,910.00 USD | 7,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `787.40` | 59,580,000.00 USD | 59,580,000.00 USD | 470,050.00 USD | 17,630.00 USD | 91,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `787.50` | 122,290.00 USD | 7,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `787.60` | 60,350,000.00 USD | 60,350,000.00 USD | 434,490.00 USD | 33,000.00 USD | 24,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `788.30` | 59,940,000.00 USD | 59,940,000.00 USD | 202,630.00 USD | 82,380.00 USD | 81,230.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `788.50` | 76,210.00 USD | 7,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `788.70` | 61,020,000.00 USD | 61,020,000.00 USD | 205,450.00 USD | 49,630.00 USD | 420,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `789.20` | 60,780,000.00 USD | 60,780,000.00 USD | 698,830.00 USD | 81,250.00 USD | 55,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `789.50` | 5,800.00 USD | 7,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `789.80` | 61,760,000.00 USD | 61,760,000.00 USD | 548,330.00 USD | 26,520.00 USD | 165,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `790.10` | 61,270,000.00 USD | 61,270,000.00 USD | 299,250.00 USD | 104,360.00 USD | 88,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `790.90` | 62,200,000.00 USD | 62,200,000.00 USD | 338,320.00 USD | 88,600.00 USD | 11,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `791.00` | 62,150,000.00 USD | 62,150,000.00 USD | 693,290.00 USD | 82,870.00 USD | 100,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `791.90` | 63,030,000.00 USD | 63,030,000.00 USD | 816,380.00 USD | 16,830.00 USD | 46,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `792.00` | 62,550,000.00 USD | 62,550,000.00 USD | 352,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `792.80` | 63,250,000.00 USD | 63,250,000.00 USD | 205,450.00 USD | 0.00 USD | 14,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `793.10` | 62,610,000.00 USD | 62,610,000.00 USD | 58,240.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `793.70` | 63,430,000.00 USD | 63,430,000.00 USD | 184,960.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `794.20` | 62,630,000.00 USD | 62,630,000.00 USD | 21,310.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `794.50` | 7,270.00 USD | 7,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `794.60` | 63,750,000.00 USD | 63,750,000.00 USD | 302,280.00 USD | 15,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `795.30` | 62,680,000.00 USD | 62,680,000.00 USD | 49,090.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `795.50` | 63,890,000.00 USD | 63,890,000.00 USD | 109,640.00 USD | 14,650.00 USD | 14,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `795.50` | 5,530.00 USD | 7,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `796.40` | 62,810,000.00 USD | 62,810,000.00 USD | 36,340.00 USD | 0.00 USD | 94,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `796.40` | 64,030,000.00 USD | 64,030,000.00 USD | 139,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `796.50` | 1,500.00 USD | 7,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `797.30` | 64,090,000.00 USD | 64,090,000.00 USD | 64,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `797.50` | 62,890,000.00 USD | 62,890,000.00 USD | 78,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `797.50` | 4,340.00 USD | 7,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `798.20` | 64,250,000.00 USD | 64,250,000.00 USD | 155,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `798.60` | 62,960,000.00 USD | 62,960,000.00 USD | 46,910.00 USD | 26,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `799.10` | 64,290,000.00 USD | 64,290,000.00 USD | 42,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `799.50` | 76,490.00 USD | 7,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `799.70` | 62,980,000.00 USD | 62,980,000.00 USD | 18,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `800.00` | 64,400,000.00 USD | 64,400,000.00 USD | 113,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `800.50` | 191.32 USD | 7,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `800.80` | 62,990,000.00 USD | 62,990,000.00 USD | 11,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `800.90` | 64,510,000.00 USD | 64,510,000.00 USD | 77,580.00 USD | 8,370.00 USD | 21,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `801.50` | 746.20 USD | 7,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `801.80` | 64,720,000.00 USD | 64,720,000.00 USD | 179,900.00 USD | 16,330.00 USD | 10,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `801.90` | 63,110,000.00 USD | 63,110,000.00 USD | 30,060.00 USD | 0.00 USD | 87,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `802.50` | 279.27 USD | 7,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `802.70` | 64,730,000.00 USD | 64,730,000.00 USD | 11,220.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `803.00` | 63,150,000.00 USD | 63,150,000.00 USD | 20,540.00 USD | 21,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `803.50` | 517,250.00 USD | 7,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `803.60` | 64,760,000.00 USD | 64,760,000.00 USD | 27,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `804.10` | 63,250,000.00 USD | 63,250,000.00 USD | 80,140.00 USD | 14,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `804.50` | 64,840,000.00 USD | 64,840,000.00 USD | 32,340.00 USD | 18,260.00 USD | 32,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `804.50` | 220,280.00 USD | 8,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `805.20` | 63,400,000.00 USD | 63,400,000.00 USD | 67,230.00 USD | 0.00 USD | 81,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `805.40` | 64,910,000.00 USD | 64,910,000.00 USD | 56,700.00 USD | 8,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `805.50` | 14,110.00 USD | 8,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `806.30` | 64,920,000.00 USD | 64,920,000.00 USD | 3,270.00 USD | 12,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `806.50` | 44,210.00 USD | 8,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `807.20` | 64,970,000.00 USD | 64,970,000.00 USD | 39,190.00 USD | 0.00 USD | 11,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `808.10` | 65,030,000.00 USD | 65,030,000.00 USD | 17,980.00 USD | 5,360.00 USD | 29,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `808.50` | 12,520.00 USD | 8,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `809.00` | 65,110,000.00 USD | 65,110,000.00 USD | 58,620.00 USD | 13,120.00 USD | 13,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `809.90` | 65,330,000.00 USD | 65,330,000.00 USD | 178,130.00 USD | 9,760.00 USD | 36,490.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `810.50` | 65,450.00 USD | 8,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `810.80` | 65,420,000.00 USD | 65,420,000.00 USD | 78,030.00 USD | 6,630.00 USD | 5,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `811.70` | 65,480,000.00 USD | 65,480,000.00 USD | 19,210.00 USD | 12,110.00 USD | 29,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `812.50` | 9,310.00 USD | 8,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `812.60` | 65,600,000.00 USD | 65,600,000.00 USD | 68,390.00 USD | 17,450.00 USD | 31,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `813.50` | 65,860,000.00 USD | 65,860,000.00 USD | 147,480.00 USD | 59,640.00 USD | 45,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `814.40` | 66,180,000.00 USD | 66,180,000.00 USD | 218,130.00 USD | 32,770.00 USD | 74,730.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `814.50` | 692.32 USD | 8,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `815.30` | 66,390,000.00 USD | 66,390,000.00 USD | 171,100.00 USD | 24,290.00 USD | 10,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `816.20` | 66,690,000.00 USD | 66,690,000.00 USD | 203,680.00 USD | 44,470.00 USD | 59,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `816.50` | 1,740.00 USD | 8,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `817.10` | 67,090,000.00 USD | 67,090,000.00 USD | 278,420.00 USD | 76,830.00 USD | 42,530.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `817.50` | 1,630.00 USD | 8,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `818.00` | 67,550,000.00 USD | 67,550,000.00 USD | 346,550.00 USD | 48,360.00 USD | 67,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `818.50` | 149,880.00 USD | 8,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `818.90` | 67,790,000.00 USD | 67,790,000.00 USD | 180,470.00 USD | 8,160.00 USD | 47,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `819.80` | 68,300,000.00 USD | 68,300,000.00 USD | 295,510.00 USD | 101,950.00 USD | 107,190.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `820.50` | 132.92 USD | 8,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `820.70` | 68,600,000.00 USD | 68,600,000.00 USD | 235,990.00 USD | 41,190.00 USD | 24,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `821.50` | 37,130.00 USD | 8,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `821.60` | 68,800,000.00 USD | 68,800,000.00 USD | 86,380.00 USD | 62,620.00 USD | 55,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `822.50` | 69,300,000.00 USD | 69,300,000.00 USD | 394,120.00 USD | 64,970.00 USD | 42,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `822.50` | 38,410.00 USD | 8,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `823.40` | 69,630,000.00 USD | 69,630,000.00 USD | 213,450.00 USD | 68,530.00 USD | 45,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `824.30` | 69,980,000.00 USD | 69,980,000.00 USD | 248,860.00 USD | 58,170.00 USD | 43,880.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `824.50` | 2,580,000.00 USD | 11,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `825.20` | 70,340,000.00 USD | 70,340,000.00 USD | 277,990.00 USD | 21,630.00 USD | 61,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `826.10` | 70,650,000.00 USD | 70,650,000.00 USD | 223,810.00 USD | 27,390.00 USD | 53,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `827.00` | 71,290,000.00 USD | 71,290,000.00 USD | 494,310.00 USD | 23,200.00 USD | 126,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `827.50` | 8,470.00 USD | 11,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `827.90` | 71,650,000.00 USD | 71,650,000.00 USD | 297,880.00 USD | 0.00 USD | 63,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `828.50` | 128,530.00 USD | 11,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `828.80` | 71,840,000.00 USD | 71,840,000.00 USD | 184,280.00 USD | 0.00 USD | 5,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `829.70` | 71,930,000.00 USD | 71,930,000.00 USD | 43,760.00 USD | 5,190.00 USD | 33,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `830.50` | 303.13 USD | 11,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `830.60` | 72,180,000.00 USD | 72,180,000.00 USD | 221,150.00 USD | 5,300.00 USD | 28,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `831.50` | 72,220,000.00 USD | 72,220,000.00 USD | 37,200.00 USD | 5,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `831.50` | 44,200.00 USD | 11,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `832.50` | 83,250.00 USD | 11,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `834.50` | 2,680.00 USD | 11,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `836.50` | 625.70 USD | 11,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `837.50` | 23,620.00 USD | 11,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `839.50` | 3,450.00 USD | 11,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `840.50` | 511.86 USD | 11,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `841.50` | 3,830.00 USD | 11,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `842.50` | 324.36 USD | 11,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `843.50` | 250,120.00 USD | 11,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `845.50` | 8,460.00 USD | 11,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `846.50` | 334,410.00 USD | 11,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `848.50` | 13,020.00 USD | 11,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `851.50` | 553,910.00 USD | 12,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `852.50` | 64,770.00 USD | 12,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `853.50` | 189,340.00 USD | 12,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `854.50` | 138.43 USD | 12,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `858.50` | 409.50 USD | 12,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `859.50` | 20,060.00 USD | 12,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `860.50` | 2,580.00 USD | 12,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `865.50` | 17,550.00 USD | 12,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `866.50` | 1,350.00 USD | 12,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `872.50` | 183,630.00 USD | 12,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `874.50` | 248.36 USD | 12,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `877.50` | 650,150.00 USD | 13,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `878.50` | 85,350.00 USD | 13,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `879.50` | 145.12 USD | 13,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `883.50` | 319.83 USD | 13,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `885.50` | 2,120.00 USD | 13,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `886.50` | 812.92 USD | 13,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `894.50` | 26,840.00 USD | 13,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `895.50` | 76,620.00 USD | 13,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `896.50` | 224,120.00 USD | 14,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `898.50` | 127.59 USD | 14,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `899.50` | 390.38 USD | 14,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `901.50` | 45,080.00 USD | 14,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `902.50` | 1,180.00 USD | 14,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `905.50` | 64,000.00 USD | 14,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `907.50` | 700.59 USD | 14,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `908.50` | 1,790.00 USD | 14,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `910.50` | 6,880.00 USD | 14,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `911.50` | 38,590.00 USD | 14,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `914.50` | 45,250.00 USD | 14,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `915.50` | 25,980.00 USD | 14,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `924.50` | 3,220.00 USD | 14,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `925.50` | 118,460.00 USD | 14,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `932.50` | 654.62 USD | 14,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `935.50` | 76,440.00 USD | 14,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `938.50` | 280.61 USD | 14,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `939.50` | 26,610.00 USD | 14,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `942.50` | 25,530.00 USD | 14,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `944.50` | 201.18 USD | 14,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `949.50` | 118,620.00 USD | 14,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `950.50` | 41,140.00 USD | 14,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `951.50` | 1,680.00 USD | 14,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `952.50` | 398.14 USD | 14,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `954.50` | 440.02 USD | 14,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `955.50` | 8,000.00 USD | 14,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `960.50` | 101.81 USD | 14,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `962.50` | 118.39 USD | 14,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `963.50` | 114.66 USD | 14,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `966.50` | 2,350,000.00 USD | 17,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `968.50` | 1,940.00 USD | 17,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `970.50` | 1,160,000.00 USD | 18,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `977.50` | 25,910.00 USD | 18,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `978.50` | 13,400.00 USD | 18,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `979.50` | 19,590.00 USD | 18,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `981.50` | 14,480.00 USD | 18,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `986.50` | 1,100.00 USD | 18,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `987.50` | 9,910.00 USD | 18,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `990.50` | 28,300.00 USD | 18,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `993.50` | 103,500.00 USD | 18,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `994.50` | 285,520.00 USD | 18,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `998.50` | 7,310.00 USD | 18,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1000.50` | 194.10 USD | 18,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1001.50` | 139.21 USD | 18,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1002.50` | 17,540.00 USD | 18,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1004.50` | 143,120.00 USD | 18,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1005.50` | 1,570.00 USD | 18,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1006.50` | 18,010.00 USD | 18,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1014.50` | 42,460.00 USD | 18,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1015.50` | 203,100.00 USD | 19,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1017.50` | 59,630.00 USD | 19,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1023.50` | 6,080.00 USD | 19,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1025.50` | 2,850.00 USD | 19,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1027.50` | 716,800.00 USD | 19,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1032.50` | 663,870.00 USD | 20,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1036.50` | 2,470.00 USD | 20,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1037.50` | 118,280.00 USD | 20,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1050.50` | 500.04 USD | 20,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1051.50` | 393,920.00 USD | 21,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1058.50` | 6,040.00 USD | 21,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1059.50` | 66,220.00 USD | 21,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1064.50` | 1,600.00 USD | 21,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1065.50` | 229,540.00 USD | 21,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1067.50` | 15,380.00 USD | 21,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1072.50` | 206,590.00 USD | 21,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1073.50` | 1,610.00 USD | 21,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1074.50` | 39,250.00 USD | 21,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1081.50` | 9,430.00 USD | 21,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1087.50` | 19,390.00 USD | 21,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1088.50` | 1,930.00 USD | 21,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1099.50` | 7,580.00 USD | 21,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1102.50` | 4,630.00 USD | 21,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1107.50` | 245,110.00 USD | 21,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1112.50` | 164,380.00 USD | 22,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1116.50` | 243,420.00 USD | 22,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1124.50` | 48,660.00 USD | 22,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1125.50` | 1,500.00 USD | 22,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1126.50` | 60,900.00 USD | 22,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1133.50` | 8,070.00 USD | 22,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1136.50` | 11,370.00 USD | 22,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1137.50` | 341,250.00 USD | 22,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1138.50` | 547.62 USD | 22,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1144.50` | 11,620.00 USD | 22,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1145.50` | 595.66 USD | 22,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1146.50` | 55,610.00 USD | 22,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1149.50` | 211.51 USD | 22,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1151.50` | 154.30 USD | 22,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1154.50` | 46,180.00 USD | 22,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1157.50` | 1,850,000.00 USD | 24,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1159.50` | 364.08 USD | 24,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1166.50` | 20,250.00 USD | 24,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1168.50` | 121.52 USD | 24,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1169.50` | 8,700.00 USD | 24,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1175.50` | 115.20 USD | 24,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1179.50` | 66,120.00 USD | 24,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1182.50` | 158.46 USD | 24,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1186.50` | 80,980.00 USD | 24,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1193.50` | 20,350.00 USD | 24,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1197.50` | 463.43 USD | 24,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1207.50` | 385.19 USD | 24,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1210.50` | 30,240.00 USD | 25,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1211.50` | 109,030.00 USD | 25,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1215.50` | 45,100.00 USD | 25,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1224.50` | 53,940.00 USD | 25,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1225.50` | 1,030.00 USD | 25,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1231.50` | 23,910.00 USD | 25,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1232.50` | 49,300.00 USD | 25,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1243.50` | 644.13 USD | 25,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1251.50` | 100.12 USD | 25,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1263.50` | 202.16 USD | 25,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1275.50` | 114,800.00 USD | 25,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1276.50` | 3,570.00 USD | 25,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1279.50` | 5,110.00 USD | 25,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1290.50` | 1,360,000.00 USD | 26,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1295.50` | 181.37 USD | 26,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1298.50` | 2,770.00 USD | 26,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1306.50` | 100.60 USD | 26,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1308.50` | 166,020.00 USD | 26,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1317.50` | 2,630.00 USD | 26,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1320.50` | 14,140.00 USD | 26,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1323.50` | 80,070.00 USD | 27,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1324.50` | 229.14 USD | 27,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1330.50` | 23,470.00 USD | 27,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1332.50` | 688,080.00 USD | 27,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1349.50` | 129,050.00 USD | 27,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1353.50` | 4,680.00 USD | 27,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1356.50` | 19,090.00 USD | 27,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1358.50` | 3,870.00 USD | 27,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1361.50` | 156,500.00 USD | 28,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1370.50` | 46,910.00 USD | 28,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1371.50` | 1,930.00 USD | 28,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1375.50` | 20,630.00 USD | 28,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1377.50` | 66,290.00 USD | 28,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1401.50` | 252,270.00 USD | 28,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1402.50` | 178.12 USD | 28,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1405.50` | 6,420.00 USD | 28,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1406.50` | 4,770.00 USD | 28,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1413.50` | 139.94 USD | 28,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `141.50` | 7,120,000.00 USD | 0.00 USD | 5,340.00 USD | `-80.01%` | `37,757,000,000.00` |
| `Live` | `Long` | `142.50` | 7,110,000.00 USD | 0.00 USD | 174.28 USD | `-79.87%` | `1,223,000,000.00` |
| `Live` | `Long` | `143.50` | 7,110,000.00 USD | 0.00 USD | 88,970.00 USD | `-79.73%` | `620,000,000,000.00` |
| `Live` | `Long` | `144.50` | 7,020,000.00 USD | 0.00 USD | 2,020.00 USD | `-79.59%` | `14,000,000,000.00` |
| `Live` | `Long` | `147.50` | 7,020,000.00 USD | 0.00 USD | 2,830.00 USD | `-79.16%` | `19,212,000,000.00` |
| `Live` | `Long` | `160.50` | 7,020,000.00 USD | 0.00 USD | 971.02 USD | `-77.33%` | `6,050,000,000.00` |
| `Live` | `Long` | `162.50` | 7,020,000.00 USD | 0.00 USD | 812.50 USD | `-77.05%` | `5,000,000,000.00` |
| `Live` | `Long` | `178.50` | 7,020,000.00 USD | 0.00 USD | 239.90 USD | `-74.79%` | `1,344,000,000.00` |
| `Live` | `Long` | `182.50` | 7,020,000.00 USD | 0.00 USD | 23,210.00 USD | `-74.22%` | `127,165,000,000.00` |
| `Live` | `Long` | `190.50` | 6,990,000.00 USD | 0.00 USD | 20,420.00 USD | `-73.09%` | `107,186,000,000.00` |
| `Live` | `Long` | `193.50` | 6,970,000.00 USD | 0.00 USD | 1,380.00 USD | `-72.67%` | `7,129,000,000.00` |
| `Live` | `Long` | `197.50` | 6,970,000.00 USD | 0.00 USD | 242.73 USD | `-72.10%` | `1,229,000,000.00` |
| `Live` | `Long` | `204.50` | 6,970,000.00 USD | 0.00 USD | 250.92 USD | `-71.11%` | `1,227,000,000.00` |
| `Live` | `Long` | `210.50` | 6,970,000.00 USD | 0.00 USD | 7,180.00 USD | `-70.27%` | `34,129,000,000.00` |
| `Live` | `Long` | `212.50` | 6,960,000.00 USD | 0.00 USD | 170.00 USD | `-69.98%` | `800,000,000.00` |
| `Live` | `Long` | `219.50` | 6,960,000.00 USD | 0.00 USD | 191.18 USD | `-68.99%` | `871,000,000.00` |
| `Live` | `Long` | `221.50` | 6,960,000.00 USD | 0.00 USD | 221,500.00 USD | `-68.71%` | `1,000,000,000,000.00` |
| `Live` | `Long` | `240.50` | 6,740,000.00 USD | 0.00 USD | 16,700.00 USD | `-66.03%` | `69,447,000,000.00` |
| `Live` | `Long` | `246.50` | 6,720,000.00 USD | 0.00 USD | 17,060.00 USD | `-65.18%` | `69,189,000,000.00` |
| `Live` | `Long` | `247.50` | 6,710,000.00 USD | 0.00 USD | 368.53 USD | `-65.04%` | `1,489,000,000.00` |
| `Live` | `Long` | `262.50` | 6,710,000.00 USD | 0.00 USD | 27,880.00 USD | `-62.92%` | `106,207,000,000.00` |
| `Live` | `Long` | `264.50` | 6,680,000.00 USD | 0.00 USD | 1,400.00 USD | `-62.64%` | `5,281,000,000.00` |
| `Live` | `Long` | `267.50` | 6,680,000.00 USD | 0.00 USD | 535.00 USD | `-62.21%` | `2,000,000,000.00` |
| `Live` | `Long` | `268.50` | 6,680,000.00 USD | 0.00 USD | 21,690.00 USD | `-62.07%` | `80,790,000,000.00` |
| `Live` | `Long` | `278.50` | 6,660,000.00 USD | 0.00 USD | 1,950.00 USD | `-60.66%` | `6,996,000,000.00` |
| `Live` | `Long` | `287.50` | 6,650,000.00 USD | 0.00 USD | 20,120.00 USD | `-59.39%` | `70,000,000,000.00` |
| `Live` | `Long` | `288.50` | 6,630,000.00 USD | 0.00 USD | 383.42 USD | `-59.25%` | `1,329,000,000.00` |
| `Live` | `Long` | `292.50` | 6,630,000.00 USD | 0.00 USD | 12,410.00 USD | `-58.68%` | `42,439,000,000.00` |
| `Live` | `Long` | `299.50` | 6,620,000.00 USD | 0.00 USD | 1,890.00 USD | `-57.69%` | `6,299,000,000.00` |
| `Live` | `Long` | `309.50` | 6,620,000.00 USD | 0.00 USD | 317.86 USD | `-56.28%` | `1,027,000,000.00` |
| `Live` | `Long` | `313.50` | 6,620,000.00 USD | 0.00 USD | 501.60 USD | `-55.72%` | `1,600,000,000.00` |
| `Live` | `Long` | `314.50` | 6,620,000.00 USD | 0.00 USD | 5,100.00 USD | `-55.57%` | `16,204,000,000.00` |
| `Live` | `Long` | `322.50` | 6,610,000.00 USD | 0.00 USD | 129,000.00 USD | `-54.44%` | `400,000,000,000.00` |
| `Live` | `Long` | `323.50` | 6,480,000.00 USD | 0.00 USD | 3,190.00 USD | `-54.30%` | `9,862,000,000.00` |
| `Live` | `Long` | `324.50` | 6,480,000.00 USD | 0.00 USD | 1,020.00 USD | `-54.16%` | `3,147,000,000.00` |
| `Live` | `Long` | `326.50` | 6,480,000.00 USD | 0.00 USD | 500.85 USD | `-53.88%` | `1,534,000,000.00` |
| `Live` | `Long` | `328.50` | 6,480,000.00 USD | 0.00 USD | 315.03 USD | `-53.60%` | `959,000,000.00` |
| `Live` | `Long` | `330.50` | 6,480,000.00 USD | 0.00 USD | 308.36 USD | `-53.31%` | `933,000,000.00` |
| `Live` | `Long` | `331.50` | 6,480,000.00 USD | 0.00 USD | 9,130.00 USD | `-53.17%` | `27,554,000,000.00` |
| `Live` | `Long` | `332.50` | 6,470,000.00 USD | 0.00 USD | 175,560.00 USD | `-53.03%` | `527,997,000,000.00` |
| `Live` | `Long` | `333.50` | 6,290,000.00 USD | 0.00 USD | 377.19 USD | `-52.89%` | `1,131,000,000.00` |
| `Live` | `Long` | `334.50` | 6,290,000.00 USD | 0.00 USD | 118.08 USD | `-52.75%` | `353,000,000.00` |
| `Live` | `Long` | `335.50` | 6,290,000.00 USD | 0.00 USD | 14,260.00 USD | `-52.61%` | `42,500,000,000.00` |
| `Live` | `Long` | `337.50` | 6,280,000.00 USD | 0.00 USD | 933.86 USD | `-52.33%` | `2,767,000,000.00` |
| `Live` | `Long` | `342.50` | 6,280,000.00 USD | 0.00 USD | 490.80 USD | `-51.62%` | `1,433,000,000.00` |
| `Live` | `Long` | `343.50` | 6,280,000.00 USD | 0.00 USD | 652.65 USD | `-51.48%` | `1,900,000,000.00` |
| `Live` | `Long` | `357.50` | 6,280,000.00 USD | 0.00 USD | 1,490.00 USD | `-49.50%` | `4,170,000,000.00` |
| `Live` | `Long` | `359.50` | 6,280,000.00 USD | 0.00 USD | 212.10 USD | `-49.22%` | `590,000,000.00` |
| `Live` | `Long` | `360.50` | 6,280,000.00 USD | 0.00 USD | 1,620.00 USD | `-49.08%` | `4,504,000,000.00` |
| `Live` | `Long` | `364.50` | 6,270,000.00 USD | 0.00 USD | 1,890.00 USD | `-48.51%` | `5,187,000,000.00` |
| `Live` | `Long` | `366.50` | 6,270,000.00 USD | 0.00 USD | 549.75 USD | `-48.23%` | `1,500,000,000.00` |
| `Live` | `Long` | `370.50` | 6,270,000.00 USD | 0.00 USD | 1,220.00 USD | `-47.66%` | `3,300,000,000.00` |
| `Live` | `Long` | `374.50` | 6,270,000.00 USD | 0.00 USD | 1,820.00 USD | `-47.10%` | `4,868,000,000.00` |
| `Live` | `Long` | `377.50` | 6,270,000.00 USD | 0.00 USD | 451.87 USD | `-46.67%` | `1,197,000,000.00` |
| `Live` | `Long` | `378.50` | 6,270,000.00 USD | 0.00 USD | 7,760.00 USD | `-46.53%` | `20,499,000,000.00` |
| `Live` | `Long` | `379.50` | 6,260,000.00 USD | 0.00 USD | 645.15 USD | `-46.39%` | `1,700,000,000.00` |
| `Live` | `Long` | `380.50` | 6,260,000.00 USD | 0.00 USD | 163.62 USD | `-46.25%` | `430,000,000.00` |
| `Live` | `Long` | `382.50` | 6,260,000.00 USD | 0.00 USD | 1,910.00 USD | `-45.97%` | `5,000,000,000.00` |
| `Live` | `Long` | `383.50` | 6,260,000.00 USD | 0.00 USD | 10,900.00 USD | `-45.83%` | `28,414,000,000.00` |
| `Live` | `Long` | `385.50` | 6,250,000.00 USD | 0.00 USD | 2,860.00 USD | `-45.54%` | `7,421,000,000.00` |
| `Live` | `Long` | `386.50` | 6,240,000.00 USD | 0.00 USD | 531.44 USD | `-45.40%` | `1,375,000,000.00` |
| `Live` | `Long` | `388.50` | 6,240,000.00 USD | 0.00 USD | 602.95 USD | `-45.12%` | `1,552,000,000.00` |
| `Live` | `Long` | `393.50` | 6,240,000.00 USD | 0.00 USD | 103.88 USD | `-44.41%` | `264,000,000.00` |
| `Live` | `Long` | `394.50` | 6,240,000.00 USD | 0.00 USD | 168.06 USD | `-44.27%` | `426,000,000.00` |
| `Live` | `Long` | `395.50` | 6,240,000.00 USD | 0.00 USD | 2,110.00 USD | `-44.13%` | `5,347,000,000.00` |
| `Live` | `Long` | `396.50` | 6,240,000.00 USD | 0.00 USD | 396.50 USD | `-43.99%` | `1,000,000,000.00` |
| `Live` | `Long` | `397.50` | 6,240,000.00 USD | 0.00 USD | 318.00 USD | `-43.85%` | `800,000,000.00` |
| `Live` | `Long` | `398.50` | 6,240,000.00 USD | 0.00 USD | 523.63 USD | `-43.71%` | `1,314,000,000.00` |
| `Live` | `Long` | `400.50` | 6,240,000.00 USD | 0.00 USD | 605.16 USD | `-43.43%` | `1,511,000,000.00` |
| `Live` | `Long` | `404.50` | 6,240,000.00 USD | 0.00 USD | 102.34 USD | `-42.86%` | `253,000,000.00` |
| `Live` | `Long` | `405.50` | 6,240,000.00 USD | 0.00 USD | 1,280.00 USD | `-42.72%` | `3,167,000,000.00` |
| `Live` | `Long` | `410.50` | 6,240,000.00 USD | 0.00 USD | 614.52 USD | `-42.01%` | `1,497,000,000.00` |
| `Live` | `Long` | `411.50` | 6,240,000.00 USD | 0.00 USD | 106.17 USD | `-41.87%` | `258,000,000.00` |
| `Live` | `Long` | `412.50` | 6,240,000.00 USD | 0.00 USD | 12,360.00 USD | `-41.73%` | `29,969,000,000.00` |
| `Live` | `Long` | `414.50` | 6,220,000.00 USD | 0.00 USD | 13,320.00 USD | `-41.45%` | `32,128,000,000.00` |
| `Live` | `Long` | `415.50` | 6,210,000.00 USD | 0.00 USD | 1,810.00 USD | `-41.31%` | `4,368,000,000.00` |
| `Live` | `Long` | `417.50` | 6,210,000.00 USD | 0.00 USD | 8,500.00 USD | `-41.02%` | `20,351,000,000.00` |
| `Live` | `Long` | `418.50` | 6,200,000.00 USD | 0.00 USD | 5,680.00 USD | `-40.88%` | `13,571,000,000.00` |
| `Live` | `Long` | `420.50` | 6,190,000.00 USD | 0.00 USD | 10,650.00 USD | `-40.60%` | `25,316,000,000.00` |
| `Live` | `Long` | `421.50` | 6,180,000.00 USD | 0.00 USD | 2,320.00 USD | `-40.46%` | `5,496,000,000.00` |
| `Live` | `Long` | `423.50` | 6,180,000.00 USD | 0.00 USD | 1,450.00 USD | `-40.18%` | `3,419,000,000.00` |
| `Live` | `Long` | `427.50` | 6,180,000.00 USD | 0.00 USD | 29,930.00 USD | `-39.61%` | `70,000,000,000.00` |
| `Live` | `Long` | `429.50` | 6,150,000.00 USD | 0.00 USD | 615.04 USD | `-39.33%` | `1,432,000,000.00` |
| `Live` | `Long` | `430.50` | 6,150,000.00 USD | 0.00 USD | 638.00 USD | `-39.19%` | `1,482,000,000.00` |
| `Live` | `Long` | `432.50` | 6,150,000.00 USD | 0.00 USD | 3,340.00 USD | `-38.91%` | `7,731,000,000.00` |
| `Live` | `Long` | `438.50` | 6,150,000.00 USD | 0.00 USD | 1,790.00 USD | `-38.06%` | `4,087,000,000.00` |
| `Live` | `Long` | `444.50` | 6,140,000.00 USD | 0.00 USD | 949.90 USD | `-37.21%` | `2,137,000,000.00` |
| `Live` | `Long` | `452.50` | 6,140,000.00 USD | 0.00 USD | 1,210.00 USD | `-36.08%` | `2,682,000,000.00` |
| `Live` | `Long` | `453.50` | 6,140,000.00 USD | 0.00 USD | 7,610.00 USD | `-35.94%` | `16,790,000,000.00` |
| `Live` | `Long` | `456.50` | 6,130,000.00 USD | 0.00 USD | 4,730.00 USD | `-35.52%` | `10,359,000,000.00` |
| `Live` | `Long` | `460.50` | 6,130,000.00 USD | 0.00 USD | 37,040.00 USD | `-34.95%` | `80,432,000,000.00` |
| `Live` | `Long` | `470.50` | 6,090,000.00 USD | 0.00 USD | 4,510.00 USD | `-33.54%` | `9,593,000,000.00` |
| `Live` | `Long` | `472.50` | 6,090,000.00 USD | 0.00 USD | 131,830.00 USD | `-33.26%` | `278,997,000,000.00` |
| `Live` | `Long` | `476.50` | 5,960,000.00 USD | 0.00 USD | 5,330.00 USD | `-32.69%` | `11,182,000,000.00` |
| `Live` | `Long` | `478.50` | 5,950,000.00 USD | 0.00 USD | 2,170.00 USD | `-32.41%` | `4,539,000,000.00` |
| `Live` | `Long` | `482.50` | 5,950,000.00 USD | 0.00 USD | 7,330.00 USD | `-31.84%` | `15,184,000,000.00` |
| `Live` | `Long` | `484.50` | 5,940,000.00 USD | 0.00 USD | 58,270.00 USD | `-31.56%` | `120,267,000,000.00` |
| `Live` | `Long` | `485.50` | 5,880,000.00 USD | 0.00 USD | 52,350.00 USD | `-31.42%` | `107,823,000,000.00` |
| `Live` | `Long` | `487.50` | 5,830,000.00 USD | 0.00 USD | 204.75 USD | `-31.14%` | `420,000,000.00` |
| `Live` | `Long` | `488.50` | 5,830,000.00 USD | 0.00 USD | 257.44 USD | `-31.00%` | `527,000,000.00` |
| `Live` | `Long` | `489.50` | 5,830,000.00 USD | 0.00 USD | 6,030.00 USD | `-30.85%` | `12,312,000,000.00` |
| `Live` | `Long` | `493.50` | 5,820,000.00 USD | 0.00 USD | 41,030.00 USD | `-30.29%` | `83,150,000,000.00` |
| `Live` | `Long` | `494.50` | 5,780,000.00 USD | 0.00 USD | 1,410.00 USD | `-30.15%` | `2,849,000,000.00` |
| `Live` | `Long` | `496.50` | 5,780,000.00 USD | 0.00 USD | 1,320.00 USD | `-29.86%` | `2,651,000,000.00` |
| `Live` | `Long` | `498.50` | 5,780,000.00 USD | 0.00 USD | 1,420.00 USD | `-29.58%` | `2,853,000,000.00` |
| `Live` | `Long` | `501.50` | 5,780,000.00 USD | 0.00 USD | 7,760.00 USD | `-29.16%` | `15,482,000,000.00` |
| `Live` | `Long` | `502.50` | 5,770,000.00 USD | 0.00 USD | 109.04 USD | `-29.02%` | `217,000,000.00` |
| `Live` | `Long` | `505.50` | 5,770,000.00 USD | 0.00 USD | 5,760.00 USD | `-28.59%` | `11,387,000,000.00` |
| `Live` | `Long` | `508.50` | 5,770,000.00 USD | 0.00 USD | 992.08 USD | `-28.17%` | `1,951,000,000.00` |
| `Live` | `Long` | `509.50` | 5,760,000.00 USD | 0.00 USD | 3,100.00 USD | `-28.03%` | `6,091,000,000.00` |
| `Live` | `Long` | `511.50` | 5,760,000.00 USD | 0.00 USD | 4,090.00 USD | `-27.75%` | `8,000,000,000.00` |
| `Live` | `Long` | `512.50` | 5,760,000.00 USD | 0.00 USD | 5,190.00 USD | `-27.60%` | `10,118,000,000.00` |
| `Live` | `Long` | `513.50` | 5,750,000.00 USD | 0.00 USD | 3,090.00 USD | `-27.46%` | `6,009,000,000.00` |
| `Live` | `Long` | `514.50` | 5,750,000.00 USD | 0.00 USD | 4,120.00 USD | `-27.32%` | `8,014,000,000.00` |
| `Live` | `Long` | `515.50` | 5,740,000.00 USD | 0.00 USD | 3,930.00 USD | `-27.18%` | `7,621,000,000.00` |
| `Live` | `Long` | `516.50` | 5,740,000.00 USD | 0.00 USD | 2,550.00 USD | `-27.04%` | `4,933,000,000.00` |
| `Live` | `Long` | `517.50` | 5,740,000.00 USD | 0.00 USD | 22,650.00 USD | `-26.90%` | `43,765,000,000.00` |
| `Live` | `Long` | `518.50` | 5,720,000.00 USD | 0.00 USD | 7,540.00 USD | `-26.76%` | `14,535,000,000.00` |
| `Live` | `Long` | `519.50` | 5,710,000.00 USD | 0.00 USD | 968.35 USD | `-26.62%` | `1,864,000,000.00` |
| `Live` | `Long` | `520.50` | 5,710,000.00 USD | 0.00 USD | 532.47 USD | `-26.47%` | `1,023,000,000.00` |
| `Live` | `Long` | `521.50` | 5,710,000.00 USD | 0.00 USD | 838.05 USD | `-26.33%` | `1,607,000,000.00` |
| `Live` | `Long` | `522.50` | 5,710,000.00 USD | 0.00 USD | 2,350.00 USD | `-26.19%` | `4,490,000,000.00` |
| `Live` | `Long` | `523.50` | 5,700,000.00 USD | 0.00 USD | 2,090.00 USD | `-26.05%` | `3,993,000,000.00` |
| `Live` | `Long` | `525.50` | 5,700,000.00 USD | 0.00 USD | 835.02 USD | `-25.77%` | `1,589,000,000.00` |
| `Live` | `Long` | `526.50` | 5,700,000.00 USD | 0.00 USD | 1,700.00 USD | `-25.63%` | `3,234,000,000.00` |
| `Live` | `Long` | `529.50` | 5,700,000.00 USD | 0.00 USD | 43,700.00 USD | `-25.20%` | `82,525,000,000.00` |
| `Live` | `Long` | `530.50` | 5,650,000.00 USD | 0.00 USD | 17,770.00 USD | `-25.06%` | `33,504,000,000.00` |
| `Live` | `Long` | `531.50` | 5,640,000.00 USD | 0.00 USD | 1,070.00 USD | `-24.92%` | `2,018,000,000.00` |
| `Live` | `Long` | `532.50` | 5,640,000.00 USD | 0.00 USD | 632.08 USD | `-24.78%` | `1,187,000,000.00` |
| `Live` | `Long` | `533.50` | 5,640,000.00 USD | 0.00 USD | 1,320.00 USD | `-24.64%` | `2,468,000,000.00` |
| `Live` | `Long` | `534.50` | 5,630,000.00 USD | 0.00 USD | 1,630.00 USD | `-24.50%` | `3,054,000,000.00` |
| `Live` | `Long` | `535.50` | 5,630,000.00 USD | 0.00 USD | 3,250.00 USD | `-24.36%` | `6,065,000,000.00` |
| `Live` | `Long` | `536.50` | 5,630,000.00 USD | 0.00 USD | 100.33 USD | `-24.21%` | `187,000,000.00` |
| `Live` | `Long` | `539.50` | 5,630,000.00 USD | 0.00 USD | 2,150.00 USD | `-23.79%` | `3,982,000,000.00` |
| `Live` | `Long` | `540.50` | 5,630,000.00 USD | 0.00 USD | 1,760.00 USD | `-23.65%` | `3,256,000,000.00` |
| `Live` | `Long` | `541.50` | 5,630,000.00 USD | 0.00 USD | 472.19 USD | `-23.51%` | `872,000,000.00` |
| `Live` | `Long` | `543.50` | 5,620,000.00 USD | 0.00 USD | 334.25 USD | `-23.23%` | `615,000,000.00` |
| `Live` | `Long` | `545.50` | 5,620,000.00 USD | 0.00 USD | 212,310.00 USD | `-22.94%` | `389,204,000,000.00` |
| `Live` | `Long` | `546.50` | 5,410,000.00 USD | 0.00 USD | 491.85 USD | `-22.80%` | `900,000,000.00` |
| `Live` | `Long` | `547.50` | 5,410,000.00 USD | 0.00 USD | 531.07 USD | `-22.66%` | `970,000,000.00` |
| `Live` | `Long` | `548.50` | 5,410,000.00 USD | 0.00 USD | 1,580.00 USD | `-22.52%` | `2,883,000,000.00` |
| `Live` | `Long` | `549.50` | 5,410,000.00 USD | 0.00 USD | 1,770.00 USD | `-22.38%` | `3,224,000,000.00` |
| `Live` | `Long` | `550.50` | 5,410,000.00 USD | 0.00 USD | 1,700.00 USD | `-22.24%` | `3,080,000,000.00` |
| `Live` | `Long` | `552.50` | 5,410,000.00 USD | 0.00 USD | 959.69 USD | `-21.95%` | `1,737,000,000.00` |
| `Live` | `Long` | `553.50` | 5,410,000.00 USD | 0.00 USD | 2,730.00 USD | `-21.81%` | `4,937,000,000.00` |
| `Live` | `Long` | `554.50` | 5,400,000.00 USD | 0.00 USD | 2,010.00 USD | `-21.67%` | `3,625,000,000.00` |
| `Live` | `Long` | `555.50` | 5,400,000.00 USD | 0.00 USD | 274.97 USD | `-21.53%` | `495,000,000.00` |
| `Live` | `Long` | `557.50` | 5,400,000.00 USD | 0.00 USD | 5,680.00 USD | `-21.25%` | `10,193,000,000.00` |
| `Live` | `Long` | `559.50` | 5,390,000.00 USD | 0.00 USD | 15,990.00 USD | `-20.97%` | `28,584,000,000.00` |
| `Live` | `Long` | `560.50` | 5,380,000.00 USD | 0.00 USD | 3,450.00 USD | `-20.82%` | `6,153,000,000.00` |
| `Live` | `Long` | `561.50` | 5,370,000.00 USD | 0.00 USD | 583.40 USD | `-20.68%` | `1,039,000,000.00` |
| `Live` | `Long` | `562.50` | 5,370,000.00 USD | 0.00 USD | 10,240.00 USD | `-20.54%` | `18,201,000,000.00` |
| `Live` | `Long` | `565.50` | 5,360,000.00 USD | 0.00 USD | 160,430.00 USD | `-20.12%` | `283,700,000,000.00` |
| `Live` | `Long` | `566.50` | 5,200,000.00 USD | 0.00 USD | 453.20 USD | `-19.98%` | `800,000,000.00` |
| `Live` | `Long` | `567.50` | 5,200,000.00 USD | 0.00 USD | 24,450.00 USD | `-19.84%` | `43,079,000,000.00` |
| `Live` | `Long` | `568.50` | 5,180,000.00 USD | 0.00 USD | 20,310.00 USD | `-19.69%` | `35,721,000,000.00` |
| `Live` | `Long` | `569.50` | 5,160,000.00 USD | 0.00 USD | 144.08 USD | `-19.55%` | `253,000,000.00` |
| `Live` | `Long` | `570.50` | 5,160,000.00 USD | 0.00 USD | 296.09 USD | `-19.41%` | `519,000,000.00` |
| `Live` | `Long` | `571.50` | 5,160,000.00 USD | 0.00 USD | 1,030.00 USD | `-19.27%` | `1,800,000,000.00` |
| `Live` | `Long` | `572.50` | 5,160,000.00 USD | 0.00 USD | 722,500.00 USD | `-19.13%` | `1,262,009,000,000.00` |
| `Live` | `Long` | `574.50` | 4,430,000.00 USD | 0.00 USD | 610.69 USD | `-18.85%` | `1,063,000,000.00` |
| `Live` | `Long` | `576.50` | 4,430,000.00 USD | 0.00 USD | 416.23 USD | `-18.56%` | `722,000,000.00` |
| `Live` | `Long` | `578.50` | 4,430,000.00 USD | 0.00 USD | 5,790.00 USD | `-18.28%` | `10,000,000,000.00` |
| `Live` | `Long` | `579.50` | 4,430,000.00 USD | 0.00 USD | 1,860.00 USD | `-18.14%` | `3,202,000,000.00` |
| `Live` | `Long` | `581.50` | 4,430,000.00 USD | 0.00 USD | 35,070.00 USD | `-17.86%` | `60,313,000,000.00` |
| `Live` | `Long` | `582.50` | 4,390,000.00 USD | 0.00 USD | 274.94 USD | `-17.72%` | `472,000,000.00` |
| `Live` | `Long` | `583.50` | 4,390,000.00 USD | 0.00 USD | 313.34 USD | `-17.58%` | `537,000,000.00` |
| `Live` | `Long` | `584.50` | 4,390,000.00 USD | 0.00 USD | 3,060.00 USD | `-17.43%` | `5,239,000,000.00` |
| `Live` | `Long` | `586.50` | 4,390,000.00 USD | 0.00 USD | 826.96 USD | `-17.15%` | `1,410,000,000.00` |
| `Live` | `Long` | `587.50` | 4,390,000.00 USD | 0.00 USD | 3,560.00 USD | `-17.01%` | `6,065,000,000.00` |
| `Live` | `Long` | `588.50` | 4,380,000.00 USD | 0.00 USD | 271.89 USD | `-16.87%` | `462,000,000.00` |
| `Live` | `Long` | `589.50` | 4,380,000.00 USD | 0.00 USD | 203.38 USD | `-16.73%` | `345,000,000.00` |
| `Live` | `Long` | `590.50` | 4,380,000.00 USD | 0.00 USD | 5,360.00 USD | `-16.59%` | `9,079,000,000.00` |
| `Live` | `Long` | `591.50` | 4,380,000.00 USD | 0.00 USD | 4,670.00 USD | `-16.45%` | `7,889,000,000.00` |
| `Live` | `Long` | `592.50` | 4,370,000.00 USD | 0.00 USD | 840.76 USD | `-16.30%` | `1,419,000,000.00` |
| `Live` | `Long` | `593.50` | 4,370,000.00 USD | 0.00 USD | 255,210.00 USD | `-16.16%` | `430,000,000,000.00` |
| `Live` | `Long` | `594.50` | 4,120,000.00 USD | 0.00 USD | 45,110.00 USD | `-16.02%` | `75,871,000,000.00` |
| `Live` | `Long` | `595.50` | 4,070,000.00 USD | 0.00 USD | 12,660.00 USD | `-15.88%` | `21,262,000,000.00` |
| `Live` | `Long` | `596.50` | 4,060,000.00 USD | 0.00 USD | 15,090.00 USD | `-15.74%` | `25,291,000,000.00` |
| `Live` | `Long` | `597.50` | 4,040,000.00 USD | 0.00 USD | 311.30 USD | `-15.60%` | `521,000,000.00` |
| `Live` | `Long` | `598.50` | 4,040,000.00 USD | 0.00 USD | 217.26 USD | `-15.46%` | `363,000,000.00` |
| `Live` | `Long` | `599.50` | 4,040,000.00 USD | 0.00 USD | 116.90 USD | `-15.32%` | `195,000,000.00` |
| `Live` | `Long` | `600.50` | 4,040,000.00 USD | 0.00 USD | 5,150.00 USD | `-15.17%` | `8,576,000,000.00` |
| `Live` | `Long` | `601.50` | 4,040,000.00 USD | 0.00 USD | 58,030.00 USD | `-15.03%` | `96,477,000,000.00` |
| `Live` | `Long` | `602.50` | 3,980,000.00 USD | 0.00 USD | 16,910.00 USD | `-14.89%` | `28,061,000,000.00` |
| `Live` | `Long` | `604.50` | 3,960,000.00 USD | 0.00 USD | 1,610.00 USD | `-14.61%` | `2,671,000,000.00` |
| `Live` | `Long` | `606.50` | 3,960,000.00 USD | 0.00 USD | 169.82 USD | `-14.33%` | `280,000,000.00` |
| `Live` | `Long` | `607.50` | 3,960,000.00 USD | 0.00 USD | 1,880.00 USD | `-14.19%` | `3,092,000,000.00` |
| `Live` | `Long` | `610.50` | 3,960,000.00 USD | 0.00 USD | 213.67 USD | `-13.76%` | `350,000,000.00` |
| `Live` | `Long` | `613.50` | 3,960,000.00 USD | 0.00 USD | 12,270.00 USD | `-13.34%` | `20,000,000,000.00` |
| `Live` | `Long` | `614.50` | 3,950,000.00 USD | 0.00 USD | 1,440.00 USD | `-13.20%` | `2,350,000,000.00` |
| `Live` | `Long` | `615.50` | 3,940,000.00 USD | 0.00 USD | 8,870.00 USD | `-13.06%` | `14,411,000,000.00` |
| `Live` | `Long` | `616.50` | 3,940,000.00 USD | 0.00 USD | 1,540.00 USD | `-12.91%` | `2,500,000,000.00` |
| `Live` | `Long` | `617.50` | 3,930,000.00 USD | 0.00 USD | 156.23 USD | `-12.77%` | `253,000,000.00` |
| `Live` | `Long` | `618.50` | 3,930,000.00 USD | 0.00 USD | 9,040.00 USD | `-12.63%` | `14,614,000,000.00` |
| `Live` | `Long` | `620.50` | 3,930,000.00 USD | 0.00 USD | 5,410.00 USD | `-12.35%` | `8,712,000,000.00` |
| `Live` | `Long` | `621.50` | 3,920,000.00 USD | 0.00 USD | 3,230.00 USD | `-12.21%` | `5,194,000,000.00` |
| `Live` | `Long` | `623.50` | 3,920,000.00 USD | 0.00 USD | 1,050.00 USD | `-11.93%` | `1,691,000,000.00` |
| `Live` | `Long` | `624.50` | 3,920,000.00 USD | 0.00 USD | 16,600.00 USD | `-11.78%` | `26,582,000,000.00` |
| `Live` | `Long` | `625.50` | 3,900,000.00 USD | 0.00 USD | 25,330.00 USD | `-11.64%` | `40,495,000,000.00` |
| `Live` | `Long` | `627.50` | 3,870,000.00 USD | 0.00 USD | 326.30 USD | `-11.36%` | `520,000,000.00` |
| `Live` | `Long` | `628.50` | 3,870,000.00 USD | 0.00 USD | 9,420.00 USD | `-11.22%` | `14,982,000,000.00` |
| `Live` | `Long` | `629.50` | 3,860,000.00 USD | 0.00 USD | 1,150,000.00 USD | `-11.08%` | `1,825,330,000,000.00` |
| `Live` | `Long` | `630.50` | 2,710,000.00 USD | 0.00 USD | 252,440.00 USD | `-10.94%` | `400,380,000,000.00` |
| `Live` | `Long` | `632.50` | 2,460,000.00 USD | 0.00 USD | 125.87 USD | `-10.65%` | `199,000,000.00` |
| `Live` | `Long` | `633.50` | 2,460,000.00 USD | 0.00 USD | 4,540.00 USD | `-10.51%` | `7,161,000,000.00` |
| `Live` | `Long` | `635.50` | 2,460,000.00 USD | 0.00 USD | 5,910.00 USD | `-10.23%` | `9,302,000,000.00` |
| `Live` | `Long` | `636.50` | 2,450,000.00 USD | 0.00 USD | 155.31 USD | `-10.09%` | `244,000,000.00` |
| `Live` | `Long` | `637.50` | 2,450,000.00 USD | 0.00 USD | 1,110.00 USD | `-9.95%` | `1,743,000,000.00` |
| `Live` | `Long` | `638.50` | 2,450,000.00 USD | 0.00 USD | 432.90 USD | `-9.81%` | `678,000,000.00` |
| `Live` | `Long` | `639.50` | 2,450,000.00 USD | 0.00 USD | 746.30 USD | `-9.66%` | `1,167,000,000.00` |
| `Live` | `Long` | `640.50` | 2,450,000.00 USD | 0.00 USD | 97,540.00 USD | `-9.52%` | `152,289,000,000.00` |
| `Live` | `Long` | `641.50` | 2,350,000.00 USD | 0.00 USD | 1,670.00 USD | `-9.38%` | `2,606,000,000.00` |
| `Live` | `Long` | `642.50` | 2,350,000.00 USD | 0.00 USD | 8,970.00 USD | `-9.24%` | `13,954,000,000.00` |
| `Live` | `Long` | `644.50` | 2,340,000.00 USD | 0.00 USD | 3,470.00 USD | `-8.96%` | `5,387,000,000.00` |
| `Live` | `Long` | `645.50` | 2,340,000.00 USD | 0.00 USD | 2,070.00 USD | `-8.82%` | `3,202,000,000.00` |
| `Live` | `Long` | `646.50` | 2,340,000.00 USD | 0.00 USD | 463.54 USD | `-8.68%` | `717,000,000.00` |
| `Live` | `Long` | `648.50` | 2,340,000.00 USD | 0.00 USD | 5,190.00 USD | `-8.39%` | `8,000,000,000.00` |
| `Live` | `Long` | `649.50` | 2,330,000.00 USD | 0.00 USD | 1,120.00 USD | `-8.25%` | `1,718,000,000.00` |
| `Live` | `Long` | `650.50` | 2,330,000.00 USD | 0.00 USD | 2,930.00 USD | `-8.11%` | `4,501,000,000.00` |
| `Live` | `Long` | `651.50` | 2,330,000.00 USD | 0.00 USD | 1,520,000.00 USD | `-7.97%` | `2,337,126,000,000.00` |
| `Live` | `Long` | `652.50` | 803,480.00 USD | 0.00 USD | 1,420.00 USD | `-7.83%` | `2,172,000,000.00` |
| `Live` | `Long` | `653.50` | 802,060.00 USD | 0.00 USD | 298.00 USD | `-7.69%` | `456,000,000.00` |
| `Live` | `Long` | `654.50` | 801,760.00 USD | 0.00 USD | 97,530.00 USD | `-7.55%` | `149,014,000,000.00` |
| `Live` | `Long` | `656.50` | 704,230.00 USD | 0.00 USD | 122.77 USD | `-7.26%` | `187,000,000.00` |
| `Live` | `Long` | `658.50` | 704,110.00 USD | 0.00 USD | 1,540.00 USD | `-6.98%` | `2,345,000,000.00` |
| `Live` | `Long` | `659.50` | 702,570.00 USD | 0.00 USD | 313,710.00 USD | `-6.84%` | `475,681,000,000.00` |
| `Live` | `Long` | `660.50` | 388,860.00 USD | 0.00 USD | 46,960.00 USD | `-6.70%` | `71,102,000,000.00` |
| `Live` | `Long` | `661.50` | 341,890.00 USD | 0.00 USD | 1,070.00 USD | `-6.56%` | `1,622,000,000.00` |
| `Live` | `Long` | `662.50` | 340,820.00 USD | 0.00 USD | 111,140.00 USD | `-6.42%` | `167,766,000,000.00` |
| `Live` | `Long` | `663.50` | 229,670.00 USD | 0.00 USD | 2,590.00 USD | `-6.27%` | `3,909,000,000.00` |
| `Live` | `Long` | `664.50` | 227,080.00 USD | 0.00 USD | 37,920.00 USD | `-6.13%` | `57,066,000,000.00` |
| `Live` | `Long` | `665.50` | 189,160.00 USD | 0.00 USD | 131.10 USD | `-5.99%` | `197,000,000.00` |
| `Live` | `Short` | `666.50` | 794,320.00 USD | 794,320.00 USD | 0.00 USD | `-5.85%` | `1,191,773,000,000.00` |
| `Live` | `Short` | `667.50` | 796,860.00 USD | 2,550.00 USD | 0.00 USD | `-5.71%` | `3,815,000,000.00` |
| `Live` | `Short` | `668.50` | 798,630.00 USD | 1,770.00 USD | 0.00 USD | `-5.57%` | `2,644,000,000.00` |
| `Live` | `Short` | `669.50` | 868,650.00 USD | 70,020.00 USD | 0.00 USD | `-5.43%` | `104,585,000,000.00` |
| `Live` | `Short` | `670.50` | 876,910.00 USD | 8,260.00 USD | 0.00 USD | `-5.29%` | `12,315,000,000.00` |
| `Live` | `Long` | `671.50` | 189,030.00 USD | 0.00 USD | 115,780.00 USD | `-5.14%` | `172,425,000,000.00` |
| `Live` | `Short` | `672.50` | 888,500.00 USD | 11,590.00 USD | 0.00 USD | `-5.00%` | `17,231,000,000.00` |
| `Live` | `Long` | `673.50` | 73,250.00 USD | 0.00 USD | 18,880.00 USD | `-4.86%` | `28,036,000,000.00` |
| `Live` | `Long` | `674.50` | 54,360.00 USD | 0.00 USD | 8,680.00 USD | `-4.72%` | `12,872,000,000.00` |
| `Live` | `Long` | `675.50` | 45,680.00 USD | 0.00 USD | 14,390.00 USD | `-4.58%` | `21,297,000,000.00` |
| `Live` | `Long` | `676.50` | 31,300.00 USD | 0.00 USD | 1,940.00 USD | `-4.44%` | `2,871,000,000.00` |
| `Live` | `Long` | `677.50` | 29,350.00 USD | 0.00 USD | 983.73 USD | `-4.30%` | `1,452,000,000.00` |
| `Live` | `Long` | `678.50` | 28,370.00 USD | 0.00 USD | 14,770.00 USD | `-4.16%` | `21,775,000,000.00` |
| `Live` | `Short` | `679.50` | 889,760.00 USD | 1,260.00 USD | 0.00 USD | `-4.01%` | `1,860,000,000.00` |
| `Live` | `Long` | `680.50` | 13,600.00 USD | 0.00 USD | 2,010.00 USD | `-3.87%` | `2,958,000,000.00` |
| `Live` | `Long` | `681.50` | 11,580.00 USD | 0.00 USD | 11,580.00 USD | `-3.73%` | `16,995,000,000.00` |
| `Live` | `Short` | `687.50` | 889,880.00 USD | 124.44 USD | 0.00 USD | `-2.88%` | `181,000,000.00` |
| `Live` | `Short` | `702.50` | 1,740,000.00 USD | 848,660.00 USD | 0.00 USD | `-0.77%` | `1,208,060,000,000.00` |
| `Live` | `Short` | `710.50` | 1,740,000.00 USD | 2,000.00 USD | 0.00 USD | `+0.36%` | `2,817,000,000.00` |
| `Live` | `Short` | `711.50` | 1,740,000.00 USD | 1,030.00 USD | 0.00 USD | `+0.51%` | `1,445,000,000.00` |
| `Live` | `Short` | `721.50` | 1,750,000.00 USD | 5,570.00 USD | 0.00 USD | `+1.92%` | `7,724,000,000.00` |
| `Live` | `Short` | `722.50` | 1,750,000.00 USD | 3,410.00 USD | 0.00 USD | `+2.06%` | `4,718,000,000.00` |
| `Live` | `Short` | `723.50` | 1,770,000.00 USD | 23,050.00 USD | 0.00 USD | `+2.20%` | `31,859,000,000.00` |
| `Live` | `Short` | `724.50` | 1,780,000.00 USD | 5,780.00 USD | 0.00 USD | `+2.34%` | `7,972,000,000.00` |
| `Live` | `Short` | `725.50` | 1,780,000.00 USD | 4,390.00 USD | 0.00 USD | `+2.48%` | `6,046,000,000.00` |
| `Live` | `Short` | `726.50` | 1,780,000.00 USD | 912.48 USD | 0.00 USD | `+2.62%` | `1,256,000,000.00` |
| `Live` | `Short` | `727.50` | 1,800,000.00 USD | 16,960.00 USD | 0.00 USD | `+2.77%` | `23,313,000,000.00` |
| `Live` | `Short` | `728.50` | 1,810,000.00 USD | 10,340.00 USD | 0.00 USD | `+2.91%` | `14,199,000,000.00` |
| `Live` | `Short` | `729.50` | 1,840,000.00 USD | 30,550.00 USD | 0.00 USD | `+3.05%` | `41,873,000,000.00` |
| `Live` | `Short` | `730.50` | 1,880,000.00 USD | 34,300.00 USD | 0.00 USD | `+3.19%` | `46,953,000,000.00` |
| `Live` | `Short` | `731.50` | 1,920,000.00 USD | 41,490.00 USD | 0.00 USD | `+3.33%` | `56,720,000,000.00` |
| `Live` | `Short` | `732.50` | 2,050,000.00 USD | 132,460.00 USD | 0.00 USD | `+3.47%` | `180,839,000,000.00` |
| `Live` | `Short` | `733.50` | 2,270,000.00 USD | 214,400.00 USD | 0.00 USD | `+3.61%` | `292,299,000,000.00` |
| `Live` | `Short` | `734.50` | 2,390,000.00 USD | 125,010.00 USD | 0.00 USD | `+3.75%` | `170,201,000,000.00` |
| `Live` | `Short` | `735.50` | 2,460,000.00 USD | 72,690.00 USD | 0.00 USD | `+3.90%` | `98,831,000,000.00` |
| `Live` | `Short` | `736.50` | 2,470,000.00 USD | 8,960.00 USD | 0.00 USD | `+4.04%` | `12,168,000,000.00` |
| `Live` | `Short` | `737.50` | 2,500,000.00 USD | 25,410.00 USD | 0.00 USD | `+4.18%` | `34,453,000,000.00` |
| `Live` | `Short` | `738.50` | 2,510,000.00 USD | 8,090.00 USD | 0.00 USD | `+4.32%` | `10,960,000,000.00` |
| `Live` | `Short` | `739.50` | 2,630,000.00 USD | 127,330.00 USD | 0.00 USD | `+4.46%` | `172,182,000,000.00` |
| `Live` | `Short` | `740.50` | 2,650,000.00 USD | 20,070.00 USD | 0.00 USD | `+4.60%` | `27,098,000,000.00` |
| `Live` | `Short` | `741.50` | 2,650,000.00 USD | 424.14 USD | 0.00 USD | `+4.74%` | `572,000,000.00` |
| `Live` | `Short` | `742.50` | 2,800,000.00 USD | 146,070.00 USD | 0.00 USD | `+4.88%` | `196,734,000,000.00` |
| `Live` | `Short` | `743.50` | 2,880,000.00 USD | 76,990.00 USD | 0.00 USD | `+5.03%` | `103,550,000,000.00` |
| `Live` | `Short` | `744.50` | 2,890,000.00 USD | 8,770.00 USD | 0.00 USD | `+5.17%` | `11,780,000,000.00` |
| `Live` | `Short` | `745.50` | 2,900,000.00 USD | 17,630.00 USD | 0.00 USD | `+5.31%` | `23,651,000,000.00` |
| `Live` | `Short` | `746.50` | 3,310,000.00 USD | 402,950.00 USD | 0.00 USD | `+5.45%` | `539,783,000,000.00` |
| `Live` | `Short` | `747.50` | 3,310,000.00 USD | 470.93 USD | 0.00 USD | `+5.59%` | `630,000,000.00` |
| `Live` | `Short` | `748.50` | 3,550,000.00 USD | 240,840.00 USD | 0.00 USD | `+5.73%` | `321,770,000,000.00` |
| `Live` | `Short` | `749.50` | 3,710,000.00 USD | 164,820.00 USD | 0.00 USD | `+5.87%` | `219,900,000,000.00` |
| `Live` | `Short` | `750.50` | 3,880,000.00 USD | 171,680.00 USD | 0.00 USD | `+6.01%` | `228,759,000,000.00` |
| `Live` | `Short` | `751.50` | 4,450,000.00 USD | 562,240.00 USD | 0.00 USD | `+6.16%` | `748,163,000,000.00` |
| `Live` | `Short` | `752.50` | 4,450,000.00 USD | 3,910.00 USD | 0.00 USD | `+6.30%` | `5,198,000,000.00` |
| `Live` | `Short` | `755.50` | 4,450,000.00 USD | 3,500.00 USD | 0.00 USD | `+6.72%` | `4,630,000,000.00` |
| `Live` | `Short` | `756.50` | 4,450,000.00 USD | 583.26 USD | 0.00 USD | `+6.86%` | `771,000,000.00` |
| `Live` | `Short` | `758.50` | 5,340,000.00 USD | 882,460.00 USD | 0.00 USD | `+7.14%` | `1,163,432,000,000.00` |
| `Live` | `Short` | `759.50` | 6,110,000.00 USD | 769,300.00 USD | 0.00 USD | `+7.29%` | `1,012,903,000,000.00` |
| `Live` | `Short` | `760.50` | 6,120,000.00 USD | 13,580.00 USD | 0.00 USD | `+7.43%` | `17,854,000,000.00` |
| `Live` | `Short` | `761.50` | 6,120,000.00 USD | 541.43 USD | 0.00 USD | `+7.57%` | `711,000,000.00` |
| `Live` | `Short` | `762.50` | 6,130,000.00 USD | 10,640.00 USD | 0.00 USD | `+7.71%` | `13,953,000,000.00` |
| `Live` | `Short` | `763.50` | 6,570,000.00 USD | 435,970.00 USD | 0.00 USD | `+7.85%` | `571,013,000,000.00` |
| `Live` | `Short` | `765.50` | 6,580,000.00 USD | 9,770.00 USD | 0.00 USD | `+8.13%` | `12,758,000,000.00` |
| `Live` | `Short` | `767.50` | 6,580,000.00 USD | 3,950.00 USD | 0.00 USD | `+8.42%` | `5,143,000,000.00` |
| `Live` | `Short` | `768.50` | 6,600,000.00 USD | 21,880.00 USD | 0.00 USD | `+8.56%` | `28,476,000,000.00` |
| `Live` | `Short` | `769.50` | 6,830,000.00 USD | 231,890.00 USD | 0.00 USD | `+8.70%` | `301,348,000,000.00` |
| `Live` | `Short` | `770.50` | 6,860,000.00 USD | 27,930.00 USD | 0.00 USD | `+8.84%` | `36,248,000,000.00` |
| `Live` | `Short` | `771.50` | 6,890,000.00 USD | 27,330.00 USD | 0.00 USD | `+8.98%` | `35,419,000,000.00` |
| `Live` | `Short` | `773.50` | 6,900,000.00 USD | 8,960.00 USD | 0.00 USD | `+9.26%` | `11,578,000,000.00` |
| `Live` | `Short` | `774.50` | 6,900,000.00 USD | 130.12 USD | 0.00 USD | `+9.41%` | `168,000,000.00` |
| `Live` | `Short` | `777.50` | 6,900,000.00 USD | 541.14 USD | 0.00 USD | `+9.83%` | `696,000,000.00` |
| `Live` | `Short` | `779.50` | 6,900,000.00 USD | 3,200.00 USD | 0.00 USD | `+10.11%` | `4,107,000,000.00` |
| `Live` | `Short` | `780.50` | 6,910,000.00 USD | 9,280.00 USD | 0.00 USD | `+10.25%` | `11,890,000,000.00` |
| `Live` | `Short` | `781.50` | 6,940,000.00 USD | 33,510.00 USD | 0.00 USD | `+10.39%` | `42,876,000,000.00` |
| `Live` | `Short` | `782.50` | 7,020,000.00 USD | 78,440.00 USD | 0.00 USD | `+10.54%` | `100,238,000,000.00` |
| `Live` | `Short` | `786.50` | 7,030,000.00 USD | 4,910.00 USD | 0.00 USD | `+11.10%` | `6,245,000,000.00` |
| `Live` | `Short` | `787.50` | 7,150,000.00 USD | 122,290.00 USD | 0.00 USD | `+11.24%` | `155,292,000,000.00` |
| `Live` | `Short` | `788.50` | 7,230,000.00 USD | 76,210.00 USD | 0.00 USD | `+11.38%` | `96,653,000,000.00` |
| `Live` | `Short` | `789.50` | 7,230,000.00 USD | 5,800.00 USD | 0.00 USD | `+11.52%` | `7,341,000,000.00` |
| `Live` | `Short` | `794.50` | 7,240,000.00 USD | 7,270.00 USD | 0.00 USD | `+12.23%` | `9,152,000,000.00` |
| `Live` | `Short` | `795.50` | 7,240,000.00 USD | 5,530.00 USD | 0.00 USD | `+12.37%` | `6,952,000,000.00` |
| `Live` | `Short` | `796.50` | 7,250,000.00 USD | 1,500.00 USD | 0.00 USD | `+12.51%` | `1,884,000,000.00` |
| `Live` | `Short` | `797.50` | 7,250,000.00 USD | 4,340.00 USD | 0.00 USD | `+12.65%` | `5,441,000,000.00` |
| `Live` | `Short` | `799.50` | 7,330,000.00 USD | 76,490.00 USD | 0.00 USD | `+12.94%` | `95,670,000,000.00` |
| `Live` | `Short` | `800.50` | 7,330,000.00 USD | 191.32 USD | 0.00 USD | `+13.08%` | `239,000,000.00` |
| `Live` | `Short` | `801.50` | 7,330,000.00 USD | 746.20 USD | 0.00 USD | `+13.22%` | `931,000,000.00` |
| `Live` | `Short` | `802.50` | 7,330,000.00 USD | 279.27 USD | 0.00 USD | `+13.36%` | `348,000,000.00` |
| `Live` | `Short` | `803.50` | 7,850,000.00 USD | 517,250.00 USD | 0.00 USD | `+13.50%` | `643,751,000,000.00` |
| `Live` | `Short` | `804.50` | 8,070,000.00 USD | 220,280.00 USD | 0.00 USD | `+13.64%` | `273,808,000,000.00` |
| `Live` | `Short` | `805.50` | 8,080,000.00 USD | 14,110.00 USD | 0.00 USD | `+13.78%` | `17,515,000,000.00` |
| `Live` | `Short` | `806.50` | 8,120,000.00 USD | 44,210.00 USD | 0.00 USD | `+13.93%` | `54,814,000,000.00` |
| `Live` | `Short` | `808.50` | 8,140,000.00 USD | 12,520.00 USD | 0.00 USD | `+14.21%` | `15,488,000,000.00` |
| `Live` | `Short` | `810.50` | 8,200,000.00 USD | 65,450.00 USD | 0.00 USD | `+14.49%` | `80,753,000,000.00` |
| `Live` | `Short` | `812.50` | 8,210,000.00 USD | 9,310.00 USD | 0.00 USD | `+14.77%` | `11,458,000,000.00` |
| `Live` | `Short` | `814.50` | 8,210,000.00 USD | 692.32 USD | 0.00 USD | `+15.06%` | `850,000,000.00` |
| `Live` | `Short` | `816.50` | 8,210,000.00 USD | 1,740.00 USD | 0.00 USD | `+15.34%` | `2,128,000,000.00` |
| `Live` | `Short` | `817.50` | 8,220,000.00 USD | 1,630.00 USD | 0.00 USD | `+15.48%` | `1,992,000,000.00` |
| `Live` | `Short` | `818.50` | 8,370,000.00 USD | 149,880.00 USD | 0.00 USD | `+15.62%` | `183,121,000,000.00` |
| `Live` | `Short` | `820.50` | 8,370,000.00 USD | 132.92 USD | 0.00 USD | `+15.90%` | `162,000,000.00` |
| `Live` | `Short` | `821.50` | 8,400,000.00 USD | 37,130.00 USD | 0.00 USD | `+16.04%` | `45,198,000,000.00` |
| `Live` | `Short` | `822.50` | 8,440,000.00 USD | 38,410.00 USD | 0.00 USD | `+16.19%` | `46,697,000,000.00` |
| `Live` | `Short` | `824.50` | 11,020,000.00 USD | 2,580,000.00 USD | 0.00 USD | `+16.47%` | `3,123,702,000,000.00` |
| `Live` | `Short` | `827.50` | 11,030,000.00 USD | 8,470.00 USD | 0.00 USD | `+16.89%` | `10,238,000,000.00` |
| `Live` | `Short` | `828.50` | 11,150,000.00 USD | 128,530.00 USD | 0.00 USD | `+17.03%` | `155,136,000,000.00` |
| `Live` | `Short` | `830.50` | 11,150,000.00 USD | 303.13 USD | 0.00 USD | `+17.32%` | `365,000,000.00` |
| `Live` | `Short` | `831.50` | 11,200,000.00 USD | 44,200.00 USD | 0.00 USD | `+17.46%` | `53,162,000,000.00` |
| `Live` | `Short` | `832.50` | 11,280,000.00 USD | 83,250.00 USD | 0.00 USD | `+17.60%` | `100,000,000,000.00` |
| `Live` | `Short` | `834.50` | 11,280,000.00 USD | 2,680.00 USD | 0.00 USD | `+17.88%` | `3,206,000,000.00` |
| `Live` | `Short` | `836.50` | 11,280,000.00 USD | 625.70 USD | 0.00 USD | `+18.16%` | `748,000,000.00` |
| `Live` | `Short` | `837.50` | 11,310,000.00 USD | 23,620.00 USD | 0.00 USD | `+18.30%` | `28,203,000,000.00` |
| `Live` | `Short` | `839.50` | 11,310,000.00 USD | 3,450.00 USD | 0.00 USD | `+18.59%` | `4,107,000,000.00` |
| `Live` | `Short` | `840.50` | 11,310,000.00 USD | 511.86 USD | 0.00 USD | `+18.73%` | `609,000,000.00` |
| `Live` | `Short` | `841.50` | 11,320,000.00 USD | 3,830.00 USD | 0.00 USD | `+18.87%` | `4,553,000,000.00` |
| `Live` | `Short` | `842.50` | 11,320,000.00 USD | 324.36 USD | 0.00 USD | `+19.01%` | `385,000,000.00` |
| `Live` | `Short` | `843.50` | 11,570,000.00 USD | 250,120.00 USD | 0.00 USD | `+19.15%` | `296,532,000,000.00` |
| `Live` | `Short` | `845.50` | 11,580,000.00 USD | 8,460.00 USD | 0.00 USD | `+19.43%` | `10,000,000,000.00` |
| `Live` | `Short` | `846.50` | 11,910,000.00 USD | 334,410.00 USD | 0.00 USD | `+19.58%` | `395,054,000,000.00` |
| `Live` | `Short` | `848.50` | 11,920,000.00 USD | 13,020.00 USD | 0.00 USD | `+19.86%` | `15,341,000,000.00` |
| `Live` | `Short` | `851.50` | 12,480,000.00 USD | 553,910.00 USD | 0.00 USD | `+20.28%` | `650,506,000,000.00` |
| `Live` | `Short` | `852.50` | 12,540,000.00 USD | 64,770.00 USD | 0.00 USD | `+20.42%` | `75,978,000,000.00` |
| `Live` | `Short` | `853.50` | 12,730,000.00 USD | 189,340.00 USD | 0.00 USD | `+20.56%` | `221,839,000,000.00` |
| `Live` | `Short` | `854.50` | 12,730,000.00 USD | 138.43 USD | 0.00 USD | `+20.71%` | `162,000,000.00` |
| `Live` | `Short` | `858.50` | 12,730,000.00 USD | 409.50 USD | 0.00 USD | `+21.27%` | `477,000,000.00` |
| `Live` | `Short` | `859.50` | 12,750,000.00 USD | 20,060.00 USD | 0.00 USD | `+21.41%` | `23,343,000,000.00` |
| `Live` | `Short` | `860.50` | 12,750,000.00 USD | 2,580.00 USD | 0.00 USD | `+21.55%` | `2,998,000,000.00` |
| `Live` | `Short` | `865.50` | 12,770,000.00 USD | 17,550.00 USD | 0.00 USD | `+22.26%` | `20,278,000,000.00` |
| `Live` | `Short` | `866.50` | 12,770,000.00 USD | 1,350.00 USD | 0.00 USD | `+22.40%` | `1,554,000,000.00` |
| `Live` | `Short` | `872.50` | 12,960,000.00 USD | 183,630.00 USD | 0.00 USD | `+23.25%` | `210,460,000,000.00` |
| `Live` | `Short` | `874.50` | 12,960,000.00 USD | 248.36 USD | 0.00 USD | `+23.53%` | `284,000,000.00` |
| `Live` | `Short` | `877.50` | 13,610,000.00 USD | 650,150.00 USD | 0.00 USD | `+23.95%` | `740,909,000,000.00` |
| `Live` | `Short` | `878.50` | 13,690,000.00 USD | 85,350.00 USD | 0.00 USD | `+24.10%` | `97,158,000,000.00` |
| `Live` | `Short` | `879.50` | 13,690,000.00 USD | 145.12 USD | 0.00 USD | `+24.24%` | `165,000,000.00` |
| `Live` | `Short` | `883.50` | 13,690,000.00 USD | 319.83 USD | 0.00 USD | `+24.80%` | `362,000,000.00` |
| `Live` | `Short` | `885.50` | 13,690,000.00 USD | 2,120.00 USD | 0.00 USD | `+25.08%` | `2,395,000,000.00` |
| `Live` | `Short` | `886.50` | 13,700,000.00 USD | 812.92 USD | 0.00 USD | `+25.23%` | `917,000,000.00` |
| `Live` | `Short` | `894.50` | 13,720,000.00 USD | 26,840.00 USD | 0.00 USD | `+26.36%` | `30,000,000,000.00` |
| `Live` | `Short` | `895.50` | 13,800,000.00 USD | 76,620.00 USD | 0.00 USD | `+26.50%` | `85,562,000,000.00` |
| `Live` | `Short` | `896.50` | 14,020,000.00 USD | 224,120.00 USD | 0.00 USD | `+26.64%` | `250,000,000,000.00` |
| `Live` | `Short` | `898.50` | 14,020,000.00 USD | 127.59 USD | 0.00 USD | `+26.92%` | `142,000,000.00` |
| `Live` | `Short` | `899.50` | 14,020,000.00 USD | 390.38 USD | 0.00 USD | `+27.06%` | `434,000,000.00` |
| `Live` | `Short` | `901.50` | 14,070,000.00 USD | 45,080.00 USD | 0.00 USD | `+27.34%` | `50,000,000,000.00` |
| `Live` | `Short` | `902.50` | 14,070,000.00 USD | 1,180.00 USD | 0.00 USD | `+27.49%` | `1,305,000,000.00` |
| `Live` | `Short` | `905.50` | 14,130,000.00 USD | 64,000.00 USD | 0.00 USD | `+27.91%` | `70,678,000,000.00` |
| `Live` | `Short` | `907.50` | 14,130,000.00 USD | 700.59 USD | 0.00 USD | `+28.19%` | `772,000,000.00` |
| `Live` | `Short` | `908.50` | 14,140,000.00 USD | 1,790.00 USD | 0.00 USD | `+28.33%` | `1,971,000,000.00` |
| `Live` | `Short` | `910.50` | 14,140,000.00 USD | 6,880.00 USD | 0.00 USD | `+28.62%` | `7,555,000,000.00` |
| `Live` | `Short` | `911.50` | 14,180,000.00 USD | 38,590.00 USD | 0.00 USD | `+28.76%` | `42,338,000,000.00` |
| `Live` | `Short` | `914.50` | 14,230,000.00 USD | 45,250.00 USD | 0.00 USD | `+29.18%` | `49,477,000,000.00` |
| `Live` | `Short` | `915.50` | 14,250,000.00 USD | 25,980.00 USD | 0.00 USD | `+29.32%` | `28,382,000,000.00` |
| `Live` | `Short` | `924.50` | 14,260,000.00 USD | 3,220.00 USD | 0.00 USD | `+30.59%` | `3,487,000,000.00` |
| `Live` | `Short` | `925.50` | 14,370,000.00 USD | 118,460.00 USD | 0.00 USD | `+30.74%` | `127,997,000,000.00` |
| `Live` | `Short` | `932.50` | 14,380,000.00 USD | 654.62 USD | 0.00 USD | `+31.72%` | `702,000,000.00` |
| `Live` | `Short` | `935.50` | 14,450,000.00 USD | 76,440.00 USD | 0.00 USD | `+32.15%` | `81,713,000,000.00` |
| `Live` | `Short` | `938.50` | 14,450,000.00 USD | 280.61 USD | 0.00 USD | `+32.57%` | `299,000,000.00` |
| `Live` | `Short` | `939.50` | 14,480,000.00 USD | 26,610.00 USD | 0.00 USD | `+32.71%` | `28,326,000,000.00` |
| `Live` | `Short` | `942.50` | 14,500,000.00 USD | 25,530.00 USD | 0.00 USD | `+33.14%` | `27,090,000,000.00` |
| `Live` | `Short` | `944.50` | 14,500,000.00 USD | 201.18 USD | 0.00 USD | `+33.42%` | `213,000,000.00` |
| `Live` | `Short` | `949.50` | 14,620,000.00 USD | 118,620.00 USD | 0.00 USD | `+34.13%` | `124,934,000,000.00` |
| `Live` | `Short` | `950.50` | 14,660,000.00 USD | 41,140.00 USD | 0.00 USD | `+34.27%` | `43,282,000,000.00` |
| `Live` | `Short` | `951.50` | 14,670,000.00 USD | 1,680.00 USD | 0.00 USD | `+34.41%` | `1,763,000,000.00` |
| `Live` | `Short` | `952.50` | 14,670,000.00 USD | 398.14 USD | 0.00 USD | `+34.55%` | `418,000,000.00` |
| `Live` | `Short` | `954.50` | 14,670,000.00 USD | 440.02 USD | 0.00 USD | `+34.83%` | `461,000,000.00` |
| `Live` | `Short` | `955.50` | 14,670,000.00 USD | 8,000.00 USD | 0.00 USD | `+34.97%` | `8,375,000,000.00` |
| `Live` | `Short` | `960.50` | 14,670,000.00 USD | 101.81 USD | 0.00 USD | `+35.68%` | `106,000,000.00` |
| `Live` | `Short` | `962.50` | 14,670,000.00 USD | 118.39 USD | 0.00 USD | `+35.96%` | `123,000,000.00` |
| `Live` | `Short` | `963.50` | 14,670,000.00 USD | 114.66 USD | 0.00 USD | `+36.10%` | `119,000,000.00` |
| `Live` | `Short` | `966.50` | 17,020,000.00 USD | 2,350,000.00 USD | 0.00 USD | `+36.53%` | `2,429,891,000,000.00` |
| `Live` | `Short` | `968.50` | 17,030,000.00 USD | 1,940.00 USD | 0.00 USD | `+36.81%` | `2,000,000,000.00` |
| `Live` | `Short` | `970.50` | 18,180,000.00 USD | 1,160,000.00 USD | 0.00 USD | `+37.09%` | `1,191,180,000,000.00` |
| `Live` | `Short` | `977.50` | 18,210,000.00 USD | 25,910.00 USD | 0.00 USD | `+38.08%` | `26,505,000,000.00` |
| `Live` | `Short` | `978.50` | 18,220,000.00 USD | 13,400.00 USD | 0.00 USD | `+38.22%` | `13,697,000,000.00` |
| `Live` | `Short` | `979.50` | 18,240,000.00 USD | 19,590.00 USD | 0.00 USD | `+38.36%` | `20,000,000,000.00` |
| `Live` | `Short` | `981.50` | 18,250,000.00 USD | 14,480.00 USD | 0.00 USD | `+38.65%` | `14,758,000,000.00` |
| `Live` | `Short` | `986.50` | 18,260,000.00 USD | 1,100.00 USD | 0.00 USD | `+39.35%` | `1,112,000,000.00` |
| `Live` | `Short` | `987.50` | 18,270,000.00 USD | 9,910.00 USD | 0.00 USD | `+39.49%` | `10,031,000,000.00` |
| `Live` | `Short` | `990.50` | 18,290,000.00 USD | 28,300.00 USD | 0.00 USD | `+39.92%` | `28,570,000,000.00` |
| `Live` | `Short` | `993.50` | 18,400,000.00 USD | 103,500.00 USD | 0.00 USD | `+40.34%` | `104,176,000,000.00` |
| `Live` | `Short` | `994.50` | 18,680,000.00 USD | 285,520.00 USD | 0.00 USD | `+40.48%` | `287,098,000,000.00` |
| `Live` | `Short` | `998.50` | 18,690,000.00 USD | 7,310.00 USD | 0.00 USD | `+41.05%` | `7,316,000,000.00` |
| `Live` | `Short` | `1000.50` | 18,690,000.00 USD | 194.10 USD | 0.00 USD | `+41.33%` | `194,000,000.00` |
| `Live` | `Short` | `1001.50` | 18,690,000.00 USD | 139.21 USD | 0.00 USD | `+41.47%` | `139,000,000.00` |
| `Live` | `Short` | `1002.50` | 18,710,000.00 USD | 17,540.00 USD | 0.00 USD | `+41.61%` | `17,497,000,000.00` |
| `Live` | `Short` | `1004.50` | 18,850,000.00 USD | 143,120.00 USD | 0.00 USD | `+41.89%` | `142,479,000,000.00` |
| `Live` | `Short` | `1005.50` | 18,850,000.00 USD | 1,570.00 USD | 0.00 USD | `+42.04%` | `1,564,000,000.00` |
| `Live` | `Short` | `1006.50` | 18,870,000.00 USD | 18,010.00 USD | 0.00 USD | `+42.18%` | `17,898,000,000.00` |
| `Live` | `Short` | `1014.50` | 18,910,000.00 USD | 42,460.00 USD | 0.00 USD | `+43.31%` | `41,858,000,000.00` |
| `Live` | `Short` | `1015.50` | 19,120,000.00 USD | 203,100.00 USD | 0.00 USD | `+43.45%` | `200,000,000,000.00` |
| `Live` | `Short` | `1017.50` | 19,180,000.00 USD | 59,630.00 USD | 0.00 USD | `+43.73%` | `58,601,000,000.00` |
| `Live` | `Short` | `1023.50` | 19,180,000.00 USD | 6,080.00 USD | 0.00 USD | `+44.58%` | `5,940,000,000.00` |
| `Live` | `Short` | `1025.50` | 19,190,000.00 USD | 2,850.00 USD | 0.00 USD | `+44.86%` | `2,777,000,000.00` |
| `Live` | `Short` | `1027.50` | 19,900,000.00 USD | 716,800.00 USD | 0.00 USD | `+45.14%` | `697,611,000,000.00` |
| `Live` | `Short` | `1032.50` | 20,570,000.00 USD | 663,870.00 USD | 0.00 USD | `+45.85%` | `642,971,000,000.00` |
| `Live` | `Short` | `1036.50` | 20,570,000.00 USD | 2,470.00 USD | 0.00 USD | `+46.41%` | `2,384,000,000.00` |
| `Live` | `Short` | `1037.50` | 20,690,000.00 USD | 118,280.00 USD | 0.00 USD | `+46.56%` | `114,000,000,000.00` |
| `Live` | `Short` | `1050.50` | 20,690,000.00 USD | 500.04 USD | 0.00 USD | `+48.39%` | `476,000,000.00` |
| `Live` | `Short` | `1051.50` | 21,080,000.00 USD | 393,920.00 USD | 0.00 USD | `+48.53%` | `374,623,000,000.00` |
| `Live` | `Short` | `1058.50` | 21,090,000.00 USD | 6,040.00 USD | 0.00 USD | `+49.52%` | `5,710,000,000.00` |
| `Live` | `Short` | `1059.50` | 21,150,000.00 USD | 66,220.00 USD | 0.00 USD | `+49.66%` | `62,500,000,000.00` |
| `Live` | `Short` | `1064.50` | 21,150,000.00 USD | 1,600.00 USD | 0.00 USD | `+50.37%` | `1,500,000,000.00` |
| `Live` | `Short` | `1065.50` | 21,380,000.00 USD | 229,540.00 USD | 0.00 USD | `+50.51%` | `215,432,000,000.00` |
| `Live` | `Short` | `1067.50` | 21,400,000.00 USD | 15,380.00 USD | 0.00 USD | `+50.79%` | `14,403,000,000.00` |
| `Live` | `Short` | `1072.50` | 21,610,000.00 USD | 206,590.00 USD | 0.00 USD | `+51.50%` | `192,625,000,000.00` |
| `Live` | `Short` | `1073.50` | 21,610,000.00 USD | 1,610.00 USD | 0.00 USD | `+51.64%` | `1,500,000,000.00` |
| `Live` | `Short` | `1074.50` | 21,650,000.00 USD | 39,250.00 USD | 0.00 USD | `+51.78%` | `36,530,000,000.00` |
| `Live` | `Short` | `1081.50` | 21,660,000.00 USD | 9,430.00 USD | 0.00 USD | `+52.77%` | `8,722,000,000.00` |
| `Live` | `Short` | `1087.50` | 21,680,000.00 USD | 19,390.00 USD | 0.00 USD | `+53.62%` | `17,826,000,000.00` |
| `Live` | `Short` | `1088.50` | 21,680,000.00 USD | 1,930.00 USD | 0.00 USD | `+53.76%` | `1,776,000,000.00` |
| `Live` | `Short` | `1099.50` | 21,690,000.00 USD | 7,580.00 USD | 0.00 USD | `+55.31%` | `6,892,000,000.00` |
| `Live` | `Short` | `1102.50` | 21,690,000.00 USD | 4,630.00 USD | 0.00 USD | `+55.74%` | `4,204,000,000.00` |
| `Live` | `Short` | `1107.50` | 21,940,000.00 USD | 245,110.00 USD | 0.00 USD | `+56.44%` | `221,319,000,000.00` |
| `Live` | `Short` | `1112.50` | 22,100,000.00 USD | 164,380.00 USD | 0.00 USD | `+57.15%` | `147,759,000,000.00` |
| `Live` | `Short` | `1116.50` | 22,340,000.00 USD | 243,420.00 USD | 0.00 USD | `+57.72%` | `218,017,000,000.00` |
| `Live` | `Short` | `1124.50` | 22,390,000.00 USD | 48,660.00 USD | 0.00 USD | `+58.85%` | `43,270,000,000.00` |
| `Live` | `Short` | `1125.50` | 22,390,000.00 USD | 1,500.00 USD | 0.00 USD | `+58.99%` | `1,337,000,000.00` |
| `Live` | `Short` | `1126.50` | 22,450,000.00 USD | 60,900.00 USD | 0.00 USD | `+59.13%` | `54,065,000,000.00` |
| `Live` | `Short` | `1133.50` | 22,460,000.00 USD | 8,070.00 USD | 0.00 USD | `+60.12%` | `7,123,000,000.00` |
| `Live` | `Short` | `1136.50` | 22,470,000.00 USD | 11,370.00 USD | 0.00 USD | `+60.54%` | `10,000,000,000.00` |
| `Live` | `Short` | `1137.50` | 22,810,000.00 USD | 341,250.00 USD | 0.00 USD | `+60.68%` | `300,000,000,000.00` |
| `Live` | `Short` | `1138.50` | 22,820,000.00 USD | 547.62 USD | 0.00 USD | `+60.82%` | `481,000,000.00` |
| `Live` | `Short` | `1144.50` | 22,830,000.00 USD | 11,620.00 USD | 0.00 USD | `+61.67%` | `10,154,000,000.00` |
| `Live` | `Short` | `1145.50` | 22,830,000.00 USD | 595.66 USD | 0.00 USD | `+61.81%` | `520,000,000.00` |
| `Live` | `Short` | `1146.50` | 22,880,000.00 USD | 55,610.00 USD | 0.00 USD | `+61.95%` | `48,508,000,000.00` |
| `Live` | `Short` | `1149.50` | 22,880,000.00 USD | 211.51 USD | 0.00 USD | `+62.38%` | `184,000,000.00` |
| `Live` | `Short` | `1151.50` | 22,880,000.00 USD | 154.30 USD | 0.00 USD | `+62.66%` | `134,000,000.00` |
| `Live` | `Short` | `1154.50` | 22,930,000.00 USD | 46,180.00 USD | 0.00 USD | `+63.08%` | `40,000,000,000.00` |
| `Live` | `Short` | `1157.50` | 24,780,000.00 USD | 1,850,000.00 USD | 0.00 USD | `+63.51%` | `1,595,407,000,000.00` |
| `Live` | `Short` | `1159.50` | 24,780,000.00 USD | 364.08 USD | 0.00 USD | `+63.79%` | `314,000,000.00` |
| `Live` | `Short` | `1166.50` | 24,800,000.00 USD | 20,250.00 USD | 0.00 USD | `+64.78%` | `17,363,000,000.00` |
| `Live` | `Short` | `1168.50` | 24,800,000.00 USD | 121.52 USD | 0.00 USD | `+65.06%` | `104,000,000.00` |
| `Live` | `Short` | `1169.50` | 24,810,000.00 USD | 8,700.00 USD | 0.00 USD | `+65.20%` | `7,442,000,000.00` |
| `Live` | `Short` | `1175.50` | 24,810,000.00 USD | 115.20 USD | 0.00 USD | `+66.05%` | `98,000,000.00` |
| `Live` | `Short` | `1179.50` | 24,870,000.00 USD | 66,120.00 USD | 0.00 USD | `+66.61%` | `56,055,000,000.00` |
| `Live` | `Short` | `1182.50` | 24,870,000.00 USD | 158.46 USD | 0.00 USD | `+67.04%` | `134,000,000.00` |
| `Live` | `Short` | `1186.50` | 24,950,000.00 USD | 80,980.00 USD | 0.00 USD | `+67.60%` | `68,249,000,000.00` |
| `Live` | `Short` | `1193.50` | 24,970,000.00 USD | 20,350.00 USD | 0.00 USD | `+68.59%` | `17,052,000,000.00` |
| `Live` | `Short` | `1197.50` | 24,970,000.00 USD | 463.43 USD | 0.00 USD | `+69.16%` | `387,000,000.00` |
| `Live` | `Short` | `1207.50` | 24,970,000.00 USD | 385.19 USD | 0.00 USD | `+70.57%` | `319,000,000.00` |
| `Live` | `Short` | `1210.50` | 25,000,000.00 USD | 30,240.00 USD | 0.00 USD | `+70.99%` | `24,982,000,000.00` |
| `Live` | `Short` | `1211.50` | 25,110,000.00 USD | 109,030.00 USD | 0.00 USD | `+71.14%` | `90,000,000,000.00` |
| `Live` | `Short` | `1215.50` | 25,160,000.00 USD | 45,100.00 USD | 0.00 USD | `+71.70%` | `37,100,000,000.00` |
| `Live` | `Short` | `1224.50` | 25,210,000.00 USD | 53,940.00 USD | 0.00 USD | `+72.97%` | `44,051,000,000.00` |
| `Live` | `Short` | `1225.50` | 25,210,000.00 USD | 1,030.00 USD | 0.00 USD | `+73.11%` | `841,000,000.00` |
| `Live` | `Short` | `1231.50` | 25,240,000.00 USD | 23,910.00 USD | 0.00 USD | `+73.96%` | `19,414,000,000.00` |
| `Live` | `Short` | `1232.50` | 25,290,000.00 USD | 49,300.00 USD | 0.00 USD | `+74.10%` | `40,000,000,000.00` |
| `Live` | `Short` | `1243.50` | 25,290,000.00 USD | 644.13 USD | 0.00 USD | `+75.66%` | `518,000,000.00` |
| `Live` | `Short` | `1251.50` | 25,290,000.00 USD | 100.12 USD | 0.00 USD | `+76.79%` | `80,000,000.00` |
| `Live` | `Short` | `1263.50` | 25,290,000.00 USD | 202.16 USD | 0.00 USD | `+78.48%` | `160,000,000.00` |
| `Live` | `Short` | `1275.50` | 25,400,000.00 USD | 114,800.00 USD | 0.00 USD | `+80.18%` | `90,000,000,000.00` |
| `Live` | `Short` | `1276.50` | 25,410,000.00 USD | 3,570.00 USD | 0.00 USD | `+80.32%` | `2,797,000,000.00` |
| `Live` | `Short` | `1279.50` | 25,410,000.00 USD | 5,110.00 USD | 0.00 USD | `+80.74%` | `3,994,000,000.00` |
| `Live` | `Short` | `1290.50` | 26,770,000.00 USD | 1,360,000.00 USD | 0.00 USD | `+82.29%` | `1,055,150,000,000.00` |
| `Live` | `Short` | `1295.50` | 26,770,000.00 USD | 181.37 USD | 0.00 USD | `+83.00%` | `140,000,000.00` |
| `Live` | `Short` | `1298.50` | 26,780,000.00 USD | 2,770.00 USD | 0.00 USD | `+83.42%` | `2,134,000,000.00` |
| `Live` | `Short` | `1306.50` | 26,780,000.00 USD | 100.60 USD | 0.00 USD | `+84.55%` | `77,000,000.00` |
| `Live` | `Short` | `1308.50` | 26,940,000.00 USD | 166,020.00 USD | 0.00 USD | `+84.84%` | `126,881,000,000.00` |
| `Live` | `Short` | `1317.50` | 26,940,000.00 USD | 2,630.00 USD | 0.00 USD | `+86.11%` | `2,000,000,000.00` |
| `Live` | `Short` | `1320.50` | 26,960,000.00 USD | 14,140.00 USD | 0.00 USD | `+86.53%` | `10,710,000,000.00` |
| `Live` | `Short` | `1323.50` | 27,040,000.00 USD | 80,070.00 USD | 0.00 USD | `+86.96%` | `60,496,000,000.00` |
| `Live` | `Short` | `1324.50` | 27,040,000.00 USD | 229.14 USD | 0.00 USD | `+87.10%` | `173,000,000.00` |
| `Live` | `Short` | `1330.50` | 27,060,000.00 USD | 23,470.00 USD | 0.00 USD | `+87.94%` | `17,640,000,000.00` |
| `Live` | `Short` | `1332.50` | 27,750,000.00 USD | 688,080.00 USD | 0.00 USD | `+88.23%` | `516,379,000,000.00` |
| `Live` | `Short` | `1349.50` | 27,880,000.00 USD | 129,050.00 USD | 0.00 USD | `+90.63%` | `95,630,000,000.00` |
| `Live` | `Short` | `1353.50` | 27,880,000.00 USD | 4,680.00 USD | 0.00 USD | `+91.19%` | `3,457,000,000.00` |
| `Live` | `Short` | `1356.50` | 27,900,000.00 USD | 19,090.00 USD | 0.00 USD | `+91.62%` | `14,070,000,000.00` |
| `Live` | `Short` | `1358.50` | 27,910,000.00 USD | 3,870.00 USD | 0.00 USD | `+91.90%` | `2,846,000,000.00` |
| `Live` | `Short` | `1361.50` | 28,060,000.00 USD | 156,500.00 USD | 0.00 USD | `+92.32%` | `114,948,000,000.00` |
| `Live` | `Short` | `1370.50` | 28,110,000.00 USD | 46,910.00 USD | 0.00 USD | `+93.60%` | `34,232,000,000.00` |
| `Live` | `Short` | `1371.50` | 28,110,000.00 USD | 1,930.00 USD | 0.00 USD | `+93.74%` | `1,409,000,000.00` |
| `Live` | `Short` | `1375.50` | 28,130,000.00 USD | 20,630.00 USD | 0.00 USD | `+94.30%` | `15,000,000,000.00` |
| `Live` | `Short` | `1377.50` | 28,200,000.00 USD | 66,290.00 USD | 0.00 USD | `+94.58%` | `48,123,000,000.00` |
| `Live` | `Short` | `1401.50` | 28,450,000.00 USD | 252,270.00 USD | 0.00 USD | `+97.97%` | `180,000,000,000.00` |
| `Live` | `Short` | `1402.50` | 28,450,000.00 USD | 178.12 USD | 0.00 USD | `+98.12%` | `127,000,000.00` |
| `Live` | `Short` | `1405.50` | 28,460,000.00 USD | 6,420.00 USD | 0.00 USD | `+98.54%` | `4,570,000,000.00` |
| `Live` | `Short` | `1406.50` | 28,460,000.00 USD | 4,770.00 USD | 0.00 USD | `+98.68%` | `3,392,000,000.00` |
| `Live` | `Short` | `1413.50` | 28,460,000.00 USD | 139.94 USD | 0.00 USD | `+99.67%` | `99,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `150.50` | 2,790,000.00 USD | 0.00 USD | 475.73 USD | `-78.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `300.50` | 2,790,000.00 USD | 0.00 USD | 4,190.00 USD | `-57.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `333.50` | 2,780,000.00 USD | 0.00 USD | 333.50 USD | `-52.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `350.50` | 2,780,000.00 USD | 0.00 USD | 127.58 USD | `-50.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `369.50` | 2,780,000.00 USD | 0.00 USD | 5,170.00 USD | `-47.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `400.50` | 2,780,000.00 USD | 0.00 USD | 17,290.00 USD | `-43.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `410.50` | 2,760,000.00 USD | 0.00 USD | 25,210.00 USD | `-42.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `412.50` | 2,730,000.00 USD | 0.00 USD | 4,550.00 USD | `-41.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `455.50` | 2,730,000.00 USD | 0.00 USD | 698.74 USD | `-35.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `458.50` | 2,730,000.00 USD | 0.00 USD | 1,750.00 USD | `-35.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `469.50` | 2,730,000.00 USD | 0.00 USD | 3,550.00 USD | `-33.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `486.50` | 2,720,000.00 USD | 0.00 USD | 100.71 USD | `-31.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `487.50` | 2,720,000.00 USD | 0.00 USD | 6,600.00 USD | `-31.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `488.50` | 2,720,000.00 USD | 0.00 USD | 2,490.00 USD | `-31.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `498.50` | 2,710,000.00 USD | 0.00 USD | 163.01 USD | `-29.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `499.50` | 2,710,000.00 USD | 0.00 USD | 214.78 USD | `-29.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `500.50` | 2,710,000.00 USD | 0.00 USD | 70,160.00 USD | `-29.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `503.50` | 2,640,000.00 USD | 0.00 USD | 42,600.00 USD | `-28.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `506.50` | 2,600,000.00 USD | 0.00 USD | 138.78 USD | `-28.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `509.50` | 2,600,000.00 USD | 0.00 USD | 185.97 USD | `-28.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `515.50` | 2,600,000.00 USD | 0.00 USD | 1,030.00 USD | `-27.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `516.50` | 2,600,000.00 USD | 0.00 USD | 125.51 USD | `-27.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `517.50` | 2,600,000.00 USD | 0.00 USD | 280.49 USD | `-26.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `521.50` | 2,600,000.00 USD | 0.00 USD | 258.14 USD | `-26.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `524.50` | 2,600,000.00 USD | 0.00 USD | 8,170.00 USD | `-25.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `528.50` | 2,590,000.00 USD | 0.00 USD | 485.16 USD | `-25.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `534.50` | 2,590,000.00 USD | 0.00 USD | 4,650.00 USD | `-24.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `538.50` | 2,580,000.00 USD | 0.00 USD | 1,680.00 USD | `-23.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `540.50` | 2,580,000.00 USD | 0.00 USD | 2,490.00 USD | `-23.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `550.50` | 2,580,000.00 USD | 0.00 USD | 5,500.00 USD | `-22.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `554.50` | 2,580,000.00 USD | 0.00 USD | 1,190.00 USD | `-21.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `555.50` | 2,570,000.00 USD | 0.00 USD | 611.05 USD | `-21.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `557.50` | 2,570,000.00 USD | 0.00 USD | 213.52 USD | `-21.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `558.50` | 2,570,000.00 USD | 0.00 USD | 51,260.00 USD | `-21.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `560.50` | 2,520,000.00 USD | 0.00 USD | 292.02 USD | `-20.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `561.50` | 2,520,000.00 USD | 0.00 USD | 748.48 USD | `-20.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `566.50` | 2,520,000.00 USD | 0.00 USD | 566.50 USD | `-19.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `567.50` | 2,520,000.00 USD | 0.00 USD | 330.85 USD | `-19.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `568.50` | 2,520,000.00 USD | 0.00 USD | 5,680.00 USD | `-19.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `570.50` | 2,510,000.00 USD | 0.00 USD | 4,760.00 USD | `-19.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `571.50` | 2,510,000.00 USD | 0.00 USD | 1,700.00 USD | `-19.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `573.50` | 2,510,000.00 USD | 0.00 USD | 291.91 USD | `-18.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `575.50` | 2,510,000.00 USD | 0.00 USD | 469.61 USD | `-18.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `576.50` | 2,510,000.00 USD | 0.00 USD | 289.98 USD | `-18.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `577.50` | 2,510,000.00 USD | 0.00 USD | 285.86 USD | `-18.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `579.50` | 2,510,000.00 USD | 0.00 USD | 289.17 USD | `-18.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `580.50` | 2,510,000.00 USD | 0.00 USD | 6,750.00 USD | `-18.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `581.50` | 2,500,000.00 USD | 0.00 USD | 1,240.00 USD | `-17.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `583.50` | 2,500,000.00 USD | 0.00 USD | 287.67 USD | `-17.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `584.50` | 2,500,000.00 USD | 0.00 USD | 763.94 USD | `-17.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `585.50` | 2,500,000.00 USD | 0.00 USD | 883.52 USD | `-17.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `586.50` | 2,500,000.00 USD | 0.00 USD | 34,020.00 USD | `-17.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `587.50` | 2,460,000.00 USD | 0.00 USD | 289.05 USD | `-17.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `588.50` | 2,460,000.00 USD | 0.00 USD | 287.78 USD | `-16.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `589.50` | 2,460,000.00 USD | 0.00 USD | 7,990.00 USD | `-16.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `590.50` | 2,450,000.00 USD | 0.00 USD | 540.31 USD | `-16.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `591.50` | 2,450,000.00 USD | 0.00 USD | 282.74 USD | `-16.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `592.50` | 2,450,000.00 USD | 0.00 USD | 698.56 USD | `-16.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `594.50` | 2,450,000.00 USD | 0.00 USD | 286.55 USD | `-16.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `598.50` | 2,450,000.00 USD | 0.00 USD | 244.79 USD | `-15.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `600.50` | 2,450,000.00 USD | 0.00 USD | 42,810.00 USD | `-15.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `601.50` | 2,410,000.00 USD | 0.00 USD | 1,590.00 USD | `-15.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `605.50` | 2,410,000.00 USD | 0.00 USD | 2,610.00 USD | `-14.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `606.50` | 2,400,000.00 USD | 0.00 USD | 103.11 USD | `-14.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `608.50` | 2,400,000.00 USD | 0.00 USD | 42,950.00 USD | `-14.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `611.50` | 2,360,000.00 USD | 0.00 USD | 4,470.00 USD | `-13.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `612.50` | 2,360,000.00 USD | 0.00 USD | 1,380.00 USD | `-13.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `614.50` | 2,360,000.00 USD | 0.00 USD | 269.15 USD | `-13.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `615.50` | 2,360,000.00 USD | 0.00 USD | 1,740.00 USD | `-13.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `616.50` | 2,350,000.00 USD | 0.00 USD | 1,990.00 USD | `-12.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `620.50` | 2,350,000.00 USD | 0.00 USD | 2,560.00 USD | `-12.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `621.50` | 2,350,000.00 USD | 0.00 USD | 2,150.00 USD | `-12.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `625.50` | 2,350,000.00 USD | 0.00 USD | 170.76 USD | `-11.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `629.50` | 2,350,000.00 USD | 0.00 USD | 1,440.00 USD | `-11.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `630.50` | 2,350,000.00 USD | 0.00 USD | 276.16 USD | `-10.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `631.50` | 2,340,000.00 USD | 0.00 USD | 3,410.00 USD | `-10.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `632.50` | 2,340,000.00 USD | 0.00 USD | 204.30 USD | `-10.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `633.50` | 2,340,000.00 USD | 0.00 USD | 4,570.00 USD | `-10.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `634.50` | 2,340,000.00 USD | 0.00 USD | 2,550.00 USD | `-10.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `636.50` | 2,330,000.00 USD | 0.00 USD | 6,460.00 USD | `-10.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `638.50` | 2,330,000.00 USD | 0.00 USD | 560.60 USD | `-9.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `639.50` | 2,330,000.00 USD | 0.00 USD | 155.40 USD | `-9.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `640.50` | 2,330,000.00 USD | 0.00 USD | 429.78 USD | `-9.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `642.50` | 2,330,000.00 USD | 0.00 USD | 1,280.00 USD | `-9.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `643.50` | 2,330,000.00 USD | 0.00 USD | 1,830.00 USD | `-9.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `644.50` | 2,320,000.00 USD | 0.00 USD | 3,790.00 USD | `-8.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `645.50` | 2,320,000.00 USD | 0.00 USD | 154.27 USD | `-8.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `646.50` | 2,320,000.00 USD | 0.00 USD | 971.04 USD | `-8.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `648.50` | 2,320,000.00 USD | 0.00 USD | 1,800.00 USD | `-8.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `649.50` | 2,320,000.00 USD | 0.00 USD | 2,230.00 USD | `-8.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `650.50` | 2,310,000.00 USD | 0.00 USD | 18,910.00 USD | `-8.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `651.50` | 2,300,000.00 USD | 0.00 USD | 2,090.00 USD | `-7.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `653.50` | 2,290,000.00 USD | 0.00 USD | 2,020.00 USD | `-7.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `654.50` | 2,290,000.00 USD | 0.00 USD | 308.92 USD | `-7.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `655.50` | 2,290,000.00 USD | 0.00 USD | 13,180.00 USD | `-7.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `656.50` | 2,280,000.00 USD | 0.00 USD | 456.27 USD | `-7.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `657.50` | 2,280,000.00 USD | 0.00 USD | 110.46 USD | `-7.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `658.50` | 2,280,000.00 USD | 0.00 USD | 1,320.00 USD | `-6.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `659.50` | 2,280,000.00 USD | 0.00 USD | 3,130.00 USD | `-6.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `660.50` | 2,270,000.00 USD | 0.00 USD | 19,610.00 USD | `-6.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `661.50` | 2,250,000.00 USD | 0.00 USD | 11,210.00 USD | `-6.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `662.50` | 2,240,000.00 USD | 0.00 USD | 4,430.00 USD | `-6.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `663.50` | 2,240,000.00 USD | 0.00 USD | 2,840.00 USD | `-6.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `664.50` | 2,230,000.00 USD | 0.00 USD | 154.83 USD | `-6.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `665.50` | 2,230,000.00 USD | 0.00 USD | 113.14 USD | `-5.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `666.50` | 2,230,000.00 USD | 0.00 USD | 4,920.00 USD | `-5.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `668.50` | 2,230,000.00 USD | 0.00 USD | 2,160.00 USD | `-5.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `669.50` | 2,230,000.00 USD | 0.00 USD | 2,030.00 USD | `-5.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `670.50` | 2,230,000.00 USD | 0.00 USD | 148,590.00 USD | `-5.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `671.50` | 2,080,000.00 USD | 0.00 USD | 17,250.00 USD | `-5.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `672.50` | 2,060,000.00 USD | 0.00 USD | 517.15 USD | `-5.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `673.50` | 2,060,000.00 USD | 0.00 USD | 10,490.00 USD | `-4.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `674.50` | 2,050,000.00 USD | 0.00 USD | 825.59 USD | `-4.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `675.50` | 2,050,000.00 USD | 0.00 USD | 5,350.00 USD | `-4.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `676.50` | 2,040,000.00 USD | 0.00 USD | 55,120.00 USD | `-4.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `677.50` | 1,990,000.00 USD | 0.00 USD | 41,270.00 USD | `-4.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `678.50` | 1,950,000.00 USD | 0.00 USD | 3,360.00 USD | `-4.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `679.50` | 1,940,000.00 USD | 0.00 USD | 2,190.00 USD | `-4.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `680.50` | 1,940,000.00 USD | 0.00 USD | 49,720.00 USD | `-3.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `681.50` | 1,890,000.00 USD | 0.00 USD | 21,670.00 USD | `-3.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `682.50` | 1,870,000.00 USD | 0.00 USD | 476.39 USD | `-3.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `683.50` | 1,870,000.00 USD | 0.00 USD | 5,280.00 USD | `-3.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `684.50` | 1,860,000.00 USD | 0.00 USD | 457.25 USD | `-3.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `685.50` | 1,860,000.00 USD | 0.00 USD | 274,290.00 USD | `-3.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `686.50` | 1,590,000.00 USD | 0.00 USD | 138.67 USD | `-3.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `687.50` | 1,590,000.00 USD | 0.00 USD | 371.25 USD | `-2.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `688.50` | 1,590,000.00 USD | 0.00 USD | 1,150.00 USD | `-2.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `689.50` | 1,590,000.00 USD | 0.00 USD | 63,840.00 USD | `-2.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `690.50` | 1,520,000.00 USD | 0.00 USD | 1,290.00 USD | `-2.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `691.50` | 1,520,000.00 USD | 0.00 USD | 691.50 USD | `-2.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `692.50` | 1,520,000.00 USD | 0.00 USD | 2,300.00 USD | `-2.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `693.50` | 1,520,000.00 USD | 0.00 USD | 1,350.00 USD | `-2.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `694.50` | 1,520,000.00 USD | 0.00 USD | 27,940.00 USD | `-1.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `695.50` | 1,490,000.00 USD | 0.00 USD | 167,560.00 USD | `-1.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `696.50` | 1,320,000.00 USD | 0.00 USD | 1,470.00 USD | `-1.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `697.50` | 1,320,000.00 USD | 0.00 USD | 21,640.00 USD | `-1.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `698.50` | 1,300,000.00 USD | 0.00 USD | 14,190.00 USD | `-1.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `699.50` | 1,280,000.00 USD | 0.00 USD | 34,790.00 USD | `-1.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `700.50` | 1,250,000.00 USD | 0.00 USD | 2,610.00 USD | `-1.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `701.50` | 1,250,000.00 USD | 0.00 USD | 894,950.00 USD | `-0.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `702.50` | 352,390.00 USD | 0.00 USD | 6,960.00 USD | `-0.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `703.50` | 345,430.00 USD | 0.00 USD | 110,090.00 USD | `-0.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `704.50` | 235,340.00 USD | 0.00 USD | 86,910.00 USD | `-0.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `705.50` | 148,430.00 USD | 0.00 USD | 33,050.00 USD | `-0.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `706.50` | 115,390.00 USD | 0.00 USD | 41,240.00 USD | `-0.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `707.50` | 74,140.00 USD | 0.00 USD | 74,140.00 USD | `-0.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `708.50` | 582,020.00 USD | 582,020.00 USD | 0.00 USD | `+0.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `709.50` | 639,990.00 USD | 57,980.00 USD | 0.00 USD | `+0.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `710.50` | 641,400.00 USD | 1,400.00 USD | 0.00 USD | `+0.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `711.50` | 642,590.00 USD | 1,190.00 USD | 0.00 USD | `+0.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `712.50` | 649,870.00 USD | 7,280.00 USD | 0.00 USD | `+0.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `713.50` | 722,610.00 USD | 72,740.00 USD | 0.00 USD | `+0.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `714.50` | 749,040.00 USD | 26,430.00 USD | 0.00 USD | `+0.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `715.50` | 769,700.00 USD | 20,660.00 USD | 0.00 USD | `+1.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `716.50` | 931,050.00 USD | 161,350.00 USD | 0.00 USD | `+1.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `717.50` | 935,400.00 USD | 4,350.00 USD | 0.00 USD | `+1.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `718.50` | 938,680.00 USD | 3,290.00 USD | 0.00 USD | `+1.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `719.50` | 975,870.00 USD | 37,190.00 USD | 0.00 USD | `+1.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `720.50` | 978,000.00 USD | 2,130.00 USD | 0.00 USD | `+1.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `721.50` | 979,710.00 USD | 1,710.00 USD | 0.00 USD | `+1.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `722.50` | 982,310.00 USD | 2,600.00 USD | 0.00 USD | `+2.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `723.50` | 992,230.00 USD | 9,930.00 USD | 0.00 USD | `+2.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `724.50` | 992,840.00 USD | 606.41 USD | 0.00 USD | `+2.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `725.50` | 1,000,000.00 USD | 11,390.00 USD | 0.00 USD | `+2.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `726.50` | 1,000,000.00 USD | 470.77 USD | 0.00 USD | `+2.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `727.50` | 1,020,000.00 USD | 14,100.00 USD | 0.00 USD | `+2.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `728.50` | 1,060,000.00 USD | 38,690.00 USD | 0.00 USD | `+2.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `729.50` | 1,200,000.00 USD | 137,880.00 USD | 0.00 USD | `+3.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `730.50` | 1,620,000.00 USD | 425,260.00 USD | 0.00 USD | `+3.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `731.50` | 1,870,000.00 USD | 253,950.00 USD | 0.00 USD | `+3.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `732.50` | 1,870,000.00 USD | 209.49 USD | 0.00 USD | `+3.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `733.50` | 1,880,000.00 USD | 1,230.00 USD | 0.00 USD | `+3.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `734.50` | 1,910,000.00 USD | 29,420.00 USD | 0.00 USD | `+3.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `735.50` | 1,910,000.00 USD | 3,150.00 USD | 0.00 USD | `+3.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `736.50` | 1,920,000.00 USD | 13,700.00 USD | 0.00 USD | `+4.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `737.50` | 1,920,000.00 USD | 685.88 USD | 0.00 USD | `+4.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `738.50` | 1,940,000.00 USD | 13,910.00 USD | 0.00 USD | `+4.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `739.50` | 1,940,000.00 USD | 790.53 USD | 0.00 USD | `+4.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `740.50` | 2,060,000.00 USD | 120,770.00 USD | 0.00 USD | `+4.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `741.50` | 2,060,000.00 USD | 1,590.00 USD | 0.00 USD | `+4.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `742.50` | 2,310,000.00 USD | 247,900.00 USD | 0.00 USD | `+4.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `743.50` | 2,400,000.00 USD | 87,580.00 USD | 0.00 USD | `+5.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `744.50` | 2,560,000.00 USD | 163,440.00 USD | 0.00 USD | `+5.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `745.50` | 2,580,000.00 USD | 18,640.00 USD | 0.00 USD | `+5.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `746.50` | 2,580,000.00 USD | 672.60 USD | 0.00 USD | `+5.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `747.50` | 2,580,000.00 USD | 1,070.00 USD | 0.00 USD | `+5.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `748.50` | 2,880,000.00 USD | 299,400.00 USD | 0.00 USD | `+5.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `749.50` | 2,880,000.00 USD | 3,530.00 USD | 0.00 USD | `+5.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `750.50` | 2,890,000.00 USD | 4,230.00 USD | 0.00 USD | `+6.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `751.50` | 2,890,000.00 USD | 4,830.00 USD | 0.00 USD | `+6.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `752.50` | 2,890,000.00 USD | 2,730.00 USD | 0.00 USD | `+6.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `753.50` | 2,890,000.00 USD | 327.77 USD | 0.00 USD | `+6.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `754.50` | 2,940,000.00 USD | 47,160.00 USD | 0.00 USD | `+6.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `755.50` | 2,950,000.00 USD | 7,550.00 USD | 0.00 USD | `+6.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `756.50` | 2,960,000.00 USD | 9,810.00 USD | 0.00 USD | `+6.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `757.50` | 3,100,000.00 USD | 142,940.00 USD | 0.00 USD | `+7.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `758.50` | 3,100,000.00 USD | 136.53 USD | 0.00 USD | `+7.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `759.50` | 3,120,000.00 USD | 21,350.00 USD | 0.00 USD | `+7.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `760.50` | 3,150,000.00 USD | 29,560.00 USD | 0.00 USD | `+7.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `761.50` | 3,160,000.00 USD | 9,640.00 USD | 0.00 USD | `+7.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `762.50` | 3,160,000.00 USD | 274.50 USD | 0.00 USD | `+7.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `763.50` | 3,350,000.00 USD | 190,180.00 USD | 0.00 USD | `+7.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `764.50` | 3,360,000.00 USD | 3,190.00 USD | 0.00 USD | `+7.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `765.50` | 3,390,000.00 USD | 38,580.00 USD | 0.00 USD | `+8.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `766.50` | 3,400,000.00 USD | 600.94 USD | 0.00 USD | `+8.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `767.50` | 3,860,000.00 USD | 468,180.00 USD | 0.00 USD | `+8.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `768.50` | 3,860,000.00 USD | 1,230.00 USD | 0.00 USD | `+8.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `769.50` | 3,860,000.00 USD | 171.60 USD | 0.00 USD | `+8.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `770.50` | 3,870,000.00 USD | 1,540.00 USD | 0.00 USD | `+8.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `771.50` | 3,870,000.00 USD | 1,370.00 USD | 0.00 USD | `+8.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `772.50` | 3,870,000.00 USD | 242.56 USD | 0.00 USD | `+9.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `773.50` | 3,870,000.00 USD | 1,240.00 USD | 0.00 USD | `+9.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `774.50` | 3,880,000.00 USD | 9,680.00 USD | 0.00 USD | `+9.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `775.50` | 3,880,000.00 USD | 853.05 USD | 0.00 USD | `+9.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `776.50` | 3,890,000.00 USD | 14,230.00 USD | 0.00 USD | `+9.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `777.50` | 3,910,000.00 USD | 15,690.00 USD | 0.00 USD | `+9.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `778.50` | 3,910,000.00 USD | 3,820.00 USD | 0.00 USD | `+9.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `779.50` | 3,920,000.00 USD | 6,420.00 USD | 0.00 USD | `+10.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `780.50` | 3,950,000.00 USD | 25,520.00 USD | 0.00 USD | `+10.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `781.50` | 3,950,000.00 USD | 2,570.00 USD | 0.00 USD | `+10.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `782.50` | 3,950,000.00 USD | 1,900.00 USD | 0.00 USD | `+10.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `783.50` | 4,360,000.00 USD | 407,870.00 USD | 0.00 USD | `+10.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `784.50` | 4,360,000.00 USD | 106.69 USD | 0.00 USD | `+10.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `785.50` | 4,360,000.00 USD | 559.28 USD | 0.00 USD | `+10.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `786.50` | 4,360,000.00 USD | 366.51 USD | 0.00 USD | `+11.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `787.50` | 4,360,000.00 USD | 2,370.00 USD | 0.00 USD | `+11.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `788.50` | 4,360,000.00 USD | 133.26 USD | 0.00 USD | `+11.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `790.50` | 4,370,000.00 USD | 4,190.00 USD | 0.00 USD | `+11.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `791.50` | 4,370,000.00 USD | 704.44 USD | 0.00 USD | `+11.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `792.50` | 4,370,000.00 USD | 4,360.00 USD | 0.00 USD | `+11.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `793.50` | 4,370,000.00 USD | 1,450.00 USD | 0.00 USD | `+12.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `794.50` | 4,380,000.00 USD | 3,630.00 USD | 0.00 USD | `+12.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `795.50` | 4,380,000.00 USD | 3,040.00 USD | 0.00 USD | `+12.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `796.50` | 4,380,000.00 USD | 154.52 USD | 0.00 USD | `+12.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `799.50` | 4,380,000.00 USD | 1,450.00 USD | 0.00 USD | `+12.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `800.50` | 4,390,000.00 USD | 11,460.00 USD | 0.00 USD | `+13.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `803.50` | 4,390,000.00 USD | 803.50 USD | 0.00 USD | `+13.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `805.50` | 4,390,000.00 USD | 120.02 USD | 0.00 USD | `+13.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `806.50` | 4,390,000.00 USD | 1,300.00 USD | 0.00 USD | `+13.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `808.50` | 4,400,000.00 USD | 3,190.00 USD | 0.00 USD | `+14.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `809.50` | 4,400,000.00 USD | 242.04 USD | 0.00 USD | `+14.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `810.50` | 4,410,000.00 USD | 15,790.00 USD | 0.00 USD | `+14.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `811.50` | 4,410,000.00 USD | 374.10 USD | 0.00 USD | `+14.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `812.50` | 4,410,000.00 USD | 844.19 USD | 0.00 USD | `+14.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `813.50` | 4,410,000.00 USD | 109.82 USD | 0.00 USD | `+14.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `814.50` | 4,420,000.00 USD | 3,210.00 USD | 0.00 USD | `+15.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `816.50` | 4,420,000.00 USD | 984.70 USD | 0.00 USD | `+15.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `817.50` | 4,420,000.00 USD | 162.68 USD | 0.00 USD | `+15.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `818.50` | 4,420,000.00 USD | 5,990.00 USD | 0.00 USD | `+15.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `820.50` | 4,430,000.00 USD | 8,230.00 USD | 0.00 USD | `+15.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `824.50` | 4,430,000.00 USD | 408.13 USD | 0.00 USD | `+16.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `825.50` | 4,760,000.00 USD | 330,200.00 USD | 0.00 USD | `+16.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `826.50` | 4,760,000.00 USD | 672.77 USD | 0.00 USD | `+16.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `827.50` | 4,760,000.00 USD | 276.38 USD | 0.00 USD | `+16.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `828.50` | 4,770,000.00 USD | 1,800.00 USD | 0.00 USD | `+17.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `830.50` | 4,800,000.00 USD | 35,850.00 USD | 0.00 USD | `+17.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `833.50` | 4,800,000.00 USD | 1,200.00 USD | 0.00 USD | `+17.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `835.50` | 4,800,000.00 USD | 187.15 USD | 0.00 USD | `+18.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `836.50` | 4,800,000.00 USD | 372.24 USD | 0.00 USD | `+18.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `837.50` | 4,800,000.00 USD | 326.62 USD | 0.00 USD | `+18.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `839.50` | 4,800,000.00 USD | 296.34 USD | 0.00 USD | `+18.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `840.50` | 4,810,000.00 USD | 441.26 USD | 0.00 USD | `+18.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `841.50` | 4,810,000.00 USD | 329.87 USD | 0.00 USD | `+18.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `843.50` | 4,810,000.00 USD | 425.97 USD | 0.00 USD | `+19.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `844.50` | 4,810,000.00 USD | 1,770.00 USD | 0.00 USD | `+19.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `850.50` | 4,810,000.00 USD | 2,550.00 USD | 0.00 USD | `+20.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `851.50` | 4,820,000.00 USD | 11,650.00 USD | 0.00 USD | `+20.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `852.50` | 4,820,000.00 USD | 102.30 USD | 0.00 USD | `+20.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `854.50` | 4,820,000.00 USD | 137.57 USD | 0.00 USD | `+20.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `857.50` | 4,820,000.00 USD | 1,200.00 USD | 0.00 USD | `+21.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `860.50` | 4,820,000.00 USD | 1,160.00 USD | 0.00 USD | `+21.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `862.50` | 4,830,000.00 USD | 1,200.00 USD | 0.00 USD | `+21.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `863.50` | 4,830,000.00 USD | 874.73 USD | 0.00 USD | `+21.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `864.50` | 4,830,000.00 USD | 2,970.00 USD | 0.00 USD | `+22.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `865.50` | 4,830,000.00 USD | 3,460.00 USD | 0.00 USD | `+22.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `868.50` | 4,840,000.00 USD | 2,610.00 USD | 0.00 USD | `+22.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `870.50` | 4,840,000.00 USD | 228.07 USD | 0.00 USD | `+22.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `872.50` | 4,840,000.00 USD | 1,110.00 USD | 0.00 USD | `+23.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `874.50` | 4,840,000.00 USD | 582.42 USD | 0.00 USD | `+23.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `884.50` | 4,890,000.00 USD | 54,820.00 USD | 0.00 USD | `+24.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `888.50` | 4,890,000.00 USD | 266.55 USD | 0.00 USD | `+25.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `890.50` | 4,890,000.00 USD | 690.14 USD | 0.00 USD | `+25.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `891.50` | 4,890,000.00 USD | 605.33 USD | 0.00 USD | `+25.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `900.50` | 4,950,000.00 USD | 53,820.00 USD | 0.00 USD | `+27.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `907.50` | 4,950,000.00 USD | 1,640.00 USD | 0.00 USD | `+28.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `914.50` | 4,950,000.00 USD | 4,150.00 USD | 0.00 USD | `+29.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `917.50` | 4,950,000.00 USD | 533.99 USD | 0.00 USD | `+29.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `919.50` | 4,950,000.00 USD | 166.43 USD | 0.00 USD | `+29.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `920.50` | 4,950,000.00 USD | 463.01 USD | 0.00 USD | `+30.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `926.50` | 4,960,000.00 USD | 320.57 USD | 0.00 USD | `+30.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `929.50` | 4,980,000.00 USD | 24,800.00 USD | 0.00 USD | `+31.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `930.50` | 4,980,000.00 USD | 552.72 USD | 0.00 USD | `+31.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `933.50` | 4,980,000.00 USD | 196.03 USD | 0.00 USD | `+31.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `935.50` | 4,980,000.00 USD | 287.20 USD | 0.00 USD | `+32.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `958.50` | 4,980,000.00 USD | 782.14 USD | 0.00 USD | `+35.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `959.50` | 4,980,000.00 USD | 498.94 USD | 0.00 USD | `+35.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `965.50` | 4,980,000.00 USD | 1,930.00 USD | 0.00 USD | `+36.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `977.50` | 4,980,000.00 USD | 293.25 USD | 0.00 USD | `+38.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `980.50` | 4,990,000.00 USD | 1,300.00 USD | 0.00 USD | `+38.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `981.50` | 4,990,000.00 USD | 109.93 USD | 0.00 USD | `+38.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `984.50` | 4,990,000.00 USD | 439.09 USD | 0.00 USD | `+39.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `987.50` | 4,990,000.00 USD | 2,590.00 USD | 0.00 USD | `+39.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `997.50` | 4,990,000.00 USD | 1,800.00 USD | 0.00 USD | `+40.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `998.50` | 4,990,000.00 USD | 3,990.00 USD | 0.00 USD | `+41.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `999.50` | 5,000,000.00 USD | 938.53 USD | 0.00 USD | `+41.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1000.50` | 5,010,000.00 USD | 11,810.00 USD | 0.00 USD | `+41.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1017.50` | 5,010,000.00 USD | 203.50 USD | 0.00 USD | `+43.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1045.50` | 5,010,000.00 USD | 195.51 USD | 0.00 USD | `+47.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1100.50` | 5,010,000.00 USD | 278.43 USD | 0.00 USD | `+55.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1111.50` | 5,010,000.00 USD | 555.75 USD | 0.00 USD | `+57.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1146.50` | 5,010,000.00 USD | 167.39 USD | 0.00 USD | `+61.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1200.50` | 5,070,000.00 USD | 62,330.00 USD | 0.00 USD | `+69.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1202.50` | 5,070,000.00 USD | 1,250.00 USD | 0.00 USD | `+69.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1226.50` | 5,070,000.00 USD | 235.49 USD | 0.00 USD | `+73.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1230.50` | 5,080,000.00 USD | 3,580.00 USD | 0.00 USD | `+73.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1250.50` | 5,080,000.00 USD | 421.42 USD | 0.00 USD | `+76.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1280.50` | 5,080,000.00 USD | 3,750.00 USD | 0.00 USD | `+80.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1297.50` | 5,080,000.00 USD | 133.64 USD | 0.00 USD | `+83.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1300.50` | 5,080,000.00 USD | 685.36 USD | 0.00 USD | `+83.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1330.50` | 5,140,000.00 USD | 58,230.00 USD | 0.00 USD | `+87.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1340.50` | 5,220,000.00 USD | 80,850.00 USD | 0.00 USD | `+89.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1360.50` | 5,230,000.00 USD | 6,210.00 USD | 0.00 USD | `+92.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1363.50` | 5,230,000.00 USD | 349.06 USD | 0.00 USD | `+92.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1370.50` | 5,230,000.00 USD | 1,060.00 USD | 0.00 USD | `+93.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1372.50` | 5,250,000.00 USD | 19,210.00 USD | 0.00 USD | `+93.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1389.50` | 5,250,000.00 USD | 425.19 USD | 0.00 USD | `+96.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1400.50` | 5,250,000.00 USD | 3,850.00 USD | 0.00 USD | `+97.83%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `606.10` | 37,790,000.00 USD | 0.00 USD | 37,790,000.00 USD | 42,510.00 USD | 3,960.00 USD | 13,520.00 USD |
| `1D` | `607.20` | 37,730,000.00 USD | 0.00 USD | 37,730,000.00 USD | 49,710.00 USD | 7,560.00 USD | 5,590.00 USD |
| `1D` | `608.30` | 37,670,000.00 USD | 0.00 USD | 37,670,000.00 USD | 11,850.00 USD | 4,880.00 USD | 3,430.00 USD |
| `1D` | `609.40` | 37,650,000.00 USD | 0.00 USD | 37,650,000.00 USD | 11,590.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `616.00` | 37,640,000.00 USD | 0.00 USD | 37,640,000.00 USD | 0.00 USD | 0.00 USD | 295,360.00 USD |
| `1D` | `617.10` | 37,340,000.00 USD | 0.00 USD | 37,340,000.00 USD | 290,320.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `619.30` | 37,050,000.00 USD | 0.00 USD | 37,050,000.00 USD | 0.00 USD | 33,270.00 USD | 0.00 USD |
| `1D` | `620.40` | 37,020,000.00 USD | 0.00 USD | 37,020,000.00 USD | 175,630.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `621.50` | 36,840,000.00 USD | 0.00 USD | 36,840,000.00 USD | 0.00 USD | 35,090.00 USD | 0.00 USD |
| `1D` | `623.70` | 36,810,000.00 USD | 0.00 USD | 36,810,000.00 USD | 460,160.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `624.80` | 36,350,000.00 USD | 0.00 USD | 36,350,000.00 USD | 238,630.00 USD | 31,450.00 USD | 274,040.00 USD |
| `1D` | `625.90` | 35,810,000.00 USD | 0.00 USD | 35,810,000.00 USD | 224,870.00 USD | 44,960.00 USD | 0.00 USD |
| `1D` | `627.00` | 35,540,000.00 USD | 0.00 USD | 35,540,000.00 USD | 186,500.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `631.40` | 35,350,000.00 USD | 0.00 USD | 35,350,000.00 USD | 0.00 USD | 10,840.00 USD | 812,350.00 USD |
| `1D` | `632.50` | 34,530,000.00 USD | 0.00 USD | 34,530,000.00 USD | 473,380.00 USD | 42,940.00 USD | 0.00 USD |
| `1D` | `633.60` | 34,010,000.00 USD | 0.00 USD | 34,010,000.00 USD | 7,730.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `634.70` | 34,000,000.00 USD | 0.00 USD | 34,000,000.00 USD | 11,290.00 USD | 23,580.00 USD | 0.00 USD |
| `1D` | `636.90` | 33,970,000.00 USD | 0.00 USD | 33,970,000.00 USD | 101,910.00 USD | 40,910.00 USD | 236,370.00 USD |
| `1D` | `639.10` | 33,590,000.00 USD | 0.00 USD | 33,590,000.00 USD | 184,100.00 USD | 37,610.00 USD | 0.00 USD |
| `1D` | `640.20` | 33,370,000.00 USD | 0.00 USD | 33,370,000.00 USD | 0.00 USD | 0.00 USD | 184,710.00 USD |
| `1D` | `642.40` | 33,180,000.00 USD | 0.00 USD | 33,180,000.00 USD | 150,090.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `644.60` | 33,030,000.00 USD | 0.00 USD | 33,030,000.00 USD | 308,550.00 USD | 0.00 USD | 341,610.00 USD |
| `1D` | `646.80` | 32,380,000.00 USD | 0.00 USD | 32,380,000.00 USD | 217,880.00 USD | 0.00 USD | 140,640.00 USD |
| `1D` | `647.90` | 32,020,000.00 USD | 0.00 USD | 32,020,000.00 USD | 106,400.00 USD | 29,080.00 USD | 0.00 USD |
| `1D` | `649.00` | 31,890,000.00 USD | 0.00 USD | 31,890,000.00 USD | 92,180.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `651.20` | 31,790,000.00 USD | 0.00 USD | 31,790,000.00 USD | 106,810.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `652.30` | 31,690,000.00 USD | 0.00 USD | 31,690,000.00 USD | 0.00 USD | 0.00 USD | 94,590.00 USD |
| `1D` | `653.40` | 31,590,000.00 USD | 0.00 USD | 31,590,000.00 USD | 0.00 USD | 26,830.00 USD | 0.00 USD |
| `1D` | `654.50` | 31,570,000.00 USD | 0.00 USD | 31,570,000.00 USD | 56,940.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `655.60` | 31,510,000.00 USD | 0.00 USD | 31,510,000.00 USD | 138,350.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `656.70` | 31,370,000.00 USD | 0.00 USD | 31,370,000.00 USD | 22,490.00 USD | 21,320.00 USD | 825,700.00 USD |
| `1D` | `657.80` | 30,500,000.00 USD | 0.00 USD | 30,500,000.00 USD | 833,200.00 USD | 14,920.00 USD | 0.00 USD |
| `1D` | `658.90` | 29,650,000.00 USD | 0.00 USD | 29,650,000.00 USD | 64,090.00 USD | 0.00 USD | 81,440.00 USD |
| `1D` | `660.00` | 29,510,000.00 USD | 0.00 USD | 29,510,000.00 USD | 90,670.00 USD | 7,460.00 USD | 14,670.00 USD |
| `1D` | `661.10` | 29,400,000.00 USD | 0.00 USD | 29,400,000.00 USD | 0.00 USD | 83,170.00 USD | 0.00 USD |
| `1D` | `662.20` | 29,310,000.00 USD | 0.00 USD | 29,310,000.00 USD | 445,210.00 USD | 87,740.00 USD | 0.00 USD |
| `1D` | `663.30` | 28,780,000.00 USD | 0.00 USD | 28,780,000.00 USD | 202,560.00 USD | 5,000.00 USD | 19,650.00 USD |
| `7D` | `664.10` | 87,050,000.00 USD | 0.00 USD | 87,050,000.00 USD | 78,740.00 USD | 18,740.00 USD | 39,340.00 USD |
| `1D` | `664.40` | 28,550,000.00 USD | 0.00 USD | 28,550,000.00 USD | 1,200,000.00 USD | 48,410.00 USD | 21,160.00 USD |
| `7D` | `665.00` | 86,910,000.00 USD | 0.00 USD | 86,910,000.00 USD | 92,030.00 USD | 22,990.00 USD | 37,000.00 USD |
| `1D` | `665.50` | 27,290,000.00 USD | 0.00 USD | 27,290,000.00 USD | 671,470.00 USD | 4,540.00 USD | 11,460.00 USD |
| `7D` | `665.90` | 86,760,000.00 USD | 0.00 USD | 86,760,000.00 USD | 264,020.00 USD | 71,380.00 USD | 63,410.00 USD |
| `1D` | `666.60` | 26,600,000.00 USD | 0.00 USD | 26,600,000.00 USD | 686,090.00 USD | 102,050.00 USD | 696,480.00 USD |
| `7D` | `666.80` | 86,360,000.00 USD | 0.00 USD | 86,360,000.00 USD | 198,550.00 USD | 33,320.00 USD | 61,710.00 USD |
| `1D` | `667.70` | 25,110,000.00 USD | 0.00 USD | 25,110,000.00 USD | 205,320.00 USD | 115,700.00 USD | 9,290.00 USD |
| `7D` | `667.70` | 86,070,000.00 USD | 0.00 USD | 86,070,000.00 USD | 199,690.00 USD | 45,130.00 USD | 51,340.00 USD |
| `7D` | `668.60` | 85,770,000.00 USD | 0.00 USD | 85,770,000.00 USD | 387,530.00 USD | 92,860.00 USD | 51,060.00 USD |
| `1D` | `668.80` | 24,780,000.00 USD | 0.00 USD | 24,780,000.00 USD | 562,170.00 USD | 25,520.00 USD | 3,620.00 USD |
| `7D` | `669.50` | 85,240,000.00 USD | 0.00 USD | 85,240,000.00 USD | 341,150.00 USD | 38,130.00 USD | 108,970.00 USD |
| `1D` | `669.90` | 24,190,000.00 USD | 0.00 USD | 24,190,000.00 USD | 253,070.00 USD | 61,020.00 USD | 1,490,000.00 USD |
| `7D` | `670.40` | 84,750,000.00 USD | 0.00 USD | 84,750,000.00 USD | 319,660.00 USD | 93,800.00 USD | 77,380.00 USD |
| `1D` | `671.00` | 22,390,000.00 USD | 0.00 USD | 22,390,000.00 USD | 143,770.00 USD | 8,380.00 USD | 10,400.00 USD |
| `7D` | `671.30` | 84,260,000.00 USD | 0.00 USD | 84,260,000.00 USD | 335,750.00 USD | 57,500.00 USD | 42,050.00 USD |
| `1D` | `672.10` | 22,230,000.00 USD | 0.00 USD | 22,230,000.00 USD | 2,020,000.00 USD | 11,460.00 USD | 35,800.00 USD |
| `7D` | `672.20` | 83,830,000.00 USD | 0.00 USD | 83,830,000.00 USD | 180,230.00 USD | 62,620.00 USD | 74,250.00 USD |
| `7D` | `673.10` | 83,510,000.00 USD | 0.00 USD | 83,510,000.00 USD | 394,120.00 USD | 64,970.00 USD | 42,710.00 USD |
| `1D` | `673.20` | 20,160,000.00 USD | 0.00 USD | 20,160,000.00 USD | 348,680.00 USD | 73,200.00 USD | 2,140,000.00 USD |
| `7D` | `674.00` | 83,010,000.00 USD | 0.00 USD | 83,010,000.00 USD | 335,670.00 USD | 105,910.00 USD | 80,360.00 USD |
| `1D` | `674.30` | 17,610,000.00 USD | 0.00 USD | 17,610,000.00 USD | 225,430.00 USD | 306,330.00 USD | 111,710.00 USD |
| `7D` | `674.90` | 82,490,000.00 USD | 0.00 USD | 82,490,000.00 USD | 247,070.00 USD | 31,490.00 USD | 44,420.00 USD |
| `1D` | `675.40` | 16,960,000.00 USD | 0.00 USD | 16,960,000.00 USD | 2,030,000.00 USD | 46,170.00 USD | 249,580.00 USD |
| `7D` | `675.80` | 82,160,000.00 USD | 0.00 USD | 82,160,000.00 USD | 387,400.00 USD | 26,020.00 USD | 79,190.00 USD |
| `1D` | `676.50` | 14,640,000.00 USD | 0.00 USD | 14,640,000.00 USD | 385,420.00 USD | 289,950.00 USD | 74,130.00 USD |
| `7D` | `676.70` | 81,670,000.00 USD | 0.00 USD | 81,670,000.00 USD | 509,100.00 USD | 35,490.00 USD | 126,570.00 USD |
| `1D` | `677.60` | 13,890,000.00 USD | 0.00 USD | 13,890,000.00 USD | 374,010.00 USD | 118,540.00 USD | 0.00 USD |
| `7D` | `677.60` | 81,000,000.00 USD | 0.00 USD | 81,000,000.00 USD | 409,810.00 USD | 0.00 USD | 63,990.00 USD |
| `7D` | `678.50` | 80,530,000.00 USD | 0.00 USD | 80,530,000.00 USD | 120,190.00 USD | 0.00 USD | 26,990.00 USD |
| `1D` | `678.70` | 13,400,000.00 USD | 0.00 USD | 13,400,000.00 USD | 1,030,000.00 USD | 111,460.00 USD | 0.00 USD |
| `7D` | `679.40` | 80,380,000.00 USD | 0.00 USD | 80,380,000.00 USD | 116,510.00 USD | 10,480.00 USD | 40,610.00 USD |
| `1D` | `679.80` | 12,260,000.00 USD | 0.00 USD | 12,260,000.00 USD | 1,200,000.00 USD | 167,040.00 USD | 0.00 USD |
| `7D` | `680.30` | 80,210,000.00 USD | 0.00 USD | 80,210,000.00 USD | 166,780.00 USD | 13,510.00 USD | 0.00 USD |
| `1D` | `680.90` | 10,900,000.00 USD | 0.00 USD | 10,900,000.00 USD | 13,920.00 USD | 99,800.00 USD | 0.00 USD |
| `7D` | `681.20` | 80,030,000.00 USD | 0.00 USD | 80,030,000.00 USD | 106,280.00 USD | 7,050.00 USD | 35,170.00 USD |
| `1D` | `682.00` | 10,780,000.00 USD | 0.00 USD | 10,780,000.00 USD | 34,310.00 USD | 305,760.00 USD | 0.00 USD |
| `7D` | `682.10` | 79,880,000.00 USD | 0.00 USD | 79,880,000.00 USD | 0.00 USD | 23,360.00 USD | 27,620.00 USD |
| `7D` | `683.00` | 79,830,000.00 USD | 0.00 USD | 79,830,000.00 USD | 175,930.00 USD | 28,470.00 USD | 11,520.00 USD |
| `1D` | `683.10` | 10,440,000.00 USD | 0.00 USD | 10,440,000.00 USD | 120,530.00 USD | 128,350.00 USD | 0.00 USD |
| `7D` | `683.90` | 79,620,000.00 USD | 0.00 USD | 79,620,000.00 USD | 77,000.00 USD | 29,510.00 USD | 17,480.00 USD |
| `1D` | `684.20` | 10,190,000.00 USD | 0.00 USD | 10,190,000.00 USD | 19,970.00 USD | 41,000.00 USD | 0.00 USD |
| `7D` | `684.80` | 79,490,000.00 USD | 0.00 USD | 79,490,000.00 USD | 246,080.00 USD | 9,850.00 USD | 39,550.00 USD |
| `7D` | `685.70` | 79,200,000.00 USD | 0.00 USD | 79,200,000.00 USD | 197,040.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `686.40` | 10,130,000.00 USD | 0.00 USD | 10,130,000.00 USD | 694,060.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `686.60` | 79,000,000.00 USD | 0.00 USD | 79,000,000.00 USD | 62,990.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `687.50` | 9,440,000.00 USD | 0.00 USD | 9,440,000.00 USD | 775,320.00 USD | 54,180.00 USD | 3,790,000.00 USD |
| `7D` | `687.50` | 78,940,000.00 USD | 0.00 USD | 78,940,000.00 USD | 148,480.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `688.40` | 78,790,000.00 USD | 0.00 USD | 78,790,000.00 USD | 67,880.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `688.60` | 4,820,000.00 USD | 0.00 USD | 4,820,000.00 USD | 1,910,000.00 USD | 0.00 USD | 146,450.00 USD |
| `7D` | `689.30` | 78,720,000.00 USD | 0.00 USD | 78,720,000.00 USD | 84,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `689.70` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 50,420.00 USD | 38,440.00 USD | 466,010.00 USD |
| `7D` | `690.20` | 78,640,000.00 USD | 0.00 USD | 78,640,000.00 USD | 283,920.00 USD | 63,230.00 USD | 82,450.00 USD |
| `1D` | `690.80` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 361,400.00 USD | 146,030.00 USD | 0.00 USD |
| `7D` | `691.10` | 78,210,000.00 USD | 0.00 USD | 78,210,000.00 USD | 362,020.00 USD | 61,370.00 USD | 81,090.00 USD |
| `1D` | `691.90` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 27,340.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `692.00` | 77,700,000.00 USD | 0.00 USD | 77,700,000.00 USD | 322,430.00 USD | 18,850.00 USD | 58,910.00 USD |
| `7D` | `692.90` | 77,300,000.00 USD | 0.00 USD | 77,300,000.00 USD | 280,830.00 USD | 19,470.00 USD | 0.00 USD |
| `7D` | `693.80` | 77,000,000.00 USD | 0.00 USD | 77,000,000.00 USD | 305,720.00 USD | 39,210.00 USD | 0.00 USD |
| `7D` | `694.70` | 76,660,000.00 USD | 0.00 USD | 76,660,000.00 USD | 279,840.00 USD | 36,640.00 USD | 35,490.00 USD |
| `7D` | `695.60` | 76,300,000.00 USD | 0.00 USD | 76,300,000.00 USD | 120,440.00 USD | 0.00 USD | 21,670.00 USD |
| `1D` | `696.30` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 0.00 USD | 137,440.00 USD | 0.00 USD |
| `7D` | `696.50` | 76,160,000.00 USD | 0.00 USD | 76,160,000.00 USD | 140,370.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `697.40` | 76,020,000.00 USD | 0.00 USD | 76,020,000.00 USD | 189,100.00 USD | 19,230.00 USD | 0.00 USD |
| `7D` | `698.30` | 75,810,000.00 USD | 0.00 USD | 75,810,000.00 USD | 273,520.00 USD | 33,120.00 USD | 54,800.00 USD |
| `7D` | `699.20` | 75,450,000.00 USD | 0.00 USD | 75,450,000.00 USD | 274,810.00 USD | 12,670.00 USD | 11,820.00 USD |
| `7D` | `700.10` | 75,150,000.00 USD | 0.00 USD | 75,150,000.00 USD | 225,450.00 USD | 40,820.00 USD | 27,440.00 USD |
| `7D` | `701.00` | 74,860,000.00 USD | 0.00 USD | 74,860,000.00 USD | 237,800.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `701.80` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `701.90` | 74,620,000.00 USD | 0.00 USD | 74,620,000.00 USD | 135,260.00 USD | 41,260.00 USD | 89,700.00 USD |
| `7D` | `702.80` | 74,360,000.00 USD | 0.00 USD | 74,360,000.00 USD | 416,820.00 USD | 57,470.00 USD | 36,720.00 USD |
| `1D` | `703.70` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `703.70` | 73,840,000.00 USD | 0.00 USD | 73,840,000.00 USD | 311,800.00 USD | 44,990.00 USD | 0.00 USD |
| `7D` | `704.60` | 73,490,000.00 USD | 0.00 USD | 73,490,000.00 USD | 537,050.00 USD | 136,550.00 USD | 194,460.00 USD |
| `1D` | `705.10` | 96,830.00 USD | 96,830.00 USD | 0.00 USD | 0.00 USD | 96,830.00 USD | 0.00 USD |
| `7D` | `705.50` | 72,620,000.00 USD | 0.00 USD | 72,620,000.00 USD | 920,340.00 USD | 162,820.00 USD | 236,670.00 USD |
| `7D` | `706.40` | 71,300,000.00 USD | 0.00 USD | 71,300,000.00 USD | 523,540.00 USD | 104,380.00 USD | 231,200.00 USD |
| `7D` | `707.30` | 70,440,000.00 USD | 0.00 USD | 70,440,000.00 USD | 604,060.00 USD | 90,200.00 USD | 53,960.00 USD |
| `7D` | `708.20` | 69,690,000.00 USD | 0.00 USD | 69,690,000.00 USD | 796,640.00 USD | 138,200.00 USD | 42,800.00 USD |
| `7D` | `709.10` | 68,710,000.00 USD | 0.00 USD | 68,710,000.00 USD | 392,150.00 USD | 156,040.00 USD | 195,500.00 USD |
| `7D` | `710.00` | 67,970,000.00 USD | 0.00 USD | 67,970,000.00 USD | 450,480.00 USD | 167,090.00 USD | 176,960.00 USD |
| `7D` | `710.90` | 67,180,000.00 USD | 0.00 USD | 67,180,000.00 USD | 922,450.00 USD | 160,040.00 USD | 236,990.00 USD |
| `7D` | `711.80` | 65,860,000.00 USD | 0.00 USD | 65,860,000.00 USD | 608,910.00 USD | 232,130.00 USD | 114,740.00 USD |
| `7D` | `712.70` | 64,900,000.00 USD | 0.00 USD | 64,900,000.00 USD | 1,190,000.00 USD | 217,390.00 USD | 236,970.00 USD |
| `7D` | `713.60` | 63,260,000.00 USD | 0.00 USD | 63,260,000.00 USD | 2,250,000.00 USD | 279,180.00 USD | 308,960.00 USD |
| `7D` | `714.50` | 60,410,000.00 USD | 0.00 USD | 60,410,000.00 USD | 508,400.00 USD | 209,320.00 USD | 292,980.00 USD |
| `7D` | `715.40` | 59,400,000.00 USD | 0.00 USD | 59,400,000.00 USD | 1,050,000.00 USD | 419,310.00 USD | 329,730.00 USD |
| `1D` | `716.10` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 137,360.00 USD | 1,060,000.00 USD |
| `7D` | `716.30` | 57,600,000.00 USD | 0.00 USD | 57,600,000.00 USD | 1,080,000.00 USD | 324,540.00 USD | 233,140.00 USD |
| `1D` | `717.20` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 253,150.00 USD | 466,010.00 USD |
| `7D` | `717.20` | 55,960,000.00 USD | 0.00 USD | 55,960,000.00 USD | 581,610.00 USD | 398,030.00 USD | 387,120.00 USD |
| `7D` | `718.10` | 54,590,000.00 USD | 0.00 USD | 54,590,000.00 USD | 1,690,000.00 USD | 246,320.00 USD | 151,880.00 USD |
| `1D` | `718.30` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 145,050.00 USD | 115,870.00 USD | 0.00 USD |
| `7D` | `719.00` | 52,510,000.00 USD | 0.00 USD | 52,510,000.00 USD | 670,390.00 USD | 137,460.00 USD | 211,490.00 USD |
| `1D` | `719.40` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 126,360.00 USD | 166,310.00 USD | 0.00 USD |
| `7D` | `719.90` | 51,490,000.00 USD | 0.00 USD | 51,490,000.00 USD | 618,020.00 USD | 173,240.00 USD | 186,780.00 USD |
| `7D` | `720.80` | 50,510,000.00 USD | 0.00 USD | 50,510,000.00 USD | 1,010,000.00 USD | 52,490.00 USD | 180,370.00 USD |
| `1D` | `721.60` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 283,170.00 USD | 0.00 USD |
| `7D` | `721.70` | 49,260,000.00 USD | 0.00 USD | 49,260,000.00 USD | 1,950,000.00 USD | 237,690.00 USD | 653,400.00 USD |
| `7D` | `722.60` | 46,430,000.00 USD | 0.00 USD | 46,430,000.00 USD | 1,930,000.00 USD | 108,200.00 USD | 229,380.00 USD |
| `7D` | `723.50` | 44,160,000.00 USD | 0.00 USD | 44,160,000.00 USD | 640,550.00 USD | 140,550.00 USD | 293,670.00 USD |
| `1D` | `723.80` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 0.00 USD | 437,890.00 USD | 0.00 USD |
| `7D` | `724.40` | 43,080,000.00 USD | 0.00 USD | 43,080,000.00 USD | 663,550.00 USD | 186,780.00 USD | 130,770.00 USD |
| `1D` | `724.90` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 0.00 USD | 57,080.00 USD | 0.00 USD |
| `7D` | `725.30` | 42,100,000.00 USD | 0.00 USD | 42,100,000.00 USD | 1,760,000.00 USD | 418,390.00 USD | 396,690.00 USD |
| `7D` | `726.20` | 39,520,000.00 USD | 0.00 USD | 39,520,000.00 USD | 1,060,000.00 USD | 311,550.00 USD | 460,020.00 USD |
| `1D` | `727.10` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 0.00 USD | 64,470.00 USD | 0.00 USD |
| `7D` | `727.10` | 37,690,000.00 USD | 0.00 USD | 37,690,000.00 USD | 1,230,000.00 USD | 331,980.00 USD | 241,010.00 USD |
| `7D` | `728.00` | 35,890,000.00 USD | 0.00 USD | 35,890,000.00 USD | 3,110,000.00 USD | 778,750.00 USD | 388,930.00 USD |
| `7D` | `728.90` | 31,610,000.00 USD | 0.00 USD | 31,610,000.00 USD | 2,330,000.00 USD | 317,590.00 USD | 644,150.00 USD |
| `1D` | `729.30` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 27,090.00 USD | 458,580.00 USD |
| `7D` | `729.80` | 28,320,000.00 USD | 0.00 USD | 28,320,000.00 USD | 1,320,000.00 USD | 430,010.00 USD | 339,140.00 USD |
| `1D` | `730.40` | 7,330,000.00 USD | 7,330,000.00 USD | 0.00 USD | 1,540,000.00 USD | 107,360.00 USD | 1,780,000.00 USD |
| `7D` | `730.70` | 26,230,000.00 USD | 0.00 USD | 26,230,000.00 USD | 2,760,000.00 USD | 351,520.00 USD | 587,010.00 USD |
| `1D` | `731.50` | 8,600,000.00 USD | 8,600,000.00 USD | 0.00 USD | 952,750.00 USD | 82,570.00 USD | 233,010.00 USD |
| `7D` | `731.60` | 22,530,000.00 USD | 0.00 USD | 22,530,000.00 USD | 1,530,000.00 USD | 133,980.00 USD | 261,910.00 USD |
| `7D` | `732.50` | 20,610,000.00 USD | 0.00 USD | 20,610,000.00 USD | 465,880.00 USD | 221,510.00 USD | 96,400.00 USD |
| `1D` | `732.60` | 9,810,000.00 USD | 9,810,000.00 USD | 0.00 USD | 430,780.00 USD | 73,020.00 USD | 703,180.00 USD |
| `7D` | `733.40` | 19,820,000.00 USD | 0.00 USD | 19,820,000.00 USD | 1,910,000.00 USD | 158,310.00 USD | 338,540.00 USD |
| `1D` | `733.70` | 11,060,000.00 USD | 11,060,000.00 USD | 0.00 USD | 1,050,000.00 USD | 206,790.00 USD | 0.00 USD |
| `7D` | `734.30` | 17,420,000.00 USD | 0.00 USD | 17,420,000.00 USD | 1,580,000.00 USD | 288,470.00 USD | 244,940.00 USD |
| `1D` | `734.80` | 11,710,000.00 USD | 11,710,000.00 USD | 0.00 USD | 460,890.00 USD | 187,740.00 USD | 0.00 USD |
| `7D` | `735.20` | 15,310,000.00 USD | 0.00 USD | 15,310,000.00 USD | 1,330,000.00 USD | 172,940.00 USD | 437,510.00 USD |
| `1D` | `735.90` | 13,490,000.00 USD | 13,490,000.00 USD | 0.00 USD | 1,110,000.00 USD | 81,400.00 USD | 590,930.00 USD |
| `7D` | `736.10` | 13,370,000.00 USD | 0.00 USD | 13,370,000.00 USD | 2,130,000.00 USD | 181,990.00 USD | 484,910.00 USD |
| `1D` | `737.00` | 13,930,000.00 USD | 13,930,000.00 USD | 0.00 USD | 438,340.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `737.00` | 10,570,000.00 USD | 0.00 USD | 10,570,000.00 USD | 2,360,000.00 USD | 175,330.00 USD | 633,690.00 USD |
| `7D` | `737.90` | 7,400,000.00 USD | 0.00 USD | 7,400,000.00 USD | 3,420,000.00 USD | 72,280.00 USD | 374,090.00 USD |
| `1D` | `738.10` | 14,260,000.00 USD | 14,260,000.00 USD | 0.00 USD | 160,280.00 USD | 162,750.00 USD | 0.00 USD |
| `7D` | `738.80` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 522,950.00 USD | 20,210.00 USD | 155,300.00 USD |
| `1D` | `739.20` | 16,000,000.00 USD | 16,000,000.00 USD | 0.00 USD | 807,980.00 USD | 0.00 USD | 934,700.00 USD |
| `7D` | `739.70` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 352,500.00 USD | 0.00 USD | 203,030.00 USD |
| `1D` | `740.30` | 16,820,000.00 USD | 16,820,000.00 USD | 0.00 USD | 661,350.00 USD | 134,150.00 USD | 22,040.00 USD |
| `7D` | `740.60` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 1,090,000.00 USD | 0.00 USD | 33,390.00 USD |
| `1D` | `741.40` | 17,230,000.00 USD | 17,230,000.00 USD | 0.00 USD | 379,980.00 USD | 32,240.00 USD | 0.00 USD |
| `7D` | `741.50` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 257,630.00 USD | 0.00 USD | 208,590.00 USD |
| `7D` | `742.40` | 689,850.00 USD | 0.00 USD | 689,850.00 USD | 0.00 USD | 0.00 USD | 183,920.00 USD |
| `1D` | `742.50` | 17,520,000.00 USD | 17,520,000.00 USD | 0.00 USD | 291,160.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `743.30` | 505,930.00 USD | 0.00 USD | 505,930.00 USD | 0.00 USD | 0.00 USD | 57,580.00 USD |
| `1D` | `743.60` | 18,080,000.00 USD | 18,080,000.00 USD | 0.00 USD | 120,950.00 USD | 0.00 USD | 436,560.00 USD |
| `7D` | `744.20` | 448,350.00 USD | 0.00 USD | 448,350.00 USD | 0.00 USD | 257,580.00 USD | 141,790.00 USD |
| `1D` | `744.70` | 19,920,000.00 USD | 19,920,000.00 USD | 0.00 USD | 878,190.00 USD | 106,580.00 USD | 854,020.00 USD |
| `7D` | `745.10` | 48,980.00 USD | 0.00 USD | 48,980.00 USD | 0.00 USD | 48,980.00 USD | 0.00 USD |
| `7D` | `745.20` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `745.80` | 20,430,000.00 USD | 20,430,000.00 USD | 0.00 USD | 443,420.00 USD | 74,600.00 USD | 0.00 USD |
| `7D` | `746.00` | 999,320.00 USD | 999,320.00 USD | 0.00 USD | 999,320.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `746.90` | 21,800,000.00 USD | 21,800,000.00 USD | 0.00 USD | 538,200.00 USD | 68,950.00 USD | 758,780.00 USD |
| `7D` | `746.90` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 215,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `748.00` | 22,550,000.00 USD | 22,550,000.00 USD | 0.00 USD | 573,840.00 USD | 103,400.00 USD | 73,330.00 USD |
| `1D` | `749.10` | 22,890,000.00 USD | 22,890,000.00 USD | 0.00 USD | 334,750.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `750.20` | 23,010,000.00 USD | 23,010,000.00 USD | 0.00 USD | 120,150.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `751.30` | 23,120,000.00 USD | 23,120,000.00 USD | 0.00 USD | 17,390.00 USD | 0.00 USD | 98,240.00 USD |
| `1D` | `752.40` | 23,850,000.00 USD | 23,850,000.00 USD | 0.00 USD | 263,850.00 USD | 25,010.00 USD | 441,380.00 USD |
| `1D` | `753.50` | 24,150,000.00 USD | 24,150,000.00 USD | 0.00 USD | 30,730.00 USD | 3,810.00 USD | 262,160.00 USD |
| `1D` | `754.60` | 24,690,000.00 USD | 24,690,000.00 USD | 0.00 USD | 352,780.00 USD | 149,020.00 USD | 43,990.00 USD |
| `7D` | `755.00` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 59,560.00 USD | 0.00 USD |
| `1D` | `755.70` | 25,310,000.00 USD | 25,310,000.00 USD | 0.00 USD | 384,280.00 USD | 176,290.00 USD | 56,900.00 USD |
| `1D` | `756.80` | 25,850,000.00 USD | 25,850,000.00 USD | 0.00 USD | 422,820.00 USD | 24,970.00 USD | 95,500.00 USD |
| `7D` | `756.80` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 47,340.00 USD | 0.00 USD |
| `7D` | `757.70` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 475,510.00 USD | 113,240.00 USD | 0.00 USD |
| `1D` | `757.90` | 26,560,000.00 USD | 26,560,000.00 USD | 0.00 USD | 482,940.00 USD | 189,940.00 USD | 32,720.00 USD |
| `7D` | `758.60` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `759.00` | 28,110,000.00 USD | 28,110,000.00 USD | 0.00 USD | 1,150,000.00 USD | 122,880.00 USD | 273,090.00 USD |
| `1D` | `760.10` | 28,650,000.00 USD | 28,650,000.00 USD | 0.00 USD | 409,880.00 USD | 80,670.00 USD | 49,480.00 USD |
| `7D` | `760.40` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 0.00 USD | 27,650.00 USD | 42,540.00 USD |
| `1D` | `761.20` | 29,810,000.00 USD | 29,810,000.00 USD | 0.00 USD | 774,860.00 USD | 90,660.00 USD | 301,000.00 USD |
| `7D` | `761.30` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 10,750.00 USD | 211,960.00 USD | 100,630.00 USD |
| `7D` | `762.20` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 699,820.00 USD | 179,270.00 USD |
| `1D` | `762.30` | 30,860,000.00 USD | 30,860,000.00 USD | 0.00 USD | 658,580.00 USD | 172,280.00 USD | 220,780.00 USD |
| `7D` | `763.10` | 7,830,000.00 USD | 7,830,000.00 USD | 0.00 USD | 2,460,000.00 USD | 590,460.00 USD | 404,720.00 USD |
| `1D` | `763.40` | 34,320,000.00 USD | 34,320,000.00 USD | 0.00 USD | 2,620,000.00 USD | 247,430.00 USD | 590,940.00 USD |
| `7D` | `764.00` | 10,270,000.00 USD | 10,270,000.00 USD | 0.00 USD | 1,590,000.00 USD | 441,980.00 USD | 402,300.00 USD |
| `1D` | `764.50` | 36,640,000.00 USD | 36,640,000.00 USD | 0.00 USD | 1,790,000.00 USD | 210,060.00 USD | 321,430.00 USD |
| `7D` | `764.90` | 12,470,000.00 USD | 12,470,000.00 USD | 0.00 USD | 1,450,000.00 USD | 352,570.00 USD | 395,630.00 USD |
| `1D` | `765.60` | 38,300,000.00 USD | 38,300,000.00 USD | 0.00 USD | 1,250,000.00 USD | 188,930.00 USD | 217,160.00 USD |
| `7D` | `765.80` | 15,460,000.00 USD | 15,460,000.00 USD | 0.00 USD | 2,470,000.00 USD | 107,550.00 USD | 416,290.00 USD |
| `1D` | `766.70` | 40,650,000.00 USD | 40,650,000.00 USD | 0.00 USD | 1,630,000.00 USD | 260,910.00 USD | 463,880.00 USD |
| `7D` | `766.70` | 20,050,000.00 USD | 20,050,000.00 USD | 0.00 USD | 3,330,000.00 USD | 416,530.00 USD | 842,330.00 USD |
| `7D` | `767.60` | 23,430,000.00 USD | 23,430,000.00 USD | 0.00 USD | 2,790,000.00 USD | 123,530.00 USD | 467,840.00 USD |
| `1D` | `767.80` | 43,170,000.00 USD | 43,170,000.00 USD | 0.00 USD | 1,990,000.00 USD | 160,290.00 USD | 364,550.00 USD |
| `7D` | `768.50` | 25,660,000.00 USD | 25,660,000.00 USD | 0.00 USD | 1,840,000.00 USD | 95,830.00 USD | 281,920.00 USD |
| `1D` | `768.90` | 44,350,000.00 USD | 44,350,000.00 USD | 0.00 USD | 986,770.00 USD | 56,740.00 USD | 135,830.00 USD |
| `7D` | `769.40` | 26,810,000.00 USD | 26,810,000.00 USD | 0.00 USD | 565,780.00 USD | 249,950.00 USD | 333,550.00 USD |
| `1D` | `770.00` | 45,190,000.00 USD | 45,190,000.00 USD | 0.00 USD | 590,250.00 USD | 180,380.00 USD | 72,790.00 USD |
| `7D` | `770.30` | 29,310,000.00 USD | 29,310,000.00 USD | 0.00 USD | 1,900,000.00 USD | 240,530.00 USD | 364,650.00 USD |
| `1D` | `771.10` | 46,190,000.00 USD | 46,190,000.00 USD | 0.00 USD | 610,340.00 USD | 46,300.00 USD | 340,350.00 USD |
| `7D` | `771.20` | 30,770,000.00 USD | 30,770,000.00 USD | 0.00 USD | 1,050,000.00 USD | 242,570.00 USD | 162,680.00 USD |
| `7D` | `772.10` | 33,190,000.00 USD | 33,190,000.00 USD | 0.00 USD | 1,750,000.00 USD | 252,650.00 USD | 419,070.00 USD |
| `1D` | `772.20` | 47,390,000.00 USD | 47,390,000.00 USD | 0.00 USD | 426,940.00 USD | 131,000.00 USD | 647,240.00 USD |
| `7D` | `773.00` | 35,800,000.00 USD | 35,800,000.00 USD | 0.00 USD | 1,950,000.00 USD | 325,680.00 USD | 338,170.00 USD |
| `1D` | `773.30` | 48,800,000.00 USD | 48,800,000.00 USD | 0.00 USD | 1,090,000.00 USD | 175,430.00 USD | 148,410.00 USD |
| `7D` | `773.90` | 37,600,000.00 USD | 37,600,000.00 USD | 0.00 USD | 1,220,000.00 USD | 276,760.00 USD | 293,960.00 USD |
| `1D` | `774.40` | 50,050,000.00 USD | 50,050,000.00 USD | 0.00 USD | 1,080,000.00 USD | 85,850.00 USD | 79,780.00 USD |
| `7D` | `774.80` | 39,980,000.00 USD | 39,980,000.00 USD | 0.00 USD | 1,310,000.00 USD | 568,930.00 USD | 502,710.00 USD |
| `1D` | `775.50` | 50,810,000.00 USD | 50,810,000.00 USD | 0.00 USD | 543,580.00 USD | 151,460.00 USD | 63,460.00 USD |
| `7D` | `775.70` | 42,470,000.00 USD | 42,470,000.00 USD | 0.00 USD | 1,830,000.00 USD | 470,960.00 USD | 187,170.00 USD |
| `1D` | `776.60` | 51,340,000.00 USD | 51,340,000.00 USD | 0.00 USD | 365,690.00 USD | 63,550.00 USD | 109,010.00 USD |
| `7D` | `776.60` | 44,740,000.00 USD | 44,740,000.00 USD | 0.00 USD | 1,630,000.00 USD | 269,050.00 USD | 378,590.00 USD |
| `7D` | `777.50` | 46,480,000.00 USD | 46,480,000.00 USD | 0.00 USD | 1,350,000.00 USD | 243,990.00 USD | 148,450.00 USD |
| `1D` | `777.70` | 52,860,000.00 USD | 52,860,000.00 USD | 0.00 USD | 996,310.00 USD | 148,330.00 USD | 372,830.00 USD |
| `7D` | `778.40` | 48,170,000.00 USD | 48,170,000.00 USD | 0.00 USD | 1,180,000.00 USD | 307,370.00 USD | 206,530.00 USD |
| `1D` | `778.80` | 54,000,000.00 USD | 54,000,000.00 USD | 0.00 USD | 927,520.00 USD | 107,660.00 USD | 106,210.00 USD |
| `7D` | `779.30` | 49,730,000.00 USD | 49,730,000.00 USD | 0.00 USD | 1,240,000.00 USD | 188,170.00 USD | 123,650.00 USD |
| `1D` | `779.90` | 54,940,000.00 USD | 54,940,000.00 USD | 0.00 USD | 670,650.00 USD | 139,800.00 USD | 127,490.00 USD |
| `7D` | `780.20` | 51,100,000.00 USD | 51,100,000.00 USD | 0.00 USD | 1,070,000.00 USD | 86,470.00 USD | 218,750.00 USD |
| `1D` | `781.00` | 55,870,000.00 USD | 55,870,000.00 USD | 0.00 USD | 691,970.00 USD | 83,750.00 USD | 148,620.00 USD |
| `7D` | `781.10` | 52,710,000.00 USD | 52,710,000.00 USD | 0.00 USD | 1,270,000.00 USD | 90,990.00 USD | 242,450.00 USD |
| `7D` | `782.00` | 54,610,000.00 USD | 54,610,000.00 USD | 0.00 USD | 1,510,000.00 USD | 87,670.00 USD | 301,190.00 USD |
| `1D` | `782.10` | 57,380,000.00 USD | 57,380,000.00 USD | 0.00 USD | 1,070,000.00 USD | 97,460.00 USD | 338,530.00 USD |
| `7D` | `782.90` | 56,600,000.00 USD | 56,600,000.00 USD | 0.00 USD | 1,750,000.00 USD | 36,140.00 USD | 202,700.00 USD |
| `1D` | `783.20` | 58,500,000.00 USD | 58,500,000.00 USD | 0.00 USD | 893,500.00 USD | 66,810.00 USD | 162,670.00 USD |
| `7D` | `783.80` | 57,170,000.00 USD | 57,170,000.00 USD | 0.00 USD | 508,000.00 USD | 10,100.00 USD | 54,380.00 USD |
| `1D` | `784.30` | 59,030,000.00 USD | 59,030,000.00 USD | 0.00 USD | 485,610.00 USD | 23,200.00 USD | 18,280.00 USD |
| `7D` | `784.70` | 57,480,000.00 USD | 57,480,000.00 USD | 0.00 USD | 208,380.00 USD | 28,260.00 USD | 70,300.00 USD |
| `1D` | `785.40` | 59,550,000.00 USD | 59,550,000.00 USD | 0.00 USD | 460,360.00 USD | 37,320.00 USD | 27,120.00 USD |
| `7D` | `785.60` | 58,610,000.00 USD | 58,610,000.00 USD | 0.00 USD | 1,010,000.00 USD | 54,140.00 USD | 71,180.00 USD |
| `1D` | `786.50` | 59,850,000.00 USD | 59,850,000.00 USD | 0.00 USD | 262,870.00 USD | 15,410.00 USD | 26,240.00 USD |
| `7D` | `786.50` | 59,000,000.00 USD | 59,000,000.00 USD | 0.00 USD | 329,230.00 USD | 30,660.00 USD | 23,970.00 USD |
| `7D` | `787.40` | 59,580,000.00 USD | 59,580,000.00 USD | 0.00 USD | 470,050.00 USD | 17,630.00 USD | 91,050.00 USD |
| `1D` | `787.60` | 60,350,000.00 USD | 60,350,000.00 USD | 0.00 USD | 434,490.00 USD | 33,000.00 USD | 24,380.00 USD |
| `7D` | `788.30` | 59,940,000.00 USD | 59,940,000.00 USD | 0.00 USD | 202,630.00 USD | 82,380.00 USD | 81,230.00 USD |
| `1D` | `788.70` | 61,020,000.00 USD | 61,020,000.00 USD | 0.00 USD | 205,450.00 USD | 49,630.00 USD | 420,190.00 USD |
| `7D` | `789.20` | 60,780,000.00 USD | 60,780,000.00 USD | 0.00 USD | 698,830.00 USD | 81,250.00 USD | 55,990.00 USD |
| `1D` | `789.80` | 61,760,000.00 USD | 61,760,000.00 USD | 0.00 USD | 548,330.00 USD | 26,520.00 USD | 165,700.00 USD |
| `7D` | `790.10` | 61,270,000.00 USD | 61,270,000.00 USD | 0.00 USD | 299,250.00 USD | 104,360.00 USD | 88,890.00 USD |
| `1D` | `790.90` | 62,200,000.00 USD | 62,200,000.00 USD | 0.00 USD | 338,320.00 USD | 88,600.00 USD | 11,310.00 USD |
| `7D` | `791.00` | 62,150,000.00 USD | 62,150,000.00 USD | 0.00 USD | 693,290.00 USD | 82,870.00 USD | 100,420.00 USD |
| `7D` | `791.90` | 63,030,000.00 USD | 63,030,000.00 USD | 0.00 USD | 816,380.00 USD | 16,830.00 USD | 46,300.00 USD |
| `1D` | `792.00` | 62,550,000.00 USD | 62,550,000.00 USD | 0.00 USD | 352,670.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `792.80` | 63,250,000.00 USD | 63,250,000.00 USD | 0.00 USD | 205,450.00 USD | 0.00 USD | 14,670.00 USD |
| `1D` | `793.10` | 62,610,000.00 USD | 62,610,000.00 USD | 0.00 USD | 58,240.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `793.70` | 63,430,000.00 USD | 63,430,000.00 USD | 0.00 USD | 184,960.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `794.20` | 62,630,000.00 USD | 62,630,000.00 USD | 0.00 USD | 21,310.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `794.60` | 63,750,000.00 USD | 63,750,000.00 USD | 0.00 USD | 302,280.00 USD | 15,690.00 USD | 0.00 USD |
| `1D` | `795.30` | 62,680,000.00 USD | 62,680,000.00 USD | 0.00 USD | 49,090.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `795.50` | 63,890,000.00 USD | 63,890,000.00 USD | 0.00 USD | 109,640.00 USD | 14,650.00 USD | 14,200.00 USD |
| `1D` | `796.40` | 62,810,000.00 USD | 62,810,000.00 USD | 0.00 USD | 36,340.00 USD | 0.00 USD | 94,590.00 USD |
| `7D` | `796.40` | 64,030,000.00 USD | 64,030,000.00 USD | 0.00 USD | 139,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `797.30` | 64,090,000.00 USD | 64,090,000.00 USD | 0.00 USD | 64,670.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `797.50` | 62,890,000.00 USD | 62,890,000.00 USD | 0.00 USD | 78,300.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `798.20` | 64,250,000.00 USD | 64,250,000.00 USD | 0.00 USD | 155,890.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `798.60` | 62,960,000.00 USD | 62,960,000.00 USD | 0.00 USD | 46,910.00 USD | 26,830.00 USD | 0.00 USD |
| `7D` | `799.10` | 64,290,000.00 USD | 64,290,000.00 USD | 0.00 USD | 42,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `799.70` | 62,980,000.00 USD | 62,980,000.00 USD | 0.00 USD | 18,790.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `800.00` | 64,400,000.00 USD | 64,400,000.00 USD | 0.00 USD | 113,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `800.80` | 62,990,000.00 USD | 62,990,000.00 USD | 0.00 USD | 11,140.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `800.90` | 64,510,000.00 USD | 64,510,000.00 USD | 0.00 USD | 77,580.00 USD | 8,370.00 USD | 21,920.00 USD |
| `7D` | `801.80` | 64,720,000.00 USD | 64,720,000.00 USD | 0.00 USD | 179,900.00 USD | 16,330.00 USD | 10,970.00 USD |
| `1D` | `801.90` | 63,110,000.00 USD | 63,110,000.00 USD | 0.00 USD | 30,060.00 USD | 0.00 USD | 87,310.00 USD |
| `7D` | `802.70` | 64,730,000.00 USD | 64,730,000.00 USD | 0.00 USD | 11,220.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `803.00` | 63,150,000.00 USD | 63,150,000.00 USD | 0.00 USD | 20,540.00 USD | 21,320.00 USD | 0.00 USD |
| `7D` | `803.60` | 64,760,000.00 USD | 64,760,000.00 USD | 0.00 USD | 27,360.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `804.10` | 63,250,000.00 USD | 63,250,000.00 USD | 0.00 USD | 80,140.00 USD | 14,920.00 USD | 0.00 USD |
| `7D` | `804.50` | 64,840,000.00 USD | 64,840,000.00 USD | 0.00 USD | 32,340.00 USD | 18,260.00 USD | 32,980.00 USD |
| `1D` | `805.20` | 63,400,000.00 USD | 63,400,000.00 USD | 0.00 USD | 67,230.00 USD | 0.00 USD | 81,440.00 USD |
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
  * Total Open Interest: `1.36B` | Total OI Tokens: `1,933,278.7 BNB`
  * 1h OI Change: `-0.01%` | 4h OI Change: `+10.95%` | 24h OI Change: `+6.91%`
  * Exchange Breakdown: Binance=`594.96M` | Bybit=`141.48M` | OKX=`59.99M` | Hyperliquid=`92.22M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-75.71K` | Last 24h: `109.28K` | Last 3d: `307.00K` | Last 7d: `451.01K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0000%` | **USDT OKX** | `-0.0140%` |
| **USDT Bybit** | `-0.0488%` | **USDT KuCoin** | `-0.0175%` |
| **USDT MEXC** | `0.0000%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0008%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0006%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `BNB` | `53.89%` | `46.11%` | `1.17` | 129,800,000.00 USD |
| `15M` | `Binance` | `52.55%` | `47.45%` | `1.11` | 56,530,000.00 USD |
| `15M` | `OKX` | `57.42%` | `42.58%` | `1.35` | 17,510,000.00 USD |
| `15M` | `Bybit` | `46.85%` | `53.15%` | `0.88` | 10,360,000.00 USD |
| `15M` | `KuCoin` | `49.63%` | `50.37%` | `0.99` | 1,120,000.00 USD |
| `15M` | `Gate` | `39.13%` | `60.87%` | `0.64` | 7,220,000.00 USD |
| `15M` | `Bitget` | `42.72%` | `57.28%` | `0.75` | 5,280,000.00 USD |
| `15M` | `BingX` | `49.8%` | `50.2%` | `0.99` | 3,140,000.00 USD |
| `15M` | `MEXC` | `59.88%` | `40.12%` | `1.49` | 4,770,000.00 USD |
| `15M` | `Bitunix` | `58.2%` | `41.8%` | `1.39` | 3,530,000.00 USD |
| `15M` | `Hyperliquid` | `87.14%` | `12.86%` | `6.78` | 13,840,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `69.46%` | `30.54%` | `2.27` | 2,580,000.00 USD |
| `15M` | `Crypto.com` | `57.92%` | `42.08%` | `1.38` | 205,800.00 USD |
| `15M` | `WhiteBIT` | `99.3%` | `0.7%` | `141.86` | 1,100,000.00 USD |
| `15M` | `HTX` | `59.9%` | `40.1%` | `1.49` | 52,570.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `22.73%` | `77.27%` | `0.29` | 680,280.00 USD |
| `15M` | `Aster` | `37.83%` | `62.17%` | `0.61` | 1,140,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `58.31%` | `41.69%` | `1.40` | 749,990.00 USD |
| `15M` | `Whale Positions` | `52.55%` | `47.45%` | `1.11` | 56,530,000.00 USD |
| `15M` | `Global Accounts` | `53.89%` | `46.11%` | `1.17` | 129,800,000.00 USD |
| `1H` | `BNB` | `46.29%` | `53.71%` | `0.86` | 771,160,000.00 USD |
| `1H` | `Binance` | `44.31%` | `55.69%` | `0.80` | 353,130,000.00 USD |
| `1H` | `OKX` | `51.49%` | `48.51%` | `1.06` | 106,980,000.00 USD |
| `1H` | `Bybit` | `37.34%` | `62.66%` | `0.60` | 70,240,000.00 USD |
| `1H` | `KuCoin` | `47.52%` | `52.48%` | `0.91` | 5,030,000.00 USD |
| `1H` | `Gate` | `50.39%` | `49.61%` | `1.02` | 31,480,000.00 USD |
| `1H` | `Bitget` | `50.41%` | `49.59%` | `1.02` | 30,510,000.00 USD |
| `1H` | `BingX` | `46.6%` | `53.4%` | `0.87` | 16,010,000.00 USD |
| `1H` | `MEXC` | `50.2%` | `49.8%` | `1.01` | 44,260,000.00 USD |
| `1H` | `Bitunix` | `47.96%` | `52.04%` | `0.92` | 25,980,000.00 USD |
| `1H` | `Hyperliquid` | `47.3%` | `52.7%` | `0.90` | 46,910,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.36%` | `49.64%` | `1.01` | 11,760,000.00 USD |
| `1H` | `Crypto.com` | `50.06%` | `49.94%` | `1.00` | 1,530,000.00 USD |
| `1H` | `WhiteBIT` | `56.54%` | `43.46%` | `1.30` | 3,270,000.00 USD |
| `1H` | `HTX` | `52.49%` | `47.51%` | `1.10` | 1,110,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `34.48%` | `65.52%` | `0.53` | 4,290,000.00 USD |
| `1H` | `Aster` | `61.19%` | `38.81%` | `1.58` | 11,800,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `49.26%` | `50.74%` | `0.97` | 6,860,000.00 USD |
| `1H` | `Whale Positions` | `44.31%` | `55.69%` | `0.80` | 353,130,000.00 USD |
| `1H` | `Global Accounts` | `46.29%` | `53.71%` | `0.86` | 771,160,000.00 USD |
| `4H` | `BNB` | `45.59%` | `54.41%` | `0.84` | 1,510,000,000.00 USD |
| `4H` | `Binance` | `44.96%` | `55.04%` | `0.82` | 580,460,000.00 USD |
| `4H` | `OKX` | `46.57%` | `53.43%` | `0.87` | 193,480,000.00 USD |
| `4H` | `Bybit` | `42.04%` | `57.96%` | `0.73` | 227,150,000.00 USD |
| `4H` | `KuCoin` | `47.84%` | `52.16%` | `0.92` | 29,210,000.00 USD |
| `4H` | `Gate` | `48.37%` | `51.63%` | `0.94` | 36,350,000.00 USD |
| `4H` | `Bitget` | `42.88%` | `57.12%` | `0.75` | 75,450,000.00 USD |
| `4H` | `BingX` | `47.53%` | `52.47%` | `0.91` | 25,340,000.00 USD |
| `4H` | `MEXC` | `51.23%` | `48.77%` | `1.05` | 145,730,000.00 USD |
| `4H` | `Bitunix` | `47.41%` | `52.59%` | `0.90` | 60,070,000.00 USD |
| `4H` | `Hyperliquid` | `41.14%` | `58.86%` | `0.70` | 73,800,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `51.91%` | `48.09%` | `1.08` | 6,070,000.00 USD |
| `4H` | `Crypto.com` | `46.16%` | `53.84%` | `0.86` | 2,540,000.00 USD |
| `4H` | `WhiteBIT` | `41.53%` | `58.47%` | `0.71` | 25,290,000.00 USD |
| `4H` | `HTX` | `44.48%` | `55.52%` | `0.80` | 1,220,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `49.62%` | `50.38%` | `0.98` | 8,240,000.00 USD |
| `4H` | `Aster` | `52.73%` | `47.27%` | `1.12` | 14,570,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `45.71%` | `54.29%` | `0.84` | 2,060,000.00 USD |
| `4H` | `Whale Positions` | `44.96%` | `55.04%` | `0.82` | 580,460,000.00 USD |
| `4H` | `Global Accounts` | `45.59%` | `54.41%` | `0.84` | 1,510,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `733.05` | `735.28` | `733.05` | `741.15` | `730.35` | 58,847,128.96 USD | 25,808,552.51 USD | 33,038,576.45 USD | -7,230,023.95 USD | `-12.29%` | `2B / 6S` |
| `0:00 UTC` | `693.15` | `709.93` | `693.15` | `733.35` | `688.35` | 287,121,588.96 USD | 130,602,079.05 USD | 156,519,509.92 USD | -25,917,430.87 USD | `-9.03%` | `0B / 21S` |
| `5:00 UTC` | `694.05` | `694.59` | `694.05` | `707.85` | `677.85` | 179,693,058.88 USD | 96,266,693.98 USD | 83,426,364.90 USD | 12,840,329.08 USD | `+7.15%` | `3B / 4S` |
| `0:00 UTC` | `705.15` | `704.71` | `705.15` | `718.65` | `690.75` | 186,631,734.60 USD | 100,794,189.14 USD | 85,837,545.46 USD | 14,956,643.67 USD | `+8.01%` | `11B / 2S` |
| `5:00 UTC` | `717.75` | `715.45` | `717.75` | `727.95` | `707.85` | 126,482,329.61 USD | 66,523,365.17 USD | 59,958,964.44 USD | 6,564,400.73 USD | `+5.19%` | `10B / 3S` |
| `0:00 UTC` | `709.95` | `710.65` | `709.95` | `715.65` | `705.45` | 34,559,429.86 USD | 16,578,658.63 USD | 17,980,771.23 USD | -1,402,112.60 USD | `-4.06%` | `2B / 2S` |
| `5:00 UTC` | `705.15` | `705.50` | `705.15` | `709.35` | `701.85` | 34,534,245.79 USD | 19,030,414.31 USD | 15,503,831.48 USD | 3,526,582.82 USD | `+10.21%` | `3B / 0S` |
| `0:00 UTC` | `703.95` | `704.22` | `703.95` | `708.75` | `700.95` | 21,370,966.63 USD | 9,634,694.93 USD | 11,736,271.71 USD | -2,101,576.78 USD | `-9.83%` | `1B / 1S` |
| `5:00 UTC` | `705.15` | `704.00` | `705.15` | `706.35` | `700.95` | 18,920,983.07 USD | 9,587,357.21 USD | 9,333,625.86 USD | 253,731.35 USD | `+1.34%` | `1B / 3S` |
| `0:00 UTC` | `701.25` | `702.31` | `701.25` | `705.75` | `700.05` | 21,719,283.89 USD | 11,222,812.76 USD | 10,496,471.13 USD | 726,341.62 USD | `+3.34%` | `0B / 2S` |

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
| `5m` | -74,790.00 USD | 815,070.00 USD | **`ACCUMULATION`** |
| `15m` | -2,120,000.00 USD | 775,180.00 USD | **`DISTRIBUTION`** |
| `30m` | -1,430,000.00 USD | -1,140,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -973,440.00 USD | -2,280,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -10,880,000.00 USD | -4,200,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -17,180,000.00 USD | -38,210,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -18,510,000.00 USD | -44,090,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -18,360,000.00 USD | -37,940,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -26,120,000.00 USD | -26,810,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -13,730,000.00 USD | -68,580,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -45,550,000.00 USD | -86,010,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -144,200,000.00 USD | -412,330,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-74.79K` | 15m=`-2.12M` | 1h=`-973.44K` | 24h=`-13.73M`
* Futures Capital Netflows: 5m=`+815.07K` | 15m=`+775.18K` | 1h=`-2.28M` | 24h=`-68.58M`
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
  * `2026-10-30 03:30:16 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:11:16 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:11:16 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:10:16 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:12:17 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:12:17 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:12:17 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:12:17 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:12:17 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:12:17 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:12:17 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:12:17 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:12:17 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:12:17 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:12:17 IST`: [ForexFactory] - (Sentiment: `Neutral`)


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
  * Execution Entry: `700.10` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `684.33` (Risk Distance: `15.77` pts)
  * +2.5R Take Profit: `739.53`
  * Mathematical Lot Sizing: **`0.63 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `714.05` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `729.82` (Risk Distance: `15.77` pts)
  * +2.5R Take Profit: `674.62`
  * Mathematical Lot Sizing: **`0.63 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`705.10`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
