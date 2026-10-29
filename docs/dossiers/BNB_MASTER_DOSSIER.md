# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BNB
**Canonical Key**: `BNB` | **Broker Instrument**: `BNBUSD.p` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 03:37:25 IST` (`2026-10-29 22:07:25 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `702.10` | **Live Ask Quote**: `702.80` | **Mid Price**: `702.45`
- **Spread Points**: `70.00` | **Spread BPS**: `9.97 bps` (Charter Threshold: `25.00 bps`)
- **Gate 1 Clearance**: **`PASS`** | **Execution Posture**: `PASSIVE LIMIT ONLY` | **Order Type Allowed**: `BUY_LIMIT / SELL_LIMIT`
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
  * Session VWAP: `733.80` | VWAP Z-Score: `-1.32` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `9.48` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `32.47` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `794.53` | Lower -3.00σ Band: `673.07`
  * Upper +2.51σ Band: `784.61` | Lower -2.51σ Band: `682.99`
  * Upper +2.01σ Band: `774.49` | Lower -2.01σ Band: `693.11`
  * Upper +2.00σ Band: `774.29` | Lower -2.00σ Band: `693.31`
  * Upper +1.28σ Band: `759.71` | Lower -1.28σ Band: `707.89`
  * Upper +1.00σ Band: `754.04` | Lower -1.00σ Band: `713.56`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`714.19` | EMA-20=`725.30` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`736.02` (Slope: `+0.0000`) | EMA-100=`741.49`
  * Institutional Anchors: EMA-144=`743.13` | EMA-200=`743.46` (Slope: `-0.3793`) | EMA-233=`743.29`
