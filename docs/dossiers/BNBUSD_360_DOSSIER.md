# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BNB
**Canonical Key**: `BNB` | **Broker Instrument**: `BNBUSD.p` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 04:47:08 IST` (`2026-10-29 23:17:08 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `701.90` | **Live Ask Quote**: `706.10` | **Mid Price**: `704.00`
- **Spread Points**: `420.00` | **Spread BPS**: `59.66 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `732.34` | VWAP Z-Score: `-1.46` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `8.59` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `33.75` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `794.95` | Lower -3.00σ Band: `669.73`
  * Upper +2.51σ Band: `784.73` | Lower -2.51σ Band: `679.96`
  * Upper +2.01σ Band: `774.29` | Lower -2.01σ Band: `690.39`
  * Upper +2.00σ Band: `774.08` | Lower -2.00σ Band: `690.60`
  * Upper +1.28σ Band: `759.06` | Lower -1.28σ Band: `705.63`
  * Upper +1.00σ Band: `753.21` | Lower -1.00σ Band: `711.47`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`705.49` | EMA-20=`715.77` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`729.67` (Slope: `+0.0000`) | EMA-100=`737.63`
  * Institutional Anchors: EMA-144=`740.30` | EMA-200=`741.31` (Slope: `-0.6300`) | EMA-233=`741.46`
- **Range Boundaries**: 24H High=`759.80` | 24H Low=`677.20` | Weekly High=`760.90` | Weekly Low=`677.20`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `713.37` (Distance: `-1.31%`)
  * Point of Control (POC) = `706.96` (Distance: `-0.42%`)
  * Value Area Low (VAL) = `699.19` (Distance: `+0.69%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`754.57` | POC=`744.11` | VAL=`738.60`
  * Prior Day Extremes: PDH=`759.80` | PDL=`677.20` | PDC=`696.20`
  * Monday Range Blueprint: High=`746.00` | Mid=`738.45` | Low=`730.90`
  * Developing Weekly Value Area: Weekly VAH=`751.13` | Weekly POC=`740.53` | Weekly VAL=`734.95`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`724.00` | Low=`689.70`
  * London Session (08:00-16:00 UTC): High=`706.82` | Low=`701.18`
  * New York Session (13:00-21:00 UTC): High=`708.22` | Low=`699.78`
  * Initial Balance (First Hour): IB High=`706.11` | IB Low=`701.89`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `701.18` - `706.82`
  * Optimal Trade Entry (OTE 0.705): `705.41`
  * Structural Invalidation Anchor (0.786): `709.63`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `701.27` | `703.80` | `700.69` | `703.00` | `9,447` | 6,633,199.92 USD | 611,202.31 USD | `+9.21%` | -20,149,025.99 USD | `+0.29` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `703.00` | `706.98` | `701.95` | `706.07` | `10,426` | 7,347,629.69 USD | 1,041,090.30 USD | `+14.17%` | -19,107,935.69 USD | `+0.57` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `706.07` | `706.07` | `704.90` | `705.37` | `1,118` | 788,588.56 USD | 49,498.62 USD | `+6.28%` | -19,058,437.07 USD | `-0.28` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `701.89` | `707.02` | `700.63` | `706.85` | `40,484` | 28,473,334.16 USD | 1,854,425.11 USD | `+6.51%` | -19,947,329.92 USD | `+0.24` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `706.85` | `707.13` | `700.32` | `706.07` | `34,706` | 24,422,860.18 USD | 1,270,743.14 USD | `+5.20%` | -18,676,586.77 USD | `+0.16` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `706.07` | `706.07` | `704.90` | `705.51` | `1,207` | 851,698.10 USD | 46,657.79 USD | `+5.48%` | -18,629,928.98 USD | `+0.01` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `697.33` | `727.80` | `690.87` | `708.57` | `539,232` | 382,207,739.86 USD | 23,645,514.63 USD | `+6.19%` | -22,126,984.95 USD | `+2.64` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `708.58` | `708.89` | `700.00` | `706.85` | `136,395` | 95,944,067.03 USD | 2,419,901.44 USD | `+2.52%` | -19,707,083.51 USD | `+0.34` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `706.85` | `707.13` | `700.32` | `705.37` | `35,824` | 25,211,448.74 USD | 1,320,241.76 USD | `+5.24%` | -18,386,841.75 USD | `+0.21` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `740.45` | `753.64` | `739.55` | `750.62` | `148,938` | 111,099,080.67 USD | 8,045,498.44 USD | `+7.24%` | -17,010,604.60 USD | `+1.70` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `750.62` | `754.90` | `743.07` | `745.33` | `88,414` | 66,199,547.89 USD | 232,195.88 USD | `+0.35%` | -16,778,408.72 USD | `+0.53` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `745.34` | `745.53` | `677.76` | `705.51` | `1,483,718` | 1,050,476,287.46 USD | -1,611,273.87 USD | `-0.15%` | -18,389,682.58 USD | `+0.24` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `747.26` | `759.90` | `745.75` | `748.51` | `156,800` | 118,182,602.62 USD | -8,240,157.99 USD | `-6.97%` | -14,715,810.54 USD | `-1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `748.51` | `753.57` | `738.70` | `740.45` | `333,019` | 248,636,999.78 USD | -10,340,292.49 USD | `-4.16%` | -25,056,103.04 USD | `-1.26` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `740.45` | `753.64` | `739.55` | `750.62` | `148,938` | 111,099,080.67 USD | 8,045,498.44 USD | `+7.24%` | -17,010,604.60 USD | `+1.70` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `750.62` | `754.90` | `743.07` | `745.33` | `88,414` | 66,199,547.89 USD | 232,195.88 USD | `+0.35%` | -16,778,408.72 USD | `+0.53` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `745.34` | `745.53` | `677.76` | `705.51` | `1,483,718` | 1,050,476,287.46 USD | -1,611,273.87 USD | `-0.15%` | -18,389,682.58 USD | `+0.24` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`704.00`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `703.78` | `18434000000.0000` | 12,973.48 USD | 116,367.37 USD | `3 orders` | `-0.08%` | `-` |
| `BID` | `703.80` | `5138000000.0000` | 3,616.12 USD | 103,393.89 USD | `1 orders` | `-0.08%` | `-` |
| `BID` | `703.82` | `1230000000.0000` | 865.70 USD | 99,777.77 USD | `2 orders` | `-0.08%` | `-` |
| `BID` | `703.83` | `319000000.0000` | 224.52 USD | 98,912.07 USD | `1 orders` | `-0.08%` | `-` |
| `BID` | `703.84` | `7768000000.0000` | 5,467.43 USD | 98,687.54 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `703.85` | `45671000000.0000` | 32,145.53 USD | 93,220.12 USD | `2 orders` | `-0.07%` | `-` |
| `BID` | `703.86` | `5139000000.0000` | 3,617.14 USD | 61,074.58 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `703.88` | `5139000000.0000` | 3,617.24 USD | 57,457.45 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `703.90` | `6183000000.0000` | 4,352.21 USD | 53,840.21 USD | `2 orders` | `-0.07%` | `-` |
| `BID` | `703.96` | `4176000000.0000` | 2,939.74 USD | 49,487.99 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `703.97` | `6746000000.0000` | 4,748.98 USD | 46,548.26 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `703.99` | `2500000000.0000` | 1,759.97 USD | 41,799.27 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `704.05` | `3853000000.0000` | 2,712.70 USD | 40,039.30 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `704.08` | `1000000000.0000` | 704.08 USD | 37,326.59 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `704.10` | `9313000000.0000` | 6,557.28 USD | 36,622.51 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `704.13` | `334000000.0000` | 235.18 USD | 30,065.23 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `704.14` | `5138000000.0000` | 3,617.87 USD | 29,830.05 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `704.22` | `12825000000.0000` | 9,031.62 USD | 26,212.18 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `704.23` | `8000000000.0000` | 5,633.84 USD | 17,180.56 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `704.24` | `16396000000.0000` | 11,546.72 USD | 11,546.72 USD | `3 orders` | `-0.02%` | `-` |
| `MID_SPREAD` | `704.36` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 704.36` | `0.00%` | `-` |
| `ASK` | `704.48` | `1025000000.0000` | 722.09 USD | 722.09 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `704.53` | `5139000000.0000` | 3,620.58 USD | 4,342.67 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `704.55` | `5139000000.0000` | 3,620.68 USD | 7,963.35 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `704.58` | `3854000000.0000` | 2,715.45 USD | 10,678.81 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `704.61` | `5468000000.0000` | 3,852.81 USD | 14,531.61 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `704.63` | `97000000.0000` | 68.35 USD | 14,599.96 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `704.65` | `5139000000.0000` | 3,621.20 USD | 18,221.16 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `704.66` | `5152000000.0000` | 3,630.41 USD | 21,851.57 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `704.71` | `150000000.0000` | 105.71 USD | 21,957.27 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `704.72` | `5288000000.0000` | 3,726.56 USD | 25,683.83 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `704.73` | `7682000000.0000` | 5,413.74 USD | 31,097.57 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `704.74` | `150000000.0000` | 105.71 USD | 31,203.28 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `704.75` | `7277000000.0000` | 5,128.47 USD | 36,331.75 USD | `3 orders` | `+0.06%` | `-` |
| `ASK` | `704.76` | `994000000.0000` | 700.53 USD | 37,032.28 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `704.78` | `3853000000.0000` | 2,715.52 USD | 39,747.79 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `704.80` | `8082000000.0000` | 5,696.19 USD | 45,443.99 USD | `2 orders` | `+0.06%` | `-` |
| `ASK` | `704.82` | `1793000000.0000` | 1,263.74 USD | 46,707.73 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `704.85` | `11767000000.0000` | 8,293.97 USD | 55,001.70 USD | `2 orders` | `+0.07%` | `-` |
| `ASK` | `704.88` | `709000000.0000` | 499.76 USD | 55,501.46 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `704.90` | `1214000000.0000` | 855.75 USD | 56,357.21 USD | `2 orders` | `+0.08%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:46:31 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `792` | `0xea00...a918` | `LONG` | 2,869,228.17 USD | `4,098,429,000,000.00` | `787.24` | `701.46` | `0.000000` | -357,198.61 USD | `-12.45%` | `5X Cross` |
| `868` | `0xb23b...4852` | `SHORT` | 2,596,197.26 USD | `3,703,087,000,000.00` | `702.34` | `701.46` | `3605.96` | 4,638.54 USD | `+0.18%` | `5X Cross` |
| `927` | `0xfe7c...b7ae` | `LONG` | 2,442,670.95 USD | `3,491,575,000,000.00` | `686.05` | `701.46` | `0.000000` | 47,260.09 USD | `+1.93%` | `10X Cross` |
| `949` | `0x7d0c...1b28` | `LONG` | 2,384,501.14 USD | `3,404,582,000,000.00` | `704.38` | `701.46` | `0.000000` | -13,630.57 USD | `-0.57%` | `10X Cross` |
| `1047` | `0x39b4...5c34` | `SHORT` | 2,119,894.66 USD | `3,025,007,000,000.00` | `707.72` | `701.46` | `840.65` | 20,948.54 USD | `+0.99%` | `10X Cross` |
| `1203` | `0x7737...bf66` | `SHORT` | 1,866,164.82 USD | `2,646,179,000,000.00` | `752.73` | `701.46` | `6675.35` | 125,705.77 USD | `+6.74%` | `10X Cross` |
| `1298` | `0x5b67...c66a` | `SHORT` | 1,703,499.38 USD | `2,429,891,000,000.00` | `691.70` | `701.46` | `951.06` | -22,740.95 USD | `-1.33%` | `10X Cross` |
| `1327` | `0x646b...01dc` | `SHORT` | 1,654,015.35 USD | `2,360,687,000,000.00` | `699.94` | `701.46` | `1053.11` | -1,671.92 USD | `-0.10%` | `10X Cross` |
| `1349` | `0xc675...795d` | `LONG` | 1,634,144.95 USD | `2,335,694,000,000.00` | `706.91` | `701.46` | `651.24` | -16,972.92 USD | `-1.04%` | `10X Cross` |
| `1435` | `0xab04...8b69` | `SHORT` | 1,538,038.20 USD | `2,198,328,000,000.00` | `696.91` | `701.46` | `1046.78` | -5,996.03 USD | `-0.39%` | `10X Cross` |
| `1475` | `0x4420...4c4b` | `LONG` | 1,483,793.12 USD | `2,121,068,000,000.00` | `704.34` | `701.46` | `340.24` | -10,167.24 USD | `-0.69%` | `10X Cross` |
| `1510` | `0x2edd...8179` | `LONG` | 1,445,276.53 USD | `2,063,590,000,000.00` | `714.56` | `701.46` | `0.000000` | -29,284.90 USD | `-2.03%` | `10X Cross` |
| `1557` | `0x325e...9564` | `LONG` | 1,400,740.00 USD | `2,000,000,000,000.00` | `713.23` | `701.46` | `0.000000` | -25,719.80 USD | `-1.84%` | `10X Cross` |
| `1643` | `0x51f6...2b39` | `LONG` | 1,301,998.25 USD | `1,856,682,000,000.00` | `703.21` | `701.46` | `0.000000` | -3,633.03 USD | `-0.28%` | `10X Cross` |
| `1680` | `0xb69e...033a` | `LONG` | 1,256,312.06 USD | `1,795,655,000,000.00` | `772.94` | `701.46` | `647.07` | -131,619.65 USD | `-10.48%` | `10X Cross` |
| `1729` | `0x07fd...689d` | `LONG` | 1,222,321.34 USD | `1,744,292,000,000.00` | `714.81` | `701.46` | `0.000000` | -24,524.46 USD | `-2.01%` | `10X Cross` |
| `1740` | `0x645b...87b8` | `LONG` | 1,206,896.29 USD | `1,721,457,000,000.00` | `747.36` | `701.46` | `0.000000` | -79,647.48 USD | `-6.60%` | `10X Cross` |
| `1778` | `0xfc27...9d9d` | `LONG` | 1,172,858.37 USD | `1,672,907,000,000.00` | `701.09` | `701.46` | `0.000000` | 5.25 USD | `+0.00%` | `10X Cross` |
| `1793` | `0xd4c1...3d1d` | `LONG` | 1,158,322.84 USD | `1,651,138,000,000.00` | `704.19` | `701.46` | `0.000000` | -4,396.24 USD | `-0.38%` | `10X Cross` |
| `1861` | `0x023a...2355` | `LONG` | 1,102,446.11 USD | `1,574,091,000,000.00` | `714.42` | `701.46` | `0.000000` | -22,115.95 USD | `-2.01%` | `10X Cross` |
| `1920` | `0x14c6...b280` | `SHORT` | 1,050,570.00 USD | `1,500,000,000,000.00` | `712.51` | `701.46` | `1462.97` | 18,191.70 USD | `+1.73%` | `10X Cross` |
| `1973` | `0xbf5a...88ba` | `SHORT` | 1,012,453.54 USD | `1,439,105,000,000.00` | `718.16` | `701.46` | `1957.63` | 21,053.41 USD | `+2.08%` | `10X Cross` |
| `1986` | `0xa4a6...46cf` | `SHORT` | 1,007,148.41 USD | `1,437,141,000,000.00` | `713.79` | `701.46` | `1969.93` | 18,664.66 USD | `+1.85%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `753.58` | 24,098.73 USD | `-` | `NEWS_INTEL` | `-` | #BNB Whale BUY: 24.10K USD at 753.5800 USD [API] | `2026-10-28 20:38:06` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`758.49` (Vol: 2,400,000.00 USD, Dist: `+7.87%`) | Long MP=`677.61` (Vol: 3,100,000.00 USD, Dist: `--3.63%`)
  * 48H Horizon: Short MP=`767.93` (Vol: 3,000,000.00 USD, Dist: `+9.21%`) | Long MP=`677.29` (Vol: 3,100,000.00 USD, Dist: `--3.68%`)
  * 3D Horizon: Short MP=`767.93` (Vol: 3,400,000.00 USD, Dist: `+9.21%`) | Long MP=`677.29` (Vol: 3,100,000.00 USD, Dist: `--3.68%`)
  * 7D Horizon: Short MP=`767.93` (Vol: 3,500,000.00 USD, Dist: `+9.21%`) | Long MP=`677.29` (Vol: 3,100,000.00 USD, Dist: `--3.68%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `141.50` | 5,340.00 USD | 7,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `142.50` | 174.28 USD | 7,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `143.50` | 2,870.00 USD | 7,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `145.50` | 87,300.00 USD | 7,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `147.50` | 2,060.00 USD | 7,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `148.50` | 1,100.00 USD | 7,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `157.50` | 787.50 USD | 7,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `161.50` | 1,940.00 USD | 7,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `166.50` | 474.03 USD | 7,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `170.50` | 308.43 USD | 7,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `175.50` | 120.57 USD | 7,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `176.50` | 17,650.00 USD | 7,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `177.50` | 1,070.00 USD | 7,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `178.50` | 239.90 USD | 7,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `190.50` | 1,710.00 USD | 7,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `201.50` | 247.24 USD | 7,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `209.50` | 4,790.00 USD | 7,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `219.50` | 191.18 USD | 7,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `222.50` | 273.45 USD | 7,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `226.50` | 160.36 USD | 7,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `227.50` | 7,760.00 USD | 7,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `246.50` | 138.78 USD | 7,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `247.50` | 17,120.00 USD | 7,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `248.50` | 255.21 USD | 7,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `250.50` | 17,400.00 USD | 7,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `256.50` | 381.93 USD | 7,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `259.50` | 259,500.00 USD | 7,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `264.50` | 1,400.00 USD | 7,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `266.50` | 21,130.00 USD | 7,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `272.50` | 414.47 USD | 7,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `283.50` | 402.57 USD | 7,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `286.50` | 20,050.00 USD | 7,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `292.50` | 7,270.00 USD | 7,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `293.50` | 2,090.00 USD | 7,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `302.50` | 38,940.00 USD | 7,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `311.50` | 1,960.00 USD | 7,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `313.50` | 501.60 USD | 7,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `324.50` | 658,720.00 USD | 7,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `325.50` | 432.59 USD | 6,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `326.50` | 500.85 USD | 6,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `327.50` | 314.07 USD | 6,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `328.50` | 3,240.00 USD | 6,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `330.50` | 9,410.00 USD | 6,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `332.50` | 174,060.00 USD | 6,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `333.50` | 226.45 USD | 6,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `334.50` | 118.08 USD | 6,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `336.50` | 14,300.00 USD | 6,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `338.50` | 936.63 USD | 6,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `343.50` | 652.65 USD | 6,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `348.50` | 1,100.00 USD | 6,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `358.50` | 717.00 USD | 6,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `359.50` | 212.10 USD | 6,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `360.50` | 1,620.00 USD | 6,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `361.50` | 6,350.00 USD | 6,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `364.50` | 863.87 USD | 6,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `366.50` | 2,110.00 USD | 6,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `370.50` | 1,220.00 USD | 6,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `372.50` | 10,930.00 USD | 6,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `374.50` | 1,820.00 USD | 6,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `377.50` | 1,400.00 USD | 6,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `379.50` | 152,450.00 USD | 6,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `382.50` | 1,910.00 USD | 6,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `383.50` | 10,900.00 USD | 6,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `384.50` | 7,970.00 USD | 6,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `385.50` | 1,800.00 USD | 6,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `386.50` | 531.44 USD | 6,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `387.50` | 392.54 USD | 6,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `388.50` | 912.98 USD | 6,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `393.50` | 103.88 USD | 6,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `394.50` | 168.06 USD | 6,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `395.50` | 2,110.00 USD | 6,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `396.50` | 610.21 USD | 6,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `397.50` | 318.00 USD | 6,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `398.50` | 523.63 USD | 6,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `399.50` | 603.64 USD | 6,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `402.50` | 173.07 USD | 6,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `404.50` | 102.34 USD | 6,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `408.50` | 1,290.00 USD | 6,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `410.50` | 614.52 USD | 6,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `411.50` | 106.17 USD | 6,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `412.50` | 3,490.00 USD | 6,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `413.50` | 1,600.00 USD | 6,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `414.50` | 15,830.00 USD | 6,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `415.50` | 1,810.00 USD | 6,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `417.50` | 7,140.00 USD | 6,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `418.50` | 465.79 USD | 6,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `420.50` | 10,650.00 USD | 6,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `421.50` | 2,320.00 USD | 6,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `422.50` | 1,380.00 USD | 6,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `423.50` | 1,450.00 USD | 6,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `429.50` | 636.52 USD | 6,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `430.50` | 30,140.00 USD | 6,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `432.50` | 4,500.00 USD | 6,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `438.50` | 1,790.00 USD | 6,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `453.50` | 7,610.00 USD | 6,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `456.50` | 4,730.00 USD | 6,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `469.50` | 4,370.00 USD | 6,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `475.50` | 5,320.00 USD | 6,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `477.50` | 827.99 USD | 6,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `481.50` | 2,620.00 USD | 6,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `482.50` | 6,840.00 USD | 6,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `484.50` | 158.43 USD | 6,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `485.50` | 137,560.00 USD | 6,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `486.50` | 486.50 USD | 5,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `487.50` | 204.75 USD | 5,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `488.50` | 257.44 USD | 5,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `489.50` | 6,030.00 USD | 5,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `492.50` | 50,740.00 USD | 5,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `493.50` | 3,270.00 USD | 5,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `494.50` | 669.06 USD | 5,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `495.50` | 386.99 USD | 5,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `497.50` | 712.42 USD | 5,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `498.50` | 60,560.00 USD | 5,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `499.50` | 10,510.00 USD | 5,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `500.50` | 41,620.00 USD | 5,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `501.50` | 8,520.00 USD | 5,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `502.50` | 109.04 USD | 5,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `505.50` | 46,410.00 USD | 5,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `508.50` | 992.08 USD | 5,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `509.50` | 3,100.00 USD | 5,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `510.50` | 4,840.00 USD | 5,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `511.50` | 4,090.00 USD | 5,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `512.50` | 5,190.00 USD | 5,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `514.50` | 4,010.00 USD | 5,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `515.50` | 3,930.00 USD | 5,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `516.50` | 2,550.00 USD | 5,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `517.50` | 23,350.00 USD | 5,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `518.50` | 7,540.00 USD | 5,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `519.50` | 968.35 USD | 5,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `520.50` | 272.22 USD | 5,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `521.50` | 838.05 USD | 5,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `523.50` | 2,090.00 USD | 5,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `524.50` | 1,120.00 USD | 5,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `525.50` | 835.02 USD | 5,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `526.50` | 1,700.00 USD | 5,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `527.50` | 555.99 USD | 5,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `529.50` | 42,820.00 USD | 5,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `530.50` | 17,900.00 USD | 5,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `531.50` | 149.35 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `532.50` | 632.08 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `534.50` | 1,350.00 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `535.50` | 100.14 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `537.50` | 268.75 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `539.50` | 490.94 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `541.50` | 472.19 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `543.50` | 2,000.00 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `545.50` | 212,800.00 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `547.50` | 815.23 USD | 5,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `548.50` | 1,580.00 USD | 5,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `549.50` | 3,300.00 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `550.50` | 633.63 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `551.50` | 957.96 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `552.50` | 10,220.00 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `553.50` | 2,730.00 USD | 5,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `554.50` | 2,250.00 USD | 5,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `555.50` | 274.97 USD | 5,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `557.50` | 15,700.00 USD | 5,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `558.50` | 212.23 USD | 5,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `560.50` | 471.38 USD | 5,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `561.50` | 583.40 USD | 5,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `565.50` | 24,810.00 USD | 5,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `566.50` | 160,720.00 USD | 5,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `569.50` | 144.08 USD | 5,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `570.50` | 1,710.00 USD | 5,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `571.50` | 712,450.00 USD | 5,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `572.50` | 9,830.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `574.50` | 323.44 USD | 4,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `576.50` | 5,760.00 USD | 4,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `578.50` | 7,640.00 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `581.50` | 35,070.00 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `582.50` | 274.94 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `584.50` | 3,380.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `586.50` | 2,650.00 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `587.50` | 105.75 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `590.50` | 9,330.00 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `592.50` | 255,620.00 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `593.50` | 209.51 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `594.50` | 45,480.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `595.50` | 10,090.00 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `597.50` | 311.30 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `598.50` | 101.75 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `599.50` | 4,430.00 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `600.50` | 945.19 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `601.50` | 16,880.00 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `603.50` | 58,220.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `604.50` | 2,080.00 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `605.50` | 3,220.00 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `606.50` | 1,230.00 USD | 3,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `607.50` | 650.03 USD | 3,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `608.50` | 170.38 USD | 3,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `610.50` | 213.67 USD | 3,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `612.50` | 1,580.00 USD | 3,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `613.50` | 12,270.00 USD | 3,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `614.50` | 1,440.00 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `615.50` | 8,870.00 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `616.50` | 13,520.00 USD | 3,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `617.50` | 156.23 USD | 3,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `618.50` | 280.18 USD | 3,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `620.50` | 5,410.00 USD | 3,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `621.50` | 3,230.00 USD | 3,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `624.50` | 3,460.00 USD | 3,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `625.50` | 25,330.00 USD | 3,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `627.50` | 326.30 USD | 3,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `629.50` | 251,890.00 USD | 3,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `630.50` | 16,960.00 USD | 3,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `630.80` | 38,600,000.00 USD | 38,600,000.00 USD | 0.00 USD | 44,070.00 USD | 318,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `631.70` | 38,230,000.00 USD | 38,230,000.00 USD | 28,120.00 USD | 49,490.00 USD | 557,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `632.50` | 3,560.00 USD | 3,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `632.60` | 37,600,000.00 USD | 37,600,000.00 USD | 575,630.00 USD | 54,360.00 USD | 40,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `633.50` | 36,930,000.00 USD | 36,930,000.00 USD | 7,730.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `633.50` | 1,090.00 USD | 3,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `634.40` | 36,920,000.00 USD | 36,920,000.00 USD | 20,270.00 USD | 23,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `635.30` | 36,880,000.00 USD | 36,880,000.00 USD | 0.00 USD | 0.00 USD | 76,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `635.50` | 6,070.00 USD | 3,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `636.20` | 36,800,000.00 USD | 36,800,000.00 USD | 0.00 USD | 40,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `637.10` | 36,760,000.00 USD | 36,760,000.00 USD | 101,910.00 USD | 0.00 USD | 236,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `637.50` | 1,150,000.00 USD | 3,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `638.50` | 432.90 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `638.90` | 36,420,000.00 USD | 36,420,000.00 USD | 145,780.00 USD | 37,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `639.50` | 2,730.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `639.80` | 36,240,000.00 USD | 36,240,000.00 USD | 38,320.00 USD | 0.00 USD | 184,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `640.50` | 116,220.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `641.50` | 1,670.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `641.60` | 36,010,000.00 USD | 36,010,000.00 USD | 33,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `642.50` | 35,980,000.00 USD | 35,980,000.00 USD | 116,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `642.50` | 8,970.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `644.30` | 35,860,000.00 USD | 35,860,000.00 USD | 308,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `644.50` | 9,660.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `645.20` | 35,560,000.00 USD | 35,560,000.00 USD | 0.00 USD | 0.00 USD | 341,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `645.50` | 2,070.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `646.10` | 35,210,000.00 USD | 35,210,000.00 USD | 87,020.00 USD | 0.00 USD | 140,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `646.50` | 2,250.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `647.00` | 34,990,000.00 USD | 34,990,000.00 USD | 158,720.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `647.90` | 34,830,000.00 USD | 34,830,000.00 USD | 78,540.00 USD | 29,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `648.80` | 34,720,000.00 USD | 34,720,000.00 USD | 92,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `649.50` | 1,120.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `650.50` | 2,930.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `651.50` | 34,630,000.00 USD | 34,630,000.00 USD | 106,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `651.50` | 1,520,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `652.40` | 34,520,000.00 USD | 34,520,000.00 USD | 0.00 USD | 0.00 USD | 94,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `652.50` | 1,420.00 USD | 720,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `653.30` | 34,430,000.00 USD | 34,430,000.00 USD | 0.00 USD | 26,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `653.50` | 298.00 USD | 718,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `654.20` | 34,400,000.00 USD | 34,400,000.00 USD | 73,900.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `654.50` | 97,530.00 USD | 718,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `655.10` | 34,330,000.00 USD | 34,330,000.00 USD | 88,130.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `655.50` | 122.58 USD | 620,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `656.00` | 34,240,000.00 USD | 34,240,000.00 USD | 120,150.00 USD | 0.00 USD | 87,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `656.90` | 34,030,000.00 USD | 34,030,000.00 USD | 76,140.00 USD | 21,320.00 USD | 738,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `657.80` | 33,190,000.00 USD | 33,190,000.00 USD | 833,200.00 USD | 14,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `658.50` | 937.05 USD | 620,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `658.70` | 32,350,000.00 USD | 32,350,000.00 USD | 81,060.00 USD | 0.00 USD | 81,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `659.50` | 157,470.00 USD | 619,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `659.60` | 32,180,000.00 USD | 32,180,000.00 USD | 0.00 USD | 7,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `660.50` | 32,180,000.00 USD | 32,180,000.00 USD | 90,670.00 USD | 0.00 USD | 14,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `660.50` | 48,030.00 USD | 462,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `661.40` | 32,070,000.00 USD | 32,070,000.00 USD | 439,070.00 USD | 83,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `661.50` | 101,450.00 USD | 414,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `662.30` | 31,550,000.00 USD | 31,550,000.00 USD | 6,140.00 USD | 87,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `662.50` | 1,530.00 USD | 312,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `663.20` | 31,450,000.00 USD | 31,450,000.00 USD | 202,560.00 USD | 5,000.00 USD | 19,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `663.50` | 2,200.00 USD | 311,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `664.10` | 31,230,000.00 USD | 31,230,000.00 USD | 45,960.00 USD | 48,410.00 USD | 21,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `664.10` | 87,050,000.00 USD | 87,050,000.00 USD | 78,740.00 USD | 18,740.00 USD | 39,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `664.50` | 47,690.00 USD | 309,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `665.00` | 31,110,000.00 USD | 31,110,000.00 USD | 1,160,000.00 USD | 0.00 USD | 8,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `665.00` | 86,910,000.00 USD | 86,910,000.00 USD | 92,030.00 USD | 22,990.00 USD | 37,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `665.50` | 2,230.00 USD | 261,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `665.90` | 29,940,000.00 USD | 29,940,000.00 USD | 682,590.00 USD | 93,330.00 USD | 688,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `665.90` | 86,760,000.00 USD | 86,760,000.00 USD | 264,020.00 USD | 71,380.00 USD | 63,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `666.50` | 49,980.00 USD | 259,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `666.80` | 28,480,000.00 USD | 28,480,000.00 USD | 805,530.00 USD | 13,270.00 USD | 11,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `666.80` | 86,360,000.00 USD | 86,360,000.00 USD | 198,550.00 USD | 33,320.00 USD | 61,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `667.50` | 5,740.00 USD | 209,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `667.70` | 27,650,000.00 USD | 27,650,000.00 USD | 181,040.00 USD | 115,700.00 USD | 9,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `667.70` | 86,070,000.00 USD | 86,070,000.00 USD | 199,690.00 USD | 45,130.00 USD | 51,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `668.50` | 20,730.00 USD | 203,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `668.60` | 27,340,000.00 USD | 27,340,000.00 USD | 581,120.00 USD | 25,520.00 USD | 3,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `668.60` | 85,770,000.00 USD | 85,770,000.00 USD | 387,530.00 USD | 92,860.00 USD | 51,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `669.50` | 26,730,000.00 USD | 26,730,000.00 USD | 116,800.00 USD | 61,020.00 USD | 10,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `669.50` | 85,240,000.00 USD | 85,240,000.00 USD | 341,150.00 USD | 38,130.00 USD | 108,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `669.50` | 4,240.00 USD | 182,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `670.40` | 26,540,000.00 USD | 26,540,000.00 USD | 255,530.00 USD | 0.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `670.40` | 84,750,000.00 USD | 84,750,000.00 USD | 319,660.00 USD | 93,800.00 USD | 77,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `670.50` | 100,710.00 USD | 178,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `671.30` | 24,810,000.00 USD | 24,810,000.00 USD | 124,990.00 USD | 11,440.00 USD | 16,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `671.30` | 84,260,000.00 USD | 84,260,000.00 USD | 335,750.00 USD | 57,500.00 USD | 42,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `671.50` | 6,100.00 USD | 77,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `672.20` | 24,660,000.00 USD | 24,660,000.00 USD | 1,990,000.00 USD | 8,400.00 USD | 29,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `672.20` | 83,830,000.00 USD | 83,830,000.00 USD | 180,230.00 USD | 62,620.00 USD | 74,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `672.50` | 16,260.00 USD | 71,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `673.10` | 22,630,000.00 USD | 22,630,000.00 USD | 348,680.00 USD | 259,540.00 USD | 824,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `673.10` | 83,510,000.00 USD | 83,510,000.00 USD | 394,120.00 USD | 64,970.00 USD | 42,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `673.50` | 6,860.00 USD | 55,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `674.00` | 21,190,000.00 USD | 21,190,000.00 USD | 305,330.00 USD | 90,530.00 USD | 1,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `674.00` | 83,010,000.00 USD | 83,010,000.00 USD | 335,670.00 USD | 105,910.00 USD | 80,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `674.50` | 2,910.00 USD | 48,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `674.90` | 19,240,000.00 USD | 19,240,000.00 USD | 1,270,000.00 USD | 366,740.00 USD | 431,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `674.90` | 82,490,000.00 USD | 82,490,000.00 USD | 247,070.00 USD | 31,490.00 USD | 44,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `675.50` | 23,760.00 USD | 45,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `675.80` | 17,180,000.00 USD | 17,180,000.00 USD | 1,010,000.00 USD | 33,210.00 USD | 209,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `675.80` | 82,160,000.00 USD | 82,160,000.00 USD | 387,400.00 USD | 26,020.00 USD | 79,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `676.50` | 922.07 USD | 21,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `676.70` | 15,920,000.00 USD | 15,920,000.00 USD | 359,550.00 USD | 265,020.00 USD | 50,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `676.70` | 81,670,000.00 USD | 81,670,000.00 USD | 509,100.00 USD | 35,490.00 USD | 126,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `677.50` | 983.73 USD | 20,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `677.60` | 15,250,000.00 USD | 15,250,000.00 USD | 350,710.00 USD | 118,540.00 USD | 250,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `677.60` | 81,000,000.00 USD | 81,000,000.00 USD | 409,810.00 USD | 0.00 USD | 63,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `678.50` | 14,530,000.00 USD | 14,530,000.00 USD | 1,030,000.00 USD | 111,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `678.50` | 80,530,000.00 USD | 80,530,000.00 USD | 120,190.00 USD | 0.00 USD | 26,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `679.40` | 13,390,000.00 USD | 13,390,000.00 USD | 1,200,000.00 USD | 9,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `679.40` | 80,380,000.00 USD | 80,380,000.00 USD | 116,510.00 USD | 10,480.00 USD | 40,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `679.50` | 2,110.00 USD | 19,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `680.30` | 12,180,000.00 USD | 12,180,000.00 USD | 0.00 USD | 157,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `680.30` | 80,210,000.00 USD | 80,210,000.00 USD | 166,780.00 USD | 13,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `680.50` | 2,010.00 USD | 17,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `681.20` | 12,020,000.00 USD | 12,020,000.00 USD | 13,940.00 USD | 167,420.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `681.20` | 80,030,000.00 USD | 80,030,000.00 USD | 106,280.00 USD | 7,050.00 USD | 35,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `681.50` | 11,580.00 USD | 15,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `682.10` | 11,840,000.00 USD | 11,840,000.00 USD | 33,390.00 USD | 232,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `682.10` | 79,880,000.00 USD | 79,880,000.00 USD | 0.00 USD | 23,360.00 USD | 27,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `683.00` | 11,580,000.00 USD | 11,580,000.00 USD | 120,530.00 USD | 11,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `683.00` | 79,830,000.00 USD | 79,830,000.00 USD | 175,930.00 USD | 28,470.00 USD | 11,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `683.50` | 2,920.00 USD | 2,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `683.90` | 11,440,000.00 USD | 11,440,000.00 USD | 19,970.00 USD | 157,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `683.90` | 79,620,000.00 USD | 79,620,000.00 USD | 77,000.00 USD | 29,510.00 USD | 17,480.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `684.50` | 2,110.00 USD | 5,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `684.80` | 79,490,000.00 USD | 79,490,000.00 USD | 246,080.00 USD | 9,850.00 USD | 39,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `685.70` | 11,270,000.00 USD | 11,270,000.00 USD | 684,860.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `685.70` | 79,200,000.00 USD | 79,200,000.00 USD | 197,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `686.60` | 10,580,000.00 USD | 10,580,000.00 USD | 9,210.00 USD | 46,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `686.60` | 79,000,000.00 USD | 79,000,000.00 USD | 62,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `687.50` | 10,530,000.00 USD | 10,530,000.00 USD | 775,320.00 USD | 467,830.00 USD | 4,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `687.50` | 78,940,000.00 USD | 78,940,000.00 USD | 148,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `688.40` | 5,180,000.00 USD | 5,180,000.00 USD | 303,890.00 USD | 105,130.00 USD | 282,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `688.40` | 78,790,000.00 USD | 78,790,000.00 USD | 67,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `688.50` | 146.65 USD | 4,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `689.30` | 4,490,000.00 USD | 4,490,000.00 USD | 2,200,000.00 USD | 72,370.00 USD | 784,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `689.30` | 78,720,000.00 USD | 78,720,000.00 USD | 84,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `689.50` | 4,080.00 USD | 4,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `690.20` | 1,430,000.00 USD | 1,430,000.00 USD | 242,130.00 USD | 146,030.00 USD | 234,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `690.20` | 78,640,000.00 USD | 78,640,000.00 USD | 283,920.00 USD | 63,230.00 USD | 82,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `691.10` | 810,760.00 USD | 810,760.00 USD | 167,270.00 USD | 0.00 USD | 306,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `691.10` | 78,210,000.00 USD | 78,210,000.00 USD | 362,020.00 USD | 61,370.00 USD | 81,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `692.00` | 337,440.00 USD | 337,440.00 USD | 5,650.00 USD | 0.00 USD | 194,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `692.00` | 77,700,000.00 USD | 77,700,000.00 USD | 322,430.00 USD | 18,850.00 USD | 58,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `692.90` | 77,300,000.00 USD | 77,300,000.00 USD | 280,830.00 USD | 19,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `693.80` | 77,000,000.00 USD | 77,000,000.00 USD | 305,720.00 USD | 39,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `694.70` | 76,660,000.00 USD | 76,660,000.00 USD | 279,840.00 USD | 36,640.00 USD | 35,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `695.60` | 137,440.00 USD | 137,440.00 USD | 0.00 USD | 137,440.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `695.60` | 76,300,000.00 USD | 76,300,000.00 USD | 120,440.00 USD | 0.00 USD | 21,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `696.50` | 76,160,000.00 USD | 76,160,000.00 USD | 140,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `697.40` | 76,020,000.00 USD | 76,020,000.00 USD | 189,100.00 USD | 19,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `698.30` | 75,810,000.00 USD | 75,810,000.00 USD | 273,520.00 USD | 33,120.00 USD | 54,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `699.20` | 75,450,000.00 USD | 75,450,000.00 USD | 274,810.00 USD | 12,670.00 USD | 11,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `700.10` | 75,150,000.00 USD | 75,150,000.00 USD | 225,450.00 USD | 40,820.00 USD | 27,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `701.00` | 74,860,000.00 USD | 74,860,000.00 USD | 237,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `701.90` | 74,620,000.00 USD | 74,620,000.00 USD | 135,260.00 USD | 41,260.00 USD | 89,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `702.80` | 74,360,000.00 USD | 74,360,000.00 USD | 416,820.00 USD | 57,470.00 USD | 36,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `703.70` | 73,840,000.00 USD | 73,840,000.00 USD | 311,800.00 USD | 44,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `704.50` | 213.46 USD | 5,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `704.60` | 73,490,000.00 USD | 73,490,000.00 USD | 537,050.00 USD | 136,550.00 USD | 194,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `705.50` | 96,830.00 USD | 96,830.00 USD | 0.00 USD | 96,830.00 USD | 0.00 USD | `Tier 1 CEX` |
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
| `1D` | `Short Liquidation` | `715.40` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 513,890.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `715.40` | 59,400,000.00 USD | 59,400,000.00 USD | 1,050,000.00 USD | 419,310.00 USD | 329,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `716.30` | 2,780,000.00 USD | 2,780,000.00 USD | 303,890.00 USD | 345,920.00 USD | 282,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `716.30` | 57,600,000.00 USD | 57,600,000.00 USD | 1,080,000.00 USD | 324,540.00 USD | 233,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `717.20` | 3,960,000.00 USD | 3,960,000.00 USD | 268,080.00 USD | 129,470.00 USD | 784,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `717.20` | 55,960,000.00 USD | 55,960,000.00 USD | 581,610.00 USD | 398,030.00 USD | 387,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `718.10` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 115,870.00 USD | 234,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `718.10` | 54,590,000.00 USD | 54,590,000.00 USD | 1,690,000.00 USD | 246,320.00 USD | 151,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `719.00` | 4,750,000.00 USD | 4,750,000.00 USD | 271,410.00 USD | 166,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `719.00` | 52,510,000.00 USD | 52,510,000.00 USD | 670,390.00 USD | 137,460.00 USD | 211,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `719.90` | 5,250,000.00 USD | 5,250,000.00 USD | 0.00 USD | 0.00 USD | 500,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `719.90` | 51,490,000.00 USD | 51,490,000.00 USD | 618,020.00 USD | 173,240.00 USD | 186,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `720.80` | 5,450,000.00 USD | 5,450,000.00 USD | 0.00 USD | 204,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `720.80` | 50,510,000.00 USD | 50,510,000.00 USD | 1,010,000.00 USD | 52,490.00 USD | 180,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `721.50` | 8,110.00 USD | 13,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `721.70` | 5,530,000.00 USD | 5,530,000.00 USD | 0.00 USD | 78,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `721.70` | 49,260,000.00 USD | 49,260,000.00 USD | 1,950,000.00 USD | 237,690.00 USD | 653,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `722.50` | 650.97 USD | 14,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `722.60` | 46,430,000.00 USD | 46,430,000.00 USD | 1,930,000.00 USD | 108,200.00 USD | 229,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `723.50` | 5,830,000.00 USD | 5,830,000.00 USD | 0.00 USD | 300,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `723.50` | 44,160,000.00 USD | 44,160,000.00 USD | 640,550.00 USD | 140,550.00 USD | 293,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `723.50` | 23,050.00 USD | 37,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `724.40` | 5,970,000.00 USD | 5,970,000.00 USD | 0.00 USD | 137,440.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `724.40` | 43,080,000.00 USD | 43,080,000.00 USD | 663,550.00 USD | 186,780.00 USD | 130,770.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `724.50` | 1,310.00 USD | 38,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `725.30` | 6,030,000.00 USD | 6,030,000.00 USD | 0.00 USD | 57,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `725.30` | 42,100,000.00 USD | 42,100,000.00 USD | 1,760,000.00 USD | 418,390.00 USD | 396,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `725.50` | 3,600.00 USD | 41,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `726.20` | 39,520,000.00 USD | 39,520,000.00 USD | 1,060,000.00 USD | 311,550.00 USD | 460,020.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `726.50` | 912.48 USD | 42,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `727.10` | 6,090,000.00 USD | 6,090,000.00 USD | 0.00 USD | 64,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `727.10` | 37,690,000.00 USD | 37,690,000.00 USD | 1,230,000.00 USD | 331,980.00 USD | 241,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `727.50` | 10,190.00 USD | 53,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `728.00` | 35,890,000.00 USD | 35,890,000.00 USD | 3,110,000.00 USD | 778,750.00 USD | 388,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `728.50` | 9,860.00 USD | 62,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `728.90` | 6,380,000.00 USD | 6,380,000.00 USD | 0.00 USD | 133,210.00 USD | 158,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `728.90` | 31,610,000.00 USD | 31,610,000.00 USD | 2,330,000.00 USD | 317,590.00 USD | 644,150.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `729.50` | 29,600.00 USD | 92,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `729.80` | 7,060,000.00 USD | 7,060,000.00 USD | 0.00 USD | 147,750.00 USD | 531,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `729.80` | 28,320,000.00 USD | 28,320,000.00 USD | 1,320,000.00 USD | 430,010.00 USD | 339,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `730.50` | 35,390.00 USD | 127,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `730.70` | 11,740,000.00 USD | 11,740,000.00 USD | 2,650,000.00 USD | 152,870.00 USD | 1,880,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `730.70` | 26,230,000.00 USD | 26,230,000.00 USD | 2,760,000.00 USD | 351,520.00 USD | 587,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `731.50` | 110,000.00 USD | 237,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `731.60` | 12,250,000.00 USD | 12,250,000.00 USD | 134,040.00 USD | 82,570.00 USD | 289,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `731.60` | 22,530,000.00 USD | 22,530,000.00 USD | 1,530,000.00 USD | 133,980.00 USD | 261,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `732.50` | 13,570,000.00 USD | 13,570,000.00 USD | 430,780.00 USD | 73,020.00 USD | 820,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `732.50` | 20,610,000.00 USD | 20,610,000.00 USD | 465,880.00 USD | 221,510.00 USD | 96,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `732.50` | 176,420.00 USD | 414,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `733.40` | 14,630,000.00 USD | 14,630,000.00 USD | 703,820.00 USD | 206,790.00 USD | 153,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `733.40` | 19,820,000.00 USD | 19,820,000.00 USD | 1,910,000.00 USD | 158,310.00 USD | 338,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `733.50` | 740,840.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `734.30` | 15,080,000.00 USD | 15,080,000.00 USD | 344,230.00 USD | 0.00 USD | 97,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `734.30` | 17,420,000.00 USD | 17,420,000.00 USD | 1,580,000.00 USD | 288,470.00 USD | 244,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `734.50` | 134,340.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `735.20` | 15,940,000.00 USD | 15,940,000.00 USD | 613,800.00 USD | 246,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `735.20` | 15,310,000.00 USD | 15,310,000.00 USD | 1,330,000.00 USD | 172,940.00 USD | 437,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `735.50` | 78,630.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `736.10` | 17,660,000.00 USD | 17,660,000.00 USD | 1,110,000.00 USD | 22,190.00 USD | 590,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `736.10` | 13,370,000.00 USD | 13,370,000.00 USD | 2,130,000.00 USD | 181,990.00 USD | 484,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `736.50` | 133,540.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `737.00` | 18,060,000.00 USD | 18,060,000.00 USD | 407,440.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `737.00` | 10,570,000.00 USD | 10,570,000.00 USD | 2,360,000.00 USD | 175,330.00 USD | 633,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `737.50` | 45,900.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `737.90` | 18,390,000.00 USD | 18,390,000.00 USD | 160,280.00 USD | 162,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `737.90` | 7,400,000.00 USD | 7,400,000.00 USD | 3,420,000.00 USD | 72,280.00 USD | 374,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `738.50` | 1,060,000.00 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `738.80` | 19,560,000.00 USD | 19,560,000.00 USD | 703,680.00 USD | 0.00 USD | 472,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `738.80` | 3,530,000.00 USD | 3,530,000.00 USD | 522,950.00 USD | 20,210.00 USD | 155,300.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `739.50` | 52,790.00 USD | 2,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `739.70` | 20,620,000.00 USD | 20,620,000.00 USD | 590,480.00 USD | 0.00 USD | 461,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `739.70` | 2,830,000.00 USD | 2,830,000.00 USD | 352,500.00 USD | 0.00 USD | 203,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `740.50` | 17,670.00 USD | 2,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `740.60` | 21,070,000.00 USD | 21,070,000.00 USD | 302,880.00 USD | 134,150.00 USD | 15,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `740.60` | 2,280,000.00 USD | 2,280,000.00 USD | 1,090,000.00 USD | 0.00 USD | 33,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `741.50` | 21,740,000.00 USD | 21,740,000.00 USD | 637,650.00 USD | 32,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `741.50` | 1,160,000.00 USD | 1,160,000.00 USD | 257,630.00 USD | 0.00 USD | 208,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `741.50` | 9,720.00 USD | 2,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `742.40` | 689,850.00 USD | 689,850.00 USD | 0.00 USD | 0.00 USD | 183,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `742.50` | 8,150.00 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `743.30` | 21,860,000.00 USD | 21,860,000.00 USD | 120,950.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `743.30` | 505,930.00 USD | 505,930.00 USD | 0.00 USD | 0.00 USD | 57,580.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `743.50` | 609,320.00 USD | 3,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `744.20` | 22,400,000.00 USD | 22,400,000.00 USD | 0.00 USD | 106,580.00 USD | 436,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `744.20` | 448,350.00 USD | 448,350.00 USD | 0.00 USD | 257,580.00 USD | 141,790.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `744.50` | 29,940.00 USD | 3,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `745.10` | 24,500,000.00 USD | 24,500,000.00 USD | 1,240,000.00 USD | 0.00 USD | 854,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `745.10` | 48,980.00 USD | 48,980.00 USD | 0.00 USD | 48,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `745.50` | 17,630.00 USD | 3,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `746.00` | 24,720,000.00 USD | 24,720,000.00 USD | 115,270.00 USD | 106,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `746.00` | 999,320.00 USD | 999,320.00 USD | 999,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `746.50` | 240,710.00 USD | 3,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `746.90` | 26,020,000.00 USD | 26,020,000.00 USD | 499,560.00 USD | 37,280.00 USD | 758,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `746.90` | 1,210,000.00 USD | 1,210,000.00 USD | 215,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `747.50` | 76,000.00 USD | 3,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `747.80` | 26,560,000.00 USD | 26,560,000.00 USD | 363,640.00 USD | 103,400.00 USD | 73,330.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `748.50` | 22,480.00 USD | 3,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `748.70` | 26,940,000.00 USD | 26,940,000.00 USD | 383,190.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `749.50` | 6,710.00 USD | 3,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `749.60` | 27,310,000.00 USD | 27,310,000.00 USD | 368,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `750.50` | 27,330,000.00 USD | 27,330,000.00 USD | 16,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `750.50` | 172,780.00 USD | 3,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `751.40` | 27,480,000.00 USD | 27,480,000.00 USD | 54,450.00 USD | 0.00 USD | 98,240.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `751.50` | 566,010.00 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `752.30` | 27,980,000.00 USD | 27,980,000.00 USD | 34,030.00 USD | 25,010.00 USD | 441,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `752.50` | 24,800.00 USD | 4,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `753.20` | 28,480,000.00 USD | 28,480,000.00 USD | 246,790.00 USD | 3,810.00 USD | 248,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `753.50` | 26,550.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `754.10` | 28,910,000.00 USD | 28,910,000.00 USD | 321,060.00 USD | 50,610.00 USD | 57,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `755.00` | 29,330,000.00 USD | 29,330,000.00 USD | 208,850.00 USD | 178,540.00 USD | 37,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `755.00` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 59,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `755.50` | 658.04 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `755.90` | 30,050,000.00 USD | 30,050,000.00 USD | 550,450.00 USD | 96,170.00 USD | 66,220.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `756.50` | 3,750.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `756.80` | 30,230,000.00 USD | 30,230,000.00 USD | 110,260.00 USD | 24,970.00 USD | 49,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `756.80` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 47,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `757.70` | 30,750,000.00 USD | 30,750,000.00 USD | 307,310.00 USD | 179,910.00 USD | 32,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `757.70` | 1,910,000.00 USD | 1,910,000.00 USD | 475,510.00 USD | 113,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `758.50` | 16,500.00 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `758.60` | 31,640,000.00 USD | 31,640,000.00 USD | 542,740.00 USD | 74,280.00 USD | 273,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `758.60` | 3,100,000.00 USD | 3,100,000.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `759.50` | 32,860,000.00 USD | 32,860,000.00 USD | 1,150,000.00 USD | 61,100.00 USD | 8,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `759.50` | 6,300.00 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `760.40` | 33,280,000.00 USD | 33,280,000.00 USD | 245,610.00 USD | 97,810.00 USD | 72,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `760.40` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 27,650.00 USD | 42,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `760.50` | 13,580.00 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `761.30` | 34,480,000.00 USD | 34,480,000.00 USD | 858,450.00 USD | 71,050.00 USD | 269,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `761.30` | 3,490,000.00 USD | 3,490,000.00 USD | 10,750.00 USD | 211,960.00 USD | 100,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `761.50` | 541.43 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `762.20` | 35,210,000.00 USD | 35,210,000.00 USD | 336,440.00 USD | 172,280.00 USD | 220,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `762.20` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 699,820.00 USD | 179,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `762.50` | 5,800.00 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `763.10` | 38,270,000.00 USD | 38,270,000.00 USD | 2,310,000.00 USD | 228,320.00 USD | 522,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `763.10` | 7,830,000.00 USD | 7,830,000.00 USD | 2,460,000.00 USD | 590,460.00 USD | 404,720.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `763.50` | 1,140,000.00 USD | 5,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `764.00` | 40,170,000.00 USD | 40,170,000.00 USD | 1,490,000.00 USD | 165,630.00 USD | 248,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `764.00` | 10,270,000.00 USD | 10,270,000.00 USD | 1,590,000.00 USD | 441,980.00 USD | 402,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `764.90` | 41,410,000.00 USD | 41,410,000.00 USD | 863,310.00 USD | 176,560.00 USD | 199,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `764.90` | 12,470,000.00 USD | 12,470,000.00 USD | 1,450,000.00 USD | 352,570.00 USD | 395,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `765.80` | 42,870,000.00 USD | 42,870,000.00 USD | 1,120,000.00 USD | 123,600.00 USD | 218,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `765.80` | 15,460,000.00 USD | 15,460,000.00 USD | 2,470,000.00 USD | 107,550.00 USD | 416,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `766.70` | 45,030,000.00 USD | 45,030,000.00 USD | 1,540,000.00 USD | 213,220.00 USD | 404,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `766.70` | 20,050,000.00 USD | 20,050,000.00 USD | 3,330,000.00 USD | 416,530.00 USD | 842,330.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `767.50` | 15,320.00 USD | 5,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `767.60` | 47,110,000.00 USD | 47,110,000.00 USD | 1,650,000.00 USD | 116,430.00 USD | 311,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `767.60` | 23,430,000.00 USD | 23,430,000.00 USD | 2,790,000.00 USD | 123,530.00 USD | 467,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `768.50` | 48,580,000.00 USD | 48,580,000.00 USD | 1,250,000.00 USD | 71,160.00 USD | 143,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `768.50` | 25,660,000.00 USD | 25,660,000.00 USD | 1,840,000.00 USD | 95,830.00 USD | 281,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `768.50` | 156.77 USD | 5,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `769.40` | 48,970,000.00 USD | 48,970,000.00 USD | 199,400.00 USD | 110,150.00 USD | 84,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `769.40` | 26,810,000.00 USD | 26,810,000.00 USD | 565,780.00 USD | 249,950.00 USD | 333,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `769.50` | 231,890.00 USD | 5,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `770.30` | 49,830,000.00 USD | 49,830,000.00 USD | 687,740.00 USD | 126,040.00 USD | 43,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `770.30` | 29,310,000.00 USD | 29,310,000.00 USD | 1,900,000.00 USD | 240,530.00 USD | 364,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `770.50` | 2,460.00 USD | 5,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `771.20` | 50,740,000.00 USD | 50,740,000.00 USD | 425,330.00 USD | 97,820.00 USD | 386,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `771.20` | 30,770,000.00 USD | 30,770,000.00 USD | 1,050,000.00 USD | 242,570.00 USD | 162,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `771.50` | 32,410.00 USD | 5,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `772.10` | 51,860,000.00 USD | 51,860,000.00 USD | 374,860.00 USD | 100,560.00 USD | 647,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `772.10` | 33,190,000.00 USD | 33,190,000.00 USD | 1,750,000.00 USD | 252,650.00 USD | 419,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `772.50` | 120,390.00 USD | 6,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `773.00` | 53,140,000.00 USD | 53,140,000.00 USD | 999,790.00 USD | 147,690.00 USD | 134,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `773.00` | 35,800,000.00 USD | 35,800,000.00 USD | 1,950,000.00 USD | 325,680.00 USD | 338,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `773.50` | 8,960.00 USD | 6,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `773.90` | 54,440,000.00 USD | 54,440,000.00 USD | 1,090,000.00 USD | 105,330.00 USD | 101,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `773.90` | 37,600,000.00 USD | 37,600,000.00 USD | 1,220,000.00 USD | 276,760.00 USD | 293,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `774.50` | 130.12 USD | 6,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `774.80` | 54,970,000.00 USD | 54,970,000.00 USD | 390,270.00 USD | 90,640.00 USD | 56,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `774.80` | 39,980,000.00 USD | 39,980,000.00 USD | 1,310,000.00 USD | 568,930.00 USD | 502,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `775.50` | 5,300.00 USD | 6,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `775.70` | 55,600,000.00 USD | 55,600,000.00 USD | 392,610.00 USD | 118,020.00 USD | 116,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `775.70` | 42,470,000.00 USD | 42,470,000.00 USD | 1,830,000.00 USD | 470,960.00 USD | 187,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `776.60` | 56,070,000.00 USD | 56,070,000.00 USD | 326,450.00 USD | 34,460.00 USD | 108,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `776.60` | 44,740,000.00 USD | 44,740,000.00 USD | 1,630,000.00 USD | 269,050.00 USD | 378,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `777.50` | 56,930,000.00 USD | 56,930,000.00 USD | 660,150.00 USD | 145,570.00 USD | 54,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `777.50` | 46,480,000.00 USD | 46,480,000.00 USD | 1,350,000.00 USD | 243,990.00 USD | 148,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `777.50` | 209.15 USD | 6,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `778.40` | 58,320,000.00 USD | 58,320,000.00 USD | 949,110.00 USD | 73,550.00 USD | 370,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `778.40` | 48,170,000.00 USD | 48,170,000.00 USD | 1,180,000.00 USD | 307,370.00 USD | 206,530.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `778.50` | 3,200.00 USD | 6,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `779.30` | 59,300,000.00 USD | 59,300,000.00 USD | 750,100.00 USD | 76,680.00 USD | 145,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `779.30` | 49,730,000.00 USD | 49,730,000.00 USD | 1,240,000.00 USD | 188,170.00 USD | 123,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `780.20` | 59,820,000.00 USD | 59,820,000.00 USD | 346,940.00 USD | 126,850.00 USD | 47,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `780.20` | 51,100,000.00 USD | 51,100,000.00 USD | 1,070,000.00 USD | 86,470.00 USD | 218,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `780.50` | 7,800.00 USD | 6,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `781.10` | 60,730,000.00 USD | 60,730,000.00 USD | 628,140.00 USD | 108,280.00 USD | 175,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `781.10` | 52,710,000.00 USD | 52,710,000.00 USD | 1,270,000.00 USD | 90,990.00 USD | 242,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `781.50` | 7,410.00 USD | 6,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `782.00` | 61,860,000.00 USD | 61,860,000.00 USD | 828,040.00 USD | 27,020.00 USD | 276,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `782.00` | 54,610,000.00 USD | 54,610,000.00 USD | 1,510,000.00 USD | 87,670.00 USD | 301,190.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `782.50` | 78,440.00 USD | 6,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `782.90` | 63,020,000.00 USD | 63,020,000.00 USD | 907,340.00 USD | 80,140.00 USD | 176,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `782.90` | 56,600,000.00 USD | 56,600,000.00 USD | 1,750,000.00 USD | 36,140.00 USD | 202,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `783.80` | 63,490,000.00 USD | 63,490,000.00 USD | 429,340.00 USD | 14,770.00 USD | 23,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `783.80` | 57,170,000.00 USD | 57,170,000.00 USD | 508,000.00 USD | 10,100.00 USD | 54,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `784.70` | 64,090,000.00 USD | 64,090,000.00 USD | 544,060.00 USD | 32,520.00 USD | 25,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `784.70` | 57,480,000.00 USD | 57,480,000.00 USD | 208,380.00 USD | 28,260.00 USD | 70,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `785.60` | 64,300,000.00 USD | 64,300,000.00 USD | 179,070.00 USD | 18,950.00 USD | 7,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `785.60` | 58,610,000.00 USD | 58,610,000.00 USD | 1,010,000.00 USD | 54,140.00 USD | 71,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `786.50` | 64,560,000.00 USD | 64,560,000.00 USD | 226,070.00 USD | 15,410.00 USD | 22,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `786.50` | 59,000,000.00 USD | 59,000,000.00 USD | 329,230.00 USD | 30,660.00 USD | 23,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `786.50` | 4,910.00 USD | 6,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `787.40` | 64,950,000.00 USD | 64,950,000.00 USD | 357,300.00 USD | 8,510.00 USD | 24,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `787.40` | 59,580,000.00 USD | 59,580,000.00 USD | 470,050.00 USD | 17,630.00 USD | 91,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `787.50` | 122,290.00 USD | 6,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `788.30` | 65,630,000.00 USD | 65,630,000.00 USD | 221,420.00 USD | 52,300.00 USD | 407,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `788.30` | 59,940,000.00 USD | 59,940,000.00 USD | 202,630.00 USD | 82,380.00 USD | 81,230.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `788.50` | 79,550.00 USD | 6,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `789.20` | 66,010,000.00 USD | 66,010,000.00 USD | 339,590.00 USD | 21,480.00 USD | 18,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `789.20` | 60,780,000.00 USD | 60,780,000.00 USD | 698,830.00 USD | 81,250.00 USD | 55,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `789.50` | 114,990.00 USD | 6,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `790.10` | 66,610,000.00 USD | 66,610,000.00 USD | 403,340.00 USD | 28,260.00 USD | 163,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `790.10` | 61,270,000.00 USD | 61,270,000.00 USD | 299,250.00 USD | 104,360.00 USD | 88,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `791.00` | 66,940,000.00 USD | 66,940,000.00 USD | 248,270.00 USD | 73,780.00 USD | 8,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `791.00` | 62,150,000.00 USD | 62,150,000.00 USD | 693,290.00 USD | 82,870.00 USD | 100,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `791.90` | 67,140,000.00 USD | 67,140,000.00 USD | 204,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `791.90` | 63,030,000.00 USD | 63,030,000.00 USD | 816,380.00 USD | 16,830.00 USD | 46,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `792.80` | 67,280,000.00 USD | 67,280,000.00 USD | 139,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `792.80` | 63,250,000.00 USD | 63,250,000.00 USD | 205,450.00 USD | 0.00 USD | 14,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `793.70` | 67,320,000.00 USD | 67,320,000.00 USD | 32,290.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `793.70` | 63,430,000.00 USD | 63,430,000.00 USD | 184,960.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `794.50` | 7,850.00 USD | 6,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `794.60` | 67,340,000.00 USD | 67,340,000.00 USD | 21,920.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `794.60` | 63,750,000.00 USD | 63,750,000.00 USD | 302,280.00 USD | 15,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `795.50` | 67,380,000.00 USD | 67,380,000.00 USD | 43,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `795.50` | 63,890,000.00 USD | 63,890,000.00 USD | 109,640.00 USD | 14,650.00 USD | 14,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `795.50` | 6,100.00 USD | 6,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `796.40` | 67,510,000.00 USD | 67,510,000.00 USD | 30,090.00 USD | 0.00 USD | 94,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `796.40` | 64,030,000.00 USD | 64,030,000.00 USD | 139,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `796.50` | 301.87 USD | 6,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `797.30` | 67,580,000.00 USD | 67,580,000.00 USD | 71,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `797.30` | 64,090,000.00 USD | 64,090,000.00 USD | 64,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `797.50` | 2,670.00 USD | 6,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `798.20` | 67,660,000.00 USD | 67,660,000.00 USD | 53,320.00 USD | 26,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `798.20` | 64,250,000.00 USD | 64,250,000.00 USD | 155,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `799.10` | 67,670,000.00 USD | 67,670,000.00 USD | 15,950.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `799.10` | 64,290,000.00 USD | 64,290,000.00 USD | 42,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `799.50` | 76,900.00 USD | 6,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `800.00` | 67,680,000.00 USD | 67,680,000.00 USD | 2,840.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `800.00` | 64,400,000.00 USD | 64,400,000.00 USD | 113,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `800.50` | 9,580.00 USD | 6,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `800.90` | 67,690,000.00 USD | 67,690,000.00 USD | 11,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `800.90` | 64,510,000.00 USD | 64,510,000.00 USD | 77,580.00 USD | 8,370.00 USD | 21,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `801.50` | 3,120.00 USD | 6,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `801.80` | 67,800,000.00 USD | 67,800,000.00 USD | 27,250.00 USD | 0.00 USD | 87,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `801.80` | 64,720,000.00 USD | 64,720,000.00 USD | 179,900.00 USD | 16,330.00 USD | 10,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `802.50` | 2,500.00 USD | 6,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `802.70` | 67,820,000.00 USD | 67,820,000.00 USD | 0.00 USD | 21,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `802.70` | 64,730,000.00 USD | 64,730,000.00 USD | 11,220.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `803.50` | 67,900,000.00 USD | 67,900,000.00 USD | 73,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `803.50` | 1,460.00 USD | 6,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `803.60` | 64,760,000.00 USD | 64,760,000.00 USD | 27,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `804.50` | 64,840,000.00 USD | 64,840,000.00 USD | 32,340.00 USD | 18,260.00 USD | 32,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `804.50` | 197,940.00 USD | 6,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `805.40` | 64,910,000.00 USD | 64,910,000.00 USD | 56,700.00 USD | 8,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `805.50` | 2,280.00 USD | 6,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `806.30` | 64,920,000.00 USD | 64,920,000.00 USD | 3,270.00 USD | 12,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `806.50` | 44,210.00 USD | 6,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `807.20` | 64,970,000.00 USD | 64,970,000.00 USD | 39,190.00 USD | 0.00 USD | 11,830.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `807.50` | 3,630.00 USD | 6,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `808.10` | 65,030,000.00 USD | 65,030,000.00 USD | 17,980.00 USD | 5,360.00 USD | 29,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `808.50` | 11,780.00 USD | 6,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `809.00` | 65,110,000.00 USD | 65,110,000.00 USD | 58,620.00 USD | 13,120.00 USD | 13,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `809.50` | 1,040.00 USD | 6,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `809.90` | 65,330,000.00 USD | 65,330,000.00 USD | 178,130.00 USD | 9,760.00 USD | 36,490.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `810.50` | 92,120.00 USD | 6,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `810.80` | 65,420,000.00 USD | 65,420,000.00 USD | 78,030.00 USD | 6,630.00 USD | 5,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `811.70` | 65,480,000.00 USD | 65,480,000.00 USD | 19,210.00 USD | 12,110.00 USD | 29,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `812.50` | 9,310.00 USD | 6,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `812.60` | 65,600,000.00 USD | 65,600,000.00 USD | 68,390.00 USD | 17,450.00 USD | 31,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `813.50` | 65,860,000.00 USD | 65,860,000.00 USD | 147,480.00 USD | 59,640.00 USD | 45,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `814.40` | 66,180,000.00 USD | 66,180,000.00 USD | 218,130.00 USD | 32,770.00 USD | 74,730.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `814.50` | 692.32 USD | 6,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `815.30` | 66,390,000.00 USD | 66,390,000.00 USD | 171,100.00 USD | 24,290.00 USD | 10,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `816.20` | 66,690,000.00 USD | 66,690,000.00 USD | 203,680.00 USD | 44,470.00 USD | 59,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `816.50` | 1,740.00 USD | 6,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `817.10` | 67,090,000.00 USD | 67,090,000.00 USD | 278,420.00 USD | 76,830.00 USD | 42,530.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `817.50` | 9,170.00 USD | 7,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `818.00` | 67,550,000.00 USD | 67,550,000.00 USD | 346,550.00 USD | 48,360.00 USD | 67,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `818.50` | 193,020.00 USD | 7,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `818.90` | 67,790,000.00 USD | 67,790,000.00 USD | 180,470.00 USD | 8,160.00 USD | 47,880.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `819.50` | 11,800.00 USD | 7,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `819.80` | 68,300,000.00 USD | 68,300,000.00 USD | 295,510.00 USD | 101,950.00 USD | 107,190.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `820.50` | 136.20 USD | 7,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `820.70` | 68,600,000.00 USD | 68,600,000.00 USD | 235,990.00 USD | 41,190.00 USD | 24,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `821.50` | 751,050.00 USD | 7,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `821.60` | 68,800,000.00 USD | 68,800,000.00 USD | 86,380.00 USD | 62,620.00 USD | 55,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `822.50` | 69,300,000.00 USD | 69,300,000.00 USD | 394,120.00 USD | 64,970.00 USD | 42,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `823.40` | 69,630,000.00 USD | 69,630,000.00 USD | 213,450.00 USD | 68,530.00 USD | 45,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `823.50` | 81,280.00 USD | 8,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `824.30` | 69,980,000.00 USD | 69,980,000.00 USD | 248,860.00 USD | 58,170.00 USD | 43,880.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `824.50` | 25,880.00 USD | 8,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `825.20` | 70,340,000.00 USD | 70,340,000.00 USD | 277,990.00 USD | 21,630.00 USD | 61,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `826.10` | 70,650,000.00 USD | 70,650,000.00 USD | 223,810.00 USD | 27,390.00 USD | 53,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `827.00` | 71,290,000.00 USD | 71,290,000.00 USD | 494,310.00 USD | 23,200.00 USD | 126,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `827.50` | 8,470.00 USD | 8,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `827.90` | 71,650,000.00 USD | 71,650,000.00 USD | 297,880.00 USD | 0.00 USD | 63,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `828.50` | 26,180.00 USD | 8,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `828.80` | 71,840,000.00 USD | 71,840,000.00 USD | 184,280.00 USD | 0.00 USD | 5,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `829.50` | 505.17 USD | 8,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `829.70` | 71,930,000.00 USD | 71,930,000.00 USD | 43,760.00 USD | 5,190.00 USD | 33,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `830.60` | 72,180,000.00 USD | 72,180,000.00 USD | 221,150.00 USD | 5,300.00 USD | 28,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `831.50` | 72,220,000.00 USD | 72,220,000.00 USD | 37,200.00 USD | 5,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `834.50` | 2,530,000.00 USD | 10,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `836.50` | 61,790.00 USD | 10,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `837.50` | 7,010.00 USD | 10,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `838.50` | 32,210.00 USD | 10,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `839.50` | 11,840.00 USD | 10,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `841.50` | 2,930.00 USD | 10,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `842.50` | 1,900.00 USD | 10,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `843.50` | 173,130.00 USD | 10,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `845.50` | 1,640.00 USD | 10,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `846.50` | 850,780.00 USD | 11,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `848.50` | 289.34 USD | 11,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `849.50` | 78,290.00 USD | 11,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `850.50` | 85,760.00 USD | 11,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `851.50` | 8,520.00 USD | 11,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `852.50` | 105,740.00 USD | 12,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `854.50` | 746.83 USD | 12,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `858.50` | 585,810.00 USD | 12,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `859.50` | 16,380.00 USD | 12,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `865.50` | 21,490.00 USD | 12,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `867.50` | 9,810.00 USD | 12,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `873.50` | 296,410.00 USD | 12,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `874.50` | 35,770.00 USD | 13,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `875.50` | 417.61 USD | 13,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `877.50` | 614,250.00 USD | 13,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `878.50` | 4,390.00 USD | 13,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `879.50` | 145.12 USD | 13,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `883.50` | 319.83 USD | 13,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `884.50` | 17,050.00 USD | 13,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `885.50` | 1,430.00 USD | 13,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `886.50` | 812.92 USD | 13,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `887.50` | 385.18 USD | 13,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `891.50` | 191,570.00 USD | 13,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `892.50` | 190,750.00 USD | 14,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `893.50` | 7,370.00 USD | 14,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `894.50` | 26,840.00 USD | 14,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `896.50` | 224,120.00 USD | 14,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `897.50` | 4,100.00 USD | 14,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `898.50` | 127.59 USD | 14,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `899.50` | 12,830.00 USD | 14,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `900.50` | 129,570.00 USD | 14,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `902.50` | 305.05 USD | 14,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `905.50` | 64,000.00 USD | 14,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `906.50` | 313.65 USD | 14,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `907.50` | 386.59 USD | 14,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `908.50` | 1,790.00 USD | 14,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `909.50` | 3,170.00 USD | 14,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `910.50` | 6,880.00 USD | 14,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `911.50` | 38,590.00 USD | 14,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `916.50` | 30,130.00 USD | 14,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `921.50` | 275.53 USD | 14,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `925.50` | 9,260.00 USD | 14,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `930.50` | 653.21 USD | 14,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `934.50` | 3,340.00 USD | 14,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `937.50` | 130.31 USD | 14,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `944.50` | 201.18 USD | 14,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `947.50` | 2,300,000.00 USD | 16,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `949.50` | 58,300.00 USD | 16,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `952.50` | 398.14 USD | 16,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `958.50` | 1,010.00 USD | 16,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `968.50` | 16,720.00 USD | 16,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `969.50` | 5,780.00 USD | 16,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `972.50` | 848,020.00 USD | 17,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `977.50` | 25,910.00 USD | 17,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `978.50` | 19,570.00 USD | 17,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `981.50` | 14,480.00 USD | 17,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `985.50` | 57,750.00 USD | 17,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `986.50` | 1,220.00 USD | 17,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `990.50` | 28,300.00 USD | 17,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `993.50` | 4,150.00 USD | 17,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `994.50` | 285,520.00 USD | 18,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `997.50` | 7,300.00 USD | 18,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `999.50` | 601.70 USD | 18,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1000.50` | 50,530.00 USD | 18,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1002.50` | 100,250.00 USD | 18,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1003.50` | 677.36 USD | 18,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1005.50` | 3,000.00 USD | 18,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1006.50` | 139.90 USD | 18,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1008.50` | 28,800.00 USD | 18,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1009.50` | 304.87 USD | 18,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1010.50` | 51,420.00 USD | 18,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1020.50` | 233,370.00 USD | 18,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1021.50` | 2,440.00 USD | 18,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1023.50` | 6,080.00 USD | 18,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1024.50` | 2,850.00 USD | 18,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1026.50` | 2,920.00 USD | 18,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1030.50` | 718,890.00 USD | 19,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1031.50` | 663,220.00 USD | 20,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1042.50` | 2,290,000.00 USD | 22,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1043.50` | 65,220.00 USD | 22,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1050.50` | 500.04 USD | 22,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1052.50` | 2,480,000.00 USD | 24,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1058.50` | 6,040.00 USD | 24,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1064.50` | 1,600.00 USD | 24,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1065.50` | 38,920.00 USD | 25,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1072.50` | 15,450.00 USD | 25,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1073.50` | 1,610.00 USD | 25,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1077.50` | 207,550.00 USD | 25,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1078.50` | 122,950.00 USD | 25,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1081.50` | 484,570.00 USD | 25,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1088.50` | 1,930.00 USD | 25,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1092.50` | 21,850.00 USD | 25,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1095.50` | 122.70 USD | 25,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1099.50` | 30,960.00 USD | 25,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1100.50` | 162,610.00 USD | 26,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1101.50` | 4,630.00 USD | 26,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1102.50` | 110,250.00 USD | 26,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1115.50` | 19,880.00 USD | 26,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1116.50` | 44,660.00 USD | 26,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1119.50` | 582.14 USD | 26,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1124.50` | 48,660.00 USD | 26,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1126.50` | 165.60 USD | 26,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1133.50` | 3,710.00 USD | 26,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1137.50` | 341,250.00 USD | 26,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1138.50` | 1,520.00 USD | 26,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1140.50` | 61,660.00 USD | 26,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1143.50` | 11,610.00 USD | 26,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1146.50` | 158.22 USD | 26,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1147.50` | 153.77 USD | 26,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1149.50` | 55,530.00 USD | 26,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1150.50` | 211.69 USD | 26,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1153.50` | 362.20 USD | 26,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1160.50` | 79,200.00 USD | 26,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1166.50` | 20,250.00 USD | 26,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1173.50` | 157.25 USD | 26,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1179.50` | 66,120.00 USD | 26,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1191.50` | 123.92 USD | 26,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1197.50` | 463.43 USD | 26,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1207.50` | 385.19 USD | 26,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1211.50` | 44,950.00 USD | 26,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1218.50` | 30,440.00 USD | 27,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1219.50` | 109,750.00 USD | 27,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1225.50` | 1,030.00 USD | 27,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1226.50` | 5,260.00 USD | 27,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1228.50` | 23,850.00 USD | 27,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1239.50` | 10,760.00 USD | 27,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1246.50` | 3,850.00 USD | 27,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1251.50` | 100.12 USD | 27,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1256.50` | 44,180.00 USD | 27,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1261.50` | 5,040.00 USD | 27,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1272.50` | 114,530.00 USD | 27,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1277.50` | 346.20 USD | 27,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1283.50` | 1,810.00 USD | 27,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1289.50` | 2,580.00 USD | 27,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1291.50` | 2,760.00 USD | 27,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1295.50` | 181.37 USD | 27,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1301.50` | 19,440.00 USD | 27,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1303.50` | 32,400.00 USD | 27,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1304.50` | 7,060.00 USD | 27,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1307.50` | 226.20 USD | 27,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1313.50` | 166,660.00 USD | 27,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1320.50` | 14,140.00 USD | 27,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1323.50` | 115.14 USD | 27,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1327.50` | 152,590.00 USD | 27,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1328.50` | 80,250.00 USD | 27,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1330.50` | 23,470.00 USD | 27,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1339.50` | 30,880.00 USD | 27,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1344.50` | 18,920.00 USD | 27,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1347.50` | 128,860.00 USD | 28,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1356.50` | 20,350.00 USD | 28,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1361.50` | 4,080.00 USD | 28,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1368.50` | 4,730.00 USD | 28,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1369.50` | 46,880.00 USD | 28,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1378.50` | 66,340.00 USD | 28,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1390.50` | 718,020.00 USD | 28,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1395.50` | 32,100.00 USD | 28,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1402.50` | 178.12 USD | 28,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1406.50` | 4,770.00 USD | 28,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1407.50` | 253,350.00 USD | 29,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `141.50` | 7,740,000.00 USD | 0.00 USD | 5,340.00 USD | `-79.92%` | `37,757,000,000.00` |
| `Live` | `Long` | `142.50` | 7,730,000.00 USD | 0.00 USD | 174.28 USD | `-79.78%` | `1,223,000,000.00` |
| `Live` | `Long` | `143.50` | 7,730,000.00 USD | 0.00 USD | 2,870.00 USD | `-79.64%` | `20,000,000,000.00` |
| `Live` | `Long` | `145.50` | 7,730,000.00 USD | 0.00 USD | 87,300.00 USD | `-79.36%` | `600,000,000,000.00` |
| `Live` | `Long` | `147.50` | 7,640,000.00 USD | 0.00 USD | 2,060.00 USD | `-79.07%` | `14,000,000,000.00` |
| `Live` | `Long` | `148.50` | 7,640,000.00 USD | 0.00 USD | 1,100.00 USD | `-78.93%` | `7,434,000,000.00` |
| `Live` | `Long` | `157.50` | 7,640,000.00 USD | 0.00 USD | 787.50 USD | `-77.65%` | `5,000,000,000.00` |
| `Live` | `Long` | `161.50` | 7,640,000.00 USD | 0.00 USD | 1,940.00 USD | `-77.09%` | `12,010,000,000.00` |
| `Live` | `Long` | `166.50` | 7,640,000.00 USD | 0.00 USD | 474.03 USD | `-76.38%` | `2,847,000,000.00` |
| `Live` | `Long` | `170.50` | 7,640,000.00 USD | 0.00 USD | 308.43 USD | `-75.81%` | `1,809,000,000.00` |
| `Live` | `Long` | `175.50` | 7,630,000.00 USD | 0.00 USD | 120.57 USD | `-75.10%` | `687,000,000.00` |
| `Live` | `Long` | `176.50` | 7,630,000.00 USD | 0.00 USD | 17,650.00 USD | `-74.96%` | `100,000,000,000.00` |
| `Live` | `Long` | `177.50` | 7,620,000.00 USD | 0.00 USD | 1,070.00 USD | `-74.82%` | `6,050,000,000.00` |
| `Live` | `Long` | `178.50` | 7,620,000.00 USD | 0.00 USD | 239.90 USD | `-74.68%` | `1,344,000,000.00` |
| `Live` | `Long` | `190.50` | 7,620,000.00 USD | 0.00 USD | 1,710.00 USD | `-72.97%` | `8,994,000,000.00` |
| `Live` | `Long` | `201.50` | 7,610,000.00 USD | 0.00 USD | 247.24 USD | `-71.41%` | `1,227,000,000.00` |
| `Live` | `Long` | `209.50` | 7,610,000.00 USD | 0.00 USD | 4,790.00 USD | `-70.28%` | `22,848,000,000.00` |
| `Live` | `Long` | `219.50` | 7,610,000.00 USD | 0.00 USD | 191.18 USD | `-68.86%` | `871,000,000.00` |
| `Live` | `Long` | `222.50` | 7,610,000.00 USD | 0.00 USD | 273.45 USD | `-68.43%` | `1,229,000,000.00` |
| `Live` | `Long` | `226.50` | 7,610,000.00 USD | 0.00 USD | 160.36 USD | `-67.87%` | `708,000,000.00` |
| `Live` | `Long` | `227.50` | 7,610,000.00 USD | 0.00 USD | 7,760.00 USD | `-67.72%` | `34,129,000,000.00` |
| `Live` | `Long` | `246.50` | 7,600,000.00 USD | 0.00 USD | 138.78 USD | `-65.03%` | `563,000,000.00` |
| `Live` | `Long` | `247.50` | 7,600,000.00 USD | 0.00 USD | 17,120.00 USD | `-64.89%` | `69,189,000,000.00` |
| `Live` | `Long` | `248.50` | 7,580,000.00 USD | 0.00 USD | 255.21 USD | `-64.74%` | `1,027,000,000.00` |
| `Live` | `Long` | `250.50` | 7,580,000.00 USD | 0.00 USD | 17,400.00 USD | `-64.46%` | `69,447,000,000.00` |
| `Live` | `Long` | `256.50` | 7,570,000.00 USD | 0.00 USD | 381.93 USD | `-63.61%` | `1,489,000,000.00` |
| `Live` | `Long` | `259.50` | 7,570,000.00 USD | 0.00 USD | 259,500.00 USD | `-63.18%` | `1,000,000,000,000.00` |
| `Live` | `Long` | `264.50` | 7,310,000.00 USD | 0.00 USD | 1,400.00 USD | `-62.47%` | `5,281,000,000.00` |
| `Live` | `Long` | `266.50` | 7,300,000.00 USD | 0.00 USD | 21,130.00 USD | `-62.19%` | `79,269,000,000.00` |
| `Live` | `Long` | `272.50` | 7,280,000.00 USD | 0.00 USD | 414.47 USD | `-61.34%` | `1,521,000,000.00` |
| `Live` | `Long` | `283.50` | 7,280,000.00 USD | 0.00 USD | 402.57 USD | `-59.78%` | `1,420,000,000.00` |
| `Live` | `Long` | `286.50` | 7,280,000.00 USD | 0.00 USD | 20,050.00 USD | `-59.35%` | `70,000,000,000.00` |
| `Live` | `Long` | `292.50` | 7,260,000.00 USD | 0.00 USD | 7,270.00 USD | `-58.50%` | `24,863,000,000.00` |
| `Live` | `Long` | `293.50` | 7,260,000.00 USD | 0.00 USD | 2,090.00 USD | `-58.36%` | `7,112,000,000.00` |
| `Live` | `Long` | `302.50` | 7,250,000.00 USD | 0.00 USD | 38,940.00 USD | `-57.08%` | `128,725,000,000.00` |
| `Live` | `Long` | `311.50` | 7,210,000.00 USD | 0.00 USD | 1,960.00 USD | `-55.81%` | `6,299,000,000.00` |
| `Live` | `Long` | `313.50` | 7,210,000.00 USD | 0.00 USD | 501.60 USD | `-55.52%` | `1,600,000,000.00` |
| `Live` | `Long` | `324.50` | 7,210,000.00 USD | 0.00 USD | 658,720.00 USD | `-53.96%` | `2,029,959,000,000.00` |
| `Live` | `Long` | `325.50` | 6,550,000.00 USD | 0.00 USD | 432.59 USD | `-53.82%` | `1,329,000,000.00` |
| `Live` | `Long` | `326.50` | 6,550,000.00 USD | 0.00 USD | 500.85 USD | `-53.68%` | `1,534,000,000.00` |
| `Live` | `Long` | `327.50` | 6,550,000.00 USD | 0.00 USD | 314.07 USD | `-53.54%` | `959,000,000.00` |
| `Live` | `Long` | `328.50` | 6,550,000.00 USD | 0.00 USD | 3,240.00 USD | `-53.39%` | `9,862,000,000.00` |
| `Live` | `Long` | `330.50` | 6,550,000.00 USD | 0.00 USD | 9,410.00 USD | `-53.11%` | `28,487,000,000.00` |
| `Live` | `Long` | `332.50` | 6,540,000.00 USD | 0.00 USD | 174,060.00 USD | `-52.83%` | `523,498,000,000.00` |
| `Live` | `Long` | `333.50` | 6,370,000.00 USD | 0.00 USD | 226.45 USD | `-52.68%` | `679,000,000.00` |
| `Live` | `Long` | `334.50` | 6,360,000.00 USD | 0.00 USD | 118.08 USD | `-52.54%` | `353,000,000.00` |
| `Live` | `Long` | `336.50` | 6,360,000.00 USD | 0.00 USD | 14,300.00 USD | `-52.26%` | `42,500,000,000.00` |
| `Live` | `Long` | `338.50` | 6,350,000.00 USD | 0.00 USD | 936.63 USD | `-51.98%` | `2,767,000,000.00` |
| `Live` | `Long` | `343.50` | 6,350,000.00 USD | 0.00 USD | 652.65 USD | `-51.27%` | `1,900,000,000.00` |
| `Live` | `Long` | `348.50` | 6,350,000.00 USD | 0.00 USD | 1,100.00 USD | `-50.56%` | `3,147,000,000.00` |
| `Live` | `Long` | `358.50` | 6,350,000.00 USD | 0.00 USD | 717.00 USD | `-49.14%` | `2,000,000,000.00` |
| `Live` | `Long` | `359.50` | 6,350,000.00 USD | 0.00 USD | 212.10 USD | `-49.00%` | `590,000,000.00` |
| `Live` | `Long` | `360.50` | 6,350,000.00 USD | 0.00 USD | 1,620.00 USD | `-48.85%` | `4,504,000,000.00` |
| `Live` | `Long` | `361.50` | 6,350,000.00 USD | 0.00 USD | 6,350.00 USD | `-48.71%` | `17,576,000,000.00` |
| `Live` | `Long` | `364.50` | 6,340,000.00 USD | 0.00 USD | 863.87 USD | `-48.29%` | `2,370,000,000.00` |
| `Live` | `Long` | `366.50` | 6,340,000.00 USD | 0.00 USD | 2,110.00 USD | `-48.00%` | `5,750,000,000.00` |
| `Live` | `Long` | `370.50` | 6,340,000.00 USD | 0.00 USD | 1,220.00 USD | `-47.44%` | `3,300,000,000.00` |
| `Live` | `Long` | `372.50` | 6,330,000.00 USD | 0.00 USD | 10,930.00 USD | `-47.15%` | `29,342,000,000.00` |
| `Live` | `Long` | `374.50` | 6,320,000.00 USD | 0.00 USD | 1,820.00 USD | `-46.87%` | `4,868,000,000.00` |
| `Live` | `Long` | `377.50` | 6,320,000.00 USD | 0.00 USD | 1,400.00 USD | `-46.44%` | `3,716,000,000.00` |
| `Live` | `Long` | `379.50` | 6,320,000.00 USD | 0.00 USD | 152,450.00 USD | `-46.16%` | `401,700,000,000.00` |
| `Live` | `Long` | `382.50` | 6,170,000.00 USD | 0.00 USD | 1,910.00 USD | `-45.73%` | `5,000,000,000.00` |
| `Live` | `Long` | `383.50` | 6,170,000.00 USD | 0.00 USD | 10,900.00 USD | `-45.59%` | `28,414,000,000.00` |
| `Live` | `Long` | `384.50` | 6,160,000.00 USD | 0.00 USD | 7,970.00 USD | `-45.45%` | `20,726,000,000.00` |
| `Live` | `Long` | `385.50` | 6,150,000.00 USD | 0.00 USD | 1,800.00 USD | `-45.31%` | `4,675,000,000.00` |
| `Live` | `Long` | `386.50` | 6,150,000.00 USD | 0.00 USD | 531.44 USD | `-45.17%` | `1,375,000,000.00` |
| `Live` | `Long` | `387.50` | 6,140,000.00 USD | 0.00 USD | 392.54 USD | `-45.02%` | `1,013,000,000.00` |
| `Live` | `Long` | `388.50` | 6,140,000.00 USD | 0.00 USD | 912.98 USD | `-44.88%` | `2,350,000,000.00` |
| `Live` | `Long` | `393.50` | 6,140,000.00 USD | 0.00 USD | 103.88 USD | `-44.17%` | `264,000,000.00` |
| `Live` | `Long` | `394.50` | 6,140,000.00 USD | 0.00 USD | 168.06 USD | `-44.03%` | `426,000,000.00` |
| `Live` | `Long` | `395.50` | 6,140,000.00 USD | 0.00 USD | 2,110.00 USD | `-43.89%` | `5,347,000,000.00` |
| `Live` | `Long` | `396.50` | 6,140,000.00 USD | 0.00 USD | 610.21 USD | `-43.75%` | `1,539,000,000.00` |
| `Live` | `Long` | `397.50` | 6,140,000.00 USD | 0.00 USD | 318.00 USD | `-43.61%` | `800,000,000.00` |
| `Live` | `Long` | `398.50` | 6,140,000.00 USD | 0.00 USD | 523.63 USD | `-43.46%` | `1,314,000,000.00` |
| `Live` | `Long` | `399.50` | 6,140,000.00 USD | 0.00 USD | 603.64 USD | `-43.32%` | `1,511,000,000.00` |
| `Live` | `Long` | `402.50` | 6,140,000.00 USD | 0.00 USD | 173.07 USD | `-42.90%` | `430,000,000.00` |
| `Live` | `Long` | `404.50` | 6,140,000.00 USD | 0.00 USD | 102.34 USD | `-42.61%` | `253,000,000.00` |
| `Live` | `Long` | `408.50` | 6,140,000.00 USD | 0.00 USD | 1,290.00 USD | `-42.04%` | `3,167,000,000.00` |
| `Live` | `Long` | `410.50` | 6,140,000.00 USD | 0.00 USD | 614.52 USD | `-41.76%` | `1,497,000,000.00` |
| `Live` | `Long` | `411.50` | 6,140,000.00 USD | 0.00 USD | 106.17 USD | `-41.62%` | `258,000,000.00` |
| `Live` | `Long` | `412.50` | 6,140,000.00 USD | 0.00 USD | 3,490.00 USD | `-41.48%` | `8,455,000,000.00` |
| `Live` | `Long` | `413.50` | 6,130,000.00 USD | 0.00 USD | 1,600.00 USD | `-41.34%` | `3,860,000,000.00` |
| `Live` | `Long` | `414.50` | 6,130,000.00 USD | 0.00 USD | 15,830.00 USD | `-41.19%` | `38,182,000,000.00` |
| `Live` | `Long` | `415.50` | 6,120,000.00 USD | 0.00 USD | 1,810.00 USD | `-41.05%` | `4,368,000,000.00` |
| `Live` | `Long` | `417.50` | 6,110,000.00 USD | 0.00 USD | 7,140.00 USD | `-40.77%` | `17,092,000,000.00` |
| `Live` | `Long` | `418.50` | 6,110,000.00 USD | 0.00 USD | 465.79 USD | `-40.63%` | `1,113,000,000.00` |
| `Live` | `Long` | `420.50` | 6,110,000.00 USD | 0.00 USD | 10,650.00 USD | `-40.34%` | `25,316,000,000.00` |
| `Live` | `Long` | `421.50` | 6,100,000.00 USD | 0.00 USD | 2,320.00 USD | `-40.20%` | `5,496,000,000.00` |
| `Live` | `Long` | `422.50` | 6,090,000.00 USD | 0.00 USD | 1,380.00 USD | `-40.06%` | `3,259,000,000.00` |
| `Live` | `Long` | `423.50` | 6,090,000.00 USD | 0.00 USD | 1,450.00 USD | `-39.92%` | `3,419,000,000.00` |
| `Live` | `Long` | `429.50` | 6,090,000.00 USD | 0.00 USD | 636.52 USD | `-39.07%` | `1,482,000,000.00` |
| `Live` | `Long` | `430.50` | 6,090,000.00 USD | 0.00 USD | 30,140.00 USD | `-38.92%` | `70,000,000,000.00` |
| `Live` | `Long` | `432.50` | 6,060,000.00 USD | 0.00 USD | 4,500.00 USD | `-38.64%` | `10,413,000,000.00` |
| `Live` | `Long` | `438.50` | 6,060,000.00 USD | 0.00 USD | 1,790.00 USD | `-37.79%` | `4,087,000,000.00` |
| `Live` | `Long` | `453.50` | 6,050,000.00 USD | 0.00 USD | 7,610.00 USD | `-35.66%` | `16,790,000,000.00` |
| `Live` | `Long` | `456.50` | 6,050,000.00 USD | 0.00 USD | 4,730.00 USD | `-35.23%` | `10,359,000,000.00` |
| `Live` | `Long` | `469.50` | 6,040,000.00 USD | 0.00 USD | 4,370.00 USD | `-33.39%` | `9,301,000,000.00` |
| `Live` | `Long` | `475.50` | 6,040,000.00 USD | 0.00 USD | 5,320.00 USD | `-32.54%` | `11,182,000,000.00` |
| `Live` | `Long` | `477.50` | 6,030,000.00 USD | 0.00 USD | 827.99 USD | `-32.26%` | `1,734,000,000.00` |
| `Live` | `Long` | `481.50` | 6,030,000.00 USD | 0.00 USD | 2,620.00 USD | `-31.69%` | `5,431,000,000.00` |
| `Live` | `Long` | `482.50` | 6,030,000.00 USD | 0.00 USD | 6,840.00 USD | `-31.55%` | `14,184,000,000.00` |
| `Live` | `Long` | `484.50` | 6,020,000.00 USD | 0.00 USD | 158.43 USD | `-31.26%` | `327,000,000.00` |
| `Live` | `Long` | `485.50` | 6,020,000.00 USD | 0.00 USD | 137,560.00 USD | `-31.12%` | `283,344,000,000.00` |
| `Live` | `Long` | `486.50` | 5,880,000.00 USD | 0.00 USD | 486.50 USD | `-30.98%` | `1,000,000,000.00` |
| `Live` | `Long` | `487.50` | 5,880,000.00 USD | 0.00 USD | 204.75 USD | `-30.84%` | `420,000,000.00` |
| `Live` | `Long` | `488.50` | 5,880,000.00 USD | 0.00 USD | 257.44 USD | `-30.69%` | `527,000,000.00` |
| `Live` | `Long` | `489.50` | 5,880,000.00 USD | 0.00 USD | 6,030.00 USD | `-30.55%` | `12,312,000,000.00` |
| `Live` | `Long` | `492.50` | 5,880,000.00 USD | 0.00 USD | 50,740.00 USD | `-30.13%` | `103,025,000,000.00` |
| `Live` | `Long` | `493.50` | 5,830,000.00 USD | 0.00 USD | 3,270.00 USD | `-29.99%` | `6,635,000,000.00` |
| `Live` | `Long` | `494.50` | 5,820,000.00 USD | 0.00 USD | 669.06 USD | `-29.84%` | `1,353,000,000.00` |
| `Live` | `Long` | `495.50` | 5,820,000.00 USD | 0.00 USD | 386.99 USD | `-29.70%` | `781,000,000.00` |
| `Live` | `Long` | `497.50` | 5,820,000.00 USD | 0.00 USD | 712.42 USD | `-29.42%` | `1,432,000,000.00` |
| `Live` | `Long` | `498.50` | 5,820,000.00 USD | 0.00 USD | 60,560.00 USD | `-29.28%` | `121,488,000,000.00` |
| `Live` | `Long` | `499.50` | 5,760,000.00 USD | 0.00 USD | 10,510.00 USD | `-29.13%` | `21,035,000,000.00` |
| `Live` | `Long` | `500.50` | 5,750,000.00 USD | 0.00 USD | 41,620.00 USD | `-28.99%` | `83,150,000,000.00` |
| `Live` | `Long` | `501.50` | 5,710,000.00 USD | 0.00 USD | 8,520.00 USD | `-28.85%` | `16,982,000,000.00` |
| `Live` | `Long` | `502.50` | 5,700,000.00 USD | 0.00 USD | 109.04 USD | `-28.71%` | `217,000,000.00` |
| `Live` | `Long` | `505.50` | 5,700,000.00 USD | 0.00 USD | 46,410.00 USD | `-28.28%` | `91,819,000,000.00` |
| `Live` | `Long` | `508.50` | 5,650,000.00 USD | 0.00 USD | 992.08 USD | `-27.86%` | `1,951,000,000.00` |
| `Live` | `Long` | `509.50` | 5,650,000.00 USD | 0.00 USD | 3,100.00 USD | `-27.72%` | `6,091,000,000.00` |
| `Live` | `Long` | `510.50` | 5,650,000.00 USD | 0.00 USD | 4,840.00 USD | `-27.57%` | `9,482,000,000.00` |
| `Live` | `Long` | `511.50` | 5,640,000.00 USD | 0.00 USD | 4,090.00 USD | `-27.43%` | `8,000,000,000.00` |
| `Live` | `Long` | `512.50` | 5,640,000.00 USD | 0.00 USD | 5,190.00 USD | `-27.29%` | `10,118,000,000.00` |
| `Live` | `Long` | `514.50` | 5,630,000.00 USD | 0.00 USD | 4,010.00 USD | `-27.01%` | `7,787,000,000.00` |
| `Live` | `Long` | `515.50` | 5,630,000.00 USD | 0.00 USD | 3,930.00 USD | `-26.86%` | `7,621,000,000.00` |
| `Live` | `Long` | `516.50` | 5,630,000.00 USD | 0.00 USD | 2,550.00 USD | `-26.72%` | `4,933,000,000.00` |
| `Live` | `Long` | `517.50` | 5,620,000.00 USD | 0.00 USD | 23,350.00 USD | `-26.58%` | `45,114,000,000.00` |
| `Live` | `Long` | `518.50` | 5,600,000.00 USD | 0.00 USD | 7,540.00 USD | `-26.44%` | `14,535,000,000.00` |
| `Live` | `Long` | `519.50` | 5,590,000.00 USD | 0.00 USD | 968.35 USD | `-26.30%` | `1,864,000,000.00` |
| `Live` | `Long` | `520.50` | 5,590,000.00 USD | 0.00 USD | 272.22 USD | `-26.15%` | `523,000,000.00` |
| `Live` | `Long` | `521.50` | 5,590,000.00 USD | 0.00 USD | 838.05 USD | `-26.01%` | `1,607,000,000.00` |
| `Live` | `Long` | `523.50` | 5,590,000.00 USD | 0.00 USD | 2,090.00 USD | `-25.73%` | `3,993,000,000.00` |
| `Live` | `Long` | `524.50` | 5,590,000.00 USD | 0.00 USD | 1,120.00 USD | `-25.59%` | `2,137,000,000.00` |
| `Live` | `Long` | `525.50` | 5,590,000.00 USD | 0.00 USD | 835.02 USD | `-25.45%` | `1,589,000,000.00` |
| `Live` | `Long` | `526.50` | 5,590,000.00 USD | 0.00 USD | 1,700.00 USD | `-25.30%` | `3,234,000,000.00` |
| `Live` | `Long` | `527.50` | 5,590,000.00 USD | 0.00 USD | 555.99 USD | `-25.16%` | `1,054,000,000.00` |
| `Live` | `Long` | `529.50` | 5,590,000.00 USD | 0.00 USD | 42,820.00 USD | `-24.88%` | `80,869,000,000.00` |
| `Live` | `Long` | `530.50` | 5,540,000.00 USD | 0.00 USD | 17,900.00 USD | `-24.74%` | `33,747,000,000.00` |
| `Live` | `Long` | `531.50` | 5,520,000.00 USD | 0.00 USD | 149.35 USD | `-24.59%` | `281,000,000.00` |
| `Live` | `Long` | `532.50` | 5,520,000.00 USD | 0.00 USD | 632.08 USD | `-24.45%` | `1,187,000,000.00` |
| `Live` | `Long` | `534.50` | 5,520,000.00 USD | 0.00 USD | 1,350.00 USD | `-24.17%` | `2,533,000,000.00` |
| `Live` | `Long` | `535.50` | 5,520,000.00 USD | 0.00 USD | 100.14 USD | `-24.03%` | `187,000,000.00` |
| `Live` | `Long` | `537.50` | 5,520,000.00 USD | 0.00 USD | 268.75 USD | `-23.74%` | `500,000,000.00` |
| `Live` | `Long` | `539.50` | 5,520,000.00 USD | 0.00 USD | 490.94 USD | `-23.46%` | `910,000,000.00` |
| `Live` | `Long` | `541.50` | 5,520,000.00 USD | 0.00 USD | 472.19 USD | `-23.18%` | `872,000,000.00` |
| `Live` | `Long` | `543.50` | 5,520,000.00 USD | 0.00 USD | 2,000.00 USD | `-22.89%` | `3,687,000,000.00` |
| `Live` | `Long` | `545.50` | 5,520,000.00 USD | 0.00 USD | 212,800.00 USD | `-22.61%` | `390,104,000,000.00` |
| `Live` | `Long` | `547.50` | 5,310,000.00 USD | 0.00 USD | 815.23 USD | `-22.32%` | `1,489,000,000.00` |
| `Live` | `Long` | `548.50` | 5,310,000.00 USD | 0.00 USD | 1,580.00 USD | `-22.18%` | `2,883,000,000.00` |
| `Live` | `Long` | `549.50` | 5,300,000.00 USD | 0.00 USD | 3,300.00 USD | `-22.04%` | `6,001,000,000.00` |
| `Live` | `Long` | `550.50` | 5,300,000.00 USD | 0.00 USD | 633.63 USD | `-21.90%` | `1,151,000,000.00` |
| `Live` | `Long` | `551.50` | 5,300,000.00 USD | 0.00 USD | 957.96 USD | `-21.76%` | `1,737,000,000.00` |
| `Live` | `Long` | `552.50` | 5,300,000.00 USD | 0.00 USD | 10,220.00 USD | `-21.61%` | `18,493,000,000.00` |
| `Live` | `Long` | `553.50` | 5,290,000.00 USD | 0.00 USD | 2,730.00 USD | `-21.47%` | `4,937,000,000.00` |
| `Live` | `Long` | `554.50` | 5,290,000.00 USD | 0.00 USD | 2,250.00 USD | `-21.33%` | `4,059,000,000.00` |
| `Live` | `Long` | `555.50` | 5,280,000.00 USD | 0.00 USD | 274.97 USD | `-21.19%` | `495,000,000.00` |
| `Live` | `Long` | `557.50` | 5,280,000.00 USD | 0.00 USD | 15,700.00 USD | `-20.91%` | `28,160,000,000.00` |
| `Live` | `Long` | `558.50` | 5,270,000.00 USD | 0.00 USD | 212.23 USD | `-20.76%` | `380,000,000.00` |
| `Live` | `Long` | `560.50` | 5,270,000.00 USD | 0.00 USD | 471.38 USD | `-20.48%` | `841,000,000.00` |
| `Live` | `Long` | `561.50` | 5,270,000.00 USD | 0.00 USD | 583.40 USD | `-20.34%` | `1,039,000,000.00` |
| `Live` | `Long` | `565.50` | 5,270,000.00 USD | 0.00 USD | 24,810.00 USD | `-19.77%` | `43,879,000,000.00` |
| `Live` | `Long` | `566.50` | 5,240,000.00 USD | 0.00 USD | 160,720.00 USD | `-19.63%` | `283,700,000,000.00` |
| `Live` | `Long` | `569.50` | 5,080,000.00 USD | 0.00 USD | 144.08 USD | `-19.20%` | `253,000,000.00` |
| `Live` | `Long` | `570.50` | 5,080,000.00 USD | 0.00 USD | 1,710.00 USD | `-19.06%` | `3,000,000,000.00` |
| `Live` | `Long` | `571.50` | 5,080,000.00 USD | 0.00 USD | 712,450.00 USD | `-18.92%` | `1,246,635,000,000.00` |
| `Live` | `Long` | `572.50` | 4,370,000.00 USD | 0.00 USD | 9,830.00 USD | `-18.78%` | `17,174,000,000.00` |
| `Live` | `Long` | `574.50` | 4,360,000.00 USD | 0.00 USD | 323.44 USD | `-18.49%` | `563,000,000.00` |
| `Live` | `Long` | `576.50` | 4,360,000.00 USD | 0.00 USD | 5,760.00 USD | `-18.21%` | `9,988,000,000.00` |
| `Live` | `Long` | `578.50` | 4,350,000.00 USD | 0.00 USD | 7,640.00 USD | `-17.93%` | `13,202,000,000.00` |
| `Live` | `Long` | `581.50` | 4,340,000.00 USD | 0.00 USD | 35,070.00 USD | `-17.50%` | `60,313,000,000.00` |
| `Live` | `Long` | `582.50` | 4,310,000.00 USD | 0.00 USD | 274.94 USD | `-17.36%` | `472,000,000.00` |
| `Live` | `Long` | `584.50` | 4,310,000.00 USD | 0.00 USD | 3,380.00 USD | `-17.07%` | `5,776,000,000.00` |
| `Live` | `Long` | `586.50` | 4,300,000.00 USD | 0.00 USD | 2,650.00 USD | `-16.79%` | `4,522,000,000.00` |
| `Live` | `Long` | `587.50` | 4,300,000.00 USD | 0.00 USD | 105.75 USD | `-16.65%` | `180,000,000.00` |
| `Live` | `Long` | `590.50` | 4,300,000.00 USD | 0.00 USD | 9,330.00 USD | `-16.22%` | `15,798,000,000.00` |
| `Live` | `Long` | `592.50` | 4,290,000.00 USD | 0.00 USD | 255,620.00 USD | `-15.94%` | `431,419,000,000.00` |
| `Live` | `Long` | `593.50` | 4,040,000.00 USD | 0.00 USD | 209.51 USD | `-15.80%` | `353,000,000.00` |
| `Live` | `Long` | `594.50` | 4,040,000.00 USD | 0.00 USD | 45,480.00 USD | `-15.66%` | `76,500,000,000.00` |
| `Live` | `Long` | `595.50` | 3,990,000.00 USD | 0.00 USD | 10,090.00 USD | `-15.51%` | `16,941,000,000.00` |
| `Live` | `Long` | `597.50` | 3,980,000.00 USD | 0.00 USD | 311.30 USD | `-15.23%` | `521,000,000.00` |
| `Live` | `Long` | `598.50` | 3,980,000.00 USD | 0.00 USD | 101.75 USD | `-15.09%` | `170,000,000.00` |
| `Live` | `Long` | `599.50` | 3,980,000.00 USD | 0.00 USD | 4,430.00 USD | `-14.95%` | `7,390,000,000.00` |
| `Live` | `Long` | `600.50` | 3,980,000.00 USD | 0.00 USD | 945.19 USD | `-14.80%` | `1,574,000,000.00` |
| `Live` | `Long` | `601.50` | 3,980,000.00 USD | 0.00 USD | 16,880.00 USD | `-14.66%` | `28,061,000,000.00` |
| `Live` | `Long` | `603.50` | 3,960,000.00 USD | 0.00 USD | 58,220.00 USD | `-14.38%` | `96,477,000,000.00` |
| `Live` | `Long` | `604.50` | 3,900,000.00 USD | 0.00 USD | 2,080.00 USD | `-14.24%` | `3,439,000,000.00` |
| `Live` | `Long` | `605.50` | 3,900,000.00 USD | 0.00 USD | 3,220.00 USD | `-14.10%` | `5,312,000,000.00` |
| `Live` | `Long` | `606.50` | 3,890,000.00 USD | 0.00 USD | 1,230.00 USD | `-13.95%` | `2,022,000,000.00` |
| `Live` | `Long` | `607.50` | 3,890,000.00 USD | 0.00 USD | 650.03 USD | `-13.81%` | `1,070,000,000.00` |
| `Live` | `Long` | `608.50` | 3,890,000.00 USD | 0.00 USD | 170.38 USD | `-13.67%` | `280,000,000.00` |
| `Live` | `Long` | `610.50` | 3,890,000.00 USD | 0.00 USD | 213.67 USD | `-13.39%` | `350,000,000.00` |
| `Live` | `Long` | `612.50` | 3,890,000.00 USD | 0.00 USD | 1,580.00 USD | `-13.10%` | `2,584,000,000.00` |
| `Live` | `Long` | `613.50` | 3,890,000.00 USD | 0.00 USD | 12,270.00 USD | `-12.96%` | `20,000,000,000.00` |
| `Live` | `Long` | `614.50` | 3,880,000.00 USD | 0.00 USD | 1,440.00 USD | `-12.82%` | `2,350,000,000.00` |
| `Live` | `Long` | `615.50` | 3,880,000.00 USD | 0.00 USD | 8,870.00 USD | `-12.68%` | `14,411,000,000.00` |
| `Live` | `Long` | `616.50` | 3,870,000.00 USD | 0.00 USD | 13,520.00 USD | `-12.53%` | `21,927,000,000.00` |
| `Live` | `Long` | `617.50` | 3,850,000.00 USD | 0.00 USD | 156.23 USD | `-12.39%` | `253,000,000.00` |
| `Live` | `Long` | `618.50` | 3,850,000.00 USD | 0.00 USD | 280.18 USD | `-12.25%` | `453,000,000.00` |
| `Live` | `Long` | `620.50` | 3,850,000.00 USD | 0.00 USD | 5,410.00 USD | `-11.97%` | `8,712,000,000.00` |
| `Live` | `Long` | `621.50` | 3,850,000.00 USD | 0.00 USD | 3,230.00 USD | `-11.83%` | `5,194,000,000.00` |
| `Live` | `Long` | `624.50` | 3,850,000.00 USD | 0.00 USD | 3,460.00 USD | `-11.40%` | `5,547,000,000.00` |
| `Live` | `Long` | `625.50` | 3,840,000.00 USD | 0.00 USD | 25,330.00 USD | `-11.26%` | `40,495,000,000.00` |
| `Live` | `Long` | `627.50` | 3,820,000.00 USD | 0.00 USD | 326.30 USD | `-10.97%` | `520,000,000.00` |
| `Live` | `Long` | `629.50` | 3,820,000.00 USD | 0.00 USD | 251,890.00 USD | `-10.69%` | `400,137,000,000.00` |
| `Live` | `Long` | `630.50` | 3,560,000.00 USD | 0.00 USD | 16,960.00 USD | `-10.55%` | `26,895,000,000.00` |
| `Live` | `Long` | `632.50` | 3,550,000.00 USD | 0.00 USD | 3,560.00 USD | `-10.26%` | `5,633,000,000.00` |
| `Live` | `Long` | `633.50` | 3,540,000.00 USD | 0.00 USD | 1,090.00 USD | `-10.12%` | `1,727,000,000.00` |
| `Live` | `Long` | `635.50` | 3,540,000.00 USD | 0.00 USD | 6,070.00 USD | `-9.84%` | `9,546,000,000.00` |
| `Live` | `Long` | `637.50` | 3,540,000.00 USD | 0.00 USD | 1,150,000.00 USD | `-9.56%` | `1,797,398,000,000.00` |
| `Live` | `Long` | `638.50` | 2,390,000.00 USD | 0.00 USD | 432.90 USD | `-9.41%` | `678,000,000.00` |
| `Live` | `Long` | `639.50` | 2,390,000.00 USD | 0.00 USD | 2,730.00 USD | `-9.27%` | `4,269,000,000.00` |
| `Live` | `Long` | `640.50` | 2,390,000.00 USD | 0.00 USD | 116,220.00 USD | `-9.13%` | `181,449,000,000.00` |
| `Live` | `Long` | `641.50` | 2,270,000.00 USD | 0.00 USD | 1,670.00 USD | `-8.99%` | `2,606,000,000.00` |
| `Live` | `Long` | `642.50` | 2,270,000.00 USD | 0.00 USD | 8,970.00 USD | `-8.85%` | `13,954,000,000.00` |
| `Live` | `Long` | `644.50` | 2,260,000.00 USD | 0.00 USD | 9,660.00 USD | `-8.56%` | `14,982,000,000.00` |
| `Live` | `Long` | `645.50` | 2,250,000.00 USD | 0.00 USD | 2,070.00 USD | `-8.42%` | `3,202,000,000.00` |
| `Live` | `Long` | `646.50` | 2,250,000.00 USD | 0.00 USD | 2,250.00 USD | `-8.28%` | `3,485,000,000.00` |
| `Live` | `Long` | `649.50` | 2,250,000.00 USD | 0.00 USD | 1,120.00 USD | `-7.85%` | `1,718,000,000.00` |
| `Live` | `Long` | `650.50` | 2,250,000.00 USD | 0.00 USD | 2,930.00 USD | `-7.71%` | `4,501,000,000.00` |
| `Live` | `Long` | `651.50` | 2,240,000.00 USD | 0.00 USD | 1,520,000.00 USD | `-7.57%` | `2,337,829,000,000.00` |
| `Live` | `Long` | `652.50` | 720,020.00 USD | 0.00 USD | 1,420.00 USD | `-7.43%` | `2,172,000,000.00` |
| `Live` | `Long` | `653.50` | 718,600.00 USD | 0.00 USD | 298.00 USD | `-7.29%` | `456,000,000.00` |
| `Live` | `Long` | `654.50` | 718,300.00 USD | 0.00 USD | 97,530.00 USD | `-7.14%` | `149,014,000,000.00` |
| `Live` | `Long` | `655.50` | 620,770.00 USD | 0.00 USD | 122.58 USD | `-7.00%` | `187,000,000.00` |
| `Live` | `Long` | `658.50` | 620,650.00 USD | 0.00 USD | 937.05 USD | `-6.58%` | `1,423,000,000.00` |
| `Live` | `Long` | `659.50` | 619,710.00 USD | 0.00 USD | 157,470.00 USD | `-6.43%` | `238,766,000,000.00` |
| `Live` | `Long` | `660.50` | 462,240.00 USD | 0.00 USD | 48,030.00 USD | `-6.29%` | `72,724,000,000.00` |
| `Live` | `Long` | `661.50` | 414,210.00 USD | 0.00 USD | 101,450.00 USD | `-6.15%` | `153,359,000,000.00` |
| `Live` | `Long` | `662.50` | 312,760.00 USD | 0.00 USD | 1,530.00 USD | `-6.01%` | `2,302,000,000.00` |
| `Live` | `Long` | `663.50` | 311,240.00 USD | 0.00 USD | 2,200.00 USD | `-5.87%` | `3,317,000,000.00` |
| `Live` | `Long` | `664.50` | 309,040.00 USD | 0.00 USD | 47,690.00 USD | `-5.72%` | `71,765,000,000.00` |
| `Live` | `Long` | `665.50` | 261,350.00 USD | 0.00 USD | 2,230.00 USD | `-5.58%` | `3,352,000,000.00` |
| `Live` | `Long` | `666.50` | 259,120.00 USD | 0.00 USD | 49,980.00 USD | `-5.44%` | `74,988,000,000.00` |
| `Live` | `Long` | `667.50` | 209,140.00 USD | 0.00 USD | 5,740.00 USD | `-5.30%` | `8,602,000,000.00` |
| `Live` | `Long` | `668.50` | 203,400.00 USD | 0.00 USD | 20,730.00 USD | `-5.16%` | `31,015,000,000.00` |
| `Live` | `Long` | `669.50` | 182,660.00 USD | 0.00 USD | 4,240.00 USD | `-5.02%` | `6,334,000,000.00` |
| `Live` | `Long` | `670.50` | 178,420.00 USD | 0.00 USD | 100,710.00 USD | `-4.87%` | `150,197,000,000.00` |
| `Live` | `Long` | `671.50` | 77,720.00 USD | 0.00 USD | 6,100.00 USD | `-4.73%` | `9,079,000,000.00` |
| `Live` | `Long` | `672.50` | 71,620.00 USD | 0.00 USD | 16,260.00 USD | `-4.59%` | `24,177,000,000.00` |
| `Live` | `Long` | `673.50` | 55,360.00 USD | 0.00 USD | 6,860.00 USD | `-4.45%` | `10,186,000,000.00` |
| `Live` | `Long` | `674.50` | 48,500.00 USD | 0.00 USD | 2,910.00 USD | `-4.31%` | `4,317,000,000.00` |
| `Live` | `Long` | `675.50` | 45,590.00 USD | 0.00 USD | 23,760.00 USD | `-4.16%` | `35,171,000,000.00` |
| `Live` | `Long` | `676.50` | 21,830.00 USD | 0.00 USD | 922.07 USD | `-4.02%` | `1,363,000,000.00` |
| `Live` | `Long` | `677.50` | 20,910.00 USD | 0.00 USD | 983.73 USD | `-3.88%` | `1,452,000,000.00` |
| `Live` | `Long` | `679.50` | 19,930.00 USD | 0.00 USD | 2,110.00 USD | `-3.60%` | `3,100,000,000.00` |
| `Live` | `Long` | `680.50` | 17,820.00 USD | 0.00 USD | 2,010.00 USD | `-3.45%` | `2,958,000,000.00` |
| `Live` | `Long` | `681.50` | 15,810.00 USD | 0.00 USD | 11,580.00 USD | `-3.31%` | `16,995,000,000.00` |
| `Live` | `Short` | `683.50` | 2,920.00 USD | 2,920.00 USD | 0.00 USD | `-3.03%` | `4,271,000,000.00` |
| `Live` | `Short` | `684.50` | 5,030.00 USD | 2,110.00 USD | 0.00 USD | `-2.89%` | `3,077,000,000.00` |
| `Live` | `Long` | `688.50` | 4,220.00 USD | 0.00 USD | 146.65 USD | `-2.32%` | `213,000,000.00` |
| `Live` | `Long` | `689.50` | 4,080.00 USD | 0.00 USD | 4,080.00 USD | `-2.18%` | `5,913,000,000.00` |
| `Live` | `Short` | `704.50` | 5,240.00 USD | 213.46 USD | 0.00 USD | `-0.05%` | `303,000,000.00` |
| `Live` | `Short` | `721.50` | 13,350.00 USD | 8,110.00 USD | 0.00 USD | `+2.36%` | `11,243,000,000.00` |
| `Live` | `Short` | `722.50` | 14,000.00 USD | 650.97 USD | 0.00 USD | `+2.50%` | `901,000,000.00` |
| `Live` | `Short` | `723.50` | 37,050.00 USD | 23,050.00 USD | 0.00 USD | `+2.65%` | `31,859,000,000.00` |
| `Live` | `Short` | `724.50` | 38,360.00 USD | 1,310.00 USD | 0.00 USD | `+2.79%` | `1,811,000,000.00` |
| `Live` | `Short` | `725.50` | 41,960.00 USD | 3,600.00 USD | 0.00 USD | `+2.93%` | `4,960,000,000.00` |
| `Live` | `Short` | `726.50` | 42,870.00 USD | 912.48 USD | 0.00 USD | `+3.07%` | `1,256,000,000.00` |
| `Live` | `Short` | `727.50` | 53,070.00 USD | 10,190.00 USD | 0.00 USD | `+3.21%` | `14,010,000,000.00` |
| `Live` | `Short` | `728.50` | 62,930.00 USD | 9,860.00 USD | 0.00 USD | `+3.36%` | `13,532,000,000.00` |
| `Live` | `Short` | `729.50` | 92,520.00 USD | 29,600.00 USD | 0.00 USD | `+3.50%` | `40,570,000,000.00` |
| `Live` | `Short` | `730.50` | 127,920.00 USD | 35,390.00 USD | 0.00 USD | `+3.64%` | `48,452,000,000.00` |
| `Live` | `Short` | `731.50` | 237,920.00 USD | 110,000.00 USD | 0.00 USD | `+3.78%` | `150,379,000,000.00` |
| `Live` | `Short` | `732.50` | 414,340.00 USD | 176,420.00 USD | 0.00 USD | `+3.92%` | `240,847,000,000.00` |
| `Live` | `Short` | `733.50` | 1,160,000.00 USD | 740,840.00 USD | 0.00 USD | `+4.06%` | `1,010,000,000,000.00` |
| `Live` | `Short` | `734.50` | 1,290,000.00 USD | 134,340.00 USD | 0.00 USD | `+4.21%` | `182,897,000,000.00` |
| `Live` | `Short` | `735.50` | 1,370,000.00 USD | 78,630.00 USD | 0.00 USD | `+4.35%` | `106,905,000,000.00` |
| `Live` | `Short` | `736.50` | 1,500,000.00 USD | 133,540.00 USD | 0.00 USD | `+4.49%` | `181,312,000,000.00` |
| `Live` | `Short` | `737.50` | 1,550,000.00 USD | 45,900.00 USD | 0.00 USD | `+4.63%` | `62,244,000,000.00` |
| `Live` | `Short` | `738.50` | 2,610,000.00 USD | 1,060,000.00 USD | 0.00 USD | `+4.77%` | `1,435,373,000,000.00` |
| `Live` | `Short` | `739.50` | 2,660,000.00 USD | 52,790.00 USD | 0.00 USD | `+4.92%` | `71,385,000,000.00` |
| `Live` | `Short` | `740.50` | 2,680,000.00 USD | 17,670.00 USD | 0.00 USD | `+5.06%` | `23,858,000,000.00` |
| `Live` | `Short` | `741.50` | 2,690,000.00 USD | 9,720.00 USD | 0.00 USD | `+5.20%` | `13,108,000,000.00` |
| `Live` | `Short` | `742.50` | 2,700,000.00 USD | 8,150.00 USD | 0.00 USD | `+5.34%` | `10,971,000,000.00` |
| `Live` | `Short` | `743.50` | 3,310,000.00 USD | 609,320.00 USD | 0.00 USD | `+5.48%` | `819,535,000,000.00` |
| `Live` | `Short` | `744.50` | 3,340,000.00 USD | 29,940.00 USD | 0.00 USD | `+5.63%` | `40,220,000,000.00` |
| `Live` | `Short` | `745.50` | 3,350,000.00 USD | 17,630.00 USD | 0.00 USD | `+5.77%` | `23,651,000,000.00` |
| `Live` | `Short` | `746.50` | 3,590,000.00 USD | 240,710.00 USD | 0.00 USD | `+5.91%` | `322,454,000,000.00` |
| `Live` | `Short` | `747.50` | 3,670,000.00 USD | 76,000.00 USD | 0.00 USD | `+6.05%` | `101,671,000,000.00` |
| `Live` | `Short` | `748.50` | 3,690,000.00 USD | 22,480.00 USD | 0.00 USD | `+6.19%` | `30,029,000,000.00` |
| `Live` | `Short` | `749.50` | 3,700,000.00 USD | 6,710.00 USD | 0.00 USD | `+6.33%` | `8,958,000,000.00` |
| `Live` | `Short` | `750.50` | 3,870,000.00 USD | 172,780.00 USD | 0.00 USD | `+6.48%` | `230,214,000,000.00` |
| `Live` | `Short` | `751.50` | 4,440,000.00 USD | 566,010.00 USD | 0.00 USD | `+6.62%` | `753,168,000,000.00` |
| `Live` | `Short` | `752.50` | 4,460,000.00 USD | 24,800.00 USD | 0.00 USD | `+6.76%` | `32,956,000,000.00` |
| `Live` | `Short` | `753.50` | 4,490,000.00 USD | 26,550.00 USD | 0.00 USD | `+6.90%` | `35,234,000,000.00` |
| `Live` | `Short` | `755.50` | 4,490,000.00 USD | 658.04 USD | 0.00 USD | `+7.19%` | `871,000,000.00` |
| `Live` | `Short` | `756.50` | 4,490,000.00 USD | 3,750.00 USD | 0.00 USD | `+7.33%` | `4,960,000,000.00` |
| `Live` | `Short` | `758.50` | 4,510,000.00 USD | 16,500.00 USD | 0.00 USD | `+7.61%` | `21,755,000,000.00` |
| `Live` | `Short` | `759.50` | 4,520,000.00 USD | 6,300.00 USD | 0.00 USD | `+7.75%` | `8,293,000,000.00` |
| `Live` | `Short` | `760.50` | 4,530,000.00 USD | 13,580.00 USD | 0.00 USD | `+7.90%` | `17,854,000,000.00` |
| `Live` | `Short` | `761.50` | 4,530,000.00 USD | 541.43 USD | 0.00 USD | `+8.04%` | `711,000,000.00` |
| `Live` | `Short` | `762.50` | 4,540,000.00 USD | 5,800.00 USD | 0.00 USD | `+8.18%` | `7,607,000,000.00` |
| `Live` | `Short` | `763.50` | 5,680,000.00 USD | 1,140,000.00 USD | 0.00 USD | `+8.32%` | `1,492,052,000,000.00` |
| `Live` | `Short` | `767.50` | 5,690,000.00 USD | 15,320.00 USD | 0.00 USD | `+8.89%` | `19,966,000,000.00` |
| `Live` | `Short` | `768.50` | 5,690,000.00 USD | 156.77 USD | 0.00 USD | `+9.03%` | `204,000,000.00` |
| `Live` | `Short` | `769.50` | 5,920,000.00 USD | 231,890.00 USD | 0.00 USD | `+9.17%` | `301,348,000,000.00` |
| `Live` | `Short` | `770.50` | 5,920,000.00 USD | 2,460.00 USD | 0.00 USD | `+9.31%` | `3,190,000,000.00` |
| `Live` | `Short` | `771.50` | 5,960,000.00 USD | 32,410.00 USD | 0.00 USD | `+9.46%` | `42,015,000,000.00` |
| `Live` | `Short` | `772.50` | 6,080,000.00 USD | 120,390.00 USD | 0.00 USD | `+9.60%` | `155,843,000,000.00` |
| `Live` | `Short` | `773.50` | 6,090,000.00 USD | 8,960.00 USD | 0.00 USD | `+9.74%` | `11,578,000,000.00` |
| `Live` | `Short` | `774.50` | 6,090,000.00 USD | 130.12 USD | 0.00 USD | `+9.88%` | `168,000,000.00` |
| `Live` | `Short` | `775.50` | 6,090,000.00 USD | 5,300.00 USD | 0.00 USD | `+10.02%` | `6,828,000,000.00` |
| `Live` | `Short` | `777.50` | 6,090,000.00 USD | 209.15 USD | 0.00 USD | `+10.31%` | `269,000,000.00` |
| `Live` | `Short` | `778.50` | 6,100,000.00 USD | 3,200.00 USD | 0.00 USD | `+10.45%` | `4,107,000,000.00` |
| `Live` | `Short` | `780.50` | 6,100,000.00 USD | 7,800.00 USD | 0.00 USD | `+10.73%` | `9,990,000,000.00` |
| `Live` | `Short` | `781.50` | 6,110,000.00 USD | 7,410.00 USD | 0.00 USD | `+10.87%` | `9,476,000,000.00` |
| `Live` | `Short` | `782.50` | 6,190,000.00 USD | 78,440.00 USD | 0.00 USD | `+11.02%` | `100,238,000,000.00` |
| `Live` | `Short` | `786.50` | 6,190,000.00 USD | 4,910.00 USD | 0.00 USD | `+11.58%` | `6,245,000,000.00` |
| `Live` | `Short` | `787.50` | 6,320,000.00 USD | 122,290.00 USD | 0.00 USD | `+11.73%` | `155,292,000,000.00` |
| `Live` | `Short` | `788.50` | 6,400,000.00 USD | 79,550.00 USD | 0.00 USD | `+11.87%` | `100,888,000,000.00` |
| `Live` | `Short` | `789.50` | 6,510,000.00 USD | 114,990.00 USD | 0.00 USD | `+12.01%` | `145,644,000,000.00` |
| `Live` | `Short` | `794.50` | 6,520,000.00 USD | 7,850.00 USD | 0.00 USD | `+12.72%` | `9,876,000,000.00` |
| `Live` | `Short` | `795.50` | 6,520,000.00 USD | 6,100.00 USD | 0.00 USD | `+12.86%` | `7,669,000,000.00` |
| `Live` | `Short` | `796.50` | 6,530,000.00 USD | 301.87 USD | 0.00 USD | `+13.00%` | `379,000,000.00` |
| `Live` | `Short` | `797.50` | 6,530,000.00 USD | 2,670.00 USD | 0.00 USD | `+13.14%` | `3,350,000,000.00` |
| `Live` | `Short` | `799.50` | 6,600,000.00 USD | 76,900.00 USD | 0.00 USD | `+13.43%` | `96,185,000,000.00` |
| `Live` | `Short` | `800.50` | 6,610,000.00 USD | 9,580.00 USD | 0.00 USD | `+13.57%` | `11,965,000,000.00` |
| `Live` | `Short` | `801.50` | 6,620,000.00 USD | 3,120.00 USD | 0.00 USD | `+13.71%` | `3,896,000,000.00` |
| `Live` | `Short` | `802.50` | 6,620,000.00 USD | 2,500.00 USD | 0.00 USD | `+13.85%` | `3,117,000,000.00` |
| `Live` | `Short` | `803.50` | 6,620,000.00 USD | 1,460.00 USD | 0.00 USD | `+14.00%` | `1,815,000,000.00` |
| `Live` | `Short` | `804.50` | 6,820,000.00 USD | 197,940.00 USD | 0.00 USD | `+14.14%` | `246,047,000,000.00` |
| `Live` | `Short` | `805.50` | 6,820,000.00 USD | 2,280.00 USD | 0.00 USD | `+14.28%` | `2,829,000,000.00` |
| `Live` | `Short` | `806.50` | 6,870,000.00 USD | 44,210.00 USD | 0.00 USD | `+14.42%` | `54,814,000,000.00` |
| `Live` | `Short` | `807.50` | 6,870,000.00 USD | 3,630.00 USD | 0.00 USD | `+14.56%` | `4,494,000,000.00` |
| `Live` | `Short` | `808.50` | 6,880,000.00 USD | 11,780.00 USD | 0.00 USD | `+14.71%` | `14,574,000,000.00` |
| `Live` | `Short` | `809.50` | 6,880,000.00 USD | 1,040.00 USD | 0.00 USD | `+14.85%` | `1,280,000,000.00` |
| `Live` | `Short` | `810.50` | 6,970,000.00 USD | 92,120.00 USD | 0.00 USD | `+14.99%` | `113,663,000,000.00` |
| `Live` | `Short` | `812.50` | 6,980,000.00 USD | 9,310.00 USD | 0.00 USD | `+15.27%` | `11,458,000,000.00` |
| `Live` | `Short` | `814.50` | 6,980,000.00 USD | 692.32 USD | 0.00 USD | `+15.56%` | `850,000,000.00` |
| `Live` | `Short` | `816.50` | 6,990,000.00 USD | 1,740.00 USD | 0.00 USD | `+15.84%` | `2,128,000,000.00` |
| `Live` | `Short` | `817.50` | 7,000,000.00 USD | 9,170.00 USD | 0.00 USD | `+15.98%` | `11,218,000,000.00` |
| `Live` | `Short` | `818.50` | 7,190,000.00 USD | 193,020.00 USD | 0.00 USD | `+16.12%` | `235,816,000,000.00` |
| `Live` | `Short` | `819.50` | 7,200,000.00 USD | 11,800.00 USD | 0.00 USD | `+16.27%` | `14,397,000,000.00` |
| `Live` | `Short` | `820.50` | 7,200,000.00 USD | 136.20 USD | 0.00 USD | `+16.41%` | `166,000,000.00` |
| `Live` | `Short` | `821.50` | 7,950,000.00 USD | 751,050.00 USD | 0.00 USD | `+16.55%` | `914,240,000,000.00` |
| `Live` | `Short` | `823.50` | 8,030,000.00 USD | 81,280.00 USD | 0.00 USD | `+16.83%` | `98,695,000,000.00` |
| `Live` | `Short` | `824.50` | 8,060,000.00 USD | 25,880.00 USD | 0.00 USD | `+16.98%` | `31,383,000,000.00` |
| `Live` | `Short` | `827.50` | 8,070,000.00 USD | 8,470.00 USD | 0.00 USD | `+17.40%` | `10,238,000,000.00` |
| `Live` | `Short` | `828.50` | 8,090,000.00 USD | 26,180.00 USD | 0.00 USD | `+17.54%` | `31,604,000,000.00` |
| `Live` | `Short` | `829.50` | 8,090,000.00 USD | 505.17 USD | 0.00 USD | `+17.68%` | `609,000,000.00` |
| `Live` | `Short` | `834.50` | 10,620,000.00 USD | 2,530,000.00 USD | 0.00 USD | `+18.39%` | `3,028,213,000,000.00` |
| `Live` | `Short` | `836.50` | 10,680,000.00 USD | 61,790.00 USD | 0.00 USD | `+18.68%` | `73,865,000,000.00` |
| `Live` | `Short` | `837.50` | 10,690,000.00 USD | 7,010.00 USD | 0.00 USD | `+18.82%` | `8,375,000,000.00` |
| `Live` | `Short` | `838.50` | 10,720,000.00 USD | 32,210.00 USD | 0.00 USD | `+18.96%` | `38,408,000,000.00` |
| `Live` | `Short` | `839.50` | 10,730,000.00 USD | 11,840.00 USD | 0.00 USD | `+19.10%` | `14,107,000,000.00` |
| `Live` | `Short` | `841.50` | 10,740,000.00 USD | 2,930.00 USD | 0.00 USD | `+19.39%` | `3,478,000,000.00` |
| `Live` | `Short` | `842.50` | 10,740,000.00 USD | 1,900.00 USD | 0.00 USD | `+19.53%` | `2,256,000,000.00` |
| `Live` | `Short` | `843.50` | 10,910,000.00 USD | 173,130.00 USD | 0.00 USD | `+19.67%` | `205,251,000,000.00` |
| `Live` | `Short` | `845.50` | 10,910,000.00 USD | 1,640.00 USD | 0.00 USD | `+19.95%` | `1,944,000,000.00` |
| `Live` | `Short` | `846.50` | 11,760,000.00 USD | 850,780.00 USD | 0.00 USD | `+20.10%` | `1,005,054,000,000.00` |
| `Live` | `Short` | `848.50` | 11,760,000.00 USD | 289.34 USD | 0.00 USD | `+20.38%` | `341,000,000.00` |
| `Live` | `Short` | `849.50` | 11,840,000.00 USD | 78,290.00 USD | 0.00 USD | `+20.52%` | `92,158,000,000.00` |
| `Live` | `Short` | `850.50` | 11,930,000.00 USD | 85,760.00 USD | 0.00 USD | `+20.66%` | `100,839,000,000.00` |
| `Live` | `Short` | `851.50` | 11,940,000.00 USD | 8,520.00 USD | 0.00 USD | `+20.81%` | `10,000,000,000.00` |
| `Live` | `Short` | `852.50` | 12,040,000.00 USD | 105,740.00 USD | 0.00 USD | `+20.95%` | `124,034,000,000.00` |
| `Live` | `Short` | `854.50` | 12,040,000.00 USD | 746.83 USD | 0.00 USD | `+21.23%` | `874,000,000.00` |
| `Live` | `Short` | `858.50` | 12,630,000.00 USD | 585,810.00 USD | 0.00 USD | `+21.80%` | `682,359,000,000.00` |
| `Live` | `Short` | `859.50` | 12,650,000.00 USD | 16,380.00 USD | 0.00 USD | `+21.94%` | `19,059,000,000.00` |
| `Live` | `Short` | `865.50` | 12,670,000.00 USD | 21,490.00 USD | 0.00 USD | `+22.79%` | `24,832,000,000.00` |
| `Live` | `Short` | `867.50` | 12,680,000.00 USD | 9,810.00 USD | 0.00 USD | `+23.08%` | `11,305,000,000.00` |
| `Live` | `Short` | `873.50` | 12,970,000.00 USD | 296,410.00 USD | 0.00 USD | `+23.93%` | `339,335,000,000.00` |
| `Live` | `Short` | `874.50` | 13,010,000.00 USD | 35,770.00 USD | 0.00 USD | `+24.07%` | `40,909,000,000.00` |
| `Live` | `Short` | `875.50` | 13,010,000.00 USD | 417.61 USD | 0.00 USD | `+24.21%` | `477,000,000.00` |
| `Live` | `Short` | `877.50` | 13,620,000.00 USD | 614,250.00 USD | 0.00 USD | `+24.49%` | `700,000,000,000.00` |
| `Live` | `Short` | `878.50` | 13,630,000.00 USD | 4,390.00 USD | 0.00 USD | `+24.64%` | `5,000,000,000.00` |
| `Live` | `Short` | `879.50` | 13,630,000.00 USD | 145.12 USD | 0.00 USD | `+24.78%` | `165,000,000.00` |
| `Live` | `Short` | `883.50` | 13,630,000.00 USD | 319.83 USD | 0.00 USD | `+25.35%` | `362,000,000.00` |
| `Live` | `Short` | `884.50` | 13,650,000.00 USD | 17,050.00 USD | 0.00 USD | `+25.49%` | `19,274,000,000.00` |
| `Live` | `Short` | `885.50` | 13,650,000.00 USD | 1,430.00 USD | 0.00 USD | `+25.63%` | `1,611,000,000.00` |
| `Live` | `Short` | `886.50` | 13,650,000.00 USD | 812.92 USD | 0.00 USD | `+25.77%` | `917,000,000.00` |
| `Live` | `Short` | `887.50` | 13,650,000.00 USD | 385.18 USD | 0.00 USD | `+25.91%` | `434,000,000.00` |
| `Live` | `Short` | `891.50` | 13,840,000.00 USD | 191,570.00 USD | 0.00 USD | `+26.48%` | `214,889,000,000.00` |
| `Live` | `Short` | `892.50` | 14,030,000.00 USD | 190,750.00 USD | 0.00 USD | `+26.62%` | `213,724,000,000.00` |
| `Live` | `Short` | `893.50` | 14,040,000.00 USD | 7,370.00 USD | 0.00 USD | `+26.76%` | `8,244,000,000.00` |
| `Live` | `Short` | `894.50` | 14,060,000.00 USD | 26,840.00 USD | 0.00 USD | `+26.91%` | `30,000,000,000.00` |
| `Live` | `Short` | `896.50` | 14,290,000.00 USD | 224,120.00 USD | 0.00 USD | `+27.19%` | `250,000,000,000.00` |
| `Live` | `Short` | `897.50` | 14,290,000.00 USD | 4,100.00 USD | 0.00 USD | `+27.33%` | `4,573,000,000.00` |
| `Live` | `Short` | `898.50` | 14,290,000.00 USD | 127.59 USD | 0.00 USD | `+27.47%` | `142,000,000.00` |
| `Live` | `Short` | `899.50` | 14,310,000.00 USD | 12,830.00 USD | 0.00 USD | `+27.62%` | `14,265,000,000.00` |
| `Live` | `Short` | `900.50` | 14,440,000.00 USD | 129,570.00 USD | 0.00 USD | `+27.76%` | `143,892,000,000.00` |
| `Live` | `Short` | `902.50` | 14,440,000.00 USD | 305.05 USD | 0.00 USD | `+28.04%` | `338,000,000.00` |
| `Live` | `Short` | `905.50` | 14,500,000.00 USD | 64,000.00 USD | 0.00 USD | `+28.47%` | `70,678,000,000.00` |
| `Live` | `Short` | `906.50` | 14,500,000.00 USD | 313.65 USD | 0.00 USD | `+28.61%` | `346,000,000.00` |
| `Live` | `Short` | `907.50` | 14,500,000.00 USD | 386.59 USD | 0.00 USD | `+28.75%` | `426,000,000.00` |
| `Live` | `Short` | `908.50` | 14,500,000.00 USD | 1,790.00 USD | 0.00 USD | `+28.89%` | `1,971,000,000.00` |
| `Live` | `Short` | `909.50` | 14,510,000.00 USD | 3,170.00 USD | 0.00 USD | `+29.03%` | `3,487,000,000.00` |
| `Live` | `Short` | `910.50` | 14,510,000.00 USD | 6,880.00 USD | 0.00 USD | `+29.18%` | `7,555,000,000.00` |
| `Live` | `Short` | `911.50` | 14,550,000.00 USD | 38,590.00 USD | 0.00 USD | `+29.32%` | `42,338,000,000.00` |
| `Live` | `Short` | `916.50` | 14,580,000.00 USD | 30,130.00 USD | 0.00 USD | `+30.03%` | `32,872,000,000.00` |
| `Live` | `Short` | `921.50` | 14,580,000.00 USD | 275.53 USD | 0.00 USD | `+30.74%` | `299,000,000.00` |
| `Live` | `Short` | `925.50` | 14,590,000.00 USD | 9,260.00 USD | 0.00 USD | `+31.30%` | `10,000,000,000.00` |
| `Live` | `Short` | `930.50` | 14,590,000.00 USD | 653.21 USD | 0.00 USD | `+32.01%` | `702,000,000.00` |
| `Live` | `Short` | `934.50` | 14,590,000.00 USD | 3,340.00 USD | 0.00 USD | `+32.58%` | `3,573,000,000.00` |
| `Live` | `Short` | `937.50` | 14,590,000.00 USD | 130.31 USD | 0.00 USD | `+33.01%` | `139,000,000.00` |
| `Live` | `Short` | `944.50` | 14,590,000.00 USD | 201.18 USD | 0.00 USD | `+34.00%` | `213,000,000.00` |
| `Live` | `Short` | `947.50` | 16,900,000.00 USD | 2,300,000.00 USD | 0.00 USD | `+34.43%` | `2,429,891,000,000.00` |
| `Live` | `Short` | `949.50` | 16,960,000.00 USD | 58,300.00 USD | 0.00 USD | `+34.71%` | `61,406,000,000.00` |
| `Live` | `Short` | `952.50` | 16,960,000.00 USD | 398.14 USD | 0.00 USD | `+35.14%` | `418,000,000.00` |
| `Live` | `Short` | `958.50` | 16,960,000.00 USD | 1,010.00 USD | 0.00 USD | `+35.99%` | `1,050,000,000.00` |
| `Live` | `Short` | `968.50` | 16,970,000.00 USD | 16,720.00 USD | 0.00 USD | `+37.41%` | `17,266,000,000.00` |
| `Live` | `Short` | `969.50` | 16,980,000.00 USD | 5,780.00 USD | 0.00 USD | `+37.55%` | `5,960,000,000.00` |
| `Live` | `Short` | `972.50` | 17,830,000.00 USD | 848,020.00 USD | 0.00 USD | `+37.97%` | `872,000,000,000.00` |
| `Live` | `Short` | `977.50` | 17,850,000.00 USD | 25,910.00 USD | 0.00 USD | `+38.68%` | `26,505,000,000.00` |
| `Live` | `Short` | `978.50` | 17,870,000.00 USD | 19,570.00 USD | 0.00 USD | `+38.82%` | `20,000,000,000.00` |
| `Live` | `Short` | `981.50` | 17,890,000.00 USD | 14,480.00 USD | 0.00 USD | `+39.25%` | `14,758,000,000.00` |
| `Live` | `Short` | `985.50` | 17,950,000.00 USD | 57,750.00 USD | 0.00 USD | `+39.82%` | `58,601,000,000.00` |
| `Live` | `Short` | `986.50` | 17,950,000.00 USD | 1,220.00 USD | 0.00 USD | `+39.96%` | `1,235,000,000.00` |
| `Live` | `Short` | `990.50` | 17,970,000.00 USD | 28,300.00 USD | 0.00 USD | `+40.53%` | `28,570,000,000.00` |
| `Live` | `Short` | `993.50` | 17,980,000.00 USD | 4,150.00 USD | 0.00 USD | `+40.95%` | `4,178,000,000.00` |
| `Live` | `Short` | `994.50` | 18,260,000.00 USD | 285,520.00 USD | 0.00 USD | `+41.09%` | `287,098,000,000.00` |
| `Live` | `Short` | `997.50` | 18,270,000.00 USD | 7,300.00 USD | 0.00 USD | `+41.52%` | `7,316,000,000.00` |
| `Live` | `Short` | `999.50` | 18,270,000.00 USD | 601.70 USD | 0.00 USD | `+41.80%` | `602,000,000.00` |
| `Live` | `Short` | `1000.50` | 18,320,000.00 USD | 50,530.00 USD | 0.00 USD | `+41.95%` | `50,508,000,000.00` |
| `Live` | `Short` | `1002.50` | 18,420,000.00 USD | 100,250.00 USD | 0.00 USD | `+42.23%` | `99,998,000,000.00` |
| `Live` | `Short` | `1003.50` | 18,420,000.00 USD | 677.36 USD | 0.00 USD | `+42.37%` | `675,000,000.00` |
| `Live` | `Short` | `1005.50` | 18,430,000.00 USD | 3,000.00 USD | 0.00 USD | `+42.65%` | `2,983,000,000.00` |
| `Live` | `Short` | `1006.50` | 18,430,000.00 USD | 139.90 USD | 0.00 USD | `+42.80%` | `139,000,000.00` |
| `Live` | `Short` | `1008.50` | 18,460,000.00 USD | 28,800.00 USD | 0.00 USD | `+43.08%` | `28,558,000,000.00` |
| `Live` | `Short` | `1009.50` | 18,460,000.00 USD | 304.87 USD | 0.00 USD | `+43.22%` | `302,000,000.00` |
| `Live` | `Short` | `1010.50` | 18,510,000.00 USD | 51,420.00 USD | 0.00 USD | `+43.36%` | `50,889,000,000.00` |
| `Live` | `Short` | `1020.50` | 18,740,000.00 USD | 233,370.00 USD | 0.00 USD | `+44.78%` | `228,681,000,000.00` |
| `Live` | `Short` | `1021.50` | 18,740,000.00 USD | 2,440.00 USD | 0.00 USD | `+44.92%` | `2,384,000,000.00` |
| `Live` | `Short` | `1023.50` | 18,750,000.00 USD | 6,080.00 USD | 0.00 USD | `+45.21%` | `5,940,000,000.00` |
| `Live` | `Short` | `1024.50` | 18,750,000.00 USD | 2,850.00 USD | 0.00 USD | `+45.35%` | `2,777,000,000.00` |
| `Live` | `Short` | `1026.50` | 18,750,000.00 USD | 2,920.00 USD | 0.00 USD | `+45.63%` | `2,846,000,000.00` |
| `Live` | `Short` | `1030.50` | 19,470,000.00 USD | 718,890.00 USD | 0.00 USD | `+46.20%` | `697,611,000,000.00` |
| `Live` | `Short` | `1031.50` | 20,140,000.00 USD | 663,220.00 USD | 0.00 USD | `+46.34%` | `642,971,000,000.00` |
| `Live` | `Short` | `1042.50` | 22,430,000.00 USD | 2,290,000.00 USD | 0.00 USD | `+47.90%` | `2,198,328,000,000.00` |
| `Live` | `Short` | `1043.50` | 22,490,000.00 USD | 65,220.00 USD | 0.00 USD | `+48.05%` | `62,500,000,000.00` |
| `Live` | `Short` | `1050.50` | 22,490,000.00 USD | 500.04 USD | 0.00 USD | `+49.04%` | `476,000,000.00` |
| `Live` | `Short` | `1052.50` | 24,980,000.00 USD | 2,480,000.00 USD | 0.00 USD | `+49.32%` | `2,360,687,000,000.00` |
| `Live` | `Short` | `1058.50` | 24,990,000.00 USD | 6,040.00 USD | 0.00 USD | `+50.17%` | `5,710,000,000.00` |
| `Live` | `Short` | `1064.50` | 24,990,000.00 USD | 1,600.00 USD | 0.00 USD | `+51.03%` | `1,500,000,000.00` |
| `Live` | `Short` | `1065.50` | 25,030,000.00 USD | 38,920.00 USD | 0.00 USD | `+51.17%` | `36,530,000,000.00` |
| `Live` | `Short` | `1072.50` | 25,040,000.00 USD | 15,450.00 USD | 0.00 USD | `+52.16%` | `14,403,000,000.00` |
| `Live` | `Short` | `1073.50` | 25,040,000.00 USD | 1,610.00 USD | 0.00 USD | `+52.30%` | `1,500,000,000.00` |
| `Live` | `Short` | `1077.50` | 25,250,000.00 USD | 207,550.00 USD | 0.00 USD | `+52.87%` | `192,625,000,000.00` |
| `Live` | `Short` | `1078.50` | 25,370,000.00 USD | 122,950.00 USD | 0.00 USD | `+53.01%` | `114,000,000,000.00` |
| `Live` | `Short` | `1081.50` | 25,860,000.00 USD | 484,570.00 USD | 0.00 USD | `+53.44%` | `448,058,000,000.00` |
| `Live` | `Short` | `1088.50` | 25,860,000.00 USD | 1,930.00 USD | 0.00 USD | `+54.43%` | `1,776,000,000.00` |
| `Live` | `Short` | `1092.50` | 25,880,000.00 USD | 21,850.00 USD | 0.00 USD | `+55.00%` | `20,000,000,000.00` |
| `Live` | `Short` | `1095.50` | 25,880,000.00 USD | 122.70 USD | 0.00 USD | `+55.42%` | `112,000,000.00` |
| `Live` | `Short` | `1099.50` | 25,910,000.00 USD | 30,960.00 USD | 0.00 USD | `+55.99%` | `28,156,000,000.00` |
| `Live` | `Short` | `1100.50` | 26,080,000.00 USD | 162,610.00 USD | 0.00 USD | `+56.13%` | `147,759,000,000.00` |
| `Live` | `Short` | `1101.50` | 26,080,000.00 USD | 4,630.00 USD | 0.00 USD | `+56.27%` | `4,204,000,000.00` |
| `Live` | `Short` | `1102.50` | 26,190,000.00 USD | 110,250.00 USD | 0.00 USD | `+56.42%` | `100,000,000,000.00` |
| `Live` | `Short` | `1115.50` | 26,210,000.00 USD | 19,880.00 USD | 0.00 USD | `+58.26%` | `17,826,000,000.00` |
| `Live` | `Short` | `1116.50` | 26,250,000.00 USD | 44,660.00 USD | 0.00 USD | `+58.40%` | `40,000,000,000.00` |
| `Live` | `Short` | `1119.50` | 26,260,000.00 USD | 582.14 USD | 0.00 USD | `+58.83%` | `520,000,000.00` |
| `Live` | `Short` | `1124.50` | 26,300,000.00 USD | 48,660.00 USD | 0.00 USD | `+59.54%` | `43,270,000,000.00` |
| `Live` | `Short` | `1126.50` | 26,300,000.00 USD | 165.60 USD | 0.00 USD | `+59.82%` | `147,000,000.00` |
| `Live` | `Short` | `1133.50` | 26,310,000.00 USD | 3,710.00 USD | 0.00 USD | `+60.81%` | `3,276,000,000.00` |
| `Live` | `Short` | `1137.50` | 26,650,000.00 USD | 341,250.00 USD | 0.00 USD | `+61.38%` | `300,000,000,000.00` |
| `Live` | `Short` | `1138.50` | 26,650,000.00 USD | 1,520.00 USD | 0.00 USD | `+61.52%` | `1,337,000,000.00` |
| `Live` | `Short` | `1140.50` | 26,710,000.00 USD | 61,660.00 USD | 0.00 USD | `+61.81%` | `54,065,000,000.00` |
| `Live` | `Short` | `1143.50` | 26,720,000.00 USD | 11,610.00 USD | 0.00 USD | `+62.23%` | `10,154,000,000.00` |
| `Live` | `Short` | `1146.50` | 26,720,000.00 USD | 158.22 USD | 0.00 USD | `+62.66%` | `138,000,000.00` |
| `Live` | `Short` | `1147.50` | 26,720,000.00 USD | 153.77 USD | 0.00 USD | `+62.80%` | `134,000,000.00` |
| `Live` | `Short` | `1149.50` | 26,780,000.00 USD | 55,530.00 USD | 0.00 USD | `+63.08%` | `48,311,000,000.00` |
| `Live` | `Short` | `1150.50` | 26,780,000.00 USD | 211.69 USD | 0.00 USD | `+63.23%` | `184,000,000.00` |
| `Live` | `Short` | `1153.50` | 26,780,000.00 USD | 362.20 USD | 0.00 USD | `+63.65%` | `314,000,000.00` |
| `Live` | `Short` | `1160.50` | 26,860,000.00 USD | 79,200.00 USD | 0.00 USD | `+64.64%` | `68,249,000,000.00` |
| `Live` | `Short` | `1166.50` | 26,880,000.00 USD | 20,250.00 USD | 0.00 USD | `+65.50%` | `17,363,000,000.00` |
| `Live` | `Short` | `1173.50` | 26,880,000.00 USD | 157.25 USD | 0.00 USD | `+66.49%` | `134,000,000.00` |
| `Live` | `Short` | `1179.50` | 26,950,000.00 USD | 66,120.00 USD | 0.00 USD | `+67.34%` | `56,055,000,000.00` |
| `Live` | `Short` | `1191.50` | 26,950,000.00 USD | 123.92 USD | 0.00 USD | `+69.04%` | `104,000,000.00` |
| `Live` | `Short` | `1197.50` | 26,950,000.00 USD | 463.43 USD | 0.00 USD | `+69.89%` | `387,000,000.00` |
| `Live` | `Short` | `1207.50` | 26,950,000.00 USD | 385.19 USD | 0.00 USD | `+71.31%` | `319,000,000.00` |
| `Live` | `Short` | `1211.50` | 26,990,000.00 USD | 44,950.00 USD | 0.00 USD | `+71.88%` | `37,100,000,000.00` |
| `Live` | `Short` | `1218.50` | 27,020,000.00 USD | 30,440.00 USD | 0.00 USD | `+72.87%` | `24,982,000,000.00` |
| `Live` | `Short` | `1219.50` | 27,130,000.00 USD | 109,750.00 USD | 0.00 USD | `+73.02%` | `90,000,000,000.00` |
| `Live` | `Short` | `1225.50` | 27,130,000.00 USD | 1,030.00 USD | 0.00 USD | `+73.87%` | `841,000,000.00` |
| `Live` | `Short` | `1226.50` | 27,140,000.00 USD | 5,260.00 USD | 0.00 USD | `+74.01%` | `4,292,000,000.00` |
| `Live` | `Short` | `1228.50` | 27,160,000.00 USD | 23,850.00 USD | 0.00 USD | `+74.29%` | `19,414,000,000.00` |
| `Live` | `Short` | `1239.50` | 27,170,000.00 USD | 10,760.00 USD | 0.00 USD | `+75.85%` | `8,680,000,000.00` |
| `Live` | `Short` | `1246.50` | 27,180,000.00 USD | 3,850.00 USD | 0.00 USD | `+76.85%` | `3,092,000,000.00` |
| `Live` | `Short` | `1251.50` | 27,180,000.00 USD | 100.12 USD | 0.00 USD | `+77.56%` | `80,000,000.00` |
| `Live` | `Short` | `1256.50` | 27,220,000.00 USD | 44,180.00 USD | 0.00 USD | `+78.26%` | `35,160,000,000.00` |
| `Live` | `Short` | `1261.50` | 27,230,000.00 USD | 5,040.00 USD | 0.00 USD | `+78.97%` | `3,994,000,000.00` |
| `Live` | `Short` | `1272.50` | 27,340,000.00 USD | 114,530.00 USD | 0.00 USD | `+80.53%` | `90,000,000,000.00` |
| `Live` | `Short` | `1277.50` | 27,340,000.00 USD | 346.20 USD | 0.00 USD | `+81.24%` | `271,000,000.00` |
| `Live` | `Short` | `1283.50` | 27,340,000.00 USD | 1,810.00 USD | 0.00 USD | `+82.10%` | `1,409,000,000.00` |
| `Live` | `Short` | `1289.50` | 27,350,000.00 USD | 2,580.00 USD | 0.00 USD | `+82.95%` | `2,000,000,000.00` |
| `Live` | `Short` | `1291.50` | 27,350,000.00 USD | 2,760.00 USD | 0.00 USD | `+83.23%` | `2,134,000,000.00` |
| `Live` | `Short` | `1295.50` | 27,350,000.00 USD | 181.37 USD | 0.00 USD | `+83.80%` | `140,000,000.00` |
| `Live` | `Short` | `1301.50` | 27,370,000.00 USD | 19,440.00 USD | 0.00 USD | `+84.65%` | `14,939,000,000.00` |
| `Live` | `Short` | `1303.50` | 27,400,000.00 USD | 32,400.00 USD | 0.00 USD | `+84.93%` | `24,853,000,000.00` |
| `Live` | `Short` | `1304.50` | 27,410,000.00 USD | 7,060.00 USD | 0.00 USD | `+85.07%` | `5,411,000,000.00` |
| `Live` | `Short` | `1307.50` | 27,410,000.00 USD | 226.20 USD | 0.00 USD | `+85.50%` | `173,000,000.00` |
| `Live` | `Short` | `1313.50` | 27,570,000.00 USD | 166,660.00 USD | 0.00 USD | `+86.35%` | `126,881,000,000.00` |
| `Live` | `Short` | `1320.50` | 27,590,000.00 USD | 14,140.00 USD | 0.00 USD | `+87.34%` | `10,710,000,000.00` |
| `Live` | `Short` | `1323.50` | 27,590,000.00 USD | 115.14 USD | 0.00 USD | `+87.77%` | `87,000,000.00` |
| `Live` | `Short` | `1327.50` | 27,740,000.00 USD | 152,590.00 USD | 0.00 USD | `+88.34%` | `114,948,000,000.00` |
| `Live` | `Short` | `1328.50` | 27,820,000.00 USD | 80,250.00 USD | 0.00 USD | `+88.48%` | `60,409,000,000.00` |
| `Live` | `Short` | `1330.50` | 27,840,000.00 USD | 23,470.00 USD | 0.00 USD | `+88.76%` | `17,640,000,000.00` |
| `Live` | `Short` | `1339.50` | 27,880,000.00 USD | 30,880.00 USD | 0.00 USD | `+90.04%` | `23,055,000,000.00` |
| `Live` | `Short` | `1344.50` | 27,890,000.00 USD | 18,920.00 USD | 0.00 USD | `+90.75%` | `14,070,000,000.00` |
| `Live` | `Short` | `1347.50` | 28,020,000.00 USD | 128,860.00 USD | 0.00 USD | `+91.18%` | `95,630,000,000.00` |
| `Live` | `Short` | `1356.50` | 28,040,000.00 USD | 20,350.00 USD | 0.00 USD | `+92.45%` | `15,000,000,000.00` |
| `Live` | `Short` | `1361.50` | 28,050,000.00 USD | 4,080.00 USD | 0.00 USD | `+93.16%` | `3,000,000,000.00` |
| `Live` | `Short` | `1368.50` | 28,050,000.00 USD | 4,730.00 USD | 0.00 USD | `+94.15%` | `3,457,000,000.00` |
| `Live` | `Short` | `1369.50` | 28,100,000.00 USD | 46,880.00 USD | 0.00 USD | `+94.30%` | `34,232,000,000.00` |
| `Live` | `Short` | `1378.50` | 28,170,000.00 USD | 66,340.00 USD | 0.00 USD | `+95.57%` | `48,123,000,000.00` |
| `Live` | `Short` | `1390.50` | 28,880,000.00 USD | 718,020.00 USD | 0.00 USD | `+97.28%` | `516,379,000,000.00` |
| `Live` | `Short` | `1395.50` | 28,920,000.00 USD | 32,100.00 USD | 0.00 USD | `+97.99%` | `23,000,000,000.00` |
| `Live` | `Short` | `1402.50` | 28,920,000.00 USD | 178.12 USD | 0.00 USD | `+98.98%` | `127,000,000.00` |
| `Live` | `Short` | `1406.50` | 28,920,000.00 USD | 4,770.00 USD | 0.00 USD | `+99.55%` | `3,392,000,000.00` |
| `Live` | `Short` | `1407.50` | 29,170,000.00 USD | 253,350.00 USD | 0.00 USD | `+99.69%` | `180,000,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `150.50` | 4,700,000.00 USD | 0.00 USD | 475.73 USD | `-78.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `300.50` | 4,700,000.00 USD | 0.00 USD | 4,190.00 USD | `-57.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `333.50` | 4,700,000.00 USD | 0.00 USD | 333.50 USD | `-52.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `350.50` | 4,700,000.00 USD | 0.00 USD | 127.58 USD | `-50.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `360.50` | 4,700,000.00 USD | 0.00 USD | 10,710.00 USD | `-48.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `369.50` | 4,690,000.00 USD | 0.00 USD | 5,170.00 USD | `-47.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `400.50` | 4,680,000.00 USD | 0.00 USD | 17,290.00 USD | `-43.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `410.50` | 4,670,000.00 USD | 0.00 USD | 25,210.00 USD | `-41.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `412.50` | 4,640,000.00 USD | 0.00 USD | 4,550.00 USD | `-41.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `455.50` | 4,640,000.00 USD | 0.00 USD | 698.74 USD | `-35.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `458.50` | 4,640,000.00 USD | 0.00 USD | 1,750.00 USD | `-34.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `469.50` | 4,630,000.00 USD | 0.00 USD | 3,550.00 USD | `-33.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `486.50` | 4,630,000.00 USD | 0.00 USD | 100.71 USD | `-30.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `487.50` | 4,630,000.00 USD | 0.00 USD | 6,600.00 USD | `-30.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `488.50` | 4,620,000.00 USD | 0.00 USD | 2,490.00 USD | `-30.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `492.50` | 4,620,000.00 USD | 0.00 USD | 2,450.00 USD | `-30.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `498.50` | 4,620,000.00 USD | 0.00 USD | 163.01 USD | `-29.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `499.50` | 4,620,000.00 USD | 0.00 USD | 214.78 USD | `-29.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `500.50` | 4,620,000.00 USD | 0.00 USD | 70,160.00 USD | `-28.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `503.50` | 4,550,000.00 USD | 0.00 USD | 42,600.00 USD | `-28.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `506.50` | 4,510,000.00 USD | 0.00 USD | 138.78 USD | `-28.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `509.50` | 4,510,000.00 USD | 0.00 USD | 185.97 USD | `-27.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `515.50` | 4,510,000.00 USD | 0.00 USD | 1,030.00 USD | `-26.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `516.50` | 4,500,000.00 USD | 0.00 USD | 125.51 USD | `-26.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `517.50` | 4,500,000.00 USD | 0.00 USD | 280.49 USD | `-26.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `521.50` | 4,500,000.00 USD | 0.00 USD | 258.14 USD | `-26.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `524.50` | 4,500,000.00 USD | 0.00 USD | 8,170.00 USD | `-25.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `528.50` | 4,500,000.00 USD | 0.00 USD | 485.16 USD | `-25.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `534.50` | 4,500,000.00 USD | 0.00 USD | 4,650.00 USD | `-24.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `538.50` | 4,490,000.00 USD | 0.00 USD | 1,680.00 USD | `-23.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `540.50` | 4,490,000.00 USD | 0.00 USD | 2,490.00 USD | `-23.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `550.50` | 4,490,000.00 USD | 0.00 USD | 4,130.00 USD | `-21.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `552.50` | 4,480,000.00 USD | 0.00 USD | 366,230.00 USD | `-21.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `554.50` | 4,120,000.00 USD | 0.00 USD | 1,190.00 USD | `-21.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `555.50` | 4,120,000.00 USD | 0.00 USD | 611.05 USD | `-21.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `557.50` | 4,110,000.00 USD | 0.00 USD | 213.52 USD | `-20.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `558.50` | 4,110,000.00 USD | 0.00 USD | 51,260.00 USD | `-20.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `560.50` | 4,060,000.00 USD | 0.00 USD | 292.02 USD | `-20.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `561.50` | 4,060,000.00 USD | 0.00 USD | 748.48 USD | `-20.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `562.50` | 4,060,000.00 USD | 0.00 USD | 199.12 USD | `-20.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `566.50` | 4,060,000.00 USD | 0.00 USD | 566.50 USD | `-19.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `567.50` | 4,060,000.00 USD | 0.00 USD | 330.85 USD | `-19.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `568.50` | 4,060,000.00 USD | 0.00 USD | 5,680.00 USD | `-19.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `570.50` | 4,060,000.00 USD | 0.00 USD | 774.17 USD | `-19.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `571.50` | 4,050,000.00 USD | 0.00 USD | 1,700.00 USD | `-18.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `573.50` | 4,050,000.00 USD | 0.00 USD | 291.91 USD | `-18.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `575.50` | 4,050,000.00 USD | 0.00 USD | 469.61 USD | `-18.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `576.50` | 4,050,000.00 USD | 0.00 USD | 289.98 USD | `-18.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `577.50` | 4,050,000.00 USD | 0.00 USD | 285.86 USD | `-18.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `579.50` | 4,050,000.00 USD | 0.00 USD | 289.17 USD | `-17.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `580.50` | 4,050,000.00 USD | 0.00 USD | 6,750.00 USD | `-17.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `581.50` | 4,040,000.00 USD | 0.00 USD | 8,830.00 USD | `-17.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `583.50` | 4,040,000.00 USD | 0.00 USD | 287.67 USD | `-17.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `584.50` | 4,040,000.00 USD | 0.00 USD | 763.94 USD | `-17.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `585.50` | 4,030,000.00 USD | 0.00 USD | 1,430.00 USD | `-16.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `586.50` | 4,030,000.00 USD | 0.00 USD | 34,020.00 USD | `-16.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `587.50` | 4,000,000.00 USD | 0.00 USD | 289.05 USD | `-16.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `588.50` | 4,000,000.00 USD | 0.00 USD | 287.78 USD | `-16.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `589.50` | 4,000,000.00 USD | 0.00 USD | 1,820.00 USD | `-16.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `590.50` | 4,000,000.00 USD | 0.00 USD | 540.31 USD | `-16.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `592.50` | 4,000,000.00 USD | 0.00 USD | 698.56 USD | `-15.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `594.50` | 4,000,000.00 USD | 0.00 USD | 286.55 USD | `-15.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `598.50` | 4,000,000.00 USD | 0.00 USD | 244.79 USD | `-15.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `600.50` | 3,990,000.00 USD | 0.00 USD | 43,120.00 USD | `-14.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `601.50` | 3,950,000.00 USD | 0.00 USD | 1,590.00 USD | `-14.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `605.50` | 3,950,000.00 USD | 0.00 USD | 2,610.00 USD | `-14.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `606.50` | 3,950,000.00 USD | 0.00 USD | 103.11 USD | `-13.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `608.50` | 3,950,000.00 USD | 0.00 USD | 30,620.00 USD | `-13.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `611.50` | 3,920,000.00 USD | 0.00 USD | 5,140.00 USD | `-13.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `612.50` | 3,910,000.00 USD | 0.00 USD | 1,380.00 USD | `-13.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `614.50` | 3,910,000.00 USD | 0.00 USD | 269.15 USD | `-12.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `615.50` | 3,910,000.00 USD | 0.00 USD | 1,740.00 USD | `-12.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `616.50` | 3,910,000.00 USD | 0.00 USD | 120.83 USD | `-12.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `620.50` | 3,910,000.00 USD | 0.00 USD | 2,560.00 USD | `-11.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `621.50` | 3,910,000.00 USD | 0.00 USD | 2,150.00 USD | `-11.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `623.50` | 3,900,000.00 USD | 0.00 USD | 8,890.00 USD | `-11.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `624.50` | 3,890,000.00 USD | 0.00 USD | 351.59 USD | `-11.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `625.50` | 3,890,000.00 USD | 0.00 USD | 445.98 USD | `-11.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `626.50` | 3,890,000.00 USD | 0.00 USD | 694.79 USD | `-11.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `628.50` | 3,890,000.00 USD | 0.00 USD | 33,300.00 USD | `-10.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `629.50` | 3,860,000.00 USD | 0.00 USD | 1,440.00 USD | `-10.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `630.50` | 3,860,000.00 USD | 0.00 USD | 546.01 USD | `-10.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `631.50` | 3,860,000.00 USD | 0.00 USD | 179.98 USD | `-10.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `632.50` | 3,860,000.00 USD | 0.00 USD | 3,800.00 USD | `-10.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `633.50` | 3,850,000.00 USD | 0.00 USD | 4,570.00 USD | `-10.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `634.50` | 3,850,000.00 USD | 0.00 USD | 2,550.00 USD | `-9.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `636.50` | 3,850,000.00 USD | 0.00 USD | 6,460.00 USD | `-9.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `638.50` | 3,840,000.00 USD | 0.00 USD | 4,200.00 USD | `-9.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `639.50` | 3,840,000.00 USD | 0.00 USD | 155.40 USD | `-9.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `640.50` | 3,840,000.00 USD | 0.00 USD | 429.78 USD | `-9.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `642.50` | 3,840,000.00 USD | 0.00 USD | 1,280.00 USD | `-8.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `643.50` | 3,830,000.00 USD | 0.00 USD | 1,830.00 USD | `-8.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `644.50` | 3,830,000.00 USD | 0.00 USD | 3,790.00 USD | `-8.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `645.50` | 3,830,000.00 USD | 0.00 USD | 1,950.00 USD | `-8.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `646.50` | 3,830,000.00 USD | 0.00 USD | 971.04 USD | `-8.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `648.50` | 3,830,000.00 USD | 0.00 USD | 1,800.00 USD | `-7.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `649.50` | 3,820,000.00 USD | 0.00 USD | 2,230.00 USD | `-7.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `650.50` | 3,820,000.00 USD | 0.00 USD | 28,150.00 USD | `-7.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `651.50` | 3,790,000.00 USD | 0.00 USD | 2,090.00 USD | `-7.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `653.50` | 3,790,000.00 USD | 0.00 USD | 2,020.00 USD | `-7.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `654.50` | 3,790,000.00 USD | 0.00 USD | 308.92 USD | `-7.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `655.50` | 3,790,000.00 USD | 0.00 USD | 13,180.00 USD | `-7.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `656.50` | 3,780,000.00 USD | 0.00 USD | 456.27 USD | `-6.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `657.50` | 3,780,000.00 USD | 0.00 USD | 110.46 USD | `-6.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `658.50` | 3,780,000.00 USD | 0.00 USD | 1,320.00 USD | `-6.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `659.50` | 3,770,000.00 USD | 0.00 USD | 3,130.00 USD | `-6.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `660.50` | 3,770,000.00 USD | 0.00 USD | 19,240.00 USD | `-6.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `661.50` | 3,750,000.00 USD | 0.00 USD | 11,210.00 USD | `-6.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `662.50` | 3,740,000.00 USD | 0.00 USD | 7,580.00 USD | `-6.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `663.50` | 3,730,000.00 USD | 0.00 USD | 2,840.00 USD | `-5.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `664.50` | 3,730,000.00 USD | 0.00 USD | 713.01 USD | `-5.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `665.50` | 3,730,000.00 USD | 0.00 USD | 11,720.00 USD | `-5.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `666.50` | 3,720,000.00 USD | 0.00 USD | 1,950.00 USD | `-5.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `667.50` | 3,720,000.00 USD | 0.00 USD | 10,740.00 USD | `-5.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `668.50` | 3,700,000.00 USD | 0.00 USD | 760.75 USD | `-5.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `669.50` | 3,700,000.00 USD | 0.00 USD | 3,440.00 USD | `-5.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `670.50` | 3,700,000.00 USD | 0.00 USD | 129,470.00 USD | `-4.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `671.50` | 3,570,000.00 USD | 0.00 USD | 22,320.00 USD | `-4.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `672.50` | 3,550,000.00 USD | 0.00 USD | 517.15 USD | `-4.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `673.50` | 3,550,000.00 USD | 0.00 USD | 279,980.00 USD | `-4.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `674.50` | 3,270,000.00 USD | 0.00 USD | 2,450.00 USD | `-4.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `675.50` | 3,270,000.00 USD | 0.00 USD | 8,300.00 USD | `-4.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `676.50` | 3,260,000.00 USD | 0.00 USD | 55,120.00 USD | `-4.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `677.50` | 3,200,000.00 USD | 0.00 USD | 41,270.00 USD | `-3.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `678.50` | 3,160,000.00 USD | 0.00 USD | 578.76 USD | `-3.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `679.50` | 3,160,000.00 USD | 0.00 USD | 2,190.00 USD | `-3.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `680.50` | 3,160,000.00 USD | 0.00 USD | 36,110.00 USD | `-3.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `681.50` | 3,120,000.00 USD | 0.00 USD | 19,910.00 USD | `-3.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `682.50` | 3,100,000.00 USD | 0.00 USD | 1,160,000.00 USD | `-3.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `683.50` | 1,940,000.00 USD | 0.00 USD | 5,280.00 USD | `-3.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `684.50` | 1,940,000.00 USD | 0.00 USD | 457.25 USD | `-2.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `685.50` | 1,940,000.00 USD | 0.00 USD | 10,560.00 USD | `-2.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `686.50` | 1,930,000.00 USD | 0.00 USD | 691.99 USD | `-2.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `687.50` | 1,930,000.00 USD | 0.00 USD | 20,970.00 USD | `-2.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `688.50` | 1,910,000.00 USD | 0.00 USD | 107.41 USD | `-2.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `689.50` | 1,900,000.00 USD | 0.00 USD | 63,840.00 USD | `-2.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `690.50` | 1,840,000.00 USD | 0.00 USD | 3,060.00 USD | `-2.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `691.50` | 1,840,000.00 USD | 0.00 USD | 691.50 USD | `-1.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `692.50` | 1,840,000.00 USD | 0.00 USD | 2,300.00 USD | `-1.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `693.50` | 1,840,000.00 USD | 0.00 USD | 1,350.00 USD | `-1.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `694.50` | 1,830,000.00 USD | 0.00 USD | 158.35 USD | `-1.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `695.50` | 1,830,000.00 USD | 0.00 USD | 167,560.00 USD | `-1.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `696.50` | 1,670,000.00 USD | 0.00 USD | 2,450.00 USD | `-1.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `697.50` | 1,660,000.00 USD | 0.00 USD | 34,560.00 USD | `-1.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `698.50` | 1,630,000.00 USD | 0.00 USD | 4,740.00 USD | `-0.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `699.50` | 1,620,000.00 USD | 0.00 USD | 49,360.00 USD | `-0.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `700.50` | 1,570,000.00 USD | 0.00 USD | 475,940.00 USD | `-0.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `701.50` | 1,100,000.00 USD | 0.00 USD | 894,950.00 USD | `-0.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `702.50` | 203,960.00 USD | 0.00 USD | 6,960.00 USD | `-0.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `703.50` | 197,000.00 USD | 0.00 USD | 110,090.00 USD | `-0.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `704.50` | 86,910.00 USD | 0.00 USD | 86,910.00 USD | `-0.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `705.50` | 4,280.00 USD | 4,280.00 USD | 0.00 USD | `+0.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `706.50` | 1,400,000.00 USD | 1,390,000.00 USD | 0.00 USD | `+0.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `707.50` | 1,510,000.00 USD | 116,450.00 USD | 0.00 USD | `+0.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `708.50` | 1,540,000.00 USD | 24,640.00 USD | 0.00 USD | `+0.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `709.50` | 1,540,000.00 USD | 1,490.00 USD | 0.00 USD | `+0.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `710.50` | 1,550,000.00 USD | 5,190.00 USD | 0.00 USD | `+0.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `711.50` | 1,550,000.00 USD | 1,320.00 USD | 0.00 USD | `+0.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `712.50` | 1,550,000.00 USD | 5,850.00 USD | 0.00 USD | `+1.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `713.50` | 1,640,000.00 USD | 89,180.00 USD | 0.00 USD | `+1.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `714.50` | 1,640,000.00 USD | 2,090.00 USD | 0.00 USD | `+1.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `715.50` | 1,640,000.00 USD | 736.97 USD | 0.00 USD | `+1.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `716.50` | 1,810,000.00 USD | 162,970.00 USD | 0.00 USD | `+1.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `717.50` | 1,810,000.00 USD | 3,020.00 USD | 0.00 USD | `+1.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `718.50` | 1,810,000.00 USD | 3,290.00 USD | 0.00 USD | `+1.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `719.50` | 1,870,000.00 USD | 53,870.00 USD | 0.00 USD | `+2.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `720.50` | 1,890,000.00 USD | 18,010.00 USD | 0.00 USD | `+2.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `721.50` | 1,890,000.00 USD | 2,050.00 USD | 0.00 USD | `+2.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `722.50` | 1,920,000.00 USD | 33,170.00 USD | 0.00 USD | `+2.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `723.50` | 1,930,000.00 USD | 9,930.00 USD | 0.00 USD | `+2.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `724.50` | 1,930,000.00 USD | 606.41 USD | 0.00 USD | `+2.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `725.50` | 1,970,000.00 USD | 34,660.00 USD | 0.00 USD | `+2.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `726.50` | 1,970,000.00 USD | 3,610.00 USD | 0.00 USD | `+3.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `727.50` | 1,980,000.00 USD | 13,920.00 USD | 0.00 USD | `+3.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `728.50` | 2,030,000.00 USD | 46,570.00 USD | 0.00 USD | `+3.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `729.50` | 2,170,000.00 USD | 137,880.00 USD | 0.00 USD | `+3.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `730.50` | 2,360,000.00 USD | 193,600.00 USD | 0.00 USD | `+3.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `731.50` | 2,600,000.00 USD | 239,120.00 USD | 0.00 USD | `+3.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `732.50` | 2,600,000.00 USD | 1,670.00 USD | 0.00 USD | `+3.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `733.50` | 3,090,000.00 USD | 486,710.00 USD | 0.00 USD | `+4.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `734.50` | 3,120,000.00 USD | 29,420.00 USD | 0.00 USD | `+4.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `735.50` | 3,130,000.00 USD | 14,030.00 USD | 0.00 USD | `+4.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `736.50` | 3,150,000.00 USD | 16,670.00 USD | 0.00 USD | `+4.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `737.50` | 3,150,000.00 USD | 3,970.00 USD | 0.00 USD | `+4.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `738.50` | 3,170,000.00 USD | 12,620.00 USD | 0.00 USD | `+4.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `739.50` | 3,170,000.00 USD | 790.53 USD | 0.00 USD | `+4.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `740.50` | 3,170,000.00 USD | 133.29 USD | 0.00 USD | `+5.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `741.50` | 3,170,000.00 USD | 1,590.00 USD | 0.00 USD | `+5.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `742.50` | 3,420,000.00 USD | 247,900.00 USD | 0.00 USD | `+5.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `743.50` | 3,500,000.00 USD | 87,580.00 USD | 0.00 USD | `+5.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `744.50` | 3,670,000.00 USD | 165,040.00 USD | 0.00 USD | `+5.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `745.50` | 3,690,000.00 USD | 19,020.00 USD | 0.00 USD | `+5.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `746.50` | 3,690,000.00 USD | 672.60 USD | 0.00 USD | `+5.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `747.50` | 3,690,000.00 USD | 1,070.00 USD | 0.00 USD | `+6.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `748.50` | 3,990,000.00 USD | 299,400.00 USD | 0.00 USD | `+6.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `749.50` | 3,990,000.00 USD | 3,530.00 USD | 0.00 USD | `+6.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `750.50` | 4,000,000.00 USD | 4,230.00 USD | 0.00 USD | `+6.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `751.50` | 4,000,000.00 USD | 4,830.00 USD | 0.00 USD | `+6.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `752.50` | 4,000,000.00 USD | 2,730.00 USD | 0.00 USD | `+6.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `753.50` | 4,010,000.00 USD | 327.77 USD | 0.00 USD | `+6.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `754.50` | 4,050,000.00 USD | 47,160.00 USD | 0.00 USD | `+7.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `755.50` | 4,060,000.00 USD | 4,420.00 USD | 0.00 USD | `+7.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `756.50` | 4,070,000.00 USD | 12,380.00 USD | 0.00 USD | `+7.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `757.50` | 4,210,000.00 USD | 142,940.00 USD | 0.00 USD | `+7.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `758.50` | 4,210,000.00 USD | 136.53 USD | 0.00 USD | `+7.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `759.50` | 4,230,000.00 USD | 21,350.00 USD | 0.00 USD | `+7.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `760.50` | 4,260,000.00 USD | 30,480.00 USD | 0.00 USD | `+7.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `761.50` | 4,280,000.00 USD | 11,460.00 USD | 0.00 USD | `+8.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `762.50` | 4,280,000.00 USD | 274.50 USD | 0.00 USD | `+8.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `763.50` | 4,470,000.00 USD | 190,180.00 USD | 0.00 USD | `+8.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `764.50` | 4,470,000.00 USD | 600.13 USD | 0.00 USD | `+8.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `765.50` | 4,510,000.00 USD | 40,940.00 USD | 0.00 USD | `+8.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `766.50` | 4,510,000.00 USD | 600.94 USD | 0.00 USD | `+8.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `767.50` | 4,980,000.00 USD | 468,180.00 USD | 0.00 USD | `+8.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `768.50` | 4,980,000.00 USD | 180.60 USD | 0.00 USD | `+9.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `769.50` | 4,980,000.00 USD | 171.60 USD | 0.00 USD | `+9.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `770.50` | 4,980,000.00 USD | 1,980.00 USD | 0.00 USD | `+9.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `771.50` | 4,980,000.00 USD | 219.88 USD | 0.00 USD | `+9.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `772.50` | 4,980,000.00 USD | 516.03 USD | 0.00 USD | `+9.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `773.50` | 4,980,000.00 USD | 1,240.00 USD | 0.00 USD | `+9.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `774.50` | 4,990,000.00 USD | 9,680.00 USD | 0.00 USD | `+9.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `775.50` | 4,990,000.00 USD | 2,240.00 USD | 0.00 USD | `+10.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `776.50` | 5,010,000.00 USD | 14,230.00 USD | 0.00 USD | `+10.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `777.50` | 5,020,000.00 USD | 15,690.00 USD | 0.00 USD | `+10.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `778.50` | 5,030,000.00 USD | 4,580.00 USD | 0.00 USD | `+10.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `779.50` | 5,030,000.00 USD | 6,420.00 USD | 0.00 USD | `+10.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `780.50` | 5,060,000.00 USD | 25,520.00 USD | 0.00 USD | `+10.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `781.50` | 5,060,000.00 USD | 2,570.00 USD | 0.00 USD | `+10.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `782.50` | 5,060,000.00 USD | 1,900.00 USD | 0.00 USD | `+11.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `783.50` | 5,470,000.00 USD | 407,870.00 USD | 0.00 USD | `+11.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `784.50` | 5,470,000.00 USD | 106.69 USD | 0.00 USD | `+11.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `785.50` | 5,470,000.00 USD | 559.28 USD | 0.00 USD | `+11.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `786.50` | 5,470,000.00 USD | 366.51 USD | 0.00 USD | `+11.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `787.50` | 5,470,000.00 USD | 2,370.00 USD | 0.00 USD | `+11.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `788.50` | 5,470,000.00 USD | 133.26 USD | 0.00 USD | `+11.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `790.50` | 5,480,000.00 USD | 4,190.00 USD | 0.00 USD | `+12.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `791.50` | 5,480,000.00 USD | 704.44 USD | 0.00 USD | `+12.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `792.50` | 5,480,000.00 USD | 4,360.00 USD | 0.00 USD | `+12.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `793.50` | 5,490,000.00 USD | 1,450.00 USD | 0.00 USD | `+12.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `794.50` | 5,490,000.00 USD | 3,630.00 USD | 0.00 USD | `+12.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `795.50` | 5,490,000.00 USD | 3,040.00 USD | 0.00 USD | `+12.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `796.50` | 5,490,000.00 USD | 154.52 USD | 0.00 USD | `+13.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `799.50` | 5,490,000.00 USD | 1,450.00 USD | 0.00 USD | `+13.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `800.50` | 5,510,000.00 USD | 12,890.00 USD | 0.00 USD | `+13.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `803.50` | 5,510,000.00 USD | 803.50 USD | 0.00 USD | `+14.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `805.50` | 5,510,000.00 USD | 120.02 USD | 0.00 USD | `+14.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `806.50` | 5,510,000.00 USD | 1,300.00 USD | 0.00 USD | `+14.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `808.50` | 5,510,000.00 USD | 3,390.00 USD | 0.00 USD | `+14.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `809.50` | 5,510,000.00 USD | 242.04 USD | 0.00 USD | `+14.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `810.50` | 5,530,000.00 USD | 15,790.00 USD | 0.00 USD | `+14.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `811.50` | 5,530,000.00 USD | 374.10 USD | 0.00 USD | `+15.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `812.50` | 5,530,000.00 USD | 844.19 USD | 0.00 USD | `+15.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `813.50` | 5,530,000.00 USD | 109.82 USD | 0.00 USD | `+15.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `814.50` | 5,530,000.00 USD | 3,210.00 USD | 0.00 USD | `+15.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `816.50` | 5,530,000.00 USD | 984.70 USD | 0.00 USD | `+15.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `817.50` | 5,530,000.00 USD | 162.68 USD | 0.00 USD | `+15.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `818.50` | 5,540,000.00 USD | 5,990.00 USD | 0.00 USD | `+16.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `820.50` | 5,550,000.00 USD | 8,230.00 USD | 0.00 USD | `+16.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `824.50` | 5,550,000.00 USD | 408.13 USD | 0.00 USD | `+16.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `826.50` | 5,550,000.00 USD | 672.77 USD | 0.00 USD | `+17.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `827.50` | 5,550,000.00 USD | 276.38 USD | 0.00 USD | `+17.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `828.50` | 5,550,000.00 USD | 1,800.00 USD | 0.00 USD | `+17.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `830.50` | 5,590,000.00 USD | 35,850.00 USD | 0.00 USD | `+17.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `833.50` | 5,590,000.00 USD | 1,200.00 USD | 0.00 USD | `+18.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `835.50` | 5,590,000.00 USD | 187.15 USD | 0.00 USD | `+18.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `836.50` | 5,590,000.00 USD | 372.24 USD | 0.00 USD | `+18.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `837.50` | 5,590,000.00 USD | 326.62 USD | 0.00 USD | `+18.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `839.50` | 5,590,000.00 USD | 296.34 USD | 0.00 USD | `+19.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `840.50` | 5,590,000.00 USD | 441.26 USD | 0.00 USD | `+19.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `841.50` | 5,590,000.00 USD | 329.87 USD | 0.00 USD | `+19.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `843.50` | 5,590,000.00 USD | 425.97 USD | 0.00 USD | `+19.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `844.50` | 5,590,000.00 USD | 1,770.00 USD | 0.00 USD | `+19.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `850.50` | 5,600,000.00 USD | 2,550.00 USD | 0.00 USD | `+20.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `851.50` | 5,610,000.00 USD | 11,650.00 USD | 0.00 USD | `+20.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `852.50` | 5,610,000.00 USD | 102.30 USD | 0.00 USD | `+20.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `854.50` | 5,610,000.00 USD | 137.57 USD | 0.00 USD | `+21.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `857.50` | 5,610,000.00 USD | 1,200.00 USD | 0.00 USD | `+21.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `860.50` | 5,610,000.00 USD | 1,160.00 USD | 0.00 USD | `+22.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `862.50` | 5,610,000.00 USD | 1,200.00 USD | 0.00 USD | `+22.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `863.50` | 5,610,000.00 USD | 874.73 USD | 0.00 USD | `+22.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `864.50` | 5,610,000.00 USD | 2,970.00 USD | 0.00 USD | `+22.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `865.50` | 5,620,000.00 USD | 3,460.00 USD | 0.00 USD | `+22.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `868.50` | 5,620,000.00 USD | 2,610.00 USD | 0.00 USD | `+23.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `870.50` | 5,620,000.00 USD | 228.07 USD | 0.00 USD | `+23.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `872.50` | 5,620,000.00 USD | 1,110.00 USD | 0.00 USD | `+23.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `874.50` | 5,620,000.00 USD | 582.42 USD | 0.00 USD | `+24.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `884.50` | 5,680,000.00 USD | 54,820.00 USD | 0.00 USD | `+25.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `888.50` | 5,680,000.00 USD | 266.55 USD | 0.00 USD | `+26.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `890.50` | 5,680,000.00 USD | 690.14 USD | 0.00 USD | `+26.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `891.50` | 5,680,000.00 USD | 605.33 USD | 0.00 USD | `+26.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `900.50` | 5,810,000.00 USD | 126,250.00 USD | 0.00 USD | `+27.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `907.50` | 5,810,000.00 USD | 1,640.00 USD | 0.00 USD | `+28.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `914.50` | 5,810,000.00 USD | 4,150.00 USD | 0.00 USD | `+29.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `917.50` | 5,810,000.00 USD | 533.99 USD | 0.00 USD | `+30.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `919.50` | 5,810,000.00 USD | 166.43 USD | 0.00 USD | `+30.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `920.50` | 5,810,000.00 USD | 463.01 USD | 0.00 USD | `+30.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `926.50` | 5,810,000.00 USD | 320.57 USD | 0.00 USD | `+31.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `929.50` | 5,840,000.00 USD | 24,800.00 USD | 0.00 USD | `+31.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `930.50` | 5,840,000.00 USD | 552.72 USD | 0.00 USD | `+32.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `933.50` | 5,840,000.00 USD | 196.03 USD | 0.00 USD | `+32.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `935.50` | 5,840,000.00 USD | 287.20 USD | 0.00 USD | `+32.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `958.50` | 5,840,000.00 USD | 782.14 USD | 0.00 USD | `+35.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `959.50` | 5,840,000.00 USD | 498.94 USD | 0.00 USD | `+36.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `965.50` | 5,840,000.00 USD | 1,930.00 USD | 0.00 USD | `+36.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `977.50` | 5,840,000.00 USD | 293.25 USD | 0.00 USD | `+38.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `980.50` | 5,840,000.00 USD | 1,300.00 USD | 0.00 USD | `+39.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `981.50` | 5,840,000.00 USD | 109.93 USD | 0.00 USD | `+39.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `984.50` | 5,840,000.00 USD | 439.09 USD | 0.00 USD | `+39.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `987.50` | 5,850,000.00 USD | 2,590.00 USD | 0.00 USD | `+40.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `997.50` | 5,850,000.00 USD | 1,800.00 USD | 0.00 USD | `+41.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `998.50` | 5,850,000.00 USD | 3,990.00 USD | 0.00 USD | `+41.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `999.50` | 5,850,000.00 USD | 938.53 USD | 0.00 USD | `+41.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1000.50` | 5,860,000.00 USD | 11,810.00 USD | 0.00 USD | `+41.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1017.50` | 5,860,000.00 USD | 203.50 USD | 0.00 USD | `+44.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1045.50` | 5,870,000.00 USD | 195.51 USD | 0.00 USD | `+48.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1053.50` | 5,870,000.00 USD | 149.60 USD | 0.00 USD | `+49.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1100.50` | 5,870,000.00 USD | 278.43 USD | 0.00 USD | `+56.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1111.50` | 5,870,000.00 USD | 555.75 USD | 0.00 USD | `+57.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1136.50` | 5,870,000.00 USD | 165.93 USD | 0.00 USD | `+61.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1146.50` | 5,870,000.00 USD | 167.39 USD | 0.00 USD | `+62.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1200.50` | 5,930,000.00 USD | 62,330.00 USD | 0.00 USD | `+70.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1202.50` | 5,930,000.00 USD | 1,250.00 USD | 0.00 USD | `+70.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1226.50` | 5,930,000.00 USD | 235.49 USD | 0.00 USD | `+74.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1230.50` | 5,930,000.00 USD | 3,580.00 USD | 0.00 USD | `+74.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1250.50` | 5,930,000.00 USD | 421.42 USD | 0.00 USD | `+77.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1280.50` | 5,940,000.00 USD | 3,750.00 USD | 0.00 USD | `+81.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1297.50` | 5,940,000.00 USD | 133.64 USD | 0.00 USD | `+84.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1300.50` | 5,940,000.00 USD | 685.36 USD | 0.00 USD | `+84.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1330.50` | 6,000,000.00 USD | 58,230.00 USD | 0.00 USD | `+88.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1340.50` | 6,080,000.00 USD | 80,850.00 USD | 0.00 USD | `+90.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1360.50` | 6,080,000.00 USD | 6,210.00 USD | 0.00 USD | `+93.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1363.50` | 6,090,000.00 USD | 2,180.00 USD | 0.00 USD | `+93.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1370.50` | 6,090,000.00 USD | 1,060.00 USD | 0.00 USD | `+94.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1372.50` | 6,110,000.00 USD | 19,210.00 USD | 0.00 USD | `+94.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1389.50` | 6,110,000.00 USD | 425.19 USD | 0.00 USD | `+97.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1400.50` | 6,110,000.00 USD | 3,850.00 USD | 0.00 USD | `+98.69%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `630.80` | 38,600,000.00 USD | 0.00 USD | 38,600,000.00 USD | 0.00 USD | 44,070.00 USD | 318,080.00 USD |
| `1D` | `631.70` | 38,230,000.00 USD | 0.00 USD | 38,230,000.00 USD | 28,120.00 USD | 49,490.00 USD | 557,590.00 USD |
| `1D` | `632.60` | 37,600,000.00 USD | 0.00 USD | 37,600,000.00 USD | 575,630.00 USD | 54,360.00 USD | 40,920.00 USD |
| `1D` | `633.50` | 36,930,000.00 USD | 0.00 USD | 36,930,000.00 USD | 7,730.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `634.40` | 36,920,000.00 USD | 0.00 USD | 36,920,000.00 USD | 20,270.00 USD | 23,580.00 USD | 0.00 USD |
| `1D` | `635.30` | 36,880,000.00 USD | 0.00 USD | 36,880,000.00 USD | 0.00 USD | 0.00 USD | 76,410.00 USD |
| `1D` | `636.20` | 36,800,000.00 USD | 0.00 USD | 36,800,000.00 USD | 0.00 USD | 40,910.00 USD | 0.00 USD |
| `1D` | `637.10` | 36,760,000.00 USD | 0.00 USD | 36,760,000.00 USD | 101,910.00 USD | 0.00 USD | 236,370.00 USD |
| `1D` | `638.90` | 36,420,000.00 USD | 0.00 USD | 36,420,000.00 USD | 145,780.00 USD | 37,610.00 USD | 0.00 USD |
| `1D` | `639.80` | 36,240,000.00 USD | 0.00 USD | 36,240,000.00 USD | 38,320.00 USD | 0.00 USD | 184,710.00 USD |
| `1D` | `641.60` | 36,010,000.00 USD | 0.00 USD | 36,010,000.00 USD | 33,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `642.50` | 35,980,000.00 USD | 0.00 USD | 35,980,000.00 USD | 116,460.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `644.30` | 35,860,000.00 USD | 0.00 USD | 35,860,000.00 USD | 308,550.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `645.20` | 35,560,000.00 USD | 0.00 USD | 35,560,000.00 USD | 0.00 USD | 0.00 USD | 341,610.00 USD |
| `1D` | `646.10` | 35,210,000.00 USD | 0.00 USD | 35,210,000.00 USD | 87,020.00 USD | 0.00 USD | 140,640.00 USD |
| `1D` | `647.00` | 34,990,000.00 USD | 0.00 USD | 34,990,000.00 USD | 158,720.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `647.90` | 34,830,000.00 USD | 0.00 USD | 34,830,000.00 USD | 78,540.00 USD | 29,080.00 USD | 0.00 USD |
| `1D` | `648.80` | 34,720,000.00 USD | 0.00 USD | 34,720,000.00 USD | 92,180.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `651.50` | 34,630,000.00 USD | 0.00 USD | 34,630,000.00 USD | 106,810.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `652.40` | 34,520,000.00 USD | 0.00 USD | 34,520,000.00 USD | 0.00 USD | 0.00 USD | 94,590.00 USD |
| `1D` | `653.30` | 34,430,000.00 USD | 0.00 USD | 34,430,000.00 USD | 0.00 USD | 26,830.00 USD | 0.00 USD |
| `1D` | `654.20` | 34,400,000.00 USD | 0.00 USD | 34,400,000.00 USD | 73,900.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `655.10` | 34,330,000.00 USD | 0.00 USD | 34,330,000.00 USD | 88,130.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `656.00` | 34,240,000.00 USD | 0.00 USD | 34,240,000.00 USD | 120,150.00 USD | 0.00 USD | 87,310.00 USD |
| `1D` | `656.90` | 34,030,000.00 USD | 0.00 USD | 34,030,000.00 USD | 76,140.00 USD | 21,320.00 USD | 738,390.00 USD |
| `1D` | `657.80` | 33,190,000.00 USD | 0.00 USD | 33,190,000.00 USD | 833,200.00 USD | 14,920.00 USD | 0.00 USD |
| `1D` | `658.70` | 32,350,000.00 USD | 0.00 USD | 32,350,000.00 USD | 81,060.00 USD | 0.00 USD | 81,440.00 USD |
| `1D` | `659.60` | 32,180,000.00 USD | 0.00 USD | 32,180,000.00 USD | 0.00 USD | 7,460.00 USD | 0.00 USD |
| `1D` | `660.50` | 32,180,000.00 USD | 0.00 USD | 32,180,000.00 USD | 90,670.00 USD | 0.00 USD | 14,670.00 USD |
| `1D` | `661.40` | 32,070,000.00 USD | 0.00 USD | 32,070,000.00 USD | 439,070.00 USD | 83,170.00 USD | 0.00 USD |
| `1D` | `662.30` | 31,550,000.00 USD | 0.00 USD | 31,550,000.00 USD | 6,140.00 USD | 87,740.00 USD | 0.00 USD |
| `1D` | `663.20` | 31,450,000.00 USD | 0.00 USD | 31,450,000.00 USD | 202,560.00 USD | 5,000.00 USD | 19,650.00 USD |
| `1D` | `664.10` | 31,230,000.00 USD | 0.00 USD | 31,230,000.00 USD | 45,960.00 USD | 48,410.00 USD | 21,160.00 USD |
| `7D` | `664.10` | 87,050,000.00 USD | 0.00 USD | 87,050,000.00 USD | 78,740.00 USD | 18,740.00 USD | 39,340.00 USD |
| `1D` | `665.00` | 31,110,000.00 USD | 0.00 USD | 31,110,000.00 USD | 1,160,000.00 USD | 0.00 USD | 8,070.00 USD |
| `7D` | `665.00` | 86,910,000.00 USD | 0.00 USD | 86,910,000.00 USD | 92,030.00 USD | 22,990.00 USD | 37,000.00 USD |
| `1D` | `665.90` | 29,940,000.00 USD | 0.00 USD | 29,940,000.00 USD | 682,590.00 USD | 93,330.00 USD | 688,480.00 USD |
| `7D` | `665.90` | 86,760,000.00 USD | 0.00 USD | 86,760,000.00 USD | 264,020.00 USD | 71,380.00 USD | 63,410.00 USD |
| `1D` | `666.80` | 28,480,000.00 USD | 0.00 USD | 28,480,000.00 USD | 805,530.00 USD | 13,270.00 USD | 11,380.00 USD |
| `7D` | `666.80` | 86,360,000.00 USD | 0.00 USD | 86,360,000.00 USD | 198,550.00 USD | 33,320.00 USD | 61,710.00 USD |
| `1D` | `667.70` | 27,650,000.00 USD | 0.00 USD | 27,650,000.00 USD | 181,040.00 USD | 115,700.00 USD | 9,290.00 USD |
| `7D` | `667.70` | 86,070,000.00 USD | 0.00 USD | 86,070,000.00 USD | 199,690.00 USD | 45,130.00 USD | 51,340.00 USD |
| `1D` | `668.60` | 27,340,000.00 USD | 0.00 USD | 27,340,000.00 USD | 581,120.00 USD | 25,520.00 USD | 3,620.00 USD |
| `7D` | `668.60` | 85,770,000.00 USD | 0.00 USD | 85,770,000.00 USD | 387,530.00 USD | 92,860.00 USD | 51,060.00 USD |
| `1D` | `669.50` | 26,730,000.00 USD | 0.00 USD | 26,730,000.00 USD | 116,800.00 USD | 61,020.00 USD | 10,960.00 USD |
| `7D` | `669.50` | 85,240,000.00 USD | 0.00 USD | 85,240,000.00 USD | 341,150.00 USD | 38,130.00 USD | 108,970.00 USD |
| `1D` | `670.40` | 26,540,000.00 USD | 0.00 USD | 26,540,000.00 USD | 255,530.00 USD | 0.00 USD | 1,480,000.00 USD |
| `7D` | `670.40` | 84,750,000.00 USD | 0.00 USD | 84,750,000.00 USD | 319,660.00 USD | 93,800.00 USD | 77,380.00 USD |
| `1D` | `671.30` | 24,810,000.00 USD | 0.00 USD | 24,810,000.00 USD | 124,990.00 USD | 11,440.00 USD | 16,650.00 USD |
| `7D` | `671.30` | 84,260,000.00 USD | 0.00 USD | 84,260,000.00 USD | 335,750.00 USD | 57,500.00 USD | 42,050.00 USD |
| `1D` | `672.20` | 24,660,000.00 USD | 0.00 USD | 24,660,000.00 USD | 1,990,000.00 USD | 8,400.00 USD | 29,210.00 USD |
| `7D` | `672.20` | 83,830,000.00 USD | 0.00 USD | 83,830,000.00 USD | 180,230.00 USD | 62,620.00 USD | 74,250.00 USD |
| `1D` | `673.10` | 22,630,000.00 USD | 0.00 USD | 22,630,000.00 USD | 348,680.00 USD | 259,540.00 USD | 824,720.00 USD |
| `7D` | `673.10` | 83,510,000.00 USD | 0.00 USD | 83,510,000.00 USD | 394,120.00 USD | 64,970.00 USD | 42,710.00 USD |
| `1D` | `674.00` | 21,190,000.00 USD | 0.00 USD | 21,190,000.00 USD | 305,330.00 USD | 90,530.00 USD | 1,560,000.00 USD |
| `7D` | `674.00` | 83,010,000.00 USD | 0.00 USD | 83,010,000.00 USD | 335,670.00 USD | 105,910.00 USD | 80,360.00 USD |
| `1D` | `674.90` | 19,240,000.00 USD | 0.00 USD | 19,240,000.00 USD | 1,270,000.00 USD | 366,740.00 USD | 431,050.00 USD |
| `7D` | `674.90` | 82,490,000.00 USD | 0.00 USD | 82,490,000.00 USD | 247,070.00 USD | 31,490.00 USD | 44,420.00 USD |
| `1D` | `675.80` | 17,180,000.00 USD | 0.00 USD | 17,180,000.00 USD | 1,010,000.00 USD | 33,210.00 USD | 209,130.00 USD |
| `7D` | `675.80` | 82,160,000.00 USD | 0.00 USD | 82,160,000.00 USD | 387,400.00 USD | 26,020.00 USD | 79,190.00 USD |
| `1D` | `676.70` | 15,920,000.00 USD | 0.00 USD | 15,920,000.00 USD | 359,550.00 USD | 265,020.00 USD | 50,290.00 USD |
| `7D` | `676.70` | 81,670,000.00 USD | 0.00 USD | 81,670,000.00 USD | 509,100.00 USD | 35,490.00 USD | 126,570.00 USD |
| `1D` | `677.60` | 15,250,000.00 USD | 0.00 USD | 15,250,000.00 USD | 350,710.00 USD | 118,540.00 USD | 250,200.00 USD |
| `7D` | `677.60` | 81,000,000.00 USD | 0.00 USD | 81,000,000.00 USD | 409,810.00 USD | 0.00 USD | 63,990.00 USD |
| `1D` | `678.50` | 14,530,000.00 USD | 0.00 USD | 14,530,000.00 USD | 1,030,000.00 USD | 111,460.00 USD | 0.00 USD |
| `7D` | `678.50` | 80,530,000.00 USD | 0.00 USD | 80,530,000.00 USD | 120,190.00 USD | 0.00 USD | 26,990.00 USD |
| `1D` | `679.40` | 13,390,000.00 USD | 0.00 USD | 13,390,000.00 USD | 1,200,000.00 USD | 9,770.00 USD | 0.00 USD |
| `7D` | `679.40` | 80,380,000.00 USD | 0.00 USD | 80,380,000.00 USD | 116,510.00 USD | 10,480.00 USD | 40,610.00 USD |
| `1D` | `680.30` | 12,180,000.00 USD | 0.00 USD | 12,180,000.00 USD | 0.00 USD | 157,270.00 USD | 0.00 USD |
| `7D` | `680.30` | 80,210,000.00 USD | 0.00 USD | 80,210,000.00 USD | 166,780.00 USD | 13,510.00 USD | 0.00 USD |
| `1D` | `681.20` | 12,020,000.00 USD | 0.00 USD | 12,020,000.00 USD | 13,940.00 USD | 167,420.00 USD | 0.00 USD |
| `7D` | `681.20` | 80,030,000.00 USD | 0.00 USD | 80,030,000.00 USD | 106,280.00 USD | 7,050.00 USD | 35,170.00 USD |
| `1D` | `682.10` | 11,840,000.00 USD | 0.00 USD | 11,840,000.00 USD | 33,390.00 USD | 232,770.00 USD | 0.00 USD |
| `7D` | `682.10` | 79,880,000.00 USD | 0.00 USD | 79,880,000.00 USD | 0.00 USD | 23,360.00 USD | 27,620.00 USD |
| `1D` | `683.00` | 11,580,000.00 USD | 0.00 USD | 11,580,000.00 USD | 120,530.00 USD | 11,650.00 USD | 0.00 USD |
| `7D` | `683.00` | 79,830,000.00 USD | 0.00 USD | 79,830,000.00 USD | 175,930.00 USD | 28,470.00 USD | 11,520.00 USD |
| `1D` | `683.90` | 11,440,000.00 USD | 0.00 USD | 11,440,000.00 USD | 19,970.00 USD | 157,700.00 USD | 0.00 USD |
| `7D` | `683.90` | 79,620,000.00 USD | 0.00 USD | 79,620,000.00 USD | 77,000.00 USD | 29,510.00 USD | 17,480.00 USD |
| `7D` | `684.80` | 79,490,000.00 USD | 0.00 USD | 79,490,000.00 USD | 246,080.00 USD | 9,850.00 USD | 39,550.00 USD |
| `1D` | `685.70` | 11,270,000.00 USD | 0.00 USD | 11,270,000.00 USD | 684,860.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `685.70` | 79,200,000.00 USD | 0.00 USD | 79,200,000.00 USD | 197,040.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `686.60` | 10,580,000.00 USD | 0.00 USD | 10,580,000.00 USD | 9,210.00 USD | 46,050.00 USD | 0.00 USD |
| `7D` | `686.60` | 79,000,000.00 USD | 0.00 USD | 79,000,000.00 USD | 62,990.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `687.50` | 10,530,000.00 USD | 0.00 USD | 10,530,000.00 USD | 775,320.00 USD | 467,830.00 USD | 4,100,000.00 USD |
| `7D` | `687.50` | 78,940,000.00 USD | 0.00 USD | 78,940,000.00 USD | 148,480.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `688.40` | 5,180,000.00 USD | 0.00 USD | 5,180,000.00 USD | 303,890.00 USD | 105,130.00 USD | 282,600.00 USD |
| `7D` | `688.40` | 78,790,000.00 USD | 0.00 USD | 78,790,000.00 USD | 67,880.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `689.30` | 4,490,000.00 USD | 0.00 USD | 4,490,000.00 USD | 2,200,000.00 USD | 72,370.00 USD | 784,380.00 USD |
| `7D` | `689.30` | 78,720,000.00 USD | 0.00 USD | 78,720,000.00 USD | 84,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `690.20` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 242,130.00 USD | 146,030.00 USD | 234,260.00 USD |
| `7D` | `690.20` | 78,640,000.00 USD | 0.00 USD | 78,640,000.00 USD | 283,920.00 USD | 63,230.00 USD | 82,450.00 USD |
| `1D` | `691.10` | 810,760.00 USD | 0.00 USD | 810,760.00 USD | 167,270.00 USD | 0.00 USD | 306,040.00 USD |
| `7D` | `691.10` | 78,210,000.00 USD | 0.00 USD | 78,210,000.00 USD | 362,020.00 USD | 61,370.00 USD | 81,090.00 USD |
| `1D` | `692.00` | 337,440.00 USD | 0.00 USD | 337,440.00 USD | 5,650.00 USD | 0.00 USD | 194,350.00 USD |
| `7D` | `692.00` | 77,700,000.00 USD | 0.00 USD | 77,700,000.00 USD | 322,430.00 USD | 18,850.00 USD | 58,910.00 USD |
| `7D` | `692.90` | 77,300,000.00 USD | 0.00 USD | 77,300,000.00 USD | 280,830.00 USD | 19,470.00 USD | 0.00 USD |
| `7D` | `693.80` | 77,000,000.00 USD | 0.00 USD | 77,000,000.00 USD | 305,720.00 USD | 39,210.00 USD | 0.00 USD |
| `7D` | `694.70` | 76,660,000.00 USD | 0.00 USD | 76,660,000.00 USD | 279,840.00 USD | 36,640.00 USD | 35,490.00 USD |
| `1D` | `695.60` | 137,440.00 USD | 0.00 USD | 137,440.00 USD | 0.00 USD | 137,440.00 USD | 0.00 USD |
| `7D` | `695.60` | 76,300,000.00 USD | 0.00 USD | 76,300,000.00 USD | 120,440.00 USD | 0.00 USD | 21,670.00 USD |
| `7D` | `696.50` | 76,160,000.00 USD | 0.00 USD | 76,160,000.00 USD | 140,370.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `697.40` | 76,020,000.00 USD | 0.00 USD | 76,020,000.00 USD | 189,100.00 USD | 19,230.00 USD | 0.00 USD |
| `7D` | `698.30` | 75,810,000.00 USD | 0.00 USD | 75,810,000.00 USD | 273,520.00 USD | 33,120.00 USD | 54,800.00 USD |
| `7D` | `699.20` | 75,450,000.00 USD | 0.00 USD | 75,450,000.00 USD | 274,810.00 USD | 12,670.00 USD | 11,820.00 USD |
| `7D` | `700.10` | 75,150,000.00 USD | 0.00 USD | 75,150,000.00 USD | 225,450.00 USD | 40,820.00 USD | 27,440.00 USD |
| `7D` | `701.00` | 74,860,000.00 USD | 0.00 USD | 74,860,000.00 USD | 237,800.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `701.90` | 74,620,000.00 USD | 0.00 USD | 74,620,000.00 USD | 135,260.00 USD | 41,260.00 USD | 89,700.00 USD |
| `7D` | `702.80` | 74,360,000.00 USD | 0.00 USD | 74,360,000.00 USD | 416,820.00 USD | 57,470.00 USD | 36,720.00 USD |
| `1D` | `703.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `703.70` | 73,840,000.00 USD | 0.00 USD | 73,840,000.00 USD | 311,800.00 USD | 44,990.00 USD | 0.00 USD |
| `7D` | `704.60` | 73,490,000.00 USD | 0.00 USD | 73,490,000.00 USD | 537,050.00 USD | 136,550.00 USD | 194,460.00 USD |
| `1D` | `705.50` | 96,830.00 USD | 96,830.00 USD | 0.00 USD | 0.00 USD | 96,830.00 USD | 0.00 USD |
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
| `1D` | `715.40` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 513,890.00 USD | 1,230,000.00 USD |
| `7D` | `715.40` | 59,400,000.00 USD | 0.00 USD | 59,400,000.00 USD | 1,050,000.00 USD | 419,310.00 USD | 329,730.00 USD |
| `1D` | `716.30` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 303,890.00 USD | 345,920.00 USD | 282,600.00 USD |
| `7D` | `716.30` | 57,600,000.00 USD | 0.00 USD | 57,600,000.00 USD | 1,080,000.00 USD | 324,540.00 USD | 233,140.00 USD |
| `1D` | `717.20` | 3,960,000.00 USD | 3,960,000.00 USD | 0.00 USD | 268,080.00 USD | 129,470.00 USD | 784,380.00 USD |
| `7D` | `717.20` | 55,960,000.00 USD | 0.00 USD | 55,960,000.00 USD | 581,610.00 USD | 398,030.00 USD | 387,120.00 USD |
| `1D` | `718.10` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 115,870.00 USD | 234,260.00 USD |
| `7D` | `718.10` | 54,590,000.00 USD | 0.00 USD | 54,590,000.00 USD | 1,690,000.00 USD | 246,320.00 USD | 151,880.00 USD |
| `1D` | `719.00` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 271,410.00 USD | 166,310.00 USD | 0.00 USD |
| `7D` | `719.00` | 52,510,000.00 USD | 0.00 USD | 52,510,000.00 USD | 670,390.00 USD | 137,460.00 USD | 211,490.00 USD |
| `1D` | `719.90` | 5,250,000.00 USD | 5,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 500,390.00 USD |
| `7D` | `719.90` | 51,490,000.00 USD | 0.00 USD | 51,490,000.00 USD | 618,020.00 USD | 173,240.00 USD | 186,780.00 USD |
| `1D` | `720.80` | 5,450,000.00 USD | 5,450,000.00 USD | 0.00 USD | 0.00 USD | 204,540.00 USD | 0.00 USD |
| `7D` | `720.80` | 50,510,000.00 USD | 0.00 USD | 50,510,000.00 USD | 1,010,000.00 USD | 52,490.00 USD | 180,370.00 USD |
| `1D` | `721.70` | 5,530,000.00 USD | 5,530,000.00 USD | 0.00 USD | 0.00 USD | 78,640.00 USD | 0.00 USD |
| `7D` | `721.70` | 49,260,000.00 USD | 0.00 USD | 49,260,000.00 USD | 1,950,000.00 USD | 237,690.00 USD | 653,400.00 USD |
| `7D` | `722.60` | 46,430,000.00 USD | 0.00 USD | 46,430,000.00 USD | 1,930,000.00 USD | 108,200.00 USD | 229,380.00 USD |
| `1D` | `723.50` | 5,830,000.00 USD | 5,830,000.00 USD | 0.00 USD | 0.00 USD | 300,460.00 USD | 0.00 USD |
| `7D` | `723.50` | 44,160,000.00 USD | 0.00 USD | 44,160,000.00 USD | 640,550.00 USD | 140,550.00 USD | 293,670.00 USD |
| `1D` | `724.40` | 5,970,000.00 USD | 5,970,000.00 USD | 0.00 USD | 0.00 USD | 137,440.00 USD | 0.00 USD |
| `7D` | `724.40` | 43,080,000.00 USD | 0.00 USD | 43,080,000.00 USD | 663,550.00 USD | 186,780.00 USD | 130,770.00 USD |
| `1D` | `725.30` | 6,030,000.00 USD | 6,030,000.00 USD | 0.00 USD | 0.00 USD | 57,080.00 USD | 0.00 USD |
| `7D` | `725.30` | 42,100,000.00 USD | 0.00 USD | 42,100,000.00 USD | 1,760,000.00 USD | 418,390.00 USD | 396,690.00 USD |
| `7D` | `726.20` | 39,520,000.00 USD | 0.00 USD | 39,520,000.00 USD | 1,060,000.00 USD | 311,550.00 USD | 460,020.00 USD |
| `1D` | `727.10` | 6,090,000.00 USD | 6,090,000.00 USD | 0.00 USD | 0.00 USD | 64,470.00 USD | 0.00 USD |
| `7D` | `727.10` | 37,690,000.00 USD | 0.00 USD | 37,690,000.00 USD | 1,230,000.00 USD | 331,980.00 USD | 241,010.00 USD |
| `7D` | `728.00` | 35,890,000.00 USD | 0.00 USD | 35,890,000.00 USD | 3,110,000.00 USD | 778,750.00 USD | 388,930.00 USD |
| `1D` | `728.90` | 6,380,000.00 USD | 6,380,000.00 USD | 0.00 USD | 0.00 USD | 133,210.00 USD | 158,290.00 USD |
| `7D` | `728.90` | 31,610,000.00 USD | 0.00 USD | 31,610,000.00 USD | 2,330,000.00 USD | 317,590.00 USD | 644,150.00 USD |
| `1D` | `729.80` | 7,060,000.00 USD | 7,060,000.00 USD | 0.00 USD | 0.00 USD | 147,750.00 USD | 531,810.00 USD |
| `7D` | `729.80` | 28,320,000.00 USD | 0.00 USD | 28,320,000.00 USD | 1,320,000.00 USD | 430,010.00 USD | 339,140.00 USD |
| `1D` | `730.70` | 11,740,000.00 USD | 11,740,000.00 USD | 0.00 USD | 2,650,000.00 USD | 152,870.00 USD | 1,880,000.00 USD |
| `7D` | `730.70` | 26,230,000.00 USD | 0.00 USD | 26,230,000.00 USD | 2,760,000.00 USD | 351,520.00 USD | 587,010.00 USD |
| `1D` | `731.60` | 12,250,000.00 USD | 12,250,000.00 USD | 0.00 USD | 134,040.00 USD | 82,570.00 USD | 289,900.00 USD |
| `7D` | `731.60` | 22,530,000.00 USD | 0.00 USD | 22,530,000.00 USD | 1,530,000.00 USD | 133,980.00 USD | 261,910.00 USD |
| `1D` | `732.50` | 13,570,000.00 USD | 13,570,000.00 USD | 0.00 USD | 430,780.00 USD | 73,020.00 USD | 820,310.00 USD |
| `7D` | `732.50` | 20,610,000.00 USD | 0.00 USD | 20,610,000.00 USD | 465,880.00 USD | 221,510.00 USD | 96,400.00 USD |
| `1D` | `733.40` | 14,630,000.00 USD | 14,630,000.00 USD | 0.00 USD | 703,820.00 USD | 206,790.00 USD | 153,020.00 USD |
| `7D` | `733.40` | 19,820,000.00 USD | 0.00 USD | 19,820,000.00 USD | 1,910,000.00 USD | 158,310.00 USD | 338,540.00 USD |
| `1D` | `734.30` | 15,080,000.00 USD | 15,080,000.00 USD | 0.00 USD | 344,230.00 USD | 0.00 USD | 97,180.00 USD |
| `7D` | `734.30` | 17,420,000.00 USD | 0.00 USD | 17,420,000.00 USD | 1,580,000.00 USD | 288,470.00 USD | 244,940.00 USD |
| `1D` | `735.20` | 15,940,000.00 USD | 15,940,000.00 USD | 0.00 USD | 613,800.00 USD | 246,950.00 USD | 0.00 USD |
| `7D` | `735.20` | 15,310,000.00 USD | 0.00 USD | 15,310,000.00 USD | 1,330,000.00 USD | 172,940.00 USD | 437,510.00 USD |
| `1D` | `736.10` | 17,660,000.00 USD | 17,660,000.00 USD | 0.00 USD | 1,110,000.00 USD | 22,190.00 USD | 590,930.00 USD |
| `7D` | `736.10` | 13,370,000.00 USD | 0.00 USD | 13,370,000.00 USD | 2,130,000.00 USD | 181,990.00 USD | 484,910.00 USD |
| `1D` | `737.00` | 18,060,000.00 USD | 18,060,000.00 USD | 0.00 USD | 407,440.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `737.00` | 10,570,000.00 USD | 0.00 USD | 10,570,000.00 USD | 2,360,000.00 USD | 175,330.00 USD | 633,690.00 USD |
| `1D` | `737.90` | 18,390,000.00 USD | 18,390,000.00 USD | 0.00 USD | 160,280.00 USD | 162,750.00 USD | 0.00 USD |
| `7D` | `737.90` | 7,400,000.00 USD | 0.00 USD | 7,400,000.00 USD | 3,420,000.00 USD | 72,280.00 USD | 374,090.00 USD |
| `1D` | `738.80` | 19,560,000.00 USD | 19,560,000.00 USD | 0.00 USD | 703,680.00 USD | 0.00 USD | 472,930.00 USD |
| `7D` | `738.80` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 522,950.00 USD | 20,210.00 USD | 155,300.00 USD |
| `1D` | `739.70` | 20,620,000.00 USD | 20,620,000.00 USD | 0.00 USD | 590,480.00 USD | 0.00 USD | 461,770.00 USD |
| `7D` | `739.70` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 352,500.00 USD | 0.00 USD | 203,030.00 USD |
| `1D` | `740.60` | 21,070,000.00 USD | 21,070,000.00 USD | 0.00 USD | 302,880.00 USD | 134,150.00 USD | 15,020.00 USD |
| `7D` | `740.60` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 1,090,000.00 USD | 0.00 USD | 33,390.00 USD |
| `1D` | `741.50` | 21,740,000.00 USD | 21,740,000.00 USD | 0.00 USD | 637,650.00 USD | 32,240.00 USD | 0.00 USD |
| `7D` | `741.50` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 257,630.00 USD | 0.00 USD | 208,590.00 USD |
| `7D` | `742.40` | 689,850.00 USD | 0.00 USD | 689,850.00 USD | 0.00 USD | 0.00 USD | 183,920.00 USD |
| `1D` | `743.30` | 21,860,000.00 USD | 21,860,000.00 USD | 0.00 USD | 120,950.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `743.30` | 505,930.00 USD | 0.00 USD | 505,930.00 USD | 0.00 USD | 0.00 USD | 57,580.00 USD |
| `1D` | `744.20` | 22,400,000.00 USD | 22,400,000.00 USD | 0.00 USD | 0.00 USD | 106,580.00 USD | 436,560.00 USD |
| `7D` | `744.20` | 448,350.00 USD | 0.00 USD | 448,350.00 USD | 0.00 USD | 257,580.00 USD | 141,790.00 USD |
| `1D` | `745.10` | 24,500,000.00 USD | 24,500,000.00 USD | 0.00 USD | 1,240,000.00 USD | 0.00 USD | 854,020.00 USD |
| `7D` | `745.10` | 48,980.00 USD | 0.00 USD | 48,980.00 USD | 0.00 USD | 48,980.00 USD | 0.00 USD |
| `7D` | `745.20` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `746.00` | 24,720,000.00 USD | 24,720,000.00 USD | 0.00 USD | 115,270.00 USD | 106,280.00 USD | 0.00 USD |
| `7D` | `746.00` | 999,320.00 USD | 999,320.00 USD | 0.00 USD | 999,320.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `746.90` | 26,020,000.00 USD | 26,020,000.00 USD | 0.00 USD | 499,560.00 USD | 37,280.00 USD | 758,780.00 USD |
| `7D` | `746.90` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 215,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `747.80` | 26,560,000.00 USD | 26,560,000.00 USD | 0.00 USD | 363,640.00 USD | 103,400.00 USD | 73,330.00 USD |
| `1D` | `748.70` | 26,940,000.00 USD | 26,940,000.00 USD | 0.00 USD | 383,190.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `749.60` | 27,310,000.00 USD | 27,310,000.00 USD | 0.00 USD | 368,790.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `750.50` | 27,330,000.00 USD | 27,330,000.00 USD | 0.00 USD | 16,590.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `751.40` | 27,480,000.00 USD | 27,480,000.00 USD | 0.00 USD | 54,450.00 USD | 0.00 USD | 98,240.00 USD |
| `1D` | `752.30` | 27,980,000.00 USD | 27,980,000.00 USD | 0.00 USD | 34,030.00 USD | 25,010.00 USD | 441,380.00 USD |
| `1D` | `753.20` | 28,480,000.00 USD | 28,480,000.00 USD | 0.00 USD | 246,790.00 USD | 3,810.00 USD | 248,870.00 USD |
| `1D` | `754.10` | 28,910,000.00 USD | 28,910,000.00 USD | 0.00 USD | 321,060.00 USD | 50,610.00 USD | 57,280.00 USD |
| `1D` | `755.00` | 29,330,000.00 USD | 29,330,000.00 USD | 0.00 USD | 208,850.00 USD | 178,540.00 USD | 37,120.00 USD |
| `7D` | `755.00` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 59,560.00 USD | 0.00 USD |
| `1D` | `755.90` | 30,050,000.00 USD | 30,050,000.00 USD | 0.00 USD | 550,450.00 USD | 96,170.00 USD | 66,220.00 USD |
| `1D` | `756.80` | 30,230,000.00 USD | 30,230,000.00 USD | 0.00 USD | 110,260.00 USD | 24,970.00 USD | 49,060.00 USD |
| `7D` | `756.80` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 47,340.00 USD | 0.00 USD |
| `1D` | `757.70` | 30,750,000.00 USD | 30,750,000.00 USD | 0.00 USD | 307,310.00 USD | 179,910.00 USD | 32,720.00 USD |
| `7D` | `757.70` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 475,510.00 USD | 113,240.00 USD | 0.00 USD |
| `1D` | `758.60` | 31,640,000.00 USD | 31,640,000.00 USD | 0.00 USD | 542,740.00 USD | 74,280.00 USD | 273,090.00 USD |
| `7D` | `758.60` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `759.50` | 32,860,000.00 USD | 32,860,000.00 USD | 0.00 USD | 1,150,000.00 USD | 61,100.00 USD | 8,370.00 USD |
| `1D` | `760.40` | 33,280,000.00 USD | 33,280,000.00 USD | 0.00 USD | 245,610.00 USD | 97,810.00 USD | 72,300.00 USD |
| `7D` | `760.40` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 0.00 USD | 27,650.00 USD | 42,540.00 USD |
| `1D` | `761.30` | 34,480,000.00 USD | 34,480,000.00 USD | 0.00 USD | 858,450.00 USD | 71,050.00 USD | 269,820.00 USD |
| `7D` | `761.30` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 10,750.00 USD | 211,960.00 USD | 100,630.00 USD |
| `1D` | `762.20` | 35,210,000.00 USD | 35,210,000.00 USD | 0.00 USD | 336,440.00 USD | 172,280.00 USD | 220,780.00 USD |
| `7D` | `762.20` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 699,820.00 USD | 179,270.00 USD |
| `1D` | `763.10` | 38,270,000.00 USD | 38,270,000.00 USD | 0.00 USD | 2,310,000.00 USD | 228,320.00 USD | 522,810.00 USD |
| `7D` | `763.10` | 7,830,000.00 USD | 7,830,000.00 USD | 0.00 USD | 2,460,000.00 USD | 590,460.00 USD | 404,720.00 USD |
| `1D` | `764.00` | 40,170,000.00 USD | 40,170,000.00 USD | 0.00 USD | 1,490,000.00 USD | 165,630.00 USD | 248,000.00 USD |
| `7D` | `764.00` | 10,270,000.00 USD | 10,270,000.00 USD | 0.00 USD | 1,590,000.00 USD | 441,980.00 USD | 402,300.00 USD |
| `1D` | `764.90` | 41,410,000.00 USD | 41,410,000.00 USD | 0.00 USD | 863,310.00 USD | 176,560.00 USD | 199,240.00 USD |
| `7D` | `764.90` | 12,470,000.00 USD | 12,470,000.00 USD | 0.00 USD | 1,450,000.00 USD | 352,570.00 USD | 395,630.00 USD |
| `1D` | `765.80` | 42,870,000.00 USD | 42,870,000.00 USD | 0.00 USD | 1,120,000.00 USD | 123,600.00 USD | 218,700.00 USD |
| `7D` | `765.80` | 15,460,000.00 USD | 15,460,000.00 USD | 0.00 USD | 2,470,000.00 USD | 107,550.00 USD | 416,290.00 USD |
| `1D` | `766.70` | 45,030,000.00 USD | 45,030,000.00 USD | 0.00 USD | 1,540,000.00 USD | 213,220.00 USD | 404,670.00 USD |
| `7D` | `766.70` | 20,050,000.00 USD | 20,050,000.00 USD | 0.00 USD | 3,330,000.00 USD | 416,530.00 USD | 842,330.00 USD |
| `1D` | `767.60` | 47,110,000.00 USD | 47,110,000.00 USD | 0.00 USD | 1,650,000.00 USD | 116,430.00 USD | 311,860.00 USD |
| `7D` | `767.60` | 23,430,000.00 USD | 23,430,000.00 USD | 0.00 USD | 2,790,000.00 USD | 123,530.00 USD | 467,840.00 USD |
| `1D` | `768.50` | 48,580,000.00 USD | 48,580,000.00 USD | 0.00 USD | 1,250,000.00 USD | 71,160.00 USD | 143,500.00 USD |
| `7D` | `768.50` | 25,660,000.00 USD | 25,660,000.00 USD | 0.00 USD | 1,840,000.00 USD | 95,830.00 USD | 281,920.00 USD |
| `1D` | `769.40` | 48,970,000.00 USD | 48,970,000.00 USD | 0.00 USD | 199,400.00 USD | 110,150.00 USD | 84,230.00 USD |
| `7D` | `769.40` | 26,810,000.00 USD | 26,810,000.00 USD | 0.00 USD | 565,780.00 USD | 249,950.00 USD | 333,550.00 USD |
| `1D` | `770.30` | 49,830,000.00 USD | 49,830,000.00 USD | 0.00 USD | 687,740.00 USD | 126,040.00 USD | 43,470.00 USD |
| `7D` | `770.30` | 29,310,000.00 USD | 29,310,000.00 USD | 0.00 USD | 1,900,000.00 USD | 240,530.00 USD | 364,650.00 USD |
| `1D` | `771.20` | 50,740,000.00 USD | 50,740,000.00 USD | 0.00 USD | 425,330.00 USD | 97,820.00 USD | 386,770.00 USD |
| `7D` | `771.20` | 30,770,000.00 USD | 30,770,000.00 USD | 0.00 USD | 1,050,000.00 USD | 242,570.00 USD | 162,680.00 USD |
| `1D` | `772.10` | 51,860,000.00 USD | 51,860,000.00 USD | 0.00 USD | 374,860.00 USD | 100,560.00 USD | 647,240.00 USD |
| `7D` | `772.10` | 33,190,000.00 USD | 33,190,000.00 USD | 0.00 USD | 1,750,000.00 USD | 252,650.00 USD | 419,070.00 USD |
| `1D` | `773.00` | 53,140,000.00 USD | 53,140,000.00 USD | 0.00 USD | 999,790.00 USD | 147,690.00 USD | 134,470.00 USD |
| `7D` | `773.00` | 35,800,000.00 USD | 35,800,000.00 USD | 0.00 USD | 1,950,000.00 USD | 325,680.00 USD | 338,170.00 USD |
| `1D` | `773.90` | 54,440,000.00 USD | 54,440,000.00 USD | 0.00 USD | 1,090,000.00 USD | 105,330.00 USD | 101,760.00 USD |
| `7D` | `773.90` | 37,600,000.00 USD | 37,600,000.00 USD | 0.00 USD | 1,220,000.00 USD | 276,760.00 USD | 293,960.00 USD |
| `1D` | `774.80` | 54,970,000.00 USD | 54,970,000.00 USD | 0.00 USD | 390,270.00 USD | 90,640.00 USD | 56,380.00 USD |
| `7D` | `774.80` | 39,980,000.00 USD | 39,980,000.00 USD | 0.00 USD | 1,310,000.00 USD | 568,930.00 USD | 502,710.00 USD |
| `1D` | `775.70` | 55,600,000.00 USD | 55,600,000.00 USD | 0.00 USD | 392,610.00 USD | 118,020.00 USD | 116,610.00 USD |
| `7D` | `775.70` | 42,470,000.00 USD | 42,470,000.00 USD | 0.00 USD | 1,830,000.00 USD | 470,960.00 USD | 187,170.00 USD |
| `1D` | `776.60` | 56,070,000.00 USD | 56,070,000.00 USD | 0.00 USD | 326,450.00 USD | 34,460.00 USD | 108,780.00 USD |
| `7D` | `776.60` | 44,740,000.00 USD | 44,740,000.00 USD | 0.00 USD | 1,630,000.00 USD | 269,050.00 USD | 378,590.00 USD |
| `1D` | `777.50` | 56,930,000.00 USD | 56,930,000.00 USD | 0.00 USD | 660,150.00 USD | 145,570.00 USD | 54,080.00 USD |
| `7D` | `777.50` | 46,480,000.00 USD | 46,480,000.00 USD | 0.00 USD | 1,350,000.00 USD | 243,990.00 USD | 148,450.00 USD |
| `1D` | `778.40` | 58,320,000.00 USD | 58,320,000.00 USD | 0.00 USD | 949,110.00 USD | 73,550.00 USD | 370,230.00 USD |
| `7D` | `778.40` | 48,170,000.00 USD | 48,170,000.00 USD | 0.00 USD | 1,180,000.00 USD | 307,370.00 USD | 206,530.00 USD |
| `1D` | `779.30` | 59,300,000.00 USD | 59,300,000.00 USD | 0.00 USD | 750,100.00 USD | 76,680.00 USD | 145,140.00 USD |
| `7D` | `779.30` | 49,730,000.00 USD | 49,730,000.00 USD | 0.00 USD | 1,240,000.00 USD | 188,170.00 USD | 123,650.00 USD |
| `1D` | `780.20` | 59,820,000.00 USD | 59,820,000.00 USD | 0.00 USD | 346,940.00 USD | 126,850.00 USD | 47,680.00 USD |
| `7D` | `780.20` | 51,100,000.00 USD | 51,100,000.00 USD | 0.00 USD | 1,070,000.00 USD | 86,470.00 USD | 218,750.00 USD |
| `1D` | `781.10` | 60,730,000.00 USD | 60,730,000.00 USD | 0.00 USD | 628,140.00 USD | 108,280.00 USD | 175,070.00 USD |
| `7D` | `781.10` | 52,710,000.00 USD | 52,710,000.00 USD | 0.00 USD | 1,270,000.00 USD | 90,990.00 USD | 242,450.00 USD |
| `1D` | `782.00` | 61,860,000.00 USD | 61,860,000.00 USD | 0.00 USD | 828,040.00 USD | 27,020.00 USD | 276,100.00 USD |
| `7D` | `782.00` | 54,610,000.00 USD | 54,610,000.00 USD | 0.00 USD | 1,510,000.00 USD | 87,670.00 USD | 301,190.00 USD |
| `1D` | `782.90` | 63,020,000.00 USD | 63,020,000.00 USD | 0.00 USD | 907,340.00 USD | 80,140.00 USD | 176,370.00 USD |
| `7D` | `782.90` | 56,600,000.00 USD | 56,600,000.00 USD | 0.00 USD | 1,750,000.00 USD | 36,140.00 USD | 202,700.00 USD |
| `1D` | `783.80` | 63,490,000.00 USD | 63,490,000.00 USD | 0.00 USD | 429,340.00 USD | 14,770.00 USD | 23,850.00 USD |
| `7D` | `783.80` | 57,170,000.00 USD | 57,170,000.00 USD | 0.00 USD | 508,000.00 USD | 10,100.00 USD | 54,380.00 USD |
| `1D` | `784.70` | 64,090,000.00 USD | 64,090,000.00 USD | 0.00 USD | 544,060.00 USD | 32,520.00 USD | 25,700.00 USD |
| `7D` | `784.70` | 57,480,000.00 USD | 57,480,000.00 USD | 0.00 USD | 208,380.00 USD | 28,260.00 USD | 70,300.00 USD |
| `1D` | `785.60` | 64,300,000.00 USD | 64,300,000.00 USD | 0.00 USD | 179,070.00 USD | 18,950.00 USD | 7,510.00 USD |
| `7D` | `785.60` | 58,610,000.00 USD | 58,610,000.00 USD | 0.00 USD | 1,010,000.00 USD | 54,140.00 USD | 71,180.00 USD |
| `1D` | `786.50` | 64,560,000.00 USD | 64,560,000.00 USD | 0.00 USD | 226,070.00 USD | 15,410.00 USD | 22,730.00 USD |
| `7D` | `786.50` | 59,000,000.00 USD | 59,000,000.00 USD | 0.00 USD | 329,230.00 USD | 30,660.00 USD | 23,970.00 USD |
| `1D` | `787.40` | 64,950,000.00 USD | 64,950,000.00 USD | 0.00 USD | 357,300.00 USD | 8,510.00 USD | 24,380.00 USD |
| `7D` | `787.40` | 59,580,000.00 USD | 59,580,000.00 USD | 0.00 USD | 470,050.00 USD | 17,630.00 USD | 91,050.00 USD |
| `1D` | `788.30` | 65,630,000.00 USD | 65,630,000.00 USD | 0.00 USD | 221,420.00 USD | 52,300.00 USD | 407,330.00 USD |
| `7D` | `788.30` | 59,940,000.00 USD | 59,940,000.00 USD | 0.00 USD | 202,630.00 USD | 82,380.00 USD | 81,230.00 USD |
| `1D` | `789.20` | 66,010,000.00 USD | 66,010,000.00 USD | 0.00 USD | 339,590.00 USD | 21,480.00 USD | 18,230.00 USD |
| `7D` | `789.20` | 60,780,000.00 USD | 60,780,000.00 USD | 0.00 USD | 698,830.00 USD | 81,250.00 USD | 55,990.00 USD |
| `1D` | `790.10` | 66,610,000.00 USD | 66,610,000.00 USD | 0.00 USD | 403,340.00 USD | 28,260.00 USD | 163,110.00 USD |
| `7D` | `790.10` | 61,270,000.00 USD | 61,270,000.00 USD | 0.00 USD | 299,250.00 USD | 104,360.00 USD | 88,890.00 USD |
| `1D` | `791.00` | 66,940,000.00 USD | 66,940,000.00 USD | 0.00 USD | 248,270.00 USD | 73,780.00 USD | 8,530.00 USD |
| `7D` | `791.00` | 62,150,000.00 USD | 62,150,000.00 USD | 0.00 USD | 693,290.00 USD | 82,870.00 USD | 100,420.00 USD |
| `1D` | `791.90` | 67,140,000.00 USD | 67,140,000.00 USD | 0.00 USD | 204,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `791.90` | 63,030,000.00 USD | 63,030,000.00 USD | 0.00 USD | 816,380.00 USD | 16,830.00 USD | 46,300.00 USD |
| `1D` | `792.80` | 67,280,000.00 USD | 67,280,000.00 USD | 0.00 USD | 139,180.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `792.80` | 63,250,000.00 USD | 63,250,000.00 USD | 0.00 USD | 205,450.00 USD | 0.00 USD | 14,670.00 USD |
| `1D` | `793.70` | 67,320,000.00 USD | 67,320,000.00 USD | 0.00 USD | 32,290.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `793.70` | 63,430,000.00 USD | 63,430,000.00 USD | 0.00 USD | 184,960.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `794.60` | 67,340,000.00 USD | 67,340,000.00 USD | 0.00 USD | 21,920.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `794.60` | 63,750,000.00 USD | 63,750,000.00 USD | 0.00 USD | 302,280.00 USD | 15,690.00 USD | 0.00 USD |
| `1D` | `795.50` | 67,380,000.00 USD | 67,380,000.00 USD | 0.00 USD | 43,060.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `795.50` | 63,890,000.00 USD | 63,890,000.00 USD | 0.00 USD | 109,640.00 USD | 14,650.00 USD | 14,200.00 USD |
| `1D` | `796.40` | 67,510,000.00 USD | 67,510,000.00 USD | 0.00 USD | 30,090.00 USD | 0.00 USD | 94,590.00 USD |
| `7D` | `796.40` | 64,030,000.00 USD | 64,030,000.00 USD | 0.00 USD | 139,030.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `797.30` | 67,580,000.00 USD | 67,580,000.00 USD | 0.00 USD | 71,880.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `797.30` | 64,090,000.00 USD | 64,090,000.00 USD | 0.00 USD | 64,670.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `798.20` | 67,660,000.00 USD | 67,660,000.00 USD | 0.00 USD | 53,320.00 USD | 26,830.00 USD | 0.00 USD |
| `7D` | `798.20` | 64,250,000.00 USD | 64,250,000.00 USD | 0.00 USD | 155,890.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `799.10` | 67,670,000.00 USD | 67,670,000.00 USD | 0.00 USD | 15,950.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `799.10` | 64,290,000.00 USD | 64,290,000.00 USD | 0.00 USD | 42,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `800.00` | 67,680,000.00 USD | 67,680,000.00 USD | 0.00 USD | 2,840.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `800.00` | 64,400,000.00 USD | 64,400,000.00 USD | 0.00 USD | 113,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `800.90` | 67,690,000.00 USD | 67,690,000.00 USD | 0.00 USD | 11,140.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `800.90` | 64,510,000.00 USD | 64,510,000.00 USD | 0.00 USD | 77,580.00 USD | 8,370.00 USD | 21,920.00 USD |
| `1D` | `801.80` | 67,800,000.00 USD | 67,800,000.00 USD | 0.00 USD | 27,250.00 USD | 0.00 USD | 87,310.00 USD |
| `7D` | `801.80` | 64,720,000.00 USD | 64,720,000.00 USD | 0.00 USD | 179,900.00 USD | 16,330.00 USD | 10,970.00 USD |
| `1D` | `802.70` | 67,820,000.00 USD | 67,820,000.00 USD | 0.00 USD | 0.00 USD | 21,320.00 USD | 0.00 USD |
| `7D` | `802.70` | 64,730,000.00 USD | 64,730,000.00 USD | 0.00 USD | 11,220.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `803.50` | 67,900,000.00 USD | 67,900,000.00 USD | 0.00 USD | 73,360.00 USD | 0.00 USD | 0.00 USD |
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
  * Total Open Interest: `1.36B` | Total OI Tokens: `1,932,917.8 BNB`
  * 1h OI Change: `+0.39%` | 4h OI Change: `+10.74%` | 24h OI Change: `+6.97%`
  * Exchange Breakdown: Binance=`589.67M` | Bybit=`139.75M` | OKX=`62.19M` | Hyperliquid=`92.96M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-87.58K` | Last 24h: `109.28K` | Last 3d: `307.00K` | Last 7d: `451.01K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0000%` | **USDT OKX** | `-0.0184%` |
| **USDT Bybit** | `-0.0575%` | **USDT KuCoin** | `-0.0212%` |
| **USDT MEXC** | `0.0000%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0002%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0086%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `BNB` | `50.44%` | `49.56%` | `1.02` | 110,780,000.00 USD |
| `15M` | `Binance` | `53.54%` | `46.46%` | `1.15` | 43,500,000.00 USD |
| `15M` | `OKX` | `39.54%` | `60.46%` | `0.65` | 17,020,000.00 USD |
| `15M` | `Bybit` | `43.8%` | `56.2%` | `0.78` | 8,310,000.00 USD |
| `15M` | `KuCoin` | `41.29%` | `58.71%` | `0.70` | 590,120.00 USD |
| `15M` | `Gate` | `48.62%` | `51.38%` | `0.95` | 5,370,000.00 USD |
| `15M` | `Bitget` | `39.57%` | `60.43%` | `0.65` | 4,400,000.00 USD |
| `15M` | `BingX` | `72.48%` | `27.52%` | `2.63` | 7,890,000.00 USD |
| `15M` | `MEXC` | `51.57%` | `48.43%` | `1.06` | 5,630,000.00 USD |
| `15M` | `Bitunix` | `43.63%` | `56.37%` | `0.77` | 4,700,000.00 USD |
| `15M` | `Hyperliquid` | `44.29%` | `55.71%` | `0.80` | 4,380,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `79.44%` | `20.56%` | `3.86` | 2,340,000.00 USD |
| `15M` | `Crypto.com` | `43.82%` | `56.18%` | `0.78` | 229,150.00 USD |
| `15M` | `WhiteBIT` | `5.66%` | `94.34%` | `0.06` | 1,190,000.00 USD |
| `15M` | `HTX` | `63.03%` | `36.97%` | `1.70` | 87,070.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `32.12%` | `67.88%` | `0.47` | 567,150.00 USD |
| `15M` | `Aster` | `63.39%` | `36.61%` | `1.73` | 2,970,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `53.8%` | `46.2%` | `1.16` | 1,620,000.00 USD |
| `15M` | `Whale Positions` | `53.54%` | `46.46%` | `1.15` | 43,500,000.00 USD |
| `15M` | `Global Accounts` | `50.44%` | `49.56%` | `1.02` | 110,780,000.00 USD |
| `1H` | `BNB` | `50.61%` | `49.39%` | `1.02` | 575,500,000.00 USD |
| `1H` | `Binance` | `50.68%` | `49.32%` | `1.03` | 258,470,000.00 USD |
| `1H` | `OKX` | `49.48%` | `50.52%` | `0.98` | 86,360,000.00 USD |
| `1H` | `Bybit` | `46.1%` | `53.9%` | `0.86` | 43,100,000.00 USD |
| `1H` | `KuCoin` | `46.63%` | `53.37%` | `0.87` | 4,130,000.00 USD |
| `1H` | `Gate` | `48.83%` | `51.17%` | `0.95` | 27,490,000.00 USD |
| `1H` | `Bitget` | `45.13%` | `54.87%` | `0.82` | 21,160,000.00 USD |
| `1H` | `BingX` | `56.74%` | `43.26%` | `1.31` | 19,680,000.00 USD |
| `1H` | `MEXC` | `52.16%` | `47.84%` | `1.09` | 26,030,000.00 USD |
| `1H` | `Bitunix` | `51.18%` | `48.82%` | `1.05` | 20,000,000.00 USD |
| `1H` | `Hyperliquid` | `61.79%` | `38.21%` | `1.62` | 31,200,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `59.59%` | `40.41%` | `1.47` | 11,700,000.00 USD |
| `1H` | `Crypto.com` | `48.65%` | `51.35%` | `0.95` | 1,470,000.00 USD |
| `1H` | `WhiteBIT` | `19.77%` | `80.23%` | `0.25` | 5,080,000.00 USD |
| `1H` | `HTX` | `52.63%` | `47.37%` | `1.11` | 604,330.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `34.7%` | `65.3%` | `0.53` | 4,420,000.00 USD |
| `1H` | `Aster` | `56.73%` | `43.27%` | `1.31` | 10,010,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `50.76%` | `49.24%` | `1.03` | 4,610,000.00 USD |
| `1H` | `Whale Positions` | `50.68%` | `49.32%` | `1.03` | 258,470,000.00 USD |
| `1H` | `Global Accounts` | `50.61%` | `49.39%` | `1.02` | 575,500,000.00 USD |
| `4H` | `BNB` | `45.42%` | `54.58%` | `0.83` | 3,960,000,000.00 USD |
| `4H` | `Binance` | `44.85%` | `55.15%` | `0.81` | 1,580,000,000.00 USD |
| `4H` | `OKX` | `46.24%` | `53.76%` | `0.86` | 630,490,000.00 USD |
| `4H` | `Bybit` | `41.73%` | `58.27%` | `0.72` | 427,080,000.00 USD |
| `4H` | `KuCoin` | `47.56%` | `52.44%` | `0.91` | 30,050,000.00 USD |
| `4H` | `Gate` | `47.78%` | `52.22%` | `0.91` | 166,650,000.00 USD |
| `4H` | `Bitget` | `42.65%` | `57.35%` | `0.74` | 145,360,000.00 USD |
| `4H` | `BingX` | `47.88%` | `52.12%` | `0.92` | 132,450,000.00 USD |
| `4H` | `MEXC` | `50.57%` | `49.43%` | `1.02` | 232,500,000.00 USD |
| `4H` | `Bitunix` | `46.99%` | `53.01%` | `0.89` | 181,300,000.00 USD |
| `4H` | `Hyperliquid` | `41.64%` | `58.36%` | `0.71` | 202,880,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `53.81%` | `46.19%` | `1.16` | 50,290,000.00 USD |
| `4H` | `Crypto.com` | `46.2%` | `53.8%` | `0.86` | 11,190,000.00 USD |
| `4H` | `WhiteBIT` | `40.97%` | `59.03%` | `0.69` | 18,280,000.00 USD |
| `4H` | `HTX` | `45.12%` | `54.88%` | `0.82` | 4,940,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `47.39%` | `52.61%` | `0.90` | 37,310,000.00 USD |
| `4H` | `Aster` | `53.71%` | `46.29%` | `1.16` | 50,640,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `46%` | `54%` | `0.85` | 56,040,000.00 USD |
| `4H` | `Whale Positions` | `44.85%` | `55.15%` | `0.81` | 1,580,000,000.00 USD |
| `4H` | `Global Accounts` | `45.42%` | `54.58%` | `0.83` | 3,960,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `694.05` | `694.59` | `694.05` | `707.85` | `677.85` | 179,693,058.88 USD | 96,266,693.98 USD | 83,426,364.90 USD | 12,840,329.08 USD | `+7.15%` | `3B / 4S` |
| `0:00 UTC` | `705.15` | `704.71` | `705.15` | `718.65` | `690.75` | 186,631,734.60 USD | 100,794,189.14 USD | 85,837,545.46 USD | 14,956,643.67 USD | `+8.01%` | `11B / 2S` |
| `5:00 UTC` | `717.75` | `715.45` | `717.75` | `727.95` | `707.85` | 126,482,329.61 USD | 66,523,365.17 USD | 59,958,964.44 USD | 6,564,400.73 USD | `+5.19%` | `10B / 3S` |
| `0:00 UTC` | `709.95` | `710.65` | `709.95` | `715.65` | `705.45` | 34,559,429.86 USD | 16,578,658.63 USD | 17,980,771.23 USD | -1,402,112.60 USD | `-4.06%` | `2B / 2S` |
| `5:00 UTC` | `705.15` | `705.50` | `705.15` | `709.35` | `701.85` | 34,534,245.79 USD | 19,030,414.31 USD | 15,503,831.48 USD | 3,526,582.82 USD | `+10.21%` | `3B / 0S` |
| `0:00 UTC` | `703.95` | `704.22` | `703.95` | `708.75` | `700.95` | 21,370,966.63 USD | 9,634,694.93 USD | 11,736,271.71 USD | -2,101,576.78 USD | `-9.83%` | `1B / 1S` |
| `5:00 UTC` | `705.15` | `704.00` | `705.15` | `706.35` | `700.95` | 18,920,983.07 USD | 9,587,357.21 USD | 9,333,625.86 USD | 253,731.35 USD | `+1.34%` | `1B / 3S` |
| `0:00 UTC` | `703.35` | `702.56` | `703.35` | `705.75` | `700.05` | 27,178,783.16 USD | 14,796,052.46 USD | 12,382,730.70 USD | 2,413,321.76 USD | `+8.88%` | `0B / 2S` |
| `5:00 UTC` | `703.95` | `703.34` | `703.95` | `706.95` | `700.65` | 28,473,334.16 USD | 15,163,879.64 USD | 13,309,454.53 USD | 1,854,425.11 USD | `+6.51%` | `3B / 0S` |
| `0:00 UTC` | `702.45` | `703.28` | `702.45` | `707.25` | `700.35` | 20,261,227.39 USD | 10,632,185.41 USD | 9,629,041.97 USD | 1,003,143.44 USD | `+4.95%` | `0B / 1S` |

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
| `5m` | 269,330.00 USD | -2,460,000.00 USD | **`DISTRIBUTION`** |
| `15m` | 1,840,000.00 USD | -3,650,000.00 USD | **`DISTRIBUTION`** |
| `30m` | 5,430,000.00 USD | -779,520.00 USD | **`ACCUMULATION`** |
| `1h` | 4,330,000.00 USD | -499,200.00 USD | **`ACCUMULATION`** |
| `2h` | 5,210,000.00 USD | 13,340,000.00 USD | **`ACCUMULATION`** |
| `4h` | -11,690,000.00 USD | -42,380,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -12,670,000.00 USD | -43,880,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -14,190,000.00 USD | -45,940,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -18,720,000.00 USD | -35,240,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -9,290,000.00 USD | -69,960,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -39,650,000.00 USD | -87,330,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -139,130,000.00 USD | -413,200,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+269.33K` | 15m=`+1.84M` | 1h=`+4.33M` | 24h=`-9.29M`
* Futures Capital Netflows: 5m=`-2.46M` | 15m=`-3.65M` | 1h=`-499.20K` | 24h=`-69.96M`
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
  * `2026-10-30 04:15:34 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:41:34 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:41:34 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:40:34 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:42:34 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:42:34 IST`: [fxstreet.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `699.19` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `682.59` (Risk Distance: `16.60` pts)
  * +2.5R Take Profit: `740.70`
  * Mathematical Lot Sizing: **`0.60 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `713.37` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `729.97` (Risk Distance: `16.60` pts)
  * +2.5R Take Profit: `671.86`
  * Mathematical Lot Sizing: **`0.60 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`709.63`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
