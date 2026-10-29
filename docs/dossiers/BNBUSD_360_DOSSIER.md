# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BNB
**Canonical Key**: `BNB` | **Broker Instrument**: `BNBUSD.p` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 02:48:52 IST` (`2026-10-29 21:18:52 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `709.40` | **Live Ask Quote**: `710.20` | **Mid Price**: `709.80`
- **Spread Points**: `80.00` | **Spread BPS**: `11.27 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `736.57` | VWAP Z-Score: `-1.39` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `9.06` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `30.73` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `795.21` | Lower -3.00σ Band: `677.93`
  * Upper +2.51σ Band: `785.64` | Lower -2.51σ Band: `687.51`
  * Upper +2.01σ Band: `775.86` | Lower -2.01σ Band: `697.28`
  * Upper +2.00σ Band: `775.67` | Lower -2.00σ Band: `697.48`
  * Upper +1.28σ Band: `761.59` | Lower -1.28σ Band: `711.55`
  * Upper +1.00σ Band: `756.12` | Lower -1.00σ Band: `717.02`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`720.80` | EMA-20=`731.56` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`739.65` (Slope: `+0.0000`) | EMA-100=`743.59`
  * Institutional Anchors: EMA-144=`744.65` | EMA-200=`744.59` (Slope: `-0.2466`) | EMA-233=`744.27`
- **Range Boundaries**: 24H High=`759.80` | 24H Low=`677.20` | Weekly High=`760.90` | Weekly Low=`677.20`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `715.61` (Distance: `-0.88%`)
  * Point of Control (POC) = `708.51` (Distance: `+0.12%`)
  * Value Area Low (VAL) = `697.59` (Distance: `+1.69%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`754.57` | POC=`744.11` | VAL=`738.60`
  * Prior Day Extremes: PDH=`759.80` | PDL=`677.20` | PDC=`696.20`
  * Monday Range Blueprint: High=`746.00` | Mid=`738.45` | Low=`730.90`
  * Developing Weekly Value Area: Weekly VAH=`750.02` | Weekly POC=`740.53` | Weekly VAL=`734.95`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`715.70` | Low=`689.70`
  * London Session (08:00-16:00 UTC): High=`712.64` | Low=`706.96`
  * New York Session (13:00-21:00 UTC): High=`714.06` | Low=`705.54`
  * Initial Balance (First Hour): IB High=`711.93` | IB Low=`707.67`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `706.96` - `712.64`
  * Optimal Trade Entry (OTE 0.705): `711.22`
  * Structural Invalidation Anchor (0.786): `715.48`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `692.06` | `718.72` | `691.05` | `713.07` | `161,653` | 113,998,871.81 USD | 21,394,376.73 USD | `+18.77%` | -30,057,032.68 USD | `+3.22` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `713.07` | `713.22` | `704.66` | `710.85` | `58,066` | 41,201,809.95 USD | -5,077,520.71 USD | `-12.32%` | -35,134,553.39 USD | `-0.64` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `710.84` | `712.01` | `707.83` | `710.10` | `3,961` | 2,813,197.26 USD | -1,498,605.21 USD | `-53.27%` | -36,633,158.61 USD | `-0.11` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `692.71` | `707.97` | `677.76` | `697.34` | `258,731` | 179,693,197.42 USD | 12,840,190.54 USD | `+7.15%` | -49,265,837.89 USD | `+2.09` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `697.33` | `718.72` | `690.87` | `710.85` | `264,856` | 186,631,734.60 USD | 14,956,643.67 USD | `+8.01%` | -34,309,194.22 USD | `+2.06` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `710.84` | `712.01` | `707.83` | `710.58` | `4,345` | 3,085,436.30 USD | -1,362,642.71 USD | `-44.16%` | -35,671,836.93 USD | `-0.07` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `744.90` | `746.16` | `743.85` | `745.33` | `9,678` | 7,209,732.85 USD | 951,958.00 USD | `+13.20%` | -20,115,888.33 USD | `+0.43` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `745.34` | `745.53` | `677.76` | `697.34` | `772,178` | 547,049,922.28 USD | -28,994,090.87 USD | `-5.30%` | -49,109,979.20 USD | `-3.64` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `697.33` | `718.72` | `690.87` | `710.95` | `265,129` | 186,825,862.51 USD | 15,070,515.86 USD | `+8.07%` | -34,039,463.34 USD | `+1.98` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `740.45` | `753.64` | `739.55` | `750.62` | `148,938` | 111,099,080.67 USD | 8,045,498.44 USD | `+7.24%` | -17,010,604.60 USD | `+1.70` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `750.62` | `754.90` | `743.07` | `745.33` | `88,414` | 66,199,547.89 USD | 232,195.88 USD | `+0.35%` | -16,778,408.72 USD | `+0.53` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `745.34` | `745.53` | `677.76` | `710.58` | `1,041,379` | 736,767,093.18 USD | -15,400,089.91 USD | `-2.09%` | -32,178,498.62 USD | `-1.32` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `747.26` | `759.90` | `745.75` | `748.51` | `156,800` | 118,182,602.62 USD | -8,240,157.99 USD | `-6.97%` | -14,715,810.54 USD | `-1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `748.51` | `753.57` | `738.70` | `740.45` | `333,019` | 248,636,999.78 USD | -10,340,292.49 USD | `-4.16%` | -25,056,103.04 USD | `-1.26` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `740.45` | `753.64` | `739.55` | `750.62` | `148,938` | 111,099,080.67 USD | 8,045,498.44 USD | `+7.24%` | -17,010,604.60 USD | `+1.70` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `750.62` | `754.90` | `743.07` | `745.33` | `88,414` | 66,199,547.89 USD | 232,195.88 USD | `+0.35%` | -16,778,408.72 USD | `+0.53` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `745.34` | `745.53` | `677.76` | `710.58` | `1,041,379` | 736,767,093.18 USD | -15,400,089.91 USD | `-2.09%` | -32,178,498.62 USD | `-1.32` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`709.80`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `708.46` | `37282000000.0000` | 26,412.81 USD | 175,919.42 USD | `1 orders` | `-0.12%` | `-` |
| `BID` | `708.47` | `13272000000.0000` | 9,402.81 USD | 149,506.61 USD | `2 orders` | `-0.12%` | `-` |
| `BID` | `708.48` | `10769000000.0000` | 7,629.62 USD | 140,103.80 USD | `1 orders` | `-0.12%` | `-` |
| `BID` | `708.49` | `3162000000.0000` | 2,240.25 USD | 132,474.18 USD | `2 orders` | `-0.12%` | `-` |
| `BID` | `708.52` | `10769000000.0000` | 7,630.05 USD | 130,233.93 USD | `1 orders` | `-0.11%` | `-` |
| `BID` | `708.53` | `1309000000.0000` | 927.47 USD | 122,603.88 USD | `1 orders` | `-0.11%` | `-` |
| `BID` | `708.61` | `22365000000.0000` | 15,848.06 USD | 121,676.42 USD | `1 orders` | `-0.10%` | `-` |
| `BID` | `708.63` | `11045000000.0000` | 7,826.82 USD | 105,828.35 USD | `2 orders` | `-0.10%` | `-` |
| `BID` | `708.64` | `319000000.0000` | 226.06 USD | 98,001.53 USD | `1 orders` | `-0.10%` | `-` |
| `BID` | `708.67` | `150000000.0000` | 106.30 USD | 97,775.48 USD | `1 orders` | `-0.09%` | `-` |
| `BID` | `708.72` | `14207000000.0000` | 10,068.79 USD | 97,669.18 USD | `1 orders` | `-0.09%` | `-` |
| `BID` | `708.73` | `7704000000.0000` | 5,460.06 USD | 87,600.39 USD | `1 orders` | `-0.09%` | `-` |
| `BID` | `708.74` | `10769000000.0000` | 7,632.42 USD | 82,140.34 USD | `1 orders` | `-0.08%` | `-` |
| `BID` | `708.85` | `8079000000.0000` | 5,726.80 USD | 74,507.92 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `708.96` | `2452000000.0000` | 1,738.37 USD | 68,781.12 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `708.97` | `14054000000.0000` | 9,963.86 USD | 67,042.75 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `709.06` | `7284000000.0000` | 5,164.79 USD | 57,078.88 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `709.07` | `33950000000.0000` | 24,072.93 USD | 51,914.09 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `709.14` | `28394000000.0000` | 20,135.32 USD | 27,841.16 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `709.17` | `10866000000.0000` | 7,705.84 USD | 7,705.84 USD | `1 orders` | `-0.02%` | `-` |
| `MID_SPREAD` | `709.34` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 709.34` | `0.00%` | `-` |
| `ASK` | `709.50` | `57000000.0000` | 40.44 USD | 40.44 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `709.59` | `2500000000.0000` | 1,773.98 USD | 1,814.42 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `709.60` | `6748000000.0000` | 4,788.38 USD | 6,602.80 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `709.63` | `319000000.0000` | 226.37 USD | 6,829.17 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `709.65` | `5501000000.0000` | 3,903.78 USD | 10,732.95 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `709.67` | `4831000000.0000` | 3,428.42 USD | 14,161.37 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `709.72` | `9748000000.0000` | 6,918.35 USD | 21,079.72 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `709.73` | `10513000000.0000` | 7,461.39 USD | 28,541.11 USD | `2 orders` | `+0.06%` | `-` |
| `ASK` | `709.76` | `7704000000.0000` | 5,467.99 USD | 34,009.10 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `709.78` | `10341000000.0000` | 7,339.83 USD | 41,348.94 USD | `2 orders` | `+0.06%` | `-` |
| `ASK` | `709.80` | `5977000000.0000` | 4,242.47 USD | 45,591.41 USD | `2 orders` | `+0.07%` | `-` |
| `ASK` | `709.81` | `2941000000.0000` | 2,087.55 USD | 47,678.96 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `709.82` | `1793000000.0000` | 1,272.71 USD | 48,951.67 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `709.84` | `10759000000.0000` | 7,637.17 USD | 56,588.84 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `709.94` | `5396000000.0000` | 3,830.84 USD | 60,419.68 USD | `1 orders` | `+0.09%` | `-` |
| `ASK` | `709.95` | `13759000000.0000` | 9,768.20 USD | 70,187.88 USD | `2 orders` | `+0.09%` | `-` |
| `ASK` | `709.96` | `3184000000.0000` | 2,260.51 USD | 72,448.39 USD | `1 orders` | `+0.09%` | `-` |
| `ASK` | `709.99` | `4187000000.0000` | 2,972.73 USD | 75,421.12 USD | `1 orders` | `+0.09%` | `-` |
| `ASK` | `710.01` | `2500000000.0000` | 1,775.03 USD | 77,196.14 USD | `1 orders` | `+0.10%` | `-` |
| `ASK` | `710.03` | `6713000000.0000` | 4,766.43 USD | 81,962.57 USD | `1 orders` | `+0.10%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:45:18 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `731` | `0xbf73...5d58` | `SHORT` | 3,114,588.15 USD | `4,350,348,000,000.00` | `711.86` | `716.37` | `2450.85` | -17,738.04 USD | `-0.57%` | `10X Cross` |
| `784` | `0xea00...a918` | `LONG` | 2,934,188.27 USD | `4,098,429,000,000.00` | `787.24` | `716.37` | `0.000000` | -292,238.51 USD | `-9.96%` | `5X Cross` |
| `857` | `0xb23b...4852` | `SHORT` | 2,655,965.09 USD | `3,703,087,000,000.00` | `702.34` | `716.37` | `3615.66` | -55,129.28 USD | `-2.08%` | `5X Cross` |
| `903` | `0xfe7c...b7ae` | `LONG` | 2,499,723.29 USD | `3,491,575,000,000.00` | `686.05` | `716.37` | `0.000000` | 104,312.43 USD | `+4.17%` | `10X Cross` |
| `1139` | `0xcac1...26b3` | `LONG` | 1,978,547.10 USD | `2,789,043,000,000.00` | `679.91` | `716.37` | `0.000000` | 82,235.94 USD | `+4.16%` | `10X Cross` |
| `1237` | `0x7737...bf66` | `SHORT` | 1,835,045.75 USD | `2,646,179,000,000.00` | `752.73` | `716.37` | `6783.26` | 156,824.83 USD | `+8.55%` | `10X Cross` |
| `1256` | `0x39b4...5c34` | `SHORT` | 1,813,737.78 USD | `2,525,007,000,000.00` | `705.75` | `716.37` | `830.50` | -31,709.58 USD | `-1.75%` | `10X Cross` |
| `1300` | `0x5b67...c66a` | `SHORT` | 1,737,031.88 USD | `2,429,891,000,000.00` | `691.70` | `716.37` | `960.03` | -56,273.45 USD | `-3.24%` | `10X Cross` |
| `1332` | `0xc675...795d` | `LONG` | 1,673,244.47 USD | `2,335,694,000,000.00` | `706.91` | `716.37` | `651.51` | 22,126.59 USD | `+1.32%` | `10X Cross` |
| `1493` | `0x2edd...8179` | `LONG` | 1,492,057.11 USD | `2,079,754,000,000.00` | `714.64` | `716.37` | `0.000000` | 5,774.18 USD | `+0.39%` | `10X Cross` |
| `1577` | `0x1809...e328` | `LONG` | 1,392,542.90 USD | `1,945,626,000,000.00` | `705.42` | `716.37` | `667.61` | 20,051.35 USD | `+1.44%` | `10X Isolated` |
| `1581` | `0x023a...2355` | `LONG` | 1,384,490.03 USD | `1,929,818,000,000.00` | `714.74` | `716.37` | `0.000000` | 5,168.74 USD | `+0.37%` | `10X Cross` |
| `1671` | `0xb69e...033a` | `LONG` | 1,286,281.55 USD | `1,795,655,000,000.00` | `772.94` | `716.37` | `619.80` | -101,650.17 USD | `-7.90%` | `10X Cross` |
| `1710` | `0x07fd...689d` | `LONG` | 1,250,657.36 USD | `1,744,292,000,000.00` | `714.81` | `716.37` | `0.000000` | 3,811.56 USD | `+0.30%` | `10X Cross` |
| `1724` | `0x645b...87b8` | `LONG` | 1,232,098.42 USD | `1,721,457,000,000.00` | `747.36` | `716.37` | `0.000000` | -54,445.35 USD | `-4.42%` | `10X Cross` |
| `1787` | `0xc926...98d3` | `SHORT` | 1,168,863.72 USD | `1,627,230,000,000.00` | `714.41` | `716.37` | `1246.71` | -6,351.39 USD | `-0.54%` | `10X Cross` |
| `1859` | `0xfc27...9d9d` | `LONG` | 1,106,286.75 USD | `1,542,035,000,000.00` | `698.79` | `716.37` | `0.000000` | 28,722.27 USD | `+2.60%` | `10X Cross` |
| `1892` | `0x14c6...b280` | `SHORT` | 1,076,250.00 USD | `1,500,000,000,000.00` | `712.51` | `716.37` | `1463.22` | -7,488.30 USD | `-0.70%` | `10X Cross` |
| `1909` | `0x456f...01ac` | `LONG` | 1,066,008.19 USD | `1,486,285,000,000.00` | `708.35` | `716.37` | `569.73` | 13,193.62 USD | `+1.24%` | `10X Cross` |
| `1918` | `0x325e...9564` | `LONG` | 1,058,206.22 USD | `1,474,708,000,000.00` | `712.02` | `716.37` | `0.000000` | 8,177.71 USD | `+0.77%` | `10X Cross` |
| `1944` | `0x5b5f...c052` | `SHORT` | 1,039,212.17 USD | `1,450,745,000,000.00` | `711.38` | `716.37` | `744.79` | -7,172.87 USD | `-0.69%` | `10X Cross` |
| `1955` | `0xa4a6...46cf` | `SHORT` | 1,029,871.20 USD | `1,433,732,000,000.00` | `718.62` | `716.37` | `2188.15` | 431.82 USD | `+0.04%` | `10X Cross` |
| `1977` | `0x7717...bd7e` | `LONG` | 1,021,267.87 USD | `1,423,231,000,000.00` | `710.75` | `716.37` | `0.000000` | 9,712.42 USD | `+0.95%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `758.72` | 157.06 USD | `-` | `NEWS_INTEL` | `-` | #BNB Liquidated Long: 0.16K USD at 758.7200 USD [API] | `2026-10-28 10:49:06` |
| `ANNOUNCEMENT` | `INFO` | `761.19` | 1,135.70 USD | `-` | `NEWS_INTEL` | `-` | #BNB Liquidated Long: 1.14K USD at 761.1900 USD [API] | `2026-10-28 11:26:33` |
| `ANNOUNCEMENT` | `INFO` | `761.19` | 12.94 USD | `-` | `NEWS_INTEL` | `-` | #BNB Liquidated Long: 0.01K USD at 761.1900 USD [API] | `2026-10-28 11:26:33` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`758.31` (Vol: 2,400,000.00 USD, Dist: `+2.47%`) | Long MP=`736.45` (Vol: 2,100,000.00 USD, Dist: `--0.48%`)
  * 48H Horizon: Short MP=`758.54` (Vol: 2,400,000.00 USD, Dist: `+2.50%`) | Long MP=`736.45` (Vol: 2,100,000.00 USD, Dist: `--0.48%`)
  * 3D Horizon: Short MP=`766.52` (Vol: 2,500,000.00 USD, Dist: `+3.58%`) | Long MP=`736.48` (Vol: 3,000,000.00 USD, Dist: `--0.48%`)
  * 7D Horizon: Short MP=`758.15` (Vol: 2,900,000.00 USD, Dist: `+2.45%`) | Long MP=`728.45` (Vol: 3,700,000.00 USD, Dist: `--1.56%`)
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
| `1D` | `Long Liquidation` | `604.30` | 30,240,000.00 USD | 30,240,000.00 USD | 53,570.00 USD | 2,300.00 USD | 15,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `604.50` | 1,610.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `605.50` | 30,170,000.00 USD | 30,170,000.00 USD | 38,430.00 USD | 2,340.00 USD | 3,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `605.50` | 4,340.00 USD | 70,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `606.70` | 30,130,000.00 USD | 30,130,000.00 USD | 20,120.00 USD | 8,630.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `607.50` | 2,690.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `607.90` | 30,080,000.00 USD | 30,080,000.00 USD | 44,630.00 USD | 4,230.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `609.10` | 30,030,000.00 USD | 30,030,000.00 USD | 23,150.00 USD | 1,920.00 USD | 1,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `610.50` | 213.67 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `613.50` | 99,140.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `614.50` | 2,280.00 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `615.10` | 30,000,000.00 USD | 30,000,000.00 USD | 0.00 USD | 0.00 USD | 295,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `615.50` | 427.16 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `616.50` | 1,320.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `617.50` | 29,710,000.00 USD | 29,710,000.00 USD | 290,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `617.50` | 156.23 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `619.50` | 600.91 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `619.90` | 29,420,000.00 USD | 29,420,000.00 USD | 0.00 USD | 33,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `620.50` | 5,410.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `621.10` | 29,380,000.00 USD | 29,380,000.00 USD | 175,630.00 USD | 35,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `621.50` | 3,230.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `622.50` | 2,110.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `623.50` | 29,170,000.00 USD | 29,170,000.00 USD | 460,160.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `623.50` | 14,580.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `624.50` | 3,460.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `624.70` | 28,710,000.00 USD | 28,710,000.00 USD | 238,630.00 USD | 31,450.00 USD | 274,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `625.50` | 29,690.00 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `625.90` | 28,170,000.00 USD | 28,170,000.00 USD | 224,870.00 USD | 44,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `626.50` | 539.42 USD | 71,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `627.10` | 27,900,000.00 USD | 27,900,000.00 USD | 186,500.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `627.50` | 326.30 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `630.50` | 153.21 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `630.70` | 27,710,000.00 USD | 27,710,000.00 USD | 0.00 USD | 0.00 USD | 254,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `631.50` | 1,130,000.00 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `631.90` | 27,460,000.00 USD | 27,460,000.00 USD | 0.00 USD | 0.00 USD | 403,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `632.50` | 125.87 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `633.10` | 27,050,000.00 USD | 27,050,000.00 USD | 461,240.00 USD | 42,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `633.50` | 1,820.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `634.50` | 1,480,000.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `635.50` | 8,680.00 USD | 234,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `636.50` | 154.67 USD | 71,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `636.70` | 26,550,000.00 USD | 26,550,000.00 USD | 101,910.00 USD | 40,910.00 USD | 236,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `637.50` | 1,110.00 USD | 225,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `638.50` | 432.90 USD | 224,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `639.10` | 26,170,000.00 USD | 26,170,000.00 USD | 184,100.00 USD | 37,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `640.30` | 25,950,000.00 USD | 25,950,000.00 USD | 0.00 USD | 0.00 USD | 184,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `640.50` | 95,270.00 USD | 223,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `641.50` | 31,030.00 USD | 128,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `642.50` | 13,340.00 USD | 97,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `642.70` | 25,760,000.00 USD | 25,760,000.00 USD | 150,090.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `643.50` | 8,490.00 USD | 84,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `645.50` | 5,050.00 USD | 75,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `646.30` | 25,610,000.00 USD | 25,610,000.00 USD | 87,020.00 USD | 0.00 USD | 140,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `646.50` | 155.81 USD | 70,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `647.50` | 25,390,000.00 USD | 25,390,000.00 USD | 227,570.00 USD | 29,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `647.50` | 143.10 USD | 71,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `648.50` | 201.68 USD | 71,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `648.70` | 25,130,000.00 USD | 25,130,000.00 USD | 101,870.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `649.50` | 136.39 USD | 70,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `650.50` | 103,150.00 USD | 175,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `651.10` | 25,030,000.00 USD | 25,030,000.00 USD | 106,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `651.50` | 633.26 USD | 70,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `652.30` | 24,920,000.00 USD | 24,920,000.00 USD | 0.00 USD | 0.00 USD | 94,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `652.50` | 281,310.00 USD | 456,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `653.50` | 24,830,000.00 USD | 24,830,000.00 USD | 0.00 USD | 26,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `653.50` | 572,750.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `654.50` | 36,890.00 USD | 69,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `655.50` | 13,670.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `655.90` | 24,800,000.00 USD | 24,800,000.00 USD | 120,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `656.50` | 14,050.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `657.10` | 24,680,000.00 USD | 24,680,000.00 USD | 5,100.00 USD | 21,320.00 USD | 825,700.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `657.50` | 18,320.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `658.30` | 23,830,000.00 USD | 23,830,000.00 USD | 799,170.00 USD | 14,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `658.50` | 3,230.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `659.50` | 23,010,000.00 USD | 23,010,000.00 USD | 64,090.00 USD | 7,460.00 USD | 81,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `659.50` | 30,770.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `660.50` | 57,190.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `660.70` | 22,860,000.00 USD | 22,860,000.00 USD | 0.00 USD | 83,170.00 USD | 14,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `661.50` | 44,730.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `661.90` | 22,760,000.00 USD | 22,760,000.00 USD | 445,210.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `662.50` | 6,630.00 USD | 32,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `663.10` | 22,320,000.00 USD | 22,320,000.00 USD | 202,560.00 USD | 92,740.00 USD | 19,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `663.50` | 112,010.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `664.10` | 87,050,000.00 USD | 87,050,000.00 USD | 78,740.00 USD | 18,740.00 USD | 39,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `664.30` | 22,000,000.00 USD | 22,000,000.00 USD | 684,100.00 USD | 48,410.00 USD | 21,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `664.50` | 18,240.00 USD | 26,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `665.00` | 86,910,000.00 USD | 86,910,000.00 USD | 92,030.00 USD | 22,990.00 USD | 37,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `665.50` | 21,250,000.00 USD | 21,250,000.00 USD | 1,180,000.00 USD | 4,540.00 USD | 11,460.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `665.50` | 41,170.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `665.90` | 86,760,000.00 USD | 86,760,000.00 USD | 264,020.00 USD | 71,380.00 USD | 63,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `666.50` | 3,810.00 USD | 7,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `666.70` | 20,050,000.00 USD | 20,050,000.00 USD | 610,130.00 USD | 102,050.00 USD | 696,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `666.80` | 86,360,000.00 USD | 86,360,000.00 USD | 198,550.00 USD | 33,320.00 USD | 61,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `667.50` | 2,600.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `667.70` | 86,070,000.00 USD | 86,070,000.00 USD | 199,690.00 USD | 45,130.00 USD | 51,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `667.90` | 18,640,000.00 USD | 18,640,000.00 USD | 187,460.00 USD | 115,700.00 USD | 9,290.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `668.50` | 237,980.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `668.60` | 85,770,000.00 USD | 85,770,000.00 USD | 387,530.00 USD | 92,860.00 USD | 51,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `669.10` | 18,330,000.00 USD | 18,330,000.00 USD | 548,420.00 USD | 82,590.00 USD | 3,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `669.50` | 85,240,000.00 USD | 85,240,000.00 USD | 341,150.00 USD | 38,130.00 USD | 108,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `669.50` | 2,570.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `670.30` | 17,690,000.00 USD | 17,690,000.00 USD | 253,490.00 USD | 3,950.00 USD | 1,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `670.40` | 84,750,000.00 USD | 84,750,000.00 USD | 319,660.00 USD | 93,800.00 USD | 77,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `670.50` | 1,580.00 USD | 4,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `671.30` | 84,260,000.00 USD | 84,260,000.00 USD | 335,750.00 USD | 57,500.00 USD | 42,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `671.50` | 15,950,000.00 USD | 15,950,000.00 USD | 1,560,000.00 USD | 18,100.00 USD | 18,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `671.50` | 151,690.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `672.20` | 83,830,000.00 USD | 83,830,000.00 USD | 180,230.00 USD | 62,620.00 USD | 74,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `672.50` | 1,380.00 USD | 2,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `672.70` | 14,350,000.00 USD | 14,350,000.00 USD | 440,210.00 USD | 21,920.00 USD | 670,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `673.10` | 83,510,000.00 USD | 83,510,000.00 USD | 394,120.00 USD | 64,970.00 USD | 42,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `673.50` | 567.76 USD | 1,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `673.90` | 13,220,000.00 USD | 13,220,000.00 USD | 471,690.00 USD | 45,440.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `674.00` | 83,010,000.00 USD | 83,010,000.00 USD | 335,670.00 USD | 105,910.00 USD | 80,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `674.50` | 259.68 USD | 638.86 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `674.90` | 82,490,000.00 USD | 82,490,000.00 USD | 247,070.00 USD | 31,490.00 USD | 44,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `675.10` | 11,650,000.00 USD | 11,650,000.00 USD | 2,020,000.00 USD | 313,780.00 USD | 27,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `675.50` | 105.38 USD | 379.18 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `675.80` | 82,160,000.00 USD | 82,160,000.00 USD | 387,400.00 USD | 26,020.00 USD | 79,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `676.30` | 9,290,000.00 USD | 9,290,000.00 USD | 140,710.00 USD | 214,200.00 USD | 85,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `676.50` | 168.45 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `676.70` | 81,670,000.00 USD | 81,670,000.00 USD | 509,100.00 USD | 35,490.00 USD | 126,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `677.50` | 8,850,000.00 USD | 8,850,000.00 USD | 531,820.00 USD | 121,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `677.60` | 81,000,000.00 USD | 81,000,000.00 USD | 409,810.00 USD | 0.00 USD | 63,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `678.50` | 80,530,000.00 USD | 80,530,000.00 USD | 120,190.00 USD | 0.00 USD | 26,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `678.70` | 8,190,000.00 USD | 8,190,000.00 USD | 1,060,000.00 USD | 111,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `679.40` | 80,380,000.00 USD | 80,380,000.00 USD | 116,510.00 USD | 10,480.00 USD | 40,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `679.90` | 7,020,000.00 USD | 7,020,000.00 USD | 1,200,000.00 USD | 169,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `680.30` | 80,210,000.00 USD | 80,210,000.00 USD | 166,780.00 USD | 13,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `681.10` | 5,650,000.00 USD | 5,650,000.00 USD | 16,450.00 USD | 99,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `681.20` | 80,030,000.00 USD | 80,030,000.00 USD | 106,280.00 USD | 7,050.00 USD | 35,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `682.10` | 79,880,000.00 USD | 79,880,000.00 USD | 0.00 USD | 23,360.00 USD | 27,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `682.30` | 5,540,000.00 USD | 5,540,000.00 USD | 36,660.00 USD | 242,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `683.00` | 79,830,000.00 USD | 79,830,000.00 USD | 175,930.00 USD | 28,470.00 USD | 11,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `683.50` | 5,260,000.00 USD | 5,260,000.00 USD | 138,150.00 USD | 127,200.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `683.90` | 79,620,000.00 USD | 79,620,000.00 USD | 77,000.00 USD | 29,510.00 USD | 17,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `684.50` | 273.80 USD | 273.80 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `684.70` | 4,990,000.00 USD | 4,990,000.00 USD | 0.00 USD | 38,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `684.80` | 79,490,000.00 USD | 79,490,000.00 USD | 246,080.00 USD | 9,850.00 USD | 39,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `685.70` | 79,200,000.00 USD | 79,200,000.00 USD | 197,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `685.90` | 4,950,000.00 USD | 4,950,000.00 USD | 694,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `686.60` | 79,000,000.00 USD | 79,000,000.00 USD | 62,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `687.50` | 78,940,000.00 USD | 78,940,000.00 USD | 148,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `688.30` | 4,260,000.00 USD | 4,260,000.00 USD | 3,940.00 USD | 0.00 USD | 2,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `688.40` | 78,790,000.00 USD | 78,790,000.00 USD | 67,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `689.30` | 78,720,000.00 USD | 78,720,000.00 USD | 84,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `689.50` | 2,240,000.00 USD | 2,240,000.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `690.20` | 78,640,000.00 USD | 78,640,000.00 USD | 283,920.00 USD | 63,230.00 USD | 82,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `690.70` | 295,360.00 USD | 295,360.00 USD | 95,780.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `691.10` | 78,210,000.00 USD | 78,210,000.00 USD | 362,020.00 USD | 61,370.00 USD | 81,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `691.90` | 199,580.00 USD | 199,580.00 USD | 33,240.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `692.00` | 77,700,000.00 USD | 77,700,000.00 USD | 322,430.00 USD | 18,850.00 USD | 58,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `692.90` | 77,300,000.00 USD | 77,300,000.00 USD | 280,830.00 USD | 19,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `693.80` | 77,000,000.00 USD | 77,000,000.00 USD | 305,720.00 USD | 39,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `694.70` | 76,660,000.00 USD | 76,660,000.00 USD | 279,840.00 USD | 36,640.00 USD | 35,490.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `695.50` | 302.54 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `695.60` | 76,300,000.00 USD | 76,300,000.00 USD | 120,440.00 USD | 0.00 USD | 21,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `696.50` | 76,160,000.00 USD | 76,160,000.00 USD | 140,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `697.40` | 76,020,000.00 USD | 76,020,000.00 USD | 189,100.00 USD | 19,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `698.30` | 75,810,000.00 USD | 75,810,000.00 USD | 273,520.00 USD | 33,120.00 USD | 54,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `699.20` | 75,450,000.00 USD | 75,450,000.00 USD | 274,810.00 USD | 12,670.00 USD | 11,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `700.10` | 75,150,000.00 USD | 75,150,000.00 USD | 225,450.00 USD | 40,820.00 USD | 27,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `701.00` | 74,860,000.00 USD | 74,860,000.00 USD | 237,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `701.90` | 74,620,000.00 USD | 74,620,000.00 USD | 135,260.00 USD | 41,260.00 USD | 89,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `702.70` | 166,340.00 USD | 166,340.00 USD | 0.00 USD | 166,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `702.80` | 74,360,000.00 USD | 74,360,000.00 USD | 416,820.00 USD | 57,470.00 USD | 36,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `703.70` | 73,840,000.00 USD | 73,840,000.00 USD | 311,800.00 USD | 44,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `703.90` | 175,470.00 USD | 175,470.00 USD | 0.00 USD | 175,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `704.60` | 73,490,000.00 USD | 73,490,000.00 USD | 537,050.00 USD | 136,550.00 USD | 194,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `705.10` | 272,300.00 USD | 272,300.00 USD | 0.00 USD | 96,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `705.50` | 72,620,000.00 USD | 72,620,000.00 USD | 920,340.00 USD | 162,820.00 USD | 236,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `705.50` | 6,470.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `706.40` | 71,300,000.00 USD | 71,300,000.00 USD | 523,540.00 USD | 104,380.00 USD | 231,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `706.50` | 98,910.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `707.30` | 70,440,000.00 USD | 70,440,000.00 USD | 604,060.00 USD | 90,200.00 USD | 53,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `707.50` | 429,570.00 USD | 429,570.00 USD | 0.00 USD | 157,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `707.50` | 4,830.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `708.20` | 69,690,000.00 USD | 69,690,000.00 USD | 796,640.00 USD | 138,200.00 USD | 42,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `709.10` | 68,710,000.00 USD | 68,710,000.00 USD | 392,150.00 USD | 156,040.00 USD | 195,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `709.50` | 1,420.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `709.90` | 654,380.00 USD | 654,380.00 USD | 0.00 USD | 224,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `710.00` | 67,970,000.00 USD | 67,970,000.00 USD | 450,480.00 USD | 167,090.00 USD | 176,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `710.50` | 153.47 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `710.90` | 67,180,000.00 USD | 67,180,000.00 USD | 922,450.00 USD | 160,040.00 USD | 236,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `711.10` | 768,540.00 USD | 768,540.00 USD | 0.00 USD | 114,160.00 USD | 0.00 USD | `Tier 1 CEX` |
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
| `1D` | `Short Liquidation` | `715.90` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 83,170.00 USD | 2,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `716.30` | 57,600,000.00 USD | 57,600,000.00 USD | 1,080,000.00 USD | 324,540.00 USD | 233,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `717.10` | 4,990,000.00 USD | 4,990,000.00 USD | 1,910,000.00 USD | 214,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `717.20` | 55,960,000.00 USD | 55,960,000.00 USD | 581,610.00 USD | 398,030.00 USD | 387,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `717.50` | 6,650.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `718.10` | 54,590,000.00 USD | 54,590,000.00 USD | 1,690,000.00 USD | 246,320.00 USD | 151,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `718.30` | 5,080,000.00 USD | 5,080,000.00 USD | 0.00 USD | 87,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `718.50` | 158.79 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `719.00` | 52,510,000.00 USD | 52,510,000.00 USD | 670,390.00 USD | 137,460.00 USD | 211,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `719.50` | 5,120,000.00 USD | 5,120,000.00 USD | 0.00 USD | 48,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `719.50` | 705.11 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `719.90` | 51,490,000.00 USD | 51,490,000.00 USD | 618,020.00 USD | 173,240.00 USD | 186,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `720.50` | 64,940.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `720.70` | 6,480,000.00 USD | 6,480,000.00 USD | 1,150,000.00 USD | 204,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `720.80` | 50,510,000.00 USD | 50,510,000.00 USD | 1,010,000.00 USD | 52,490.00 USD | 180,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `721.50` | 160,460.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `721.70` | 49,260,000.00 USD | 49,260,000.00 USD | 1,950,000.00 USD | 237,690.00 USD | 653,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `721.90` | 9,530,000.00 USD | 9,530,000.00 USD | 1,110,000.00 USD | 78,640.00 USD | 1,870,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `722.50` | 3,740.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `722.60` | 46,430,000.00 USD | 46,430,000.00 USD | 1,930,000.00 USD | 108,200.00 USD | 229,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `723.10` | 10,210,000.00 USD | 10,210,000.00 USD | 562,170.00 USD | 112,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `723.50` | 44,160,000.00 USD | 44,160,000.00 USD | 640,550.00 USD | 140,550.00 USD | 293,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `723.50` | 111,640.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `724.30` | 11,590,000.00 USD | 11,590,000.00 USD | 1,200,000.00 USD | 188,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `724.40` | 43,080,000.00 USD | 43,080,000.00 USD | 663,550.00 USD | 186,780.00 USD | 130,770.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `724.50` | 112,820.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `725.30` | 42,100,000.00 USD | 42,100,000.00 USD | 1,760,000.00 USD | 418,390.00 USD | 396,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `725.50` | 12,570,000.00 USD | 12,570,000.00 USD | 0.00 USD | 57,080.00 USD | 923,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `725.50` | 42.80 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `726.20` | 39,520,000.00 USD | 39,520,000.00 USD | 1,060,000.00 USD | 311,550.00 USD | 460,020.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `726.50` | 56,650.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `726.70` | 12,630,000.00 USD | 12,630,000.00 USD | 0.00 USD | 64,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `727.10` | 37,690,000.00 USD | 37,690,000.00 USD | 1,230,000.00 USD | 331,980.00 USD | 241,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `727.50` | 6,020.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `727.90` | 13,560,000.00 USD | 13,560,000.00 USD | 924,740.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `728.00` | 35,890,000.00 USD | 35,890,000.00 USD | 3,110,000.00 USD | 778,750.00 USD | 388,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `728.50` | 140,520.00 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `728.90` | 31,610,000.00 USD | 31,610,000.00 USD | 2,330,000.00 USD | 317,590.00 USD | 644,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `729.10` | 14,200,000.00 USD | 14,200,000.00 USD | 0.00 USD | 0.00 USD | 636,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `729.50` | 13,400.00 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `729.80` | 28,320,000.00 USD | 28,320,000.00 USD | 1,320,000.00 USD | 430,010.00 USD | 339,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `730.30` | 15,310,000.00 USD | 15,310,000.00 USD | 0.00 USD | 107,360.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `730.50` | 842.27 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `730.70` | 26,230,000.00 USD | 26,230,000.00 USD | 2,760,000.00 USD | 351,520.00 USD | 587,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `731.50` | 16,330,000.00 USD | 16,330,000.00 USD | 952,750.00 USD | 63,350.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `731.50` | 38,660.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `731.60` | 22,530,000.00 USD | 22,530,000.00 USD | 1,530,000.00 USD | 133,980.00 USD | 261,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `732.50` | 20,610,000.00 USD | 20,610,000.00 USD | 465,880.00 USD | 221,510.00 USD | 96,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `732.50` | 29,020.00 USD | 2,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `732.70` | 18,030,000.00 USD | 18,030,000.00 USD | 998,900.00 USD | 0.00 USD | 703,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `733.40` | 19,820,000.00 USD | 19,820,000.00 USD | 1,910,000.00 USD | 158,310.00 USD | 338,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `733.50` | 207,280.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `733.90` | 18,580,000.00 USD | 18,580,000.00 USD | 344,230.00 USD | 206,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `734.30` | 17,420,000.00 USD | 17,420,000.00 USD | 1,580,000.00 USD | 288,470.00 USD | 244,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `734.50` | 161,950.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `735.10` | 19,440,000.00 USD | 19,440,000.00 USD | 613,800.00 USD | 241,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `735.20` | 15,310,000.00 USD | 15,310,000.00 USD | 1,330,000.00 USD | 172,940.00 USD | 437,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `735.50` | 339.80 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `736.10` | 13,370,000.00 USD | 13,370,000.00 USD | 2,130,000.00 USD | 181,990.00 USD | 484,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `736.30` | 21,330,000.00 USD | 21,330,000.00 USD | 1,270,000.00 USD | 27,530.00 USD | 590,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `736.50` | 90,550.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `737.00` | 10,570,000.00 USD | 10,570,000.00 USD | 2,360,000.00 USD | 175,330.00 USD | 633,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `737.50` | 21,610,000.00 USD | 21,610,000.00 USD | 186,520.00 USD | 94,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `737.50` | 530,510.00 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `737.90` | 7,400,000.00 USD | 7,400,000.00 USD | 3,420,000.00 USD | 72,280.00 USD | 374,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `738.50` | 77,910.00 USD | 3,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `738.70` | 22,740,000.00 USD | 22,740,000.00 USD | 658,340.00 USD | 0.00 USD | 472,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `738.80` | 3,530,000.00 USD | 3,530,000.00 USD | 522,950.00 USD | 20,210.00 USD | 155,300.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `739.50` | 29,980.00 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `739.70` | 2,830,000.00 USD | 2,830,000.00 USD | 352,500.00 USD | 0.00 USD | 203,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `739.90` | 23,730,000.00 USD | 23,730,000.00 USD | 518,470.00 USD | 0.00 USD | 476,790.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `740.50` | 537,670.00 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `740.60` | 2,280,000.00 USD | 2,280,000.00 USD | 1,090,000.00 USD | 0.00 USD | 33,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `741.10` | 24,510,000.00 USD | 24,510,000.00 USD | 603,910.00 USD | 166,390.00 USD | 7,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `741.50` | 1,160,000.00 USD | 1,160,000.00 USD | 257,630.00 USD | 0.00 USD | 208,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `741.50` | 1,500.00 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `742.30` | 24,800,000.00 USD | 24,800,000.00 USD | 291,160.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `742.40` | 689,850.00 USD | 689,850.00 USD | 0.00 USD | 0.00 USD | 183,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `742.50` | 1,800.00 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `743.30` | 505,930.00 USD | 505,930.00 USD | 0.00 USD | 0.00 USD | 57,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `743.50` | 25,240,000.00 USD | 25,240,000.00 USD | 0.00 USD | 0.00 USD | 436,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `743.50` | 526,730.00 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `744.20` | 448,350.00 USD | 448,350.00 USD | 0.00 USD | 257,580.00 USD | 141,790.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `744.50` | 29,480.00 USD | 4,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `744.70` | 25,450,000.00 USD | 25,450,000.00 USD | 106,810.00 USD | 106,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `745.10` | 48,980.00 USD | 48,980.00 USD | 0.00 USD | 48,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `745.50` | 456.25 USD | 4,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `745.90` | 26,040,000.00 USD | 26,040,000.00 USD | 482,060.00 USD | 106,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `746.00` | 999,320.00 USD | 999,320.00 USD | 999,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `746.50` | 11,580.00 USD | 4,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `746.90` | 1,210,000.00 USD | 1,210,000.00 USD | 215,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `747.10` | 27,620,000.00 USD | 27,620,000.00 USD | 748,640.00 USD | 67,980.00 USD | 758,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `747.50` | 47,340.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `748.30` | 28,050,000.00 USD | 28,050,000.00 USD | 286,680.00 USD | 72,690.00 USD | 73,330.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `748.50` | 213,670.00 USD | 5,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `749.50` | 28,470,000.00 USD | 28,470,000.00 USD | 417,840.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `749.50` | 5,040.00 USD | 5,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `750.50` | 88,430.00 USD | 5,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `751.90` | 28,920,000.00 USD | 28,920,000.00 USD | 0.00 USD | 25,010.00 USD | 433,820.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `752.50` | 646,750.00 USD | 5,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `753.10` | 29,510,000.00 USD | 29,510,000.00 USD | 229,820.00 USD | 0.00 USD | 354,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `753.50` | 768.57 USD | 5,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `754.30` | 30,020,000.00 USD | 30,020,000.00 USD | 383,510.00 USD | 74,660.00 USD | 57,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `754.50` | 3,280.00 USD | 5,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `755.00` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 59,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `755.50` | 30,630,000.00 USD | 30,630,000.00 USD | 293,610.00 USD | 254,460.00 USD | 56,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `755.50` | 1,990.00 USD | 5,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `756.70` | 31,140,000.00 USD | 31,140,000.00 USD | 390,390.00 USD | 24,970.00 USD | 95,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `756.80` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 47,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `757.50` | 859,510.00 USD | 6,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `757.70` | 1,910,000.00 USD | 1,910,000.00 USD | 475,510.00 USD | 113,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `757.90` | 31,880,000.00 USD | 31,880,000.00 USD | 515,360.00 USD | 189,940.00 USD | 32,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `758.60` | 3,100,000.00 USD | 3,100,000.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `759.10` | 33,490,000.00 USD | 33,490,000.00 USD | 1,220,000.00 USD | 122,880.00 USD | 273,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `760.30` | 34,160,000.00 USD | 34,160,000.00 USD | 508,710.00 USD | 100,270.00 USD | 61,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `760.40` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 27,650.00 USD | 42,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `760.50` | 2,360.00 USD | 6,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `761.30` | 3,490,000.00 USD | 3,490,000.00 USD | 10,750.00 USD | 211,960.00 USD | 100,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `761.50` | 35,480,000.00 USD | 35,480,000.00 USD | 929,820.00 USD | 77,330.00 USD | 308,810.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `761.50` | 131.74 USD | 6,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `762.20` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 699,820.00 USD | 179,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `762.50` | 269.93 USD | 6,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `762.70` | 37,790,000.00 USD | 37,790,000.00 USD | 1,450,000.00 USD | 234,890.00 USD | 624,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `763.10` | 7,830,000.00 USD | 7,830,000.00 USD | 2,460,000.00 USD | 590,460.00 USD | 404,720.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `763.50` | 435,970.00 USD | 7,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `763.90` | 40,740,000.00 USD | 40,740,000.00 USD | 2,350,000.00 USD | 269,760.00 USD | 335,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `764.00` | 10,270,000.00 USD | 10,270,000.00 USD | 1,590,000.00 USD | 441,980.00 USD | 402,300.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `764.50` | 949,210.00 USD | 8,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `764.90` | 12,470,000.00 USD | 12,470,000.00 USD | 1,450,000.00 USD | 352,570.00 USD | 395,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `765.10` | 42,630,000.00 USD | 42,630,000.00 USD | 1,380,000.00 USD | 280,250.00 USD | 231,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `765.50` | 9,770.00 USD | 8,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `765.80` | 15,460,000.00 USD | 15,460,000.00 USD | 2,470,000.00 USD | 107,550.00 USD | 416,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `766.30` | 44,610,000.00 USD | 44,610,000.00 USD | 1,240,000.00 USD | 267,070.00 USD | 475,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `766.50` | 820.92 USD | 8,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `766.70` | 20,050,000.00 USD | 20,050,000.00 USD | 3,330,000.00 USD | 416,530.00 USD | 842,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `767.50` | 47,730,000.00 USD | 47,730,000.00 USD | 2,570,000.00 USD | 120,630.00 USD | 424,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `767.60` | 23,430,000.00 USD | 23,430,000.00 USD | 2,790,000.00 USD | 123,530.00 USD | 467,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `768.50` | 25,660,000.00 USD | 25,660,000.00 USD | 1,840,000.00 USD | 95,830.00 USD | 281,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `768.50` | 35,070.00 USD | 8,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `768.70` | 49,550,000.00 USD | 49,550,000.00 USD | 1,540,000.00 USD | 117,770.00 USD | 164,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `769.40` | 26,810,000.00 USD | 26,810,000.00 USD | 565,780.00 USD | 249,950.00 USD | 333,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `769.90` | 50,410,000.00 USD | 50,410,000.00 USD | 591,420.00 USD | 166,630.00 USD | 96,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `770.30` | 29,310,000.00 USD | 29,310,000.00 USD | 1,900,000.00 USD | 240,530.00 USD | 364,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `770.50` | 500.05 USD | 8,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `771.10` | 51,520,000.00 USD | 51,520,000.00 USD | 682,120.00 USD | 76,340.00 USD | 355,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `771.20` | 30,770,000.00 USD | 30,770,000.00 USD | 1,050,000.00 USD | 242,570.00 USD | 162,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `771.50` | 14,940.00 USD | 8,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `772.10` | 33,190,000.00 USD | 33,190,000.00 USD | 1,750,000.00 USD | 252,650.00 USD | 419,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `772.30` | 52,950,000.00 USD | 52,950,000.00 USD | 773,930.00 USD | 160,720.00 USD | 492,830.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `772.50` | 21,470.00 USD | 8,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `773.00` | 35,800,000.00 USD | 35,800,000.00 USD | 1,950,000.00 USD | 325,680.00 USD | 338,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `773.50` | 54,360,000.00 USD | 54,360,000.00 USD | 946,610.00 USD | 185,610.00 USD | 281,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `773.50` | 11,500.00 USD | 8,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `773.90` | 37,600,000.00 USD | 37,600,000.00 USD | 1,220,000.00 USD | 276,760.00 USD | 293,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `774.50` | 464,830.00 USD | 8,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `774.70` | 55,830,000.00 USD | 55,830,000.00 USD | 1,310,000.00 USD | 88,980.00 USD | 65,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `774.80` | 39,980,000.00 USD | 39,980,000.00 USD | 1,310,000.00 USD | 568,930.00 USD | 502,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `775.50` | 85,620.00 USD | 8,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `775.70` | 42,470,000.00 USD | 42,470,000.00 USD | 1,830,000.00 USD | 470,960.00 USD | 187,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `775.90` | 56,540,000.00 USD | 56,540,000.00 USD | 470,290.00 USD | 153,780.00 USD | 84,640.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `776.50` | 2,230.00 USD | 8,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `776.60` | 44,740,000.00 USD | 44,740,000.00 USD | 1,630,000.00 USD | 269,050.00 USD | 378,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `777.10` | 57,140,000.00 USD | 57,140,000.00 USD | 429,240.00 USD | 58,250.00 USD | 110,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `777.50` | 46,480,000.00 USD | 46,480,000.00 USD | 1,350,000.00 USD | 243,990.00 USD | 148,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `777.50` | 209.15 USD | 8,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `778.30` | 59,060,000.00 USD | 59,060,000.00 USD | 1,370,000.00 USD | 175,590.00 USD | 376,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `778.40` | 48,170,000.00 USD | 48,170,000.00 USD | 1,180,000.00 USD | 307,370.00 USD | 206,530.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `778.50` | 207,580.00 USD | 8,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `779.30` | 49,730,000.00 USD | 49,730,000.00 USD | 1,240,000.00 USD | 188,170.00 USD | 123,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `779.50` | 60,260,000.00 USD | 60,260,000.00 USD | 936,610.00 USD | 105,030.00 USD | 160,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `780.20` | 51,100,000.00 USD | 51,100,000.00 USD | 1,070,000.00 USD | 86,470.00 USD | 218,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `780.70` | 61,080,000.00 USD | 61,080,000.00 USD | 585,300.00 USD | 124,740.00 USD | 108,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `781.10` | 52,710,000.00 USD | 52,710,000.00 USD | 1,270,000.00 USD | 90,990.00 USD | 242,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `781.50` | 1,430.00 USD | 8,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `781.90` | 62,660,000.00 USD | 62,660,000.00 USD | 1,100,000.00 USD | 109,060.00 USD | 382,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `782.00` | 54,610,000.00 USD | 54,610,000.00 USD | 1,510,000.00 USD | 87,670.00 USD | 301,190.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `782.50` | 240,380.00 USD | 9,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `782.90` | 56,600,000.00 USD | 56,600,000.00 USD | 1,750,000.00 USD | 36,140.00 USD | 202,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `783.10` | 64,010,000.00 USD | 64,010,000.00 USD | 1,090,000.00 USD | 80,140.00 USD | 176,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `783.50` | 52,930.00 USD | 9,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `783.80` | 57,170,000.00 USD | 57,170,000.00 USD | 508,000.00 USD | 10,100.00 USD | 54,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `784.30` | 64,560,000.00 USD | 64,560,000.00 USD | 494,760.00 USD | 28,920.00 USD | 29,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `784.50` | 13,210.00 USD | 9,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `784.70` | 57,480,000.00 USD | 57,480,000.00 USD | 208,380.00 USD | 28,260.00 USD | 70,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `785.50` | 65,110,000.00 USD | 65,110,000.00 USD | 482,590.00 USD | 37,320.00 USD | 27,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `785.60` | 58,610,000.00 USD | 58,610,000.00 USD | 1,010,000.00 USD | 54,140.00 USD | 71,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `786.50` | 59,000,000.00 USD | 59,000,000.00 USD | 329,230.00 USD | 30,660.00 USD | 23,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `786.50` | 11,280.00 USD | 9,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `786.70` | 65,420,000.00 USD | 65,420,000.00 USD | 240,650.00 USD | 29,920.00 USD | 40,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `787.40` | 59,580,000.00 USD | 59,580,000.00 USD | 470,050.00 USD | 17,630.00 USD | 91,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `787.50` | 124,850.00 USD | 9,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `787.90` | 65,820,000.00 USD | 65,820,000.00 USD | 285,740.00 USD | 42,520.00 USD | 75,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `788.30` | 59,940,000.00 USD | 59,940,000.00 USD | 202,630.00 USD | 82,380.00 USD | 81,230.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `788.50` | 73,300.00 USD | 9,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `789.10` | 66,400,000.00 USD | 66,400,000.00 USD | 443,990.00 USD | 62,290.00 USD | 69,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `789.20` | 60,780,000.00 USD | 60,780,000.00 USD | 698,830.00 USD | 81,250.00 USD | 55,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `789.50` | 43,710.00 USD | 9,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `790.10` | 61,270,000.00 USD | 61,270,000.00 USD | 299,250.00 USD | 104,360.00 USD | 88,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `790.30` | 67,060,000.00 USD | 67,060,000.00 USD | 459,640.00 USD | 40,140.00 USD | 163,110.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `790.50` | 939.90 USD | 9,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `791.00` | 62,150,000.00 USD | 62,150,000.00 USD | 693,290.00 USD | 82,870.00 USD | 100,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `791.50` | 67,490,000.00 USD | 67,490,000.00 USD | 357,910.00 USD | 61,910.00 USD | 8,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `791.90` | 63,030,000.00 USD | 63,030,000.00 USD | 816,380.00 USD | 16,830.00 USD | 46,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `792.70` | 67,690,000.00 USD | 67,690,000.00 USD | 203,200.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `792.80` | 63,250,000.00 USD | 63,250,000.00 USD | 205,450.00 USD | 0.00 USD | 14,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `793.70` | 63,430,000.00 USD | 63,430,000.00 USD | 184,960.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `793.90` | 67,740,000.00 USD | 67,740,000.00 USD | 47,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `794.50` | 73,100.00 USD | 9,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `794.60` | 63,750,000.00 USD | 63,750,000.00 USD | 302,280.00 USD | 15,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `795.10` | 67,790,000.00 USD | 67,790,000.00 USD | 44,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `795.50` | 63,890,000.00 USD | 63,890,000.00 USD | 109,640.00 USD | 14,650.00 USD | 14,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `795.50` | 60,100.00 USD | 9,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `796.30` | 67,840,000.00 USD | 67,840,000.00 USD | 50,250.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `796.40` | 64,030,000.00 USD | 64,030,000.00 USD | 139,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `796.50` | 172.84 USD | 9,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `797.30` | 64,090,000.00 USD | 64,090,000.00 USD | 64,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `797.50` | 68,010,000.00 USD | 68,010,000.00 USD | 78,300.00 USD | 0.00 USD | 94,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `797.50` | 24,140.00 USD | 9,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `798.20` | 64,250,000.00 USD | 64,250,000.00 USD | 155,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `798.50` | 35,530.00 USD | 9,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `798.70` | 68,080,000.00 USD | 68,080,000.00 USD | 46,910.00 USD | 26,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `799.10` | 64,290,000.00 USD | 64,290,000.00 USD | 42,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `799.50` | 8,100.00 USD | 9,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `799.90` | 68,100,000.00 USD | 68,100,000.00 USD | 18,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `800.00` | 64,400,000.00 USD | 64,400,000.00 USD | 113,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `800.90` | 64,510,000.00 USD | 64,510,000.00 USD | 77,580.00 USD | 8,370.00 USD | 21,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `801.10` | 68,120,000.00 USD | 68,120,000.00 USD | 20,010.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `801.80` | 64,720,000.00 USD | 64,720,000.00 USD | 179,900.00 USD | 16,330.00 USD | 10,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `802.30` | 68,260,000.00 USD | 68,260,000.00 USD | 32,010.00 USD | 21,320.00 USD | 87,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `802.50` | 279.27 USD | 9,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `802.70` | 64,730,000.00 USD | 64,730,000.00 USD | 11,220.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `803.50` | 68,350,000.00 USD | 68,350,000.00 USD | 89,870.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `803.60` | 64,760,000.00 USD | 64,760,000.00 USD | 27,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `804.50` | 64,840,000.00 USD | 64,840,000.00 USD | 32,340.00 USD | 18,260.00 USD | 32,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `804.50` | 142,720.00 USD | 9,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `804.70` | 68,430,000.00 USD | 68,430,000.00 USD | 67,230.00 USD | 14,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `805.40` | 64,910,000.00 USD | 64,910,000.00 USD | 56,700.00 USD | 8,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `805.50` | 17,140.00 USD | 9,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `805.90` | 68,540,000.00 USD | 68,540,000.00 USD | 12,090.00 USD | 7,460.00 USD | 81,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `806.30` | 64,920,000.00 USD | 64,920,000.00 USD | 3,270.00 USD | 12,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `806.50` | 45,660.00 USD | 9,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `807.10` | 68,560,000.00 USD | 68,560,000.00 USD | 11,450.00 USD | 0.00 USD | 14,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `807.20` | 64,970,000.00 USD | 64,970,000.00 USD | 39,190.00 USD | 0.00 USD | 11,830.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `807.50` | 73,430.00 USD | 10,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `808.10` | 65,030,000.00 USD | 65,030,000.00 USD | 17,980.00 USD | 5,360.00 USD | 29,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `808.30` | 68,570,000.00 USD | 68,570,000.00 USD | 6,570.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `808.50` | 738.97 USD | 10,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `809.00` | 65,110,000.00 USD | 65,110,000.00 USD | 58,620.00 USD | 13,120.00 USD | 13,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `809.50` | 68,580,000.00 USD | 68,580,000.00 USD | 13,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `809.50` | 172,010.00 USD | 10,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `809.90` | 65,330,000.00 USD | 65,330,000.00 USD | 178,130.00 USD | 9,760.00 USD | 36,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `810.70` | 68,610,000.00 USD | 68,610,000.00 USD | 5,050.00 USD | 5,000.00 USD | 19,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `810.80` | 65,420,000.00 USD | 65,420,000.00 USD | 78,030.00 USD | 6,630.00 USD | 5,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `811.70` | 65,480,000.00 USD | 65,480,000.00 USD | 19,210.00 USD | 12,110.00 USD | 29,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `811.90` | 68,680,000.00 USD | 68,680,000.00 USD | 45,960.00 USD | 0.00 USD | 21,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `812.60` | 65,600,000.00 USD | 65,600,000.00 USD | 68,390.00 USD | 17,450.00 USD | 31,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `813.10` | 68,710,000.00 USD | 68,710,000.00 USD | 19,990.00 USD | 4,540.00 USD | 11,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `813.50` | 65,860,000.00 USD | 65,860,000.00 USD | 147,480.00 USD | 59,640.00 USD | 45,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `814.30` | 68,760,000.00 USD | 68,760,000.00 USD | 25,260.00 USD | 15,040.00 USD | 7,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `814.40` | 66,180,000.00 USD | 66,180,000.00 USD | 218,130.00 USD | 32,770.00 USD | 74,730.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `814.50` | 862.56 USD | 10,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `815.30` | 66,390,000.00 USD | 66,390,000.00 USD | 171,100.00 USD | 24,290.00 USD | 10,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `815.50` | 68,830,000.00 USD | 68,830,000.00 USD | 38,910.00 USD | 11,670.00 USD | 13,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `816.20` | 66,690,000.00 USD | 66,690,000.00 USD | 203,680.00 USD | 44,470.00 USD | 59,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `816.70` | 68,900,000.00 USD | 68,900,000.00 USD | 54,370.00 USD | 13,980.00 USD | 3,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `817.10` | 67,090,000.00 USD | 67,090,000.00 USD | 278,420.00 USD | 76,830.00 USD | 42,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `817.90` | 68,950,000.00 USD | 68,950,000.00 USD | 43,280.00 USD | 11,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `818.00` | 67,550,000.00 USD | 67,550,000.00 USD | 346,550.00 USD | 48,360.00 USD | 67,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `818.50` | 205.44 USD | 10,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `818.90` | 67,790,000.00 USD | 67,790,000.00 USD | 180,470.00 USD | 8,160.00 USD | 47,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `819.10` | 69,150,000.00 USD | 69,150,000.00 USD | 182,710.00 USD | 3,950.00 USD | 12,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `819.50` | 5,990.00 USD | 10,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `819.80` | 68,300,000.00 USD | 68,300,000.00 USD | 295,510.00 USD | 101,950.00 USD | 107,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `820.30` | 69,370,000.00 USD | 69,370,000.00 USD | 46,010.00 USD | 11,440.00 USD | 159,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `820.50` | 3,550.00 USD | 10,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `820.70` | 68,600,000.00 USD | 68,600,000.00 USD | 235,990.00 USD | 41,190.00 USD | 24,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `821.50` | 69,490,000.00 USD | 69,490,000.00 USD | 81,550.00 USD | 8,400.00 USD | 33,660.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `821.50` | 11,840.00 USD | 10,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `821.60` | 68,800,000.00 USD | 68,800,000.00 USD | 86,380.00 USD | 62,620.00 USD | 55,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `822.50` | 69,300,000.00 USD | 69,300,000.00 USD | 394,120.00 USD | 64,970.00 USD | 42,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `822.50` | 57,150.00 USD | 10,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `822.70` | 70,060,000.00 USD | 70,060,000.00 USD | 493,840.00 USD | 41,790.00 USD | 31,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `823.40` | 69,630,000.00 USD | 69,630,000.00 USD | 213,450.00 USD | 68,530.00 USD | 45,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `823.50` | 1,770.00 USD | 10,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `823.90` | 70,290,000.00 USD | 70,290,000.00 USD | 173,720.00 USD | 36,950.00 USD | 17,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `824.30` | 69,980,000.00 USD | 69,980,000.00 USD | 248,860.00 USD | 58,170.00 USD | 43,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `825.10` | 70,430,000.00 USD | 70,430,000.00 USD | 86,360.00 USD | 26,950.00 USD | 27,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `825.20` | 70,340,000.00 USD | 70,340,000.00 USD | 277,990.00 USD | 21,630.00 USD | 61,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `825.50` | 58,040.00 USD | 10,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `826.10` | 70,650,000.00 USD | 70,650,000.00 USD | 223,810.00 USD | 27,390.00 USD | 53,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `826.30` | 70,650,000.00 USD | 70,650,000.00 USD | 137,210.00 USD | 35,550.00 USD | 52,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `826.50` | 301.67 USD | 10,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `827.00` | 71,290,000.00 USD | 71,290,000.00 USD | 494,310.00 USD | 23,200.00 USD | 126,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `827.50` | 71,080,000.00 USD | 71,080,000.00 USD | 342,740.00 USD | 17,720.00 USD | 65,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `827.90` | 71,650,000.00 USD | 71,650,000.00 USD | 297,880.00 USD | 0.00 USD | 63,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `828.30` | 71,220,000.00 USD | 71,220,000.00 USD | 140,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
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
| `Live` | `Long` | `142.50` | 5,570,000.00 USD | 0.00 USD | 5,550.00 USD | `-79.50%` | `38,980,000,000.00` |
| `Live` | `Long` | `145.50` | 5,570,000.00 USD | 0.00 USD | 2,680.00 USD | `-79.07%` | `18,405,000,000.00` |
| `Live` | `Long` | `151.50` | 5,570,000.00 USD | 0.00 USD | 2,120.00 USD | `-78.21%` | `14,000,000,000.00` |
| `Live` | `Long` | `153.50` | 5,560,000.00 USD | 0.00 USD | 1,890.00 USD | `-77.92%` | `12,312,000,000.00` |
| `Live` | `Long` | `154.50` | 5,560,000.00 USD | 0.00 USD | 439.86 USD | `-77.77%` | `2,847,000,000.00` |
| `Live` | `Long` | `161.50` | 5,560,000.00 USD | 0.00 USD | 807.50 USD | `-76.77%` | `5,000,000,000.00` |
| `Live` | `Long` | `178.50` | 5,560,000.00 USD | 0.00 USD | 239.90 USD | `-74.32%` | `1,344,000,000.00` |
| `Live` | `Long` | `182.50` | 5,560,000.00 USD | 0.00 USD | 662.29 USD | `-73.75%` | `3,629,000,000.00` |
| `Live` | `Long` | `186.50` | 5,560,000.00 USD | 0.00 USD | 18,650.00 USD | `-73.17%` | `100,000,000,000.00` |
| `Live` | `Long` | `191.50` | 5,540,000.00 USD | 0.00 USD | 983.35 USD | `-72.45%` | `5,135,000,000.00` |
| `Live` | `Long` | `194.50` | 5,540,000.00 USD | 0.00 USD | 1,400.00 USD | `-72.02%` | `7,186,000,000.00` |
| `Live` | `Long` | `205.50` | 5,540,000.00 USD | 0.00 USD | 14,470.00 USD | `-70.44%` | `70,416,000,000.00` |
| `Live` | `Long` | `219.50` | 5,520,000.00 USD | 0.00 USD | 191.18 USD | `-68.42%` | `871,000,000.00` |
| `Live` | `Long` | `226.50` | 5,520,000.00 USD | 0.00 USD | 30,920.00 USD | `-67.42%` | `136,492,000,000.00` |
| `Live` | `Long` | `229.50` | 5,490,000.00 USD | 0.00 USD | 282.06 USD | `-66.98%` | `1,229,000,000.00` |
| `Live` | `Long` | `232.50` | 5,490,000.00 USD | 0.00 USD | 232,730.00 USD | `-66.55%` | `1,000,994,000,000.00` |
| `Live` | `Long` | `245.50` | 5,260,000.00 USD | 0.00 USD | 56,470.00 USD | `-64.68%` | `230,000,000,000.00` |
| `Live` | `Long` | `254.50` | 5,200,000.00 USD | 0.00 USD | 17,670.00 USD | `-63.39%` | `69,447,000,000.00` |
| `Live` | `Long` | `257.50` | 5,190,000.00 USD | 0.00 USD | 4,370.00 USD | `-62.96%` | `16,965,000,000.00` |
| `Live` | `Long` | `260.50` | 5,180,000.00 USD | 0.00 USD | 9,280.00 USD | `-62.52%` | `35,618,000,000.00` |
| `Live` | `Long` | `261.50` | 5,170,000.00 USD | 0.00 USD | 1,380.00 USD | `-62.38%` | `5,281,000,000.00` |
| `Live` | `Long` | `267.50` | 5,170,000.00 USD | 0.00 USD | 383.33 USD | `-61.52%` | `1,433,000,000.00` |
| `Live` | `Long` | `277.50` | 5,170,000.00 USD | 0.00 USD | 22,000.00 USD | `-60.08%` | `79,269,000,000.00` |
| `Live` | `Long` | `279.50` | 5,150,000.00 USD | 0.00 USD | 464,330.00 USD | `-59.79%` | `1,661,280,000,000.00` |
| `Live` | `Long` | `281.50` | 4,680,000.00 USD | 0.00 USD | 428.16 USD | `-59.50%` | `1,521,000,000.00` |
| `Live` | `Long` | `284.50` | 4,680,000.00 USD | 0.00 USD | 707.84 USD | `-59.07%` | `2,488,000,000.00` |
| `Live` | `Long` | `293.50` | 4,680,000.00 USD | 0.00 USD | 413.83 USD | `-57.78%` | `1,410,000,000.00` |
| `Live` | `Long` | `308.50` | 4,680,000.00 USD | 0.00 USD | 624.10 USD | `-55.62%` | `2,023,000,000.00` |
| `Live` | `Long` | `313.50` | 4,680,000.00 USD | 0.00 USD | 501.60 USD | `-54.90%` | `1,600,000,000.00` |
| `Live` | `Long` | `326.50` | 4,680,000.00 USD | 0.00 USD | 1,530.00 USD | `-53.03%` | `4,681,000,000.00` |
| `Live` | `Long` | `328.50` | 4,680,000.00 USD | 0.00 USD | 315.03 USD | `-52.74%` | `959,000,000.00` |
| `Live` | `Long` | `330.50` | 4,680,000.00 USD | 0.00 USD | 308.36 USD | `-52.45%` | `933,000,000.00` |
| `Live` | `Long` | `332.50` | 4,680,000.00 USD | 0.00 USD | 1,650.00 USD | `-52.17%` | `4,951,000,000.00` |
| `Live` | `Long` | `333.50` | 4,680,000.00 USD | 0.00 USD | 377.19 USD | `-52.02%` | `1,131,000,000.00` |
| `Live` | `Long` | `334.50` | 4,680,000.00 USD | 0.00 USD | 444.55 USD | `-51.88%` | `1,329,000,000.00` |
| `Live` | `Long` | `335.50` | 4,680,000.00 USD | 0.00 USD | 118.43 USD | `-51.74%` | `353,000,000.00` |
| `Live` | `Long` | `337.50` | 4,680,000.00 USD | 0.00 USD | 14,340.00 USD | `-51.45%` | `42,500,000,000.00` |
| `Live` | `Long` | `338.50` | 4,660,000.00 USD | 0.00 USD | 936.63 USD | `-51.30%` | `2,767,000,000.00` |
| `Live` | `Short` | `339.50` | 23,360.00 USD | 23,360.00 USD | 0.00 USD | `-51.16%` | `68,813,000,000.00` |
| `Live` | `Long` | `343.50` | 4,660,000.00 USD | 0.00 USD | 652.65 USD | `-50.58%` | `1,900,000,000.00` |
| `Live` | `Long` | `359.50` | 4,660,000.00 USD | 0.00 USD | 212.10 USD | `-48.28%` | `590,000,000.00` |
| `Live` | `Long` | `362.50` | 4,660,000.00 USD | 0.00 USD | 1,630.00 USD | `-47.85%` | `4,504,000,000.00` |
| `Live` | `Long` | `363.50` | 4,660,000.00 USD | 0.00 USD | 1,540.00 USD | `-47.71%` | `4,250,000,000.00` |
| `Live` | `Long` | `366.50` | 4,660,000.00 USD | 0.00 USD | 549.75 USD | `-47.28%` | `1,500,000,000.00` |
| `Live` | `Long` | `370.50` | 4,660,000.00 USD | 0.00 USD | 1,220.00 USD | `-46.70%` | `3,300,000,000.00` |
| `Live` | `Long` | `373.50` | 4,650,000.00 USD | 0.00 USD | 709.65 USD | `-46.27%` | `1,900,000,000.00` |
| `Live` | `Long` | `374.50` | 4,650,000.00 USD | 0.00 USD | 7,440.00 USD | `-46.13%` | `19,854,000,000.00` |
| `Live` | `Long` | `377.50` | 4,650,000.00 USD | 0.00 USD | 438.65 USD | `-45.69%` | `1,162,000,000.00` |
| `Live` | `Long` | `378.50` | 4,650,000.00 USD | 0.00 USD | 7,760.00 USD | `-45.55%` | `20,499,000,000.00` |
| `Live` | `Long` | `379.50` | 4,640,000.00 USD | 0.00 USD | 645.15 USD | `-45.41%` | `1,700,000,000.00` |
| `Live` | `Long` | `382.50` | 4,640,000.00 USD | 0.00 USD | 1,910.00 USD | `-44.97%` | `5,000,000,000.00` |
| `Live` | `Long` | `383.50` | 4,640,000.00 USD | 0.00 USD | 10,900.00 USD | `-44.83%` | `28,414,000,000.00` |
| `Live` | `Long` | `385.50` | 4,630,000.00 USD | 0.00 USD | 2,860.00 USD | `-44.54%` | `7,421,000,000.00` |
| `Live` | `Long` | `386.50` | 4,620,000.00 USD | 0.00 USD | 531.44 USD | `-44.40%` | `1,375,000,000.00` |
| `Live` | `Long` | `388.50` | 4,620,000.00 USD | 0.00 USD | 393.55 USD | `-44.11%` | `1,013,000,000.00` |
| `Live` | `Long` | `391.50` | 4,620,000.00 USD | 0.00 USD | 211.02 USD | `-43.68%` | `539,000,000.00` |
| `Live` | `Long` | `393.50` | 4,620,000.00 USD | 0.00 USD | 103.88 USD | `-43.39%` | `264,000,000.00` |
| `Live` | `Long` | `394.50` | 4,620,000.00 USD | 0.00 USD | 13,030.00 USD | `-43.25%` | `33,032,000,000.00` |
| `Live` | `Long` | `395.50` | 4,610,000.00 USD | 0.00 USD | 2,110.00 USD | `-43.10%` | `5,347,000,000.00` |
| `Live` | `Long` | `396.50` | 4,610,000.00 USD | 0.00 USD | 396.50 USD | `-42.96%` | `1,000,000,000.00` |
| `Live` | `Long` | `397.50` | 4,610,000.00 USD | 0.00 USD | 318.00 USD | `-42.82%` | `800,000,000.00` |
| `Live` | `Long` | `398.50` | 4,610,000.00 USD | 0.00 USD | 360.64 USD | `-42.67%` | `905,000,000.00` |
| `Live` | `Long` | `400.50` | 4,600,000.00 USD | 0.00 USD | 605.16 USD | `-42.38%` | `1,511,000,000.00` |
| `Live` | `Long` | `404.50` | 4,600,000.00 USD | 0.00 USD | 102.34 USD | `-41.81%` | `253,000,000.00` |
| `Live` | `Long` | `410.50` | 4,600,000.00 USD | 0.00 USD | 614.52 USD | `-40.95%` | `1,497,000,000.00` |
| `Live` | `Long` | `411.50` | 4,600,000.00 USD | 0.00 USD | 3,590.00 USD | `-40.80%` | `8,713,000,000.00` |
| `Live` | `Long` | `414.50` | 4,600,000.00 USD | 0.00 USD | 23,680.00 USD | `-40.37%` | `57,128,000,000.00` |
| `Live` | `Long` | `415.50` | 4,580,000.00 USD | 0.00 USD | 1,810.00 USD | `-40.23%` | `4,368,000,000.00` |
| `Live` | `Long` | `416.50` | 4,570,000.00 USD | 0.00 USD | 880.90 USD | `-40.08%` | `2,115,000,000.00` |
| `Live` | `Long` | `417.50` | 4,570,000.00 USD | 0.00 USD | 10,390.00 USD | `-39.94%` | `24,891,000,000.00` |
| `Live` | `Long` | `418.50` | 4,560,000.00 USD | 0.00 USD | 1,790.00 USD | `-39.80%` | `4,280,000,000.00` |
| `Live` | `Long` | `420.50` | 4,560,000.00 USD | 0.00 USD | 2,660.00 USD | `-39.51%` | `6,316,000,000.00` |
| `Live` | `Long` | `421.50` | 4,560,000.00 USD | 0.00 USD | 2,320.00 USD | `-39.36%` | `5,496,000,000.00` |
| `Live` | `Long` | `423.50` | 4,560,000.00 USD | 0.00 USD | 1,450.00 USD | `-39.08%` | `3,419,000,000.00` |
| `Live` | `Long` | `424.50` | 4,550,000.00 USD | 0.00 USD | 31,490.00 USD | `-38.93%` | `74,170,000,000.00` |
| `Live` | `Long` | `428.50` | 4,520,000.00 USD | 0.00 USD | 1,400.00 USD | `-38.36%` | `3,259,000,000.00` |
| `Live` | `Long` | `430.50` | 4,520,000.00 USD | 0.00 USD | 638.00 USD | `-38.07%` | `1,482,000,000.00` |
| `Live` | `Long` | `439.50` | 4,520,000.00 USD | 0.00 USD | 1,800.00 USD | `-36.77%` | `4,087,000,000.00` |
| `Live` | `Long` | `441.50` | 4,520,000.00 USD | 0.00 USD | 120.53 USD | `-36.49%` | `273,000,000.00` |
| `Live` | `Long` | `442.50` | 4,520,000.00 USD | 0.00 USD | 6,370.00 USD | `-36.34%` | `14,406,000,000.00` |
| `Live` | `Long` | `445.50` | 4,510,000.00 USD | 0.00 USD | 16,030.00 USD | `-35.91%` | `35,988,000,000.00` |
| `Live` | `Long` | `457.50` | 4,500,000.00 USD | 0.00 USD | 4,740.00 USD | `-34.18%` | `10,359,000,000.00` |
| `Live` | `Long` | `459.50` | 4,490,000.00 USD | 0.00 USD | 197.59 USD | `-33.90%` | `430,000,000.00` |
| `Live` | `Long` | `461.50` | 4,490,000.00 USD | 0.00 USD | 5,350.00 USD | `-33.61%` | `11,600,000,000.00` |
| `Live` | `Long` | `464.50` | 4,490,000.00 USD | 0.00 USD | 665.16 USD | `-33.18%` | `1,432,000,000.00` |
| `Live` | `Long` | `470.50` | 4,490,000.00 USD | 0.00 USD | 4,380.00 USD | `-32.31%` | `9,301,000,000.00` |
| `Live` | `Long` | `476.50` | 4,480,000.00 USD | 0.00 USD | 5,330.00 USD | `-31.45%` | `11,182,000,000.00` |
| `Live` | `Long` | `482.50` | 4,480,000.00 USD | 0.00 USD | 6,840.00 USD | `-30.59%` | `14,184,000,000.00` |
| `Live` | `Long` | `484.50` | 4,470,000.00 USD | 0.00 USD | 642.93 USD | `-30.30%` | `1,327,000,000.00` |
| `Live` | `Long` | `485.50` | 4,470,000.00 USD | 0.00 USD | 2,110.00 USD | `-30.16%` | `4,347,000,000.00` |
| `Live` | `Long` | `490.50` | 4,470,000.00 USD | 0.00 USD | 63,470.00 USD | `-29.44%` | `129,389,000,000.00` |
| `Live` | `Long` | `494.50` | 4,400,000.00 USD | 0.00 USD | 8,100.00 USD | `-28.86%` | `16,385,000,000.00` |
| `Live` | `Long` | `495.50` | 4,400,000.00 USD | 0.00 USD | 1,090.00 USD | `-28.72%` | `2,205,000,000.00` |
| `Live` | `Long` | `496.50` | 4,390,000.00 USD | 0.00 USD | 1,320.00 USD | `-28.57%` | `2,651,000,000.00` |
| `Live` | `Long` | `499.50` | 4,390,000.00 USD | 0.00 USD | 673.83 USD | `-28.14%` | `1,349,000,000.00` |
| `Live` | `Long` | `500.50` | 4,390,000.00 USD | 0.00 USD | 60,030.00 USD | `-28.00%` | `119,940,000,000.00` |
| `Live` | `Long` | `501.50` | 4,330,000.00 USD | 0.00 USD | 7,760.00 USD | `-27.86%` | `15,482,000,000.00` |
| `Live` | `Long` | `502.50` | 4,320,000.00 USD | 0.00 USD | 1,180.00 USD | `-27.71%` | `2,354,000,000.00` |
| `Live` | `Long` | `504.50` | 4,320,000.00 USD | 0.00 USD | 765.33 USD | `-27.42%` | `1,517,000,000.00` |
| `Live` | `Long` | `506.50` | 4,320,000.00 USD | 0.00 USD | 5,770.00 USD | `-27.14%` | `11,387,000,000.00` |
| `Live` | `Long` | `509.50` | 4,320,000.00 USD | 0.00 USD | 3,610.00 USD | `-26.70%` | `7,091,000,000.00` |
| `Live` | `Long` | `511.50` | 4,310,000.00 USD | 0.00 USD | 4,470.00 USD | `-26.42%` | `8,732,000,000.00` |
| `Live` | `Long` | `512.50` | 4,310,000.00 USD | 0.00 USD | 5,960.00 USD | `-26.27%` | `11,630,000,000.00` |
| `Live` | `Long` | `513.50` | 4,300,000.00 USD | 0.00 USD | 295.78 USD | `-26.13%` | `576,000,000.00` |
| `Live` | `Long` | `514.50` | 4,300,000.00 USD | 0.00 USD | 4,010.00 USD | `-25.99%` | `7,787,000,000.00` |
| `Live` | `Long` | `515.50` | 4,300,000.00 USD | 0.00 USD | 3,780.00 USD | `-25.84%` | `7,323,000,000.00` |
| `Live` | `Long` | `516.50` | 4,290,000.00 USD | 0.00 USD | 5,700.00 USD | `-25.70%` | `11,040,000,000.00` |
| `Live` | `Long` | `517.50` | 4,290,000.00 USD | 0.00 USD | 1,160.00 USD | `-25.55%` | `2,246,000,000.00` |
| `Live` | `Long` | `518.50` | 4,290,000.00 USD | 0.00 USD | 22,690.00 USD | `-25.41%` | `43,765,000,000.00` |
| `Live` | `Long` | `519.50` | 4,260,000.00 USD | 0.00 USD | 968.35 USD | `-25.27%` | `1,864,000,000.00` |
| `Live` | `Long` | `520.50` | 4,260,000.00 USD | 0.00 USD | 272.22 USD | `-25.12%` | `523,000,000.00` |
| `Live` | `Long` | `521.50` | 4,260,000.00 USD | 0.00 USD | 838.05 USD | `-24.98%` | `1,607,000,000.00` |
| `Live` | `Long` | `522.50` | 4,260,000.00 USD | 0.00 USD | 261.25 USD | `-24.83%` | `500,000,000.00` |
| `Live` | `Long` | `523.50` | 4,260,000.00 USD | 0.00 USD | 2,090.00 USD | `-24.69%` | `3,993,000,000.00` |
| `Live` | `Long` | `525.50` | 4,260,000.00 USD | 0.00 USD | 992.67 USD | `-24.40%` | `1,889,000,000.00` |
| `Live` | `Long` | `526.50` | 4,260,000.00 USD | 0.00 USD | 2,960.00 USD | `-24.26%` | `5,624,000,000.00` |
| `Live` | `Long` | `529.50` | 4,260,000.00 USD | 0.00 USD | 42,820.00 USD | `-23.83%` | `80,869,000,000.00` |
| `Live` | `Long` | `530.50` | 4,210,000.00 USD | 0.00 USD | 17,770.00 USD | `-23.68%` | `33,504,000,000.00` |
| `Live` | `Long` | `531.50` | 4,200,000.00 USD | 0.00 USD | 1,070.00 USD | `-23.54%` | `2,018,000,000.00` |
| `Live` | `Long` | `532.50` | 4,190,000.00 USD | 0.00 USD | 632.08 USD | `-23.40%` | `1,187,000,000.00` |
| `Live` | `Long` | `534.50` | 4,190,000.00 USD | 0.00 USD | 11,100.00 USD | `-23.11%` | `20,764,000,000.00` |
| `Live` | `Long` | `536.50` | 4,180,000.00 USD | 0.00 USD | 100.33 USD | `-22.82%` | `187,000,000.00` |
| `Live` | `Long` | `539.50` | 4,180,000.00 USD | 0.00 USD | 490.94 USD | `-22.39%` | `910,000,000.00` |
| `Live` | `Long` | `541.50` | 4,180,000.00 USD | 0.00 USD | 472.19 USD | `-22.10%` | `872,000,000.00` |
| `Live` | `Long` | `543.50` | 4,180,000.00 USD | 0.00 USD | 5,130.00 USD | `-21.81%` | `9,439,000,000.00` |
| `Live` | `Long` | `544.50` | 4,180,000.00 USD | 0.00 USD | 31,770.00 USD | `-21.67%` | `58,356,000,000.00` |
| `Live` | `Long` | `545.50` | 4,150,000.00 USD | 0.00 USD | 212,310.00 USD | `-21.53%` | `389,204,000,000.00` |
| `Live` | `Long` | `546.50` | 3,930,000.00 USD | 0.00 USD | 491.85 USD | `-21.38%` | `900,000,000.00` |
| `Live` | `Long` | `547.50` | 3,930,000.00 USD | 0.00 USD | 49,120.00 USD | `-21.24%` | `89,710,000,000.00` |
| `Live` | `Long` | `549.50` | 3,880,000.00 USD | 0.00 USD | 1,770.00 USD | `-20.95%` | `3,224,000,000.00` |
| `Live` | `Long` | `550.50` | 3,880,000.00 USD | 0.00 USD | 633.63 USD | `-20.81%` | `1,151,000,000.00` |
| `Live` | `Long` | `552.50` | 3,880,000.00 USD | 0.00 USD | 959.69 USD | `-20.52%` | `1,737,000,000.00` |
| `Live` | `Long` | `553.50` | 3,880,000.00 USD | 0.00 USD | 2,730.00 USD | `-20.37%` | `4,937,000,000.00` |
| `Live` | `Long` | `554.50` | 3,880,000.00 USD | 0.00 USD | 415.88 USD | `-20.23%` | `750,000,000.00` |
| `Live` | `Long` | `555.50` | 3,880,000.00 USD | 0.00 USD | 274.97 USD | `-20.09%` | `495,000,000.00` |
| `Live` | `Long` | `556.50` | 3,880,000.00 USD | 0.00 USD | 556.50 USD | `-19.94%` | `1,000,000,000.00` |
| `Live` | `Long` | `557.50` | 3,880,000.00 USD | 0.00 USD | 5,680.00 USD | `-19.80%` | `10,193,000,000.00` |
| `Live` | `Long` | `559.50` | 3,870,000.00 USD | 0.00 USD | 212.61 USD | `-19.51%` | `380,000,000.00` |
| `Live` | `Long` | `561.50` | 3,870,000.00 USD | 0.00 USD | 583.40 USD | `-19.22%` | `1,039,000,000.00` |
| `Live` | `Long` | `565.50` | 3,870,000.00 USD | 0.00 USD | 1,630.00 USD | `-18.65%` | `2,883,000,000.00` |
| `Live` | `Long` | `568.50` | 3,870,000.00 USD | 0.00 USD | 454.80 USD | `-18.22%` | `800,000,000.00` |
| `Live` | `Long` | `572.50` | 3,870,000.00 USD | 0.00 USD | 723,830.00 USD | `-17.64%` | `1,264,326,000,000.00` |
| `Live` | `Short` | `573.50` | 66,470.00 USD | 43,110.00 USD | 0.00 USD | `-17.50%` | `75,162,000,000.00` |
| `Live` | `Long` | `574.50` | 3,140,000.00 USD | 0.00 USD | 323.44 USD | `-17.35%` | `563,000,000.00` |
| `Live` | `Long` | `576.50` | 3,140,000.00 USD | 0.00 USD | 416.23 USD | `-17.07%` | `722,000,000.00` |
| `Live` | `Long` | `578.50` | 3,140,000.00 USD | 0.00 USD | 6,120.00 USD | `-16.78%` | `10,579,000,000.00` |
| `Live` | `Long` | `579.50` | 3,140,000.00 USD | 0.00 USD | 2,240.00 USD | `-16.63%` | `3,861,000,000.00` |
| `Live` | `Long` | `581.50` | 3,130,000.00 USD | 0.00 USD | 35,070.00 USD | `-16.35%` | `60,313,000,000.00` |
| `Live` | `Long` | `583.50` | 3,100,000.00 USD | 0.00 USD | 567.16 USD | `-16.06%` | `972,000,000.00` |
| `Live` | `Long` | `585.50` | 3,100,000.00 USD | 0.00 USD | 314.41 USD | `-15.77%` | `537,000,000.00` |
| `Live` | `Long` | `587.50` | 3,100,000.00 USD | 0.00 USD | 1,530.00 USD | `-15.48%` | `2,612,000,000.00` |
| `Live` | `Long` | `590.50` | 3,100,000.00 USD | 0.00 USD | 304.11 USD | `-15.05%` | `515,000,000.00` |
| `Live` | `Long` | `594.50` | 3,100,000.00 USD | 0.00 USD | 44,800.00 USD | `-14.48%` | `75,354,000,000.00` |
| `Live` | `Long` | `595.50` | 3,050,000.00 USD | 0.00 USD | 19,210.00 USD | `-14.33%` | `32,260,000,000.00` |
| `Live` | `Long` | `597.50` | 3,030,000.00 USD | 0.00 USD | 100.98 USD | `-14.04%` | `169,000,000.00` |
| `Live` | `Long` | `598.50` | 3,030,000.00 USD | 0.00 USD | 101.75 USD | `-13.90%` | `170,000,000.00` |
| `Live` | `Long` | `599.50` | 3,030,000.00 USD | 0.00 USD | 116.90 USD | `-13.76%` | `195,000,000.00` |
| `Live` | `Long` | `600.50` | 3,030,000.00 USD | 0.00 USD | 7,670.00 USD | `-13.61%` | `12,768,000,000.00` |
| `Live` | `Long` | `601.50` | 3,020,000.00 USD | 0.00 USD | 191.28 USD | `-13.47%` | `318,000,000.00` |
| `Live` | `Long` | `602.50` | 3,020,000.00 USD | 0.00 USD | 4,220.00 USD | `-13.33%` | `7,002,000,000.00` |
| `Live` | `Long` | `604.50` | 3,020,000.00 USD | 0.00 USD | 1,610.00 USD | `-13.04%` | `2,671,000,000.00` |
| `Live` | `Short` | `605.50` | 70,810.00 USD | 4,340.00 USD | 0.00 USD | `-12.89%` | `7,168,000,000.00` |
| `Live` | `Long` | `607.50` | 3,020,000.00 USD | 0.00 USD | 2,690.00 USD | `-12.61%` | `4,428,000,000.00` |
| `Live` | `Long` | `610.50` | 3,020,000.00 USD | 0.00 USD | 213.67 USD | `-12.17%` | `350,000,000.00` |
| `Live` | `Long` | `613.50` | 3,020,000.00 USD | 0.00 USD | 99,140.00 USD | `-11.74%` | `161,593,000,000.00` |
| `Live` | `Long` | `614.50` | 2,920,000.00 USD | 0.00 USD | 2,280.00 USD | `-11.60%` | `3,710,000,000.00` |
| `Live` | `Long` | `615.50` | 2,910,000.00 USD | 0.00 USD | 427.16 USD | `-11.46%` | `694,000,000.00` |
| `Live` | `Long` | `616.50` | 2,910,000.00 USD | 0.00 USD | 1,320.00 USD | `-11.31%` | `2,146,000,000.00` |
| `Live` | `Long` | `617.50` | 2,910,000.00 USD | 0.00 USD | 156.23 USD | `-11.17%` | `253,000,000.00` |
| `Live` | `Long` | `619.50` | 2,910,000.00 USD | 0.00 USD | 600.91 USD | `-10.88%` | `970,000,000.00` |
| `Live` | `Long` | `620.50` | 2,910,000.00 USD | 0.00 USD | 5,410.00 USD | `-10.74%` | `8,712,000,000.00` |
| `Live` | `Long` | `621.50` | 2,910,000.00 USD | 0.00 USD | 3,230.00 USD | `-10.59%` | `5,194,000,000.00` |
| `Live` | `Long` | `622.50` | 2,900,000.00 USD | 0.00 USD | 2,110.00 USD | `-10.45%` | `3,397,000,000.00` |
| `Live` | `Long` | `623.50` | 2,900,000.00 USD | 0.00 USD | 14,580.00 USD | `-10.30%` | `23,389,000,000.00` |
| `Live` | `Long` | `624.50` | 2,890,000.00 USD | 0.00 USD | 3,460.00 USD | `-10.16%` | `5,547,000,000.00` |
| `Live` | `Long` | `625.50` | 2,880,000.00 USD | 0.00 USD | 29,690.00 USD | `-10.02%` | `47,468,000,000.00` |
| `Live` | `Short` | `626.50` | 71,350.00 USD | 539.42 USD | 0.00 USD | `-9.87%` | `861,000,000.00` |
| `Live` | `Long` | `627.50` | 2,850,000.00 USD | 0.00 USD | 326.30 USD | `-9.73%` | `520,000,000.00` |
| `Live` | `Long` | `630.50` | 2,850,000.00 USD | 0.00 USD | 153.21 USD | `-9.30%` | `243,000,000.00` |
| `Live` | `Long` | `631.50` | 2,850,000.00 USD | 0.00 USD | 1,130,000.00 USD | `-9.15%` | `1,796,973,000,000.00` |
| `Live` | `Long` | `632.50` | 1,720,000.00 USD | 0.00 USD | 125.87 USD | `-9.01%` | `199,000,000.00` |
| `Live` | `Long` | `633.50` | 1,720,000.00 USD | 0.00 USD | 1,820.00 USD | `-8.87%` | `2,880,000,000.00` |
| `Live` | `Long` | `634.50` | 1,720,000.00 USD | 0.00 USD | 1,480,000.00 USD | `-8.72%` | `2,335,694,000,000.00` |
| `Live` | `Long` | `635.50` | 234,070.00 USD | 0.00 USD | 8,680.00 USD | `-8.58%` | `13,666,000,000.00` |
| `Live` | `Short` | `636.50` | 71,500.00 USD | 154.67 USD | 0.00 USD | `-8.43%` | `243,000,000.00` |
| `Live` | `Long` | `637.50` | 225,390.00 USD | 0.00 USD | 1,110.00 USD | `-8.29%` | `1,743,000,000.00` |
| `Live` | `Long` | `638.50` | 224,280.00 USD | 0.00 USD | 432.90 USD | `-8.15%` | `678,000,000.00` |
| `Live` | `Long` | `640.50` | 223,840.00 USD | 0.00 USD | 95,270.00 USD | `-7.86%` | `148,737,000,000.00` |
| `Live` | `Long` | `641.50` | 128,580.00 USD | 0.00 USD | 31,030.00 USD | `-7.72%` | `48,374,000,000.00` |
| `Live` | `Long` | `642.50` | 97,550.00 USD | 0.00 USD | 13,340.00 USD | `-7.57%` | `20,755,000,000.00` |
| `Live` | `Long` | `643.50` | 84,210.00 USD | 0.00 USD | 8,490.00 USD | `-7.43%` | `13,199,000,000.00` |
| `Live` | `Long` | `645.50` | 75,720.00 USD | 0.00 USD | 5,050.00 USD | `-7.14%` | `7,817,000,000.00` |
| `Live` | `Long` | `646.50` | 70,670.00 USD | 0.00 USD | 155.81 USD | `-7.00%` | `241,000,000.00` |
| `Live` | `Short` | `647.50` | 71,640.00 USD | 143.10 USD | 0.00 USD | `-6.85%` | `221,000,000.00` |
| `Live` | `Short` | `648.50` | 71,850.00 USD | 201.68 USD | 0.00 USD | `-6.71%` | `311,000,000.00` |
| `Live` | `Long` | `649.50` | 70,520.00 USD | 0.00 USD | 136.39 USD | `-6.56%` | `210,000,000.00` |
| `Live` | `Short` | `650.50` | 175,000.00 USD | 103,150.00 USD | 0.00 USD | `-6.42%` | `158,569,000,000.00` |
| `Live` | `Long` | `651.50` | 70,380.00 USD | 0.00 USD | 633.26 USD | `-6.28%` | `972,000,000.00` |
| `Live` | `Short` | `652.50` | 456,300.00 USD | 281,310.00 USD | 0.00 USD | `-6.13%` | `431,120,000,000.00` |
| `Live` | `Short` | `653.50` | 1,030,000.00 USD | 572,750.00 USD | 0.00 USD | `-5.99%` | `876,433,000,000.00` |
| `Live` | `Long` | `654.50` | 69,750.00 USD | 0.00 USD | 36,890.00 USD | `-5.84%` | `56,361,000,000.00` |
| `Live` | `Short` | `655.50` | 1,040,000.00 USD | 13,670.00 USD | 0.00 USD | `-5.70%` | `20,856,000,000.00` |
| `Live` | `Short` | `656.50` | 1,060,000.00 USD | 14,050.00 USD | 0.00 USD | `-5.56%` | `21,402,000,000.00` |
| `Live` | `Short` | `657.50` | 1,080,000.00 USD | 18,320.00 USD | 0.00 USD | `-5.41%` | `27,856,000,000.00` |
| `Live` | `Short` | `658.50` | 1,080,000.00 USD | 3,230.00 USD | 0.00 USD | `-5.27%` | `4,902,000,000.00` |
| `Live` | `Short` | `659.50` | 1,110,000.00 USD | 30,770.00 USD | 0.00 USD | `-5.13%` | `46,654,000,000.00` |
| `Live` | `Short` | `660.50` | 1,170,000.00 USD | 57,190.00 USD | 0.00 USD | `-4.98%` | `86,588,000,000.00` |
| `Live` | `Short` | `661.50` | 1,210,000.00 USD | 44,730.00 USD | 0.00 USD | `-4.84%` | `67,615,000,000.00` |
| `Live` | `Long` | `662.50` | 32,860.00 USD | 0.00 USD | 6,630.00 USD | `-4.69%` | `10,007,000,000.00` |
| `Live` | `Short` | `663.50` | 1,320,000.00 USD | 112,010.00 USD | 0.00 USD | `-4.55%` | `168,822,000,000.00` |
| `Live` | `Long` | `664.50` | 26,230.00 USD | 0.00 USD | 18,240.00 USD | `-4.41%` | `27,453,000,000.00` |
| `Live` | `Short` | `665.50` | 1,360,000.00 USD | 41,170.00 USD | 0.00 USD | `-4.26%` | `61,867,000,000.00` |
| `Live` | `Long` | `666.50` | 7,990.00 USD | 0.00 USD | 3,810.00 USD | `-4.12%` | `5,723,000,000.00` |
| `Live` | `Short` | `667.50` | 1,370,000.00 USD | 2,600.00 USD | 0.00 USD | `-3.97%` | `3,889,000,000.00` |
| `Live` | `Short` | `668.50` | 1,600,000.00 USD | 237,980.00 USD | 0.00 USD | `-3.83%` | `355,993,000,000.00` |
| `Live` | `Short` | `669.50` | 1,610,000.00 USD | 2,570.00 USD | 0.00 USD | `-3.69%` | `3,846,000,000.00` |
| `Live` | `Long` | `670.50` | 4,170.00 USD | 0.00 USD | 1,580.00 USD | `-3.54%` | `2,363,000,000.00` |
| `Live` | `Short` | `671.50` | 1,760,000.00 USD | 151,690.00 USD | 0.00 USD | `-3.40%` | `225,898,000,000.00` |
| `Live` | `Long` | `672.50` | 2,590.00 USD | 0.00 USD | 1,380.00 USD | `-3.26%` | `2,053,000,000.00` |
| `Live` | `Long` | `673.50` | 1,210.00 USD | 0.00 USD | 567.76 USD | `-3.11%` | `843,000,000.00` |
| `Live` | `Long` | `674.50` | 638.86 USD | 0.00 USD | 259.68 USD | `-2.97%` | `385,000,000.00` |
| `Live` | `Long` | `675.50` | 379.18 USD | 0.00 USD | 105.38 USD | `-2.82%` | `156,000,000.00` |
| `Live` | `Short` | `676.50` | 1,760,000.00 USD | 168.45 USD | 0.00 USD | `-2.68%` | `249,000,000.00` |
| `Live` | `Long` | `684.50` | 273.80 USD | 0.00 USD | 273.80 USD | `-1.53%` | `400,000,000.00` |
| `Live` | `Short` | `695.50` | 1,760,000.00 USD | 302.54 USD | 0.00 USD | `+0.05%` | `435,000,000.00` |
| `Live` | `Short` | `705.50` | 1,770,000.00 USD | 6,470.00 USD | 0.00 USD | `+1.49%` | `9,168,000,000.00` |
| `Live` | `Short` | `706.50` | 1,860,000.00 USD | 98,910.00 USD | 0.00 USD | `+1.64%` | `140,000,000,000.00` |
| `Live` | `Short` | `707.50` | 1,870,000.00 USD | 4,830.00 USD | 0.00 USD | `+1.78%` | `6,828,000,000.00` |
| `Live` | `Short` | `709.50` | 1,870,000.00 USD | 1,420.00 USD | 0.00 USD | `+2.07%` | `2,000,000,000.00` |
| `Live` | `Short` | `710.50` | 1,870,000.00 USD | 153.47 USD | 0.00 USD | `+2.21%` | `216,000,000.00` |
| `Live` | `Short` | `711.50` | 1,880,000.00 USD | 3,750.00 USD | 0.00 USD | `+2.35%` | `5,272,000,000.00` |
| `Live` | `Short` | `712.50` | 1,880,000.00 USD | 971.14 USD | 0.00 USD | `+2.50%` | `1,363,000,000.00` |
| `Live` | `Short` | `713.50` | 1,900,000.00 USD | 27,480.00 USD | 0.00 USD | `+2.64%` | `38,515,000,000.00` |
| `Live` | `Short` | `714.50` | 1,900,000.00 USD | 178.62 USD | 0.00 USD | `+2.79%` | `250,000,000.00` |
| `Live` | `Short` | `715.50` | 1,910,000.00 USD | 9,950.00 USD | 0.00 USD | `+2.93%` | `13,912,000,000.00` |
| `Live` | `Short` | `717.50` | 1,920,000.00 USD | 6,650.00 USD | 0.00 USD | `+3.22%` | `9,268,000,000.00` |
| `Live` | `Short` | `718.50` | 1,920,000.00 USD | 158.79 USD | 0.00 USD | `+3.36%` | `221,000,000.00` |
| `Live` | `Short` | `719.50` | 1,920,000.00 USD | 705.11 USD | 0.00 USD | `+3.51%` | `980,000,000.00` |
| `Live` | `Short` | `720.50` | 1,990,000.00 USD | 64,940.00 USD | 0.00 USD | `+3.65%` | `90,138,000,000.00` |
| `Live` | `Short` | `721.50` | 2,150,000.00 USD | 160,460.00 USD | 0.00 USD | `+3.79%` | `222,401,000,000.00` |
| `Live` | `Short` | `722.50` | 2,150,000.00 USD | 3,740.00 USD | 0.00 USD | `+3.94%` | `5,172,000,000.00` |
| `Live` | `Short` | `723.50` | 2,260,000.00 USD | 111,640.00 USD | 0.00 USD | `+4.08%` | `154,307,000,000.00` |
| `Live` | `Short` | `724.50` | 2,370,000.00 USD | 112,820.00 USD | 0.00 USD | `+4.23%` | `155,720,000,000.00` |
| `Live` | `Short` | `725.50` | 2,370,000.00 USD | 42.80 USD | 0.00 USD | `+4.37%` | `59,000,000.00` |
| `Live` | `Short` | `726.50` | 2,430,000.00 USD | 56,650.00 USD | 0.00 USD | `+4.51%` | `77,971,000,000.00` |
| `Live` | `Short` | `727.50` | 2,440,000.00 USD | 6,020.00 USD | 0.00 USD | `+4.66%` | `8,281,000,000.00` |
| `Live` | `Short` | `728.50` | 2,580,000.00 USD | 140,520.00 USD | 0.00 USD | `+4.80%` | `192,886,000,000.00` |
| `Live` | `Short` | `729.50` | 2,590,000.00 USD | 13,400.00 USD | 0.00 USD | `+4.94%` | `18,373,000,000.00` |
| `Live` | `Short` | `730.50` | 2,590,000.00 USD | 842.27 USD | 0.00 USD | `+5.09%` | `1,153,000,000.00` |
| `Live` | `Short` | `731.50` | 2,630,000.00 USD | 38,660.00 USD | 0.00 USD | `+5.23%` | `52,844,000,000.00` |
| `Live` | `Short` | `732.50` | 2,660,000.00 USD | 29,020.00 USD | 0.00 USD | `+5.38%` | `39,615,000,000.00` |
| `Live` | `Short` | `733.50` | 2,870,000.00 USD | 207,280.00 USD | 0.00 USD | `+5.52%` | `282,594,000,000.00` |
| `Live` | `Short` | `734.50` | 3,030,000.00 USD | 161,950.00 USD | 0.00 USD | `+5.66%` | `220,493,000,000.00` |
| `Live` | `Short` | `735.50` | 3,030,000.00 USD | 339.80 USD | 0.00 USD | `+5.81%` | `462,000,000.00` |
| `Live` | `Short` | `736.50` | 3,120,000.00 USD | 90,550.00 USD | 0.00 USD | `+5.95%` | `122,948,000,000.00` |
| `Live` | `Short` | `737.50` | 3,650,000.00 USD | 530,510.00 USD | 0.00 USD | `+6.10%` | `719,340,000,000.00` |
| `Live` | `Short` | `738.50` | 3,730,000.00 USD | 77,910.00 USD | 0.00 USD | `+6.24%` | `105,491,000,000.00` |
| `Live` | `Short` | `739.50` | 3,760,000.00 USD | 29,980.00 USD | 0.00 USD | `+6.38%` | `40,547,000,000.00` |
| `Live` | `Short` | `740.50` | 4,300,000.00 USD | 537,670.00 USD | 0.00 USD | `+6.53%` | `726,085,000,000.00` |
| `Live` | `Short` | `741.50` | 4,300,000.00 USD | 1,500.00 USD | 0.00 USD | `+6.67%` | `2,028,000,000.00` |
| `Live` | `Short` | `742.50` | 4,300,000.00 USD | 1,800.00 USD | 0.00 USD | `+6.81%` | `2,430,000,000.00` |
| `Live` | `Short` | `743.50` | 4,830,000.00 USD | 526,730.00 USD | 0.00 USD | `+6.96%` | `708,444,000,000.00` |
| `Live` | `Short` | `744.50` | 4,860,000.00 USD | 29,480.00 USD | 0.00 USD | `+7.10%` | `39,594,000,000.00` |
| `Live` | `Short` | `745.50` | 4,860,000.00 USD | 456.25 USD | 0.00 USD | `+7.25%` | `612,000,000.00` |
| `Live` | `Short` | `746.50` | 4,870,000.00 USD | 11,580.00 USD | 0.00 USD | `+7.39%` | `15,508,000,000.00` |
| `Live` | `Short` | `747.50` | 4,910,000.00 USD | 47,340.00 USD | 0.00 USD | `+7.53%` | `63,329,000,000.00` |
| `Live` | `Short` | `748.50` | 5,130,000.00 USD | 213,670.00 USD | 0.00 USD | `+7.68%` | `285,467,000,000.00` |
| `Live` | `Short` | `749.50` | 5,130,000.00 USD | 5,040.00 USD | 0.00 USD | `+7.82%` | `6,719,000,000.00` |
| `Live` | `Short` | `750.50` | 5,220,000.00 USD | 88,430.00 USD | 0.00 USD | `+7.97%` | `117,833,000,000.00` |
| `Live` | `Short` | `752.50` | 5,870,000.00 USD | 646,750.00 USD | 0.00 USD | `+8.25%` | `859,475,000,000.00` |
| `Live` | `Short` | `753.50` | 5,870,000.00 USD | 768.57 USD | 0.00 USD | `+8.40%` | `1,020,000,000.00` |
| `Live` | `Short` | `754.50` | 5,870,000.00 USD | 3,280.00 USD | 0.00 USD | `+8.54%` | `4,349,000,000.00` |
| `Live` | `Short` | `755.50` | 5,870,000.00 USD | 1,990.00 USD | 0.00 USD | `+8.68%` | `2,637,000,000.00` |
| `Live` | `Short` | `757.50` | 6,730,000.00 USD | 859,510.00 USD | 0.00 USD | `+8.97%` | `1,134,665,000,000.00` |
| `Live` | `Short` | `760.50` | 6,740,000.00 USD | 2,360.00 USD | 0.00 USD | `+9.40%` | `3,103,000,000.00` |
| `Live` | `Short` | `761.50` | 6,740,000.00 USD | 131.74 USD | 0.00 USD | `+9.55%` | `173,000,000.00` |
| `Live` | `Short` | `762.50` | 6,740,000.00 USD | 269.93 USD | 0.00 USD | `+9.69%` | `354,000,000.00` |
| `Live` | `Short` | `763.50` | 7,170,000.00 USD | 435,970.00 USD | 0.00 USD | `+9.84%` | `571,013,000,000.00` |
| `Live` | `Short` | `764.50` | 8,120,000.00 USD | 949,210.00 USD | 0.00 USD | `+9.98%` | `1,241,615,000,000.00` |
| `Live` | `Short` | `765.50` | 8,130,000.00 USD | 9,770.00 USD | 0.00 USD | `+10.12%` | `12,758,000,000.00` |
| `Live` | `Short` | `766.50` | 8,130,000.00 USD | 820.92 USD | 0.00 USD | `+10.27%` | `1,071,000,000.00` |
| `Live` | `Short` | `768.50` | 8,170,000.00 USD | 35,070.00 USD | 0.00 USD | `+10.55%` | `45,640,000,000.00` |
| `Live` | `Short` | `770.50` | 8,170,000.00 USD | 500.05 USD | 0.00 USD | `+10.84%` | `649,000,000.00` |
| `Live` | `Short` | `771.50` | 8,180,000.00 USD | 14,940.00 USD | 0.00 USD | `+10.99%` | `19,371,000,000.00` |
| `Live` | `Short` | `772.50` | 8,200,000.00 USD | 21,470.00 USD | 0.00 USD | `+11.13%` | `27,788,000,000.00` |
| `Live` | `Short` | `773.50` | 8,220,000.00 USD | 11,500.00 USD | 0.00 USD | `+11.27%` | `14,863,000,000.00` |
| `Live` | `Short` | `774.50` | 8,680,000.00 USD | 464,830.00 USD | 0.00 USD | `+11.42%` | `600,168,000,000.00` |
| `Live` | `Short` | `775.50` | 8,770,000.00 USD | 85,620.00 USD | 0.00 USD | `+11.56%` | `110,402,000,000.00` |
| `Live` | `Short` | `776.50` | 8,770,000.00 USD | 2,230.00 USD | 0.00 USD | `+11.71%` | `2,874,000,000.00` |
| `Live` | `Short` | `777.50` | 8,770,000.00 USD | 209.15 USD | 0.00 USD | `+11.85%` | `269,000,000.00` |
| `Live` | `Short` | `778.50` | 8,980,000.00 USD | 207,580.00 USD | 0.00 USD | `+11.99%` | `266,639,000,000.00` |
| `Live` | `Short` | `781.50` | 8,980,000.00 USD | 1,430.00 USD | 0.00 USD | `+12.43%` | `1,824,000,000.00` |
| `Live` | `Short` | `782.50` | 9,220,000.00 USD | 240,380.00 USD | 0.00 USD | `+12.57%` | `307,189,000,000.00` |
| `Live` | `Short` | `783.50` | 9,270,000.00 USD | 52,930.00 USD | 0.00 USD | `+12.71%` | `67,551,000,000.00` |
| `Live` | `Short` | `784.50` | 9,280,000.00 USD | 13,210.00 USD | 0.00 USD | `+12.86%` | `16,838,000,000.00` |
| `Live` | `Short` | `786.50` | 9,300,000.00 USD | 11,280.00 USD | 0.00 USD | `+13.14%` | `14,348,000,000.00` |
| `Live` | `Short` | `787.50` | 9,420,000.00 USD | 124,850.00 USD | 0.00 USD | `+13.29%` | `158,542,000,000.00` |
| `Live` | `Short` | `788.50` | 9,490,000.00 USD | 73,300.00 USD | 0.00 USD | `+13.43%` | `92,964,000,000.00` |
| `Live` | `Short` | `789.50` | 9,540,000.00 USD | 43,710.00 USD | 0.00 USD | `+13.58%` | `55,369,000,000.00` |
| `Live` | `Short` | `790.50` | 9,540,000.00 USD | 939.90 USD | 0.00 USD | `+13.72%` | `1,189,000,000.00` |
| `Live` | `Short` | `794.50` | 9,610,000.00 USD | 73,100.00 USD | 0.00 USD | `+14.30%` | `92,010,000,000.00` |
| `Live` | `Short` | `795.50` | 9,670,000.00 USD | 60,100.00 USD | 0.00 USD | `+14.44%` | `75,551,000,000.00` |
| `Live` | `Short` | `796.50` | 9,670,000.00 USD | 172.84 USD | 0.00 USD | `+14.58%` | `217,000,000.00` |
| `Live` | `Short` | `797.50` | 9,700,000.00 USD | 24,140.00 USD | 0.00 USD | `+14.73%` | `30,273,000,000.00` |
| `Live` | `Short` | `798.50` | 9,730,000.00 USD | 35,530.00 USD | 0.00 USD | `+14.87%` | `44,490,000,000.00` |
| `Live` | `Short` | `799.50` | 9,740,000.00 USD | 8,100.00 USD | 0.00 USD | `+15.01%` | `10,133,000,000.00` |
| `Live` | `Short` | `802.50` | 9,740,000.00 USD | 279.27 USD | 0.00 USD | `+15.45%` | `348,000,000.00` |
| `Live` | `Short` | `804.50` | 9,880,000.00 USD | 142,720.00 USD | 0.00 USD | `+15.73%` | `177,408,000,000.00` |
| `Live` | `Short` | `805.50` | 9,900,000.00 USD | 17,140.00 USD | 0.00 USD | `+15.88%` | `21,284,000,000.00` |
| `Live` | `Short` | `806.50` | 9,950,000.00 USD | 45,660.00 USD | 0.00 USD | `+16.02%` | `56,614,000,000.00` |
| `Live` | `Short` | `807.50` | 10,020,000.00 USD | 73,430.00 USD | 0.00 USD | `+16.17%` | `90,934,000,000.00` |
| `Live` | `Short` | `808.50` | 10,020,000.00 USD | 738.97 USD | 0.00 USD | `+16.31%` | `914,000,000.00` |
| `Live` | `Short` | `809.50` | 10,190,000.00 USD | 172,010.00 USD | 0.00 USD | `+16.45%` | `212,492,000,000.00` |
| `Live` | `Short` | `814.50` | 10,190,000.00 USD | 862.56 USD | 0.00 USD | `+17.17%` | `1,059,000,000.00` |
| `Live` | `Short` | `818.50` | 10,190,000.00 USD | 205.44 USD | 0.00 USD | `+17.75%` | `251,000,000.00` |
| `Live` | `Short` | `819.50` | 10,200,000.00 USD | 5,990.00 USD | 0.00 USD | `+17.89%` | `7,313,000,000.00` |
| `Live` | `Short` | `820.50` | 10,200,000.00 USD | 3,550.00 USD | 0.00 USD | `+18.04%` | `4,323,000,000.00` |
| `Live` | `Short` | `821.50` | 10,210,000.00 USD | 11,840.00 USD | 0.00 USD | `+18.18%` | `14,418,000,000.00` |
| `Live` | `Short` | `822.50` | 10,270,000.00 USD | 57,150.00 USD | 0.00 USD | `+18.32%` | `69,481,000,000.00` |
| `Live` | `Short` | `823.50` | 10,270,000.00 USD | 1,770.00 USD | 0.00 USD | `+18.47%` | `2,144,000,000.00` |
| `Live` | `Short` | `825.50` | 10,330,000.00 USD | 58,040.00 USD | 0.00 USD | `+18.75%` | `70,314,000,000.00` |
| `Live` | `Short` | `826.50` | 10,330,000.00 USD | 301.67 USD | 0.00 USD | `+18.90%` | `365,000,000.00` |
| `Live` | `Short` | `830.50` | 10,350,000.00 USD | 17,560.00 USD | 0.00 USD | `+19.47%` | `21,141,000,000.00` |
| `Live` | `Short` | `831.50` | 10,410,000.00 USD | 62,670.00 USD | 0.00 USD | `+19.62%` | `75,369,000,000.00` |
| `Live` | `Short` | `834.50` | 10,410,000.00 USD | 1,010.00 USD | 0.00 USD | `+20.05%` | `1,206,000,000.00` |
| `Live` | `Short` | `836.50` | 10,410,000.00 USD | 625.70 USD | 0.00 USD | `+20.34%` | `748,000,000.00` |
| `Live` | `Short` | `838.50` | 10,410,000.00 USD | 399.96 USD | 0.00 USD | `+20.62%` | `477,000,000.00` |
| `Live` | `Short` | `839.50` | 10,410,000.00 USD | 572.54 USD | 0.00 USD | `+20.77%` | `682,000,000.00` |
| `Live` | `Short` | `841.50` | 10,420,000.00 USD | 2,680.00 USD | 0.00 USD | `+21.06%` | `3,182,000,000.00` |
| `Live` | `Short` | `842.50` | 10,420,000.00 USD | 4,210.00 USD | 0.00 USD | `+21.20%` | `4,992,000,000.00` |
| `Live` | `Short` | `843.50` | 10,590,000.00 USD | 173,300.00 USD | 0.00 USD | `+21.34%` | `205,454,000,000.00` |
| `Live` | `Short` | `848.50` | 10,600,000.00 USD | 289.34 USD | 0.00 USD | `+22.06%` | `341,000,000.00` |
| `Live` | `Short` | `851.50` | 10,600,000.00 USD | 108.99 USD | 0.00 USD | `+22.50%` | `128,000,000.00` |
| `Live` | `Short` | `853.50` | 10,780,000.00 USD | 179,830.00 USD | 0.00 USD | `+22.78%` | `210,698,000,000.00` |
| `Live` | `Short` | `854.50` | 10,830,000.00 USD | 50,440.00 USD | 0.00 USD | `+22.93%` | `59,033,000,000.00` |
| `Live` | `Short` | `855.50` | 10,830,000.00 USD | 3,630.00 USD | 0.00 USD | `+23.07%` | `4,243,000,000.00` |
| `Live` | `Short` | `856.50` | 11,450,000.00 USD | 625,560.00 USD | 0.00 USD | `+23.21%` | `730,365,000,000.00` |
| `Live` | `Short` | `857.50` | 11,460,000.00 USD | 444.19 USD | 0.00 USD | `+23.36%` | `518,000,000.00` |
| `Live` | `Short` | `858.50` | 11,810,000.00 USD | 351,280.00 USD | 0.00 USD | `+23.50%` | `409,174,000,000.00` |
| `Live` | `Short` | `859.50` | 11,810,000.00 USD | 3,790.00 USD | 0.00 USD | `+23.65%` | `4,411,000,000.00` |
| `Live` | `Short` | `860.50` | 11,810,000.00 USD | 4,200.00 USD | 0.00 USD | `+23.79%` | `4,882,000,000.00` |
| `Live` | `Short` | `861.50` | 11,820,000.00 USD | 2,370.00 USD | 0.00 USD | `+23.93%` | `2,754,000,000.00` |
| `Live` | `Short` | `862.50` | 11,830,000.00 USD | 9,880.00 USD | 0.00 USD | `+24.08%` | `11,451,000,000.00` |
| `Live` | `Short` | `863.50` | 11,830,000.00 USD | 3,340.00 USD | 0.00 USD | `+24.22%` | `3,869,000,000.00` |
| `Live` | `Short` | `864.50` | 11,830,000.00 USD | 1,580.00 USD | 0.00 USD | `+24.37%` | `1,829,000,000.00` |
| `Live` | `Short` | `865.50` | 11,950,000.00 USD | 114,320.00 USD | 0.00 USD | `+24.51%` | `132,086,000,000.00` |
| `Live` | `Short` | `866.50` | 11,950,000.00 USD | 807.58 USD | 0.00 USD | `+24.65%` | `932,000,000.00` |
| `Live` | `Short` | `867.50` | 11,950,000.00 USD | 2,000.00 USD | 0.00 USD | `+24.80%` | `2,301,000,000.00` |
| `Live` | `Short` | `868.50` | 11,950,000.00 USD | 341.32 USD | 0.00 USD | `+24.94%` | `393,000,000.00` |
| `Live` | `Short` | `869.50` | 11,950,000.00 USD | 622.56 USD | 0.00 USD | `+25.08%` | `716,000,000.00` |
| `Live` | `Short` | `870.50` | 11,950,000.00 USD | 2,050.00 USD | 0.00 USD | `+25.23%` | `2,357,000,000.00` |
| `Live` | `Short` | `871.50` | 11,950,000.00 USD | 1,430.00 USD | 0.00 USD | `+25.37%` | `1,638,000,000.00` |
| `Live` | `Short` | `872.50` | 11,950,000.00 USD | 1,420.00 USD | 0.00 USD | `+25.52%` | `1,626,000,000.00` |
| `Live` | `Short` | `873.50` | 11,960,000.00 USD | 1,110.00 USD | 0.00 USD | `+25.66%` | `1,269,000,000.00` |
| `Live` | `Short` | `874.50` | 11,960,000.00 USD | 933.97 USD | 0.00 USD | `+25.80%` | `1,068,000,000.00` |
| `Live` | `Short` | `875.50` | 11,960,000.00 USD | 896.51 USD | 0.00 USD | `+25.95%` | `1,024,000,000.00` |
| `Live` | `Short` | `876.50` | 11,960,000.00 USD | 1,040.00 USD | 0.00 USD | `+26.09%` | `1,188,000,000.00` |
| `Live` | `Short` | `877.50` | 12,140,000.00 USD | 183,140.00 USD | 0.00 USD | `+26.24%` | `208,706,000,000.00` |
| `Live` | `Short` | `878.50` | 12,150,000.00 USD | 13,120.00 USD | 0.00 USD | `+26.38%` | `14,931,000,000.00` |
| `Live` | `Short` | `879.50` | 12,170,000.00 USD | 12,760.00 USD | 0.00 USD | `+26.52%` | `14,506,000,000.00` |
| `Live` | `Short` | `880.50` | 12,190,000.00 USD | 26,960.00 USD | 0.00 USD | `+26.67%` | `30,614,000,000.00` |
| `Live` | `Short` | `881.50` | 12,200,000.00 USD | 651.43 USD | 0.00 USD | `+26.81%` | `739,000,000.00` |
| `Live` | `Short` | `882.50` | 12,200,000.00 USD | 3,740.00 USD | 0.00 USD | `+26.95%` | `4,233,000,000.00` |
| `Live` | `Short` | `884.50` | 12,200,000.00 USD | 240.58 USD | 0.00 USD | `+27.24%` | `272,000,000.00` |
| `Live` | `Short` | `885.50` | 12,200,000.00 USD | 2,520.00 USD | 0.00 USD | `+27.39%` | `2,848,000,000.00` |
| `Live` | `Short` | `886.50` | 12,200,000.00 USD | 948.56 USD | 0.00 USD | `+27.53%` | `1,070,000,000.00` |
| `Live` | `Short` | `888.50` | 12,200,000.00 USD | 394.49 USD | 0.00 USD | `+27.82%` | `444,000,000.00` |
| `Live` | `Short` | `889.50` | 12,200,000.00 USD | 362.92 USD | 0.00 USD | `+27.96%` | `408,000,000.00` |
| `Live` | `Short` | `891.50` | 12,200,000.00 USD | 197.91 USD | 0.00 USD | `+28.25%` | `222,000,000.00` |
| `Live` | `Short` | `892.50` | 12,200,000.00 USD | 166.90 USD | 0.00 USD | `+28.39%` | `187,000,000.00` |
| `Live` | `Short` | `893.50` | 12,200,000.00 USD | 140.28 USD | 0.00 USD | `+28.54%` | `157,000,000.00` |
| `Live` | `Short` | `895.50` | 12,200,000.00 USD | 196.11 USD | 0.00 USD | `+28.82%` | `219,000,000.00` |
| `Live` | `Short` | `896.50` | 12,430,000.00 USD | 224,120.00 USD | 0.00 USD | `+28.97%` | `250,000,000,000.00` |
| `Live` | `Short` | `897.50` | 12,430,000.00 USD | 1,330.00 USD | 0.00 USD | `+29.11%` | `1,481,000,000.00` |
| `Live` | `Short` | `898.50` | 12,460,000.00 USD | 33,170.00 USD | 0.00 USD | `+29.26%` | `36,919,000,000.00` |
| `Live` | `Short` | `900.50` | 12,550,000.00 USD | 85,180.00 USD | 0.00 USD | `+29.54%` | `94,597,000,000.00` |
| `Live` | `Short` | `902.50` | 12,550,000.00 USD | 172.38 USD | 0.00 USD | `+29.83%` | `191,000,000.00` |
| `Live` | `Short` | `907.50` | 12,550,000.00 USD | 1,540.00 USD | 0.00 USD | `+30.55%` | `1,696,000,000.00` |
| `Live` | `Short` | `908.50` | 12,550,000.00 USD | 1,290.00 USD | 0.00 USD | `+30.69%` | `1,418,000,000.00` |
| `Live` | `Short` | `910.50` | 12,560,000.00 USD | 13,360.00 USD | 0.00 USD | `+30.98%` | `14,677,000,000.00` |
| `Live` | `Short` | `911.50` | 12,600,000.00 USD | 38,590.00 USD | 0.00 USD | `+31.13%` | `42,338,000,000.00` |
| `Live` | `Short` | `916.50` | 12,630,000.00 USD | 28,660.00 USD | 0.00 USD | `+31.85%` | `31,272,000,000.00` |
| `Live` | `Short` | `918.50` | 12,640,000.00 USD | 8,850.00 USD | 0.00 USD | `+32.13%` | `9,632,000,000.00` |
| `Live` | `Short` | `922.50` | 12,640,000.00 USD | 3,220.00 USD | 0.00 USD | `+32.71%` | `3,487,000,000.00` |
| `Live` | `Short` | `924.50` | 12,640,000.00 USD | 152.54 USD | 0.00 USD | `+33.00%` | `165,000,000.00` |
| `Live` | `Short` | `925.50` | 12,650,000.00 USD | 9,260.00 USD | 0.00 USD | `+33.14%` | `10,000,000,000.00` |
| `Live` | `Short` | `926.50` | 12,650,000.00 USD | 189.01 USD | 0.00 USD | `+33.28%` | `204,000,000.00` |
| `Live` | `Short` | `930.50` | 12,650,000.00 USD | 108.87 USD | 0.00 USD | `+33.86%` | `117,000,000.00` |
| `Live` | `Short` | `931.50` | 12,670,000.00 USD | 13,070.00 USD | 0.00 USD | `+34.00%` | `14,028,000,000.00` |
| `Live` | `Short` | `934.50` | 12,670,000.00 USD | 656.02 USD | 0.00 USD | `+34.44%` | `702,000,000.00` |
| `Live` | `Short` | `937.50` | 12,690,000.00 USD | 25,080.00 USD | 0.00 USD | `+34.87%` | `26,749,000,000.00` |
| `Live` | `Short` | `938.50` | 12,790,000.00 USD | 99,100.00 USD | 0.00 USD | `+35.01%` | `105,590,000,000.00` |
| `Live` | `Short` | `939.50` | 12,790,000.00 USD | 125.89 USD | 0.00 USD | `+35.15%` | `134,000,000.00` |
| `Live` | `Short` | `945.50` | 12,790,000.00 USD | 201.39 USD | 0.00 USD | `+36.02%` | `213,000,000.00` |
| `Live` | `Short` | `950.50` | 12,850,000.00 USD | 58,370.00 USD | 0.00 USD | `+36.74%` | `61,406,000,000.00` |
| `Live` | `Short` | `952.50` | 12,850,000.00 USD | 398.14 USD | 0.00 USD | `+37.02%` | `418,000,000.00` |
| `Live` | `Short` | `954.50` | 12,850,000.00 USD | 228.13 USD | 0.00 USD | `+37.31%` | `239,000,000.00` |
| `Live` | `Short` | `957.50` | 12,850,000.00 USD | 416.51 USD | 0.00 USD | `+37.74%` | `435,000,000.00` |
| `Live` | `Short` | `959.50` | 12,850,000.00 USD | 114.18 USD | 0.00 USD | `+38.03%` | `119,000,000.00` |
| `Live` | `Short` | `963.50` | 13,040,000.00 USD | 192,700.00 USD | 0.00 USD | `+38.61%` | `200,000,000,000.00` |
| `Live` | `Short` | `966.50` | 13,080,000.00 USD | 40,050.00 USD | 0.00 USD | `+39.04%` | `41,438,000,000.00` |
| `Live` | `Short` | `969.50` | 13,930,000.00 USD | 845,400.00 USD | 0.00 USD | `+39.47%` | `872,000,000,000.00` |
| `Live` | `Short` | `970.50` | 13,930,000.00 USD | 5,780.00 USD | 0.00 USD | `+39.61%` | `5,960,000,000.00` |
| `Live` | `Short` | `971.50` | 13,940,000.00 USD | 336.14 USD | 0.00 USD | `+39.76%` | `346,000,000.00` |
| `Live` | `Short` | `981.50` | 13,950,000.00 USD | 14,480.00 USD | 0.00 USD | `+41.20%` | `14,758,000,000.00` |
| `Live` | `Short` | `982.50` | 14,730,000.00 USD | 781,760.00 USD | 0.00 USD | `+41.34%` | `795,684,000,000.00` |
| `Live` | `Short` | `991.50` | 14,760,000.00 USD | 28,330.00 USD | 0.00 USD | `+42.64%` | `28,570,000,000.00` |
| `Live` | `Short` | `993.50` | 14,770,000.00 USD | 12,540.00 USD | 0.00 USD | `+42.92%` | `12,621,000,000.00` |
| `Live` | `Short` | `994.50` | 15,160,000.00 USD | 384,970.00 USD | 0.00 USD | `+43.07%` | `387,096,000,000.00` |
| `Live` | `Short` | `997.50` | 15,160,000.00 USD | 2,130.00 USD | 0.00 USD | `+43.50%` | `2,139,000,000.00` |
| `Live` | `Short` | `1001.50` | 15,310,000.00 USD | 155,460.00 USD | 0.00 USD | `+44.07%` | `155,232,000,000.00` |
| `Live` | `Short` | `1002.50` | 15,330,000.00 USD | 16,920.00 USD | 0.00 USD | `+44.22%` | `16,879,000,000.00` |
| `Live` | `Short` | `1005.50` | 15,330,000.00 USD | 1,570.00 USD | 0.00 USD | `+44.65%` | `1,564,000,000.00` |
| `Live` | `Short` | `1007.50` | 15,480,000.00 USD | 150,170.00 USD | 0.00 USD | `+44.94%` | `149,055,000,000.00` |
| `Live` | `Short` | `1011.50` | 15,490,000.00 USD | 5,230.00 USD | 0.00 USD | `+45.51%` | `5,173,000,000.00` |
| `Live` | `Short` | `1013.50` | 15,550,000.00 USD | 59,390.00 USD | 0.00 USD | `+45.80%` | `58,601,000,000.00` |
| `Live` | `Short` | `1016.50` | 16,240,000.00 USD | 695,500.00 USD | 0.00 USD | `+46.23%` | `684,207,000,000.00` |
| `Live` | `Short` | `1018.50` | 16,590,000.00 USD | 341,520.00 USD | 0.00 USD | `+46.52%` | `335,314,000,000.00` |
| `Live` | `Short` | `1019.50` | 16,590,000.00 USD | 139.67 USD | 0.00 USD | `+46.66%` | `137,000,000.00` |
| `Live` | `Short` | `1023.50` | 17,360,000.00 USD | 771,380.00 USD | 0.00 USD | `+47.24%` | `753,666,000,000.00` |
| `Live` | `Short` | `1028.50` | 18,380,000.00 USD | 1,020,000.00 USD | 0.00 USD | `+47.96%` | `995,887,000,000.00` |
| `Live` | `Short` | `1032.50` | 18,420,000.00 USD | 37,420.00 USD | 0.00 USD | `+48.53%` | `36,243,000,000.00` |
| `Live` | `Short` | `1038.50` | 18,420,000.00 USD | 201.47 USD | 0.00 USD | `+49.40%` | `194,000,000.00` |
| `Live` | `Short` | `1047.50` | 18,430,000.00 USD | 10,470.00 USD | 0.00 USD | `+50.69%` | `10,000,000,000.00` |
| `Live` | `Short` | `1048.50` | 18,430,000.00 USD | 448.76 USD | 0.00 USD | `+50.84%` | `428,000,000.00` |
| `Live` | `Short` | `1050.50` | 18,430,000.00 USD | 500.04 USD | 0.00 USD | `+51.12%` | `476,000,000.00` |
| `Live` | `Short` | `1054.50` | 18,440,000.00 USD | 11,070.00 USD | 0.00 USD | `+51.70%` | `10,494,000,000.00` |
| `Live` | `Short` | `1056.50` | 18,780,000.00 USD | 338,080.00 USD | 0.00 USD | `+51.99%` | `320,000,000,000.00` |
| `Live` | `Short` | `1057.50` | 18,810,000.00 USD | 32,220.00 USD | 0.00 USD | `+52.13%` | `30,469,000,000.00` |
| `Live` | `Short` | `1060.50` | 19,490,000.00 USD | 681,870.00 USD | 0.00 USD | `+52.56%` | `642,971,000,000.00` |
| `Live` | `Short` | `1064.50` | 19,490,000.00 USD | 1,600.00 USD | 0.00 USD | `+53.14%` | `1,500,000,000.00` |
| `Live` | `Short` | `1073.50` | 19,500,000.00 USD | 1,610.00 USD | 0.00 USD | `+54.43%` | `1,500,000,000.00` |
| `Live` | `Short` | `1088.50` | 19,500,000.00 USD | 1,930.00 USD | 0.00 USD | `+56.59%` | `1,776,000,000.00` |
| `Live` | `Short` | `1092.50` | 19,630,000.00 USD | 131,100.00 USD | 0.00 USD | `+57.16%` | `120,000,000,000.00` |
| `Live` | `Short` | `1094.50` | 19,630,000.00 USD | 4,630.00 USD | 0.00 USD | `+57.45%` | `4,234,000,000.00` |
| `Live` | `Short` | `1100.50` | 19,640,000.00 USD | 7,580.00 USD | 0.00 USD | `+58.32%` | `6,892,000,000.00` |
| `Live` | `Short` | `1104.50` | 19,640,000.00 USD | 831.69 USD | 0.00 USD | `+58.89%` | `753,000,000.00` |
| `Live` | `Short` | `1105.50` | 20,220,000.00 USD | 579,230.00 USD | 0.00 USD | `+59.04%` | `523,957,000,000.00` |
| `Live` | `Short` | `1107.50` | 20,230,000.00 USD | 4,460.00 USD | 0.00 USD | `+59.32%` | `4,027,000,000.00` |
| `Live` | `Short` | `1113.50` | 20,250,000.00 USD | 19,850.00 USD | 0.00 USD | `+60.19%` | `17,826,000,000.00` |
| `Live` | `Short` | `1115.50` | 20,300,000.00 USD | 53,890.00 USD | 0.00 USD | `+60.47%` | `48,311,000,000.00` |
| `Live` | `Short` | `1125.50` | 20,300,000.00 USD | 2,120.00 USD | 0.00 USD | `+61.91%` | `1,884,000,000.00` |
| `Live` | `Short` | `1130.50` | 20,330,000.00 USD | 28,260.00 USD | 0.00 USD | `+62.63%` | `25,000,000,000.00` |
| `Live` | `Short` | `1137.50` | 20,670,000.00 USD | 341,250.00 USD | 0.00 USD | `+63.64%` | `300,000,000,000.00` |
| `Live` | `Short` | `1138.50` | 21,810,000.00 USD | 1,140,000.00 USD | 0.00 USD | `+63.78%` | `1,000,405,000,000.00` |
| `Live` | `Short` | `1142.50` | 21,810,000.00 USD | 4,070.00 USD | 0.00 USD | `+64.36%` | `3,562,000,000.00` |
| `Live` | `Short` | `1150.50` | 21,810,000.00 USD | 128.86 USD | 0.00 USD | `+65.51%` | `112,000,000.00` |
| `Live` | `Short` | `1151.50` | 21,820,000.00 USD | 877.44 USD | 0.00 USD | `+65.65%` | `762,000,000.00` |
| `Live` | `Short` | `1153.50` | 22,180,000.00 USD | 361,330.00 USD | 0.00 USD | `+65.94%` | `313,243,000,000.00` |
| `Live` | `Short` | `1154.50` | 22,190,000.00 USD | 10,890.00 USD | 0.00 USD | `+66.08%` | `9,430,000,000.00` |
| `Live` | `Short` | `1156.50` | 22,420,000.00 USD | 231,450.00 USD | 0.00 USD | `+66.37%` | `200,134,000,000.00` |
| `Live` | `Short` | `1160.50` | 22,640,000.00 USD | 216,400.00 USD | 0.00 USD | `+66.95%` | `186,472,000,000.00` |
| `Live` | `Short` | `1169.50` | 22,640,000.00 USD | 367.22 USD | 0.00 USD | `+68.24%` | `314,000,000.00` |
| `Live` | `Short` | `1178.50` | 22,640,000.00 USD | 1,820.00 USD | 0.00 USD | `+69.54%` | `1,542,000,000.00` |
| `Live` | `Short` | `1186.50` | 22,640,000.00 USD | 158.99 USD | 0.00 USD | `+70.69%` | `134,000,000.00` |
| `Live` | `Short` | `1197.50` | 22,640,000.00 USD | 463.43 USD | 0.00 USD | `+72.27%` | `387,000,000.00` |
| `Live` | `Short` | `1208.50` | 22,640,000.00 USD | 385.51 USD | 0.00 USD | `+73.85%` | `319,000,000.00` |
| `Live` | `Short` | `1211.50` | 22,670,000.00 USD | 30,270.00 USD | 0.00 USD | `+74.28%` | `24,982,000,000.00` |
| `Live` | `Short` | `1215.50` | 22,710,000.00 USD | 45,100.00 USD | 0.00 USD | `+74.86%` | `37,100,000,000.00` |
| `Live` | `Short` | `1225.50` | 22,720,000.00 USD | 1,030.00 USD | 0.00 USD | `+76.30%` | `841,000,000.00` |
| `Live` | `Short` | `1236.50` | 22,770,000.00 USD | 54,470.00 USD | 0.00 USD | `+77.88%` | `44,051,000,000.00` |
| `Live` | `Short` | `1237.50` | 22,830,000.00 USD | 63,700.00 USD | 0.00 USD | `+78.02%` | `51,476,000,000.00` |
| `Live` | `Short` | `1252.50` | 22,830,000.00 USD | 100.20 USD | 0.00 USD | `+80.18%` | `80,000,000.00` |
| `Live` | `Short` | `1268.50` | 22,830,000.00 USD | 202.96 USD | 0.00 USD | `+82.48%` | `160,000,000.00` |
| `Live` | `Short` | `1276.50` | 22,950,000.00 USD | 114,890.00 USD | 0.00 USD | `+83.63%` | `90,000,000,000.00` |
| `Live` | `Short` | `1278.50` | 22,950,000.00 USD | 346.47 USD | 0.00 USD | `+83.92%` | `271,000,000.00` |
| `Live` | `Short` | `1284.50` | 23,010,000.00 USD | 65,600.00 USD | 0.00 USD | `+84.79%` | `51,070,000,000.00` |
| `Live` | `Short` | `1287.50` | 23,020,000.00 USD | 5,140.00 USD | 0.00 USD | `+85.22%` | `3,994,000,000.00` |
| `Live` | `Short` | `1295.50` | 23,020,000.00 USD | 181.37 USD | 0.00 USD | `+86.37%` | `140,000,000.00` |
| `Live` | `Short` | `1308.50` | 23,020,000.00 USD | 100.75 USD | 0.00 USD | `+88.24%` | `77,000,000.00` |
| `Live` | `Short` | `1317.50` | 23,190,000.00 USD | 167,170.00 USD | 0.00 USD | `+89.53%` | `126,881,000,000.00` |
| `Live` | `Short` | `1320.50` | 23,200,000.00 USD | 14,140.00 USD | 0.00 USD | `+89.96%` | `10,710,000,000.00` |
| `Live` | `Short` | `1331.50` | 23,240,000.00 USD | 36,800.00 USD | 0.00 USD | `+91.55%` | `27,640,000,000.00` |
| `Live` | `Short` | `1337.50` | 23,250,000.00 USD | 8,300.00 USD | 0.00 USD | `+92.41%` | `6,204,000,000.00` |
| `Live` | `Short` | `1346.50` | 23,250,000.00 USD | 651.71 USD | 0.00 USD | `+93.70%` | `484,000,000.00` |
| `Live` | `Short` | `1348.50` | 23,290,000.00 USD | 40,450.00 USD | 0.00 USD | `+93.99%` | `30,000,000,000.00` |
| `Live` | `Short` | `1354.50` | 23,300,000.00 USD | 13,540.00 USD | 0.00 USD | `+94.86%` | `10,000,000,000.00` |
| `Live` | `Short` | `1358.50` | 23,430,000.00 USD | 129,910.00 USD | 0.00 USD | `+95.43%` | `95,630,000,000.00` |
| `Live` | `Short` | `1361.50` | 23,590,000.00 USD | 156,500.00 USD | 0.00 USD | `+95.86%` | `114,948,000,000.00` |
| `Live` | `Short` | `1364.50` | 23,590,000.00 USD | 255.16 USD | 0.00 USD | `+96.29%` | `187,000,000.00` |
| `Live` | `Short` | `1372.50` | 23,590,000.00 USD | 1,310.00 USD | 0.00 USD | `+97.45%` | `958,000,000.00` |
| `Live` | `Short` | `1375.50` | 23,670,000.00 USD | 76,140.00 USD | 0.00 USD | `+97.88%` | `55,351,000,000.00` |
| `Live` | `Short` | `1380.50` | 24,420,000.00 USD | 750,070.00 USD | 0.00 USD | `+98.60%` | `543,331,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `150.50` | 755,660.00 USD | 0.00 USD | 475.73 USD | `-78.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `300.50` | 755,180.00 USD | 0.00 USD | 2,400.00 USD | `-56.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `333.50` | 752,780.00 USD | 0.00 USD | 333.50 USD | `-52.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `350.50` | 752,440.00 USD | 0.00 USD | 127.58 USD | `-49.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `369.50` | 752,320.00 USD | 0.00 USD | 5,170.00 USD | `-46.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `400.50` | 747,140.00 USD | 0.00 USD | 17,290.00 USD | `-42.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `410.50` | 729,850.00 USD | 0.00 USD | 25,210.00 USD | `-40.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `412.50` | 704,650.00 USD | 0.00 USD | 4,550.00 USD | `-40.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `455.50` | 700,100.00 USD | 0.00 USD | 698.74 USD | `-34.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `469.50` | 699,400.00 USD | 0.00 USD | 3,550.00 USD | `-32.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `486.50` | 695,850.00 USD | 0.00 USD | 100.71 USD | `-30.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `487.50` | 695,750.00 USD | 0.00 USD | 6,600.00 USD | `-29.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `488.50` | 689,150.00 USD | 0.00 USD | 2,490.00 USD | `-29.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `498.50` | 686,670.00 USD | 0.00 USD | 163.01 USD | `-28.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `499.50` | 686,500.00 USD | 0.00 USD | 214.78 USD | `-28.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `500.50` | 686,290.00 USD | 0.00 USD | 168.67 USD | `-28.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `503.50` | 686,120.00 USD | 0.00 USD | 47,830.00 USD | `-27.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `509.50` | 638,290.00 USD | 0.00 USD | 185.97 USD | `-26.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `515.50` | 638,100.00 USD | 0.00 USD | 1,030.00 USD | `-25.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `516.50` | 637,070.00 USD | 0.00 USD | 125.51 USD | `-25.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `517.50` | 636,940.00 USD | 0.00 USD | 280.49 USD | `-25.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `521.50` | 636,660.00 USD | 0.00 USD | 258.14 USD | `-24.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `524.50` | 636,410.00 USD | 0.00 USD | 8,170.00 USD | `-24.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `528.50` | 628,230.00 USD | 0.00 USD | 485.16 USD | `-23.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `534.50` | 627,750.00 USD | 0.00 USD | 4,650.00 USD | `-23.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `538.50` | 623,100.00 USD | 0.00 USD | 1,680.00 USD | `-22.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `540.50` | 621,430.00 USD | 0.00 USD | 2,490.00 USD | `-22.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `554.50` | 618,940.00 USD | 0.00 USD | 1,190.00 USD | `-20.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `555.50` | 617,750.00 USD | 0.00 USD | 17,280.00 USD | `-20.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `558.50` | 600,480.00 USD | 0.00 USD | 51,260.00 USD | `-19.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `560.50` | 549,220.00 USD | 0.00 USD | 292.02 USD | `-19.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `561.50` | 548,920.00 USD | 0.00 USD | 748.48 USD | `-19.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `566.50` | 548,180.00 USD | 0.00 USD | 566.50 USD | `-18.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `567.50` | 547,610.00 USD | 0.00 USD | 126.55 USD | `-18.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `568.50` | 547,480.00 USD | 0.00 USD | 5,680.00 USD | `-18.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `570.50` | 541,800.00 USD | 0.00 USD | 4,760.00 USD | `-17.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `571.50` | 537,040.00 USD | 0.00 USD | 1,700.00 USD | `-17.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `573.50` | 535,340.00 USD | 0.00 USD | 291.91 USD | `-17.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `575.50` | 535,050.00 USD | 0.00 USD | 469.61 USD | `-17.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `576.50` | 534,580.00 USD | 0.00 USD | 289.98 USD | `-17.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `577.50` | 534,290.00 USD | 0.00 USD | 285.86 USD | `-16.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `579.50` | 534,000.00 USD | 0.00 USD | 289.17 USD | `-16.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `580.50` | 533,710.00 USD | 0.00 USD | 6,750.00 USD | `-16.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `581.50` | 526,960.00 USD | 0.00 USD | 289.59 USD | `-16.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `583.50` | 526,670.00 USD | 0.00 USD | 287.67 USD | `-16.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `584.50` | 526,390.00 USD | 0.00 USD | 763.94 USD | `-15.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `585.50` | 525,620.00 USD | 0.00 USD | 883.52 USD | `-15.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `586.50` | 524,740.00 USD | 0.00 USD | 1,170.00 USD | `-15.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `587.50` | 523,570.00 USD | 0.00 USD | 289.05 USD | `-15.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `588.50` | 523,280.00 USD | 0.00 USD | 287.78 USD | `-15.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `589.50` | 522,990.00 USD | 0.00 USD | 7,990.00 USD | `-15.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `590.50` | 515,000.00 USD | 0.00 USD | 721.00 USD | `-15.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `591.50` | 514,280.00 USD | 0.00 USD | 282.74 USD | `-14.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `592.50` | 514,000.00 USD | 0.00 USD | 170.05 USD | `-14.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `594.50` | 513,830.00 USD | 0.00 USD | 286.55 USD | `-14.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `598.50` | 513,540.00 USD | 0.00 USD | 244.79 USD | `-13.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `600.50` | 513,290.00 USD | 0.00 USD | 38,030.00 USD | `-13.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `601.50` | 475,260.00 USD | 0.00 USD | 1,590.00 USD | `-13.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `605.50` | 473,670.00 USD | 0.00 USD | 2,610.00 USD | `-12.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `606.50` | 471,060.00 USD | 0.00 USD | 103.11 USD | `-12.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `611.50` | 470,960.00 USD | 0.00 USD | 170.00 USD | `-12.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `612.50` | 470,790.00 USD | 0.00 USD | 1,380.00 USD | `-11.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `614.50` | 469,410.00 USD | 0.00 USD | 269.15 USD | `-11.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `615.50` | 469,140.00 USD | 0.00 USD | 1,740.00 USD | `-11.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `616.50` | 467,400.00 USD | 0.00 USD | 120.83 USD | `-11.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `620.50` | 467,280.00 USD | 0.00 USD | 105.49 USD | `-10.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `621.50` | 467,170.00 USD | 0.00 USD | 1,470.00 USD | `-10.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `625.50` | 465,710.00 USD | 0.00 USD | 170.76 USD | `-10.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `629.50` | 465,540.00 USD | 0.00 USD | 1,440.00 USD | `-9.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `630.50` | 464,090.00 USD | 0.00 USD | 276.16 USD | `-9.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `632.50` | 463,820.00 USD | 0.00 USD | 204.30 USD | `-9.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `633.50` | 463,610.00 USD | 0.00 USD | 4,570.00 USD | `-8.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `634.50` | 459,040.00 USD | 0.00 USD | 2,550.00 USD | `-8.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `636.50` | 456,490.00 USD | 0.00 USD | 31,820.00 USD | `-8.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `638.50` | 424,660.00 USD | 0.00 USD | 560.60 USD | `-8.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `639.50` | 424,100.00 USD | 0.00 USD | 304.40 USD | `-8.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `642.50` | 423,800.00 USD | 0.00 USD | 1,280.00 USD | `-7.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `644.50` | 422,510.00 USD | 0.00 USD | 3,790.00 USD | `-7.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `645.50` | 418,720.00 USD | 0.00 USD | 154.27 USD | `-7.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `646.50` | 418,570.00 USD | 0.00 USD | 971.04 USD | `-7.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `649.50` | 417,600.00 USD | 0.00 USD | 103,200.00 USD | `-6.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `650.50` | 314,390.00 USD | 0.00 USD | 82,070.00 USD | `-6.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `651.50` | 232,320.00 USD | 0.00 USD | 4,270.00 USD | `-6.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `653.50` | 228,050.00 USD | 0.00 USD | 2,020.00 USD | `-5.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `654.50` | 226,030.00 USD | 0.00 USD | 308.92 USD | `-5.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `655.50` | 225,720.00 USD | 0.00 USD | 13,180.00 USD | `-5.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `656.50` | 212,540.00 USD | 0.00 USD | 456.27 USD | `-5.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `657.50` | 212,080.00 USD | 0.00 USD | 823.19 USD | `-5.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `658.50` | 211,260.00 USD | 0.00 USD | 1,320.00 USD | `-5.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `659.50` | 209,940.00 USD | 0.00 USD | 3,130.00 USD | `-5.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `660.50` | 206,820.00 USD | 0.00 USD | 198.15 USD | `-4.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `661.50` | 206,620.00 USD | 0.00 USD | 7,850.00 USD | `-4.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `662.50` | 198,760.00 USD | 0.00 USD | 1,780.00 USD | `-4.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `663.50` | 196,990.00 USD | 0.00 USD | 2,840.00 USD | `-4.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `664.50` | 194,150.00 USD | 0.00 USD | 154.83 USD | `-4.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `665.50` | 193,990.00 USD | 0.00 USD | 113.14 USD | `-4.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `666.50` | 193,880.00 USD | 0.00 USD | 4,920.00 USD | `-4.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `668.50` | 188,960.00 USD | 0.00 USD | 2,160.00 USD | `-3.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `669.50` | 186,800.00 USD | 0.00 USD | 2,940.00 USD | `-3.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `670.50` | 183,860.00 USD | 0.00 USD | 9,770.00 USD | `-3.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `672.50` | 174,090.00 USD | 0.00 USD | 8,610.00 USD | `-3.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `673.50` | 165,480.00 USD | 0.00 USD | 2,090.00 USD | `-3.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `674.50` | 163,390.00 USD | 0.00 USD | 2,350.00 USD | `-2.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `675.50` | 161,040.00 USD | 0.00 USD | 1,760.00 USD | `-2.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `676.50` | 159,280.00 USD | 0.00 USD | 56,050.00 USD | `-2.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `678.50` | 103,220.00 USD | 0.00 USD | 3,360.00 USD | `-2.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `679.50` | 99,870.00 USD | 0.00 USD | 175.31 USD | `-2.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `680.50` | 99,690.00 USD | 0.00 USD | 490.64 USD | `-2.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `681.50` | 99,200.00 USD | 0.00 USD | 146.52 USD | `-1.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `683.50` | 99,060.00 USD | 0.00 USD | 24,240.00 USD | `-1.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `684.50` | 74,820.00 USD | 0.00 USD | 49,290.00 USD | `-1.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `685.50` | 25,520.00 USD | 0.00 USD | 7,610.00 USD | `-1.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `687.50` | 17,910.00 USD | 0.00 USD | 371.25 USD | `-1.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `688.50` | 17,540.00 USD | 0.00 USD | 1,150.00 USD | `-0.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `689.50` | 16,390.00 USD | 0.00 USD | 3,080.00 USD | `-0.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `690.50` | 13,310.00 USD | 0.00 USD | 1,300.00 USD | `-0.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `691.50` | 12,010.00 USD | 0.00 USD | 691.50 USD | `-0.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `692.50` | 11,320.00 USD | 0.00 USD | 2,530.00 USD | `-0.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `693.50` | 8,790.00 USD | 0.00 USD | 8,410.00 USD | `-0.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `694.50` | 374.34 USD | 0.00 USD | 374.34 USD | `-0.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `695.50` | 30,620.00 USD | 30,620.00 USD | 0.00 USD | `+0.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `696.50` | 40,310.00 USD | 9,690.00 USD | 0.00 USD | `+0.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `697.50` | 44,650.00 USD | 4,340.00 USD | 0.00 USD | `+0.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `698.50` | 50,110.00 USD | 5,460.00 USD | 0.00 USD | `+0.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `699.50` | 53,410.00 USD | 3,300.00 USD | 0.00 USD | `+0.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `700.50` | 56,350.00 USD | 2,940.00 USD | 0.00 USD | `+0.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `701.50` | 184,780.00 USD | 128,430.00 USD | 0.00 USD | `+0.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `702.50` | 191,740.00 USD | 6,960.00 USD | 0.00 USD | `+1.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `703.50` | 301,830.00 USD | 110,090.00 USD | 0.00 USD | `+1.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `704.50` | 388,740.00 USD | 86,910.00 USD | 0.00 USD | `+1.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `705.50` | 421,780.00 USD | 33,050.00 USD | 0.00 USD | `+1.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `706.50` | 463,030.00 USD | 41,240.00 USD | 0.00 USD | `+1.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `707.50` | 537,170.00 USD | 74,140.00 USD | 0.00 USD | `+1.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `708.50` | 1,120,000.00 USD | 582,020.00 USD | 0.00 USD | `+1.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `709.50` | 1,120,000.00 USD | 2,240.00 USD | 0.00 USD | `+2.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `710.50` | 1,140,000.00 USD | 23,320.00 USD | 0.00 USD | `+2.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `711.50` | 1,150,000.00 USD | 6,510.00 USD | 0.00 USD | `+2.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `712.50` | 1,270,000.00 USD | 116,280.00 USD | 0.00 USD | `+2.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `713.50` | 1,470,000.00 USD | 206,290.00 USD | 0.00 USD | `+2.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `714.50` | 2,150,000.00 USD | 679,520.00 USD | 0.00 USD | `+2.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `715.50` | 2,760,000.00 USD | 609,010.00 USD | 0.00 USD | `+2.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `716.50` | 2,770,000.00 USD | 3,090.00 USD | 0.00 USD | `+3.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `717.50` | 2,770,000.00 USD | 138.48 USD | 0.00 USD | `+3.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `718.50` | 2,900,000.00 USD | 133,310.00 USD | 0.00 USD | `+3.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `719.50` | 3,110,000.00 USD | 215,040.00 USD | 0.00 USD | `+3.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `720.50` | 3,470,000.00 USD | 352,290.00 USD | 0.00 USD | `+3.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `721.50` | 3,470,000.00 USD | 704.18 USD | 0.00 USD | `+3.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `722.50` | 3,490,000.00 USD | 18,480.00 USD | 0.00 USD | `+3.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `723.50` | 3,490,000.00 USD | 7,240.00 USD | 0.00 USD | `+4.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `724.50` | 3,500,000.00 USD | 9,620.00 USD | 0.00 USD | `+4.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `725.50` | 3,570,000.00 USD | 67,220.00 USD | 0.00 USD | `+4.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `726.50` | 3,570,000.00 USD | 470.77 USD | 0.00 USD | `+4.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `727.50` | 3,620,000.00 USD | 47,190.00 USD | 0.00 USD | `+4.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `728.50` | 3,620,000.00 USD | 235.31 USD | 0.00 USD | `+4.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `729.50` | 3,620,000.00 USD | 6,820.00 USD | 0.00 USD | `+4.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `730.50` | 3,630,000.00 USD | 1,640.00 USD | 0.00 USD | `+5.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `731.50` | 3,640,000.00 USD | 16,270.00 USD | 0.00 USD | `+5.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `732.50` | 3,690,000.00 USD | 52,090.00 USD | 0.00 USD | `+5.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `733.50` | 3,740,000.00 USD | 49,550.00 USD | 0.00 USD | `+5.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `734.50` | 3,750,000.00 USD | 2,290.00 USD | 0.00 USD | `+5.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `735.50` | 3,750,000.00 USD | 1,820.00 USD | 0.00 USD | `+5.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `736.50` | 3,750,000.00 USD | 2,810.00 USD | 0.00 USD | `+5.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `737.50` | 3,750,000.00 USD | 685.88 USD | 0.00 USD | `+6.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `738.50` | 3,750,000.00 USD | 1,070.00 USD | 0.00 USD | `+6.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `739.50` | 3,750,000.00 USD | 790.53 USD | 0.00 USD | `+6.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `740.50` | 3,750,000.00 USD | 1,220.00 USD | 0.00 USD | `+6.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `741.50` | 3,760,000.00 USD | 1,590.00 USD | 0.00 USD | `+6.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `742.50` | 4,000,000.00 USD | 247,900.00 USD | 0.00 USD | `+6.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `743.50` | 4,000,000.00 USD | 897.40 USD | 0.00 USD | `+6.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `744.50` | 4,160,000.00 USD | 155,450.00 USD | 0.00 USD | `+7.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `745.50` | 4,160,000.00 USD | 1,000.00 USD | 0.00 USD | `+7.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `746.50` | 4,160,000.00 USD | 1,920.00 USD | 0.00 USD | `+7.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `747.50` | 4,160,000.00 USD | 301.24 USD | 0.00 USD | `+7.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `748.50` | 4,170,000.00 USD | 2,950.00 USD | 0.00 USD | `+7.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `749.50` | 4,170,000.00 USD | 999.83 USD | 0.00 USD | `+7.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `750.50` | 4,170,000.00 USD | 123.83 USD | 0.00 USD | `+7.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `751.50` | 4,170,000.00 USD | 1,010.00 USD | 0.00 USD | `+8.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `752.50` | 4,170,000.00 USD | 2,730.00 USD | 0.00 USD | `+8.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `753.50` | 4,170,000.00 USD | 327.77 USD | 0.00 USD | `+8.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `754.50` | 4,170,000.00 USD | 258.79 USD | 0.00 USD | `+8.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `755.50` | 4,170,000.00 USD | 979.13 USD | 0.00 USD | `+8.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `756.50` | 4,180,000.00 USD | 4,980.00 USD | 0.00 USD | `+8.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `757.50` | 4,300,000.00 USD | 121,650.00 USD | 0.00 USD | `+8.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `758.50` | 4,300,000.00 USD | 136.53 USD | 0.00 USD | `+9.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `759.50` | 4,300,000.00 USD | 253.67 USD | 0.00 USD | `+9.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `760.50` | 4,300,000.00 USD | 109.51 USD | 0.00 USD | `+9.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `761.50` | 4,300,000.00 USD | 1,910.00 USD | 0.00 USD | `+9.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `762.50` | 4,300,000.00 USD | 147.93 USD | 0.00 USD | `+9.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `763.50` | 4,580,000.00 USD | 279,950.00 USD | 0.00 USD | `+9.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `764.50` | 4,580,000.00 USD | 2,870.00 USD | 0.00 USD | `+9.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `765.50` | 4,630,000.00 USD | 43,490.00 USD | 0.00 USD | `+10.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `766.50` | 4,630,000.00 USD | 331.13 USD | 0.00 USD | `+10.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `767.50` | 4,630,000.00 USD | 1,360.00 USD | 0.00 USD | `+10.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `768.50` | 4,630,000.00 USD | 1,230.00 USD | 0.00 USD | `+10.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `769.50` | 4,630,000.00 USD | 171.60 USD | 0.00 USD | `+10.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `770.50` | 4,860,000.00 USD | 231,150.00 USD | 0.00 USD | `+10.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `771.50` | 4,860,000.00 USD | 1,370.00 USD | 0.00 USD | `+10.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `772.50` | 4,860,000.00 USD | 242.56 USD | 0.00 USD | `+11.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `773.50` | 4,870,000.00 USD | 1,240.00 USD | 0.00 USD | `+11.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `774.50` | 4,880,000.00 USD | 9,680.00 USD | 0.00 USD | `+11.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `775.50` | 4,880,000.00 USD | 853.05 USD | 0.00 USD | `+11.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `776.50` | 4,890,000.00 USD | 14,230.00 USD | 0.00 USD | `+11.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `777.50` | 4,910,000.00 USD | 23,920.00 USD | 0.00 USD | `+11.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `778.50` | 4,920,000.00 USD | 3,820.00 USD | 0.00 USD | `+11.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `779.50` | 4,920,000.00 USD | 6,420.00 USD | 0.00 USD | `+12.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `780.50` | 4,930,000.00 USD | 9,690.00 USD | 0.00 USD | `+12.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `781.50` | 4,940,000.00 USD | 2,290.00 USD | 0.00 USD | `+12.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `782.50` | 4,940,000.00 USD | 1,620.00 USD | 0.00 USD | `+12.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `783.50` | 5,350,000.00 USD | 407,870.00 USD | 0.00 USD | `+12.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `784.50` | 5,350,000.00 USD | 106.69 USD | 0.00 USD | `+12.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `785.50` | 5,350,000.00 USD | 559.28 USD | 0.00 USD | `+13.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `786.50` | 5,350,000.00 USD | 366.51 USD | 0.00 USD | `+13.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `787.50` | 5,350,000.00 USD | 393.75 USD | 0.00 USD | `+13.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `788.50` | 5,350,000.00 USD | 133.26 USD | 0.00 USD | `+13.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `790.50` | 5,350,000.00 USD | 4,190.00 USD | 0.00 USD | `+13.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `791.50` | 5,350,000.00 USD | 704.44 USD | 0.00 USD | `+13.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `792.50` | 5,360,000.00 USD | 4,360.00 USD | 0.00 USD | `+14.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `793.50` | 5,360,000.00 USD | 1,450.00 USD | 0.00 USD | `+14.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `794.50` | 5,360,000.00 USD | 3,630.00 USD | 0.00 USD | `+14.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `795.50` | 5,360,000.00 USD | 3,040.00 USD | 0.00 USD | `+14.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `796.50` | 5,370,000.00 USD | 154.52 USD | 0.00 USD | `+14.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `799.50` | 5,370,000.00 USD | 2,370.00 USD | 0.00 USD | `+15.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `800.50` | 5,370,000.00 USD | 194.52 USD | 0.00 USD | `+15.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `803.50` | 5,370,000.00 USD | 803.50 USD | 0.00 USD | `+15.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `805.50` | 5,370,000.00 USD | 179.63 USD | 0.00 USD | `+15.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `806.50` | 5,370,000.00 USD | 1,300.00 USD | 0.00 USD | `+16.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `808.50` | 5,370,000.00 USD | 3,190.00 USD | 0.00 USD | `+16.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `809.50` | 5,370,000.00 USD | 242.04 USD | 0.00 USD | `+16.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `810.50` | 5,390,000.00 USD | 15,790.00 USD | 0.00 USD | `+16.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `811.50` | 5,390,000.00 USD | 374.10 USD | 0.00 USD | `+16.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `812.50` | 5,390,000.00 USD | 844.19 USD | 0.00 USD | `+16.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `813.50` | 5,390,000.00 USD | 109.82 USD | 0.00 USD | `+17.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `814.50` | 5,390,000.00 USD | 3,210.00 USD | 0.00 USD | `+17.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `816.50` | 5,390,000.00 USD | 984.70 USD | 0.00 USD | `+17.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `817.50` | 5,390,000.00 USD | 162.68 USD | 0.00 USD | `+17.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `820.50` | 5,400,000.00 USD | 8,230.00 USD | 0.00 USD | `+18.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `824.50` | 5,400,000.00 USD | 408.13 USD | 0.00 USD | `+18.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `825.50` | 5,730,000.00 USD | 330,200.00 USD | 0.00 USD | `+18.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `826.50` | 5,730,000.00 USD | 672.77 USD | 0.00 USD | `+18.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `827.50` | 5,730,000.00 USD | 276.38 USD | 0.00 USD | `+19.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `828.50` | 5,740,000.00 USD | 1,800.00 USD | 0.00 USD | `+19.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `830.50` | 5,770,000.00 USD | 35,850.00 USD | 0.00 USD | `+19.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `833.50` | 5,770,000.00 USD | 1,200.00 USD | 0.00 USD | `+19.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `835.50` | 5,770,000.00 USD | 187.15 USD | 0.00 USD | `+20.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `836.50` | 5,770,000.00 USD | 372.24 USD | 0.00 USD | `+20.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `837.50` | 5,770,000.00 USD | 326.62 USD | 0.00 USD | `+20.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `839.50` | 5,770,000.00 USD | 296.34 USD | 0.00 USD | `+20.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `840.50` | 5,780,000.00 USD | 441.26 USD | 0.00 USD | `+20.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `841.50` | 5,780,000.00 USD | 329.87 USD | 0.00 USD | `+21.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `843.50` | 5,780,000.00 USD | 425.97 USD | 0.00 USD | `+21.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `844.50` | 5,780,000.00 USD | 1,770.00 USD | 0.00 USD | `+21.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `850.50` | 5,780,000.00 USD | 2,550.00 USD | 0.00 USD | `+22.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `851.50` | 5,790,000.00 USD | 11,650.00 USD | 0.00 USD | `+22.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `852.50` | 5,790,000.00 USD | 102.30 USD | 0.00 USD | `+22.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `854.50` | 5,790,000.00 USD | 137.57 USD | 0.00 USD | `+22.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `857.50` | 5,790,000.00 USD | 1,200.00 USD | 0.00 USD | `+23.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `860.50` | 5,790,000.00 USD | 674.63 USD | 0.00 USD | `+23.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `862.50` | 5,800,000.00 USD | 1,200.00 USD | 0.00 USD | `+24.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `863.50` | 5,800,000.00 USD | 874.73 USD | 0.00 USD | `+24.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `864.50` | 5,800,000.00 USD | 2,970.00 USD | 0.00 USD | `+24.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `865.50` | 5,800,000.00 USD | 3,460.00 USD | 0.00 USD | `+24.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `868.50` | 5,800,000.00 USD | 2,610.00 USD | 0.00 USD | `+24.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `870.50` | 5,810,000.00 USD | 228.07 USD | 0.00 USD | `+25.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `872.50` | 5,810,000.00 USD | 1,110.00 USD | 0.00 USD | `+25.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `874.50` | 5,810,000.00 USD | 582.42 USD | 0.00 USD | `+25.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `884.50` | 5,860,000.00 USD | 54,820.00 USD | 0.00 USD | `+27.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `888.50` | 5,860,000.00 USD | 266.55 USD | 0.00 USD | `+27.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `890.50` | 5,860,000.00 USD | 690.14 USD | 0.00 USD | `+28.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `891.50` | 5,860,000.00 USD | 605.33 USD | 0.00 USD | `+28.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `900.50` | 5,920,000.00 USD | 53,820.00 USD | 0.00 USD | `+29.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `914.50` | 5,920,000.00 USD | 4,150.00 USD | 0.00 USD | `+31.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `917.50` | 5,920,000.00 USD | 533.99 USD | 0.00 USD | `+31.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `919.50` | 5,920,000.00 USD | 166.43 USD | 0.00 USD | `+32.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `920.50` | 5,920,000.00 USD | 463.01 USD | 0.00 USD | `+32.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `926.50` | 5,920,000.00 USD | 320.57 USD | 0.00 USD | `+33.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `929.50` | 5,950,000.00 USD | 24,800.00 USD | 0.00 USD | `+33.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `930.50` | 5,950,000.00 USD | 552.72 USD | 0.00 USD | `+33.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `933.50` | 5,950,000.00 USD | 196.03 USD | 0.00 USD | `+34.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `935.50` | 5,950,000.00 USD | 287.20 USD | 0.00 USD | `+34.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `958.50` | 5,950,000.00 USD | 782.14 USD | 0.00 USD | `+37.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `959.50` | 5,950,000.00 USD | 498.94 USD | 0.00 USD | `+38.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `965.50` | 5,950,000.00 USD | 1,930.00 USD | 0.00 USD | `+38.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `977.50` | 5,950,000.00 USD | 293.25 USD | 0.00 USD | `+40.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `980.50` | 5,950,000.00 USD | 1,300.00 USD | 0.00 USD | `+41.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `981.50` | 5,950,000.00 USD | 109.93 USD | 0.00 USD | `+41.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `984.50` | 5,950,000.00 USD | 439.09 USD | 0.00 USD | `+41.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `987.50` | 5,960,000.00 USD | 2,590.00 USD | 0.00 USD | `+42.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `997.50` | 5,960,000.00 USD | 1,820.00 USD | 0.00 USD | `+43.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `998.50` | 5,960,000.00 USD | 3,990.00 USD | 0.00 USD | `+43.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `999.50` | 5,960,000.00 USD | 938.53 USD | 0.00 USD | `+43.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1000.50` | 5,980,000.00 USD | 11,810.00 USD | 0.00 USD | `+43.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1017.50` | 5,980,000.00 USD | 203.50 USD | 0.00 USD | `+46.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1045.50` | 5,980,000.00 USD | 195.51 USD | 0.00 USD | `+50.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1100.50` | 5,980,000.00 USD | 278.43 USD | 0.00 USD | `+58.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1111.50` | 5,980,000.00 USD | 555.75 USD | 0.00 USD | `+59.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1200.50` | 6,040,000.00 USD | 62,330.00 USD | 0.00 USD | `+72.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1202.50` | 6,040,000.00 USD | 1,250.00 USD | 0.00 USD | `+72.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1226.50` | 6,040,000.00 USD | 235.49 USD | 0.00 USD | `+76.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1230.50` | 6,040,000.00 USD | 3,580.00 USD | 0.00 USD | `+77.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1250.50` | 6,040,000.00 USD | 421.42 USD | 0.00 USD | `+79.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1280.50` | 6,050,000.00 USD | 3,750.00 USD | 0.00 USD | `+84.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1297.50` | 6,050,000.00 USD | 133.64 USD | 0.00 USD | `+86.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1300.50` | 6,050,000.00 USD | 685.36 USD | 0.00 USD | `+87.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1330.50` | 6,110,000.00 USD | 58,230.00 USD | 0.00 USD | `+91.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1340.50` | 6,190,000.00 USD | 80,850.00 USD | 0.00 USD | `+92.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1360.50` | 6,190,000.00 USD | 6,210.00 USD | 0.00 USD | `+95.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1363.50` | 6,190,000.00 USD | 349.06 USD | 0.00 USD | `+96.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1370.50` | 6,200,000.00 USD | 1,060.00 USD | 0.00 USD | `+97.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1372.50` | 6,210,000.00 USD | 19,210.00 USD | 0.00 USD | `+97.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1389.50` | 6,220,000.00 USD | 425.19 USD | 0.00 USD | `+99.89%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `604.30` | 30,240,000.00 USD | 0.00 USD | 30,240,000.00 USD | 53,570.00 USD | 2,300.00 USD | 15,090.00 USD |
| `1D` | `605.50` | 30,170,000.00 USD | 0.00 USD | 30,170,000.00 USD | 38,430.00 USD | 2,340.00 USD | 3,690.00 USD |
| `1D` | `606.70` | 30,130,000.00 USD | 0.00 USD | 30,130,000.00 USD | 20,120.00 USD | 8,630.00 USD | 17,660.00 USD |
| `1D` | `607.90` | 30,080,000.00 USD | 0.00 USD | 30,080,000.00 USD | 44,630.00 USD | 4,230.00 USD | 2,800.00 USD |
| `1D` | `609.10` | 30,030,000.00 USD | 0.00 USD | 30,030,000.00 USD | 23,150.00 USD | 1,920.00 USD | 1,710.00 USD |
| `1D` | `615.10` | 30,000,000.00 USD | 0.00 USD | 30,000,000.00 USD | 0.00 USD | 0.00 USD | 295,360.00 USD |
| `1D` | `617.50` | 29,710,000.00 USD | 0.00 USD | 29,710,000.00 USD | 290,320.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `619.90` | 29,420,000.00 USD | 0.00 USD | 29,420,000.00 USD | 0.00 USD | 33,270.00 USD | 0.00 USD |
| `1D` | `621.10` | 29,380,000.00 USD | 0.00 USD | 29,380,000.00 USD | 175,630.00 USD | 35,090.00 USD | 0.00 USD |
| `1D` | `623.50` | 29,170,000.00 USD | 0.00 USD | 29,170,000.00 USD | 460,160.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `624.70` | 28,710,000.00 USD | 0.00 USD | 28,710,000.00 USD | 238,630.00 USD | 31,450.00 USD | 274,040.00 USD |
| `1D` | `625.90` | 28,170,000.00 USD | 0.00 USD | 28,170,000.00 USD | 224,870.00 USD | 44,960.00 USD | 0.00 USD |
| `1D` | `627.10` | 27,900,000.00 USD | 0.00 USD | 27,900,000.00 USD | 186,500.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `630.70` | 27,710,000.00 USD | 0.00 USD | 27,710,000.00 USD | 0.00 USD | 0.00 USD | 254,760.00 USD |
| `1D` | `631.90` | 27,460,000.00 USD | 0.00 USD | 27,460,000.00 USD | 0.00 USD | 0.00 USD | 403,180.00 USD |
| `1D` | `633.10` | 27,050,000.00 USD | 0.00 USD | 27,050,000.00 USD | 461,240.00 USD | 42,940.00 USD | 0.00 USD |
| `1D` | `636.70` | 26,550,000.00 USD | 0.00 USD | 26,550,000.00 USD | 101,910.00 USD | 40,910.00 USD | 236,370.00 USD |
| `1D` | `639.10` | 26,170,000.00 USD | 0.00 USD | 26,170,000.00 USD | 184,100.00 USD | 37,610.00 USD | 0.00 USD |
| `1D` | `640.30` | 25,950,000.00 USD | 0.00 USD | 25,950,000.00 USD | 0.00 USD | 0.00 USD | 184,710.00 USD |
| `1D` | `642.70` | 25,760,000.00 USD | 0.00 USD | 25,760,000.00 USD | 150,090.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `646.30` | 25,610,000.00 USD | 0.00 USD | 25,610,000.00 USD | 87,020.00 USD | 0.00 USD | 140,640.00 USD |
| `1D` | `647.50` | 25,390,000.00 USD | 0.00 USD | 25,390,000.00 USD | 227,570.00 USD | 29,080.00 USD | 0.00 USD |
| `1D` | `648.70` | 25,130,000.00 USD | 0.00 USD | 25,130,000.00 USD | 101,870.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `651.10` | 25,030,000.00 USD | 0.00 USD | 25,030,000.00 USD | 106,810.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `652.30` | 24,920,000.00 USD | 0.00 USD | 24,920,000.00 USD | 0.00 USD | 0.00 USD | 94,590.00 USD |
| `1D` | `653.50` | 24,830,000.00 USD | 0.00 USD | 24,830,000.00 USD | 0.00 USD | 26,830.00 USD | 0.00 USD |
| `1D` | `655.90` | 24,800,000.00 USD | 0.00 USD | 24,800,000.00 USD | 120,150.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `657.10` | 24,680,000.00 USD | 0.00 USD | 24,680,000.00 USD | 5,100.00 USD | 21,320.00 USD | 825,700.00 USD |
| `1D` | `658.30` | 23,830,000.00 USD | 0.00 USD | 23,830,000.00 USD | 799,170.00 USD | 14,920.00 USD | 0.00 USD |
| `1D` | `659.50` | 23,010,000.00 USD | 0.00 USD | 23,010,000.00 USD | 64,090.00 USD | 7,460.00 USD | 81,440.00 USD |
| `1D` | `660.70` | 22,860,000.00 USD | 0.00 USD | 22,860,000.00 USD | 0.00 USD | 83,170.00 USD | 14,670.00 USD |
| `1D` | `661.90` | 22,760,000.00 USD | 0.00 USD | 22,760,000.00 USD | 445,210.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `663.10` | 22,320,000.00 USD | 0.00 USD | 22,320,000.00 USD | 202,560.00 USD | 92,740.00 USD | 19,650.00 USD |
| `7D` | `664.10` | 87,050,000.00 USD | 0.00 USD | 87,050,000.00 USD | 78,740.00 USD | 18,740.00 USD | 39,340.00 USD |
| `1D` | `664.30` | 22,000,000.00 USD | 0.00 USD | 22,000,000.00 USD | 684,100.00 USD | 48,410.00 USD | 21,160.00 USD |
| `7D` | `665.00` | 86,910,000.00 USD | 0.00 USD | 86,910,000.00 USD | 92,030.00 USD | 22,990.00 USD | 37,000.00 USD |
| `1D` | `665.50` | 21,250,000.00 USD | 0.00 USD | 21,250,000.00 USD | 1,180,000.00 USD | 4,540.00 USD | 11,460.00 USD |
| `7D` | `665.90` | 86,760,000.00 USD | 0.00 USD | 86,760,000.00 USD | 264,020.00 USD | 71,380.00 USD | 63,410.00 USD |
| `1D` | `666.70` | 20,050,000.00 USD | 0.00 USD | 20,050,000.00 USD | 610,130.00 USD | 102,050.00 USD | 696,480.00 USD |
| `7D` | `666.80` | 86,360,000.00 USD | 0.00 USD | 86,360,000.00 USD | 198,550.00 USD | 33,320.00 USD | 61,710.00 USD |
| `7D` | `667.70` | 86,070,000.00 USD | 0.00 USD | 86,070,000.00 USD | 199,690.00 USD | 45,130.00 USD | 51,340.00 USD |
| `1D` | `667.90` | 18,640,000.00 USD | 0.00 USD | 18,640,000.00 USD | 187,460.00 USD | 115,700.00 USD | 9,290.00 USD |
| `7D` | `668.60` | 85,770,000.00 USD | 0.00 USD | 85,770,000.00 USD | 387,530.00 USD | 92,860.00 USD | 51,060.00 USD |
| `1D` | `669.10` | 18,330,000.00 USD | 0.00 USD | 18,330,000.00 USD | 548,420.00 USD | 82,590.00 USD | 3,620.00 USD |
| `7D` | `669.50` | 85,240,000.00 USD | 0.00 USD | 85,240,000.00 USD | 341,150.00 USD | 38,130.00 USD | 108,970.00 USD |
| `1D` | `670.30` | 17,690,000.00 USD | 0.00 USD | 17,690,000.00 USD | 253,490.00 USD | 3,950.00 USD | 1,490,000.00 USD |
| `7D` | `670.40` | 84,750,000.00 USD | 0.00 USD | 84,750,000.00 USD | 319,660.00 USD | 93,800.00 USD | 77,380.00 USD |
| `7D` | `671.30` | 84,260,000.00 USD | 0.00 USD | 84,260,000.00 USD | 335,750.00 USD | 57,500.00 USD | 42,050.00 USD |
| `1D` | `671.50` | 15,950,000.00 USD | 0.00 USD | 15,950,000.00 USD | 1,560,000.00 USD | 18,100.00 USD | 18,140.00 USD |
| `7D` | `672.20` | 83,830,000.00 USD | 0.00 USD | 83,830,000.00 USD | 180,230.00 USD | 62,620.00 USD | 74,250.00 USD |
| `1D` | `672.70` | 14,350,000.00 USD | 0.00 USD | 14,350,000.00 USD | 440,210.00 USD | 21,920.00 USD | 670,660.00 USD |
| `7D` | `673.10` | 83,510,000.00 USD | 0.00 USD | 83,510,000.00 USD | 394,120.00 USD | 64,970.00 USD | 42,710.00 USD |
| `1D` | `673.90` | 13,220,000.00 USD | 0.00 USD | 13,220,000.00 USD | 471,690.00 USD | 45,440.00 USD | 1,050,000.00 USD |
| `7D` | `674.00` | 83,010,000.00 USD | 0.00 USD | 83,010,000.00 USD | 335,670.00 USD | 105,910.00 USD | 80,360.00 USD |
| `7D` | `674.90` | 82,490,000.00 USD | 0.00 USD | 82,490,000.00 USD | 247,070.00 USD | 31,490.00 USD | 44,420.00 USD |
| `1D` | `675.10` | 11,650,000.00 USD | 0.00 USD | 11,650,000.00 USD | 2,020,000.00 USD | 313,780.00 USD | 27,680.00 USD |
| `7D` | `675.80` | 82,160,000.00 USD | 0.00 USD | 82,160,000.00 USD | 387,400.00 USD | 26,020.00 USD | 79,190.00 USD |
| `1D` | `676.30` | 9,290,000.00 USD | 0.00 USD | 9,290,000.00 USD | 140,710.00 USD | 214,200.00 USD | 85,400.00 USD |
| `7D` | `676.70` | 81,670,000.00 USD | 0.00 USD | 81,670,000.00 USD | 509,100.00 USD | 35,490.00 USD | 126,570.00 USD |
| `1D` | `677.50` | 8,850,000.00 USD | 0.00 USD | 8,850,000.00 USD | 531,820.00 USD | 121,270.00 USD | 0.00 USD |
| `7D` | `677.60` | 81,000,000.00 USD | 0.00 USD | 81,000,000.00 USD | 409,810.00 USD | 0.00 USD | 63,990.00 USD |
| `7D` | `678.50` | 80,530,000.00 USD | 0.00 USD | 80,530,000.00 USD | 120,190.00 USD | 0.00 USD | 26,990.00 USD |
| `1D` | `678.70` | 8,190,000.00 USD | 0.00 USD | 8,190,000.00 USD | 1,060,000.00 USD | 111,460.00 USD | 0.00 USD |
| `7D` | `679.40` | 80,380,000.00 USD | 0.00 USD | 80,380,000.00 USD | 116,510.00 USD | 10,480.00 USD | 40,610.00 USD |
| `1D` | `679.90` | 7,020,000.00 USD | 0.00 USD | 7,020,000.00 USD | 1,200,000.00 USD | 169,140.00 USD | 0.00 USD |
| `7D` | `680.30` | 80,210,000.00 USD | 0.00 USD | 80,210,000.00 USD | 166,780.00 USD | 13,510.00 USD | 0.00 USD |
| `1D` | `681.10` | 5,650,000.00 USD | 0.00 USD | 5,650,000.00 USD | 16,450.00 USD | 99,800.00 USD | 0.00 USD |
| `7D` | `681.20` | 80,030,000.00 USD | 0.00 USD | 80,030,000.00 USD | 106,280.00 USD | 7,050.00 USD | 35,170.00 USD |
| `7D` | `682.10` | 79,880,000.00 USD | 0.00 USD | 79,880,000.00 USD | 0.00 USD | 23,360.00 USD | 27,620.00 USD |
| `1D` | `682.30` | 5,540,000.00 USD | 0.00 USD | 5,540,000.00 USD | 36,660.00 USD | 242,460.00 USD | 0.00 USD |
| `7D` | `683.00` | 79,830,000.00 USD | 0.00 USD | 79,830,000.00 USD | 175,930.00 USD | 28,470.00 USD | 11,520.00 USD |
| `1D` | `683.50` | 5,260,000.00 USD | 0.00 USD | 5,260,000.00 USD | 138,150.00 USD | 127,200.00 USD | 0.00 USD |
| `7D` | `683.90` | 79,620,000.00 USD | 0.00 USD | 79,620,000.00 USD | 77,000.00 USD | 29,510.00 USD | 17,480.00 USD |
| `1D` | `684.70` | 4,990,000.00 USD | 0.00 USD | 4,990,000.00 USD | 0.00 USD | 38,160.00 USD | 0.00 USD |
| `7D` | `684.80` | 79,490,000.00 USD | 0.00 USD | 79,490,000.00 USD | 246,080.00 USD | 9,850.00 USD | 39,550.00 USD |
| `7D` | `685.70` | 79,200,000.00 USD | 0.00 USD | 79,200,000.00 USD | 197,040.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `685.90` | 4,950,000.00 USD | 0.00 USD | 4,950,000.00 USD | 694,060.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `686.60` | 79,000,000.00 USD | 0.00 USD | 79,000,000.00 USD | 62,990.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `687.50` | 78,940,000.00 USD | 0.00 USD | 78,940,000.00 USD | 148,480.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `688.30` | 4,260,000.00 USD | 0.00 USD | 4,260,000.00 USD | 3,940.00 USD | 0.00 USD | 2,020,000.00 USD |
| `7D` | `688.40` | 78,790,000.00 USD | 0.00 USD | 78,790,000.00 USD | 67,880.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `689.30` | 78,720,000.00 USD | 0.00 USD | 78,720,000.00 USD | 84,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `689.50` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `690.20` | 78,640,000.00 USD | 0.00 USD | 78,640,000.00 USD | 283,920.00 USD | 63,230.00 USD | 82,450.00 USD |
| `1D` | `690.70` | 295,360.00 USD | 0.00 USD | 295,360.00 USD | 95,780.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `691.10` | 78,210,000.00 USD | 0.00 USD | 78,210,000.00 USD | 362,020.00 USD | 61,370.00 USD | 81,090.00 USD |
| `1D` | `691.90` | 199,580.00 USD | 0.00 USD | 199,580.00 USD | 33,240.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `692.00` | 77,700,000.00 USD | 0.00 USD | 77,700,000.00 USD | 322,430.00 USD | 18,850.00 USD | 58,910.00 USD |
| `7D` | `692.90` | 77,300,000.00 USD | 0.00 USD | 77,300,000.00 USD | 280,830.00 USD | 19,470.00 USD | 0.00 USD |
| `7D` | `693.80` | 77,000,000.00 USD | 0.00 USD | 77,000,000.00 USD | 305,720.00 USD | 39,210.00 USD | 0.00 USD |
| `7D` | `694.70` | 76,660,000.00 USD | 0.00 USD | 76,660,000.00 USD | 279,840.00 USD | 36,640.00 USD | 35,490.00 USD |
| `7D` | `695.60` | 76,300,000.00 USD | 0.00 USD | 76,300,000.00 USD | 120,440.00 USD | 0.00 USD | 21,670.00 USD |
| `7D` | `696.50` | 76,160,000.00 USD | 0.00 USD | 76,160,000.00 USD | 140,370.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `697.40` | 76,020,000.00 USD | 0.00 USD | 76,020,000.00 USD | 189,100.00 USD | 19,230.00 USD | 0.00 USD |
| `7D` | `698.30` | 75,810,000.00 USD | 0.00 USD | 75,810,000.00 USD | 273,520.00 USD | 33,120.00 USD | 54,800.00 USD |
| `7D` | `699.20` | 75,450,000.00 USD | 0.00 USD | 75,450,000.00 USD | 274,810.00 USD | 12,670.00 USD | 11,820.00 USD |
| `7D` | `700.10` | 75,150,000.00 USD | 0.00 USD | 75,150,000.00 USD | 225,450.00 USD | 40,820.00 USD | 27,440.00 USD |
| `7D` | `701.00` | 74,860,000.00 USD | 0.00 USD | 74,860,000.00 USD | 237,800.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `701.90` | 74,620,000.00 USD | 0.00 USD | 74,620,000.00 USD | 135,260.00 USD | 41,260.00 USD | 89,700.00 USD |
| `1D` | `702.70` | 166,340.00 USD | 0.00 USD | 166,340.00 USD | 0.00 USD | 166,340.00 USD | 0.00 USD |
| `7D` | `702.80` | 74,360,000.00 USD | 0.00 USD | 74,360,000.00 USD | 416,820.00 USD | 57,470.00 USD | 36,720.00 USD |
| `1D` | `703.50` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `703.70` | 73,840,000.00 USD | 0.00 USD | 73,840,000.00 USD | 311,800.00 USD | 44,990.00 USD | 0.00 USD |
| `1D` | `703.90` | 175,470.00 USD | 175,470.00 USD | 0.00 USD | 0.00 USD | 175,470.00 USD | 0.00 USD |
| `7D` | `704.60` | 73,490,000.00 USD | 0.00 USD | 73,490,000.00 USD | 537,050.00 USD | 136,550.00 USD | 194,460.00 USD |
| `1D` | `705.10` | 272,300.00 USD | 272,300.00 USD | 0.00 USD | 0.00 USD | 96,830.00 USD | 0.00 USD |
| `7D` | `705.50` | 72,620,000.00 USD | 0.00 USD | 72,620,000.00 USD | 920,340.00 USD | 162,820.00 USD | 236,670.00 USD |
| `7D` | `706.40` | 71,300,000.00 USD | 0.00 USD | 71,300,000.00 USD | 523,540.00 USD | 104,380.00 USD | 231,200.00 USD |
| `7D` | `707.30` | 70,440,000.00 USD | 0.00 USD | 70,440,000.00 USD | 604,060.00 USD | 90,200.00 USD | 53,960.00 USD |
| `1D` | `707.50` | 429,570.00 USD | 429,570.00 USD | 0.00 USD | 0.00 USD | 157,270.00 USD | 0.00 USD |
| `7D` | `708.20` | 69,690,000.00 USD | 0.00 USD | 69,690,000.00 USD | 796,640.00 USD | 138,200.00 USD | 42,800.00 USD |
| `7D` | `709.10` | 68,710,000.00 USD | 0.00 USD | 68,710,000.00 USD | 392,150.00 USD | 156,040.00 USD | 195,500.00 USD |
| `1D` | `709.90` | 654,380.00 USD | 654,380.00 USD | 0.00 USD | 0.00 USD | 224,810.00 USD | 0.00 USD |
| `7D` | `710.00` | 67,970,000.00 USD | 0.00 USD | 67,970,000.00 USD | 450,480.00 USD | 167,090.00 USD | 176,960.00 USD |
| `7D` | `710.90` | 67,180,000.00 USD | 0.00 USD | 67,180,000.00 USD | 922,450.00 USD | 160,040.00 USD | 236,990.00 USD |
| `1D` | `711.10` | 768,540.00 USD | 768,540.00 USD | 0.00 USD | 0.00 USD | 114,160.00 USD | 0.00 USD |
| `7D` | `711.80` | 65,860,000.00 USD | 0.00 USD | 65,860,000.00 USD | 608,910.00 USD | 232,130.00 USD | 114,740.00 USD |
| `7D` | `712.70` | 64,900,000.00 USD | 0.00 USD | 64,900,000.00 USD | 1,190,000.00 USD | 217,390.00 USD | 236,970.00 USD |
| `7D` | `713.60` | 63,260,000.00 USD | 0.00 USD | 63,260,000.00 USD | 2,250,000.00 USD | 279,180.00 USD | 308,960.00 USD |
| `7D` | `714.50` | 60,410,000.00 USD | 0.00 USD | 60,410,000.00 USD | 508,400.00 USD | 209,320.00 USD | 292,980.00 USD |
| `7D` | `715.40` | 59,400,000.00 USD | 0.00 USD | 59,400,000.00 USD | 1,050,000.00 USD | 419,310.00 USD | 329,730.00 USD |
| `1D` | `715.90` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 83,170.00 USD | 2,020,000.00 USD |
| `7D` | `716.30` | 57,600,000.00 USD | 0.00 USD | 57,600,000.00 USD | 1,080,000.00 USD | 324,540.00 USD | 233,140.00 USD |
| `1D` | `717.10` | 4,990,000.00 USD | 4,990,000.00 USD | 0.00 USD | 1,910,000.00 USD | 214,720.00 USD | 0.00 USD |
| `7D` | `717.20` | 55,960,000.00 USD | 0.00 USD | 55,960,000.00 USD | 581,610.00 USD | 398,030.00 USD | 387,120.00 USD |
| `7D` | `718.10` | 54,590,000.00 USD | 0.00 USD | 54,590,000.00 USD | 1,690,000.00 USD | 246,320.00 USD | 151,880.00 USD |
| `1D` | `718.30` | 5,080,000.00 USD | 5,080,000.00 USD | 0.00 USD | 0.00 USD | 87,740.00 USD | 0.00 USD |
| `7D` | `719.00` | 52,510,000.00 USD | 0.00 USD | 52,510,000.00 USD | 670,390.00 USD | 137,460.00 USD | 211,490.00 USD |
| `1D` | `719.50` | 5,120,000.00 USD | 5,120,000.00 USD | 0.00 USD | 0.00 USD | 48,410.00 USD | 0.00 USD |
| `7D` | `719.90` | 51,490,000.00 USD | 0.00 USD | 51,490,000.00 USD | 618,020.00 USD | 173,240.00 USD | 186,780.00 USD |
| `1D` | `720.70` | 6,480,000.00 USD | 6,480,000.00 USD | 0.00 USD | 1,150,000.00 USD | 204,540.00 USD | 0.00 USD |
| `7D` | `720.80` | 50,510,000.00 USD | 0.00 USD | 50,510,000.00 USD | 1,010,000.00 USD | 52,490.00 USD | 180,370.00 USD |
| `7D` | `721.70` | 49,260,000.00 USD | 0.00 USD | 49,260,000.00 USD | 1,950,000.00 USD | 237,690.00 USD | 653,400.00 USD |
| `1D` | `721.90` | 9,530,000.00 USD | 9,530,000.00 USD | 0.00 USD | 1,110,000.00 USD | 78,640.00 USD | 1,870,000.00 USD |
| `7D` | `722.60` | 46,430,000.00 USD | 0.00 USD | 46,430,000.00 USD | 1,930,000.00 USD | 108,200.00 USD | 229,380.00 USD |
| `1D` | `723.10` | 10,210,000.00 USD | 10,210,000.00 USD | 0.00 USD | 562,170.00 USD | 112,400.00 USD | 0.00 USD |
| `7D` | `723.50` | 44,160,000.00 USD | 0.00 USD | 44,160,000.00 USD | 640,550.00 USD | 140,550.00 USD | 293,670.00 USD |
| `1D` | `724.30` | 11,590,000.00 USD | 11,590,000.00 USD | 0.00 USD | 1,200,000.00 USD | 188,050.00 USD | 0.00 USD |
| `7D` | `724.40` | 43,080,000.00 USD | 0.00 USD | 43,080,000.00 USD | 663,550.00 USD | 186,780.00 USD | 130,770.00 USD |
| `7D` | `725.30` | 42,100,000.00 USD | 0.00 USD | 42,100,000.00 USD | 1,760,000.00 USD | 418,390.00 USD | 396,690.00 USD |
| `1D` | `725.50` | 12,570,000.00 USD | 12,570,000.00 USD | 0.00 USD | 0.00 USD | 57,080.00 USD | 923,540.00 USD |
| `7D` | `726.20` | 39,520,000.00 USD | 0.00 USD | 39,520,000.00 USD | 1,060,000.00 USD | 311,550.00 USD | 460,020.00 USD |
| `1D` | `726.70` | 12,630,000.00 USD | 12,630,000.00 USD | 0.00 USD | 0.00 USD | 64,470.00 USD | 0.00 USD |
| `7D` | `727.10` | 37,690,000.00 USD | 0.00 USD | 37,690,000.00 USD | 1,230,000.00 USD | 331,980.00 USD | 241,010.00 USD |
| `1D` | `727.90` | 13,560,000.00 USD | 13,560,000.00 USD | 0.00 USD | 924,740.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `728.00` | 35,890,000.00 USD | 0.00 USD | 35,890,000.00 USD | 3,110,000.00 USD | 778,750.00 USD | 388,930.00 USD |
| `7D` | `728.90` | 31,610,000.00 USD | 0.00 USD | 31,610,000.00 USD | 2,330,000.00 USD | 317,590.00 USD | 644,150.00 USD |
| `1D` | `729.10` | 14,200,000.00 USD | 14,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 636,900.00 USD |
| `7D` | `729.80` | 28,320,000.00 USD | 0.00 USD | 28,320,000.00 USD | 1,320,000.00 USD | 430,010.00 USD | 339,140.00 USD |
| `1D` | `730.30` | 15,310,000.00 USD | 15,310,000.00 USD | 0.00 USD | 0.00 USD | 107,360.00 USD | 1,010,000.00 USD |
| `7D` | `730.70` | 26,230,000.00 USD | 0.00 USD | 26,230,000.00 USD | 2,760,000.00 USD | 351,520.00 USD | 587,010.00 USD |
| `1D` | `731.50` | 16,330,000.00 USD | 16,330,000.00 USD | 0.00 USD | 952,750.00 USD | 63,350.00 USD | 0.00 USD |
| `7D` | `731.60` | 22,530,000.00 USD | 0.00 USD | 22,530,000.00 USD | 1,530,000.00 USD | 133,980.00 USD | 261,910.00 USD |
| `7D` | `732.50` | 20,610,000.00 USD | 0.00 USD | 20,610,000.00 USD | 465,880.00 USD | 221,510.00 USD | 96,400.00 USD |
| `1D` | `732.70` | 18,030,000.00 USD | 18,030,000.00 USD | 0.00 USD | 998,900.00 USD | 0.00 USD | 703,180.00 USD |
| `7D` | `733.40` | 19,820,000.00 USD | 0.00 USD | 19,820,000.00 USD | 1,910,000.00 USD | 158,310.00 USD | 338,540.00 USD |
| `1D` | `733.90` | 18,580,000.00 USD | 18,580,000.00 USD | 0.00 USD | 344,230.00 USD | 206,790.00 USD | 0.00 USD |
| `7D` | `734.30` | 17,420,000.00 USD | 0.00 USD | 17,420,000.00 USD | 1,580,000.00 USD | 288,470.00 USD | 244,940.00 USD |
| `1D` | `735.10` | 19,440,000.00 USD | 19,440,000.00 USD | 0.00 USD | 613,800.00 USD | 241,610.00 USD | 0.00 USD |
| `7D` | `735.20` | 15,310,000.00 USD | 0.00 USD | 15,310,000.00 USD | 1,330,000.00 USD | 172,940.00 USD | 437,510.00 USD |
| `7D` | `736.10` | 13,370,000.00 USD | 0.00 USD | 13,370,000.00 USD | 2,130,000.00 USD | 181,990.00 USD | 484,910.00 USD |
| `1D` | `736.30` | 21,330,000.00 USD | 21,330,000.00 USD | 0.00 USD | 1,270,000.00 USD | 27,530.00 USD | 590,930.00 USD |
| `7D` | `737.00` | 10,570,000.00 USD | 0.00 USD | 10,570,000.00 USD | 2,360,000.00 USD | 175,330.00 USD | 633,690.00 USD |
| `1D` | `737.50` | 21,610,000.00 USD | 21,610,000.00 USD | 0.00 USD | 186,520.00 USD | 94,030.00 USD | 0.00 USD |
| `7D` | `737.90` | 7,400,000.00 USD | 0.00 USD | 7,400,000.00 USD | 3,420,000.00 USD | 72,280.00 USD | 374,090.00 USD |
| `1D` | `738.70` | 22,740,000.00 USD | 22,740,000.00 USD | 0.00 USD | 658,340.00 USD | 0.00 USD | 472,930.00 USD |
| `7D` | `738.80` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 522,950.00 USD | 20,210.00 USD | 155,300.00 USD |
| `7D` | `739.70` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 352,500.00 USD | 0.00 USD | 203,030.00 USD |
| `1D` | `739.90` | 23,730,000.00 USD | 23,730,000.00 USD | 0.00 USD | 518,470.00 USD | 0.00 USD | 476,790.00 USD |
| `7D` | `740.60` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 1,090,000.00 USD | 0.00 USD | 33,390.00 USD |
| `1D` | `741.10` | 24,510,000.00 USD | 24,510,000.00 USD | 0.00 USD | 603,910.00 USD | 166,390.00 USD | 7,010.00 USD |
| `7D` | `741.50` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 257,630.00 USD | 0.00 USD | 208,590.00 USD |
| `1D` | `742.30` | 24,800,000.00 USD | 24,800,000.00 USD | 0.00 USD | 291,160.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `742.40` | 689,850.00 USD | 0.00 USD | 689,850.00 USD | 0.00 USD | 0.00 USD | 183,920.00 USD |
| `7D` | `743.30` | 505,930.00 USD | 0.00 USD | 505,930.00 USD | 0.00 USD | 0.00 USD | 57,580.00 USD |
| `1D` | `743.50` | 25,240,000.00 USD | 25,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 436,560.00 USD |
| `7D` | `744.20` | 448,350.00 USD | 0.00 USD | 448,350.00 USD | 0.00 USD | 257,580.00 USD | 141,790.00 USD |
| `1D` | `744.70` | 25,450,000.00 USD | 25,450,000.00 USD | 0.00 USD | 106,810.00 USD | 106,580.00 USD | 0.00 USD |
| `7D` | `745.10` | 48,980.00 USD | 0.00 USD | 48,980.00 USD | 0.00 USD | 48,980.00 USD | 0.00 USD |
| `7D` | `745.20` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `745.90` | 26,040,000.00 USD | 26,040,000.00 USD | 0.00 USD | 482,060.00 USD | 106,280.00 USD | 0.00 USD |
| `7D` | `746.00` | 999,320.00 USD | 999,320.00 USD | 0.00 USD | 999,320.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `746.90` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 215,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `747.10` | 27,620,000.00 USD | 27,620,000.00 USD | 0.00 USD | 748,640.00 USD | 67,980.00 USD | 758,780.00 USD |
| `1D` | `748.30` | 28,050,000.00 USD | 28,050,000.00 USD | 0.00 USD | 286,680.00 USD | 72,690.00 USD | 73,330.00 USD |
| `1D` | `749.50` | 28,470,000.00 USD | 28,470,000.00 USD | 0.00 USD | 417,840.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `751.90` | 28,920,000.00 USD | 28,920,000.00 USD | 0.00 USD | 0.00 USD | 25,010.00 USD | 433,820.00 USD |
| `1D` | `753.10` | 29,510,000.00 USD | 29,510,000.00 USD | 0.00 USD | 229,820.00 USD | 0.00 USD | 354,670.00 USD |
| `1D` | `754.30` | 30,020,000.00 USD | 30,020,000.00 USD | 0.00 USD | 383,510.00 USD | 74,660.00 USD | 57,280.00 USD |
| `7D` | `755.00` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 59,560.00 USD | 0.00 USD |
| `1D` | `755.50` | 30,630,000.00 USD | 30,630,000.00 USD | 0.00 USD | 293,610.00 USD | 254,460.00 USD | 56,900.00 USD |
| `1D` | `756.70` | 31,140,000.00 USD | 31,140,000.00 USD | 0.00 USD | 390,390.00 USD | 24,970.00 USD | 95,500.00 USD |
| `7D` | `756.80` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 47,340.00 USD | 0.00 USD |
| `7D` | `757.70` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 475,510.00 USD | 113,240.00 USD | 0.00 USD |
| `1D` | `757.90` | 31,880,000.00 USD | 31,880,000.00 USD | 0.00 USD | 515,360.00 USD | 189,940.00 USD | 32,720.00 USD |
| `7D` | `758.60` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `759.10` | 33,490,000.00 USD | 33,490,000.00 USD | 0.00 USD | 1,220,000.00 USD | 122,880.00 USD | 273,090.00 USD |
| `1D` | `760.30` | 34,160,000.00 USD | 34,160,000.00 USD | 0.00 USD | 508,710.00 USD | 100,270.00 USD | 61,750.00 USD |
| `7D` | `760.40` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 0.00 USD | 27,650.00 USD | 42,540.00 USD |
| `7D` | `761.30` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 10,750.00 USD | 211,960.00 USD | 100,630.00 USD |
| `1D` | `761.50` | 35,480,000.00 USD | 35,480,000.00 USD | 0.00 USD | 929,820.00 USD | 77,330.00 USD | 308,810.00 USD |
| `7D` | `762.20` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 699,820.00 USD | 179,270.00 USD |
| `1D` | `762.70` | 37,790,000.00 USD | 37,790,000.00 USD | 0.00 USD | 1,450,000.00 USD | 234,890.00 USD | 624,780.00 USD |
| `7D` | `763.10` | 7,830,000.00 USD | 7,830,000.00 USD | 0.00 USD | 2,460,000.00 USD | 590,460.00 USD | 404,720.00 USD |
| `1D` | `763.90` | 40,740,000.00 USD | 40,740,000.00 USD | 0.00 USD | 2,350,000.00 USD | 269,760.00 USD | 335,210.00 USD |
| `7D` | `764.00` | 10,270,000.00 USD | 10,270,000.00 USD | 0.00 USD | 1,590,000.00 USD | 441,980.00 USD | 402,300.00 USD |
| `7D` | `764.90` | 12,470,000.00 USD | 12,470,000.00 USD | 0.00 USD | 1,450,000.00 USD | 352,570.00 USD | 395,630.00 USD |
| `1D` | `765.10` | 42,630,000.00 USD | 42,630,000.00 USD | 0.00 USD | 1,380,000.00 USD | 280,250.00 USD | 231,980.00 USD |
| `7D` | `765.80` | 15,460,000.00 USD | 15,460,000.00 USD | 0.00 USD | 2,470,000.00 USD | 107,550.00 USD | 416,290.00 USD |
| `1D` | `766.30` | 44,610,000.00 USD | 44,610,000.00 USD | 0.00 USD | 1,240,000.00 USD | 267,070.00 USD | 475,350.00 USD |
| `7D` | `766.70` | 20,050,000.00 USD | 20,050,000.00 USD | 0.00 USD | 3,330,000.00 USD | 416,530.00 USD | 842,330.00 USD |
| `1D` | `767.50` | 47,730,000.00 USD | 47,730,000.00 USD | 0.00 USD | 2,570,000.00 USD | 120,630.00 USD | 424,210.00 USD |
| `7D` | `767.60` | 23,430,000.00 USD | 23,430,000.00 USD | 0.00 USD | 2,790,000.00 USD | 123,530.00 USD | 467,840.00 USD |
| `7D` | `768.50` | 25,660,000.00 USD | 25,660,000.00 USD | 0.00 USD | 1,840,000.00 USD | 95,830.00 USD | 281,920.00 USD |
| `1D` | `768.70` | 49,550,000.00 USD | 49,550,000.00 USD | 0.00 USD | 1,540,000.00 USD | 117,770.00 USD | 164,680.00 USD |
| `7D` | `769.40` | 26,810,000.00 USD | 26,810,000.00 USD | 0.00 USD | 565,780.00 USD | 249,950.00 USD | 333,550.00 USD |
| `1D` | `769.90` | 50,410,000.00 USD | 50,410,000.00 USD | 0.00 USD | 591,420.00 USD | 166,630.00 USD | 96,060.00 USD |
| `7D` | `770.30` | 29,310,000.00 USD | 29,310,000.00 USD | 0.00 USD | 1,900,000.00 USD | 240,530.00 USD | 364,650.00 USD |
| `1D` | `771.10` | 51,520,000.00 USD | 51,520,000.00 USD | 0.00 USD | 682,120.00 USD | 76,340.00 USD | 355,380.00 USD |
| `7D` | `771.20` | 30,770,000.00 USD | 30,770,000.00 USD | 0.00 USD | 1,050,000.00 USD | 242,570.00 USD | 162,680.00 USD |
| `7D` | `772.10` | 33,190,000.00 USD | 33,190,000.00 USD | 0.00 USD | 1,750,000.00 USD | 252,650.00 USD | 419,070.00 USD |
| `1D` | `772.30` | 52,950,000.00 USD | 52,950,000.00 USD | 0.00 USD | 773,930.00 USD | 160,720.00 USD | 492,830.00 USD |
| `7D` | `773.00` | 35,800,000.00 USD | 35,800,000.00 USD | 0.00 USD | 1,950,000.00 USD | 325,680.00 USD | 338,170.00 USD |
| `1D` | `773.50` | 54,360,000.00 USD | 54,360,000.00 USD | 0.00 USD | 946,610.00 USD | 185,610.00 USD | 281,920.00 USD |
| `7D` | `773.90` | 37,600,000.00 USD | 37,600,000.00 USD | 0.00 USD | 1,220,000.00 USD | 276,760.00 USD | 293,960.00 USD |
| `1D` | `774.70` | 55,830,000.00 USD | 55,830,000.00 USD | 0.00 USD | 1,310,000.00 USD | 88,980.00 USD | 65,690.00 USD |
| `7D` | `774.80` | 39,980,000.00 USD | 39,980,000.00 USD | 0.00 USD | 1,310,000.00 USD | 568,930.00 USD | 502,710.00 USD |
| `7D` | `775.70` | 42,470,000.00 USD | 42,470,000.00 USD | 0.00 USD | 1,830,000.00 USD | 470,960.00 USD | 187,170.00 USD |
| `1D` | `775.90` | 56,540,000.00 USD | 56,540,000.00 USD | 0.00 USD | 470,290.00 USD | 153,780.00 USD | 84,640.00 USD |
| `7D` | `776.60` | 44,740,000.00 USD | 44,740,000.00 USD | 0.00 USD | 1,630,000.00 USD | 269,050.00 USD | 378,590.00 USD |
| `1D` | `777.10` | 57,140,000.00 USD | 57,140,000.00 USD | 0.00 USD | 429,240.00 USD | 58,250.00 USD | 110,390.00 USD |
| `7D` | `777.50` | 46,480,000.00 USD | 46,480,000.00 USD | 0.00 USD | 1,350,000.00 USD | 243,990.00 USD | 148,450.00 USD |
| `1D` | `778.30` | 59,060,000.00 USD | 59,060,000.00 USD | 0.00 USD | 1,370,000.00 USD | 175,590.00 USD | 376,490.00 USD |
| `7D` | `778.40` | 48,170,000.00 USD | 48,170,000.00 USD | 0.00 USD | 1,180,000.00 USD | 307,370.00 USD | 206,530.00 USD |
| `7D` | `779.30` | 49,730,000.00 USD | 49,730,000.00 USD | 0.00 USD | 1,240,000.00 USD | 188,170.00 USD | 123,650.00 USD |
| `1D` | `779.50` | 60,260,000.00 USD | 60,260,000.00 USD | 0.00 USD | 936,610.00 USD | 105,030.00 USD | 160,710.00 USD |
| `7D` | `780.20` | 51,100,000.00 USD | 51,100,000.00 USD | 0.00 USD | 1,070,000.00 USD | 86,470.00 USD | 218,750.00 USD |
| `1D` | `780.70` | 61,080,000.00 USD | 61,080,000.00 USD | 0.00 USD | 585,300.00 USD | 124,740.00 USD | 108,580.00 USD |
| `7D` | `781.10` | 52,710,000.00 USD | 52,710,000.00 USD | 0.00 USD | 1,270,000.00 USD | 90,990.00 USD | 242,450.00 USD |
| `1D` | `781.90` | 62,660,000.00 USD | 62,660,000.00 USD | 0.00 USD | 1,100,000.00 USD | 109,060.00 USD | 382,030.00 USD |
| `7D` | `782.00` | 54,610,000.00 USD | 54,610,000.00 USD | 0.00 USD | 1,510,000.00 USD | 87,670.00 USD | 301,190.00 USD |
| `7D` | `782.90` | 56,600,000.00 USD | 56,600,000.00 USD | 0.00 USD | 1,750,000.00 USD | 36,140.00 USD | 202,700.00 USD |
| `1D` | `783.10` | 64,010,000.00 USD | 64,010,000.00 USD | 0.00 USD | 1,090,000.00 USD | 80,140.00 USD | 176,370.00 USD |
| `7D` | `783.80` | 57,170,000.00 USD | 57,170,000.00 USD | 0.00 USD | 508,000.00 USD | 10,100.00 USD | 54,380.00 USD |
| `1D` | `784.30` | 64,560,000.00 USD | 64,560,000.00 USD | 0.00 USD | 494,760.00 USD | 28,920.00 USD | 29,950.00 USD |
| `7D` | `784.70` | 57,480,000.00 USD | 57,480,000.00 USD | 0.00 USD | 208,380.00 USD | 28,260.00 USD | 70,300.00 USD |
| `1D` | `785.50` | 65,110,000.00 USD | 65,110,000.00 USD | 0.00 USD | 482,590.00 USD | 37,320.00 USD | 27,120.00 USD |
| `7D` | `785.60` | 58,610,000.00 USD | 58,610,000.00 USD | 0.00 USD | 1,010,000.00 USD | 54,140.00 USD | 71,180.00 USD |
| `7D` | `786.50` | 59,000,000.00 USD | 59,000,000.00 USD | 0.00 USD | 329,230.00 USD | 30,660.00 USD | 23,970.00 USD |
| `1D` | `786.70` | 65,420,000.00 USD | 65,420,000.00 USD | 0.00 USD | 240,650.00 USD | 29,920.00 USD | 40,510.00 USD |
| `7D` | `787.40` | 59,580,000.00 USD | 59,580,000.00 USD | 0.00 USD | 470,050.00 USD | 17,630.00 USD | 91,050.00 USD |
| `1D` | `787.90` | 65,820,000.00 USD | 65,820,000.00 USD | 0.00 USD | 285,740.00 USD | 42,520.00 USD | 75,010.00 USD |
| `7D` | `788.30` | 59,940,000.00 USD | 59,940,000.00 USD | 0.00 USD | 202,630.00 USD | 82,380.00 USD | 81,230.00 USD |
| `1D` | `789.10` | 66,400,000.00 USD | 66,400,000.00 USD | 0.00 USD | 443,990.00 USD | 62,290.00 USD | 69,790.00 USD |
| `7D` | `789.20` | 60,780,000.00 USD | 60,780,000.00 USD | 0.00 USD | 698,830.00 USD | 81,250.00 USD | 55,990.00 USD |
| `7D` | `790.10` | 61,270,000.00 USD | 61,270,000.00 USD | 0.00 USD | 299,250.00 USD | 104,360.00 USD | 88,890.00 USD |
| `1D` | `790.30` | 67,060,000.00 USD | 67,060,000.00 USD | 0.00 USD | 459,640.00 USD | 40,140.00 USD | 163,110.00 USD |
| `7D` | `791.00` | 62,150,000.00 USD | 62,150,000.00 USD | 0.00 USD | 693,290.00 USD | 82,870.00 USD | 100,420.00 USD |
| `1D` | `791.50` | 67,490,000.00 USD | 67,490,000.00 USD | 0.00 USD | 357,910.00 USD | 61,910.00 USD | 8,530.00 USD |
| `7D` | `791.90` | 63,030,000.00 USD | 63,030,000.00 USD | 0.00 USD | 816,380.00 USD | 16,830.00 USD | 46,300.00 USD |
| `1D` | `792.70` | 67,690,000.00 USD | 67,690,000.00 USD | 0.00 USD | 203,200.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `792.80` | 63,250,000.00 USD | 63,250,000.00 USD | 0.00 USD | 205,450.00 USD | 0.00 USD | 14,670.00 USD |
| `7D` | `793.70` | 63,430,000.00 USD | 63,430,000.00 USD | 0.00 USD | 184,960.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `793.90` | 67,740,000.00 USD | 67,740,000.00 USD | 0.00 USD | 47,320.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `794.60` | 63,750,000.00 USD | 63,750,000.00 USD | 0.00 USD | 302,280.00 USD | 15,690.00 USD | 0.00 USD |
| `1D` | `795.10` | 67,790,000.00 USD | 67,790,000.00 USD | 0.00 USD | 44,970.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `795.50` | 63,890,000.00 USD | 63,890,000.00 USD | 0.00 USD | 109,640.00 USD | 14,650.00 USD | 14,200.00 USD |
| `1D` | `796.30` | 67,840,000.00 USD | 67,840,000.00 USD | 0.00 USD | 50,250.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `796.40` | 64,030,000.00 USD | 64,030,000.00 USD | 0.00 USD | 139,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `797.30` | 64,090,000.00 USD | 64,090,000.00 USD | 0.00 USD | 64,670.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `797.50` | 68,010,000.00 USD | 68,010,000.00 USD | 0.00 USD | 78,300.00 USD | 0.00 USD | 94,590.00 USD |
| `7D` | `798.20` | 64,250,000.00 USD | 64,250,000.00 USD | 0.00 USD | 155,890.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `798.70` | 68,080,000.00 USD | 68,080,000.00 USD | 0.00 USD | 46,910.00 USD | 26,830.00 USD | 0.00 USD |
| `7D` | `799.10` | 64,290,000.00 USD | 64,290,000.00 USD | 0.00 USD | 42,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `799.90` | 68,100,000.00 USD | 68,100,000.00 USD | 0.00 USD | 18,790.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `800.00` | 64,400,000.00 USD | 64,400,000.00 USD | 0.00 USD | 113,540.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `800.90` | 64,510,000.00 USD | 64,510,000.00 USD | 0.00 USD | 77,580.00 USD | 8,370.00 USD | 21,920.00 USD |
| `1D` | `801.10` | 68,120,000.00 USD | 68,120,000.00 USD | 0.00 USD | 20,010.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `801.80` | 64,720,000.00 USD | 64,720,000.00 USD | 0.00 USD | 179,900.00 USD | 16,330.00 USD | 10,970.00 USD |
| `1D` | `802.30` | 68,260,000.00 USD | 68,260,000.00 USD | 0.00 USD | 32,010.00 USD | 21,320.00 USD | 87,310.00 USD |
| `7D` | `802.70` | 64,730,000.00 USD | 64,730,000.00 USD | 0.00 USD | 11,220.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `803.50` | 68,350,000.00 USD | 68,350,000.00 USD | 0.00 USD | 89,870.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `803.60` | 64,760,000.00 USD | 64,760,000.00 USD | 0.00 USD | 27,360.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `804.50` | 64,840,000.00 USD | 64,840,000.00 USD | 0.00 USD | 32,340.00 USD | 18,260.00 USD | 32,980.00 USD |
| `1D` | `804.70` | 68,430,000.00 USD | 68,430,000.00 USD | 0.00 USD | 67,230.00 USD | 14,920.00 USD | 0.00 USD |
| `7D` | `805.40` | 64,910,000.00 USD | 64,910,000.00 USD | 0.00 USD | 56,700.00 USD | 8,140.00 USD | 0.00 USD |
| `1D` | `805.90` | 68,540,000.00 USD | 68,540,000.00 USD | 0.00 USD | 12,090.00 USD | 7,460.00 USD | 81,440.00 USD |
| `7D` | `806.30` | 64,920,000.00 USD | 64,920,000.00 USD | 0.00 USD | 3,270.00 USD | 12,000.00 USD | 0.00 USD |
| `1D` | `807.10` | 68,560,000.00 USD | 68,560,000.00 USD | 0.00 USD | 11,450.00 USD | 0.00 USD | 14,670.00 USD |
| `7D` | `807.20` | 64,970,000.00 USD | 64,970,000.00 USD | 0.00 USD | 39,190.00 USD | 0.00 USD | 11,830.00 USD |
| `7D` | `808.10` | 65,030,000.00 USD | 65,030,000.00 USD | 0.00 USD | 17,980.00 USD | 5,360.00 USD | 29,800.00 USD |
| `1D` | `808.30` | 68,570,000.00 USD | 68,570,000.00 USD | 0.00 USD | 6,570.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `809.00` | 65,110,000.00 USD | 65,110,000.00 USD | 0.00 USD | 58,620.00 USD | 13,120.00 USD | 13,000.00 USD |
| `1D` | `809.50` | 68,580,000.00 USD | 68,580,000.00 USD | 0.00 USD | 13,320.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `809.90` | 65,330,000.00 USD | 65,330,000.00 USD | 0.00 USD | 178,130.00 USD | 9,760.00 USD | 36,490.00 USD |
| `1D` | `810.70` | 68,610,000.00 USD | 68,610,000.00 USD | 0.00 USD | 5,050.00 USD | 5,000.00 USD | 19,650.00 USD |
| `7D` | `810.80` | 65,420,000.00 USD | 65,420,000.00 USD | 0.00 USD | 78,030.00 USD | 6,630.00 USD | 5,340.00 USD |
| `7D` | `811.70` | 65,480,000.00 USD | 65,480,000.00 USD | 0.00 USD | 19,210.00 USD | 12,110.00 USD | 29,380.00 USD |
| `1D` | `811.90` | 68,680,000.00 USD | 68,680,000.00 USD | 0.00 USD | 45,960.00 USD | 0.00 USD | 21,160.00 USD |
| `7D` | `812.60` | 65,600,000.00 USD | 65,600,000.00 USD | 0.00 USD | 68,390.00 USD | 17,450.00 USD | 31,430.00 USD |
| `1D` | `813.10` | 68,710,000.00 USD | 68,710,000.00 USD | 0.00 USD | 19,990.00 USD | 4,540.00 USD | 11,460.00 USD |
| `7D` | `813.50` | 65,860,000.00 USD | 65,860,000.00 USD | 0.00 USD | 147,480.00 USD | 59,640.00 USD | 45,810.00 USD |
| `1D` | `814.30` | 68,760,000.00 USD | 68,760,000.00 USD | 0.00 USD | 25,260.00 USD | 15,040.00 USD | 7,420.00 USD |
| `7D` | `814.40` | 66,180,000.00 USD | 66,180,000.00 USD | 0.00 USD | 218,130.00 USD | 32,770.00 USD | 74,730.00 USD |
| `7D` | `815.30` | 66,390,000.00 USD | 66,390,000.00 USD | 0.00 USD | 171,100.00 USD | 24,290.00 USD | 10,150.00 USD |
| `1D` | `815.50` | 68,830,000.00 USD | 68,830,000.00 USD | 0.00 USD | 38,910.00 USD | 11,670.00 USD | 13,240.00 USD |
| `7D` | `816.20` | 66,690,000.00 USD | 66,690,000.00 USD | 0.00 USD | 203,680.00 USD | 44,470.00 USD | 59,870.00 USD |
| `1D` | `816.70` | 68,900,000.00 USD | 68,900,000.00 USD | 0.00 USD | 54,370.00 USD | 13,980.00 USD | 3,620.00 USD |
| `7D` | `817.10` | 67,090,000.00 USD | 67,090,000.00 USD | 0.00 USD | 278,420.00 USD | 76,830.00 USD | 42,530.00 USD |
| `1D` | `817.90` | 68,950,000.00 USD | 68,950,000.00 USD | 0.00 USD | 43,280.00 USD | 11,530.00 USD | 0.00 USD |
| `7D` | `818.00` | 67,550,000.00 USD | 67,550,000.00 USD | 0.00 USD | 346,550.00 USD | 48,360.00 USD | 67,950.00 USD |
| `7D` | `818.90` | 67,790,000.00 USD | 67,790,000.00 USD | 0.00 USD | 180,470.00 USD | 8,160.00 USD | 47,880.00 USD |
| `1D` | `819.10` | 69,150,000.00 USD | 69,150,000.00 USD | 0.00 USD | 182,710.00 USD | 3,950.00 USD | 12,090.00 USD |
| `7D` | `819.80` | 68,300,000.00 USD | 68,300,000.00 USD | 0.00 USD | 295,510.00 USD | 101,950.00 USD | 107,190.00 USD |
| `1D` | `820.30` | 69,370,000.00 USD | 69,370,000.00 USD | 0.00 USD | 46,010.00 USD | 11,440.00 USD | 159,090.00 USD |
| `7D` | `820.70` | 68,600,000.00 USD | 68,600,000.00 USD | 0.00 USD | 235,990.00 USD | 41,190.00 USD | 24,080.00 USD |
| `1D` | `821.50` | 69,490,000.00 USD | 69,490,000.00 USD | 0.00 USD | 81,550.00 USD | 8,400.00 USD | 33,660.00 USD |
| `7D` | `821.60` | 68,800,000.00 USD | 68,800,000.00 USD | 0.00 USD | 86,380.00 USD | 62,620.00 USD | 55,540.00 USD |
| `7D` | `822.50` | 69,300,000.00 USD | 69,300,000.00 USD | 0.00 USD | 394,120.00 USD | 64,970.00 USD | 42,710.00 USD |
| `1D` | `822.70` | 70,060,000.00 USD | 70,060,000.00 USD | 0.00 USD | 493,840.00 USD | 41,790.00 USD | 31,790.00 USD |
| `7D` | `823.40` | 69,630,000.00 USD | 69,630,000.00 USD | 0.00 USD | 213,450.00 USD | 68,530.00 USD | 45,900.00 USD |
| `1D` | `823.90` | 70,290,000.00 USD | 70,290,000.00 USD | 0.00 USD | 173,720.00 USD | 36,950.00 USD | 17,890.00 USD |
| `7D` | `824.30` | 69,980,000.00 USD | 69,980,000.00 USD | 0.00 USD | 248,860.00 USD | 58,170.00 USD | 43,880.00 USD |
| `1D` | `825.10` | 70,430,000.00 USD | 70,430,000.00 USD | 0.00 USD | 86,360.00 USD | 26,950.00 USD | 27,680.00 USD |
| `7D` | `825.20` | 70,340,000.00 USD | 70,340,000.00 USD | 0.00 USD | 277,990.00 USD | 21,630.00 USD | 61,140.00 USD |
| `7D` | `826.10` | 70,650,000.00 USD | 70,650,000.00 USD | 0.00 USD | 223,810.00 USD | 27,390.00 USD | 53,050.00 USD |
| `1D` | `826.30` | 70,650,000.00 USD | 70,650,000.00 USD | 0.00 USD | 137,210.00 USD | 35,550.00 USD | 52,670.00 USD |
| `7D` | `827.00` | 71,290,000.00 USD | 71,290,000.00 USD | 0.00 USD | 494,310.00 USD | 23,200.00 USD | 126,570.00 USD |
| `1D` | `827.50` | 71,080,000.00 USD | 71,080,000.00 USD | 0.00 USD | 342,740.00 USD | 17,720.00 USD | 65,600.00 USD |
| `7D` | `827.90` | 71,650,000.00 USD | 71,650,000.00 USD | 0.00 USD | 297,880.00 USD | 0.00 USD | 63,990.00 USD |
| `1D` | `828.30` | 71,220,000.00 USD | 71,220,000.00 USD | 0.00 USD | 140,560.00 USD | 0.00 USD | 0.00 USD |
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
  * Total Open Interest: `1.39B` | Total OI Tokens: `1,937,581.8 BNB`
  * 1h OI Change: `+14.40%` | 4h OI Change: `+12.65%` | 24h OI Change: `+9.57%`
  * Exchange Breakdown: Binance=`614.65M` | Bybit=`138.60M` | OKX=`60.44M` | Hyperliquid=`98.05M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-27.64K` | Last 24h: `109.28K` | Last 3d: `307.00K` | Last 7d: `451.01K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0000%` | **USDT OKX** | `0.0080%` |
| **USDT Bybit** | `-0.0253%` | **USDT KuCoin** | `-0.0006%` |
| **USDT MEXC** | `0.0000%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0099%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0000%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `BNB` | `54.97%` | `45.03%` | `1.22` | 115,730,000.00 USD |
| `15M` | `Binance` | `53.99%` | `46.01%` | `1.17` | 49,200,000.00 USD |
| `15M` | `OKX` | `53.45%` | `46.55%` | `1.15` | 11,670,000.00 USD |
| `15M` | `Bybit` | `50.3%` | `49.7%` | `1.01` | 20,220,000.00 USD |
| `15M` | `KuCoin` | `51.64%` | `48.36%` | `1.07` | 2,340,000.00 USD |
| `15M` | `Gate` | `67.37%` | `32.63%` | `2.06` | 3,060,000.00 USD |
| `15M` | `Bitget` | `55.37%` | `44.63%` | `1.24` | 6,250,000.00 USD |
| `15M` | `BingX` | `51.69%` | `48.31%` | `1.07` | 1,450,000.00 USD |
| `15M` | `MEXC` | `59.79%` | `40.21%` | `1.49` | 10,460,000.00 USD |
| `15M` | `Bitunix` | `54.15%` | `45.85%` | `1.18` | 4,060,000.00 USD |
| `15M` | `Hyperliquid` | `64.01%` | `35.99%` | `1.78` | 3,730,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `66.98%` | `33.02%` | `2.03` | 295,180.00 USD |
| `15M` | `Crypto.com` | `47.15%` | `52.85%` | `0.89` | 124,560.00 USD |
| `15M` | `WhiteBIT` | `96.66%` | `3.34%` | `28.94` | 811,810.00 USD |
| `15M` | `HTX` | `46.91%` | `53.09%` | `0.88` | 54,460.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `65.53%` | `34.47%` | `1.90` | 974,630.00 USD |
| `15M` | `Aster` | `58.78%` | `41.22%` | `1.43` | 866,310.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `67.16%` | `32.84%` | `2.05` | 146,530.00 USD |
| `15M` | `Whale Positions` | `53.99%` | `46.01%` | `1.17` | 49,200,000.00 USD |
| `15M` | `Global Accounts` | `54.97%` | `45.03%` | `1.22` | 115,730,000.00 USD |
| `1H` | `BNB` | `44.48%` | `55.52%` | `0.80` | 821,540,000.00 USD |
| `1H` | `Binance` | `44.68%` | `55.32%` | `0.81` | 321,380,000.00 USD |
| `1H` | `OKX` | `45.99%` | `54.01%` | `0.85` | 114,510,000.00 USD |
| `1H` | `Bybit` | `41.14%` | `58.86%` | `0.70` | 130,920,000.00 USD |
| `1H` | `KuCoin` | `46.43%` | `53.57%` | `0.87` | 14,220,000.00 USD |
| `1H` | `Gate` | `49.62%` | `50.38%` | `0.98` | 10,300,000.00 USD |
| `1H` | `Bitget` | `47.23%` | `52.77%` | `0.90` | 36,240,000.00 USD |
| `1H` | `BingX` | `36.33%` | `63.67%` | `0.57` | 10,640,000.00 USD |
| `1H` | `MEXC` | `42.5%` | `57.5%` | `0.74` | 71,520,000.00 USD |
| `1H` | `Bitunix` | `46.01%` | `53.99%` | `0.85` | 28,950,000.00 USD |
| `1H` | `Hyperliquid` | `42.95%` | `57.05%` | `0.75` | 56,700,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `41.15%` | `58.85%` | `0.70` | 3,710,000.00 USD |
| `1H` | `Crypto.com` | `48.64%` | `51.36%` | `0.95` | 1,470,000.00 USD |
| `1H` | `WhiteBIT` | `83.84%` | `16.16%` | `5.19` | 6,420,000.00 USD |
| `1H` | `HTX` | `47.97%` | `52.03%` | `0.92` | 487,520.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `51.78%` | `48.22%` | `1.07` | 4,630,000.00 USD |
| `1H` | `Aster` | `44.75%` | `55.25%` | `0.81` | 8,340,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `49.77%` | `50.23%` | `0.99` | 1,130,000.00 USD |
| `1H` | `Whale Positions` | `44.68%` | `55.32%` | `0.81` | 321,380,000.00 USD |
| `1H` | `Global Accounts` | `44.48%` | `55.52%` | `0.80` | 821,540,000.00 USD |
| `4H` | `BNB` | `44.02%` | `55.98%` | `0.79` | 1,300,000,000.00 USD |
| `4H` | `Binance` | `44.09%` | `55.91%` | `0.79` | 482,060,000.00 USD |
| `4H` | `OKX` | `44.14%` | `55.86%` | `0.79` | 167,390,000.00 USD |
| `4H` | `Bybit` | `40.85%` | `59.15%` | `0.69` | 195,760,000.00 USD |
| `4H` | `KuCoin` | `46.27%` | `53.73%` | `0.86` | 19,450,000.00 USD |
| `4H` | `Gate` | `48.51%` | `51.49%` | `0.94` | 31,640,000.00 USD |
| `4H` | `Bitget` | `43.49%` | `56.51%` | `0.77` | 69,520,000.00 USD |
| `4H` | `BingX` | `31.95%` | `68.05%` | `0.47` | 25,160,000.00 USD |
| `4H` | `MEXC` | `43.08%` | `56.92%` | `0.76` | 122,440,000.00 USD |
| `4H` | `Bitunix` | `46.15%` | `53.85%` | `0.86` | 57,810,000.00 USD |
| `4H` | `Hyperliquid` | `41.67%` | `58.33%` | `0.71` | 67,210,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.62%` | `51.38%` | `0.95` | 5,760,000.00 USD |
| `4H` | `Crypto.com` | `49.92%` | `50.08%` | `1.00` | 2,150,000.00 USD |
| `4H` | `WhiteBIT` | `73.26%` | `26.74%` | `2.74` | 26,780,000.00 USD |
| `4H` | `HTX` | `55.11%` | `44.89%` | `1.23` | 984,750.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `43.71%` | `56.29%` | `0.78` | 6,960,000.00 USD |
| `4H` | `Aster` | `46.23%` | `53.77%` | `0.86` | 13,500,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `48.02%` | `51.98%` | `0.92` | 1,700,000.00 USD |
| `4H` | `Whale Positions` | `44.09%` | `55.91%` | `0.79` | 482,060,000.00 USD |
| `4H` | `Global Accounts` | `44.02%` | `55.98%` | `0.79` | 1,300,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `745.05` | `744.69` | `745.05` | `745.65` | `743.85` | 1,732,972.70 USD | 1,039,625.11 USD | 693,347.59 USD | 346,277.52 USD | `+19.98%` | `0B / 0S` |
| `0:00 UTC` | `744.15` | `744.46` | `744.15` | `745.35` | `743.85` | 2,147,535.09 USD | 1,307,335.66 USD | 840,199.43 USD | 467,136.24 USD | `+21.75%` | `0B / 0S` |
| `5:00 UTC` | `744.45` | `744.43` | `744.45` | `745.05` | `743.85` | 1,240,697.54 USD | 644,810.68 USD | 595,886.86 USD | 48,923.82 USD | `+3.94%` | `0B / 0S` |
| `0:00 UTC` | `745.35` | `745.38` | `745.35` | `746.25` | `744.45` | 2,107,319.68 USD | 1,122,788.81 USD | 984,530.87 USD | 138,257.94 USD | `+6.56%` | `1B / 1S` |
| `5:00 UTC` | `745.35` | `745.55` | `745.35` | `746.25` | `745.05` | 1,714,180.55 USD | 1,005,910.28 USD | 708,270.27 USD | 297,640.01 USD | `+17.36%` | `2B / 0S` |
| `0:00 UTC` | `739.95` | `741.09` | `739.95` | `745.65` | `737.55` | 21,388,145.47 USD | 6,350,590.17 USD | 15,037,555.30 USD | -8,686,965.13 USD | `-40.62%` | `2B / 11S` |
| `5:00 UTC` | `733.05` | `735.28` | `733.05` | `741.15` | `730.35` | 58,847,128.96 USD | 25,808,552.51 USD | 33,038,576.45 USD | -7,230,023.95 USD | `-12.29%` | `2B / 6S` |
| `0:00 UTC` | `693.15` | `709.93` | `693.15` | `733.35` | `688.35` | 287,121,588.96 USD | 130,602,079.05 USD | 156,519,509.92 USD | -25,917,430.87 USD | `-9.03%` | `0B / 21S` |
| `5:00 UTC` | `694.05` | `694.59` | `694.05` | `707.85` | `677.85` | 179,693,058.88 USD | 96,266,693.98 USD | 83,426,364.90 USD | 12,840,329.08 USD | `+7.15%` | `3B / 4S` |
| `0:00 UTC` | `705.15` | `704.30` | `705.15` | `718.65` | `690.75` | 169,802,008.70 USD | 93,524,348.57 USD | 76,277,660.14 USD | 17,246,688.43 USD | `+10.16%` | `13B / 2S` |

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
| `5m` | -3,070,000.00 USD | -6,000,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -1,700,000.00 USD | 15,780,000.00 USD | **`ACCUMULATION`** |
| `30m` | -5,430,000.00 USD | 32,170,000.00 USD | **`ACCUMULATION`** |
| `1h` | -13,850,000.00 USD | -44,250,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -19,240,000.00 USD | -54,200,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -20,310,000.00 USD | -54,280,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -21,610,000.00 USD | -62,200,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -17,150,000.00 USD | -48,910,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -33,660,000.00 USD | -62,360,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -14,970,000.00 USD | -84,050,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -45,510,000.00 USD | -99,040,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -144,090,000.00 USD | -423,480,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-3.07M` | 15m=`-1.70M` | 1h=`-13.85M` | 24h=`-14.97M`
* Futures Capital Netflows: 5m=`-6.00M` | 15m=`+15.78M` | 1h=`-44.25M` | 24h=`-84.05M`
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
  * `2026-10-30 02:15:06 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:41:06 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:41:06 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:41:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:40:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:42:06 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:42:06 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:42:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:42:06 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)


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
  * Execution Entry: `697.59` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `685.51` (Risk Distance: `12.08` pts)
  * +2.5R Take Profit: `727.78`
  * Mathematical Lot Sizing: **`0.82 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `715.61` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `727.69` (Risk Distance: `12.08` pts)
  * +2.5R Take Profit: `685.42`
  * Mathematical Lot Sizing: **`0.82 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`715.48`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