- **Range Boundaries**: 24H High=`759.80` | 24H Low=`677.20` | Weekly High=`760.90` | Weekly Low=`677.20`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `714.51` (Distance: `-1.72%`)
  * Point of Control (POC) = `706.96` (Distance: `-0.67%`)
  * Value Area Low (VAL) = `700.56` (Distance: `+0.24%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`754.57` | POC=`744.11` | VAL=`738.60`
  * Prior Day Extremes: PDH=`759.80` | PDL=`677.20` | PDC=`696.20`
  * Monday Range Blueprint: High=`746.00` | Mid=`738.45` | Low=`730.90`
  * Developing Weekly Value Area: Weekly VAH=`751.13` | Weekly POC=`740.53` | Weekly VAL=`734.95`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`724.00` | Low=`689.70`
  * London Session (08:00-16:00 UTC): High=`705.26` | Low=`699.64`
  * New York Session (13:00-21:00 UTC): High=`706.66` | Low=`698.24`
  * Initial Balance (First Hour): IB High=`704.56` | IB Low=`700.34`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `699.64` - `705.26`
  * Optimal Trade Entry (OTE 0.705): `703.85`
  * Structural Invalidation Anchor (0.786): `708.07`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `705.03` | `709.47` | `702.81` | `708.57` | `15,482` | 10,943,553.68 USD | 3,495,160.61 USD | `+31.94%` | -25,437,337.82 USD | `+0.49` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `708.58` | `708.89` | `703.38` | `703.61` | `11,358` | 8,015,568.38 USD | -2,651,761.16 USD | `-33.08%` | -28,089,098.98 USD | `-0.40` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `703.61` | `703.67` | `703.00` | `703.16` | `388` | 272,787.49 USD | -139,508.33 USD | `-51.14%` | -28,228,607.31 USD | `-0.08` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `712.88` | `715.77` | `705.45` | `705.49` | `48,632` | 34,559,429.86 USD | -1,402,112.60 USD | `-4.06%` | -28,891,694.90 USD | `-0.12` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `705.49` | `709.47` | `701.84` | `708.57` | `48,951` | 34,534,245.79 USD | 3,526,582.82 USD | `+10.21%` | -25,365,112.08 USD | `+0.49` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `708.58` | `708.89` | `703.00` | `703.38` | `11,782` | 8,313,632.42 USD | -2,778,032.34 USD | `-33.42%` | -28,143,144.42 USD | `-0.30` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `745.34` | `745.53` | `677.76` | `697.34` | `772,178` | 547,049,922.28 USD | -28,994,090.87 USD | `-5.30%` | -47,816,369.31 USD | `-3.64` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `697.33` | `727.80` | `690.87` | `708.57` | `539,232` | 382,207,739.86 USD | 23,645,514.63 USD | `+6.19%` | -24,170,854.68 USD | `+2.64` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `708.58` | `708.89` | `703.00` | `703.48` | `11,781` | 8,312,527.94 USD | -2,776,956.01 USD | `-33.41%` | -26,947,810.68 USD | `-0.19` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `740.45` | `753.64` | `739.55` | `750.62` | `148,938` | 111,099,080.67 USD | 8,045,498.44 USD | `+7.24%` | -17,010,604.60 USD | `+1.70` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `750.62` | `754.90` | `743.07` | `745.33` | `88,414` | 66,199,547.89 USD | 232,195.88 USD | `+0.35%` | -16,778,408.72 USD | `+0.53` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `745.34` | `745.53` | `677.76` | `703.48` | `1,323,191` | 937,570,190.08 USD | -8,125,532.24 USD | `-0.87%` | -24,903,940.96 USD | `-0.62` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `747.26` | `759.90` | `745.75` | `748.51` | `156,800` | 118,182,602.62 USD | -8,240,157.99 USD | `-6.97%` | -14,715,810.54 USD | `-1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `748.51` | `753.57` | `738.70` | `740.45` | `333,019` | 248,636,999.78 USD | -10,340,292.49 USD | `-4.16%` | -25,056,103.04 USD | `-1.26` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `740.45` | `753.64` | `739.55` | `750.62` | `148,938` | 111,099,080.67 USD | 8,045,498.44 USD | `+7.24%` | -17,010,604.60 USD | `+1.70` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `750.62` | `754.90` | `743.07` | `745.33` | `88,414` | 66,199,547.89 USD | 232,195.88 USD | `+0.35%` | -16,778,408.72 USD | `+0.53` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `745.34` | `745.53` | `677.76` | `703.48` | `1,323,191` | 937,570,190.08 USD | -8,125,532.24 USD | `-0.87%` | -24,903,940.96 USD | `-0.62` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`702.45`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `702.05` | `8863000000.0000` | 6,222.27 USD | 139,480.35 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `702.06` | `6664000000.0000` | 4,678.53 USD | 133,258.09 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `702.07` | `8906000000.0000` | 6,252.64 USD | 128,579.56 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `702.08` | `6230000000.0000` | 4,373.96 USD | 122,326.92 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `702.09` | `1150000000.0000` | 807.40 USD | 117,952.96 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `702.12` | `50112000000.0000` | 35,184.64 USD | 117,145.56 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `702.13` | `150000000.0000` | 105.32 USD | 81,960.92 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `702.15` | `278000000.0000` | 195.20 USD | 81,855.60 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `702.16` | `1000000000.0000` | 702.16 USD | 81,660.41 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `702.17` | `8996000000.0000` | 6,316.72 USD | 80,958.25 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `702.18` | `6133000000.0000` | 4,306.47 USD | 74,641.52 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `702.19` | `15262000000.0000` | 10,716.82 USD | 70,335.05 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `702.22` | `6228000000.0000` | 4,373.43 USD | 59,618.23 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `702.24` | `150000000.0000` | 105.34 USD | 55,244.80 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `702.25` | `7938000000.0000` | 5,574.46 USD | 55,139.47 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `702.29` | `9037000000.0000` | 6,346.59 USD | 49,565.01 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `702.34` | `6227000000.0000` | 4,373.47 USD | 43,218.41 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `702.35` | `8881000000.0000` | 6,237.57 USD | 38,844.94 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `702.36` | `15557000000.0000` | 10,926.61 USD | 32,607.37 USD | `2 orders` | `-0.00%` | `-` |
| `BID` | `702.37` | `30868000000.0000` | 21,680.76 USD | 21,680.76 USD | `4 orders` | `-0.00%` | `-` |
| `ASK` | `702.38` | `92347000000.0000` | 64,862.69 USD | 64,862.69 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `702.38` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 702.38` | `0.00%` | `-` |
| `ASK` | `702.59` | `1144000000.0000` | 803.76 USD | 65,666.45 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `702.60` | `8901000000.0000` | 6,253.84 USD | 71,920.29 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `702.66` | `6675000000.0000` | 4,690.26 USD | 76,610.55 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `702.67` | `8874000000.0000` | 6,235.49 USD | 82,846.04 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `702.68` | `8869000000.0000` | 6,232.07 USD | 89,078.11 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `702.74` | `8901000000.0000` | 6,255.09 USD | 95,333.20 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `702.78` | `9097000000.0000` | 6,393.19 USD | 101,726.39 USD | `2 orders` | `+0.06%` | `-` |
| `ASK` | `702.84` | `8834000000.0000` | 6,208.89 USD | 107,935.28 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `702.85` | `8230000000.0000` | 5,784.46 USD | 113,719.73 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `702.89` | `8855000000.0000` | 6,224.09 USD | 119,943.82 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `702.93` | `8656000000.0000` | 6,084.56 USD | 126,028.38 USD | `1 orders` | `+0.08%` | `-` |
| `ASK` | `702.99` | `24846000000.0000` | 17,466.49 USD | 143,494.87 USD | `3 orders` | `+0.09%` | `-` |
| `ASK` | `703.00` | `300000000.0000` | 210.90 USD | 143,705.77 USD | `2 orders` | `+0.09%` | `-` |
| `ASK` | `703.01` | `6132000000.0000` | 4,310.86 USD | 148,016.63 USD | `1 orders` | `+0.09%` | `-` |
| `ASK` | `703.05` | `20264000000.0000` | 14,246.61 USD | 162,263.24 USD | `3 orders` | `+0.10%` | `-` |
| `ASK` | `703.06` | `1793000000.0000` | 1,260.59 USD | 163,523.82 USD | `1 orders` | `+0.10%` | `-` |
| `ASK` | `703.07` | `22663000000.0000` | 15,933.68 USD | 179,457.50 USD | `2 orders` | `+0.10%` | `-` |
| `ASK` | `703.09` | `150000000.0000` | 105.46 USD | 179,562.96 USD | `1 orders` | `+0.10%` | `-` |
| `ASK` | `703.12` | `8899000000.0000` | 6,257.06 USD | 185,820.03 USD | `2 orders` | `+0.11%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 03:35:39 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `803` | `0xea00...a918` | `LONG` | 2,878,613.58 USD | `4,098,429,000,000.00` | `787.24` | `704.73` | `0.000000` | -347,813.21 USD | `-12.08%` | `5X Cross` |
| `875` | `0xb23b...4852` | `SHORT` | 2,599,789.26 USD | `3,703,087,000,000.00` | `702.34` | `704.73` | `3614.38` | 1,046.55 USD | `+0.04%` | `5X Cross` |
| `930` | `0xfe7c...b7ae` | `LONG` | 2,451,539.55 USD | `3,491,575,000,000.00` | `686.05` | `704.73` | `0.000000` | 56,128.69 USD | `+2.29%` | `10X Cross` |
| `1051` | `0x39b4...5c34` | `SHORT` | 2,123,948.16 USD | `3,025,007,000,000.00` | `707.72` | `704.73` | `825.54` | 16,895.03 USD | `+0.80%` | `10X Cross` |
| `1155` | `0xcac1...26b3` | `LONG` | 1,961,896.52 USD | `2,789,043,000,000.00` | `679.91` | `704.73` | `0.000000` | 65,585.35 USD | `+3.34%` | `10X Cross` |
| `1223` | `0x7737...bf66` | `SHORT` | 1,858,437.97 USD | `2,646,179,000,000.00` | `752.73` | `704.73` | `6774.68` | 133,432.61 USD | `+7.18%` | `10X Cross` |
| `1318` | `0x5b67...c66a` | `SHORT` | 1,710,837.66 USD | `2,429,891,000,000.00` | `691.70` | `704.73` | `965.63` | -30,079.22 USD | `-1.76%` | `10X Cross` |
| `1370` | `0xc675...795d` | `LONG` | 1,641,245.46 USD | `2,335,694,000,000.00` | `706.91` | `704.73` | `651.51` | -9,872.42 USD | `-0.60%` | `10X Cross` |
| `1532` | `0x2edd...8179` | `LONG` | 1,451,285.26 USD | `2,070,632,000,000.00` | `714.56` | `704.73` | `0.000000` | -28,308.11 USD | `-1.95%` | `10X Cross` |
| `1582` | `0x325e...9564` | `LONG` | 1,405,380.00 USD | `2,000,000,000,000.00` | `713.23` | `704.73` | `0.000000` | -21,079.80 USD | `-1.50%` | `10X Cross` |
| `1678` | `0xb69e...033a` | `LONG` | 1,286,281.55 USD | `1,795,655,000,000.00` | `772.94` | `704.73` | `619.80` | -101,650.17 USD | `-7.90%` | `10X Cross` |
| `1739` | `0x07fd...689d` | `LONG` | 1,224,693.58 USD | `1,744,292,000,000.00` | `714.81` | `704.73` | `0.000000` | -22,152.23 USD | `-1.81%` | `10X Cross` |
| `1745` | `0x645b...87b8` | `LONG` | 1,210,924.50 USD | `1,721,457,000,000.00` | `747.36` | `704.73` | `0.000000` | -75,619.27 USD | `-6.24%` | `10X Cross` |
| `1843` | `0xa4a6...46cf` | `SHORT` | 1,122,198.06 USD | `1,595,323,000,000.00` | `713.84` | `704.73` | `1839.91` | 16,601.21 USD | `+1.48%` | `10X Cross` |
| `1845` | `0xab04...8b69` | `SHORT` | 1,121,060.59 USD | `1,595,407,000,000.00` | `694.40` | `704.73` | `1158.98` | -13,203.84 USD | `-1.18%` | `10X Cross` |
| `1846` | `0x023a...2355` | `LONG` | 1,120,982.43 USD | `1,593,579,000,000.00` | `714.42` | `704.73` | `0.000000` | -17,502.25 USD | `-1.56%` | `10X Cross` |
| `1922` | `0x14c6...b280` | `SHORT` | 1,055,010.00 USD | `1,500,000,000,000.00` | `712.51` | `704.73` | `1463.22` | 13,751.70 USD | `+1.30%` | `10X Cross` |
| `1955` | `0x1367...560e` | `SHORT` | 1,033,976.96 USD | `1,472,000,000,000.00` | `713.72` | `704.73` | `2030.12` | 16,616.67 USD | `+1.61%` | `10X Cross` |
| `1994` | `0xbf5a...88ba` | `SHORT` | 1,010,755.40 USD | `1,439,105,000,000.00` | `718.16` | `704.73` | `1972.74` | 22,751.55 USD | `+2.25%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`758.49` (Vol: 2,400,000.00 USD, Dist: `+7.38%`) | Long MP=`677.61` (Vol: 3,100,000.00 USD, Dist: `--4.07%`)
  * 48H Horizon: Short MP=`767.93` (Vol: 3,000,000.00 USD, Dist: `+8.71%`) | Long MP=`677.29` (Vol: 3,100,000.00 USD, Dist: `--4.12%`)
  * 3D Horizon: Short MP=`767.93` (Vol: 3,400,000.00 USD, Dist: `+8.71%`) | Long MP=`677.29` (Vol: 3,100,000.00 USD, Dist: `--4.12%`)
  * 7D Horizon: Short MP=`767.93` (Vol: 3,500,000.00 USD, Dist: `+8.71%`) | Long MP=`677.29` (Vol: 3,100,000.00 USD, Dist: `--4.12%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `142.50` | 5,550.00 USD | 5,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `145.50` | 2,680.00 USD | 5,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `151.50` | 2,120.00 USD | 5,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `153.50` | 1,890.00 USD | 5,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `154.50` | 439.86 USD | 5,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `161.50` | 807.50 USD | 5,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `178.50` | 239.90 USD | 5,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `182.50` | 662.29 USD | 5,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `186.50` | 18,650.00 USD | 5,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `191.50` | 983.35 USD | 5,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `194.50` | 1,400.00 USD | 5,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `205.50` | 14,470.00 USD | 5,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `219.50` | 191.18 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `226.50` | 30,920.00 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `229.50` | 282.06 USD | 5,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `232.50` | 232,730.00 USD | 5,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `245.50` | 56,470.00 USD | 5,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `254.50` | 17,670.00 USD | 5,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `257.50` | 4,370.00 USD | 5,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `260.50` | 9,280.00 USD | 5,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `261.50` | 1,380.00 USD | 5,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `267.50` | 383.33 USD | 5,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `277.50` | 22,000.00 USD | 5,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `279.50` | 464,330.00 USD | 5,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `281.50` | 428.16 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `284.50` | 707.84 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `293.50` | 413.83 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `308.50` | 624.10 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `313.50` | 501.60 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `326.50` | 1,530.00 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `328.50` | 315.03 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `330.50` | 308.36 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `332.50` | 1,650.00 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `333.50` | 377.19 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `334.50` | 444.55 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `335.50` | 118.43 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `337.50` | 14,340.00 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `338.50` | 936.63 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `339.50` | 23,360.00 USD | 23,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `343.50` | 652.65 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `359.50` | 212.10 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `362.50` | 1,630.00 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `363.50` | 1,540.00 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `366.50` | 549.75 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `370.50` | 1,220.00 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `373.50` | 709.65 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `374.50` | 7,440.00 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `377.50` | 438.65 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `378.50` | 7,760.00 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `379.50` | 645.15 USD | 4,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `382.50` | 1,910.00 USD | 4,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `383.50` | 10,900.00 USD | 4,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `385.50` | 2,860.00 USD | 4,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `386.50` | 531.44 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `388.50` | 393.55 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `391.50` | 211.02 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `393.50` | 103.88 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `394.50` | 13,030.00 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `395.50` | 2,110.00 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `396.50` | 396.50 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `397.50` | 318.00 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `398.50` | 360.64 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `400.50` | 605.16 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `404.50` | 102.34 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `410.50` | 614.52 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `411.50` | 3,590.00 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `414.50` | 23,680.00 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `415.50` | 1,810.00 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `416.50` | 880.90 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `417.50` | 10,390.00 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `418.50` | 1,790.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `420.50` | 2,660.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `421.50` | 2,320.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `423.50` | 1,450.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `424.50` | 31,490.00 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `428.50` | 1,400.00 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `430.50` | 638.00 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `439.50` | 1,800.00 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `441.50` | 120.53 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `442.50` | 6,370.00 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `445.50` | 16,030.00 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `457.50` | 4,740.00 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `459.50` | 197.59 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `461.50` | 5,350.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `464.50` | 665.16 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `470.50` | 4,380.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `476.50` | 5,330.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `482.50` | 6,840.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `484.50` | 642.93 USD | 4,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `485.50` | 2,110.00 USD | 4,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `490.50` | 63,470.00 USD | 4,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `494.50` | 8,100.00 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `495.50` | 1,090.00 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `496.50` | 1,320.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `499.50` | 673.83 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `500.50` | 60,030.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `501.50` | 7,760.00 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `502.50` | 1,180.00 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `504.50` | 765.33 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `506.50` | 5,770.00 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `509.50` | 3,610.00 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `511.50` | 4,470.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `512.50` | 5,960.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `513.50` | 295.78 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `514.50` | 4,010.00 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `515.50` | 3,780.00 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `516.50` | 5,700.00 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `517.50` | 1,160.00 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `518.50` | 22,690.00 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `519.50` | 968.35 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `520.50` | 272.22 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `521.50` | 838.05 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `522.50` | 261.25 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `523.50` | 2,090.00 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `525.50` | 992.67 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `526.50` | 2,960.00 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `529.50` | 42,820.00 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `530.50` | 17,770.00 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `531.50` | 1,070.00 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `532.50` | 632.08 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `534.50` | 11,100.00 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `536.50` | 100.33 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `539.50` | 490.94 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `541.50` | 472.19 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `543.50` | 5,130.00 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `544.50` | 31,770.00 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `545.50` | 212,310.00 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `546.50` | 491.85 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `547.50` | 49,120.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `549.50` | 1,770.00 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `550.50` | 633.63 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `552.50` | 959.69 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `553.50` | 2,730.00 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `554.50` | 415.88 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `555.50` | 274.97 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `556.50` | 556.50 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `557.50` | 5,680.00 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `559.50` | 212.61 USD | 3,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `561.50` | 583.40 USD | 3,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `565.50` | 1,630.00 USD | 3,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `568.50` | 454.80 USD | 3,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `572.50` | 723,830.00 USD | 3,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `573.50` | 43,110.00 USD | 66,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `574.50` | 323.44 USD | 3,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `576.50` | 416.23 USD | 3,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `578.50` | 6,120.00 USD | 3,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `579.50` | 2,240.00 USD | 3,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `581.50` | 35,070.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `583.50` | 567.16 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `585.50` | 314.41 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `587.50` | 1,530.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `590.50` | 304.11 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `594.50` | 44,800.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `595.50` | 19,210.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `597.50` | 100.98 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `598.50` | 101.75 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `599.50` | 116.90 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `600.50` | 7,670.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `601.50` | 191.28 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `602.50` | 4,220.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `604.40` | 36,770,000.00 USD | 36,770,000.00 USD | 53,940.00 USD | 2,300.00 USD | 18,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `604.50` | 1,610.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `605.50` | 4,340.00 USD | 70,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `605.60` | 36,700,000.00 USD | 36,700,000.00 USD | 30,830.00 USD | 3,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `606.80` | 36,660,000.00 USD | 36,660,000.00 USD | 39,340.00 USD | 7,740.00 USD | 10,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `607.50` | 2,690.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `608.00` | 36,600,000.00 USD | 36,600,000.00 USD | 25,410.00 USD | 6,160.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `609.20` | 36,570,000.00 USD | 36,570,000.00 USD | 23,150.00 USD | 0.00 USD | 1,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `610.50` | 213.67 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `613.50` | 99,140.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `614.50` | 2,280.00 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `615.20` | 36,550,000.00 USD | 36,550,000.00 USD | 0.00 USD | 0.00 USD | 295,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `615.50` | 427.16 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `616.50` | 1,320.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `617.50` | 156.23 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `617.60` | 36,250,000.00 USD | 36,250,000.00 USD | 290,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `619.50` | 600.91 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `620.00` | 35,960,000.00 USD | 35,960,000.00 USD | 175,630.00 USD | 33,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `620.50` | 5,410.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `621.20` | 35,750,000.00 USD | 35,750,000.00 USD | 0.00 USD | 35,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `621.50` | 3,230.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `622.50` | 2,110.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `623.50` | 14,580.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `623.60` | 35,720,000.00 USD | 35,720,000.00 USD | 460,160.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `624.50` | 3,460.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `624.80` | 35,260,000.00 USD | 35,260,000.00 USD | 238,630.00 USD | 31,450.00 USD | 274,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `625.50` | 29,690.00 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `626.00` | 34,710,000.00 USD | 34,710,000.00 USD | 224,870.00 USD | 44,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `626.50` | 539.42 USD | 71,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `627.20` | 34,440,000.00 USD | 34,440,000.00 USD | 186,500.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `627.50` | 326.30 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `630.50` | 153.21 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `630.80` | 34,250,000.00 USD | 34,250,000.00 USD | 0.00 USD | 0.00 USD | 254,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `631.50` | 1,130,000.00 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `632.00` | 34,000,000.00 USD | 34,000,000.00 USD | 0.00 USD | 42,940.00 USD | 557,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `632.50` | 125.87 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `633.20` | 33,400,000.00 USD | 33,400,000.00 USD | 461,240.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `633.50` | 1,820.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `634.40` | 32,940,000.00 USD | 32,940,000.00 USD | 0.00 USD | 23,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `634.50` | 1,480,000.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `635.50` | 8,680.00 USD | 234,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `636.50` | 154.67 USD | 71,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `636.80` | 32,910,000.00 USD | 32,910,000.00 USD | 101,910.00 USD | 40,910.00 USD | 236,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `637.50` | 1,110.00 USD | 225,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `638.50` | 432.90 USD | 224,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `639.20` | 32,540,000.00 USD | 32,540,000.00 USD | 184,100.00 USD | 37,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `640.40` | 32,310,000.00 USD | 32,310,000.00 USD | 0.00 USD | 0.00 USD | 184,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `640.50` | 95,270.00 USD | 223,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `641.50` | 31,030.00 USD | 128,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `641.60` | 32,130,000.00 USD | 32,130,000.00 USD | 33,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `642.50` | 13,340.00 USD | 97,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `642.80` | 32,100,000.00 USD | 32,100,000.00 USD | 116,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `643.50` | 8,490.00 USD | 84,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `645.20` | 31,980,000.00 USD | 31,980,000.00 USD | 308,550.00 USD | 0.00 USD | 341,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `645.50` | 5,050.00 USD | 75,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `646.40` | 31,330,000.00 USD | 31,330,000.00 USD | 87,020.00 USD | 0.00 USD | 140,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `646.50` | 155.81 USD | 70,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `647.50` | 143.10 USD | 71,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `647.60` | 31,100,000.00 USD | 31,100,000.00 USD | 237,260.00 USD | 29,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `648.50` | 201.68 USD | 71,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `648.80` | 30,830,000.00 USD | 30,830,000.00 USD | 92,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `649.50` | 136.39 USD | 70,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `650.50` | 103,150.00 USD | 175,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `651.20` | 30,740,000.00 USD | 30,740,000.00 USD | 106,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `651.50` | 633.26 USD | 70,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `652.40` | 30,640,000.00 USD | 30,640,000.00 USD | 0.00 USD | 0.00 USD | 94,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `652.50` | 281,310.00 USD | 456,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `653.50` | 572,750.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `653.60` | 30,540,000.00 USD | 30,540,000.00 USD | 0.00 USD | 26,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `654.50` | 36,890.00 USD | 69,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `655.50` | 13,670.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `656.00` | 30,510,000.00 USD | 30,510,000.00 USD | 120,150.00 USD | 0.00 USD | 87,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `656.50` | 14,050.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `657.20` | 30,310,000.00 USD | 30,310,000.00 USD | 5,100.00 USD | 21,320.00 USD | 738,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `657.50` | 18,320.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `658.40` | 29,540,000.00 USD | 29,540,000.00 USD | 863,250.00 USD | 14,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `658.50` | 3,230.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `659.50` | 30,770.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `659.60` | 28,660,000.00 USD | 28,660,000.00 USD | 0.00 USD | 7,460.00 USD | 81,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `660.50` | 57,190.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `660.80` | 28,580,000.00 USD | 28,580,000.00 USD | 90,670.00 USD | 83,170.00 USD | 14,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `661.50` | 44,730.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `662.00` | 28,390,000.00 USD | 28,390,000.00 USD | 445,210.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `662.50` | 6,630.00 USD | 32,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `663.20` | 27,940,000.00 USD | 27,940,000.00 USD | 202,560.00 USD | 92,740.00 USD | 19,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `663.50` | 112,010.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `664.10` | 87,050,000.00 USD | 87,050,000.00 USD | 78,740.00 USD | 18,740.00 USD | 39,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `664.40` | 27,630,000.00 USD | 27,630,000.00 USD | 1,200,000.00 USD | 48,410.00 USD | 21,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `664.50` | 18,240.00 USD | 26,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `665.00` | 86,910,000.00 USD | 86,910,000.00 USD | 92,030.00 USD | 22,990.00 USD | 37,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `665.50` | 41,170.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `665.60` | 26,360,000.00 USD | 26,360,000.00 USD | 680,490.00 USD | 5,880.00 USD | 11,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `665.90` | 86,760,000.00 USD | 86,760,000.00 USD | 264,020.00 USD | 71,380.00 USD | 63,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `666.50` | 3,810.00 USD | 7,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `666.80` | 25,660,000.00 USD | 25,660,000.00 USD | 601,110.00 USD | 100,720.00 USD | 696,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `666.80` | 86,360,000.00 USD | 86,360,000.00 USD | 198,550.00 USD | 33,320.00 USD | 61,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `667.50` | 2,600.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `667.70` | 86,070,000.00 USD | 86,070,000.00 USD | 199,690.00 USD | 45,130.00 USD | 51,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `668.00` | 24,260,000.00 USD | 24,260,000.00 USD | 218,160.00 USD | 124,030.00 USD | 9,290.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `668.50` | 237,980.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `668.60` | 85,770,000.00 USD | 85,770,000.00 USD | 387,530.00 USD | 92,860.00 USD | 51,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `669.20` | 23,910,000.00 USD | 23,910,000.00 USD | 517,710.00 USD | 74,270.00 USD | 10,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `669.50` | 85,240,000.00 USD | 85,240,000.00 USD | 341,150.00 USD | 38,130.00 USD | 108,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `669.50` | 2,570.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `670.40` | 23,310,000.00 USD | 23,310,000.00 USD | 258,440.00 USD | 3,950.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `670.40` | 84,750,000.00 USD | 84,750,000.00 USD | 319,660.00 USD | 93,800.00 USD | 77,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `670.50` | 1,580.00 USD | 4,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `671.30` | 84,260,000.00 USD | 84,260,000.00 USD | 335,750.00 USD | 57,500.00 USD | 42,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `671.50` | 151,690.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `671.60` | 21,560,000.00 USD | 21,560,000.00 USD | 1,900,000.00 USD | 18,100.00 USD | 16,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `672.20` | 83,830,000.00 USD | 83,830,000.00 USD | 180,230.00 USD | 62,620.00 USD | 74,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `672.50` | 1,380.00 USD | 2,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `672.80` | 19,630,000.00 USD | 19,630,000.00 USD | 329,500.00 USD | 32,620.00 USD | 670,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `673.10` | 83,510,000.00 USD | 83,510,000.00 USD | 394,120.00 USD | 64,970.00 USD | 42,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `673.50` | 567.76 USD | 1,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `674.00` | 18,600,000.00 USD | 18,600,000.00 USD | 366,350.00 USD | 38,230.00 USD | 1,440,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `674.00` | 83,010,000.00 USD | 83,010,000.00 USD | 335,670.00 USD | 105,910.00 USD | 80,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `674.50` | 259.68 USD | 638.86 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `674.90` | 82,490,000.00 USD | 82,490,000.00 USD | 247,070.00 USD | 31,490.00 USD | 44,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `675.20` | 16,760,000.00 USD | 16,760,000.00 USD | 2,020,000.00 USD | 310,280.00 USD | 260,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `675.50` | 105.38 USD | 379.18 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `675.80` | 82,160,000.00 USD | 82,160,000.00 USD | 387,400.00 USD | 26,020.00 USD | 79,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `676.40` | 14,170,000.00 USD | 14,170,000.00 USD | 209,330.00 USD | 273,150.00 USD | 85,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `676.50` | 168.45 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `676.70` | 81,670,000.00 USD | 81,670,000.00 USD | 509,100.00 USD | 35,490.00 USD | 126,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `677.60` | 13,600,000.00 USD | 13,600,000.00 USD | 495,590.00 USD | 121,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `677.60` | 81,000,000.00 USD | 81,000,000.00 USD | 409,810.00 USD | 0.00 USD | 63,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `678.50` | 80,530,000.00 USD | 80,530,000.00 USD | 120,190.00 USD | 0.00 USD | 26,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `678.80` | 12,980,000.00 USD | 12,980,000.00 USD | 1,030,000.00 USD | 113,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `679.40` | 80,380,000.00 USD | 80,380,000.00 USD | 116,510.00 USD | 10,480.00 USD | 40,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `680.00` | 11,840,000.00 USD | 11,840,000.00 USD | 1,200,000.00 USD | 166,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `680.30` | 80,210,000.00 USD | 80,210,000.00 USD | 166,780.00 USD | 13,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `681.20` | 10,480,000.00 USD | 10,480,000.00 USD | 15,290.00 USD | 168,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `681.20` | 80,030,000.00 USD | 80,030,000.00 USD | 106,280.00 USD | 7,050.00 USD | 35,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `682.10` | 79,880,000.00 USD | 79,880,000.00 USD | 0.00 USD | 23,360.00 USD | 27,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `682.40` | 10,290,000.00 USD | 10,290,000.00 USD | 35,750.00 USD | 242,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `683.00` | 79,830,000.00 USD | 79,830,000.00 USD | 175,930.00 USD | 28,470.00 USD | 11,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `683.60` | 10,020,000.00 USD | 10,020,000.00 USD | 138,150.00 USD | 133,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `683.90` | 79,620,000.00 USD | 79,620,000.00 USD | 77,000.00 USD | 29,510.00 USD | 17,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `684.50` | 273.80 USD | 273.80 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `684.80` | 9,740,000.00 USD | 9,740,000.00 USD | 0.00 USD | 32,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `684.80` | 79,490,000.00 USD | 79,490,000.00 USD | 246,080.00 USD | 9,850.00 USD | 39,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `685.70` | 79,200,000.00 USD | 79,200,000.00 USD | 197,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `686.00` | 9,710,000.00 USD | 9,710,000.00 USD | 694,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `686.60` | 79,000,000.00 USD | 79,000,000.00 USD | 62,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `687.20` | 9,020,000.00 USD | 9,020,000.00 USD | 771,380.00 USD | 0.00 USD | 2,790,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `687.50` | 78,940,000.00 USD | 78,940,000.00 USD | 148,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `688.40` | 5,460,000.00 USD | 5,460,000.00 USD | 3,940.00 USD | 0.00 USD | 854,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `688.40` | 78,790,000.00 USD | 78,790,000.00 USD | 67,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `689.30` | 78,720,000.00 USD | 78,720,000.00 USD | 84,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `689.60` | 4,600,000.00 USD | 4,600,000.00 USD | 1,940,000.00 USD | 0.00 USD | 466,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `690.20` | 78,640,000.00 USD | 78,640,000.00 USD | 283,920.00 USD | 63,230.00 USD | 82,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `690.80` | 2,190,000.00 USD | 2,190,000.00 USD | 101,670.00 USD | 117,900.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `691.10` | 78,210,000.00 USD | 78,210,000.00 USD | 362,020.00 USD | 61,370.00 USD | 81,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `692.00` | 1,970,000.00 USD | 1,970,000.00 USD | 27,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `692.00` | 77,700,000.00 USD | 77,700,000.00 USD | 322,430.00 USD | 18,850.00 USD | 58,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `692.90` | 77,300,000.00 USD | 77,300,000.00 USD | 280,830.00 USD | 19,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `693.80` | 77,000,000.00 USD | 77,000,000.00 USD | 305,720.00 USD | 39,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `694.70` | 76,660,000.00 USD | 76,660,000.00 USD | 279,840.00 USD | 36,640.00 USD | 35,490.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `695.50` | 302.54 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `695.60` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 137,440.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `695.60` | 76,300,000.00 USD | 76,300,000.00 USD | 120,440.00 USD | 0.00 USD | 21,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `696.50` | 76,160,000.00 USD | 76,160,000.00 USD | 140,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `697.40` | 76,020,000.00 USD | 76,020,000.00 USD | 189,100.00 USD | 19,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `698.30` | 75,810,000.00 USD | 75,810,000.00 USD | 273,520.00 USD | 33,120.00 USD | 54,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `699.20` | 75,450,000.00 USD | 75,450,000.00 USD | 274,810.00 USD | 12,670.00 USD | 11,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `700.10` | 75,150,000.00 USD | 75,150,000.00 USD | 225,450.00 USD | 40,820.00 USD | 27,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `701.00` | 74,860,000.00 USD | 74,860,000.00 USD | 237,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `701.60` | 1,810,000.00 USD | 1,810,000.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `701.90` | 74,620,000.00 USD | 74,620,000.00 USD | 135,260.00 USD | 41,260.00 USD | 89,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `702.80` | 263,170.00 USD | 263,170.00 USD | 0.00 USD | 166,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `702.80` | 74,360,000.00 USD | 74,360,000.00 USD | 416,820.00 USD | 57,470.00 USD | 36,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `703.70` | 73,840,000.00 USD | 73,840,000.00 USD | 311,800.00 USD | 44,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `704.60` | 73,490,000.00 USD | 73,490,000.00 USD | 537,050.00 USD | 136,550.00 USD | 194,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `705.20` | 96,830.00 USD | 96,830.00 USD | 0.00 USD | 96,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `705.50` | 72,620,000.00 USD | 72,620,000.00 USD | 920,340.00 USD | 162,820.00 USD | 236,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `705.50` | 6,470.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `706.40` | 71,300,000.00 USD | 71,300,000.00 USD | 523,540.00 USD | 104,380.00 USD | 231,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `706.50` | 98,910.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `707.30` | 70,440,000.00 USD | 70,440,000.00 USD | 604,060.00 USD | 90,200.00 USD | 53,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `707.50` | 4,830.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `708.20` | 69,690,000.00 USD | 69,690,000.00 USD | 796,640.00 USD | 138,200.00 USD | 42,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `709.10` | 68,710,000.00 USD | 68,710,000.00 USD | 392,150.00 USD | 156,040.00 USD | 195,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `709.50` | 1,420.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `710.00` | 67,970,000.00 USD | 67,970,000.00 USD | 450,480.00 USD | 167,090.00 USD | 176,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `710.50` | 153.47 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `710.90` | 67,180,000.00 USD | 67,180,000.00 USD | 922,450.00 USD | 160,040.00 USD | 236,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `711.50` | 3,750.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `711.80` | 65,860,000.00 USD | 65,860,000.00 USD | 608,910.00 USD | 232,130.00 USD | 114,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `712.50` | 971.14 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `712.70` | 64,900,000.00 USD | 64,900,000.00 USD | 1,190,000.00 USD | 217,390.00 USD | 236,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `713.50` | 27,480.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `713.60` | 63,260,000.00 USD | 63,260,000.00 USD | 2,250,000.00 USD | 279,180.00 USD | 308,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `714.50` | 60,410,000.00 USD | 60,410,000.00 USD | 508,400.00 USD | 209,320.00 USD | 292,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `714.50` | 178.62 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `715.40` | 59,400,000.00 USD | 59,400,000.00 USD | 1,050,000.00 USD | 419,310.00 USD | 329,730.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `715.50` | 9,950.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `716.00` | 855,230.00 USD | 855,230.00 USD | 0.00 USD | 83,170.00 USD | 772,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `716.30` | 57,600,000.00 USD | 57,600,000.00 USD | 1,080,000.00 USD | 324,540.00 USD | 233,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `717.20` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 214,720.00 USD | 466,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `717.20` | 55,960,000.00 USD | 55,960,000.00 USD | 581,610.00 USD | 398,030.00 USD | 387,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `717.50` | 6,650.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `718.10` | 54,590,000.00 USD | 54,590,000.00 USD | 1,690,000.00 USD | 246,320.00 USD | 151,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `718.40` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 205,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `718.50` | 158.79 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `719.00` | 52,510,000.00 USD | 52,510,000.00 USD | 670,390.00 USD | 137,460.00 USD | 211,490.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `719.50` | 705.11 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `719.60` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 48,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `719.90` | 51,490,000.00 USD | 51,490,000.00 USD | 618,020.00 USD | 173,240.00 USD | 186,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `720.50` | 64,940.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `720.80` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 204,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `720.80` | 50,510,000.00 USD | 50,510,000.00 USD | 1,010,000.00 USD | 52,490.00 USD | 180,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `721.50` | 160,460.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `721.70` | 49,260,000.00 USD | 49,260,000.00 USD | 1,950,000.00 USD | 237,690.00 USD | 653,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `722.00` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 78,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `722.50` | 3,740.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `722.60` | 46,430,000.00 USD | 46,430,000.00 USD | 1,930,000.00 USD | 108,200.00 USD | 229,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `723.20` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 300,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `723.50` | 44,160,000.00 USD | 44,160,000.00 USD | 640,550.00 USD | 140,550.00 USD | 293,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `723.50` | 111,640.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `724.40` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 137,440.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `724.40` | 43,080,000.00 USD | 43,080,000.00 USD | 663,550.00 USD | 186,780.00 USD | 130,770.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `724.50` | 112,820.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `725.30` | 42,100,000.00 USD | 42,100,000.00 USD | 1,760,000.00 USD | 418,390.00 USD | 396,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `725.50` | 42.80 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `725.60` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 57,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `726.20` | 39,520,000.00 USD | 39,520,000.00 USD | 1,060,000.00 USD | 311,550.00 USD | 460,020.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `726.50` | 56,650.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `726.80` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 64,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `727.10` | 37,690,000.00 USD | 37,690,000.00 USD | 1,230,000.00 USD | 331,980.00 USD | 241,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `727.50` | 6,020.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `728.00` | 35,890,000.00 USD | 35,890,000.00 USD | 3,110,000.00 USD | 778,750.00 USD | 388,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `728.50` | 140,520.00 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `728.90` | 31,610,000.00 USD | 31,610,000.00 USD | 2,330,000.00 USD | 317,590.00 USD | 644,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `729.20` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 386,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `729.50` | 13,400.00 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `729.80` | 28,320,000.00 USD | 28,320,000.00 USD | 1,320,000.00 USD | 430,010.00 USD | 339,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `730.40` | 6,380,000.00 USD | 6,380,000.00 USD | 1,540,000.00 USD | 107,360.00 USD | 1,710,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `730.50` | 842.27 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `730.70` | 26,230,000.00 USD | 26,230,000.00 USD | 2,760,000.00 USD | 351,520.00 USD | 587,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `731.50` | 38,660.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `731.60` | 7,630,000.00 USD | 7,630,000.00 USD | 952,750.00 USD | 63,350.00 USD | 233,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `731.60` | 22,530,000.00 USD | 22,530,000.00 USD | 1,530,000.00 USD | 133,980.00 USD | 261,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `732.50` | 20,610,000.00 USD | 20,610,000.00 USD | 465,880.00 USD | 221,510.00 USD | 96,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `732.50` | 29,020.00 USD | 2,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `732.80` | 9,450,000.00 USD | 9,450,000.00 USD | 998,900.00 USD | 120,350.00 USD | 703,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `733.40` | 19,820,000.00 USD | 19,820,000.00 USD | 1,910,000.00 USD | 158,310.00 USD | 338,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `733.50` | 207,280.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `734.00` | 9,940,000.00 USD | 9,940,000.00 USD | 344,230.00 USD | 145,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `734.30` | 17,420,000.00 USD | 17,420,000.00 USD | 1,580,000.00 USD | 288,470.00 USD | 244,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `734.50` | 161,950.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `735.20` | 10,800,000.00 USD | 10,800,000.00 USD | 613,800.00 USD | 246,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `735.20` | 15,310,000.00 USD | 15,310,000.00 USD | 1,330,000.00 USD | 172,940.00 USD | 437,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `735.50` | 339.80 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `736.10` | 13,370,000.00 USD | 13,370,000.00 USD | 2,130,000.00 USD | 181,990.00 USD | 484,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `736.40` | 12,710,000.00 USD | 12,710,000.00 USD | 1,300,000.00 USD | 22,190.00 USD | 590,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `736.50` | 90,550.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `737.00` | 10,570,000.00 USD | 10,570,000.00 USD | 2,360,000.00 USD | 175,330.00 USD | 633,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `737.50` | 530,510.00 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `737.60` | 12,960,000.00 USD | 12,960,000.00 USD | 160,280.00 USD | 94,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `737.90` | 7,400,000.00 USD | 7,400,000.00 USD | 3,420,000.00 USD | 72,280.00 USD | 374,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `738.50` | 77,910.00 USD | 3,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `738.80` | 14,160,000.00 USD | 14,160,000.00 USD | 658,340.00 USD | 68,720.00 USD | 472,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `738.80` | 3,530,000.00 USD | 3,530,000.00 USD | 522,950.00 USD | 20,210.00 USD | 155,300.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `739.50` | 29,980.00 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `739.70` | 2,830,000.00 USD | 2,830,000.00 USD | 352,500.00 USD | 0.00 USD | 203,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `740.00` | 15,290,000.00 USD | 15,290,000.00 USD | 648,020.00 USD | 0.00 USD | 476,790.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `740.50` | 537,670.00 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `740.60` | 2,280,000.00 USD | 2,280,000.00 USD | 1,090,000.00 USD | 0.00 USD | 33,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `741.20` | 15,940,000.00 USD | 15,940,000.00 USD | 474,360.00 USD | 166,390.00 USD | 7,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `741.50` | 1,160,000.00 USD | 1,160,000.00 USD | 257,630.00 USD | 0.00 USD | 208,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `741.50` | 1,500.00 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `742.40` | 16,230,000.00 USD | 16,230,000.00 USD | 291,160.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `742.40` | 689,850.00 USD | 689,850.00 USD | 0.00 USD | 0.00 USD | 183,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `742.50` | 1,800.00 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `743.30` | 505,930.00 USD | 505,930.00 USD | 0.00 USD | 0.00 USD | 57,580.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `743.50` | 526,730.00 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `743.60` | 16,790,000.00 USD | 16,790,000.00 USD | 120,950.00 USD | 0.00 USD | 436,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `744.20` | 448,350.00 USD | 448,350.00 USD | 0.00 USD | 257,580.00 USD | 141,790.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `744.50` | 29,480.00 USD | 4,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `744.80` | 18,620,000.00 USD | 18,620,000.00 USD | 878,190.00 USD | 106,580.00 USD | 854,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `745.10` | 48,980.00 USD | 48,980.00 USD | 0.00 USD | 48,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `745.50` | 456.25 USD | 4,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `746.00` | 19,210,000.00 USD | 19,210,000.00 USD | 482,060.00 USD | 106,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `746.00` | 999,320.00 USD | 999,320.00 USD | 999,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `746.50` | 11,580.00 USD | 4,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `746.90` | 1,210,000.00 USD | 1,210,000.00 USD | 215,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `747.20` | 20,790,000.00 USD | 20,790,000.00 USD | 748,640.00 USD | 67,980.00 USD | 758,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `747.50` | 47,340.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `748.40` | 21,220,000.00 USD | 21,220,000.00 USD | 286,680.00 USD | 72,690.00 USD | 73,330.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `748.50` | 213,670.00 USD | 5,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `749.50` | 5,040.00 USD | 5,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `749.60` | 21,640,000.00 USD | 21,640,000.00 USD | 417,840.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `750.50` | 88,430.00 USD | 5,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `752.00` | 22,200,000.00 USD | 22,200,000.00 USD | 0.00 USD | 25,010.00 USD | 539,620.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `752.50` | 646,750.00 USD | 5,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `753.20` | 22,690,000.00 USD | 22,690,000.00 USD | 229,820.00 USD | 3,810.00 USD | 248,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `753.50` | 768.57 USD | 5,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `754.40` | 23,200,000.00 USD | 23,200,000.00 USD | 383,510.00 USD | 70,850.00 USD | 57,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `754.50` | 3,280.00 USD | 5,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `755.00` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 59,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `755.50` | 1,990.00 USD | 5,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `755.60` | 23,890,000.00 USD | 23,890,000.00 USD | 384,280.00 USD | 254,460.00 USD | 56,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `756.80` | 24,440,000.00 USD | 24,440,000.00 USD | 422,820.00 USD | 24,970.00 USD | 95,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `756.80` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 47,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `757.50` | 859,510.00 USD | 6,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `757.70` | 1,910,000.00 USD | 1,910,000.00 USD | 475,510.00 USD | 113,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `758.00` | 25,140,000.00 USD | 25,140,000.00 USD | 482,940.00 USD | 189,940.00 USD | 32,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `758.60` | 3,100,000.00 USD | 3,100,000.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `759.20` | 26,800,000.00 USD | 26,800,000.00 USD | 1,260,000.00 USD | 122,880.00 USD | 273,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `760.40` | 27,490,000.00 USD | 27,490,000.00 USD | 508,240.00 USD | 100,270.00 USD | 80,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `760.40` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 27,650.00 USD | 42,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `760.50` | 2,360.00 USD | 6,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `761.30` | 3,490,000.00 USD | 3,490,000.00 USD | 10,750.00 USD | 211,960.00 USD | 100,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `761.50` | 131.74 USD | 6,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `761.60` | 28,890,000.00 USD | 28,890,000.00 USD | 886,440.00 USD | 102,890.00 USD | 409,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `762.20` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 699,820.00 USD | 179,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `762.50` | 269.93 USD | 6,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `762.80` | 31,810,000.00 USD | 31,810,000.00 USD | 2,120,000.00 USD | 214,840.00 USD | 583,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `763.10` | 7,830,000.00 USD | 7,830,000.00 USD | 2,460,000.00 USD | 590,460.00 USD | 404,720.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `763.50` | 435,970.00 USD | 7,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `764.00` | 34,370,000.00 USD | 34,370,000.00 USD | 1,980,000.00 USD | 319,550.00 USD | 268,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `764.00` | 10,270,000.00 USD | 10,270,000.00 USD | 1,590,000.00 USD | 441,980.00 USD | 402,300.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `764.50` | 949,210.00 USD | 8,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `764.90` | 12,470,000.00 USD | 12,470,000.00 USD | 1,450,000.00 USD | 352,570.00 USD | 395,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `765.20` | 35,900,000.00 USD | 35,900,000.00 USD | 1,070,000.00 USD | 230,270.00 USD | 220,460.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `765.50` | 9,770.00 USD | 8,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `765.80` | 15,460,000.00 USD | 15,460,000.00 USD | 2,470,000.00 USD | 107,550.00 USD | 416,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `766.40` | 38,020,000.00 USD | 38,020,000.00 USD | 1,270,000.00 USD | 269,470.00 USD | 582,040.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `766.50` | 820.92 USD | 8,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `766.70` | 20,050,000.00 USD | 20,050,000.00 USD | 3,330,000.00 USD | 416,530.00 USD | 842,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `767.60` | 41,310,000.00 USD | 41,310,000.00 USD | 2,840,000.00 USD | 130,060.00 USD | 331,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `767.60` | 23,430,000.00 USD | 23,430,000.00 USD | 2,790,000.00 USD | 123,530.00 USD | 467,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `768.50` | 25,660,000.00 USD | 25,660,000.00 USD | 1,840,000.00 USD | 95,830.00 USD | 281,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `768.50` | 35,070.00 USD | 8,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `768.80` | 42,840,000.00 USD | 42,840,000.00 USD | 1,250,000.00 USD | 100,610.00 USD | 176,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `769.40` | 26,810,000.00 USD | 26,810,000.00 USD | 565,780.00 USD | 249,950.00 USD | 333,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `770.00` | 43,770,000.00 USD | 43,770,000.00 USD | 663,210.00 USD | 180,380.00 USD | 84,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `770.30` | 29,310,000.00 USD | 29,310,000.00 USD | 1,900,000.00 USD | 240,530.00 USD | 364,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `770.50` | 500.05 USD | 8,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `771.20` | 44,850,000.00 USD | 44,850,000.00 USD | 678,410.00 USD | 56,760.00 USD | 340,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `771.20` | 30,770,000.00 USD | 30,770,000.00 USD | 1,050,000.00 USD | 242,570.00 USD | 162,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `771.50` | 14,940.00 USD | 8,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `772.10` | 33,190,000.00 USD | 33,190,000.00 USD | 1,750,000.00 USD | 252,650.00 USD | 419,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `772.40` | 46,220,000.00 USD | 46,220,000.00 USD | 509,090.00 USD | 216,960.00 USD | 647,240.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `772.50` | 21,470.00 USD | 8,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `773.00` | 35,800,000.00 USD | 35,800,000.00 USD | 1,950,000.00 USD | 325,680.00 USD | 338,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `773.50` | 11,500.00 USD | 8,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `773.60` | 47,550,000.00 USD | 47,550,000.00 USD | 993,840.00 USD | 124,190.00 USD | 206,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `773.90` | 37,600,000.00 USD | 37,600,000.00 USD | 1,220,000.00 USD | 276,760.00 USD | 293,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `774.50` | 464,830.00 USD | 8,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `774.80` | 48,950,000.00 USD | 48,950,000.00 USD | 1,220,000.00 USD | 116,800.00 USD | 67,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `774.80` | 39,980,000.00 USD | 39,980,000.00 USD | 1,310,000.00 USD | 568,930.00 USD | 502,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `775.50` | 85,620.00 USD | 8,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `775.70` | 42,470,000.00 USD | 42,470,000.00 USD | 1,830,000.00 USD | 470,960.00 USD | 187,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `776.00` | 49,640,000.00 USD | 49,640,000.00 USD | 469,240.00 USD | 137,760.00 USD | 79,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `776.50` | 2,230.00 USD | 8,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `776.60` | 44,740,000.00 USD | 44,740,000.00 USD | 1,630,000.00 USD | 269,050.00 USD | 378,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `777.20` | 50,290,000.00 USD | 50,290,000.00 USD | 421,750.00 USD | 125,850.00 USD | 110,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `777.50` | 46,480,000.00 USD | 46,480,000.00 USD | 1,350,000.00 USD | 243,990.00 USD | 148,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `777.50` | 209.15 USD | 8,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `778.40` | 52,220,000.00 USD | 52,220,000.00 USD | 1,440,000.00 USD | 107,990.00 USD | 383,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `778.40` | 48,170,000.00 USD | 48,170,000.00 USD | 1,180,000.00 USD | 307,370.00 USD | 206,530.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `778.50` | 207,580.00 USD | 8,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `779.30` | 49,730,000.00 USD | 49,730,000.00 USD | 1,240,000.00 USD | 188,170.00 USD | 123,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `779.60` | 53,450,000.00 USD | 53,450,000.00 USD | 941,870.00 USD | 114,610.00 USD | 171,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `780.20` | 51,100,000.00 USD | 51,100,000.00 USD | 1,070,000.00 USD | 86,470.00 USD | 218,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `780.80` | 54,240,000.00 USD | 54,240,000.00 USD | 543,830.00 USD | 123,860.00 USD | 119,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `781.10` | 52,710,000.00 USD | 52,710,000.00 USD | 1,270,000.00 USD | 90,990.00 USD | 242,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `781.50` | 1,430.00 USD | 8,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `782.00` | 55,760,000.00 USD | 55,760,000.00 USD | 1,070,000.00 USD | 100,360.00 USD | 352,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `782.00` | 54,610,000.00 USD | 54,610,000.00 USD | 1,510,000.00 USD | 87,670.00 USD | 301,190.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `782.50` | 240,380.00 USD | 9,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `782.90` | 56,600,000.00 USD | 56,600,000.00 USD | 1,750,000.00 USD | 36,140.00 USD | 202,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `783.20` | 57,120,000.00 USD | 57,120,000.00 USD | 1,090,000.00 USD | 85,870.00 USD | 188,040.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `783.50` | 52,930.00 USD | 9,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `783.80` | 57,170,000.00 USD | 57,170,000.00 USD | 508,000.00 USD | 10,100.00 USD | 54,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `784.40` | 57,680,000.00 USD | 57,680,000.00 USD | 485,610.00 USD | 41,570.00 USD | 28,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `784.50` | 13,210.00 USD | 9,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `784.70` | 57,480,000.00 USD | 57,480,000.00 USD | 208,380.00 USD | 28,260.00 USD | 70,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `785.60` | 58,210,000.00 USD | 58,210,000.00 USD | 482,590.00 USD | 24,180.00 USD | 20,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `785.60` | 58,610,000.00 USD | 58,610,000.00 USD | 1,010,000.00 USD | 54,140.00 USD | 71,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `786.50` | 59,000,000.00 USD | 59,000,000.00 USD | 329,230.00 USD | 30,660.00 USD | 23,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `786.50` | 11,280.00 USD | 9,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `786.80` | 58,510,000.00 USD | 58,510,000.00 USD | 244,430.00 USD | 26,670.00 USD | 37,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `787.40` | 59,580,000.00 USD | 59,580,000.00 USD | 470,050.00 USD | 17,630.00 USD | 91,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `787.50` | 124,850.00 USD | 9,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `788.00` | 59,440,000.00 USD | 59,440,000.00 USD | 492,120.00 USD | 31,760.00 USD | 399,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `788.30` | 59,940,000.00 USD | 59,940,000.00 USD | 202,630.00 USD | 82,380.00 USD | 81,230.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `788.50` | 73,300.00 USD | 9,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `789.20` | 59,980,000.00 USD | 59,980,000.00 USD | 434,090.00 USD | 59,690.00 USD | 47,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `789.20` | 60,780,000.00 USD | 60,780,000.00 USD | 698,830.00 USD | 81,250.00 USD | 55,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `789.50` | 43,710.00 USD | 9,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `790.10` | 61,270,000.00 USD | 61,270,000.00 USD | 299,250.00 USD | 104,360.00 USD | 88,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `790.40` | 60,660,000.00 USD | 60,660,000.00 USD | 469,100.00 USD | 49,740.00 USD | 163,110.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `790.50` | 939.90 USD | 9,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `791.00` | 62,150,000.00 USD | 62,150,000.00 USD | 693,290.00 USD | 82,870.00 USD | 100,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `791.60` | 61,090,000.00 USD | 61,090,000.00 USD | 364,500.00 USD | 52,300.00 USD | 8,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `791.90` | 63,030,000.00 USD | 63,030,000.00 USD | 816,380.00 USD | 16,830.00 USD | 46,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `792.80` | 61,260,000.00 USD | 61,260,000.00 USD | 169,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `792.80` | 63,250,000.00 USD | 63,250,000.00 USD | 205,450.00 USD | 0.00 USD | 14,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `793.70` | 63,430,000.00 USD | 63,430,000.00 USD | 184,960.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `794.00` | 61,310,000.00 USD | 61,310,000.00 USD | 51,700.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `794.50` | 73,100.00 USD | 9,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `794.60` | 63,750,000.00 USD | 63,750,000.00 USD | 302,280.00 USD | 15,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `795.20` | 61,350,000.00 USD | 61,350,000.00 USD | 44,220.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `795.50` | 63,890,000.00 USD | 63,890,000.00 USD | 109,640.00 USD | 14,650.00 USD | 14,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `795.50` | 60,100.00 USD | 9,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `796.40` | 61,490,000.00 USD | 61,490,000.00 USD | 41,210.00 USD | 0.00 USD | 94,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `796.40` | 64,030,000.00 USD | 64,030,000.00 USD | 139,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `796.50` | 172.84 USD | 9,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `797.30` | 64,090,000.00 USD | 64,090,000.00 USD | 64,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `797.50` | 24,140.00 USD | 9,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `797.60` | 61,570,000.00 USD | 61,570,000.00 USD | 86,930.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `798.20` | 64,250,000.00 USD | 64,250,000.00 USD | 155,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `798.50` | 35,530.00 USD | 9,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `798.80` | 61,640,000.00 USD | 61,640,000.00 USD | 38,270.00 USD | 26,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `799.10` | 64,290,000.00 USD | 64,290,000.00 USD | 42,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `799.50` | 8,100.00 USD | 9,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `800.00` | 61,660,000.00 USD | 61,660,000.00 USD | 18,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `800.00` | 64,400,000.00 USD | 64,400,000.00 USD | 113,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `800.90` | 64,510,000.00 USD | 64,510,000.00 USD | 77,580.00 USD | 8,370.00 USD | 21,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `801.20` | 61,680,000.00 USD | 61,680,000.00 USD | 20,010.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `801.80` | 64,720,000.00 USD | 64,720,000.00 USD | 179,900.00 USD | 16,330.00 USD | 10,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `802.40` | 61,820,000.00 USD | 61,820,000.00 USD | 32,010.00 USD | 21,320.00 USD | 87,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `802.50` | 279.27 USD | 9,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `802.70` | 64,730,000.00 USD | 64,730,000.00 USD | 11,220.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `803.60` | 61,910,000.00 USD | 61,910,000.00 USD | 89,870.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `803.60` | 64,760,000.00 USD | 64,760,000.00 USD | 27,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `804.50` | 64,840,000.00 USD | 64,840,000.00 USD | 32,340.00 USD | 18,260.00 USD | 32,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `804.50` | 142,720.00 USD | 9,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `804.80` | 61,990,000.00 USD | 61,990,000.00 USD | 67,230.00 USD | 14,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `805.40` | 64,910,000.00 USD | 64,910,000.00 USD | 56,700.00 USD | 8,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `805.50` | 17,140.00 USD | 9,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `806.00` | 62,090,000.00 USD | 62,090,000.00 USD | 13,570.00 USD | 7,460.00 USD | 81,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `806.30` | 64,920,000.00 USD | 64,920,000.00 USD | 3,270.00 USD | 12,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `806.50` | 45,660.00 USD | 9,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `807.20` | 62,120,000.00 USD | 62,120,000.00 USD | 7,560.00 USD | 0.00 USD | 14,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `807.20` | 64,970,000.00 USD | 64,970,000.00 USD | 39,190.00 USD | 0.00 USD | 11,830.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `807.50` | 73,430.00 USD | 10,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `808.10` | 65,030,000.00 USD | 65,030,000.00 USD | 17,980.00 USD | 5,360.00 USD | 29,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `808.40` | 62,120,000.00 USD | 62,120,000.00 USD | 7,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `808.50` | 738.97 USD | 10,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `809.00` | 65,110,000.00 USD | 65,110,000.00 USD | 58,620.00 USD | 13,120.00 USD | 13,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `809.50` | 172,010.00 USD | 10,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `809.60` | 62,130,000.00 USD | 62,130,000.00 USD | 11,010.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `809.90` | 65,330,000.00 USD | 65,330,000.00 USD | 178,130.00 USD | 9,760.00 USD | 36,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `810.80` | 62,160,000.00 USD | 62,160,000.00 USD | 5,050.00 USD | 5,000.00 USD | 19,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `810.80` | 65,420,000.00 USD | 65,420,000.00 USD | 78,030.00 USD | 6,630.00 USD | 5,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `811.70` | 65,480,000.00 USD | 65,480,000.00 USD | 19,210.00 USD | 12,110.00 USD | 29,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `812.00` | 62,230,000.00 USD | 62,230,000.00 USD | 45,960.00 USD | 0.00 USD | 21,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `812.60` | 65,600,000.00 USD | 65,600,000.00 USD | 68,390.00 USD | 17,450.00 USD | 31,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `813.20` | 62,270,000.00 USD | 62,270,000.00 USD | 22,940.00 USD | 4,540.00 USD | 11,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `813.50` | 65,860,000.00 USD | 65,860,000.00 USD | 147,480.00 USD | 59,640.00 USD | 45,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `814.40` | 62,340,000.00 USD | 62,340,000.00 USD | 43,410.00 USD | 15,040.00 USD | 7,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `814.40` | 66,180,000.00 USD | 66,180,000.00 USD | 218,130.00 USD | 32,770.00 USD | 74,730.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `814.50` | 862.56 USD | 10,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `815.30` | 66,390,000.00 USD | 66,390,000.00 USD | 171,100.00 USD | 24,290.00 USD | 10,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `815.60` | 62,380,000.00 USD | 62,380,000.00 USD | 17,810.00 USD | 11,670.00 USD | 13,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `816.20` | 66,690,000.00 USD | 66,690,000.00 USD | 203,680.00 USD | 44,470.00 USD | 59,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `816.80` | 62,450,000.00 USD | 62,450,000.00 USD | 54,370.00 USD | 17,360.00 USD | 3,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `817.10` | 67,090,000.00 USD | 67,090,000.00 USD | 278,420.00 USD | 76,830.00 USD | 42,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `818.00` | 62,510,000.00 USD | 62,510,000.00 USD | 43,280.00 USD | 8,150.00 USD | 6,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `818.00` | 67,550,000.00 USD | 67,550,000.00 USD | 346,550.00 USD | 48,360.00 USD | 67,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `818.50` | 205.44 USD | 10,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `818.90` | 67,790,000.00 USD | 67,790,000.00 USD | 180,470.00 USD | 8,160.00 USD | 47,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `819.20` | 62,700,000.00 USD | 62,700,000.00 USD | 182,710.00 USD | 3,950.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `819.50` | 5,990.00 USD | 10,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `819.80` | 68,300,000.00 USD | 68,300,000.00 USD | 295,510.00 USD | 101,950.00 USD | 107,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `820.40` | 62,930,000.00 USD | 62,930,000.00 USD | 47,350.00 USD | 11,440.00 USD | 165,820.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `820.50` | 3,550.00 USD | 10,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `820.70` | 68,600,000.00 USD | 68,600,000.00 USD | 235,990.00 USD | 41,190.00 USD | 24,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `821.50` | 11,840.00 USD | 10,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `821.60` | 63,050,000.00 USD | 63,050,000.00 USD | 80,210.00 USD | 8,400.00 USD | 29,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `821.60` | 68,800,000.00 USD | 68,800,000.00 USD | 86,380.00 USD | 62,620.00 USD | 55,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `822.50` | 69,300,000.00 USD | 69,300,000.00 USD | 394,120.00 USD | 64,970.00 USD | 42,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `822.50` | 57,150.00 USD | 10,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `822.80` | 63,620,000.00 USD | 63,620,000.00 USD | 493,840.00 USD | 46,110.00 USD | 31,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `823.40` | 69,630,000.00 USD | 69,630,000.00 USD | 213,450.00 USD | 68,530.00 USD | 45,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `823.50` | 1,770.00 USD | 10,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `824.00` | 63,910,000.00 USD | 63,910,000.00 USD | 225,430.00 USD | 32,630.00 USD | 30,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `824.30` | 69,980,000.00 USD | 69,980,000.00 USD | 248,860.00 USD | 58,170.00 USD | 43,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `825.20` | 63,980,000.00 USD | 63,980,000.00 USD | 36,860.00 USD | 26,950.00 USD | 13,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `825.20` | 70,340,000.00 USD | 70,340,000.00 USD | 277,990.00 USD | 21,630.00 USD | 61,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `825.50` | 58,040.00 USD | 10,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `826.10` | 70,650,000.00 USD | 70,650,000.00 USD | 223,810.00 USD | 27,390.00 USD | 53,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `826.40` | 64,220,000.00 USD | 64,220,000.00 USD | 138,510.00 USD | 38,730.00 USD | 64,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `826.50` | 301.67 USD | 10,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `827.00` | 71,290,000.00 USD | 71,290,000.00 USD | 494,310.00 USD | 23,200.00 USD | 126,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `827.50` | 64,580,000.00 USD | 64,580,000.00 USD | 330,770.00 USD | 0.00 USD | 21,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `827.90` | 71,650,000.00 USD | 71,650,000.00 USD | 297,880.00 USD | 0.00 USD | 63,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `828.80` | 71,840,000.00 USD | 71,840,000.00 USD | 184,280.00 USD | 0.00 USD | 5,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `829.70` | 71,930,000.00 USD | 71,930,000.00 USD | 43,760.00 USD | 5,190.00 USD | 33,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `830.50` | 17,560.00 USD | 10,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `830.60` | 72,180,000.00 USD | 72,180,000.00 USD | 221,150.00 USD | 5,300.00 USD | 28,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `831.50` | 72,220,000.00 USD | 72,220,000.00 USD | 37,200.00 USD | 5,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `831.50` | 62,670.00 USD | 10,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `834.50` | 1,010.00 USD | 10,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `836.50` | 625.70 USD | 10,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `838.50` | 399.96 USD | 10,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `839.50` | 572.54 USD | 10,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `841.50` | 2,680.00 USD | 10,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `842.50` | 4,210.00 USD | 10,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `843.50` | 173,300.00 USD | 10,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `848.50` | 289.34 USD | 10,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `851.50` | 108.99 USD | 10,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `853.50` | 179,830.00 USD | 10,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `854.50` | 50,440.00 USD | 10,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `855.50` | 3,630.00 USD | 10,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `856.50` | 625,560.00 USD | 11,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `857.50` | 444.19 USD | 11,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `858.50` | 351,280.00 USD | 11,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `859.50` | 3,790.00 USD | 11,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `860.50` | 4,200.00 USD | 11,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `861.50` | 2,370.00 USD | 11,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `862.50` | 9,880.00 USD | 11,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `863.50` | 3,340.00 USD | 11,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `864.50` | 1,580.00 USD | 11,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `865.50` | 114,320.00 USD | 11,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `866.50` | 807.58 USD | 11,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `867.50` | 2,000.00 USD | 11,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `868.50` | 341.32 USD | 11,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `869.50` | 622.56 USD | 11,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `870.50` | 2,050.00 USD | 11,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `871.50` | 1,430.00 USD | 11,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `872.50` | 1,420.00 USD | 11,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `873.50` | 1,110.00 USD | 11,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `874.50` | 933.97 USD | 11,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `875.50` | 896.51 USD | 11,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `876.50` | 1,040.00 USD | 11,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `877.50` | 183,140.00 USD | 12,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `878.50` | 13,120.00 USD | 12,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `879.50` | 12,760.00 USD | 12,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `880.50` | 26,960.00 USD | 12,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `881.50` | 651.43 USD | 12,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `882.50` | 3,740.00 USD | 12,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `884.50` | 240.58 USD | 12,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `885.50` | 2,520.00 USD | 12,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `886.50` | 948.56 USD | 12,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `888.50` | 394.49 USD | 12,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `889.50` | 362.92 USD | 12,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `891.50` | 197.91 USD | 12,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `892.50` | 166.90 USD | 12,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `893.50` | 140.28 USD | 12,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `895.50` | 196.11 USD | 12,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `896.50` | 224,120.00 USD | 12,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `897.50` | 1,330.00 USD | 12,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `898.50` | 33,170.00 USD | 12,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `900.50` | 85,180.00 USD | 12,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `902.50` | 172.38 USD | 12,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `907.50` | 1,540.00 USD | 12,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `908.50` | 1,290.00 USD | 12,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `910.50` | 13,360.00 USD | 12,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `911.50` | 38,590.00 USD | 12,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `916.50` | 28,660.00 USD | 12,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `918.50` | 8,850.00 USD | 12,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `922.50` | 3,220.00 USD | 12,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `924.50` | 152.54 USD | 12,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `925.50` | 9,260.00 USD | 12,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `926.50` | 189.01 USD | 12,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `930.50` | 108.87 USD | 12,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `931.50` | 13,070.00 USD | 12,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `934.50` | 656.02 USD | 12,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `937.50` | 25,080.00 USD | 12,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `938.50` | 99,100.00 USD | 12,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `939.50` | 125.89 USD | 12,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `945.50` | 201.39 USD | 12,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `950.50` | 58,370.00 USD | 12,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `952.50` | 398.14 USD | 12,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `954.50` | 228.13 USD | 12,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `957.50` | 416.51 USD | 12,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `959.50` | 114.18 USD | 12,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `963.50` | 192,700.00 USD | 13,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `966.50` | 40,050.00 USD | 13,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `969.50` | 845,400.00 USD | 13,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `970.50` | 5,780.00 USD | 13,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `971.50` | 336.14 USD | 13,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `981.50` | 14,480.00 USD | 13,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `982.50` | 781,760.00 USD | 14,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `991.50` | 28,330.00 USD | 14,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `993.50` | 12,540.00 USD | 14,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `994.50` | 384,970.00 USD | 15,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `997.50` | 2,130.00 USD | 15,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1001.50` | 155,460.00 USD | 15,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1002.50` | 16,920.00 USD | 15,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1005.50` | 1,570.00 USD | 15,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1007.50` | 150,170.00 USD | 15,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1011.50` | 5,230.00 USD | 15,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1013.50` | 59,390.00 USD | 15,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1016.50` | 695,500.00 USD | 16,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1018.50` | 341,520.00 USD | 16,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1019.50` | 139.67 USD | 16,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1023.50` | 771,380.00 USD | 17,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1028.50` | 1,020,000.00 USD | 18,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1032.50` | 37,420.00 USD | 18,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1038.50` | 201.47 USD | 18,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1047.50` | 10,470.00 USD | 18,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1048.50` | 448.76 USD | 18,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1050.50` | 500.04 USD | 18,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1054.50` | 11,070.00 USD | 18,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1056.50` | 338,080.00 USD | 18,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1057.50` | 32,220.00 USD | 18,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1060.50` | 681,870.00 USD | 19,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1064.50` | 1,600.00 USD | 19,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1073.50` | 1,610.00 USD | 19,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1088.50` | 1,930.00 USD | 19,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1092.50` | 131,100.00 USD | 19,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1094.50` | 4,630.00 USD | 19,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1100.50` | 7,580.00 USD | 19,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1104.50` | 831.69 USD | 19,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1105.50` | 579,230.00 USD | 20,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1107.50` | 4,460.00 USD | 20,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1113.50` | 19,850.00 USD | 20,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1115.50` | 53,890.00 USD | 20,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1125.50` | 2,120.00 USD | 20,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1130.50` | 28,260.00 USD | 20,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1137.50` | 341,250.00 USD | 20,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1138.50` | 1,140,000.00 USD | 21,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1142.50` | 4,070.00 USD | 21,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1150.50` | 128.86 USD | 21,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1151.50` | 877.44 USD | 21,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1153.50` | 361,330.00 USD | 22,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1154.50` | 10,890.00 USD | 22,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1156.50` | 231,450.00 USD | 22,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1160.50` | 216,400.00 USD | 22,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1169.50` | 367.22 USD | 22,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1178.50` | 1,820.00 USD | 22,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1186.50` | 158.99 USD | 22,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1197.50` | 463.43 USD | 22,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1208.50` | 385.51 USD | 22,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1211.50` | 30,270.00 USD | 22,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1215.50` | 45,100.00 USD | 22,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1225.50` | 1,030.00 USD | 22,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1236.50` | 54,470.00 USD | 22,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1237.50` | 63,700.00 USD | 22,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1252.50` | 100.20 USD | 22,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1268.50` | 202.96 USD | 22,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1276.50` | 114,890.00 USD | 22,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1278.50` | 346.47 USD | 22,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1284.50` | 65,600.00 USD | 23,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1287.50` | 5,140.00 USD | 23,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1295.50` | 181.37 USD | 23,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1308.50` | 100.75 USD | 23,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1317.50` | 167,170.00 USD | 23,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1320.50` | 14,140.00 USD | 23,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1331.50` | 36,800.00 USD | 23,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1337.50` | 8,300.00 USD | 23,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1346.50` | 651.71 USD | 23,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1348.50` | 40,450.00 USD | 23,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1354.50` | 13,540.00 USD | 23,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1358.50` | 129,910.00 USD | 23,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1361.50` | 156,500.00 USD | 23,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1364.50` | 255.16 USD | 23,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1372.50` | 1,310.00 USD | 23,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1375.50` | 76,140.00 USD | 23,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1380.50` | 750,070.00 USD | 24,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

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
| `1D` | `604.40` | 36,770,000.00 USD | 0.00 USD | 36,770,000.00 USD | 53,940.00 USD | 2,300.00 USD | 18,770.00 USD |
| `1D` | `605.60` | 36,700,000.00 USD | 0.00 USD | 36,700,000.00 USD | 30,830.00 USD | 3,220.00 USD | 0.00 USD |
| `1D` | `606.80` | 36,660,000.00 USD | 0.00 USD | 36,660,000.00 USD | 39,340.00 USD | 7,740.00 USD | 10,460.00 USD |
| `1D` | `608.00` | 36,600,000.00 USD | 0.00 USD | 36,600,000.00 USD | 25,410.00 USD | 6,160.00 USD | 2,800.00 USD |
| `1D` | `609.20` | 36,570,000.00 USD | 0.00 USD | 36,570,000.00 USD | 23,150.00 USD | 0.00 USD | 1,710.00 USD |
| `1D` | `615.20` | 36,550,000.00 USD | 0.00 USD | 36,550,000.00 USD | 0.00 USD | 0.00 USD | 295,360.00 USD |
| `1D` | `617.60` | 36,250,000.00 USD | 0.00 USD | 36,250,000.00 USD | 290,320.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `620.00` | 35,960,000.00 USD | 0.00 USD | 35,960,000.00 USD | 175,630.00 USD | 33,270.00 USD | 0.00 USD |
| `1D` | `621.20` | 35,750,000.00 USD | 0.00 USD | 35,750,000.00 USD | 0.00 USD | 35,090.00 USD | 0.00 USD |
| `1D` | `623.60` | 35,720,000.00 USD | 0.00 USD | 35,720,000.00 USD | 460,160.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `624.80` | 35,260,000.00 USD | 0.00 USD | 35,260,000.00 USD | 238,630.00 USD | 31,450.00 USD | 274,040.00 USD |
| `1D` | `626.00` | 34,710,000.00 USD | 0.00 USD | 34,710,000.00 USD | 224,870.00 USD | 44,960.00 USD | 0.00 USD |
| `1D` | `627.20` | 34,440,000.00 USD | 0.00 USD | 34,440,000.00 USD | 186,500.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `630.80` | 34,250,000.00 USD | 0.00 USD | 34,250,000.00 USD | 0.00 USD | 0.00 USD | 254,760.00 USD |
| `1D` | `632.00` | 34,000,000.00 USD | 0.00 USD | 34,000,000.00 USD | 0.00 USD | 42,940.00 USD | 557,590.00 USD |
| `1D` | `633.20` | 33,400,000.00 USD | 0.00 USD | 33,400,000.00 USD | 461,240.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `634.40` | 32,940,000.00 USD | 0.00 USD | 32,940,000.00 USD | 0.00 USD | 23,580.00 USD | 0.00 USD |
| `1D` | `636.80` | 32,910,000.00 USD | 0.00 USD | 32,910,000.00 USD | 101,910.00 USD | 40,910.00 USD | 236,370.00 USD |
| `1D` | `639.20` | 32,540,000.00 USD | 0.00 USD | 32,540,000.00 USD | 184,100.00 USD | 37,610.00 USD | 0.00 USD |
| `1D` | `640.40` | 32,310,000.00 USD | 0.00 USD | 32,310,000.00 USD | 0.00 USD | 0.00 USD | 184,710.00 USD |
| `1D` | `641.60` | 32,130,000.00 USD | 0.00 USD | 32,130,000.00 USD | 33,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `642.80` | 32,100,000.00 USD | 0.00 USD | 32,100,000.00 USD | 116,460.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `645.20` | 31,980,000.00 USD | 0.00 USD | 31,980,000.00 USD | 308,550.00 USD | 0.00 USD | 341,610.00 USD |
| `1D` | `646.40` | 31,330,000.00 USD | 0.00 USD | 31,330,000.00 USD | 87,020.00 USD | 0.00 USD | 140,640.00 USD |
| `1D` | `647.60` | 31,100,000.00 USD | 0.00 USD | 31,100,000.00 USD | 237,260.00 USD | 29,080.00 USD | 0.00 USD |
| `1D` | `648.80` | 30,830,000.00 USD | 0.00 USD | 30,830,000.00 USD | 92,180.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `651.20` | 30,740,000.00 USD | 0.00 USD | 30,740,000.00 USD | 106,810.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `652.40` | 30,640,000.00 USD | 0.00 USD | 30,640,000.00 USD | 0.00 USD | 0.00 USD | 94,590.00 USD |
| `1D` | `653.60` | 30,540,000.00 USD | 0.00 USD | 30,540,000.00 USD | 0.00 USD | 26,830.00 USD | 0.00 USD |
| `1D` | `656.00` | 30,510,000.00 USD | 0.00 USD | 30,510,000.00 USD | 120,150.00 USD | 0.00 USD | 87,310.00 USD |
| `1D` | `657.20` | 30,310,000.00 USD | 0.00 USD | 30,310,000.00 USD | 5,100.00 USD | 21,320.00 USD | 738,390.00 USD |
| `1D` | `658.40` | 29,540,000.00 USD | 0.00 USD | 29,540,000.00 USD | 863,250.00 USD | 14,920.00 USD | 0.00 USD |
| `1D` | `659.60` | 28,660,000.00 USD | 0.00 USD | 28,660,000.00 USD | 0.00 USD | 7,460.00 USD | 81,440.00 USD |
| `1D` | `660.80` | 28,580,000.00 USD | 0.00 USD | 28,580,000.00 USD | 90,670.00 USD | 83,170.00 USD | 14,670.00 USD |
| `1D` | `662.00` | 28,390,000.00 USD | 0.00 USD | 28,390,000.00 USD | 445,210.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `663.20` | 27,940,000.00 USD | 0.00 USD | 27,940,000.00 USD | 202,560.00 USD | 92,740.00 USD | 19,650.00 USD |
| `7D` | `664.10` | 87,050,000.00 USD | 0.00 USD | 87,050,000.00 USD | 78,740.00 USD | 18,740.00 USD | 39,340.00 USD |
| `1D` | `664.40` | 27,630,000.00 USD | 0.00 USD | 27,630,000.00 USD | 1,200,000.00 USD | 48,410.00 USD | 21,160.00 USD |
| `7D` | `665.00` | 86,910,000.00 USD | 0.00 USD | 86,910,000.00 USD | 92,030.00 USD | 22,990.00 USD | 37,000.00 USD |
| `1D` | `665.60` | 26,360,000.00 USD | 0.00 USD | 26,360,000.00 USD | 680,490.00 USD | 5,880.00 USD | 11,460.00 USD |
| `7D` | `665.90` | 86,760,000.00 USD | 0.00 USD | 86,760,000.00 USD | 264,020.00 USD | 71,380.00 USD | 63,410.00 USD |
| `1D` | `666.80` | 25,660,000.00 USD | 0.00 USD | 25,660,000.00 USD | 601,110.00 USD | 100,720.00 USD | 696,480.00 USD |
| `7D` | `666.80` | 86,360,000.00 USD | 0.00 USD | 86,360,000.00 USD | 198,550.00 USD | 33,320.00 USD | 61,710.00 USD |
| `7D` | `667.70` | 86,070,000.00 USD | 0.00 USD | 86,070,000.00 USD | 199,690.00 USD | 45,130.00 USD | 51,340.00 USD |
| `1D` | `668.00` | 24,260,000.00 USD | 0.00 USD | 24,260,000.00 USD | 218,160.00 USD | 124,030.00 USD | 9,290.00 USD |
| `7D` | `668.60` | 85,770,000.00 USD | 0.00 USD | 85,770,000.00 USD | 387,530.00 USD | 92,860.00 USD | 51,060.00 USD |
| `1D` | `669.20` | 23,910,000.00 USD | 0.00 USD | 23,910,000.00 USD | 517,710.00 USD | 74,270.00 USD | 10,400.00 USD |
| `7D` | `669.50` | 85,240,000.00 USD | 0.00 USD | 85,240,000.00 USD | 341,150.00 USD | 38,130.00 USD | 108,970.00 USD |
| `1D` | `670.40` | 23,310,000.00 USD | 0.00 USD | 23,310,000.00 USD | 258,440.00 USD | 3,950.00 USD | 1,480,000.00 USD |
| `7D` | `670.40` | 84,750,000.00 USD | 0.00 USD | 84,750,000.00 USD | 319,660.00 USD | 93,800.00 USD | 77,380.00 USD |
| `7D` | `671.30` | 84,260,000.00 USD | 0.00 USD | 84,260,000.00 USD | 335,750.00 USD | 57,500.00 USD | 42,050.00 USD |
| `1D` | `671.60` | 21,560,000.00 USD | 0.00 USD | 21,560,000.00 USD | 1,900,000.00 USD | 18,100.00 USD | 16,650.00 USD |
| `7D` | `672.20` | 83,830,000.00 USD | 0.00 USD | 83,830,000.00 USD | 180,230.00 USD | 62,620.00 USD | 74,250.00 USD |
| `1D` | `672.80` | 19,630,000.00 USD | 0.00 USD | 19,630,000.00 USD | 329,500.00 USD | 32,620.00 USD | 670,660.00 USD |
| `7D` | `673.10` | 83,510,000.00 USD | 0.00 USD | 83,510,000.00 USD | 394,120.00 USD | 64,970.00 USD | 42,710.00 USD |
| `1D` | `674.00` | 18,600,000.00 USD | 0.00 USD | 18,600,000.00 USD | 366,350.00 USD | 38,230.00 USD | 1,440,000.00 USD |
| `7D` | `674.00` | 83,010,000.00 USD | 0.00 USD | 83,010,000.00 USD | 335,670.00 USD | 105,910.00 USD | 80,360.00 USD |
| `7D` | `674.90` | 82,490,000.00 USD | 0.00 USD | 82,490,000.00 USD | 247,070.00 USD | 31,490.00 USD | 44,420.00 USD |
| `1D` | `675.20` | 16,760,000.00 USD | 0.00 USD | 16,760,000.00 USD | 2,020,000.00 USD | 310,280.00 USD | 260,690.00 USD |
| `7D` | `675.80` | 82,160,000.00 USD | 0.00 USD | 82,160,000.00 USD | 387,400.00 USD | 26,020.00 USD | 79,190.00 USD |
| `1D` | `676.40` | 14,170,000.00 USD | 0.00 USD | 14,170,000.00 USD | 209,330.00 USD | 273,150.00 USD | 85,400.00 USD |
| `7D` | `676.70` | 81,670,000.00 USD | 0.00 USD | 81,670,000.00 USD | 509,100.00 USD | 35,490.00 USD | 126,570.00 USD |
| `1D` | `677.60` | 13,600,000.00 USD | 0.00 USD | 13,600,000.00 USD | 495,590.00 USD | 121,270.00 USD | 0.00 USD |
| `7D` | `677.60` | 81,000,000.00 USD | 0.00 USD | 81,000,000.00 USD | 409,810.00 USD | 0.00 USD | 63,990.00 USD |
| `7D` | `678.50` | 80,530,000.00 USD | 0.00 USD | 80,530,000.00 USD | 120,190.00 USD | 0.00 USD | 26,990.00 USD |
| `1D` | `678.80` | 12,980,000.00 USD | 0.00 USD | 12,980,000.00 USD | 1,030,000.00 USD | 113,650.00 USD | 0.00 USD |
| `7D` | `679.40` | 80,380,000.00 USD | 0.00 USD | 80,380,000.00 USD | 116,510.00 USD | 10,480.00 USD | 40,610.00 USD |
| `1D` | `680.00` | 11,840,000.00 USD | 0.00 USD | 11,840,000.00 USD | 1,200,000.00 USD | 166,940.00 USD | 0.00 USD |
| `7D` | `680.30` | 80,210,000.00 USD | 0.00 USD | 80,210,000.00 USD | 166,780.00 USD | 13,510.00 USD | 0.00 USD |
| `1D` | `681.20` | 10,480,000.00 USD | 0.00 USD | 10,480,000.00 USD | 15,290.00 USD | 168,520.00 USD | 0.00 USD |
| `7D` | `681.20` | 80,030,000.00 USD | 0.00 USD | 80,030,000.00 USD | 106,280.00 USD | 7,050.00 USD | 35,170.00 USD |
| `7D` | `682.10` | 79,880,000.00 USD | 0.00 USD | 79,880,000.00 USD | 0.00 USD | 23,360.00 USD | 27,620.00 USD |
| `1D` | `682.40` | 10,290,000.00 USD | 0.00 USD | 10,290,000.00 USD | 35,750.00 USD | 242,460.00 USD | 0.00 USD |
| `7D` | `683.00` | 79,830,000.00 USD | 0.00 USD | 79,830,000.00 USD | 175,930.00 USD | 28,470.00 USD | 11,520.00 USD |
| `1D` | `683.60` | 10,020,000.00 USD | 0.00 USD | 10,020,000.00 USD | 138,150.00 USD | 133,120.00 USD | 0.00 USD |
| `7D` | `683.90` | 79,620,000.00 USD | 0.00 USD | 79,620,000.00 USD | 77,000.00 USD | 29,510.00 USD | 17,480.00 USD |
| `1D` | `684.80` | 9,740,000.00 USD | 0.00 USD | 9,740,000.00 USD | 0.00 USD | 32,240.00 USD | 0.00 USD |
| `7D` | `684.80` | 79,490,000.00 USD | 0.00 USD | 79,490,000.00 USD | 246,080.00 USD | 9,850.00 USD | 39,550.00 USD |
| `7D` | `685.70` | 79,200,000.00 USD | 0.00 USD | 79,200,000.00 USD | 197,040.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `686.00` | 9,710,000.00 USD | 0.00 USD | 9,710,000.00 USD | 694,060.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `686.60` | 79,000,000.00 USD | 0.00 USD | 79,000,000.00 USD | 62,990.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `687.20` | 9,020,000.00 USD | 0.00 USD | 9,020,000.00 USD | 771,380.00 USD | 0.00 USD | 2,790,000.00 USD |
| `7D` | `687.50` | 78,940,000.00 USD | 0.00 USD | 78,940,000.00 USD | 148,480.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `688.40` | 5,460,000.00 USD | 0.00 USD | 5,460,000.00 USD | 3,940.00 USD | 0.00 USD | 854,020.00 USD |
| `7D` | `688.40` | 78,790,000.00 USD | 0.00 USD | 78,790,000.00 USD | 67,880.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `689.30` | 78,720,000.00 USD | 0.00 USD | 78,720,000.00 USD | 84,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `689.60` | 4,600,000.00 USD | 0.00 USD | 4,600,000.00 USD | 1,940,000.00 USD | 0.00 USD | 466,010.00 USD |
| `7D` | `690.20` | 78,640,000.00 USD | 0.00 USD | 78,640,000.00 USD | 283,920.00 USD | 63,230.00 USD | 82,450.00 USD |
| `1D` | `690.80` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 101,670.00 USD | 117,900.00 USD | 0.00 USD |
| `7D` | `691.10` | 78,210,000.00 USD | 0.00 USD | 78,210,000.00 USD | 362,020.00 USD | 61,370.00 USD | 81,090.00 USD |
| `1D` | `692.00` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 27,340.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `692.00` | 77,700,000.00 USD | 0.00 USD | 77,700,000.00 USD | 322,430.00 USD | 18,850.00 USD | 58,910.00 USD |
| `7D` | `692.90` | 77,300,000.00 USD | 0.00 USD | 77,300,000.00 USD | 280,830.00 USD | 19,470.00 USD | 0.00 USD |
| `7D` | `693.80` | 77,000,000.00 USD | 0.00 USD | 77,000,000.00 USD | 305,720.00 USD | 39,210.00 USD | 0.00 USD |
| `7D` | `694.70` | 76,660,000.00 USD | 0.00 USD | 76,660,000.00 USD | 279,840.00 USD | 36,640.00 USD | 35,490.00 USD |
| `1D` | `695.60` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 0.00 USD | 137,440.00 USD | 0.00 USD |
| `7D` | `695.60` | 76,300,000.00 USD | 0.00 USD | 76,300,000.00 USD | 120,440.00 USD | 0.00 USD | 21,670.00 USD |
| `7D` | `696.50` | 76,160,000.00 USD | 0.00 USD | 76,160,000.00 USD | 140,370.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `697.40` | 76,020,000.00 USD | 0.00 USD | 76,020,000.00 USD | 189,100.00 USD | 19,230.00 USD | 0.00 USD |
| `7D` | `698.30` | 75,810,000.00 USD | 0.00 USD | 75,810,000.00 USD | 273,520.00 USD | 33,120.00 USD | 54,800.00 USD |
| `7D` | `699.20` | 75,450,000.00 USD | 0.00 USD | 75,450,000.00 USD | 274,810.00 USD | 12,670.00 USD | 11,820.00 USD |
| `7D` | `700.10` | 75,150,000.00 USD | 0.00 USD | 75,150,000.00 USD | 225,450.00 USD | 40,820.00 USD | 27,440.00 USD |
| `7D` | `701.00` | 74,860,000.00 USD | 0.00 USD | 74,860,000.00 USD | 237,800.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `701.60` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `701.90` | 74,620,000.00 USD | 0.00 USD | 74,620,000.00 USD | 135,260.00 USD | 41,260.00 USD | 89,700.00 USD |
| `1D` | `702.80` | 263,170.00 USD | 0.00 USD | 263,170.00 USD | 0.00 USD | 166,340.00 USD | 0.00 USD |
| `7D` | `702.80` | 74,360,000.00 USD | 0.00 USD | 74,360,000.00 USD | 416,820.00 USD | 57,470.00 USD | 36,720.00 USD |
| `7D` | `703.70` | 73,840,000.00 USD | 0.00 USD | 73,840,000.00 USD | 311,800.00 USD | 44,990.00 USD | 0.00 USD |
| `7D` | `704.60` | 73,490,000.00 USD | 0.00 USD | 73,490,000.00 USD | 537,050.00 USD | 136,550.00 USD | 194,460.00 USD |
| `1D` | `705.20` | 96,830.00 USD | 0.00 USD | 96,830.00 USD | 0.00 USD | 96,830.00 USD | 0.00 USD |
| `7D` | `705.50` | 72,620,000.00 USD | 0.00 USD | 72,620,000.00 USD | 920,340.00 USD | 162,820.00 USD | 236,670.00 USD |
| `7D` | `706.40` | 71,300,000.00 USD | 0.00 USD | 71,300,000.00 USD | 523,540.00 USD | 104,380.00 USD | 231,200.00 USD |
| `7D` | `707.30` | 70,440,000.00 USD | 0.00 USD | 70,440,000.00 USD | 604,060.00 USD | 90,200.00 USD | 53,960.00 USD |
| `7D` | `708.20` | 69,690,000.00 USD | 0.00 USD | 69,690,000.00 USD | 796,640.00 USD | 138,200.00 USD | 42,800.00 USD |
| `1D` | `708.50` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `709.10` | 68,710,000.00 USD | 0.00 USD | 68,710,000.00 USD | 392,150.00 USD | 156,040.00 USD | 195,500.00 USD |
| `7D` | `710.00` | 67,970,000.00 USD | 0.00 USD | 67,970,000.00 USD | 450,480.00 USD | 167,090.00 USD | 176,960.00 USD |
| `7D` | `710.90` | 67,180,000.00 USD | 0.00 USD | 67,180,000.00 USD | 922,450.00 USD | 160,040.00 USD | 236,990.00 USD |
| `7D` | `711.80` | 65,860,000.00 USD | 0.00 USD | 65,860,000.00 USD | 608,910.00 USD | 232,130.00 USD | 114,740.00 USD |
| `7D` | `712.70` | 64,900,000.00 USD | 0.00 USD | 64,900,000.00 USD | 1,190,000.00 USD | 217,390.00 USD | 236,970.00 USD |
| `7D` | `713.60` | 63,260,000.00 USD | 0.00 USD | 63,260,000.00 USD | 2,250,000.00 USD | 279,180.00 USD | 308,960.00 USD |
| `7D` | `714.50` | 60,410,000.00 USD | 0.00 USD | 60,410,000.00 USD | 508,400.00 USD | 209,320.00 USD | 292,980.00 USD |
| `7D` | `715.40` | 59,400,000.00 USD | 0.00 USD | 59,400,000.00 USD | 1,050,000.00 USD | 419,310.00 USD | 329,730.00 USD |
| `1D` | `716.00` | 855,230.00 USD | 855,230.00 USD | 0.00 USD | 0.00 USD | 83,170.00 USD | 772,060.00 USD |
| `7D` | `716.30` | 57,600,000.00 USD | 0.00 USD | 57,600,000.00 USD | 1,080,000.00 USD | 324,540.00 USD | 233,140.00 USD |
| `1D` | `717.20` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 214,720.00 USD | 466,010.00 USD |
| `7D` | `717.20` | 55,960,000.00 USD | 0.00 USD | 55,960,000.00 USD | 581,610.00 USD | 398,030.00 USD | 387,120.00 USD |
| `7D` | `718.10` | 54,590,000.00 USD | 0.00 USD | 54,590,000.00 USD | 1,690,000.00 USD | 246,320.00 USD | 151,880.00 USD |
| `1D` | `718.40` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 205,630.00 USD | 0.00 USD |
| `7D` | `719.00` | 52,510,000.00 USD | 0.00 USD | 52,510,000.00 USD | 670,390.00 USD | 137,460.00 USD | 211,490.00 USD |
| `1D` | `719.60` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 48,410.00 USD | 0.00 USD |
| `7D` | `719.90` | 51,490,000.00 USD | 0.00 USD | 51,490,000.00 USD | 618,020.00 USD | 173,240.00 USD | 186,780.00 USD |
| `1D` | `720.80` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 204,540.00 USD | 0.00 USD |
| `7D` | `720.80` | 50,510,000.00 USD | 0.00 USD | 50,510,000.00 USD | 1,010,000.00 USD | 52,490.00 USD | 180,370.00 USD |
| `7D` | `721.70` | 49,260,000.00 USD | 0.00 USD | 49,260,000.00 USD | 1,950,000.00 USD | 237,690.00 USD | 653,400.00 USD |
| `1D` | `722.00` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 78,640.00 USD | 0.00 USD |
| `7D` | `722.60` | 46,430,000.00 USD | 0.00 USD | 46,430,000.00 USD | 1,930,000.00 USD | 108,200.00 USD | 229,380.00 USD |
| `1D` | `723.20` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 300,460.00 USD | 0.00 USD |
| `7D` | `723.50` | 44,160,000.00 USD | 0.00 USD | 44,160,000.00 USD | 640,550.00 USD | 140,550.00 USD | 293,670.00 USD |
| `1D` | `724.40` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 137,440.00 USD | 0.00 USD |
| `7D` | `724.40` | 43,080,000.00 USD | 0.00 USD | 43,080,000.00 USD | 663,550.00 USD | 186,780.00 USD | 130,770.00 USD |
| `7D` | `725.30` | 42,100,000.00 USD | 0.00 USD | 42,100,000.00 USD | 1,760,000.00 USD | 418,390.00 USD | 396,690.00 USD |
| `1D` | `725.60` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 0.00 USD | 57,080.00 USD | 0.00 USD |
| `7D` | `726.20` | 39,520,000.00 USD | 0.00 USD | 39,520,000.00 USD | 1,060,000.00 USD | 311,550.00 USD | 460,020.00 USD |
| `1D` | `726.80` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 64,470.00 USD | 0.00 USD |
| `7D` | `727.10` | 37,690,000.00 USD | 0.00 USD | 37,690,000.00 USD | 1,230,000.00 USD | 331,980.00 USD | 241,010.00 USD |
| `7D` | `728.00` | 35,890,000.00 USD | 0.00 USD | 35,890,000.00 USD | 3,110,000.00 USD | 778,750.00 USD | 388,930.00 USD |
| `7D` | `728.90` | 31,610,000.00 USD | 0.00 USD | 31,610,000.00 USD | 2,330,000.00 USD | 317,590.00 USD | 644,150.00 USD |
| `1D` | `729.20` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 386,030.00 USD |
| `7D` | `729.80` | 28,320,000.00 USD | 0.00 USD | 28,320,000.00 USD | 1,320,000.00 USD | 430,010.00 USD | 339,140.00 USD |
| `1D` | `730.40` | 6,380,000.00 USD | 6,380,000.00 USD | 0.00 USD | 1,540,000.00 USD | 107,360.00 USD | 1,710,000.00 USD |
| `7D` | `730.70` | 26,230,000.00 USD | 0.00 USD | 26,230,000.00 USD | 2,760,000.00 USD | 351,520.00 USD | 587,010.00 USD |
| `1D` | `731.60` | 7,630,000.00 USD | 7,630,000.00 USD | 0.00 USD | 952,750.00 USD | 63,350.00 USD | 233,010.00 USD |
| `7D` | `731.60` | 22,530,000.00 USD | 0.00 USD | 22,530,000.00 USD | 1,530,000.00 USD | 133,980.00 USD | 261,910.00 USD |
| `7D` | `732.50` | 20,610,000.00 USD | 0.00 USD | 20,610,000.00 USD | 465,880.00 USD | 221,510.00 USD | 96,400.00 USD |
| `1D` | `732.80` | 9,450,000.00 USD | 9,450,000.00 USD | 0.00 USD | 998,900.00 USD | 120,350.00 USD | 703,180.00 USD |
| `7D` | `733.40` | 19,820,000.00 USD | 0.00 USD | 19,820,000.00 USD | 1,910,000.00 USD | 158,310.00 USD | 338,540.00 USD |
| `1D` | `734.00` | 9,940,000.00 USD | 9,940,000.00 USD | 0.00 USD | 344,230.00 USD | 145,390.00 USD | 0.00 USD |
| `7D` | `734.30` | 17,420,000.00 USD | 0.00 USD | 17,420,000.00 USD | 1,580,000.00 USD | 288,470.00 USD | 244,940.00 USD |
| `1D` | `735.20` | 10,800,000.00 USD | 10,800,000.00 USD | 0.00 USD | 613,800.00 USD | 246,950.00 USD | 0.00 USD |
| `7D` | `735.20` | 15,310,000.00 USD | 0.00 USD | 15,310,000.00 USD | 1,330,000.00 USD | 172,940.00 USD | 437,510.00 USD |
| `7D` | `736.10` | 13,370,000.00 USD | 0.00 USD | 13,370,000.00 USD | 2,130,000.00 USD | 181,990.00 USD | 484,910.00 USD |
| `1D` | `736.40` | 12,710,000.00 USD | 12,710,000.00 USD | 0.00 USD | 1,300,000.00 USD | 22,190.00 USD | 590,930.00 USD |
| `7D` | `737.00` | 10,570,000.00 USD | 0.00 USD | 10,570,000.00 USD | 2,360,000.00 USD | 175,330.00 USD | 633,690.00 USD |
| `1D` | `737.60` | 12,960,000.00 USD | 12,960,000.00 USD | 0.00 USD | 160,280.00 USD | 94,030.00 USD | 0.00 USD |
| `7D` | `737.90` | 7,400,000.00 USD | 0.00 USD | 7,400,000.00 USD | 3,420,000.00 USD | 72,280.00 USD | 374,090.00 USD |
| `1D` | `738.80` | 14,160,000.00 USD | 14,160,000.00 USD | 0.00 USD | 658,340.00 USD | 68,720.00 USD | 472,930.00 USD |
| `7D` | `738.80` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 522,950.00 USD | 20,210.00 USD | 155,300.00 USD |
| `7D` | `739.70` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 352,500.00 USD | 0.00 USD | 203,030.00 USD |
| `1D` | `740.00` | 15,290,000.00 USD | 15,290,000.00 USD | 0.00 USD | 648,020.00 USD | 0.00 USD | 476,790.00 USD |
| `7D` | `740.60` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 1,090,000.00 USD | 0.00 USD | 33,390.00 USD |
| `1D` | `741.20` | 15,940,000.00 USD | 15,940,000.00 USD | 0.00 USD | 474,360.00 USD | 166,390.00 USD | 7,010.00 USD |
| `7D` | `741.50` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 257,630.00 USD | 0.00 USD | 208,590.00 USD |
| `1D` | `742.40` | 16,230,000.00 USD | 16,230,000.00 USD | 0.00 USD | 291,160.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `742.40` | 689,850.00 USD | 0.00 USD | 689,850.00 USD | 0.00 USD | 0.00 USD | 183,920.00 USD |
| `7D` | `743.30` | 505,930.00 USD | 0.00 USD | 505,930.00 USD | 0.00 USD | 0.00 USD | 57,580.00 USD |
| `1D` | `743.60` | 16,790,000.00 USD | 16,790,000.00 USD | 0.00 USD | 120,950.00 USD | 0.00 USD | 436,560.00 USD |
| `7D` | `744.20` | 448,350.00 USD | 0.00 USD | 448,350.00 USD | 0.00 USD | 257,580.00 USD | 141,790.00 USD |
| `1D` | `744.80` | 18,620,000.00 USD | 18,620,000.00 USD | 0.00 USD | 878,190.00 USD | 106,580.00 USD | 854,020.00 USD |
| `7D` | `745.10` | 48,980.00 USD | 0.00 USD | 48,980.00 USD | 0.00 USD | 48,980.00 USD | 0.00 USD |
| `7D` | `745.20` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `746.00` | 19,210,000.00 USD | 19,210,000.00 USD | 0.00 USD | 482,060.00 USD | 106,280.00 USD | 0.00 USD |
| `7D` | `746.00` | 999,320.00 USD | 999,320.00 USD | 0.00 USD | 999,320.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `746.90` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 215,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `747.20` | 20,790,000.00 USD | 20,790,000.00 USD | 0.00 USD | 748,640.00 USD | 67,980.00 USD | 758,780.00 USD |
| `1D` | `748.40` | 21,220,000.00 USD | 21,220,000.00 USD | 0.00 USD | 286,680.00 USD | 72,690.00 USD | 73,330.00 USD |
| `1D` | `749.60` | 21,640,000.00 USD | 21,640,000.00 USD | 0.00 USD | 417,840.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `752.00` | 22,200,000.00 USD | 22,200,000.00 USD | 0.00 USD | 0.00 USD | 25,010.00 USD | 539,620.00 USD |
| `1D` | `753.20` | 22,690,000.00 USD | 22,690,000.00 USD | 0.00 USD | 229,820.00 USD | 3,810.00 USD | 248,870.00 USD |
| `1D` | `754.40` | 23,200,000.00 USD | 23,200,000.00 USD | 0.00 USD | 383,510.00 USD | 70,850.00 USD | 57,280.00 USD |
| `7D` | `755.00` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 59,560.00 USD | 0.00 USD |
| `1D` | `755.60` | 23,890,000.00 USD | 23,890,000.00 USD | 0.00 USD | 384,280.00 USD | 254,460.00 USD | 56,900.00 USD |
| `1D` | `756.80` | 24,440,000.00 USD | 24,440,000.00 USD | 0.00 USD | 422,820.00 USD | 24,970.00 USD | 95,500.00 USD |
| `7D` | `756.80` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 47,340.00 USD | 0.00 USD |
| `7D` | `757.70` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 475,510.00 USD | 113,240.00 USD | 0.00 USD |
| `1D` | `758.00` | 25,140,000.00 USD | 25,140,000.00 USD | 0.00 USD | 482,940.00 USD | 189,940.00 USD | 32,720.00 USD |
| `7D` | `758.60` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `759.20` | 26,800,000.00 USD | 26,800,000.00 USD | 0.00 USD | 1,260,000.00 USD | 122,880.00 USD | 273,090.00 USD |
| `1D` | `760.40` | 27,490,000.00 USD | 27,490,000.00 USD | 0.00 USD | 508,240.00 USD | 100,270.00 USD | 80,660.00 USD |
| `7D` | `760.40` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 0.00 USD | 27,650.00 USD | 42,540.00 USD |
| `7D` | `761.30` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 10,750.00 USD | 211,960.00 USD | 100,630.00 USD |
| `1D` | `761.60` | 28,890,000.00 USD | 28,890,000.00 USD | 0.00 USD | 886,440.00 USD | 102,890.00 USD | 409,630.00 USD |
| `7D` | `762.20` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 699,820.00 USD | 179,270.00 USD |
| `1D` | `762.80` | 31,810,000.00 USD | 31,810,000.00 USD | 0.00 USD | 2,120,000.00 USD | 214,840.00 USD | 583,620.00 USD |
| `7D` | `763.10` | 7,830,000.00 USD | 7,830,000.00 USD | 0.00 USD | 2,460,000.00 USD | 590,460.00 USD | 404,720.00 USD |
| `1D` | `764.00` | 34,370,000.00 USD | 34,370,000.00 USD | 0.00 USD | 1,980,000.00 USD | 319,550.00 USD | 268,150.00 USD |
| `7D` | `764.00` | 10,270,000.00 USD | 10,270,000.00 USD | 0.00 USD | 1,590,000.00 USD | 441,980.00 USD | 402,300.00 USD |
| `7D` | `764.90` | 12,470,000.00 USD | 12,470,000.00 USD | 0.00 USD | 1,450,000.00 USD | 352,570.00 USD | 395,630.00 USD |
| `1D` | `765.20` | 35,900,000.00 USD | 35,900,000.00 USD | 0.00 USD | 1,070,000.00 USD | 230,270.00 USD | 220,460.00 USD |
| `7D` | `765.80` | 15,460,000.00 USD | 15,460,000.00 USD | 0.00 USD | 2,470,000.00 USD | 107,550.00 USD | 416,290.00 USD |
| `1D` | `766.40` | 38,020,000.00 USD | 38,020,000.00 USD | 0.00 USD | 1,270,000.00 USD | 269,470.00 USD | 582,040.00 USD |
| `7D` | `766.70` | 20,050,000.00 USD | 20,050,000.00 USD | 0.00 USD | 3,330,000.00 USD | 416,530.00 USD | 842,330.00 USD |
| `1D` | `767.60` | 41,310,000.00 USD | 41,310,000.00 USD | 0.00 USD | 2,840,000.00 USD | 130,060.00 USD | 331,970.00 USD |
| `7D` | `767.60` | 23,430,000.00 USD | 23,430,000.00 USD | 0.00 USD | 2,790,000.00 USD | 123,530.00 USD | 467,840.00 USD |
| `7D` | `768.50` | 25,660,000.00 USD | 25,660,000.00 USD | 0.00 USD | 1,840,000.00 USD | 95,830.00 USD | 281,920.00 USD |
| `1D` | `768.80` | 42,840,000.00 USD | 42,840,000.00 USD | 0.00 USD | 1,250,000.00 USD | 100,610.00 USD | 176,320.00 USD |
| `7D` | `769.40` | 26,810,000.00 USD | 26,810,000.00 USD | 0.00 USD | 565,780.00 USD | 249,950.00 USD | 333,550.00 USD |
| `1D` | `770.00` | 43,770,000.00 USD | 43,770,000.00 USD | 0.00 USD | 663,210.00 USD | 180,380.00 USD | 84,990.00 USD |
| `7D` | `770.30` | 29,310,000.00 USD | 29,310,000.00 USD | 0.00 USD | 1,900,000.00 USD | 240,530.00 USD | 364,650.00 USD |
| `1D` | `771.20` | 44,850,000.00 USD | 44,850,000.00 USD | 0.00 USD | 678,410.00 USD | 56,760.00 USD | 340,350.00 USD |
| `7D` | `771.20` | 30,770,000.00 USD | 30,770,000.00 USD | 0.00 USD | 1,050,000.00 USD | 242,570.00 USD | 162,680.00 USD |
| `7D` | `772.10` | 33,190,000.00 USD | 33,190,000.00 USD | 0.00 USD | 1,750,000.00 USD | 252,650.00 USD | 419,070.00 USD |
| `1D` | `772.40` | 46,220,000.00 USD | 46,220,000.00 USD | 0.00 USD | 509,090.00 USD | 216,960.00 USD | 647,240.00 USD |
| `7D` | `773.00` | 35,800,000.00 USD | 35,800,000.00 USD | 0.00 USD | 1,950,000.00 USD | 325,680.00 USD | 338,170.00 USD |
| `1D` | `773.60` | 47,550,000.00 USD | 47,550,000.00 USD | 0.00 USD | 993,840.00 USD | 124,190.00 USD | 206,930.00 USD |
| `7D` | `773.90` | 37,600,000.00 USD | 37,600,000.00 USD | 0.00 USD | 1,220,000.00 USD | 276,760.00 USD | 293,960.00 USD |
| `1D` | `774.80` | 48,950,000.00 USD | 48,950,000.00 USD | 0.00 USD | 1,220,000.00 USD | 116,800.00 USD | 67,110.00 USD |
| `7D` | `774.80` | 39,980,000.00 USD | 39,980,000.00 USD | 0.00 USD | 1,310,000.00 USD | 568,930.00 USD | 502,710.00 USD |
| `7D` | `775.70` | 42,470,000.00 USD | 42,470,000.00 USD | 0.00 USD | 1,830,000.00 USD | 470,960.00 USD | 187,170.00 USD |
| `1D` | `776.00` | 49,640,000.00 USD | 49,640,000.00 USD | 0.00 USD | 469,240.00 USD | 137,760.00 USD | 79,080.00 USD |
| `7D` | `776.60` | 44,740,000.00 USD | 44,740,000.00 USD | 0.00 USD | 1,630,000.00 USD | 269,050.00 USD | 378,590.00 USD |
| `1D` | `777.20` | 50,290,000.00 USD | 50,290,000.00 USD | 0.00 USD | 421,750.00 USD | 125,850.00 USD | 110,390.00 USD |
| `7D` | `777.50` | 46,480,000.00 USD | 46,480,000.00 USD | 0.00 USD | 1,350,000.00 USD | 243,990.00 USD | 148,450.00 USD |
| `1D` | `778.40` | 52,220,000.00 USD | 52,220,000.00 USD | 0.00 USD | 1,440,000.00 USD | 107,990.00 USD | 383,820.00 USD |
| `7D` | `778.40` | 48,170,000.00 USD | 48,170,000.00 USD | 0.00 USD | 1,180,000.00 USD | 307,370.00 USD | 206,530.00 USD |
| `7D` | `779.30` | 49,730,000.00 USD | 49,730,000.00 USD | 0.00 USD | 1,240,000.00 USD | 188,170.00 USD | 123,650.00 USD |
| `1D` | `779.60` | 53,450,000.00 USD | 53,450,000.00 USD | 0.00 USD | 941,870.00 USD | 114,610.00 USD | 171,610.00 USD |
| `7D` | `780.20` | 51,100,000.00 USD | 51,100,000.00 USD | 0.00 USD | 1,070,000.00 USD | 86,470.00 USD | 218,750.00 USD |
| `1D` | `780.80` | 54,240,000.00 USD | 54,240,000.00 USD | 0.00 USD | 543,830.00 USD | 123,860.00 USD | 119,950.00 USD |
| `7D` | `781.10` | 52,710,000.00 USD | 52,710,000.00 USD | 0.00 USD | 1,270,000.00 USD | 90,990.00 USD | 242,450.00 USD |
| `1D` | `782.00` | 55,760,000.00 USD | 55,760,000.00 USD | 0.00 USD | 1,070,000.00 USD | 100,360.00 USD | 352,430.00 USD |
| `7D` | `782.00` | 54,610,000.00 USD | 54,610,000.00 USD | 0.00 USD | 1,510,000.00 USD | 87,670.00 USD | 301,190.00 USD |
| `7D` | `782.90` | 56,600,000.00 USD | 56,600,000.00 USD | 0.00 USD | 1,750,000.00 USD | 36,140.00 USD | 202,700.00 USD |
| `1D` | `783.20` | 57,120,000.00 USD | 57,120,000.00 USD | 0.00 USD | 1,090,000.00 USD | 85,870.00 USD | 188,040.00 USD |
| `7D` | `783.80` | 57,170,000.00 USD | 57,170,000.00 USD | 0.00 USD | 508,000.00 USD | 10,100.00 USD | 54,380.00 USD |
| `1D` | `784.40` | 57,680,000.00 USD | 57,680,000.00 USD | 0.00 USD | 485,610.00 USD | 41,570.00 USD | 28,210.00 USD |
| `7D` | `784.70` | 57,480,000.00 USD | 57,480,000.00 USD | 0.00 USD | 208,380.00 USD | 28,260.00 USD | 70,300.00 USD |
| `1D` | `785.60` | 58,210,000.00 USD | 58,210,000.00 USD | 0.00 USD | 482,590.00 USD | 24,180.00 USD | 20,700.00 USD |
| `7D` | `785.60` | 58,610,000.00 USD | 58,610,000.00 USD | 0.00 USD | 1,010,000.00 USD | 54,140.00 USD | 71,180.00 USD |
| `7D` | `786.50` | 59,000,000.00 USD | 59,000,000.00 USD | 0.00 USD | 329,230.00 USD | 30,660.00 USD | 23,970.00 USD |
| `1D` | `786.80` | 58,510,000.00 USD | 58,510,000.00 USD | 0.00 USD | 244,430.00 USD | 26,670.00 USD | 37,000.00 USD |
| `7D` | `787.40` | 59,580,000.00 USD | 59,580,000.00 USD | 0.00 USD | 470,050.00 USD | 17,630.00 USD | 91,050.00 USD |
| `1D` | `788.00` | 59,440,000.00 USD | 59,440,000.00 USD | 0.00 USD | 492,120.00 USD | 31,760.00 USD | 399,040.00 USD |
| `7D` | `788.30` | 59,940,000.00 USD | 59,940,000.00 USD | 0.00 USD | 202,630.00 USD | 82,380.00 USD | 81,230.00 USD |
| `1D` | `789.20` | 59,980,000.00 USD | 59,980,000.00 USD | 0.00 USD | 434,090.00 USD | 59,690.00 USD | 47,810.00 USD |
| `7D` | `789.20` | 60,780,000.00 USD | 60,780,000.00 USD | 0.00 USD | 698,830.00 USD | 81,250.00 USD | 55,990.00 USD |
| `7D` | `790.10` | 61,270,000.00 USD | 61,270,000.00 USD | 0.00 USD | 299,250.00 USD | 104,360.00 USD | 88,890.00 USD |
| `1D` | `790.40` | 60,660,000.00 USD | 60,660,000.00 USD | 0.00 USD | 469,100.00 USD | 49,740.00 USD | 163,110.00 USD |
| `7D` | `791.00` | 62,150,000.00 USD | 62,150,000.00 USD | 0.00 USD | 693,290.00 USD | 82,870.00 USD | 100,420.00 USD |
| `1D` | `791.60` | 61,090,000.00 USD | 61,090,000.00 USD | 0.00 USD | 364,500.00 USD | 52,300.00 USD | 8,530.00 USD |
| `7D` | `791.90` | 63,030,000.00 USD | 63,030,000.00 USD | 0.00 USD | 816,380.00 USD | 16,830.00 USD | 46,300.00 USD |
| `1D` | `792.80` | 61,260,000.00 USD | 61,260,000.00 USD | 0.00 USD | 169,620.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `792.80` | 63,250,000.00 USD | 63,250,000.00 USD | 0.00 USD | 205,450.00 USD | 0.00 USD | 14,670.00 USD |
| `7D` | `793.70` | 63,430,000.00 USD | 63,430,000.00 USD | 0.00 USD | 184,960.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `794.00` | 61,310,000.00 USD | 61,310,000.00 USD | 0.00 USD | 51,700.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `794.60` | 63,750,000.00 USD | 63,750,000.00 USD | 0.00 USD | 302,280.00 USD | 15,690.00 USD | 0.00 USD |
| `1D` | `795.20` | 61,350,000.00 USD | 61,350,000.00 USD | 0.00 USD | 44,220.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `795.50` | 63,890,000.00 USD | 63,890,000.00 USD | 0.00 USD | 109,640.00 USD | 14,650.00 USD | 14,200.00 USD |
| `1D` | `796.40` | 61,490,000.00 USD | 61,490,000.00 USD | 0.00 USD | 41,210.00 USD | 0.00 USD | 94,590.00 USD |
| `7D` | `796.40` | 64,030,000.00 USD | 64,030,000.00 USD | 0.00 USD | 139,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `797.30` | 64,090,000.00 USD | 64,090,000.00 USD | 0.00 USD | 64,670.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `797.60` | 61,570,000.00 USD | 61,570,000.00 USD | 0.00 USD | 86,930.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `798.20` | 64,250,000.00 USD | 64,250,000.00 USD | 0.00 USD | 155,890.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `798.80` | 61,640,000.00 USD | 61,640,000.00 USD | 0.00 USD | 38,270.00 USD | 26,830.00 USD | 0.00 USD |
| `7D` | `799.10` | 64,290,000.00 USD | 64,290,000.00 USD | 0.00 USD | 42,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `800.00` | 61,660,000.00 USD | 61,660,000.00 USD | 0.00 USD | 18,790.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `800.00` | 64,400,000.00 USD | 64,400,000.00 USD | 0.00 USD | 113,540.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `800.90` | 64,510,000.00 USD | 64,510,000.00 USD | 0.00 USD | 77,580.00 USD | 8,370.00 USD | 21,920.00 USD |
| `1D` | `801.20` | 61,680,000.00 USD | 61,680,000.00 USD | 0.00 USD | 20,010.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `801.80` | 64,720,000.00 USD | 64,720,000.00 USD | 0.00 USD | 179,900.00 USD | 16,330.00 USD | 10,970.00 USD |
| `1D` | `802.40` | 61,820,000.00 USD | 61,820,000.00 USD | 0.00 USD | 32,010.00 USD | 21,320.00 USD | 87,310.00 USD |
| `7D` | `802.70` | 64,730,000.00 USD | 64,730,000.00 USD | 0.00 USD | 11,220.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `803.60` | 61,910,000.00 USD | 61,910,000.00 USD | 0.00 USD | 89,870.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `803.60` | 64,760,000.00 USD | 64,760,000.00 USD | 0.00 USD | 27,360.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `804.50` | 64,840,000.00 USD | 64,840,000.00 USD | 0.00 USD | 32,340.00 USD | 18,260.00 USD | 32,980.00 USD |
| `1D` | `804.80` | 61,990,000.00 USD | 61,990,000.00 USD | 0.00 USD | 67,230.00 USD | 14,920.00 USD | 0.00 USD |
| `7D` | `805.40` | 64,910,000.00 USD | 64,910,000.00 USD | 0.00 USD | 56,700.00 USD | 8,140.00 USD | 0.00 USD |
| `1D` | `806.00` | 62,090,000.00 USD | 62,090,000.00 USD | 0.00 USD | 13,570.00 USD | 7,460.00 USD | 81,440.00 USD |
| `7D` | `806.30` | 64,920,000.00 USD | 64,920,000.00 USD | 0.00 USD | 3,270.00 USD | 12,000.00 USD | 0.00 USD |
| `1D` | `807.20` | 62,120,000.00 USD | 62,120,000.00 USD | 0.00 USD | 7,560.00 USD | 0.00 USD | 14,670.00 USD |
| `7D` | `807.20` | 64,970,000.00 USD | 64,970,000.00 USD | 0.00 USD | 39,190.00 USD | 0.00 USD | 11,830.00 USD |
| `7D` | `808.10` | 65,030,000.00 USD | 65,030,000.00 USD | 0.00 USD | 17,980.00 USD | 5,360.00 USD | 29,800.00 USD |
| `1D` | `808.40` | 62,120,000.00 USD | 62,120,000.00 USD | 0.00 USD | 7,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `809.00` | 65,110,000.00 USD | 65,110,000.00 USD | 0.00 USD | 58,620.00 USD | 13,120.00 USD | 13,000.00 USD |
| `1D` | `809.60` | 62,130,000.00 USD | 62,130,000.00 USD | 0.00 USD | 11,010.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `809.90` | 65,330,000.00 USD | 65,330,000.00 USD | 0.00 USD | 178,130.00 USD | 9,760.00 USD | 36,490.00 USD |
| `1D` | `810.80` | 62,160,000.00 USD | 62,160,000.00 USD | 0.00 USD | 5,050.00 USD | 5,000.00 USD | 19,650.00 USD |
| `7D` | `810.80` | 65,420,000.00 USD | 65,420,000.00 USD | 0.00 USD | 78,030.00 USD | 6,630.00 USD | 5,340.00 USD |
| `7D` | `811.70` | 65,480,000.00 USD | 65,480,000.00 USD | 0.00 USD | 19,210.00 USD | 12,110.00 USD | 29,380.00 USD |
| `1D` | `812.00` | 62,230,000.00 USD | 62,230,000.00 USD | 0.00 USD | 45,960.00 USD | 0.00 USD | 21,160.00 USD |
| `7D` | `812.60` | 65,600,000.00 USD | 65,600,000.00 USD | 0.00 USD | 68,390.00 USD | 17,450.00 USD | 31,430.00 USD |
| `1D` | `813.20` | 62,270,000.00 USD | 62,270,000.00 USD | 0.00 USD | 22,940.00 USD | 4,540.00 USD | 11,460.00 USD |
| `7D` | `813.50` | 65,860,000.00 USD | 65,860,000.00 USD | 0.00 USD | 147,480.00 USD | 59,640.00 USD | 45,810.00 USD |
| `1D` | `814.40` | 62,340,000.00 USD | 62,340,000.00 USD | 0.00 USD | 43,410.00 USD | 15,040.00 USD | 7,420.00 USD |
| `7D` | `814.40` | 66,180,000.00 USD | 66,180,000.00 USD | 0.00 USD | 218,130.00 USD | 32,770.00 USD | 74,730.00 USD |
| `7D` | `815.30` | 66,390,000.00 USD | 66,390,000.00 USD | 0.00 USD | 171,100.00 USD | 24,290.00 USD | 10,150.00 USD |
| `1D` | `815.60` | 62,380,000.00 USD | 62,380,000.00 USD | 0.00 USD | 17,810.00 USD | 11,670.00 USD | 13,240.00 USD |
| `7D` | `816.20` | 66,690,000.00 USD | 66,690,000.00 USD | 0.00 USD | 203,680.00 USD | 44,470.00 USD | 59,870.00 USD |
| `1D` | `816.80` | 62,450,000.00 USD | 62,450,000.00 USD | 0.00 USD | 54,370.00 USD | 17,360.00 USD | 3,620.00 USD |
| `7D` | `817.10` | 67,090,000.00 USD | 67,090,000.00 USD | 0.00 USD | 278,420.00 USD | 76,830.00 USD | 42,530.00 USD |
| `1D` | `818.00` | 62,510,000.00 USD | 62,510,000.00 USD | 0.00 USD | 43,280.00 USD | 8,150.00 USD | 6,790.00 USD |
| `7D` | `818.00` | 67,550,000.00 USD | 67,550,000.00 USD | 0.00 USD | 346,550.00 USD | 48,360.00 USD | 67,950.00 USD |
| `7D` | `818.90` | 67,790,000.00 USD | 67,790,000.00 USD | 0.00 USD | 180,470.00 USD | 8,160.00 USD | 47,880.00 USD |
| `1D` | `819.20` | 62,700,000.00 USD | 62,700,000.00 USD | 0.00 USD | 182,710.00 USD | 3,950.00 USD | 5,300.00 USD |
| `7D` | `819.80` | 68,300,000.00 USD | 68,300,000.00 USD | 0.00 USD | 295,510.00 USD | 101,950.00 USD | 107,190.00 USD |
| `1D` | `820.40` | 62,930,000.00 USD | 62,930,000.00 USD | 0.00 USD | 47,350.00 USD | 11,440.00 USD | 165,820.00 USD |
| `7D` | `820.70` | 68,600,000.00 USD | 68,600,000.00 USD | 0.00 USD | 235,990.00 USD | 41,190.00 USD | 24,080.00 USD |
| `1D` | `821.60` | 63,050,000.00 USD | 63,050,000.00 USD | 0.00 USD | 80,210.00 USD | 8,400.00 USD | 29,210.00 USD |
| `7D` | `821.60` | 68,800,000.00 USD | 68,800,000.00 USD | 0.00 USD | 86,380.00 USD | 62,620.00 USD | 55,540.00 USD |
| `7D` | `822.50` | 69,300,000.00 USD | 69,300,000.00 USD | 0.00 USD | 394,120.00 USD | 64,970.00 USD | 42,710.00 USD |
| `1D` | `822.80` | 63,620,000.00 USD | 63,620,000.00 USD | 0.00 USD | 493,840.00 USD | 46,110.00 USD | 31,300.00 USD |
| `7D` | `823.40` | 69,630,000.00 USD | 69,630,000.00 USD | 0.00 USD | 213,450.00 USD | 68,530.00 USD | 45,900.00 USD |
| `1D` | `824.00` | 63,910,000.00 USD | 63,910,000.00 USD | 0.00 USD | 225,430.00 USD | 32,630.00 USD | 30,490.00 USD |
| `7D` | `824.30` | 69,980,000.00 USD | 69,980,000.00 USD | 0.00 USD | 248,860.00 USD | 58,170.00 USD | 43,880.00 USD |
| `1D` | `825.20` | 63,980,000.00 USD | 63,980,000.00 USD | 0.00 USD | 36,860.00 USD | 26,950.00 USD | 13,300.00 USD |
| `7D` | `825.20` | 70,340,000.00 USD | 70,340,000.00 USD | 0.00 USD | 277,990.00 USD | 21,630.00 USD | 61,140.00 USD |
| `7D` | `826.10` | 70,650,000.00 USD | 70,650,000.00 USD | 0.00 USD | 223,810.00 USD | 27,390.00 USD | 53,050.00 USD |
| `1D` | `826.40` | 64,220,000.00 USD | 64,220,000.00 USD | 0.00 USD | 138,510.00 USD | 38,730.00 USD | 64,060.00 USD |
| `7D` | `827.00` | 71,290,000.00 USD | 71,290,000.00 USD | 0.00 USD | 494,310.00 USD | 23,200.00 USD | 126,570.00 USD |
| `1D` | `827.50` | 64,580,000.00 USD | 64,580,000.00 USD | 0.00 USD | 330,770.00 USD | 0.00 USD | 21,340.00 USD |
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
  * Total Open Interest: `1.37B` | Total OI Tokens: `1,934,140.5 BNB`
  * 1h OI Change: `+0.79%` | 4h OI Change: `+11.18%` | 24h OI Change: `+7.48%`
  * Exchange Breakdown: Binance=`599.50M` | Bybit=`140.79M` | OKX=`60.40M` | Hyperliquid=`91.00M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-56.89K` | Last 24h: `109.28K` | Last 3d: `307.00K` | Last 7d: `451.01K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0000%` | **USDT OKX** | `-0.0030%` |
| **USDT Bybit** | `-0.0410%` | **USDT KuCoin** | `-0.0109%` |
| **USDT MEXC** | `0.0000%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0006%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0000%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `BNB` | `42.54%` | `57.46%` | `0.74` | 227,370,000.00 USD |
| `15M` | `Binance` | `35.61%` | `64.39%` | `0.55` | 111,230,000.00 USD |
| `15M` | `OKX` | `44.71%` | `55.29%` | `0.81` | 29,480,000.00 USD |
| `15M` | `Bybit` | `38.56%` | `61.44%` | `0.63` | 17,530,000.00 USD |
| `15M` | `KuCoin` | `49.29%` | `50.71%` | `0.97` | 1,080,000.00 USD |
| `15M` | `Gate` | `49.91%` | `50.09%` | `1.00` | 8,840,000.00 USD |
| `15M` | `Bitget` | `56.24%` | `43.76%` | `1.29` | 12,230,000.00 USD |
| `15M` | `BingX` | `46.78%` | `53.22%` | `0.88` | 3,670,000.00 USD |
| `15M` | `MEXC` | `67.14%` | `32.86%` | `2.04` | 15,760,000.00 USD |
| `15M` | `Bitunix` | `34.67%` | `65.33%` | `0.53` | 6,400,000.00 USD |
| `15M` | `Hyperliquid` | `40.28%` | `59.72%` | `0.67` | 10,800,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.89%` | `50.11%` | `1.00` | 2,590,000.00 USD |
| `15M` | `Crypto.com` | `51.37%` | `48.63%` | `1.06` | 318,680.00 USD |
| `15M` | `WhiteBIT` | `84.31%` | `15.69%` | `5.37` | 667,480.00 USD |
| `15M` | `HTX` | `46.09%` | `53.91%` | `0.85` | 329,460.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `38.14%` | `61.86%` | `0.62` | 839,010.00 USD |
| `15M` | `Aster` | `75.12%` | `24.88%` | `3.02` | 3,430,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `65.19%` | `34.81%` | `1.87` | 2,190,000.00 USD |
| `15M` | `Whale Positions` | `35.61%` | `64.39%` | `0.55` | 111,230,000.00 USD |
| `15M` | `Global Accounts` | `42.54%` | `57.46%` | `0.74` | 227,370,000.00 USD |
| `1H` | `BNB` | `44.01%` | `55.99%` | `0.79` | 947,460,000.00 USD |
| `1H` | `Binance` | `39.3%` | `60.7%` | `0.65` | 415,740,000.00 USD |
| `1H` | `OKX` | `49.27%` | `50.73%` | `0.97` | 137,560,000.00 USD |
| `1H` | `Bybit` | `38.53%` | `61.47%` | `0.63` | 102,350,000.00 USD |
| `1H` | `KuCoin` | `58.09%` | `41.91%` | `1.39` | 6,890,000.00 USD |
| `1H` | `Gate` | `50.84%` | `49.16%` | `1.03` | 38,520,000.00 USD |
| `1H` | `Bitget` | `50.85%` | `49.15%` | `1.03` | 36,850,000.00 USD |
| `1H` | `BingX` | `46.65%` | `53.35%` | `0.87` | 19,000,000.00 USD |
| `1H` | `MEXC` | `53.76%` | `46.24%` | `1.16` | 58,040,000.00 USD |
| `1H` | `Bitunix` | `48.95%` | `51.05%` | `0.96` | 35,640,000.00 USD |
| `1H` | `Hyperliquid` | `42.54%` | `57.46%` | `0.74` | 51,370,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.34%` | `49.66%` | `1.01` | 11,940,000.00 USD |
| `1H` | `Crypto.com` | `47.25%` | `52.75%` | `0.90` | 1,640,000.00 USD |
| `1H` | `WhiteBIT` | `80.48%` | `19.52%` | `4.12` | 2,640,000.00 USD |
| `1H` | `HTX` | `56.62%` | `43.38%` | `1.31` | 1,450,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `46.27%` | `53.73%` | `0.86` | 6,220,000.00 USD |
| `1H` | `Aster` | `60.78%` | `39.22%` | `1.55` | 12,910,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `48.45%` | `51.55%` | `0.94` | 8,710,000.00 USD |
| `1H` | `Whale Positions` | `39.3%` | `60.7%` | `0.65` | 415,740,000.00 USD |
| `1H` | `Global Accounts` | `44.01%` | `55.99%` | `0.79` | 947,460,000.00 USD |
| `4H` | `BNB` | `48.71%` | `51.29%` | `0.95` | 2,200,000,000.00 USD |
| `4H` | `Binance` | `48.66%` | `51.34%` | `0.95` | 1,260,000,000.00 USD |
| `4H` | `OKX` | `50.53%` | `49.47%` | `1.02` | 137,610,000.00 USD |
| `4H` | `Bybit` | `48.53%` | `51.47%` | `0.94` | 254,030,000.00 USD |
| `4H` | `KuCoin` | `45.53%` | `54.47%` | `0.84` | 13,140,000.00 USD |
| `4H` | `Gate` | `49.16%` | `50.84%` | `0.97` | 52,180,000.00 USD |
| `4H` | `Bitget` | `47.15%` | `52.85%` | `0.89` | 60,480,000.00 USD |
| `4H` | `BingX` | `47.05%` | `52.95%` | `0.89` | 23,040,000.00 USD |
| `4H` | `MEXC` | `49.17%` | `50.83%` | `0.97` | 29,610,000.00 USD |
| `4H` | `Bitunix` | `48.17%` | `51.83%` | `0.93` | 52,320,000.00 USD |
| `4H` | `Hyperliquid` | `48.65%` | `51.35%` | `0.95` | 220,160,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.19%` | `49.81%` | `1.01` | 14,340,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `44.35%` | `55.65%` | `0.80` | 3,790,000.00 USD |
| `4H` | `HTX` | `38.94%` | `61.06%` | `0.64` | 3,270,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `44.27%` | `55.73%` | `0.79` | 7,080,000.00 USD |
| `4H` | `Aster` | `49.81%` | `50.19%` | `0.99` | 46,440,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `50.76%` | `49.24%` | `1.03` | 24,000,000.00 USD |
| `4H` | `Whale Positions` | `48.66%` | `51.34%` | `0.95` | 1,260,000,000.00 USD |
| `4H` | `Global Accounts` | `48.71%` | `51.29%` | `0.95` | 2,200,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `745.35` | `745.55` | `745.35` | `746.25` | `745.05` | 1,714,180.55 USD | 1,005,910.28 USD | 708,270.27 USD | 297,640.01 USD | `+17.36%` | `2B / 0S` |
| `0:00 UTC` | `739.95` | `741.09` | `739.95` | `745.65` | `737.55` | 21,388,145.47 USD | 6,350,590.17 USD | 15,037,555.30 USD | -8,686,965.13 USD | `-40.62%` | `2B / 11S` |
| `5:00 UTC` | `733.05` | `735.28` | `733.05` | `741.15` | `730.35` | 58,847,128.96 USD | 25,808,552.51 USD | 33,038,576.45 USD | -7,230,023.95 USD | `-12.29%` | `2B / 6S` |
| `0:00 UTC` | `693.15` | `709.93` | `693.15` | `733.35` | `688.35` | 287,121,588.96 USD | 130,602,079.05 USD | 156,519,509.92 USD | -25,917,430.87 USD | `-9.03%` | `0B / 21S` |
| `5:00 UTC` | `694.05` | `694.59` | `694.05` | `707.85` | `677.85` | 179,693,058.88 USD | 96,266,693.98 USD | 83,426,364.90 USD | 12,840,329.08 USD | `+7.15%` | `3B / 4S` |
| `0:00 UTC` | `705.15` | `704.71` | `705.15` | `718.65` | `690.75` | 186,631,734.60 USD | 100,794,189.14 USD | 85,837,545.46 USD | 14,956,643.67 USD | `+8.01%` | `11B / 2S` |
| `5:00 UTC` | `717.75` | `715.45` | `717.75` | `727.95` | `707.85` | 126,482,329.61 USD | 66,523,365.17 USD | 59,958,964.44 USD | 6,564,400.73 USD | `+5.19%` | `10B / 3S` |
| `0:00 UTC` | `709.95` | `710.65` | `709.95` | `715.65` | `705.45` | 34,559,429.86 USD | 16,578,658.63 USD | 17,980,771.23 USD | -1,402,112.60 USD | `-4.06%` | `2B / 2S` |
| `5:00 UTC` | `705.15` | `705.50` | `705.15` | `709.35` | `701.85` | 34,534,245.79 USD | 19,030,414.31 USD | 15,503,831.48 USD | 3,526,582.82 USD | `+10.21%` | `3B / 0S` |
| `0:00 UTC` | `707.25` | `707.27` | `707.25` | `708.75` | `705.75` | 2,842,360.63 USD | 1,059,282.70 USD | 1,783,077.93 USD | -723,795.22 USD | `-25.46%` | `0B / 2S` |

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
| `5m` | -215,510.00 USD | -4,000,000.00 USD | **`DISTRIBUTION`** |
| `15m` | 888,210.00 USD | 625,100.00 USD | **`ACCUMULATION`** |
| `30m` | 332,870.00 USD | -2,320,000.00 USD | **`DISTRIBUTION`** |
| `1h` | 268,440.00 USD | 32,000,000.00 USD | **`ACCUMULATION`** |
| `2h` | -14,610,000.00 USD | -33,690,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -16,230,000.00 USD | -40,030,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -17,250,000.00 USD | -43,420,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -15,610,000.00 USD | -38,660,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -32,960,000.00 USD | -40,930,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -11,900,000.00 USD | -70,520,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -44,140,000.00 USD | -87,740,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -142,550,000.00 USD | -414,070,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-215.51K` | 15m=`+888.21K` | 1h=`+268.44K` | 24h=`-11.90M`
* Futures Capital Netflows: 5m=`-4.00M` | 15m=`+625.10K` | 1h=`+32.00M` | 24h=`-70.52M`
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
  * `2026-10-30 03:29:54 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:53:54 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:30:54 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:30:54 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 03:29:54 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:29:54 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:31:54 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:31:54 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:54 IST`: [ForexFactory] - (Sentiment: `Neutral`)


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
  * Execution Entry: `700.56` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `688.13` (Risk Distance: `12.43` pts)
  * +2.5R Take Profit: `731.63`
  * Mathematical Lot Sizing: **`0.80 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `714.51` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `726.94` (Risk Distance: `12.43` pts)
  * +2.5R Take Profit: `683.44`
  * Mathematical Lot Sizing: **`0.80 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`708.07`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
