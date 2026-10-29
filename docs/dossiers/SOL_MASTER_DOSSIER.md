# 🏛️ SOVEREIGN CANDIDATE DOSSIER: SOL
**Canonical Key**: `SOL` | **Broker Instrument**: `SOLUSD.p` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 01:51:14 IST` (`2026-10-29 20:21:14 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `98.78` | **Live Ask Quote**: `99.02` | **Mid Price**: `98.90`
- **Spread Points**: `24.00` | **Spread BPS**: `24.27 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `100.41` | VWAP Z-Score: `-1.03` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.4791` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `31.52` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `102.96` | Lower -3.00σ Band: `97.86`
  * Upper +2.51σ Band: `102.54` | Lower -2.51σ Band: `98.28`
  * Upper +2.01σ Band: `102.12` | Lower -2.01σ Band: `98.70`
  * Upper +2.00σ Band: `102.11` | Lower -2.00σ Band: `98.71`
  * Upper +1.28σ Band: `101.50` | Lower -1.28σ Band: `99.32`
  * Upper +1.00σ Band: `101.26` | Lower -1.00σ Band: `99.56`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`100.21` | EMA-20=`100.59` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`100.67` (Slope: `+0.0000`) | EMA-100=`100.74`
  * Institutional Anchors: EMA-144=`100.76` | EMA-200=`100.73` (Slope: `-0.0347`) | EMA-233=`100.70`
- **Range Boundaries**: 24H High=`103.63` | 24H Low=`98.95` | Weekly High=`103.63` | Weekly Low=`98.85`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `101.20` (Distance: `-2.29%`)
  * Point of Control (POC) = `99.95` (Distance: `-1.06%`)
  * Value Area Low (VAL) = `99.04` (Distance: `-0.15%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`102.11` | POC=`100.90` | VAL=`100.63`
  * Prior Day Extremes: PDH=`103.63` | PDL=`100.15` | PDC=`102.27`
  * Monday Range Blueprint: High=`102.46` | Mid=`101.01` | Low=`99.56`
  * Developing Weekly Value Area: Weekly VAH=`101.47` | Weekly POC=`100.80` | Weekly VAL=`99.66`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`102.77` | Low=`98.95`
  * London Session (08:00-16:00 UTC): High=`100.61` | Low=`99.44`
  * New York Session (13:00-21:00 UTC): High=`102.93` | Low=`99.78`
  * Initial Balance (First Hour): IB High=`100.61` | IB Low=`99.91`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `98.50` - `99.30`
  * Optimal Trade Entry (OTE 0.705): `99.10`
  * Structural Invalidation Anchor (0.786): `99.69`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `99.78` | `99.90` | `99.00` | `99.03` | `595,505` | 59,206,308.60 USD | -24,885,547.75 USD | `-42.03%` | -107,217,515.79 USD | `-4.08` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `99.03` | `99.04` | `98.33` | `98.80` | `506,436` | 49,984,824.35 USD | -2,608,022.37 USD | `-5.22%` | -109,825,538.16 USD | `-0.15` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `98.79` | `99.21` | `98.45` | `99.03` | `280,005` | 27,707,579.34 USD | 10,831,930.56 USD | `+39.09%` | -98,993,607.60 USD | `+1.89` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `100.18` | `100.37` | `100.08` | `100.09` | `160,050` | 16,033,450.26 USD | 1,955,816.89 USD | `+12.20%` | -80,335,662.30 USD | `+1.17` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `100.08` | `100.21` | `99.76` | `99.78` | `315,037` | 31,495,982.01 USD | -1,996,305.75 USD | `-6.34%` | -82,331,968.05 USD | `-0.18` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `99.78` | `99.90` | `98.33` | `99.01` | `1,381,814` | 136,885,614.60 USD | -16,673,251.96 USD | `-12.18%` | -99,005,220.00 USD | `-3.35` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `101.06` | `101.18` | `100.29` | `100.57` | `555,290` | 55,901,104.31 USD | -7,049,401.02 USD | `-12.61%` | -75,438,050.93 USD | `-0.46` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `100.57` | `100.61` | `99.76` | `99.78` | `679,393` | 68,026,040.28 USD | -1,354,724.67 USD | `-1.99%` | -76,792,775.60 USD | `+0.26` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `99.78` | `99.90` | `98.33` | `99.01` | `1,381,814` | 136,885,614.60 USD | -16,673,251.96 USD | `-12.18%` | -93,466,027.55 USD | `-1.51` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `100.34` | `102.70` | `100.03` | `102.66` | `4,178,003` | 423,242,147.26 USD | -1,557,927.33 USD | `-0.37%` | -35,217,193.40 USD | `+0.47` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `102.66` | `103.16` | `99.76` | `99.78` | `3,108,106` | 314,906,395.99 USD | -32,242,782.78 USD | `-10.24%` | -67,459,976.18 USD | `-1.12` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `99.78` | `99.90` | `98.33` | `99.01` | `1,381,814` | 136,885,614.60 USD | -16,673,251.96 USD | `-12.18%` | -84,133,228.13 USD | `-0.17` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `99.63` | `100.78` | `99.40` | `99.71` | `1,690,194` | 169,196,763.38 USD | 5,656,394.57 USD | `+3.34%` | -29,365,912.19 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `99.71` | `100.79` | `99.70` | `100.34` | `1,518,349` | 152,283,655.59 USD | -4,293,353.88 USD | `-2.82%` | -33,659,266.07 USD | `+0.40` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `100.34` | `102.70` | `100.03` | `102.66` | `4,178,003` | 423,242,147.26 USD | -1,557,927.33 USD | `-0.37%` | -35,217,193.40 USD | `+0.47` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `102.66` | `103.16` | `99.76` | `99.78` | `3,108,106` | 314,906,395.99 USD | -32,242,782.78 USD | `-10.24%` | -67,459,976.18 USD | `-1.12` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `99.78` | `99.90` | `98.33` | `99.01` | `1,381,814` | 136,885,614.60 USD | -16,673,251.96 USD | `-12.18%` | -84,133,228.13 USD | `-0.17` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`98.90`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `99.00` | `72.2000` | 7,148.16 USD | 173,354.38 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `99.00` | `1831.6700` | 181,342.66 USD | 354,697.04 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `99.00` | `825.8300` | 81,758.82 USD | 436,455.86 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `99.00` | `5.6900` | 563.32 USD | 437,019.17 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `99.01` | `41.3100` | 4,090.23 USD | 67,527.05 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `99.01` | `314.4900` | 31,138.28 USD | 98,665.33 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `99.01` | `98.3100` | 9,733.77 USD | 108,399.10 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `99.01` | `182.8600` | 18,104.97 USD | 126,504.07 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `99.01` | `208.8500` | 20,678.03 USD | 147,182.10 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `99.01` | `46.8200` | 4,635.55 USD | 151,817.66 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `99.01` | `19.2000` | 1,900.93 USD | 153,718.59 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `99.01` | `126.1300` | 12,487.63 USD | 166,206.22 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `99.02` | `138.6900` | 13,733.08 USD | 54,571.67 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `99.02` | `66.2300` | 6,558.03 USD | 61,129.70 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `99.02` | `23.3000` | 2,307.12 USD | 63,436.82 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `99.03` | `192.7900` | 19,092.76 USD | 19,945.50 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `99.03` | `144.9500` | 14,354.40 USD | 34,299.90 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `99.03` | `66.0300` | 6,538.69 USD | 40,838.59 USD | `1 orders` | `-0.02%` | `-` |
| `ASK` | `99.04` | `246.7300` | 24,437.13 USD | 298,046.38 USD | `3 orders` | `+0.00%` | `-` |
| `ASK` | `99.04` | `2762.5300` | 273,609.26 USD | 273,609.26 USD | `24 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `99.04` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 99.04` | `0.00%` | `-` |
| `BID` | `99.04` | `6.6000` | 653.68 USD | 653.68 USD | `2 orders` | `-0.00%` | `-` |
| `BID` | `99.04` | `2.0100` | 199.06 USD | 852.74 USD | `1 orders` | `-0.01%` | `-` |
| `ASK` | `99.05` | `80.7600` | 7,999.60 USD | 559,598.20 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `99.05` | `85.8000` | 8,498.75 USD | 551,598.60 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `99.05` | `80.7600` | 7,999.44 USD | 543,099.85 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `99.05` | `106.8300` | 10,581.62 USD | 535,100.41 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `99.05` | `142.7000` | 14,134.43 USD | 524,518.80 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `99.05` | `1188.6300` | 117,732.61 USD | 510,384.36 USD | `5 orders` | `+0.01%` | `-` |
| `ASK` | `99.05` | `327.4800` | 32,436.24 USD | 392,651.75 USD | `5 orders` | `+0.01%` | `-` |
| `ASK` | `99.05` | `133.9500` | 13,267.35 USD | 360,215.51 USD | `3 orders` | `+0.00%` | `-` |
| `ASK` | `99.05` | `291.2400` | 28,846.16 USD | 346,948.16 USD | `4 orders` | `+0.00%` | `-` |
| `ASK` | `99.05` | `202.4900` | 20,055.62 USD | 318,102.01 USD | `2 orders` | `+0.00%` | `-` |
| `ASK` | `99.06` | `42.6600` | 4,225.98 USD | 1,511,394.88 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `99.06` | `2035.2100` | 201,609.94 USD | 1,507,168.89 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `99.06` | `4515.5000` | 447,305.43 USD | 1,305,558.96 USD | `13 orders` | `+0.02%` | `-` |
| `ASK` | `99.06` | `448.1000` | 44,388.34 USD | 858,253.53 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `99.06` | `2044.5200` | 202,526.06 USD | 813,865.19 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `99.06` | `92.2300` | 9,136.03 USD | 611,339.13 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `99.06` | `349.3500` | 34,605.21 USD | 602,203.10 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `99.06` | `80.7600` | 7,999.68 USD | 567,597.88 USD | `2 orders` | `+0.01%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:44:44 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `14` | `0x5b5d...c060` | `SHORT` | 71,495,602.71 USD | `721,165.26` | `94.33` | `99.12` | `323.33` | -3,464,712.30 USD | `-4.85%` | `7X Cross` |
| `22` | `0x9c6a...a4ed` | `LONG` | 54,400,922.10 USD | `550,087.69` | `80.86` | `99.12` | `68.18` | 9,921,935.71 USD | `+18.24%` | `20X Cross` |
| `49` | `0xb83d...6e36` | `SHORT` | 25,636,344.73 USD | `259,300.02` | `91.42` | `99.12` | `628.59` | -1,931,211.71 USD | `-7.53%` | `5X Cross` |
| `80` | `0x3dc9...54b0` | `SHORT` | 21,768,886.80 USD | `220,000.19` | `105.90` | `99.12` | `167.99` | 1,530,220.48 USD | `+7.03%` | `20X Cross` |
| `104` | `0x9c89...600e` | `LONG` | 18,712,493.57 USD | `189,472.50` | `115.21` | `99.12` | `34.78` | -3,116,521.69 USD | `-16.65%` | `20X Cross` |
| `112` | `0x4a20...3c26` | `LONG` | 17,845,020.00 USD | `180,000.00` | `106.43` | `99.12` | `66.15` | -1,313,258.71 USD | `-7.36%` | `20X Cross` |
| `137` | `0xecb6...2b00` | `SHORT` | 14,867,880.39 USD | `149,997.28` | `102.71` | `99.12` | `287.01` | 538,465.23 USD | `+3.62%` | `20X Cross` |
| `199` | `0x7a5a...0394` | `SHORT` | 10,817,700.82 USD | `109,114.30` | `100.79` | `99.12` | `123.97` | 179,426.97 USD | `+1.66%` | `10X Cross` |
| `209` | `0x13da...08be` | `LONG` | 10,442,241.47 USD | `105,329.30` | `100.47` | `99.12` | `98.01` | -140,318.62 USD | `-1.34%` | `20X Isolated` |
| `233` | `0xc63a...a3cd` | `LONG` | 9,892,000.00 USD | `100,000.00` | `112.22` | `99.12` | `0.000000` | -1,330,108.97 USD | `-13.45%` | `20X Cross` |
| `270` | `0xb581...6f4f` | `LONG` | 8,888,490.00 USD | `90,000.00` | `114.59` | `99.12` | `0.000000` | -1,424,802.29 USD | `-16.03%` | `3X Cross` |
| `294` | `0x645b...87b8` | `SHORT` | 8,268,145.15 USD | `83,605.29` | `103.91` | `99.12` | `339.50` | 418,984.01 USD | `+5.07%` | `20X Cross` |
| `299` | `0xdb3a...cf3b` | `LONG` | 8,106,272.88 USD | `81,851.78` | `106.04` | `99.12` | `47.78` | -573,473.97 USD | `-7.07%` | `4X Cross` |
| `319` | `0xe927...98ef` | `LONG` | 7,719,582.00 USD | `78,000.00` | `96.34` | `99.12` | `38.44` | 205,440.52 USD | `+2.66%` | `3X Cross` |
| `327` | `0xca49...53c8` | `SHORT` | 7,331,049.41 USD | `73,943.45` | `110.70` | `99.12` | `279.27` | 854,572.85 USD | `+11.66%` | `20X Cross` |
| `331` | `0x8ae4...3d60` | `LONG` | 7,142,143.77 USD | `72,180.05` | `111.72` | `99.12` | `4.00` | -922,016.47 USD | `-12.91%` | `10X Cross` |
| `338` | `0xa0b7...6165` | `SHORT` | 7,025,937.92 USD | `71,044.42` | `107.87` | `99.12` | `190.90` | 637,529.28 USD | `+9.07%` | `2X Cross` |
| `354` | `0xf517...c032` | `SHORT` | 6,713,870.07 USD | `67,778.53` | `84.64` | `99.12` | `230.61` | -976,838.90 USD | `-14.55%` | `20X Cross` |
| `478` | `0x7e23...5a5a` | `LONG` | 4,808,911.30 USD | `48,564.56` | `105.17` | `99.12` | `67.55` | -298,657.87 USD | `-6.21%` | `5X Isolated` |
| `578` | `0x7fda...17d1` | `SHORT` | 4,007,387.69 USD | `40,429.25` | `103.65` | `99.12` | `1025.01` | 183,227.90 USD | `+4.57%` | `20X Cross` |
| `585` | `0x2e2b...2fab` | `LONG` | 3,960,840.00 USD | `40,000.00` | `119.55` | `99.12` | `55.01` | -821,195.64 USD | `-20.73%` | `10X Cross` |
| `608` | `0xf899...88db` | `SHORT` | 3,817,416.86 USD | `38,586.27` | `87.86` | `99.12` | `117.41` | -427,041.67 USD | `-11.19%` | `20X Cross` |
| `620` | `0x9946...0852` | `SHORT` | 3,746,022.86 USD | `37,784.80` | `112.11` | `99.12` | `131.84` | 490,204.46 USD | `+13.09%` | `20X Cross` |
| `641` | `0x27b8...12fc` | `LONG` | 3,573,540.97 USD | `36,085.73` | `110.86` | `99.12` | `16.10` | -426,804.28 USD | `-11.94%` | `10X Cross` |
| `647` | `0x9c16...4a6f` | `SHORT` | 3,545,713.77 USD | `35,779.15` | `90.45` | `99.12` | `128.52` | -309,608.74 USD | `-8.73%` | `20X Cross` |
| `653` | `0x3440...32c5` | `SHORT` | 3,518,804.04 USD | `35,529.12` | `95.02` | `99.12` | `170.29` | -142,782.61 USD | `-4.06%` | `20X Cross` |
| `663` | `0xfc66...ca06` | `SHORT` | 3,477,371.75 USD | `35,149.11` | `101.68` | `99.12` | `1107.05` | 96,646.64 USD | `+2.78%` | `20X Cross` |
| `723` | `0x023a...2355` | `SHORT` | 3,184,776.69 USD | `32,188.97` | `101.45` | `99.12` | `353.13` | 80,693.95 USD | `+2.53%` | `20X Cross` |
| `727` | `0x96a7...79df` | `LONG` | 3,166,112.00 USD | `32,000.00` | `74.39` | `99.12` | `0.000000` | 785,706.15 USD | `+24.82%` | `20X Cross` |
| `773` | `0xbe19...8bd1` | `SHORT` | 3,019,011.00 USD | `30,451.69` | `97.62` | `99.12` | `743.91` | -46,464.37 USD | `-1.54%` | `3X Cross` |
| `775` | `0x482b...cae4` | `SHORT` | 3,004,951.67 USD | `30,310.49` | `88.03` | `99.12` | `154.26` | -336,703.38 USD | `-11.20%` | `20X Cross` |
| `789` | `0x610b...b613` | `LONG` | 2,932,861.20 USD | `29,634.14` | `101.23` | `99.12` | `70.39` | -67,138.15 USD | `-2.29%` | `3X Isolated` |
| `798` | `0x45d2...4029` | `SHORT` | 2,896,315.62 USD | `29,220.00` | `93.28` | `99.12` | `1403.66` | -170,539.64 USD | `-5.89%` | `20X Cross` |
| `807` | `0xa61c...66b9` | `LONG` | 2,860,951.97 USD | `28,888.00` | `104.39` | `99.12` | `0.000000` | -154,612.15 USD | `-5.40%` | `5X Cross` |
| `846` | `0x458d...ab3b` | `LONG` | 2,709,502.25 USD | `27,385.03` | `117.17` | `99.12` | `81.07` | -499,160.26 USD | `-18.42%` | `3X Isolated` |
| `871` | `0xfc27...9d9d` | `SHORT` | 2,601,287.91 USD | `26,243.56` | `102.67` | `99.12` | `673.35` | 93,168.10 USD | `+3.58%` | `20X Cross` |
| `913` | `0x051c...693c` | `LONG` | 2,488,830.30 USD | `25,139.70` | `89.76` | `99.12` | `24.92` | 232,268.97 USD | `+9.33%` | `20X Cross` |
| `943` | `0x638f...f5f0` | `LONG` | 2,379,456.00 USD | `24,000.00` | `136.71` | `99.12` | `43.70` | -901,512.54 USD | `-37.89%` | `20X Cross` |
| `1002` | `0x7178...0854` | `LONG` | 2,230,445.68 USD | `22,545.24` | `110.94` | `99.12` | `32.65` | -270,698.79 USD | `-12.14%` | `10X Cross` |
| `1019` | `0x739c...cfb2` | `LONG` | 2,176,886.80 USD | `22,000.00` | `91.95` | `99.12` | `73.17` | 153,979.49 USD | `+7.07%` | `20X Cross` |
| `1029` | `0x69cc...14fd` | `SHORT` | 2,151,515.35 USD | `21,701.57` | `99.01` | `99.12` | `461.28` | -2,862.60 USD | `-0.13%` | `20X Cross` |
| `1107` | `0x7737...bf66` | `SHORT` | 2,016,635.82 USD | `20,384.06` | `102.94` | `99.12` | `969.22` | 81,706.07 USD | `+4.05%` | `10X Cross` |
| `1139` | `0xea00...a918` | `LONG` | 1,981,233.16 USD | `20,022.69` | `66.09` | `99.12` | `0.000000` | 657,924.56 USD | `+33.21%` | `20X Cross` |
| `1140` | `0x251f...6e5d` | `LONG` | 1,980,800.00 USD | `20,000.00` | `101.15` | `99.12` | `52.20` | -42,297.77 USD | `-2.14%` | `20X Cross` |
| `1141` | `0xdf60...d3c7` | `LONG` | 1,980,420.00 USD | `20,000.00` | `120.12` | `99.12` | `94.00` | -421,988.53 USD | `-21.31%` | `7X Isolated` |
| `1143` | `0x3fc5...c0c1` | `SHORT` | 1,978,988.00 USD | `20,000.00` | `98.28` | `99.12` | `209.01` | -13,428.16 USD | `-0.68%` | `20X Cross` |
| `1144` | `0xbfc7...80b4` | `SHORT` | 1,978,800.00 USD | `20,000.00` | `85.98` | `99.12` | `337.39` | -259,265.50 USD | `-13.10%` | `20X Cross` |
| `1157` | `0xb322...d51f` | `LONG` | 1,958,814.57 USD | `19,774.82` | `102.98` | `99.12` | `56.53` | -77,656.83 USD | `-3.96%` | `20X Cross` |
| `1164` | `0x34e6...8d74` | `LONG` | 1,951,698.07 USD | `19,688.07` | `101.19` | `99.12` | `53.20` | -40,465.73 USD | `-2.07%` | `20X Cross` |
| `1168` | `0x936c...bb0f` | `SHORT` | 1,947,034.06 USD | `19,639.04` | `105.58` | `99.12` | `635.00` | 126,487.14 USD | `+6.50%` | `20X Cross` |
| `1180` | `0x7160...d47c` | `LONG` | 1,925,064.21 USD | `19,434.10` | `105.03` | `99.12` | `80.57` | -116,157.08 USD | `-6.03%` | `20X Cross` |
| `1199` | `0xe097...d0fe` | `LONG` | 1,881,225.11 USD | `18,995.75` | `109.71` | `99.12` | `0.000000` | -202,771.78 USD | `-10.78%` | `20X Cross` |
| `1295` | `0xe98b...8cd5` | `SHORT` | 1,743,115.30 USD | `17,622.89` | `187.95` | `99.12` | `260.94` | 1,569,105.43 USD | `+90.02%` | `20X Cross` |
| `1302` | `0xdf95...7d72` | `SHORT` | 1,733,760.87 USD | `17,487.30` | `104.68` | `99.12` | `2255.56` | 96,860.02 USD | `+5.59%` | `20X Cross` |
| `1334` | `0xee2b...d67e` | `LONG` | 1,680,560.20 USD | `16,963.19` | `119.86` | `99.12` | `23.57` | -352,711.44 USD | `-20.99%` | `4X Cross` |
| `1345` | `0x123d...3bff` | `LONG` | 1,674,068.50 USD | `16,918.43` | `89.53` | `99.12` | `0.000000` | 159,282.01 USD | `+9.51%` | `10X Cross` |
| `1454` | `0x73d7...8be1` | `LONG` | 1,553,278.68 USD | `15,668.95` | `106.60` | `99.12` | `72.51` | -117,062.28 USD | `-7.54%` | `20X Cross` |
| `1469` | `0xc74a...ab93` | `LONG` | 1,537,088.68 USD | `15,536.82` | `64.06` | `99.12` | `54.88` | 541,859.84 USD | `+35.25%` | `5X Isolated` |
| `1514` | `0xc7d1...51af` | `SHORT` | 1,484,535.00 USD | `15,000.00` | `105.79` | `99.12` | `138.76` | 102,340.00 USD | `+6.89%` | `20X Cross` |
| `1551` | `0xffb2...5ed6` | `LONG` | 1,436,324.47 USD | `14,504.05` | `117.89` | `99.12` | `88.51` | -273,580.24 USD | `-19.05%` | `20X Cross` |
| `1578` | `0x0d6a...ca57` | `LONG` | 1,405,739.49 USD | `14,206.65` | `110.41` | `99.12` | `91.60` | -162,850.86 USD | `-11.58%` | `5X Isolated` |
| `1612` | `0x7277...0b98` | `SHORT` | 1,371,883.42 USD | `13,837.70` | `101.18` | `99.12` | `197.30` | 28,236.35 USD | `+2.06%` | `20X Cross` |
| `1859` | `0x2482...0e55` | `LONG` | 1,120,636.16 USD | `11,363.98` | `122.03` | `99.12` | `94.24` | -266,065.76 USD | `-23.74%` | `20X Isolated` |
| `1869` | `0xe105...6a47` | `LONG` | 1,109,748.15 USD | `11,205.05` | `107.11` | `99.12` | `92.61` | -90,408.90 USD | `-8.15%` | `20X Cross` |
| `1879` | `0x45db...86eb` | `LONG` | 1,099,277.40 USD | `11,100.00` | `110.69` | `99.12` | `67.97` | -129,404.50 USD | `-11.77%` | `5X Cross` |
| `1915` | `0x1d04...7c43` | `LONG` | 1,069,412.81 USD | `10,811.76` | `111.55` | `99.12` | `21.38` | -136,648.69 USD | `-12.78%` | `6X Cross` |
| `1985` | `0x0a06...2a7b` | `SHORT` | 1,017,642.01 USD | `10,264.80` | `99.76` | `99.12` | `146.96` | 6,383.77 USD | `+0.63%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `130.74` | 1,361.00 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 1.36K USD at 130.7400 USD [API] | `2026-01-21 15:16:43` |
| `ANNOUNCEMENT` | `INFO` | `122.75` | 4,485.28 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 4.49K USD at 122.7500 USD [API] | `2025-12-23 13:36:37` |
| `ANNOUNCEMENT` | `INFO` | `124.95` | 3,751.00 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 3.75K USD at 124.9500 USD [API] | `2025-12-19 07:07:44` |
| `ANNOUNCEMENT` | `INFO` | `124.95` | 820.92 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.82K USD at 124.9500 USD [API] | `2025-12-19 07:07:44` |
| `ANNOUNCEMENT` | `INFO` | `126.81` | 3,182.93 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 3.18K USD at 126.8100 USD [API] | `2025-12-17 15:52:14` |
| `ANNOUNCEMENT` | `INFO` | `125.94` | 1,808.50 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.81K USD at 125.9400 USD [API] | `2025-12-15 16:36:52` |
| `ANNOUNCEMENT` | `INFO` | `125.94` | 1,998.67 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.00K USD at 125.9400 USD [API] | `2025-12-15 16:36:52` |
| `ANNOUNCEMENT` | `INFO` | `125.94` | 1,510.02 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.51K USD at 125.9400 USD [API] | `2025-12-15 16:36:52` |
| `ANNOUNCEMENT` | `INFO` | `129.25` | 4,809.39 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 4.81K USD at 129.2500 USD [API] | `2025-12-14 23:27:00` |
| `ANNOUNCEMENT` | `INFO` | `134.26` | 5,544.94 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 5.54K USD at 134.2600 USD [API] | `2025-12-11 18:35:47` |
| `ANNOUNCEMENT` | `INFO` | `128.92` | 6,032.17 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 6.03K USD at 128.9200 USD [API] | `2025-12-07 14:24:53` |
| `ANNOUNCEMENT` | `INFO` | `140.60` | 6,367.77 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 6.37K USD at 140.6000 USD [API] | `2025-12-04 18:46:05` |
| `ANNOUNCEMENT` | `INFO` | `140.60` | 19.68 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.02K USD at 140.6000 USD [API] | `2025-12-04 18:46:05` |
| `ANNOUNCEMENT` | `INFO` | `140.60` | 12.65 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.01K USD at 140.6000 USD [API] | `2025-12-04 18:46:05` |
| `ANNOUNCEMENT` | `INFO` | `140.60` | 202.46 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.20K USD at 140.6000 USD [API] | `2025-12-04 18:46:05` |
| `ANNOUNCEMENT` | `INFO` | `129.79` | 1,588.63 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 1.59K USD at 129.7900 USD [API] | `2025-12-02 13:16:02` |
| `ANNOUNCEMENT` | `INFO` | `129.79` | 2,040.30 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 2.04K USD at 129.7900 USD [API] | `2025-12-02 13:16:02` |
| `ANNOUNCEMENT` | `INFO` | `129.79` | 2,710.02 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 2.71K USD at 129.7900 USD [API] | `2025-12-02 13:16:02` |
| `ANNOUNCEMENT` | `INFO` | `140.45` | 1,543.55 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 1.54K USD at 140.4500 USD [API] | `2025-11-25 23:19:31` |
| `ANNOUNCEMENT` | `INFO` | `140.45` | 2,490.18 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 2.49K USD at 140.4500 USD [API] | `2025-11-25 23:19:31` |
| `ANNOUNCEMENT` | `INFO` | `101.15` | 86,233.41 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 86.23K USD at 101.1500 USD [API] | `2026-10-27 23:35:20` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`101.14` (Vol: 4,700,000.00 USD, Dist: `+2.21%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 48H Horizon: Short MP=`104.08` (Vol: 4,800,000.00 USD, Dist: `+5.18%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 3D Horizon: Short MP=`101.14` (Vol: 4,700,000.00 USD, Dist: `+2.20%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 7D Horizon: Short MP=`104.05` (Vol: 6,100,000.00 USD, Dist: `+5.14%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `19.85` | 214,610.00 USD | 142,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.95` | 847.08 USD | 141,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.05` | 7,950.00 USD | 141,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.25` | 1,350.00 USD | 141,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.35` | 7,510.00 USD | 141,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.55` | 58,780.00 USD | 141,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.65` | 1,260.00 USD | 141,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.85` | 353,680.00 USD | 141,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.95` | 120,470.00 USD | 141,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.05` | 1,050.00 USD | 141,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.25` | 1,060.00 USD | 141,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.35` | 1,410.00 USD | 141,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.45` | 289.36 USD | 141,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.55` | 993.24 USD | 141,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.75` | 5,360.00 USD | 141,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.95` | 194.48 USD | 141,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.05` | 3,040.00 USD | 141,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.35` | 335.25 USD | 141,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.55` | 159.43 USD | 141,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.75` | 386.30 USD | 141,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.95` | 601,510.00 USD | 141,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.45` | 1,380.00 USD | 140,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.75` | 47,330.00 USD | 140,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.85` | 1,910.00 USD | 140,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.05` | 721.50 USD | 140,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.15` | 939.68 USD | 140,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.25` | 147.92 USD | 140,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.35` | 1,470.00 USD | 140,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.55` | 245.50 USD | 140,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.95` | 1,380.00 USD | 140,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.05` | 1,440.00 USD | 140,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.15` | 2,010.00 USD | 140,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.45` | 106.64 USD | 140,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.55` | 10,650.00 USD | 140,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.75` | 464.27 USD | 140,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.95` | 54,830.00 USD | 140,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.15` | 8,910.00 USD | 140,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.25` | 2,770.00 USD | 140,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.55` | 308.51 USD | 140,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.65` | 309.67 USD | 140,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.35` | 164,540.00 USD | 140,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.45` | 272.30 USD | 140,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.55` | 1,300.00 USD | 140,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.65` | 3,590.00 USD | 140,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.85` | 412.18 USD | 140,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.95` | 605.40 USD | 140,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.05` | 2,930.00 USD | 140,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.25` | 9,610.00 USD | 140,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.35` | 6,200.00 USD | 140,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.45` | 980.96 USD | 140,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.75` | 763.60 USD | 140,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.85` | 825.11 USD | 140,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.95` | 2,920.00 USD | 140,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.15` | 11,590.00 USD | 140,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.25` | 32,410.00 USD | 140,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.45` | 61,700.00 USD | 140,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.55` | 1,480.00 USD | 140,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.75` | 2,760.00 USD | 140,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.05` | 3,010.00 USD | 140,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.15` | 53,500.00 USD | 140,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.35` | 10,380.00 USD | 140,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.55` | 2,590.00 USD | 140,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.65` | 1,910.00 USD | 140,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.75` | 693,470.00 USD | 140,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.95` | 1,070.00 USD | 139,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.15` | 26,940.00 USD | 139,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.25` | 14,760.00 USD | 139,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.35` | 38,730.00 USD | 139,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.45` | 278.33 USD | 139,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.55` | 1,560.00 USD | 139,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.65` | 214.59 USD | 139,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.85` | 911.55 USD | 139,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.95` | 4,350.00 USD | 139,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.15` | 1,450.00 USD | 139,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.75` | 274.77 USD | 139,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.85` | 5,240.00 USD | 139,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.35` | 33,350.00 USD | 139,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.45` | 50,640.00 USD | 139,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.55` | 944.10 USD | 139,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.75` | 318,010.00 USD | 139,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.15` | 4,650.00 USD | 139,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.65` | 3,140.00 USD | 139,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.75` | 6,580,000.00 USD | 139,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.95` | 4,270.00 USD | 132,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.15` | 441.84 USD | 132,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.25` | 17,860.00 USD | 132,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.35` | 340.77 USD | 132,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.75` | 5,880.00 USD | 132,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.95` | 5,610.00 USD | 132,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.15` | 5,570.00 USD | 132,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.35` | 4,410.00 USD | 132,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.45` | 2,410.00 USD | 132,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.55` | 2,940.00 USD | 132,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.75` | 500.90 USD | 132,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.95` | 112,510.00 USD | 132,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.25` | 373.62 USD | 132,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.35` | 38,140.00 USD | 132,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.45` | 1,050.00 USD | 132,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.55` | 2,850.00 USD | 132,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.65` | 2,430.00 USD | 132,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.85` | 189,470.00 USD | 132,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.95` | 4,160.00 USD | 132,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.05` | 542.59 USD | 132,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.45` | 3,000,000.00 USD | 132,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.75` | 2,480.00 USD | 129,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.85` | 4,270.00 USD | 129,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.95` | 607.62 USD | 129,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.05` | 50,470.00 USD | 129,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.25` | 827.00 USD | 129,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.35` | 4,260.00 USD | 129,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.45` | 1,130.00 USD | 129,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.65` | 1,560.00 USD | 129,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.75` | 159.00 USD | 129,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.85` | 1,390.00 USD | 129,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.05` | 10,950.00 USD | 129,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.15` | 15,910.00 USD | 129,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.25` | 41,500.00 USD | 129,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.55` | 3,160.00 USD | 128,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.65` | 7,850.00 USD | 128,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.85` | 2,770.00 USD | 128,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.95` | 5,670.00 USD | 128,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.05` | 10,990.00 USD | 128,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.15` | 3,440.00 USD | 128,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.25` | 368.36 USD | 128,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.35` | 148.45 USD | 128,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.55` | 427.13 USD | 128,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.65` | 770.11 USD | 128,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.75` | 1,380.00 USD | 128,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.85` | 21,150.00 USD | 128,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.95` | 1,210.00 USD | 128,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.05` | 10,340.00 USD | 128,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.15` | 2,590.00 USD | 128,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.25` | 1,020,000.00 USD | 128,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.35` | 307.04 USD | 127,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.65` | 57,330.00 USD | 127,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.75` | 855.00 USD | 127,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.05` | 4,300.00 USD | 127,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.35` | 4,710.00 USD | 127,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.45` | 1,260.00 USD | 127,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.55` | 34,820.00 USD | 127,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.75` | 76,670.00 USD | 127,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.95` | 242.16 USD | 127,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.05` | 11,330.00 USD | 127,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.25` | 18,430.00 USD | 127,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.35` | 22,840.00 USD | 127,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.55` | 17,870.00 USD | 127,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.65` | 125,070.00 USD | 127,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.75` | 59,120.00 USD | 127,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.85` | 3,300.00 USD | 127,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.95` | 4,350.00 USD | 127,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.15` | 179.70 USD | 127,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.35` | 4,100.00 USD | 127,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.45` | 9,980.00 USD | 127,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.55` | 9,050.00 USD | 127,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.65` | 871.00 USD | 127,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.75` | 9,450.00 USD | 127,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.85` | 3,050.00 USD | 127,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.95` | 26,070.00 USD | 127,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.05` | 921,000.00 USD | 127,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.15` | 142.14 USD | 126,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.25` | 2,080.00 USD | 126,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.45` | 824.95 USD | 126,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.55` | 522.76 USD | 126,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.65` | 933,540.00 USD | 126,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.75` | 374.00 USD | 125,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.85` | 140.55 USD | 125,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.95` | 2,090.00 USD | 125,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.05` | 3,850,000.00 USD | 125,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.15` | 51,780.00 USD | 121,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.25` | 3,050.00 USD | 121,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.35` | 400.11 USD | 121,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.55` | 106.04 USD | 121,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.65` | 105,250.00 USD | 121,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.75` | 160.92 USD | 121,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.95` | 435.39 USD | 121,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.05` | 4,630.00 USD | 121,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.15` | 5,470.00 USD | 121,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.25` | 5,510.00 USD | 121,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.35` | 1,970.00 USD | 121,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.45` | 14,710.00 USD | 121,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.55` | 3,770.00 USD | 121,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.65` | 13,880.00 USD | 121,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.75` | 453.38 USD | 121,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.85` | 12,410.00 USD | 121,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.95` | 7,960.00 USD | 121,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.05` | 1,980.00 USD | 121,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.15` | 10,850.00 USD | 121,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.25` | 469.84 USD | 121,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.35` | 585.29 USD | 121,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.45` | 5,700.00 USD | 121,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.55` | 27,880.00 USD | 121,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.65` | 892.21 USD | 121,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.95` | 14,670.00 USD | 121,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.05` | 8,560.00 USD | 121,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.15` | 1,390.00 USD | 121,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.25` | 22,830.00 USD | 121,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.45` | 9,790.00 USD | 121,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.55` | 2,910.00 USD | 121,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.65` | 824.08 USD | 121,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.75` | 12,040.00 USD | 121,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.85` | 19,130.00 USD | 121,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.95` | 2,820.00 USD | 121,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.05` | 2,680.00 USD | 121,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.15` | 61,080.00 USD | 121,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.25` | 11,710.00 USD | 121,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.35` | 6,260.00 USD | 121,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.45` | 8,540.00 USD | 121,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.55` | 17,880.00 USD | 121,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.65` | 774.23 USD | 121,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.75` | 34,200.00 USD | 121,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.85` | 62,680.00 USD | 121,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.95` | 565,190.00 USD | 121,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.05` | 98,480.00 USD | 120,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.15` | 4,270.00 USD | 120,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.25` | 6,720.00 USD | 120,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.35` | 3,980.00 USD | 120,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.45` | 3,540.00 USD | 120,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.55` | 1,740.00 USD | 120,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.65` | 4,420.00 USD | 120,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.75` | 39,500.00 USD | 120,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.85` | 4,380.00 USD | 120,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.95` | 5,360.00 USD | 120,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.05` | 6,430.00 USD | 120,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.15` | 10,150.00 USD | 120,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.25` | 1,050,000.00 USD | 120,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.35` | 2,130.00 USD | 119,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.45` | 34,550.00 USD | 119,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.55` | 46,410.00 USD | 119,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.65` | 2,530.00 USD | 119,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.75` | 18,180.00 USD | 119,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.85` | 6,610.00 USD | 119,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.95` | 83,470.00 USD | 119,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.05` | 2,160,000.00 USD | 119,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.15` | 15,030.00 USD | 116,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.25` | 11,500.00 USD | 116,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.35` | 2,460.00 USD | 116,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.45` | 43,920.00 USD | 116,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.55` | 63,370.00 USD | 116,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.65` | 2,420.00 USD | 116,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.75` | 17,320.00 USD | 116,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.85` | 864,880.00 USD | 116,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.95` | 163,690.00 USD | 115,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.05` | 6,000.00 USD | 115,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.15` | 10,600.00 USD | 115,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.25` | 49,450.00 USD | 115,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.35` | 9,810.00 USD | 115,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.45` | 6,450.00 USD | 115,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.55` | 1,110,000.00 USD | 115,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.65` | 31,860.00 USD | 114,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.75` | 85,360.00 USD | 114,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.85` | 8,280.00 USD | 114,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.05` | 8,360.00 USD | 114,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.15` | 22,690.00 USD | 114,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.25` | 24,190.00 USD | 114,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.35` | 7,880.00 USD | 114,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.45` | 5,350.00 USD | 114,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.55` | 4,730.00 USD | 114,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.65` | 3,590.00 USD | 114,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.75` | 39,680.00 USD | 114,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.85` | 122.80 USD | 114,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.95` | 14,710.00 USD | 114,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.05` | 346,070.00 USD | 114,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.15` | 5,380.00 USD | 113,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.25` | 1,780.00 USD | 113,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.35` | 9,580.00 USD | 113,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.45` | 17,480.00 USD | 113,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.55` | 6,580.00 USD | 113,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.65` | 242.13 USD | 113,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.75` | 42,310.00 USD | 113,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.85` | 28,030.00 USD | 113,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.95` | 324.52 USD | 113,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.05` | 5,010.00 USD | 113,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.15` | 123,440.00 USD | 113,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.25` | 6,670.00 USD | 113,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.35` | 22,100.00 USD | 113,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.45` | 10,130.00 USD | 113,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.55` | 2,970.00 USD | 113,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.65` | 4,640.00 USD | 113,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.75` | 453.55 USD | 113,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.85` | 7,310.00 USD | 113,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.95` | 650.81 USD | 113,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.05` | 12,180.00 USD | 113,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.15` | 6,170.00 USD | 113,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.25` | 19,550.00 USD | 113,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.35` | 28,320.00 USD | 113,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.45` | 9,240.00 USD | 113,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.55` | 8,740.00 USD | 113,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.65` | 5,110.00 USD | 113,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.75` | 13,880.00 USD | 113,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.85` | 150.82 USD | 113,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.95` | 37,880.00 USD | 113,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.05` | 12,840.00 USD | 113,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.15` | 38,140.00 USD | 113,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.25` | 2,340.00 USD | 113,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.35` | 2,090.00 USD | 113,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.45` | 557.35 USD | 113,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.55` | 2,760.00 USD | 113,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.65` | 5,880.00 USD | 113,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.75` | 1,650.00 USD | 113,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.85` | 36,120.00 USD | 113,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.95` | 55,130.00 USD | 113,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.05` | 22,740.00 USD | 113,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.15` | 683.66 USD | 113,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.25` | 125,370.00 USD | 113,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.35` | 19,870.00 USD | 113,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.45` | 14,620.00 USD | 113,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.55` | 2,490.00 USD | 113,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.65` | 21,020.00 USD | 113,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.75` | 16,580.00 USD | 113,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.85` | 18,940.00 USD | 113,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.95` | 14,100.00 USD | 113,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.05` | 4,790.00 USD | 113,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.15` | 25,780.00 USD | 113,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.25` | 1,800.00 USD | 113,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.35` | 31,770.00 USD | 113,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.45` | 120,170.00 USD | 113,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.55` | 3,130.00 USD | 112,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.65` | 2,050.00 USD | 112,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.75` | 3,140.00 USD | 112,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.85` | 31,310.00 USD | 112,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.95` | 74,040.00 USD | 112,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.05` | 17,480.00 USD | 112,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.15` | 81,490.00 USD | 112,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.25` | 14,620.00 USD | 112,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.45` | 43,420.00 USD | 112,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.55` | 10,530.00 USD | 112,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.65` | 9,350.00 USD | 112,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.75` | 8,220.00 USD | 112,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.85` | 87,380.00 USD | 112,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.95` | 12,230.00 USD | 112,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.15` | 4,550.00 USD | 112,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.25` | 4,550.00 USD | 112,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.35` | 875.16 USD | 112,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.45` | 5,800.00 USD | 112,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.55` | 579.66 USD | 112,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.65` | 27,600.00 USD | 112,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.75` | 5,280.00 USD | 112,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.85` | 4,400.00 USD | 112,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.95` | 209.79 USD | 112,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.05` | 18,350.00 USD | 112,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.15` | 12,400.00 USD | 112,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.25` | 844.34 USD | 112,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.35` | 15,790.00 USD | 112,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.45` | 11,800,000.00 USD | 112,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.55` | 23,320.00 USD | 100,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.65` | 58,050.00 USD | 100,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.75` | 1,620.00 USD | 100,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.85` | 14,380.00 USD | 100,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.95` | 11,240.00 USD | 100,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.05` | 605.68 USD | 100,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.15` | 17,760.00 USD | 100,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.25` | 1,180.00 USD | 100,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.35` | 1,200.00 USD | 100,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.55` | 42,920.00 USD | 100,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.65` | 842.46 USD | 100,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.85` | 4,420.00 USD | 100,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.95` | 937.30 USD | 100,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.05` | 33,620.00 USD | 100,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.15` | 2,510.00 USD | 100,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.25` | 13,780.00 USD | 100,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.35` | 1,050.00 USD | 100,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.45` | 270.47 USD | 100,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.55` | 106,280.00 USD | 100,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.65` | 159,710.00 USD | 100,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.75` | 7,740.00 USD | 100,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.85` | 2,880.00 USD | 100,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.95` | 756,930.00 USD | 100,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.05` | 271.52 USD | 99,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.15` | 37,490,000.00 USD | 99,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.25` | 13,650.00 USD | 61,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.35` | 19,360.00 USD | 61,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.45` | 26,940.00 USD | 61,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.55` | 22,870.00 USD | 61,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.65` | 7,610.00 USD | 61,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.75` | 47,000.00 USD | 61,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.85` | 3,240.00 USD | 61,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.95` | 57,510.00 USD | 61,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.05` | 39,100.00 USD | 61,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.15` | 7,190.00 USD | 61,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.25` | 26,470.00 USD | 61,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.35` | 3,550.00 USD | 61,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.45` | 16,310.00 USD | 61,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.55` | 10,070.00 USD | 61,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.65` | 10,560.00 USD | 61,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.75` | 31,040.00 USD | 61,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.85` | 21,860.00 USD | 61,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.95` | 16,400.00 USD | 61,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.05` | 3,030.00 USD | 61,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.15` | 20,420.00 USD | 61,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.25` | 73,520.00 USD | 61,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.35` | 2,130,000.00 USD | 61,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.45` | 1,220,000.00 USD | 59,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.65` | 12,780.00 USD | 58,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.75` | 34,270.00 USD | 58,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.85` | 20,920.00 USD | 57,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.95` | 6,970.00 USD | 57,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.05` | 49,470.00 USD | 57,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.15` | 62,230.00 USD | 57,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.25` | 55,120.00 USD | 57,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.35` | 9,520.00 USD | 57,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.45` | 18,840.00 USD | 57,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.55` | 310,740.00 USD | 57,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.65` | 520.90 USD | 57,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.75` | 28,190.00 USD | 57,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.85` | 9,160.00 USD | 57,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.95` | 22,890.00 USD | 57,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.05` | 12,050.00 USD | 57,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.15` | 165,720.00 USD | 57,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.25` | 41,840.00 USD | 57,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.35` | 6,370.00 USD | 57,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.45` | 7,370.00 USD | 57,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.55` | 17,050.00 USD | 57,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.65` | 13,250.00 USD | 57,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.75` | 46,640.00 USD | 57,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.85` | 1,600,000.00 USD | 57,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.95` | 9,630.00 USD | 55,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.05` | 47,590.00 USD | 55,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.15` | 4,110.00 USD | 55,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.25` | 36,380.00 USD | 55,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.35` | 3,410.00 USD | 55,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.45` | 259,640.00 USD | 55,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.55` | 10,950.00 USD | 55,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.65` | 100,210.00 USD | 55,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.75` | 73,540.00 USD | 55,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.85` | 21,270.00 USD | 54,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.95` | 40,150.00 USD | 54,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.05` | 25,710.00 USD | 54,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.15` | 9,960.00 USD | 54,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.25` | 44,690.00 USD | 54,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.35` | 111,410.00 USD | 54,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.45` | 104,270.00 USD | 54,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.55` | 10,330.00 USD | 54,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.75` | 37,430.00 USD | 54,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.85` | 22,530.00 USD | 54,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.95` | 20,450.00 USD | 54,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.05` | 286,760.00 USD | 54,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.15` | 4,180.00 USD | 54,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.25` | 38,370.00 USD | 54,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.35` | 15,520.00 USD | 54,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.45` | 2,010.00 USD | 54,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.55` | 28,710.00 USD | 54,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.65` | 129,590.00 USD | 54,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.75` | 55,240.00 USD | 53,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.85` | 37,490.00 USD | 53,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.95` | 38,420.00 USD | 53,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.05` | 1,850.00 USD | 53,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.15` | 35,140.00 USD | 53,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.25` | 1,880.00 USD | 53,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.35` | 33,110.00 USD | 53,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.55` | 56,440.00 USD | 53,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.65` | 3,220.00 USD | 53,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.75` | 36,970.00 USD | 53,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.85` | 15,790.00 USD | 53,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.95` | 28,120.00 USD | 53,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.05` | 24,640.00 USD | 53,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.15` | 3,640.00 USD | 53,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.25` | 32,220.00 USD | 53,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.35` | 3,700.00 USD | 53,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.45` | 26,660.00 USD | 53,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.55` | 59,620.00 USD | 53,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.65` | 205,370.00 USD | 53,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.75` | 364,430.00 USD | 53,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.85` | 19,060.00 USD | 52,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.95` | 702,830.00 USD | 52,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.05` | 17,080.00 USD | 52,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.15` | 4,080,000.00 USD | 52,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.25` | 314,050.00 USD | 48,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.35` | 64,400.00 USD | 47,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.45` | 40,930.00 USD | 47,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.55` | 242,250.00 USD | 47,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.65` | 80,590.00 USD | 47,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.75` | 166,510.00 USD | 47,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.85` | 9,620.00 USD | 47,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.95` | 2,260.00 USD | 47,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.05` | 1,380.00 USD | 47,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.15` | 643,210.00 USD | 47,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.25` | 114,920.00 USD | 46,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.35` | 8,140.00 USD | 46,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.45` | 15,750.00 USD | 46,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.55` | 674.58 USD | 46,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.65` | 149.74 USD | 46,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.75` | 485.68 USD | 46,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.85` | 12,020.00 USD | 46,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.95` | 7,240.00 USD | 46,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.15` | 23,880.00 USD | 46,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.25` | 1,680,000.00 USD | 46,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.35` | 182,170.00 USD | 44,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.45` | 160,090.00 USD | 44,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.55` | 22,390.00 USD | 44,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.65` | 25,780.00 USD | 44,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.75` | 3,200.00 USD | 44,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.85` | 19,980.00 USD | 44,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.95` | 7,010.00 USD | 44,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.05` | 2,230,000.00 USD | 44,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.15` | 3,260.00 USD | 42,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.25` | 26,530.00 USD | 42,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.35` | 58,860.00 USD | 41,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.45` | 70,130.00 USD | 41,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.55` | 27,800.00 USD | 41,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.65` | 35,020.00 USD | 41,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.75` | 65,150.00 USD | 41,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.85` | 40,780.00 USD | 41,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.95` | 31,640.00 USD | 41,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.05` | 124,470.00 USD | 41,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.15` | 870,580.00 USD | 41,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.25` | 20,720.00 USD | 40,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.35` | 26,580.00 USD | 40,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.45` | 211,320.00 USD | 40,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.55` | 38,980.00 USD | 40,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.65` | 121,240.00 USD | 40,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.75` | 30,430.00 USD | 40,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.85` | 31,470.00 USD | 40,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.95` | 17,060.00 USD | 40,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.05` | 37,350.00 USD | 40,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.15` | 25,420.00 USD | 40,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.25` | 40,780.00 USD | 40,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.35` | 155,780.00 USD | 40,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.45` | 22,860.00 USD | 39,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.55` | 34,370.00 USD | 39,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.65` | 71,540.00 USD | 39,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.75` | 72,310.00 USD | 39,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.85` | 209,940.00 USD | 39,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.95` | 20,640.00 USD | 39,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.05` | 181,910.00 USD | 39,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.15` | 114,710.00 USD | 39,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.25` | 33,770.00 USD | 39,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.35` | 53,940.00 USD | 39,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.45` | 91,090.00 USD | 39,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.55` | 7,160.00 USD | 39,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.65` | 60,500.00 USD | 38,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.75` | 60,970.00 USD | 38,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.85` | 2,300.00 USD | 38,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.95` | 2,170.00 USD | 38,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.05` | 77,070.00 USD | 38,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.15` | 15,110.00 USD | 38,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.25` | 560,340.00 USD | 38,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.35` | 35,030.00 USD | 38,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.45` | 29,040.00 USD | 38,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.55` | 8,860.00 USD | 38,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.65` | 17,880.00 USD | 38,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.75` | 4,140.00 USD | 38,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.85` | 41,690.00 USD | 38,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.95` | 39,990.00 USD | 38,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.05` | 163,490.00 USD | 38,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.15` | 119,700.00 USD | 37,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.25` | 42,970.00 USD | 37,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.35` | 24,000.00 USD | 37,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.45` | 31,090.00 USD | 37,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.55` | 202,180.00 USD | 37,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.65` | 118,650.00 USD | 37,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.75` | 55,780.00 USD | 37,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.85` | 25,290.00 USD | 37,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.95` | 81,620.00 USD | 37,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.05` | 244,410.00 USD | 37,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.15` | 273,840.00 USD | 36,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.25` | 16,540.00 USD | 36,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.35` | 29,950.00 USD | 36,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.45` | 187,780.00 USD | 36,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.55` | 185,620.00 USD | 36,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.65` | 465,580.00 USD | 36,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.75` | 5,050.00 USD | 35,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.85` | 28,150.00 USD | 35,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.95` | 15,710.00 USD | 35,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.05` | 3,310,000.00 USD | 35,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.15` | 24,030.00 USD | 32,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.25` | 64,120.00 USD | 32,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.35` | 34,940.00 USD | 32,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.45` | 104,460.00 USD | 32,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.55` | 3,070.00 USD | 32,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.65` | 162,310.00 USD | 32,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.75` | 177,330.00 USD | 32,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.80` | 116,720,000.00 USD | 116,720,000.00 USD | 146,090.00 USD | 1,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `88.80` | 271,450,000.00 USD | 271,450,000.00 USD | 17,650.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.85` | 25,310.00 USD | 31,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.95` | 79,760.00 USD | 31,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.00` | 116,570,000.00 USD | 116,570,000.00 USD | 3,720.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `89.00` | 271,430,000.00 USD | 271,430,000.00 USD | 241,970.00 USD | 175,650.00 USD | 7,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.05` | 10,550.00 USD | 31,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.15` | 10,140.00 USD | 31,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.20` | 116,570,000.00 USD | 116,570,000.00 USD | 5,350.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `89.20` | 271,010,000.00 USD | 271,010,000.00 USD | 8,180.00 USD | 10,750.00 USD | 1,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.25` | 18,790.00 USD | 31,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.35` | 214,440.00 USD | 31,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.40` | 116,560,000.00 USD | 116,560,000.00 USD | 12,630.00 USD | 48,770.00 USD | 137,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `89.40` | 270,990,000.00 USD | 270,990,000.00 USD | 33,150.00 USD | 11,770.00 USD | 136,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.45` | 169,960.00 USD | 31,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.55` | 1,310,000.00 USD | 31,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.60` | 116,360,000.00 USD | 116,360,000.00 USD | 557,950.00 USD | 163,120.00 USD | 315,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `89.60` | 270,800,000.00 USD | 270,800,000.00 USD | 684,220.00 USD | 270,260.00 USD | 723,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.65` | 5,080.00 USD | 30,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.75` | 81,270.00 USD | 29,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.80` | 115,330,000.00 USD | 115,330,000.00 USD | 532,910.00 USD | 381,520.00 USD | 197,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `89.80` | 269,130,000.00 USD | 269,130,000.00 USD | 425,950.00 USD | 283,370.00 USD | 291,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.85` | 39,690.00 USD | 29,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.95` | 27,000.00 USD | 29,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.00` | 114,210,000.00 USD | 114,210,000.00 USD | 412,230.00 USD | 479,230.00 USD | 454,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.00` | 268,120,000.00 USD | 268,120,000.00 USD | 374,600.00 USD | 545,850.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.05` | 8,210.00 USD | 29,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.15` | 23,430.00 USD | 29,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.20` | 112,870,000.00 USD | 112,870,000.00 USD | 489,160.00 USD | 406,910.00 USD | 432,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.20` | 266,110,000.00 USD | 266,110,000.00 USD | 1,250,000.00 USD | 573,800.00 USD | 724,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.25` | 10,570.00 USD | 29,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.35` | 35,550.00 USD | 29,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.40` | 111,540,000.00 USD | 111,540,000.00 USD | 505,770.00 USD | 339,750.00 USD | 509,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.40` | 263,560,000.00 USD | 263,560,000.00 USD | 796,240.00 USD | 30,920.00 USD | 694,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.45` | 37,560.00 USD | 29,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.55` | 8,220.00 USD | 29,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.60` | 110,190,000.00 USD | 110,190,000.00 USD | 270,180.00 USD | 392,650.00 USD | 477,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.60` | 262,030,000.00 USD | 262,030,000.00 USD | 978,100.00 USD | 994,460.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.65` | 87,230.00 USD | 29,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.75` | 52,590.00 USD | 29,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.80` | 109,040,000.00 USD | 109,040,000.00 USD | 106,320.00 USD | 101,660.00 USD | 1,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.80` | 258,920,000.00 USD | 258,920,000.00 USD | 1,210,000.00 USD | 685,900.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.85` | 45,990.00 USD | 29,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.95` | 10,090.00 USD | 29,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.00` | 108,840,000.00 USD | 108,840,000.00 USD | 57,100.00 USD | 882.42 USD | 129,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.00` | 255,940,000.00 USD | 255,940,000.00 USD | 1,190,000.00 USD | 575,820.00 USD | 295,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.05` | 492,790.00 USD | 29,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.15` | 280,380.00 USD | 29,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.20` | 108,650,000.00 USD | 108,650,000.00 USD | 27,610.00 USD | 769.97 USD | 307.73 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.20` | 253,880,000.00 USD | 253,880,000.00 USD | 946,940.00 USD | 807,150.00 USD | 576,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.25` | 39,810.00 USD | 28,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.35` | 82,210.00 USD | 28,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.40` | 108,620,000.00 USD | 108,620,000.00 USD | 3,800.00 USD | 125,680.00 USD | 43,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.40` | 251,550,000.00 USD | 251,550,000.00 USD | 1,180,000.00 USD | 1,000,000.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.45` | 365,890.00 USD | 28,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.55` | 1,410,000.00 USD | 28,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.60` | 108,450,000.00 USD | 108,450,000.00 USD | 25,530.00 USD | 96,080.00 USD | 1,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.60` | 248,230,000.00 USD | 248,230,000.00 USD | 500,280.00 USD | 295,810.00 USD | 827,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.65` | 17,090.00 USD | 26,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.75` | 309,530.00 USD | 26,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.80` | 108,320,000.00 USD | 108,320,000.00 USD | 229,430.00 USD | 103,030.00 USD | 11,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.80` | 246,600,000.00 USD | 246,600,000.00 USD | 932,400.00 USD | 581,530.00 USD | 688,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.85` | 77,180.00 USD | 26,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.95` | 112,500.00 USD | 26,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.00` | 107,980,000.00 USD | 107,980,000.00 USD | 137,240.00 USD | 74,290.00 USD | 90,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.00` | 244,400,000.00 USD | 244,400,000.00 USD | 681,440.00 USD | 586,560.00 USD | 471,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.05` | 17,200.00 USD | 26,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.15` | 1,090,000.00 USD | 26,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.20` | 107,680,000.00 USD | 107,680,000.00 USD | 153,400.00 USD | 41,040.00 USD | 107,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.20` | 242,660,000.00 USD | 242,660,000.00 USD | 210,560.00 USD | 354,230.00 USD | 294,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.25` | 149,610.00 USD | 25,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.35` | 46,550.00 USD | 25,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.40` | 107,370,000.00 USD | 107,370,000.00 USD | 141,800.00 USD | 72,380.00 USD | 782,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.40` | 241,800,000.00 USD | 241,800,000.00 USD | 415,170.00 USD | 289,690.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.45` | 156,810.00 USD | 25,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.55` | 114,460.00 USD | 24,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.60` | 106,380,000.00 USD | 106,380,000.00 USD | 31,270.00 USD | 66,860.00 USD | 45,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.60` | 239,890,000.00 USD | 239,890,000.00 USD | 175,470.00 USD | 267,710.00 USD | 636,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.65` | 191,670.00 USD | 24,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.75` | 425,980.00 USD | 24,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.80` | 106,230,000.00 USD | 106,230,000.00 USD | 55,570.00 USD | 0.00 USD | 97,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.80` | 238,810,000.00 USD | 238,810,000.00 USD | 92,010.00 USD | 62,840.00 USD | 69,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.85` | 367,830.00 USD | 24,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.95` | 22,550.00 USD | 23,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `93.00` | 238,580,000.00 USD | 238,580,000.00 USD | 0.00 USD | 109,950.00 USD | 281,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.05` | 81,780.00 USD | 23,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.15` | 75,520.00 USD | 23,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `93.20` | 238,190,000.00 USD | 238,190,000.00 USD | 54,470.00 USD | 4,160.00 USD | 49,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.25` | 296,810.00 USD | 23,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.35` | 132,180.00 USD | 23,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `93.40` | 238,080,000.00 USD | 238,080,000.00 USD | 11,220.00 USD | 2,430.00 USD | 1,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.45` | 21,870.00 USD | 23,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.55` | 341,510.00 USD | 23,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `93.60` | 238,070,000.00 USD | 238,070,000.00 USD | 238,200.00 USD | 299,520.00 USD | 114,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.65` | 47,710.00 USD | 22,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.75` | 91,550.00 USD | 22,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `93.80` | 237,420,000.00 USD | 237,420,000.00 USD | 281,530.00 USD | 179,760.00 USD | 91,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.85` | 120,450.00 USD | 22,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.95` | 1,950,000.00 USD | 22,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `94.00` | 236,860,000.00 USD | 236,860,000.00 USD | 78,790.00 USD | 153,680.00 USD | 64,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.05` | 186,970.00 USD | 20,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.15` | 78,960.00 USD | 20,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `94.20` | 236,570,000.00 USD | 236,570,000.00 USD | 172,550.00 USD | 229,720.00 USD | 258,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.25` | 1,090,000.00 USD | 20,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.35` | 33,820.00 USD | 19,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `94.40` | 235,910,000.00 USD | 235,910,000.00 USD | 109,990.00 USD | 0.00 USD | 184,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.45` | 926,780.00 USD | 19,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.55` | 262,610.00 USD | 18,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.60` | 106,080,000.00 USD | 106,080,000.00 USD | 30,840.00 USD | 4,870.00 USD | 964.12 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.60` | 235,610,000.00 USD | 235,610,000.00 USD | 79,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.65` | 202,690.00 USD | 18,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.75` | 47,830.00 USD | 17,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.80` | 106,040,000.00 USD | 106,040,000.00 USD | 343,700.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.80` | 235,530,000.00 USD | 235,530,000.00 USD | 351,370.00 USD | 15,050.00 USD | 8,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.85` | 83,350.00 USD | 17,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.95` | 82,180.00 USD | 17,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.00` | 105,700,000.00 USD | 105,700,000.00 USD | 117,050.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.00` | 235,160,000.00 USD | 235,160,000.00 USD | 418,320.00 USD | 532,260.00 USD | 13,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.05` | 207,190.00 USD | 17,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.15` | 16,510.00 USD | 17,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.20` | 105,580,000.00 USD | 105,580,000.00 USD | 26,240.00 USD | 2,330.00 USD | 6,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.20` | 234,190,000.00 USD | 234,190,000.00 USD | 47,840.00 USD | 200,720.00 USD | 138,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.25` | 309,400.00 USD | 17,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.35` | 35,320.00 USD | 17,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.40` | 105,550,000.00 USD | 105,550,000.00 USD | 333,560.00 USD | 304,630.00 USD | 344,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.40` | 233,810,000.00 USD | 233,810,000.00 USD | 866,300.00 USD | 239,410.00 USD | 1,380,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.45` | 166,630.00 USD | 17,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.55` | 202,790.00 USD | 16,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.60` | 104,570,000.00 USD | 104,570,000.00 USD | 1,190,000.00 USD | 706,940.00 USD | 1,270,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.60` | 231,320,000.00 USD | 231,320,000.00 USD | 1,740,000.00 USD | 1,320,000.00 USD | 986,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.65` | 166,370.00 USD | 16,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.75` | 89,790.00 USD | 16,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.80` | 101,390,000.00 USD | 101,390,000.00 USD | 1,840,000.00 USD | 1,400,000.00 USD | 797,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.80` | 227,280,000.00 USD | 227,280,000.00 USD | 1,910,000.00 USD | 1,030,000.00 USD | 1,330,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.85` | 35,590.00 USD | 16,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.95` | 633,290.00 USD | 16,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `96.00` | 97,350,000.00 USD | 97,350,000.00 USD | 1,760,000.00 USD | 1,380,000.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.00` | 223,000,000.00 USD | 223,000,000.00 USD | 1,870,000.00 USD | 2,140,000.00 USD | 3,170,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `96.05` | 73,770.00 USD | 15,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `96.15` | 614,360.00 USD | 15,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `96.20` | 92,850,000.00 USD | 92,850,000.00 USD | 1,970,000.00 USD | 1,310,000.00 USD | 1,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.20` | 215,830,000.00 USD | 215,830,000.00 USD | 3,950,000.00 USD | 2,080,000.00 USD | 2,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `96.25` | 162,540.00 USD | 15,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `96.35` | 12,030.00 USD | 14,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `96.40` | 88,330,000.00 USD | 88,330,000.00 USD | 1,540,000.00 USD | 1,270,000.00 USD | 1,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.40` | 207,220,000.00 USD | 207,220,000.00 USD | 3,260,000.00 USD | 643,110.00 USD | 2,910,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `96.45` | 101,960.00 USD | 14,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `96.55` | 106,550.00 USD | 14,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `96.60` | 83,930,000.00 USD | 83,930,000.00 USD | 1,770,000.00 USD | 848,780.00 USD | 934,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.60` | 200,400,000.00 USD | 200,400,000.00 USD | 3,250,000.00 USD | 2,480,000.00 USD | 2,380,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `96.65` | 49,990.00 USD | 14,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `96.75` | 341,460.00 USD | 14,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `96.80` | 80,370,000.00 USD | 80,370,000.00 USD | 346,250.00 USD | 738,000.00 USD | 729,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.80` | 192,300,000.00 USD | 192,300,000.00 USD | 3,710,000.00 USD | 2,770,000.00 USD | 2,960,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `96.85` | 23,740.00 USD | 14,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `96.95` | 23,640.00 USD | 14,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `97.00` | 78,560,000.00 USD | 78,560,000.00 USD | 544,560.00 USD | 114,330.00 USD | 170,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `97.00` | 182,870,000.00 USD | 182,870,000.00 USD | 5,510,000.00 USD | 2,530,000.00 USD | 2,040,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `97.05` | 452,710.00 USD | 14,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `97.15` | 252,820.00 USD | 13,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `97.20` | 77,730,000.00 USD | 77,730,000.00 USD | 362,430.00 USD | 11,540.00 USD | 336,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `97.20` | 172,780,000.00 USD | 172,780,000.00 USD | 5,490,000.00 USD | 4,350,000.00 USD | 3,980,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `97.25` | 33,050.00 USD | 13,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `97.35` | 153,020.00 USD | 13,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `97.40` | 77,020,000.00 USD | 77,020,000.00 USD | 845,630.00 USD | 872,410.00 USD | 824,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `97.40` | 158,970,000.00 USD | 158,970,000.00 USD | 5,010,000.00 USD | 2,440,000.00 USD | 4,890,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `97.45` | 420,520.00 USD | 13,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `97.55` | 115,160.00 USD | 115,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `97.60` | 74,470,000.00 USD | 74,470,000.00 USD | 3,860,000.00 USD | 1,700,000.00 USD | 2,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `97.60` | 146,630,000.00 USD | 146,630,000.00 USD | 5,190,000.00 USD | 5,230,000.00 USD | 4,930,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `97.65` | 517,090.00 USD | 12,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `97.75` | 334,790.00 USD | 12,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `97.80` | 66,360,000.00 USD | 66,360,000.00 USD | 4,070,000.00 USD | 3,260,000.00 USD | 1,820,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `97.80` | 131,280,000.00 USD | 131,280,000.00 USD | 7,010,000.00 USD | 2,970,000.00 USD | 4,790,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `97.85` | 128,480.00 USD | 12,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `97.95` | 333,740.00 USD | 11,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `98.00` | 57,220,000.00 USD | 57,220,000.00 USD | 4,600,000.00 USD | 3,190,000.00 USD | 3,090,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `98.00` | 116,520,000.00 USD | 116,520,000.00 USD | 8,930,000.00 USD | 8,500,000.00 USD | 8,720,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `98.05` | 9,630,000.00 USD | 11,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `98.15` | 204,770.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `98.20` | 46,340,000.00 USD | 46,340,000.00 USD | 4,520,000.00 USD | 2,920,000.00 USD | 2,700,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `98.20` | 90,370,000.00 USD | 90,370,000.00 USD | 9,810,000.00 USD | 6,890,000.00 USD | 6,860,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `98.25` | 543,670.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `98.35` | 103,360.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `98.40` | 36,190,000.00 USD | 36,190,000.00 USD | 1,860,000.00 USD | 3,980,000.00 USD | 5,720,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `98.40` | 66,810,000.00 USD | 66,810,000.00 USD | 5,610,000.00 USD | 2,950,000.00 USD | 13,520,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `98.45` | 252,890.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `98.55` | 58,520.00 USD | 861,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `98.60` | 24,630,000.00 USD | 24,630,000.00 USD | 0.00 USD | 4,570,000.00 USD | 8,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `98.60` | 44,720,000.00 USD | 44,720,000.00 USD | 0.00 USD | 10,810,000.00 USD | 10,950,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `98.65` | 472,720.00 USD | 803,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `98.75` | 31,490.00 USD | 330,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `98.80` | 12,040,000.00 USD | 12,040,000.00 USD | 0.00 USD | 7,160,000.00 USD | 4,880,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `98.80` | 22,960,000.00 USD | 22,960,000.00 USD | 0.00 USD | 9,880,000.00 USD | 13,080,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `98.85` | 65,440.00 USD | 299,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `98.95` | 12,570.00 USD | 233,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.00` | 11,630,000.00 USD | 11,630,000.00 USD | 20,350.00 USD | 5,630,000.00 USD | 5,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `99.00` | 23,260,000.00 USD | 23,260,000.00 USD | 20,350.00 USD | 5,630,000.00 USD | 5,980,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `99.00` | 28,270,000.00 USD | 28,270,000.00 USD | 0.00 USD | 11,470,000.00 USD | 16,810,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `99.05` | 31,910.00 USD | 221,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `99.15` | 13,880.00 USD | 189,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.20` | 37,510,000.00 USD | 37,510,000.00 USD | 7,990,000.00 USD | 2,620,000.00 USD | 3,650,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `99.20` | 35,630,000.00 USD | 35,630,000.00 USD | 0.00 USD | 7,360,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `99.25` | 1,400.00 USD | 175,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `99.35` | 90,510.00 USD | 173,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.40` | 40,330,000.00 USD | 40,330,000.00 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `99.40` | 36,230,000.00 USD | 36,230,000.00 USD | 0.00 USD | 599,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `99.45` | 1,030.00 USD | 83,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `99.55` | 34,660.00 USD | 82,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.60` | 44,990,000.00 USD | 44,990,000.00 USD | 1,340,000.00 USD | 3,320,000.00 USD | 6,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `99.60` | 38,140,000.00 USD | 38,140,000.00 USD | 0.00 USD | 1,900,000.00 USD | 6,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `99.65` | 14,550.00 USD | 47,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `99.75` | 11,930.00 USD | 33,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.80` | 50,980,000.00 USD | 50,980,000.00 USD | 1,070,000.00 USD | 1,760,000.00 USD | 3,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `99.80` | 39,870,000.00 USD | 39,870,000.00 USD | 1,230,000.00 USD | 490,550.00 USD | 2,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `99.85` | 21,270.00 USD | 21,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.00` | 52,130,000.00 USD | 52,130,000.00 USD | 468,220.00 USD | 24,320.00 USD | 657,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.00` | 39,950,000.00 USD | 39,950,000.00 USD | 48,160.00 USD | 36,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.05` | 3,580.00 USD | 118,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.20` | 52,140,000.00 USD | 52,140,000.00 USD | 0.00 USD | 0.00 USD | 11,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.25` | 211.53 USD | 118,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.40` | 53,950,000.00 USD | 53,950,000.00 USD | 0.00 USD | 453,740.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.40` | 43,720,000.00 USD | 43,720,000.00 USD | 865,170.00 USD | 68,710.00 USD | 2,830,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.55` | 23,220.00 USD | 142,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.60` | 60,040,000.00 USD | 60,040,000.00 USD | 1,850,000.00 USD | 177,410.00 USD | 4,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.60` | 45,490,000.00 USD | 45,490,000.00 USD | 46,010.00 USD | 245,560.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `100.80` | 61,970,000.00 USD | 61,970,000.00 USD | 802,270.00 USD | 1,120,000.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.80` | 47,170,000.00 USD | 47,170,000.00 USD | 702,740.00 USD | 981,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `101.00` | 71,560,000.00 USD | 71,560,000.00 USD | 7,260,000.00 USD | 1,820,000.00 USD | 519,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.00` | 58,390,000.00 USD | 58,390,000.00 USD | 1,920,000.00 USD | 5,560,000.00 USD | 3,730,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `101.20` | 88,250,000.00 USD | 88,250,000.00 USD | 5,910,000.00 USD | 6,710,000.00 USD | 4,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.20` | 73,110,000.00 USD | 73,110,000.00 USD | 6,220,000.00 USD | 3,670,000.00 USD | 4,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `101.40` | 96,220,000.00 USD | 96,220,000.00 USD | 3,390,000.00 USD | 1,950,000.00 USD | 2,630,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.40` | 88,910,000.00 USD | 88,910,000.00 USD | 4,720,000.00 USD | 28,510.00 USD | 11,050,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.45` | 953.63 USD | 143,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `101.55` | 468.15 USD | 143,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.60` | 117,210,000.00 USD | 117,210,000.00 USD | 5,190,000.00 USD | 2,550,000.00 USD | 13,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.60` | 98,760,000.00 USD | 98,760,000.00 USD | 3,650,000.00 USD | 0.00 USD | 6,200,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.65` | 416.76 USD | 144,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.80` | 124,210,000.00 USD | 124,210,000.00 USD | 483,810.00 USD | 304,910.00 USD | 6,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.80` | 108,180,000.00 USD | 108,180,000.00 USD | 3,050,000.00 USD | 453,970.00 USD | 5,920,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.85` | 211.85 USD | 144,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.00` | 128,600,000.00 USD | 128,600,000.00 USD | 2,230,000.00 USD | 873,740.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.00` | 112,330,000.00 USD | 112,330,000.00 USD | 1,810,000.00 USD | 503,680.00 USD | 1,840,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `102.20` | 135,430,000.00 USD | 135,430,000.00 USD | 3,030,000.00 USD | 1,390,000.00 USD | 2,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.20` | 119,040,000.00 USD | 119,040,000.00 USD | 2,390,000.00 USD | 803,220.00 USD | 3,520,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.25` | 505.11 USD | 144,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.40` | 139,960,000.00 USD | 139,960,000.00 USD | 1,390,000.00 USD | 574,230.00 USD | 2,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.40` | 123,750,000.00 USD | 123,750,000.00 USD | 1,760,000.00 USD | 299,640.00 USD | 2,650,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.45` | 16,890.00 USD | 161,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `102.55` | 3,300.00 USD | 164,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.60` | 140,780,000.00 USD | 140,780,000.00 USD | 623,960.00 USD | 190,630.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.60` | 126,210,000.00 USD | 126,210,000.00 USD | 1,450,000.00 USD | 979,270.00 USD | 37,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.65` | 4,300.00 USD | 169,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `102.75` | 69,020.00 USD | 238,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.80` | 144,630,000.00 USD | 144,630,000.00 USD | 1,420,000.00 USD | 1,870,000.00 USD | 563,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.80` | 134,400,000.00 USD | 134,400,000.00 USD | 7,900,000.00 USD | 0.00 USD | 277,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.85` | 86,600.00 USD | 324,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `102.95` | 2,870.00 USD | 327,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.00` | 149,120,000.00 USD | 149,120,000.00 USD | 2,720,000.00 USD | 1,430,000.00 USD | 340,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.00` | 148,920,000.00 USD | 148,920,000.00 USD | 11,690,000.00 USD | 0.00 USD | 2,830,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.05` | 22,850.00 USD | 350,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `103.15` | 1,750.00 USD | 352,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.20` | 154,470,000.00 USD | 154,470,000.00 USD | 1,850,000.00 USD | 1,670,000.00 USD | 1,820,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.20` | 162,530,000.00 USD | 162,530,000.00 USD | 12,970,000.00 USD | 4,380.00 USD | 631,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.25` | 1,470.00 USD | 353,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `103.35` | 691.41 USD | 354,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.40` | 162,160,000.00 USD | 162,160,000.00 USD | 3,930,000.00 USD | 1,900,000.00 USD | 1,860,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.40` | 178,490,000.00 USD | 178,490,000.00 USD | 12,450,000.00 USD | 233,330.00 USD | 3,280,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.55` | 8,800.00 USD | 363,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.60` | 177,160,000.00 USD | 177,160,000.00 USD | 4,540,000.00 USD | 2,110,000.00 USD | 8,360,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.60` | 196,880,000.00 USD | 196,880,000.00 USD | 11,460,000.00 USD | 1,720,000.00 USD | 5,210,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.75` | 3,990.00 USD | 367,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.80` | 186,850,000.00 USD | 186,850,000.00 USD | 3,480,000.00 USD | 2,770,000.00 USD | 3,430,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.80` | 209,260,000.00 USD | 209,260,000.00 USD | 7,960,000.00 USD | 1,880,000.00 USD | 2,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.85` | 28,920.00 USD | 396,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `103.95` | 10,060.00 USD | 406,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.00` | 196,420,000.00 USD | 196,420,000.00 USD | 3,550,000.00 USD | 2,800,000.00 USD | 3,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.00` | 238,420,000.00 USD | 238,420,000.00 USD | 11,880,000.00 USD | 7,160,000.00 USD | 10,110,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.05` | 1,590.00 USD | 407,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.15` | 2,330.00 USD | 410,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.20` | 203,960,000.00 USD | 203,960,000.00 USD | 3,270,000.00 USD | 2,180,000.00 USD | 2,090,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.20` | 260,230,000.00 USD | 260,230,000.00 USD | 8,520,000.00 USD | 7,010,000.00 USD | 6,280,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.25` | 325.26 USD | 410,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.35` | 2,010.00 USD | 412,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.40` | 211,450,000.00 USD | 211,450,000.00 USD | 3,300,000.00 USD | 1,930,000.00 USD | 2,260,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.40` | 277,200,000.00 USD | 277,200,000.00 USD | 5,100,000.00 USD | 3,700,000.00 USD | 8,170,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.45` | 12,140.00 USD | 424,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.55` | 4,250.00 USD | 428,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.60` | 217,410,000.00 USD | 217,410,000.00 USD | 1,830,000.00 USD | 1,220,000.00 USD | 2,920,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.60` | 294,760,000.00 USD | 294,760,000.00 USD | 7,180,000.00 USD | 3,550,000.00 USD | 6,830,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.65` | 631,520.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.75` | 59,710.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.80` | 223,190,000.00 USD | 223,190,000.00 USD | 1,610,000.00 USD | 1,100,000.00 USD | 3,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.80` | 311,900,000.00 USD | 311,900,000.00 USD | 5,170,000.00 USD | 4,150,000.00 USD | 7,820,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.85` | 16,470.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.95` | 1,030.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.00` | 225,130,000.00 USD | 225,130,000.00 USD | 708,730.00 USD | 483,120.00 USD | 746,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.00` | 329,020,000.00 USD | 329,020,000.00 USD | 5,730,000.00 USD | 5,070,000.00 USD | 6,330,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.05` | 16,290.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `105.15` | 4,320.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.20` | 226,450,000.00 USD | 226,450,000.00 USD | 514,940.00 USD | 4,110.00 USD | 809,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.20` | 341,730,000.00 USD | 341,730,000.00 USD | 5,340,000.00 USD | 4,850,000.00 USD | 2,530,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.25` | 7,300.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.40` | 226,650,000.00 USD | 226,650,000.00 USD | 72,850.00 USD | 2,770.00 USD | 123,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.40` | 353,690,000.00 USD | 353,690,000.00 USD | 2,960,000.00 USD | 4,450,000.00 USD | 4,540,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.45` | 8,610.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `105.55` | 4,180.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.60` | 227,230,000.00 USD | 227,230,000.00 USD | 178,510.00 USD | 263,160.00 USD | 135,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.60` | 371,160,000.00 USD | 371,160,000.00 USD | 5,650,000.00 USD | 6,010,000.00 USD | 5,810,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.75` | 1,460.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.80` | 227,670,000.00 USD | 227,670,000.00 USD | 132,310.00 USD | 285,640.00 USD | 19,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.80` | 381,920,000.00 USD | 381,920,000.00 USD | 3,540,000.00 USD | 3,020,000.00 USD | 4,200,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.95` | 2,020.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.00` | 228,720,000.00 USD | 228,720,000.00 USD | 377,210.00 USD | 456,530.00 USD | 222,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.00` | 391,900,000.00 USD | 391,900,000.00 USD | 4,000,000.00 USD | 2,430,000.00 USD | 3,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.05` | 4,790.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.20` | 230,130,000.00 USD | 230,130,000.00 USD | 606,390.00 USD | 420,460.00 USD | 375,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.20` | 406,050,000.00 USD | 406,050,000.00 USD | 6,780,000.00 USD | 3,540,000.00 USD | 3,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `106.40` | 231,230,000.00 USD | 231,230,000.00 USD | 583,540.00 USD | 313,010.00 USD | 207,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.40` | 413,600,000.00 USD | 413,600,000.00 USD | 3,250,000.00 USD | 2,670,000.00 USD | 1,630,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.45` | 10,970.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.60` | 233,760,000.00 USD | 233,760,000.00 USD | 887,290.00 USD | 440,970.00 USD | 1,200,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.60` | 422,800,000.00 USD | 422,800,000.00 USD | 2,470,000.00 USD | 2,360,000.00 USD | 4,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `106.80` | 235,750,000.00 USD | 235,750,000.00 USD | 643,510.00 USD | 182,880.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.80` | 428,690,000.00 USD | 428,690,000.00 USD | 1,340,000.00 USD | 1,750,000.00 USD | 2,800,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.85` | 771.46 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `106.95` | 543.31 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.00` | 236,420,000.00 USD | 236,420,000.00 USD | 199,140.00 USD | 184,400.00 USD | 288,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.00` | 434,250,000.00 USD | 434,250,000.00 USD | 1,370,000.00 USD | 1,260,000.00 USD | 2,930,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.05` | 12,960.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.15` | 35,700.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.20` | 236,800,000.00 USD | 236,800,000.00 USD | 138,920.00 USD | 0.00 USD | 242,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.20` | 435,970,000.00 USD | 435,970,000.00 USD | 866,170.00 USD | 389,810.00 USD | 461,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.25` | 2,690.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.35` | 212,780.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.40` | 236,860,000.00 USD | 236,860,000.00 USD | 0.00 USD | 0.00 USD | 61,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.40` | 436,950,000.00 USD | 436,950,000.00 USD | 0.00 USD | 280,650.00 USD | 703,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.45` | 55,230.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.55` | 3,570.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `107.60` | 437,320,000.00 USD | 437,320,000.00 USD | 213,520.00 USD | 0.00 USD | 154,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.65` | 1,770.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.75` | 5,840.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `107.80` | 438,100,000.00 USD | 438,100,000.00 USD | 489,650.00 USD | 10,400.00 USD | 277,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.85` | 1,480.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.00` | 438,130,000.00 USD | 438,130,000.00 USD | 25,580.00 USD | 6,070.00 USD | 5,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.05` | 1,080.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.15` | 863.04 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.20` | 440,250,000.00 USD | 440,250,000.00 USD | 860,420.00 USD | 826,850.00 USD | 427,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.25` | 546.66 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.35` | 4,430.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `108.40` | 236,880,000.00 USD | 236,880,000.00 USD | 12,330.00 USD | 1,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `108.40` | 442,330,000.00 USD | 442,330,000.00 USD | 1,140,000.00 USD | 528,370.00 USD | 411,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.45` | 121,890.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.55` | 117.23 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `108.60` | 237,010,000.00 USD | 237,010,000.00 USD | 133,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `108.60` | 443,600,000.00 USD | 443,600,000.00 USD | 419,250.00 USD | 515,740.00 USD | 332,360.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.65` | 64,720.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.75` | 9,470.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `108.80` | 237,020,000.00 USD | 237,020,000.00 USD | 3,720.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `108.80` | 446,400,000.00 USD | 446,400,000.00 USD | 750,710.00 USD | 1,190,000.00 USD | 855,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.85` | 333.08 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.95` | 2,620.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `109.00` | 237,020,000.00 USD | 237,020,000.00 USD | 5,350.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `109.00` | 446,940,000.00 USD | 446,940,000.00 USD | 248,800.00 USD | 112,280.00 USD | 176,770.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.15` | 44,720.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `109.20` | 237,220,000.00 USD | 237,220,000.00 USD | 12,630.00 USD | 48,770.00 USD | 137,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `109.20` | 448,180,000.00 USD | 448,180,000.00 USD | 613,010.00 USD | 87,870.00 USD | 544,580.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.25` | 1,170.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.35` | 7,560.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `109.40` | 237,350,000.00 USD | 237,350,000.00 USD | 123,410.00 USD | 7,590.00 USD | 2,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `109.40` | 448,800,000.00 USD | 448,800,000.00 USD | 158,460.00 USD | 81,870.00 USD | 375,580.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.45` | 103,840.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.55` | 106.26 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `109.60` | 238,260,000.00 USD | 238,260,000.00 USD | 434,540.00 USD | 155,520.00 USD | 313,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `109.60` | 449,860,000.00 USD | 449,860,000.00 USD | 525,760.00 USD | 188,400.00 USD | 347,790.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.65` | 53,730.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.75` | 231.57 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `109.80` | 239,370,000.00 USD | 239,370,000.00 USD | 532,910.00 USD | 381,520.00 USD | 197,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `109.80` | 450,860,000.00 USD | 450,860,000.00 USD | 425,950.00 USD | 283,370.00 USD | 291,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.85` | 848.04 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.95` | 1,590.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `110.00` | 240,710,000.00 USD | 240,710,000.00 USD | 412,230.00 USD | 479,230.00 USD | 454,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `110.00` | 452,880,000.00 USD | 452,880,000.00 USD | 374,600.00 USD | 545,850.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `110.05` | 2,910.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.15` | 194.97 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `110.20` | 242,040,000.00 USD | 242,040,000.00 USD | 489,160.00 USD | 406,910.00 USD | 432,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `110.20` | 455,430,000.00 USD | 455,430,000.00 USD | 1,250,000.00 USD | 573,800.00 USD | 724,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `110.25` | 324.13 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.35` | 148,440.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `110.40` | 243,400,000.00 USD | 243,400,000.00 USD | 505,770.00 USD | 339,750.00 USD | 509,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `110.40` | 456,950,000.00 USD | 456,950,000.00 USD | 796,240.00 USD | 30,920.00 USD | 694,770.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `110.45` | 16,940.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.55` | 203.41 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `110.60` | 243,850,000.00 USD | 243,850,000.00 USD | 110,850.00 USD | 104,840.00 USD | 240,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `110.60` | 458,050,000.00 USD | 458,050,000.00 USD | 506,360.00 USD | 293,650.00 USD | 301,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `110.65` | 219.09 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.75` | 7,600.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `110.80` | 244,540,000.00 USD | 244,540,000.00 USD | 159,320.00 USD | 287,810.00 USD | 237,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `110.80` | 460,070,000.00 USD | 460,070,000.00 USD | 471,740.00 USD | 700,800.00 USD | 841,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `110.85` | 103.09 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.95` | 15,300.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `111.00` | 244,750,000.00 USD | 244,750,000.00 USD | 106,320.00 USD | 101,660.00 USD | 1,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `111.00` | 463,050,000.00 USD | 463,050,000.00 USD | 1,210,000.00 USD | 685,900.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `111.05` | 6,860.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.15` | 1,710.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `111.20` | 244,940,000.00 USD | 244,940,000.00 USD | 57,100.00 USD | 882.42 USD | 129,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `111.20` | 465,110,000.00 USD | 465,110,000.00 USD | 1,190,000.00 USD | 575,820.00 USD | 295,620.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `111.35` | 2,350,000.00 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `111.40` | 244,960,000.00 USD | 244,960,000.00 USD | 27,610.00 USD | 769.97 USD | 307.73 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `111.40` | 467,440,000.00 USD | 467,440,000.00 USD | 946,940.00 USD | 807,150.00 USD | 576,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `111.45` | 841.45 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.55` | 311.22 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `111.60` | 245,080,000.00 USD | 245,080,000.00 USD | 0.00 USD | 77,530.00 USD | 42,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `111.60` | 468,400,000.00 USD | 468,400,000.00 USD | 662,880.00 USD | 172,700.00 USD | 122,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `111.75` | 114,530.00 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `111.80` | 470,760,000.00 USD | 470,760,000.00 USD | 515,920.00 USD | 829,010.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `111.85` | 17,210.00 USD | 4,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.95` | 1,460.00 USD | 4,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `112.00` | 472,390,000.00 USD | 472,390,000.00 USD | 500,280.00 USD | 295,810.00 USD | 827,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `112.05` | 216.26 USD | 4,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `112.20` | 474,590,000.00 USD | 474,590,000.00 USD | 932,400.00 USD | 581,530.00 USD | 688,730.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `112.25` | 1,370.00 USD | 4,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `112.40` | 476,330,000.00 USD | 476,330,000.00 USD | 681,440.00 USD | 586,560.00 USD | 471,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `112.55` | 844.13 USD | 4,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `112.60` | 477,190,000.00 USD | 477,190,000.00 USD | 210,560.00 USD | 354,230.00 USD | 294,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `112.75` | 110.50 USD | 4,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `112.80` | 478,060,000.00 USD | 478,060,000.00 USD | 207,390.00 USD | 162,590.00 USD | 505,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `113.00` | 479,100,000.00 USD | 479,100,000.00 USD | 207,780.00 USD | 127,100.00 USD | 702,160.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `113.05` | 103,600.00 USD | 4,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.15` | 10,200.00 USD | 4,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `113.20` | 480,180,000.00 USD | 480,180,000.00 USD | 175,470.00 USD | 267,710.00 USD | 636,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `113.25` | 114.38 USD | 4,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `113.40` | 480,400,000.00 USD | 480,400,000.00 USD | 92,010.00 USD | 62,840.00 USD | 69,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `113.55` | 10,470.00 USD | 4,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `113.60` | 480,790,000.00 USD | 480,790,000.00 USD | 0.00 USD | 109,950.00 USD | 281,490.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `113.65` | 3,220.00 USD | 4,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.75` | 2,130.00 USD | 4,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `113.80` | 480,800,000.00 USD | 480,800,000.00 USD | 2,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `113.85` | 14,390.00 USD | 4,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.95` | 21,840.00 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `114.00` | 480,890,000.00 USD | 480,890,000.00 USD | 48,760.00 USD | 0.00 USD | 49,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `114.05` | 23,300.00 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.15` | 1,960.00 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.25` | 2,150.00 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.45` | 9,310.00 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.85` | 51,610.00 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.95` | 15,310.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.05` | 569,550.00 USD | 5,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.15` | 877,850.00 USD | 6,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.25` | 18,240.00 USD | 6,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.35` | 408,270.00 USD | 6,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.55` | 46,710.00 USD | 6,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.75` | 160.89 USD | 6,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.85` | 289.62 USD | 6,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.05` | 4,450.00 USD | 6,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.15` | 22,160.00 USD | 6,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.25` | 5,870.00 USD | 6,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.35` | 90,140.00 USD | 6,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.55` | 2,040.00 USD | 6,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.65` | 555.25 USD | 6,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.75` | 31,980.00 USD | 6,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.85` | 261,600.00 USD | 7,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.05` | 4,520,000.00 USD | 11,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.15` | 51,230.00 USD | 11,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.25` | 157.12 USD | 11,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.45` | 128.02 USD | 11,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.75` | 2,720.00 USD | 11,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.85` | 584.54 USD | 11,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.95` | 12,060.00 USD | 11,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.45` | 32,620.00 USD | 11,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.55` | 1,110.00 USD | 11,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.75` | 309.94 USD | 11,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.95` | 1,780.00 USD | 11,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.15` | 3,520.00 USD | 11,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.25` | 58,110.00 USD | 11,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.45` | 115.87 USD | 11,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.55` | 1,070.00 USD | 11,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.65` | 90,800.00 USD | 12,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.75` | 374.82 USD | 12,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.95` | 178,050.00 USD | 12,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.15` | 4,930.00 USD | 12,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.35` | 145.62 USD | 12,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.55` | 2,520.00 USD | 12,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.95` | 28,790.00 USD | 12,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.25` | 414.68 USD | 12,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.45` | 45,000.00 USD | 12,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.55` | 5,940.00 USD | 12,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.65` | 16,300.00 USD | 12,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.75` | 19,900.00 USD | 12,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.05` | 56,710.00 USD | 12,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.15` | 169.79 USD | 12,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.25` | 2,200.00 USD | 12,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.45` | 20,160.00 USD | 12,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.65` | 116.52 USD | 12,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.95` | 2,790.00 USD | 12,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.25` | 483.14 USD | 12,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.35` | 2,330.00 USD | 12,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.45` | 2,520.00 USD | 12,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.55` | 3,430.00 USD | 12,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.05` | 586.76 USD | 12,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.15` | 11,520.00 USD | 12,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.25` | 17,600.00 USD | 12,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.45` | 3,080.00 USD | 12,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.55` | 649,140.00 USD | 13,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.65` | 675.60 USD | 13,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.75` | 7,200.00 USD | 13,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.95` | 14,160.00 USD | 13,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.35` | 6,470.00 USD | 13,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.65` | 487.52 USD | 13,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.75` | 1,930.00 USD | 13,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.85` | 6,200.00 USD | 13,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.95` | 110.84 USD | 13,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.05` | 810.50 USD | 13,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.15` | 12,930,000.00 USD | 26,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.35` | 305.77 USD | 26,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.45` | 11,380.00 USD | 26,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.65` | 31,220.00 USD | 26,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.85` | 1,710.00 USD | 26,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.95` | 9,460.00 USD | 26,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.05` | 2,030.00 USD | 26,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.25` | 2,480.00 USD | 26,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.35` | 16,190.00 USD | 26,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.65` | 694,870.00 USD | 26,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.85` | 44,240.00 USD | 26,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.95` | 10,510.00 USD | 26,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.05` | 116,200.00 USD | 27,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.35` | 195.09 USD | 27,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.45` | 863,880.00 USD | 27,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.65` | 4,600,000.00 USD | 32,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.75` | 18,730.00 USD | 32,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.85` | 43,250.00 USD | 32,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.25` | 32,480.00 USD | 32,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.35` | 888.63 USD | 32,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.45` | 2,990.00 USD | 32,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.55` | 65,100.00 USD | 32,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.75` | 38,040.00 USD | 32,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.85` | 4,930,000.00 USD | 37,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.25` | 46,990.00 USD | 37,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.35` | 1,040.00 USD | 37,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.55` | 4,970.00 USD | 37,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.65` | 1,080,000.00 USD | 38,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.85` | 504,660.00 USD | 39,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.95` | 2,070.00 USD | 39,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.05` | 188.71 USD | 39,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.25` | 1,560.00 USD | 39,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.45` | 715.09 USD | 39,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.55` | 171.02 USD | 39,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.85` | 5,820.00 USD | 39,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.15` | 325.09 USD | 39,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.25` | 47,650.00 USD | 39,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.35` | 5,320.00 USD | 39,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.45` | 8,530.00 USD | 39,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.55` | 196.17 USD | 39,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.65` | 240.10 USD | 39,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.85` | 49,280.00 USD | 39,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.05` | 5,730.00 USD | 39,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.15` | 9,170.00 USD | 39,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.55` | 186.97 USD | 39,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.65` | 8,400.00 USD | 39,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.75` | 151,500.00 USD | 39,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.95` | 503.65 USD | 39,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.05` | 142.09 USD | 39,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.25` | 92,140.00 USD | 39,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.85` | 18,510.00 USD | 39,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.15` | 532,900.00 USD | 40,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.25` | 1,560.00 USD | 40,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.35` | 246.34 USD | 40,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.45` | 746.33 USD | 40,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.85` | 3,250.00 USD | 40,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.95` | 504.37 USD | 40,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.15` | 48,850.00 USD | 40,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.45` | 608.57 USD | 40,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.55` | 136.55 USD | 40,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.65` | 7,940.00 USD | 40,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.85` | 133,160.00 USD | 40,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.05` | 1,640.00 USD | 40,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.55` | 1,650.00 USD | 40,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.75` | 212.13 USD | 40,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.05` | 1,270.00 USD | 40,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.15` | 115,290.00 USD | 40,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.35` | 18,980.00 USD | 40,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.45` | 132,700.00 USD | 40,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.75` | 2,080,000.00 USD | 42,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.95` | 459.92 USD | 42,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.15` | 552.43 USD | 42,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.25` | 66,520.00 USD | 42,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.65` | 22,260.00 USD | 42,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.85` | 1,060,000.00 USD | 43,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.05` | 116.24 USD | 43,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.45` | 4,870.00 USD | 43,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.55` | 7,330.00 USD | 43,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.75` | 210,790.00 USD | 44,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.95` | 1,940.00 USD | 44,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.05` | 125.53 USD | 44,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.15` | 927.36 USD | 44,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.35` | 210.61 USD | 44,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.45` | 247,540.00 USD | 44,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.55` | 236.39 USD | 44,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.65` | 2,140.00 USD | 44,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.75` | 239.56 USD | 44,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.15` | 80,180.00 USD | 44,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.45` | 151.00 USD | 44,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.75` | 847.93 USD | 44,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.25` | 15,400.00 USD | 44,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.35` | 22,260.00 USD | 44,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.55` | 143,550.00 USD | 44,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.75` | 1,340.00 USD | 44,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.85` | 29,340.00 USD | 44,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.05` | 3,750.00 USD | 44,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.25` | 7,270.00 USD | 44,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.35` | 114.04 USD | 44,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.45` | 78,000.00 USD | 44,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.65` | 2,330.00 USD | 44,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.95` | 2,090.00 USD | 44,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.15` | 1,760.00 USD | 44,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.35` | 5,340.00 USD | 44,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.65` | 857,010.00 USD | 45,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.85` | 5,850.00 USD | 45,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.95` | 820.24 USD | 45,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.15` | 88,760.00 USD | 45,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.25` | 2,770.00 USD | 45,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.35` | 7,330.00 USD | 45,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.55` | 2,690.00 USD | 45,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.65` | 587,730.00 USD | 46,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.75` | 1,880.00 USD | 46,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.95` | 3,070.00 USD | 46,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.05` | 166.17 USD | 46,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.15` | 1,730.00 USD | 46,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.35` | 5,770.00 USD | 46,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.45` | 204.96 USD | 46,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.55` | 94,970.00 USD | 46,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.65` | 558.12 USD | 46,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.85` | 300.14 USD | 46,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.15` | 1,380,000.00 USD | 47,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.35` | 445,050.00 USD | 48,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.45` | 163.29 USD | 48,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.55` | 344,780.00 USD | 48,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.65` | 709.06 USD | 48,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.75` | 91,450.00 USD | 48,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.95` | 1,460.00 USD | 48,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.15` | 343.04 USD | 48,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.45` | 1,490.00 USD | 48,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.55` | 116.65 USD | 48,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.65` | 16,900.00 USD | 48,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.75` | 724.79 USD | 48,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.85` | 37,240.00 USD | 48,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.95` | 178.44 USD | 48,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.05` | 2,930.00 USD | 48,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.25` | 29,740.00 USD | 48,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.65` | 2,910.00 USD | 48,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.15` | 2,770.00 USD | 48,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.25` | 86,240.00 USD | 48,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.45` | 8,830.00 USD | 48,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.65` | 409.46 USD | 48,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.75` | 2,280.00 USD | 48,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.85` | 6,670.00 USD | 48,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.95` | 1,920.00 USD | 48,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.15` | 200.84 USD | 48,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.25` | 304,500.00 USD | 49,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.35` | 384,300.00 USD | 49,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.45` | 3,150.00 USD | 49,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.55` | 585,740.00 USD | 50,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.75` | 1,570.00 USD | 50,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.05` | 230,640.00 USD | 50,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.35` | 2,300.00 USD | 50,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.65` | 51,450.00 USD | 50,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.75` | 1,270.00 USD | 50,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.85` | 43,120.00 USD | 50,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.05` | 5,930.00 USD | 50,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.25` | 2,340.00 USD | 50,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.45` | 4,240.00 USD | 50,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.55` | 363.19 USD | 50,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.15` | 4,820,000.00 USD | 55,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.55` | 8,050.00 USD | 55,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.25` | 39,850.00 USD | 55,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.35` | 3,320.00 USD | 55,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.45` | 1,370,000.00 USD | 56,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.95` | 1,140,000.00 USD | 57,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.15` | 66,400.00 USD | 57,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.25` | 190.27 USD | 57,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.45` | 1,880.00 USD | 57,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.55` | 30,560.00 USD | 57,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.65` | 2,390.00 USD | 57,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.75` | 93,830.00 USD | 58,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.95` | 315,900.00 USD | 58,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.15` | 120.19 USD | 58,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.35` | 88,130.00 USD | 58,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.75` | 13,730.00 USD | 58,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.85` | 794.25 USD | 58,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.95` | 26,450.00 USD | 58,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.05` | 44,690.00 USD | 58,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.15` | 249,820.00 USD | 58,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.25` | 27,920.00 USD | 58,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.65` | 2,080.00 USD | 58,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.95` | 6,100.00 USD | 58,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.15` | 683,000.00 USD | 59,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.25` | 32,970.00 USD | 59,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.35` | 118,850.00 USD | 59,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.85` | 318.48 USD | 59,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.05` | 2,240.00 USD | 59,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.35` | 2,160.00 USD | 59,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.55` | 41,510.00 USD | 59,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.65` | 119.62 USD | 59,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.85` | 142,330.00 USD | 59,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.95` | 145,330.00 USD | 60,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `162.05` | 304.65 USD | 60,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `162.45` | 2,270.00 USD | 60,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `162.55` | 650.20 USD | 60,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.45` | 8,110.00 USD | 60,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.65` | 21,930.00 USD | 60,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.75` | 1,310.00 USD | 60,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.85` | 5,140.00 USD | 60,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `164.75` | 207,840.00 USD | 60,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `164.85` | 1,680.00 USD | 60,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `165.15` | 198.18 USD | 60,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `165.45` | 144,260.00 USD | 60,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `165.85` | 36,560,000.00 USD | 96,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.25` | 190,590.00 USD | 97,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.35` | 1,230.00 USD | 97,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.25` | 319.45 USD | 97,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.35` | 19,220.00 USD | 97,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.45` | 5,950,000.00 USD | 103,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.65` | 115.68 USD | 103,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.75` | 1,890.00 USD | 103,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.85` | 3,460.00 USD | 103,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.95` | 2,780.00 USD | 103,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.35` | 19,740.00 USD | 103,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.45` | 1,110,000.00 USD | 104,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.65` | 325,850.00 USD | 104,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `169.95` | 101,970.00 USD | 104,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.45` | 111.44 USD | 104,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.75` | 3,320.00 USD | 104,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.95` | 398.92 USD | 104,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `172.45` | 51,970.00 USD | 104,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `172.85` | 10,200.00 USD | 104,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.45` | 16,540.00 USD | 104,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.85` | 695.40 USD | 104,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.05` | 104,430.00 USD | 104,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.25` | 245,010.00 USD | 105,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.35` | 205,490.00 USD | 105,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.55` | 1,650.00 USD | 105,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.75` | 146.79 USD | 105,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.05` | 175.05 USD | 105,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.15` | 1,320.00 USD | 105,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.35` | 119.24 USD | 105,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.55` | 158.00 USD | 105,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.75` | 263.62 USD | 105,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.05` | 24,820.00 USD | 105,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.25` | 625.69 USD | 105,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.45` | 520.53 USD | 105,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.55` | 3,530.00 USD | 105,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.65` | 2,070.00 USD | 105,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.95` | 80,850.00 USD | 105,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `178.25` | 1,610.00 USD | 105,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `178.35` | 3,130.00 USD | 105,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `178.85` | 132.35 USD | 105,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.05` | 2,970,000.00 USD | 108,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.15` | 2,110.00 USD | 108,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.35` | 473.48 USD | 108,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.95` | 15,590.00 USD | 108,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.05` | 2,360.00 USD | 108,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.35` | 7,470.00 USD | 108,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.55` | 3,970.00 USD | 108,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.95` | 334.76 USD | 108,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.55` | 254.17 USD | 108,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.65` | 5,150.00 USD | 108,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `182.05` | 964.87 USD | 108,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `182.15` | 3,990.00 USD | 108,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `182.25` | 291,600.00 USD | 108,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `182.55` | 5,110.00 USD | 108,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `182.85` | 618.03 USD | 108,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `183.15` | 1,310.00 USD | 108,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `183.35` | 5,500.00 USD | 108,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.55` | 369,100.00 USD | 109,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.95` | 165,440.00 USD | 109,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.15` | 3,690.00 USD | 109,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.25` | 737.29 USD | 109,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.45` | 2,770.00 USD | 109,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.65` | 137.38 USD | 109,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.75` | 19,050.00 USD | 109,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `186.35` | 181,490.00 USD | 109,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `186.45` | 231.20 USD | 109,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `186.75` | 115.78 USD | 109,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.45` | 2,110.00 USD | 109,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.95` | 39,010.00 USD | 109,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.25` | 19,000.00 USD | 109,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.35` | 19,090.00 USD | 109,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.55` | 231.92 USD | 109,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.95` | 1,450.00 USD | 109,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.05` | 137,350.00 USD | 109,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.25` | 64,800.00 USD | 109,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.95` | 284,930.00 USD | 110,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.05` | 788,710.00 USD | 110,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.15` | 286,480.00 USD | 111,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.65` | 57,200.00 USD | 111,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.85` | 534.38 USD | 111,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.95` | 13,570,000.00 USD | 124,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.95` | 322.48 USD | 124,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `192.25` | 336.44 USD | 124,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `192.75` | 88,240.00 USD | 124,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `193.05` | 7,410.00 USD | 124,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `193.15` | 1,190.00 USD | 124,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `193.45` | 12,910.00 USD | 124,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `193.55` | 114,580.00 USD | 125,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `193.65` | 4,750.00 USD | 125,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `193.85` | 15,590.00 USD | 125,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `194.25` | 3,710.00 USD | 125,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `194.55` | 8,670.00 USD | 125,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `194.65` | 136,260.00 USD | 125,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `194.75` | 266.81 USD | 125,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `195.05` | 9,500.00 USD | 125,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `195.25` | 13,690.00 USD | 125,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `195.35` | 48,840.00 USD | 125,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `195.75` | 9,790.00 USD | 125,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `196.05` | 4,080.00 USD | 125,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `196.15` | 415.84 USD | 125,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `196.25` | 3,470.00 USD | 125,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `196.45` | 4,350.00 USD | 125,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `196.75` | 127.89 USD | 125,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `196.95` | 2,000.00 USD | 125,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `197.15` | 193.21 USD | 125,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `197.35` | 6,310.00 USD | 125,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `197.65` | 292,380.00 USD | 125,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `198.05` | 1,580.00 USD | 125,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `198.15` | 223,280.00 USD | 125,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `198.25` | 12,030.00 USD | 125,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `198.35` | 396.70 USD | 125,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `198.45` | 16,790.00 USD | 125,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `198.55` | 1,950.00 USD | 125,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `198.85` | 78,030.00 USD | 125,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `199.05` | 1,520.00 USD | 125,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `199.15` | 2,550.00 USD | 125,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `199.35` | 139.55 USD | 125,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `199.55` | 8,130.00 USD | 125,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `199.65` | 8,020.00 USD | 125,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `199.75` | 27,860.00 USD | 125,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `19.85` | 142,200,000.00 USD | 0.00 USD | 214,610.00 USD | `-80.13%` | `10,811.76` |
| `Live` | `Long` | `19.95` | 141,980,000.00 USD | 0.00 USD | 847.08 USD | `-80.03%` | `42.46` |
| `Live` | `Long` | `20.05` | 141,980,000.00 USD | 0.00 USD | 7,950.00 USD | `-79.93%` | `396.72` |
| `Live` | `Long` | `20.25` | 141,970,000.00 USD | 0.00 USD | 1,350.00 USD | `-79.73%` | `66.78` |
| `Live` | `Long` | `20.35` | 141,970,000.00 USD | 0.00 USD | 7,510.00 USD | `-79.63%` | `369.00` |
| `Live` | `Long` | `20.55` | 141,960,000.00 USD | 0.00 USD | 58,780.00 USD | `-79.43%` | `2,860.17` |
| `Live` | `Long` | `20.65` | 141,910,000.00 USD | 0.00 USD | 1,260.00 USD | `-79.33%` | `61.19` |
| `Live` | `Long` | `20.85` | 141,900,000.00 USD | 0.00 USD | 353,680.00 USD | `-79.13%` | `16,963.19` |
| `Live` | `Long` | `20.95` | 141,550,000.00 USD | 0.00 USD | 120,470.00 USD | `-79.03%` | `5,750.44` |
| `Live` | `Long` | `21.05` | 141,430,000.00 USD | 0.00 USD | 1,050.00 USD | `-78.93%` | `50.00` |
| `Live` | `Long` | `21.25` | 141,430,000.00 USD | 0.00 USD | 1,060.00 USD | `-78.73%` | `50.00` |
| `Live` | `Long` | `21.35` | 141,430,000.00 USD | 0.00 USD | 1,410.00 USD | `-78.62%` | `65.89` |
| `Live` | `Long` | `21.45` | 141,430,000.00 USD | 0.00 USD | 289.36 USD | `-78.52%` | `13.49` |
| `Live` | `Long` | `21.55` | 141,430,000.00 USD | 0.00 USD | 993.24 USD | `-78.42%` | `46.09` |
| `Live` | `Long` | `21.75` | 141,430,000.00 USD | 0.00 USD | 5,360.00 USD | `-78.22%` | `246.38` |
| `Live` | `Long` | `21.95` | 141,420,000.00 USD | 0.00 USD | 194.48 USD | `-78.02%` | `8.86` |
| `Live` | `Long` | `22.05` | 141,420,000.00 USD | 0.00 USD | 3,040.00 USD | `-77.92%` | `138.08` |
| `Live` | `Long` | `22.35` | 141,420,000.00 USD | 0.00 USD | 335.25 USD | `-77.62%` | `15.00` |
| `Live` | `Long` | `22.55` | 141,420,000.00 USD | 0.00 USD | 159.43 USD | `-77.42%` | `7.07` |
| `Live` | `Long` | `22.75` | 141,420,000.00 USD | 0.00 USD | 386.30 USD | `-77.22%` | `16.98` |
| `Live` | `Long` | `22.95` | 141,420,000.00 USD | 0.00 USD | 601,510.00 USD | `-77.02%` | `26,209.70` |
| `Live` | `Long` | `23.45` | 140,810,000.00 USD | 0.00 USD | 1,380.00 USD | `-76.52%` | `58.86` |
| `Live` | `Long` | `23.75` | 140,810,000.00 USD | 0.00 USD | 47,330.00 USD | `-76.22%` | `1,992.69` |
| `Live` | `Long` | `23.85` | 140,770,000.00 USD | 0.00 USD | 1,910.00 USD | `-76.12%` | `80.00` |
| `Live` | `Long` | `24.05` | 140,760,000.00 USD | 0.00 USD | 721.50 USD | `-75.92%` | `30.00` |
| `Live` | `Long` | `24.15` | 140,760,000.00 USD | 0.00 USD | 939.68 USD | `-75.82%` | `38.91` |
| `Live` | `Long` | `24.25` | 140,760,000.00 USD | 0.00 USD | 147.92 USD | `-75.72%` | `6.10` |
| `Live` | `Long` | `24.35` | 140,760,000.00 USD | 0.00 USD | 1,470.00 USD | `-75.62%` | `60.30` |
| `Live` | `Long` | `24.55` | 140,760,000.00 USD | 0.00 USD | 245.50 USD | `-75.42%` | `10.00` |
| `Live` | `Long` | `24.95` | 140,760,000.00 USD | 0.00 USD | 1,380.00 USD | `-75.02%` | `55.47` |
| `Live` | `Long` | `25.05` | 140,760,000.00 USD | 0.00 USD | 1,440.00 USD | `-74.92%` | `57.39` |
| `Live` | `Long` | `25.15` | 140,760,000.00 USD | 0.00 USD | 2,010.00 USD | `-74.82%` | `80.00` |
| `Live` | `Long` | `25.45` | 140,760,000.00 USD | 0.00 USD | 106.64 USD | `-74.52%` | `4.19` |
| `Live` | `Long` | `25.55` | 140,760,000.00 USD | 0.00 USD | 10,650.00 USD | `-74.42%` | `416.67` |
| `Live` | `Long` | `25.75` | 140,740,000.00 USD | 0.00 USD | 464.27 USD | `-74.22%` | `18.03` |
| `Live` | `Long` | `25.95` | 140,740,000.00 USD | 0.00 USD | 54,830.00 USD | `-74.02%` | `2,113.00` |
| `Live` | `Long` | `26.15` | 140,690,000.00 USD | 0.00 USD | 8,910.00 USD | `-73.82%` | `340.88` |
| `Live` | `Long` | `26.25` | 140,680,000.00 USD | 0.00 USD | 2,770.00 USD | `-73.72%` | `105.65` |
| `Live` | `Long` | `26.55` | 140,680,000.00 USD | 0.00 USD | 308.51 USD | `-73.42%` | `11.62` |
| `Live` | `Long` | `26.65` | 140,680,000.00 USD | 0.00 USD | 309.67 USD | `-73.32%` | `11.62` |
| `Live` | `Long` | `27.35` | 140,680,000.00 USD | 0.00 USD | 164,540.00 USD | `-72.62%` | `6,016.09` |
| `Live` | `Long` | `27.45` | 140,510,000.00 USD | 0.00 USD | 272.30 USD | `-72.52%` | `9.92` |
| `Live` | `Long` | `27.55` | 140,510,000.00 USD | 0.00 USD | 1,300.00 USD | `-72.42%` | `47.31` |
| `Live` | `Long` | `27.65` | 140,510,000.00 USD | 0.00 USD | 3,590.00 USD | `-72.32%` | `129.70` |
| `Live` | `Long` | `27.85` | 140,510,000.00 USD | 0.00 USD | 412.18 USD | `-72.12%` | `14.80` |
| `Live` | `Long` | `27.95` | 140,510,000.00 USD | 0.00 USD | 605.40 USD | `-72.02%` | `21.66` |
| `Live` | `Long` | `28.05` | 140,510,000.00 USD | 0.00 USD | 2,930.00 USD | `-71.92%` | `104.42` |
| `Live` | `Long` | `28.25` | 140,500,000.00 USD | 0.00 USD | 9,610.00 USD | `-71.72%` | `340.00` |
| `Live` | `Long` | `28.35` | 140,490,000.00 USD | 0.00 USD | 6,200.00 USD | `-71.62%` | `218.55` |
| `Live` | `Long` | `28.45` | 140,490,000.00 USD | 0.00 USD | 980.96 USD | `-71.52%` | `34.48` |
| `Live` | `Long` | `28.75` | 140,490,000.00 USD | 0.00 USD | 763.60 USD | `-71.22%` | `26.56` |
| `Live` | `Long` | `28.85` | 140,490,000.00 USD | 0.00 USD | 825.11 USD | `-71.12%` | `28.60` |
| `Live` | `Long` | `28.95` | 140,490,000.00 USD | 0.00 USD | 2,920.00 USD | `-71.02%` | `100.71` |
| `Live` | `Long` | `29.15` | 140,480,000.00 USD | 0.00 USD | 11,590.00 USD | `-70.82%` | `397.62` |
| `Live` | `Long` | `29.25` | 140,470,000.00 USD | 0.00 USD | 32,410.00 USD | `-70.72%` | `1,108.13` |
| `Live` | `Long` | `29.45` | 140,440,000.00 USD | 0.00 USD | 61,700.00 USD | `-70.52%` | `2,095.00` |
| `Live` | `Long` | `29.55` | 140,380,000.00 USD | 0.00 USD | 1,480.00 USD | `-70.42%` | `50.00` |
| `Live` | `Long` | `29.75` | 140,380,000.00 USD | 0.00 USD | 2,760.00 USD | `-70.22%` | `92.74` |
| `Live` | `Long` | `30.05` | 140,370,000.00 USD | 0.00 USD | 3,010.00 USD | `-69.91%` | `100.04` |
| `Live` | `Long` | `30.15` | 140,370,000.00 USD | 0.00 USD | 53,500.00 USD | `-69.81%` | `1,774.62` |
| `Live` | `Long` | `30.35` | 140,320,000.00 USD | 0.00 USD | 10,380.00 USD | `-69.61%` | `341.92` |
| `Live` | `Long` | `30.55` | 140,310,000.00 USD | 0.00 USD | 2,590.00 USD | `-69.41%` | `84.85` |
| `Live` | `Long` | `30.65` | 140,300,000.00 USD | 0.00 USD | 1,910.00 USD | `-69.31%` | `62.28` |
| `Live` | `Long` | `30.75` | 140,300,000.00 USD | 0.00 USD | 693,470.00 USD | `-69.21%` | `22,551.90` |
| `Live` | `Long` | `30.95` | 139,610,000.00 USD | 0.00 USD | 1,070.00 USD | `-69.01%` | `34.66` |
| `Live` | `Long` | `31.15` | 139,610,000.00 USD | 0.00 USD | 26,940.00 USD | `-68.81%` | `864.91` |
| `Live` | `Long` | `31.25` | 139,580,000.00 USD | 0.00 USD | 14,760.00 USD | `-68.71%` | `472.38` |
| `Live` | `Long` | `31.35` | 139,560,000.00 USD | 0.00 USD | 38,730.00 USD | `-68.61%` | `1,235.38` |
| `Live` | `Long` | `31.45` | 139,530,000.00 USD | 0.00 USD | 278.33 USD | `-68.51%` | `8.85` |
| `Live` | `Long` | `31.55` | 139,530,000.00 USD | 0.00 USD | 1,560.00 USD | `-68.41%` | `49.45` |
| `Live` | `Long` | `31.65` | 139,520,000.00 USD | 0.00 USD | 214.59 USD | `-68.31%` | `6.78` |
| `Live` | `Long` | `31.85` | 139,520,000.00 USD | 0.00 USD | 911.55 USD | `-68.11%` | `28.62` |
| `Live` | `Long` | `31.95` | 139,520,000.00 USD | 0.00 USD | 4,350.00 USD | `-68.01%` | `136.10` |
| `Live` | `Long` | `32.15` | 139,520,000.00 USD | 0.00 USD | 1,450.00 USD | `-67.81%` | `45.06` |
| `Live` | `Long` | `32.75` | 139,520,000.00 USD | 0.00 USD | 274.77 USD | `-67.21%` | `8.39` |
| `Live` | `Long` | `32.85` | 139,520,000.00 USD | 0.00 USD | 5,240.00 USD | `-67.11%` | `159.61` |
| `Live` | `Long` | `33.35` | 139,510,000.00 USD | 0.00 USD | 33,350.00 USD | `-66.61%` | `1,000.00` |
| `Live` | `Long` | `33.45` | 139,480,000.00 USD | 0.00 USD | 50,640.00 USD | `-66.51%` | `1,513.85` |
| `Live` | `Long` | `33.55` | 139,430,000.00 USD | 0.00 USD | 944.10 USD | `-66.41%` | `28.14` |
| `Live` | `Long` | `33.75` | 139,430,000.00 USD | 0.00 USD | 318,010.00 USD | `-66.21%` | `9,422.56` |
| `Live` | `Long` | `34.15` | 139,110,000.00 USD | 0.00 USD | 4,650.00 USD | `-65.81%` | `136.16` |
| `Live` | `Long` | `34.65` | 139,100,000.00 USD | 0.00 USD | 3,140.00 USD | `-65.31%` | `90.50` |
| `Live` | `Long` | `34.75` | 139,100,000.00 USD | 0.00 USD | 6,580,000.00 USD | `-65.21%` | `189,478.86` |
| `Live` | `Long` | `34.95` | 132,520,000.00 USD | 0.00 USD | 4,270.00 USD | `-65.01%` | `122.11` |
| `Live` | `Long` | `35.15` | 132,510,000.00 USD | 0.00 USD | 441.84 USD | `-64.81%` | `12.57` |
| `Live` | `Long` | `35.25` | 132,510,000.00 USD | 0.00 USD | 17,860.00 USD | `-64.71%` | `506.77` |
| `Live` | `Long` | `35.35` | 132,490,000.00 USD | 0.00 USD | 340.77 USD | `-64.61%` | `9.64` |
| `Live` | `Long` | `35.75` | 132,490,000.00 USD | 0.00 USD | 5,880.00 USD | `-64.21%` | `164.57` |
| `Live` | `Long` | `35.95` | 132,490,000.00 USD | 0.00 USD | 5,610.00 USD | `-64.01%` | `156.13` |
| `Live` | `Long` | `36.15` | 132,480,000.00 USD | 0.00 USD | 5,570.00 USD | `-63.81%` | `154.13` |
| `Live` | `Long` | `36.35` | 132,480,000.00 USD | 0.00 USD | 4,410.00 USD | `-63.61%` | `121.32` |
| `Live` | `Long` | `36.45` | 132,470,000.00 USD | 0.00 USD | 2,410.00 USD | `-63.51%` | `66.24` |
| `Live` | `Long` | `36.55` | 132,470,000.00 USD | 0.00 USD | 2,940.00 USD | `-63.41%` | `80.49` |
| `Live` | `Long` | `36.75` | 132,470,000.00 USD | 0.00 USD | 500.90 USD | `-63.21%` | `13.63` |
| `Live` | `Long` | `36.95` | 132,470,000.00 USD | 0.00 USD | 112,510.00 USD | `-63.01%` | `3,045.00` |
| `Live` | `Long` | `37.25` | 132,350,000.00 USD | 0.00 USD | 373.62 USD | `-62.71%` | `10.03` |
| `Live` | `Long` | `37.35` | 132,350,000.00 USD | 0.00 USD | 38,140.00 USD | `-62.61%` | `1,021.26` |
| `Live` | `Long` | `37.45` | 132,320,000.00 USD | 0.00 USD | 1,050.00 USD | `-62.51%` | `27.92` |
| `Live` | `Long` | `37.55` | 132,310,000.00 USD | 0.00 USD | 2,850.00 USD | `-62.41%` | `75.81` |
| `Live` | `Long` | `37.65` | 132,310,000.00 USD | 0.00 USD | 2,430.00 USD | `-62.31%` | `64.52` |
| `Live` | `Long` | `37.85` | 132,310,000.00 USD | 0.00 USD | 189,470.00 USD | `-62.11%` | `5,005.69` |
| `Live` | `Long` | `37.95` | 132,120,000.00 USD | 0.00 USD | 4,160.00 USD | `-62.01%` | `109.49` |
| `Live` | `Long` | `38.05` | 132,120,000.00 USD | 0.00 USD | 542.59 USD | `-61.91%` | `14.26` |
| `Live` | `Long` | `38.45` | 132,110,000.00 USD | 0.00 USD | 3,000,000.00 USD | `-61.50%` | `78,000.00` |
| `Live` | `Long` | `38.75` | 129,120,000.00 USD | 0.00 USD | 2,480.00 USD | `-61.20%` | `63.95` |
| `Live` | `Long` | `38.85` | 129,110,000.00 USD | 0.00 USD | 4,270.00 USD | `-61.10%` | `109.96` |
| `Live` | `Long` | `38.95` | 129,110,000.00 USD | 0.00 USD | 607.62 USD | `-61.00%` | `15.60` |
| `Live` | `Long` | `39.05` | 129,110,000.00 USD | 0.00 USD | 50,470.00 USD | `-60.90%` | `1,292.50` |
| `Live` | `Long` | `39.25` | 129,060,000.00 USD | 0.00 USD | 827.00 USD | `-60.70%` | `21.07` |
| `Live` | `Long` | `39.35` | 129,060,000.00 USD | 0.00 USD | 4,260.00 USD | `-60.60%` | `108.26` |
| `Live` | `Long` | `39.45` | 129,050,000.00 USD | 0.00 USD | 1,130.00 USD | `-60.50%` | `28.55` |
| `Live` | `Long` | `39.65` | 129,050,000.00 USD | 0.00 USD | 1,560.00 USD | `-60.30%` | `39.31` |
| `Live` | `Long` | `39.75` | 129,050,000.00 USD | 0.00 USD | 159.00 USD | `-60.20%` | `4.00` |
| `Live` | `Long` | `39.85` | 129,050,000.00 USD | 0.00 USD | 1,390.00 USD | `-60.10%` | `34.86` |
| `Live` | `Long` | `40.05` | 129,050,000.00 USD | 0.00 USD | 10,950.00 USD | `-59.90%` | `273.48` |
| `Live` | `Long` | `40.15` | 129,040,000.00 USD | 0.00 USD | 15,910.00 USD | `-59.80%` | `396.38` |
| `Live` | `Long` | `40.25` | 129,020,000.00 USD | 0.00 USD | 41,500.00 USD | `-59.70%` | `1,031.08` |
| `Live` | `Long` | `40.55` | 128,980,000.00 USD | 0.00 USD | 3,160.00 USD | `-59.40%` | `77.90` |
| `Live` | `Long` | `40.65` | 128,980,000.00 USD | 0.00 USD | 7,850.00 USD | `-59.30%` | `193.00` |
| `Live` | `Long` | `40.85` | 128,970,000.00 USD | 0.00 USD | 2,770.00 USD | `-59.10%` | `67.92` |
| `Live` | `Long` | `40.95` | 128,970,000.00 USD | 0.00 USD | 5,670.00 USD | `-59.00%` | `138.37` |
| `Live` | `Long` | `41.05` | 128,960,000.00 USD | 0.00 USD | 10,990.00 USD | `-58.90%` | `267.69` |
| `Live` | `Long` | `41.15` | 128,950,000.00 USD | 0.00 USD | 3,440.00 USD | `-58.80%` | `83.48` |
| `Live` | `Long` | `41.25` | 128,950,000.00 USD | 0.00 USD | 368.36 USD | `-58.70%` | `8.93` |
| `Live` | `Long` | `41.35` | 128,950,000.00 USD | 0.00 USD | 148.45 USD | `-58.60%` | `3.59` |
| `Live` | `Long` | `41.55` | 128,950,000.00 USD | 0.00 USD | 427.13 USD | `-58.40%` | `10.28` |
| `Live` | `Long` | `41.65` | 128,950,000.00 USD | 0.00 USD | 770.11 USD | `-58.30%` | `18.49` |
| `Live` | `Long` | `41.75` | 128,940,000.00 USD | 0.00 USD | 1,380.00 USD | `-58.20%` | `33.09` |
| `Live` | `Long` | `41.85` | 128,940,000.00 USD | 0.00 USD | 21,150.00 USD | `-58.10%` | `505.39` |
| `Live` | `Long` | `41.95` | 128,920,000.00 USD | 0.00 USD | 1,210.00 USD | `-58.00%` | `28.91` |
| `Live` | `Long` | `42.05` | 128,920,000.00 USD | 0.00 USD | 10,340.00 USD | `-57.90%` | `245.93` |
| `Live` | `Long` | `42.15` | 128,910,000.00 USD | 0.00 USD | 2,590.00 USD | `-57.80%` | `61.49` |
| `Live` | `Long` | `42.25` | 128,910,000.00 USD | 0.00 USD | 1,020,000.00 USD | `-57.70%` | `24,130.96` |
| `Live` | `Long` | `42.35` | 127,890,000.00 USD | 0.00 USD | 307.04 USD | `-57.60%` | `7.25` |
| `Live` | `Long` | `42.65` | 127,890,000.00 USD | 0.00 USD | 57,330.00 USD | `-57.30%` | `1,344.19` |
| `Live` | `Long` | `42.75` | 127,830,000.00 USD | 0.00 USD | 855.00 USD | `-57.20%` | `20.00` |
| `Live` | `Long` | `43.05` | 127,830,000.00 USD | 0.00 USD | 4,300.00 USD | `-56.90%` | `100.00` |
| `Live` | `Long` | `43.35` | 127,830,000.00 USD | 0.00 USD | 4,710.00 USD | `-56.60%` | `108.68` |
| `Live` | `Long` | `43.45` | 127,820,000.00 USD | 0.00 USD | 1,260.00 USD | `-56.50%` | `29.06` |
| `Live` | `Long` | `43.55` | 127,820,000.00 USD | 0.00 USD | 34,820.00 USD | `-56.40%` | `799.54` |
| `Live` | `Long` | `43.75` | 127,780,000.00 USD | 0.00 USD | 76,670.00 USD | `-56.20%` | `1,752.43` |
| `Live` | `Long` | `43.95` | 127,710,000.00 USD | 0.00 USD | 242.16 USD | `-56.00%` | `5.51` |
| `Live` | `Long` | `44.05` | 127,710,000.00 USD | 0.00 USD | 11,330.00 USD | `-55.90%` | `257.20` |
| `Live` | `Long` | `44.25` | 127,700,000.00 USD | 0.00 USD | 18,430.00 USD | `-55.70%` | `416.42` |
| `Live` | `Long` | `44.35` | 127,680,000.00 USD | 0.00 USD | 22,840.00 USD | `-55.60%` | `514.94` |
| `Live` | `Long` | `44.55` | 127,660,000.00 USD | 0.00 USD | 17,870.00 USD | `-55.40%` | `401.03` |
| `Live` | `Long` | `44.65` | 127,640,000.00 USD | 0.00 USD | 125,070.00 USD | `-55.30%` | `2,801.14` |
| `Live` | `Long` | `44.75` | 127,510,000.00 USD | 0.00 USD | 59,120.00 USD | `-55.20%` | `1,321.06` |
| `Live` | `Long` | `44.85` | 127,450,000.00 USD | 0.00 USD | 3,300.00 USD | `-55.10%` | `73.69` |
| `Live` | `Long` | `44.95` | 127,450,000.00 USD | 0.00 USD | 4,350.00 USD | `-55.00%` | `96.78` |
| `Live` | `Long` | `45.15` | 127,450,000.00 USD | 0.00 USD | 179.70 USD | `-54.80%` | `3.98` |
| `Live` | `Long` | `45.35` | 127,450,000.00 USD | 0.00 USD | 4,100.00 USD | `-54.60%` | `90.30` |
| `Live` | `Long` | `45.45` | 127,440,000.00 USD | 0.00 USD | 9,980.00 USD | `-54.50%` | `219.48` |
| `Live` | `Long` | `45.55` | 127,430,000.00 USD | 0.00 USD | 9,050.00 USD | `-54.40%` | `198.64` |
| `Live` | `Long` | `45.65` | 127,420,000.00 USD | 0.00 USD | 871.00 USD | `-54.30%` | `19.08` |
| `Live` | `Long` | `45.75` | 127,420,000.00 USD | 0.00 USD | 9,450.00 USD | `-54.20%` | `206.46` |
| `Live` | `Long` | `45.85` | 127,410,000.00 USD | 0.00 USD | 3,050.00 USD | `-54.10%` | `66.48` |
| `Live` | `Long` | `45.95` | 127,410,000.00 USD | 0.00 USD | 26,070.00 USD | `-54.00%` | `567.34` |
| `Live` | `Long` | `46.05` | 127,380,000.00 USD | 0.00 USD | 921,000.00 USD | `-53.90%` | `20,000.00` |
| `Live` | `Long` | `46.15` | 126,460,000.00 USD | 0.00 USD | 142.14 USD | `-53.80%` | `3.08` |
| `Live` | `Long` | `46.25` | 126,460,000.00 USD | 0.00 USD | 2,080.00 USD | `-53.70%` | `44.99` |
| `Live` | `Long` | `46.45` | 126,460,000.00 USD | 0.00 USD | 824.95 USD | `-53.50%` | `17.76` |
| `Live` | `Long` | `46.55` | 126,460,000.00 USD | 0.00 USD | 522.76 USD | `-53.40%` | `11.23` |
| `Live` | `Long` | `46.65` | 126,460,000.00 USD | 0.00 USD | 933,540.00 USD | `-53.30%` | `20,011.62` |
| `Live` | `Long` | `46.75` | 125,520,000.00 USD | 0.00 USD | 374.00 USD | `-53.20%` | `8.00` |
| `Live` | `Long` | `46.85` | 125,520,000.00 USD | 0.00 USD | 140.55 USD | `-53.10%` | `3.00` |
| `Live` | `Long` | `46.95` | 125,520,000.00 USD | 0.00 USD | 2,090.00 USD | `-53.00%` | `44.48` |
| `Live` | `Long` | `47.05` | 125,520,000.00 USD | 0.00 USD | 3,850,000.00 USD | `-52.89%` | `81,851.78` |
| `Live` | `Long` | `47.15` | 121,670,000.00 USD | 0.00 USD | 51,780.00 USD | `-52.79%` | `1,098.25` |
| `Live` | `Long` | `47.25` | 121,620,000.00 USD | 0.00 USD | 3,050.00 USD | `-52.69%` | `64.59` |
| `Live` | `Long` | `47.35` | 121,620,000.00 USD | 0.00 USD | 400.11 USD | `-52.59%` | `8.45` |
| `Live` | `Long` | `47.55` | 121,620,000.00 USD | 0.00 USD | 106.04 USD | `-52.39%` | `2.23` |
| `Live` | `Long` | `47.65` | 121,620,000.00 USD | 0.00 USD | 105,250.00 USD | `-52.29%` | `2,208.83` |
| `Live` | `Long` | `47.75` | 121,510,000.00 USD | 0.00 USD | 160.92 USD | `-52.19%` | `3.37` |
| `Live` | `Long` | `47.95` | 121,510,000.00 USD | 0.00 USD | 435.39 USD | `-51.99%` | `9.08` |
| `Live` | `Long` | `48.05` | 121,510,000.00 USD | 0.00 USD | 4,630.00 USD | `-51.89%` | `96.46` |
| `Live` | `Long` | `48.15` | 121,510,000.00 USD | 0.00 USD | 5,470.00 USD | `-51.79%` | `113.54` |
| `Live` | `Long` | `48.25` | 121,500,000.00 USD | 0.00 USD | 5,510.00 USD | `-51.69%` | `114.11` |
| `Live` | `Long` | `48.35` | 121,490,000.00 USD | 0.00 USD | 1,970.00 USD | `-51.59%` | `40.67` |
| `Live` | `Long` | `48.45` | 121,490,000.00 USD | 0.00 USD | 14,710.00 USD | `-51.49%` | `303.71` |
| `Live` | `Long` | `48.55` | 121,480,000.00 USD | 0.00 USD | 3,770.00 USD | `-51.39%` | `77.60` |
| `Live` | `Long` | `48.65` | 121,470,000.00 USD | 0.00 USD | 13,880.00 USD | `-51.29%` | `285.23` |
| `Live` | `Long` | `48.75` | 121,460,000.00 USD | 0.00 USD | 453.38 USD | `-51.19%` | `9.30` |
| `Live` | `Long` | `48.85` | 121,460,000.00 USD | 0.00 USD | 12,410.00 USD | `-51.09%` | `254.11` |
| `Live` | `Long` | `48.95` | 121,450,000.00 USD | 0.00 USD | 7,960.00 USD | `-50.99%` | `162.62` |
| `Live` | `Long` | `49.05` | 121,440,000.00 USD | 0.00 USD | 1,980.00 USD | `-50.89%` | `40.40` |
| `Live` | `Long` | `49.15` | 121,440,000.00 USD | 0.00 USD | 10,850.00 USD | `-50.79%` | `220.76` |
| `Live` | `Long` | `49.25` | 121,430,000.00 USD | 0.00 USD | 469.84 USD | `-50.69%` | `9.54` |
| `Live` | `Long` | `49.35` | 121,430,000.00 USD | 0.00 USD | 585.29 USD | `-50.59%` | `11.86` |
| `Live` | `Long` | `49.45` | 121,430,000.00 USD | 0.00 USD | 5,700.00 USD | `-50.49%` | `115.36` |
| `Live` | `Long` | `49.55` | 121,420,000.00 USD | 0.00 USD | 27,880.00 USD | `-50.39%` | `562.58` |
| `Live` | `Long` | `49.65` | 121,390,000.00 USD | 0.00 USD | 892.21 USD | `-50.29%` | `17.97` |
| `Live` | `Long` | `49.95` | 121,390,000.00 USD | 0.00 USD | 14,670.00 USD | `-49.99%` | `293.63` |
| `Live` | `Long` | `50.05` | 121,380,000.00 USD | 0.00 USD | 8,560.00 USD | `-49.89%` | `171.08` |
| `Live` | `Long` | `50.15` | 121,370,000.00 USD | 0.00 USD | 1,390.00 USD | `-49.79%` | `27.77` |
| `Live` | `Long` | `50.25` | 121,370,000.00 USD | 0.00 USD | 22,830.00 USD | `-49.69%` | `454.26` |
| `Live` | `Long` | `50.45` | 121,340,000.00 USD | 0.00 USD | 9,790.00 USD | `-49.49%` | `193.96` |
| `Live` | `Long` | `50.55` | 121,330,000.00 USD | 0.00 USD | 2,910.00 USD | `-49.39%` | `57.47` |
| `Live` | `Long` | `50.65` | 121,330,000.00 USD | 0.00 USD | 824.08 USD | `-49.29%` | `16.27` |
| `Live` | `Long` | `50.75` | 121,330,000.00 USD | 0.00 USD | 12,040.00 USD | `-49.19%` | `237.21` |
| `Live` | `Long` | `50.85` | 121,320,000.00 USD | 0.00 USD | 19,130.00 USD | `-49.09%` | `376.18` |
| `Live` | `Long` | `50.95` | 121,300,000.00 USD | 0.00 USD | 2,820.00 USD | `-48.99%` | `55.29` |
| `Live` | `Long` | `51.05` | 121,300,000.00 USD | 0.00 USD | 2,680.00 USD | `-48.89%` | `52.57` |
| `Live` | `Long` | `51.15` | 121,290,000.00 USD | 0.00 USD | 61,080.00 USD | `-48.79%` | `1,194.04` |
| `Live` | `Long` | `51.25` | 121,230,000.00 USD | 0.00 USD | 11,710.00 USD | `-48.69%` | `228.44` |
| `Live` | `Long` | `51.35` | 121,220,000.00 USD | 0.00 USD | 6,260.00 USD | `-48.59%` | `121.89` |
| `Live` | `Long` | `51.45` | 121,210,000.00 USD | 0.00 USD | 8,540.00 USD | `-48.49%` | `166.02` |
| `Live` | `Long` | `51.55` | 121,210,000.00 USD | 0.00 USD | 17,880.00 USD | `-48.39%` | `346.90` |
| `Live` | `Long` | `51.65` | 121,190,000.00 USD | 0.00 USD | 774.23 USD | `-48.29%` | `14.99` |
| `Live` | `Long` | `51.75` | 121,190,000.00 USD | 0.00 USD | 34,200.00 USD | `-48.19%` | `660.91` |
| `Live` | `Long` | `51.85` | 121,150,000.00 USD | 0.00 USD | 62,680.00 USD | `-48.09%` | `1,208.95` |
| `Live` | `Long` | `51.95` | 121,090,000.00 USD | 0.00 USD | 565,190.00 USD | `-47.99%` | `10,879.56` |
| `Live` | `Long` | `52.05` | 120,520,000.00 USD | 0.00 USD | 98,480.00 USD | `-47.89%` | `1,891.98` |
| `Live` | `Long` | `52.15` | 120,430,000.00 USD | 0.00 USD | 4,270.00 USD | `-47.79%` | `81.90` |
| `Live` | `Long` | `52.25` | 120,420,000.00 USD | 0.00 USD | 6,720.00 USD | `-47.69%` | `128.70` |
| `Live` | `Long` | `52.35` | 120,420,000.00 USD | 0.00 USD | 3,980.00 USD | `-47.59%` | `76.11` |
| `Live` | `Long` | `52.45` | 120,410,000.00 USD | 0.00 USD | 3,540.00 USD | `-47.49%` | `67.51` |
| `Live` | `Long` | `52.55` | 120,410,000.00 USD | 0.00 USD | 1,740.00 USD | `-47.39%` | `33.04` |
| `Live` | `Long` | `52.65` | 120,410,000.00 USD | 0.00 USD | 4,420.00 USD | `-47.29%` | `83.92` |
| `Live` | `Long` | `52.75` | 120,400,000.00 USD | 0.00 USD | 39,500.00 USD | `-47.19%` | `748.86` |
| `Live` | `Long` | `52.85` | 120,360,000.00 USD | 0.00 USD | 4,380.00 USD | `-47.09%` | `82.94` |
| `Live` | `Long` | `52.95` | 120,360,000.00 USD | 0.00 USD | 5,360.00 USD | `-46.99%` | `101.30` |
| `Live` | `Long` | `53.05` | 120,350,000.00 USD | 0.00 USD | 6,430.00 USD | `-46.89%` | `121.30` |
| `Live` | `Long` | `53.15` | 120,350,000.00 USD | 0.00 USD | 10,150.00 USD | `-46.79%` | `191.05` |
| `Live` | `Long` | `53.25` | 120,340,000.00 USD | 0.00 USD | 1,050,000.00 USD | `-46.69%` | `19,715.81` |
| `Live` | `Long` | `53.35` | 119,290,000.00 USD | 0.00 USD | 2,130.00 USD | `-46.59%` | `39.99` |
| `Live` | `Long` | `53.45` | 119,280,000.00 USD | 0.00 USD | 34,550.00 USD | `-46.49%` | `646.33` |
| `Live` | `Long` | `53.55` | 119,250,000.00 USD | 0.00 USD | 46,410.00 USD | `-46.39%` | `866.75` |
| `Live` | `Long` | `53.65` | 119,200,000.00 USD | 0.00 USD | 2,530.00 USD | `-46.29%` | `47.19` |
| `Live` | `Long` | `53.75` | 119,200,000.00 USD | 0.00 USD | 18,180.00 USD | `-46.19%` | `338.18` |
| `Live` | `Long` | `53.85` | 119,180,000.00 USD | 0.00 USD | 6,610.00 USD | `-46.09%` | `122.68` |
| `Live` | `Long` | `53.95` | 119,180,000.00 USD | 0.00 USD | 83,470.00 USD | `-45.99%` | `1,547.13` |
| `Live` | `Long` | `54.05` | 119,090,000.00 USD | 0.00 USD | 2,160,000.00 USD | `-45.89%` | `40,006.49` |
| `Live` | `Long` | `54.15` | 116,930,000.00 USD | 0.00 USD | 15,030.00 USD | `-45.79%` | `277.53` |
| `Live` | `Long` | `54.25` | 116,910,000.00 USD | 0.00 USD | 11,500.00 USD | `-45.69%` | `211.99` |
| `Live` | `Long` | `54.35` | 116,900,000.00 USD | 0.00 USD | 2,460.00 USD | `-45.59%` | `45.23` |
| `Live` | `Long` | `54.45` | 116,900,000.00 USD | 0.00 USD | 43,920.00 USD | `-45.49%` | `806.58` |
| `Live` | `Long` | `54.55` | 116,860,000.00 USD | 0.00 USD | 63,370.00 USD | `-45.39%` | `1,161.73` |
| `Live` | `Long` | `54.65` | 116,790,000.00 USD | 0.00 USD | 2,420.00 USD | `-45.29%` | `44.29` |
| `Live` | `Long` | `54.75` | 116,790,000.00 USD | 0.00 USD | 17,320.00 USD | `-45.19%` | `316.32` |
| `Live` | `Long` | `54.85` | 116,770,000.00 USD | 0.00 USD | 864,880.00 USD | `-45.09%` | `15,768.09` |
| `Live` | `Long` | `54.95` | 115,910,000.00 USD | 0.00 USD | 163,690.00 USD | `-44.99%` | `2,978.89` |
| `Live` | `Long` | `55.05` | 115,750,000.00 USD | 0.00 USD | 6,000.00 USD | `-44.89%` | `108.99` |
| `Live` | `Long` | `55.15` | 115,740,000.00 USD | 0.00 USD | 10,600.00 USD | `-44.79%` | `192.26` |
| `Live` | `Long` | `55.25` | 115,730,000.00 USD | 0.00 USD | 49,450.00 USD | `-44.69%` | `895.08` |
| `Live` | `Long` | `55.35` | 115,680,000.00 USD | 0.00 USD | 9,810.00 USD | `-44.59%` | `177.30` |
| `Live` | `Long` | `55.45` | 115,670,000.00 USD | 0.00 USD | 6,450.00 USD | `-44.49%` | `116.35` |
| `Live` | `Long` | `55.55` | 115,660,000.00 USD | 0.00 USD | 1,110,000.00 USD | `-44.38%` | `20,013.19` |
| `Live` | `Long` | `55.65` | 114,550,000.00 USD | 0.00 USD | 31,860.00 USD | `-44.28%` | `572.47` |
| `Live` | `Long` | `55.75` | 114,520,000.00 USD | 0.00 USD | 85,360.00 USD | `-44.18%` | `1,531.18` |
| `Live` | `Long` | `55.85` | 114,430,000.00 USD | 0.00 USD | 8,280.00 USD | `-44.08%` | `148.18` |
| `Live` | `Long` | `56.05` | 114,430,000.00 USD | 0.00 USD | 8,360.00 USD | `-43.88%` | `149.22` |
| `Live` | `Long` | `56.15` | 114,420,000.00 USD | 0.00 USD | 22,690.00 USD | `-43.78%` | `404.10` |
| `Live` | `Long` | `56.25` | 114,390,000.00 USD | 0.00 USD | 24,190.00 USD | `-43.68%` | `429.98` |
| `Live` | `Long` | `56.35` | 114,370,000.00 USD | 0.00 USD | 7,880.00 USD | `-43.58%` | `139.77` |
| `Live` | `Long` | `56.45` | 114,360,000.00 USD | 0.00 USD | 5,350.00 USD | `-43.48%` | `94.82` |
| `Live` | `Long` | `56.55` | 114,360,000.00 USD | 0.00 USD | 4,730.00 USD | `-43.38%` | `83.63` |
| `Live` | `Long` | `56.65` | 114,350,000.00 USD | 0.00 USD | 3,590.00 USD | `-43.28%` | `63.40` |
| `Live` | `Long` | `56.75` | 114,350,000.00 USD | 0.00 USD | 39,680.00 USD | `-43.18%` | `699.20` |
| `Live` | `Long` | `56.85` | 114,310,000.00 USD | 0.00 USD | 122.80 USD | `-43.08%` | `2.16` |
| `Live` | `Long` | `56.95` | 114,310,000.00 USD | 0.00 USD | 14,710.00 USD | `-42.98%` | `258.32` |
| `Live` | `Long` | `57.05` | 114,290,000.00 USD | 0.00 USD | 346,070.00 USD | `-42.88%` | `6,066.06` |
| `Live` | `Long` | `57.15` | 113,950,000.00 USD | 0.00 USD | 5,380.00 USD | `-42.78%` | `94.22` |
| `Live` | `Long` | `57.25` | 113,940,000.00 USD | 0.00 USD | 1,780.00 USD | `-42.68%` | `31.02` |
| `Live` | `Long` | `57.35` | 113,940,000.00 USD | 0.00 USD | 9,580.00 USD | `-42.58%` | `167.07` |
| `Live` | `Long` | `57.45` | 113,930,000.00 USD | 0.00 USD | 17,480.00 USD | `-42.48%` | `304.28` |
| `Live` | `Long` | `57.55` | 113,910,000.00 USD | 0.00 USD | 6,580.00 USD | `-42.38%` | `114.37` |
| `Live` | `Long` | `57.65` | 113,910,000.00 USD | 0.00 USD | 242.13 USD | `-42.28%` | `4.20` |
| `Live` | `Long` | `57.75` | 113,910,000.00 USD | 0.00 USD | 42,310.00 USD | `-42.18%` | `732.64` |
| `Live` | `Long` | `57.85` | 113,860,000.00 USD | 0.00 USD | 28,030.00 USD | `-42.08%` | `484.46` |
| `Live` | `Long` | `57.95` | 113,840,000.00 USD | 0.00 USD | 324.52 USD | `-41.98%` | `5.60` |
| `Live` | `Long` | `58.05` | 113,840,000.00 USD | 0.00 USD | 5,010.00 USD | `-41.88%` | `86.34` |
| `Live` | `Long` | `58.15` | 113,830,000.00 USD | 0.00 USD | 123,440.00 USD | `-41.78%` | `2,122.70` |
| `Live` | `Long` | `58.25` | 113,710,000.00 USD | 0.00 USD | 6,670.00 USD | `-41.68%` | `114.44` |
| `Live` | `Long` | `58.35` | 113,700,000.00 USD | 0.00 USD | 22,100.00 USD | `-41.58%` | `378.72` |
| `Live` | `Long` | `58.45` | 113,680,000.00 USD | 0.00 USD | 10,130.00 USD | `-41.48%` | `173.34` |
| `Live` | `Long` | `58.55` | 113,670,000.00 USD | 0.00 USD | 2,970.00 USD | `-41.38%` | `50.81` |
| `Live` | `Long` | `58.65` | 113,670,000.00 USD | 0.00 USD | 4,640.00 USD | `-41.28%` | `79.11` |
| `Live` | `Long` | `58.75` | 113,660,000.00 USD | 0.00 USD | 453.55 USD | `-41.18%` | `7.72` |
| `Live` | `Long` | `58.85` | 113,660,000.00 USD | 0.00 USD | 7,310.00 USD | `-41.08%` | `124.13` |
| `Live` | `Long` | `58.95` | 113,650,000.00 USD | 0.00 USD | 650.81 USD | `-40.98%` | `11.04` |
| `Live` | `Long` | `59.05` | 113,650,000.00 USD | 0.00 USD | 12,180.00 USD | `-40.88%` | `206.30` |
| `Live` | `Long` | `59.15` | 113,640,000.00 USD | 0.00 USD | 6,170.00 USD | `-40.78%` | `104.31` |
| `Live` | `Long` | `59.25` | 113,630,000.00 USD | 0.00 USD | 19,550.00 USD | `-40.68%` | `330.00` |
| `Live` | `Long` | `59.35` | 113,620,000.00 USD | 0.00 USD | 28,320.00 USD | `-40.58%` | `477.21` |
| `Live` | `Long` | `59.45` | 113,590,000.00 USD | 0.00 USD | 9,240.00 USD | `-40.48%` | `155.46` |
| `Live` | `Long` | `59.55` | 113,580,000.00 USD | 0.00 USD | 8,740.00 USD | `-40.38%` | `146.83` |
| `Live` | `Long` | `59.65` | 113,570,000.00 USD | 0.00 USD | 5,110.00 USD | `-40.28%` | `85.59` |
| `Live` | `Long` | `59.75` | 113,560,000.00 USD | 0.00 USD | 13,880.00 USD | `-40.18%` | `232.30` |
| `Live` | `Long` | `59.85` | 113,550,000.00 USD | 0.00 USD | 150.82 USD | `-40.08%` | `2.52` |
| `Live` | `Long` | `59.95` | 113,550,000.00 USD | 0.00 USD | 37,880.00 USD | `-39.98%` | `631.87` |
| `Live` | `Long` | `60.05` | 113,510,000.00 USD | 0.00 USD | 12,840.00 USD | `-39.88%` | `213.86` |
| `Live` | `Long` | `60.15` | 113,500,000.00 USD | 0.00 USD | 38,140.00 USD | `-39.78%` | `634.16` |
| `Live` | `Long` | `60.25` | 113,460,000.00 USD | 0.00 USD | 2,340.00 USD | `-39.68%` | `38.84` |
| `Live` | `Long` | `60.35` | 113,460,000.00 USD | 0.00 USD | 2,090.00 USD | `-39.58%` | `34.55` |
| `Live` | `Long` | `60.45` | 113,460,000.00 USD | 0.00 USD | 557.35 USD | `-39.48%` | `9.22` |
| `Live` | `Long` | `60.55` | 113,460,000.00 USD | 0.00 USD | 2,760.00 USD | `-39.38%` | `45.51` |
| `Live` | `Long` | `60.65` | 113,450,000.00 USD | 0.00 USD | 5,880.00 USD | `-39.28%` | `96.94` |
| `Live` | `Long` | `60.75` | 113,450,000.00 USD | 0.00 USD | 1,650.00 USD | `-39.18%` | `27.09` |
| `Live` | `Long` | `60.85` | 113,450,000.00 USD | 0.00 USD | 36,120.00 USD | `-39.08%` | `593.57` |
| `Live` | `Long` | `60.95` | 113,410,000.00 USD | 0.00 USD | 55,130.00 USD | `-38.98%` | `904.59` |
| `Live` | `Long` | `61.05` | 113,350,000.00 USD | 0.00 USD | 22,740.00 USD | `-38.88%` | `372.46` |
| `Live` | `Long` | `61.15` | 113,330,000.00 USD | 0.00 USD | 683.66 USD | `-38.78%` | `11.18` |
| `Live` | `Long` | `61.25` | 113,330,000.00 USD | 0.00 USD | 125,370.00 USD | `-38.68%` | `2,046.90` |
| `Live` | `Long` | `61.35` | 113,210,000.00 USD | 0.00 USD | 19,870.00 USD | `-38.58%` | `323.92` |
| `Live` | `Long` | `61.45` | 113,190,000.00 USD | 0.00 USD | 14,620.00 USD | `-38.48%` | `237.85` |
| `Live` | `Long` | `61.55` | 113,170,000.00 USD | 0.00 USD | 2,490.00 USD | `-38.38%` | `40.45` |
| `Live` | `Long` | `61.65` | 113,170,000.00 USD | 0.00 USD | 21,020.00 USD | `-38.28%` | `340.91` |
| `Live` | `Long` | `61.75` | 113,150,000.00 USD | 0.00 USD | 16,580.00 USD | `-38.18%` | `268.54` |
| `Live` | `Long` | `61.85` | 113,130,000.00 USD | 0.00 USD | 18,940.00 USD | `-38.08%` | `306.24` |
| `Live` | `Long` | `61.95` | 113,110,000.00 USD | 0.00 USD | 14,100.00 USD | `-37.98%` | `227.53` |
| `Live` | `Long` | `62.05` | 113,100,000.00 USD | 0.00 USD | 4,790.00 USD | `-37.88%` | `77.17` |
| `Live` | `Long` | `62.15` | 113,090,000.00 USD | 0.00 USD | 25,780.00 USD | `-37.78%` | `414.87` |
| `Live` | `Long` | `62.25` | 113,070,000.00 USD | 0.00 USD | 1,800.00 USD | `-37.68%` | `28.90` |
| `Live` | `Long` | `62.35` | 113,070,000.00 USD | 0.00 USD | 31,770.00 USD | `-37.58%` | `509.49` |
| `Live` | `Long` | `62.45` | 113,030,000.00 USD | 0.00 USD | 120,170.00 USD | `-37.48%` | `1,924.29` |
| `Live` | `Long` | `62.55` | 112,910,000.00 USD | 0.00 USD | 3,130.00 USD | `-37.38%` | `50.00` |
| `Live` | `Long` | `62.65` | 112,910,000.00 USD | 0.00 USD | 2,050.00 USD | `-37.28%` | `32.79` |
| `Live` | `Long` | `62.75` | 112,910,000.00 USD | 0.00 USD | 3,140.00 USD | `-37.18%` | `49.97` |
| `Live` | `Long` | `62.85` | 112,910,000.00 USD | 0.00 USD | 31,310.00 USD | `-37.08%` | `498.17` |
| `Live` | `Long` | `62.95` | 112,870,000.00 USD | 0.00 USD | 74,040.00 USD | `-36.98%` | `1,176.16` |
| `Live` | `Long` | `63.05` | 112,800,000.00 USD | 0.00 USD | 17,480.00 USD | `-36.88%` | `277.29` |
| `Live` | `Long` | `63.15` | 112,780,000.00 USD | 0.00 USD | 81,490.00 USD | `-36.78%` | `1,290.43` |
| `Live` | `Long` | `63.25` | 112,700,000.00 USD | 0.00 USD | 14,620.00 USD | `-36.68%` | `231.15` |
| `Live` | `Long` | `63.45` | 112,690,000.00 USD | 0.00 USD | 43,420.00 USD | `-36.48%` | `684.37` |
| `Live` | `Long` | `63.55` | 112,640,000.00 USD | 0.00 USD | 10,530.00 USD | `-36.38%` | `165.71` |
| `Live` | `Long` | `63.65` | 112,630,000.00 USD | 0.00 USD | 9,350.00 USD | `-36.28%` | `146.88` |
| `Live` | `Long` | `63.75` | 112,620,000.00 USD | 0.00 USD | 8,220.00 USD | `-36.18%` | `128.89` |
| `Live` | `Long` | `63.85` | 112,610,000.00 USD | 0.00 USD | 87,380.00 USD | `-36.08%` | `1,368.56` |
| `Live` | `Long` | `63.95` | 112,530,000.00 USD | 0.00 USD | 12,230.00 USD | `-35.98%` | `191.32` |
| `Live` | `Long` | `64.15` | 112,520,000.00 USD | 0.00 USD | 4,550.00 USD | `-35.77%` | `70.96` |
| `Live` | `Long` | `64.25` | 112,510,000.00 USD | 0.00 USD | 4,550.00 USD | `-35.67%` | `70.81` |
| `Live` | `Long` | `64.35` | 112,510,000.00 USD | 0.00 USD | 875.16 USD | `-35.57%` | `13.60` |
| `Live` | `Long` | `64.45` | 112,510,000.00 USD | 0.00 USD | 5,800.00 USD | `-35.47%` | `89.99` |
| `Live` | `Long` | `64.55` | 112,500,000.00 USD | 0.00 USD | 579.66 USD | `-35.37%` | `8.98` |
| `Live` | `Long` | `64.65` | 112,500,000.00 USD | 0.00 USD | 27,600.00 USD | `-35.27%` | `426.99` |
| `Live` | `Long` | `64.75` | 112,470,000.00 USD | 0.00 USD | 5,280.00 USD | `-35.17%` | `81.58` |
| `Live` | `Long` | `64.85` | 112,470,000.00 USD | 0.00 USD | 4,400.00 USD | `-35.07%` | `67.84` |
| `Live` | `Long` | `64.95` | 112,460,000.00 USD | 0.00 USD | 209.79 USD | `-34.97%` | `3.23` |
| `Live` | `Long` | `65.05` | 112,460,000.00 USD | 0.00 USD | 18,350.00 USD | `-34.87%` | `282.02` |
| `Live` | `Long` | `65.15` | 112,440,000.00 USD | 0.00 USD | 12,400.00 USD | `-34.77%` | `190.37` |
| `Live` | `Long` | `65.25` | 112,430,000.00 USD | 0.00 USD | 844.34 USD | `-34.67%` | `12.94` |
| `Live` | `Long` | `65.35` | 112,430,000.00 USD | 0.00 USD | 15,790.00 USD | `-34.57%` | `241.58` |
| `Live` | `Long` | `65.45` | 112,410,000.00 USD | 0.00 USD | 11,800,000.00 USD | `-34.47%` | `180,300.00` |
| `Live` | `Long` | `65.55` | 100,610,000.00 USD | 0.00 USD | 23,320.00 USD | `-34.37%` | `355.75` |
| `Live` | `Long` | `65.65` | 100,590,000.00 USD | 0.00 USD | 58,050.00 USD | `-34.27%` | `884.16` |
| `Live` | `Long` | `65.75` | 100,530,000.00 USD | 0.00 USD | 1,620.00 USD | `-34.17%` | `24.70` |
| `Live` | `Long` | `65.85` | 100,530,000.00 USD | 0.00 USD | 14,380.00 USD | `-34.07%` | `218.31` |
| `Live` | `Long` | `65.95` | 100,520,000.00 USD | 0.00 USD | 11,240.00 USD | `-33.97%` | `170.36` |
| `Live` | `Long` | `66.05` | 100,500,000.00 USD | 0.00 USD | 605.68 USD | `-33.87%` | `9.17` |
| `Live` | `Long` | `66.15` | 100,500,000.00 USD | 0.00 USD | 17,760.00 USD | `-33.77%` | `268.49` |
| `Live` | `Long` | `66.25` | 100,490,000.00 USD | 0.00 USD | 1,180.00 USD | `-33.67%` | `17.75` |
| `Live` | `Long` | `66.35` | 100,490,000.00 USD | 0.00 USD | 1,200.00 USD | `-33.57%` | `18.02` |
| `Live` | `Long` | `66.55` | 100,480,000.00 USD | 0.00 USD | 42,920.00 USD | `-33.37%` | `644.93` |
| `Live` | `Long` | `66.65` | 100,440,000.00 USD | 0.00 USD | 842.46 USD | `-33.27%` | `12.64` |
| `Live` | `Long` | `66.85` | 100,440,000.00 USD | 0.00 USD | 4,420.00 USD | `-33.07%` | `66.17` |
| `Live` | `Long` | `66.95` | 100,440,000.00 USD | 0.00 USD | 937.30 USD | `-32.97%` | `14.00` |
| `Live` | `Long` | `67.05` | 100,440,000.00 USD | 0.00 USD | 33,620.00 USD | `-32.87%` | `501.43` |
| `Live` | `Long` | `67.15` | 100,400,000.00 USD | 0.00 USD | 2,510.00 USD | `-32.77%` | `37.39` |
| `Live` | `Long` | `67.25` | 100,400,000.00 USD | 0.00 USD | 13,780.00 USD | `-32.67%` | `204.86` |
| `Live` | `Long` | `67.35` | 100,390,000.00 USD | 0.00 USD | 1,050.00 USD | `-32.57%` | `15.57` |
| `Live` | `Long` | `67.45` | 100,380,000.00 USD | 0.00 USD | 270.47 USD | `-32.47%` | `4.01` |
| `Live` | `Long` | `67.55` | 100,380,000.00 USD | 0.00 USD | 106,280.00 USD | `-32.37%` | `1,573.29` |
| `Live` | `Long` | `67.65` | 100,280,000.00 USD | 0.00 USD | 159,710.00 USD | `-32.27%` | `2,360.77` |
| `Live` | `Long` | `67.75` | 100,120,000.00 USD | 0.00 USD | 7,740.00 USD | `-32.17%` | `114.17` |
| `Live` | `Long` | `67.85` | 100,110,000.00 USD | 0.00 USD | 2,880.00 USD | `-32.07%` | `42.40` |
| `Live` | `Long` | `67.95` | 100,110,000.00 USD | 0.00 USD | 756,930.00 USD | `-31.97%` | `11,139.56` |
| `Live` | `Long` | `68.05` | 99,350,000.00 USD | 0.00 USD | 271.52 USD | `-31.87%` | `3.99` |
| `Live` | `Long` | `68.15` | 99,350,000.00 USD | 0.00 USD | 37,490,000.00 USD | `-31.77%` | `550,095.11` |
| `Live` | `Long` | `68.25` | 61,860,000.00 USD | 0.00 USD | 13,650.00 USD | `-31.67%` | `199.93` |
| `Live` | `Long` | `68.35` | 61,850,000.00 USD | 0.00 USD | 19,360.00 USD | `-31.57%` | `283.29` |
| `Live` | `Long` | `68.45` | 61,830,000.00 USD | 0.00 USD | 26,940.00 USD | `-31.47%` | `393.58` |
| `Live` | `Long` | `68.55` | 61,800,000.00 USD | 0.00 USD | 22,870.00 USD | `-31.37%` | `333.63` |
| `Live` | `Long` | `68.65` | 61,780,000.00 USD | 0.00 USD | 7,610.00 USD | `-31.27%` | `110.83` |
| `Live` | `Long` | `68.75` | 61,770,000.00 USD | 0.00 USD | 47,000.00 USD | `-31.17%` | `683.60` |
| `Live` | `Long` | `68.85` | 61,720,000.00 USD | 0.00 USD | 3,240.00 USD | `-31.07%` | `47.11` |
| `Live` | `Long` | `68.95` | 61,720,000.00 USD | 0.00 USD | 57,510.00 USD | `-30.97%` | `834.15` |
| `Live` | `Long` | `69.05` | 61,660,000.00 USD | 0.00 USD | 39,100.00 USD | `-30.87%` | `566.30` |
| `Live` | `Long` | `69.15` | 61,620,000.00 USD | 0.00 USD | 7,190.00 USD | `-30.77%` | `103.93` |
| `Live` | `Long` | `69.25` | 61,620,000.00 USD | 0.00 USD | 26,470.00 USD | `-30.67%` | `382.22` |
| `Live` | `Long` | `69.35` | 61,590,000.00 USD | 0.00 USD | 3,550.00 USD | `-30.57%` | `51.20` |
| `Live` | `Long` | `69.45` | 61,590,000.00 USD | 0.00 USD | 16,310.00 USD | `-30.47%` | `234.84` |
| `Live` | `Long` | `69.55` | 61,570,000.00 USD | 0.00 USD | 10,070.00 USD | `-30.37%` | `144.80` |
| `Live` | `Long` | `69.65` | 61,560,000.00 USD | 0.00 USD | 10,560.00 USD | `-30.27%` | `151.55` |
| `Live` | `Long` | `69.75` | 61,550,000.00 USD | 0.00 USD | 31,040.00 USD | `-30.17%` | `445.08` |
| `Live` | `Long` | `69.85` | 61,520,000.00 USD | 0.00 USD | 21,860.00 USD | `-30.07%` | `312.96` |
| `Live` | `Long` | `69.95` | 61,500,000.00 USD | 0.00 USD | 16,400.00 USD | `-29.97%` | `234.39` |
| `Live` | `Long` | `70.05` | 61,480,000.00 USD | 0.00 USD | 3,030.00 USD | `-29.87%` | `43.21` |
| `Live` | `Long` | `70.15` | 61,480,000.00 USD | 0.00 USD | 20,420.00 USD | `-29.77%` | `291.16` |
| `Live` | `Long` | `70.25` | 61,460,000.00 USD | 0.00 USD | 73,520.00 USD | `-29.67%` | `1,046.55` |
| `Live` | `Long` | `70.35` | 61,380,000.00 USD | 0.00 USD | 2,130,000.00 USD | `-29.57%` | `30,306.57` |
| `Live` | `Long` | `70.45` | 59,250,000.00 USD | 0.00 USD | 1,220,000.00 USD | `-29.47%` | `17,325.39` |
| `Live` | `Long` | `70.65` | 58,030,000.00 USD | 0.00 USD | 12,780.00 USD | `-29.27%` | `180.91` |
| `Live` | `Long` | `70.75` | 58,020,000.00 USD | 0.00 USD | 34,270.00 USD | `-29.17%` | `484.41` |
| `Live` | `Long` | `70.85` | 57,980,000.00 USD | 0.00 USD | 20,920.00 USD | `-29.07%` | `295.21` |
| `Live` | `Long` | `70.95` | 57,960,000.00 USD | 0.00 USD | 6,970.00 USD | `-28.97%` | `98.25` |
| `Live` | `Long` | `71.05` | 57,960,000.00 USD | 0.00 USD | 49,470.00 USD | `-28.87%` | `696.32` |
| `Live` | `Long` | `71.15` | 57,910,000.00 USD | 0.00 USD | 62,230.00 USD | `-28.77%` | `874.67` |
| `Live` | `Long` | `71.25` | 57,840,000.00 USD | 0.00 USD | 55,120.00 USD | `-28.67%` | `773.66` |
| `Live` | `Long` | `71.35` | 57,790,000.00 USD | 0.00 USD | 9,520.00 USD | `-28.57%` | `133.36` |
| `Live` | `Long` | `71.45` | 57,780,000.00 USD | 0.00 USD | 18,840.00 USD | `-28.47%` | `263.73` |
| `Live` | `Long` | `71.55` | 57,760,000.00 USD | 0.00 USD | 310,740.00 USD | `-28.37%` | `4,343.00` |
| `Live` | `Long` | `71.65` | 57,450,000.00 USD | 0.00 USD | 520.90 USD | `-28.27%` | `7.27` |
| `Live` | `Long` | `71.75` | 57,450,000.00 USD | 0.00 USD | 28,190.00 USD | `-28.17%` | `392.87` |
| `Live` | `Long` | `71.85` | 57,420,000.00 USD | 0.00 USD | 9,160.00 USD | `-28.07%` | `127.52` |
| `Live` | `Long` | `71.95` | 57,410,000.00 USD | 0.00 USD | 22,890.00 USD | `-27.97%` | `318.19` |
| `Live` | `Long` | `72.05` | 57,390,000.00 USD | 0.00 USD | 12,050.00 USD | `-27.87%` | `167.27` |
| `Live` | `Long` | `72.15` | 57,380,000.00 USD | 0.00 USD | 165,720.00 USD | `-27.77%` | `2,296.93` |
| `Live` | `Long` | `72.25` | 57,210,000.00 USD | 0.00 USD | 41,840.00 USD | `-27.67%` | `579.08` |
| `Live` | `Long` | `72.35` | 57,170,000.00 USD | 0.00 USD | 6,370.00 USD | `-27.57%` | `87.99` |
| `Live` | `Long` | `72.45` | 57,160,000.00 USD | 0.00 USD | 7,370.00 USD | `-27.47%` | `101.74` |
| `Live` | `Long` | `72.55` | 57,160,000.00 USD | 0.00 USD | 17,050.00 USD | `-27.37%` | `235.03` |
| `Live` | `Long` | `72.65` | 57,140,000.00 USD | 0.00 USD | 13,250.00 USD | `-27.26%` | `182.38` |
| `Live` | `Long` | `72.75` | 57,130,000.00 USD | 0.00 USD | 46,640.00 USD | `-27.16%` | `641.13` |
| `Live` | `Long` | `72.85` | 57,080,000.00 USD | 0.00 USD | 1,600,000.00 USD | `-27.06%` | `22,016.88` |
| `Live` | `Long` | `72.95` | 55,470,000.00 USD | 0.00 USD | 9,630.00 USD | `-26.96%` | `131.95` |
| `Live` | `Long` | `73.05` | 55,470,000.00 USD | 0.00 USD | 47,590.00 USD | `-26.86%` | `651.50` |
| `Live` | `Long` | `73.15` | 55,420,000.00 USD | 0.00 USD | 4,110.00 USD | `-26.76%` | `56.14` |
| `Live` | `Long` | `73.25` | 55,410,000.00 USD | 0.00 USD | 36,380.00 USD | `-26.66%` | `496.61` |
| `Live` | `Long` | `73.35` | 55,380,000.00 USD | 0.00 USD | 3,410.00 USD | `-26.56%` | `46.52` |
| `Live` | `Long` | `73.45` | 55,370,000.00 USD | 0.00 USD | 259,640.00 USD | `-26.46%` | `3,534.89` |
| `Live` | `Long` | `73.55` | 55,110,000.00 USD | 0.00 USD | 10,950.00 USD | `-26.36%` | `148.91` |
| `Live` | `Long` | `73.65` | 55,100,000.00 USD | 0.00 USD | 100,210.00 USD | `-26.26%` | `1,360.62` |
| `Live` | `Long` | `73.75` | 55,000,000.00 USD | 0.00 USD | 73,540.00 USD | `-26.16%` | `997.21` |
| `Live` | `Long` | `73.85` | 54,930,000.00 USD | 0.00 USD | 21,270.00 USD | `-26.06%` | `287.96` |
| `Live` | `Long` | `73.95` | 54,910,000.00 USD | 0.00 USD | 40,150.00 USD | `-25.96%` | `542.87` |
| `Live` | `Long` | `74.05` | 54,870,000.00 USD | 0.00 USD | 25,710.00 USD | `-25.86%` | `347.17` |
| `Live` | `Long` | `74.15` | 54,840,000.00 USD | 0.00 USD | 9,960.00 USD | `-25.76%` | `134.32` |
| `Live` | `Long` | `74.25` | 54,830,000.00 USD | 0.00 USD | 44,690.00 USD | `-25.66%` | `601.92` |
| `Live` | `Long` | `74.35` | 54,790,000.00 USD | 0.00 USD | 111,410.00 USD | `-25.56%` | `1,498.45` |
| `Live` | `Long` | `74.45` | 54,680,000.00 USD | 0.00 USD | 104,270.00 USD | `-25.46%` | `1,400.59` |
| `Live` | `Long` | `74.55` | 54,570,000.00 USD | 0.00 USD | 10,330.00 USD | `-25.36%` | `138.56` |
| `Live` | `Long` | `74.75` | 54,560,000.00 USD | 0.00 USD | 37,430.00 USD | `-25.16%` | `500.69` |
| `Live` | `Long` | `74.85` | 54,520,000.00 USD | 0.00 USD | 22,530.00 USD | `-25.06%` | `300.96` |
| `Live` | `Long` | `74.95` | 54,500,000.00 USD | 0.00 USD | 20,450.00 USD | `-24.96%` | `272.85` |
| `Live` | `Long` | `75.05` | 54,480,000.00 USD | 0.00 USD | 286,760.00 USD | `-24.86%` | `3,820.98` |
| `Live` | `Long` | `75.15` | 54,190,000.00 USD | 0.00 USD | 4,180.00 USD | `-24.76%` | `55.67` |
| `Live` | `Long` | `75.25` | 54,190,000.00 USD | 0.00 USD | 38,370.00 USD | `-24.66%` | `509.86` |
| `Live` | `Long` | `75.35` | 54,150,000.00 USD | 0.00 USD | 15,520.00 USD | `-24.56%` | `206.02` |
| `Live` | `Long` | `75.45` | 54,140,000.00 USD | 0.00 USD | 2,010.00 USD | `-24.46%` | `26.63` |
| `Live` | `Long` | `75.55` | 54,130,000.00 USD | 0.00 USD | 28,710.00 USD | `-24.36%` | `380.01` |
| `Live` | `Long` | `75.65` | 54,110,000.00 USD | 0.00 USD | 129,590.00 USD | `-24.26%` | `1,713.02` |
| `Live` | `Long` | `75.75` | 53,980,000.00 USD | 0.00 USD | 55,240.00 USD | `-24.16%` | `729.27` |
| `Live` | `Long` | `75.85` | 53,920,000.00 USD | 0.00 USD | 37,490.00 USD | `-24.06%` | `494.28` |
| `Live` | `Long` | `75.95` | 53,880,000.00 USD | 0.00 USD | 38,420.00 USD | `-23.96%` | `505.80` |
| `Live` | `Long` | `76.05` | 53,840,000.00 USD | 0.00 USD | 1,850.00 USD | `-23.86%` | `24.30` |
| `Live` | `Long` | `76.15` | 53,840,000.00 USD | 0.00 USD | 35,140.00 USD | `-23.76%` | `461.40` |
| `Live` | `Long` | `76.25` | 53,810,000.00 USD | 0.00 USD | 1,880.00 USD | `-23.66%` | `24.63` |
| `Live` | `Long` | `76.35` | 53,810,000.00 USD | 0.00 USD | 33,110.00 USD | `-23.56%` | `433.65` |
| `Live` | `Long` | `76.55` | 53,770,000.00 USD | 0.00 USD | 56,440.00 USD | `-23.36%` | `737.34` |
| `Live` | `Long` | `76.65` | 53,720,000.00 USD | 0.00 USD | 3,220.00 USD | `-23.26%` | `42.00` |
| `Live` | `Long` | `76.75` | 53,710,000.00 USD | 0.00 USD | 36,970.00 USD | `-23.16%` | `481.64` |
| `Live` | `Long` | `76.85` | 53,680,000.00 USD | 0.00 USD | 15,790.00 USD | `-23.06%` | `205.43` |
| `Live` | `Long` | `76.95` | 53,660,000.00 USD | 0.00 USD | 28,120.00 USD | `-22.96%` | `365.40` |
| `Live` | `Long` | `77.05` | 53,630,000.00 USD | 0.00 USD | 24,640.00 USD | `-22.86%` | `319.82` |
| `Live` | `Long` | `77.15` | 53,610,000.00 USD | 0.00 USD | 3,640.00 USD | `-22.76%` | `47.13` |
| `Live` | `Long` | `77.25` | 53,600,000.00 USD | 0.00 USD | 32,220.00 USD | `-22.66%` | `417.08` |
| `Live` | `Long` | `77.35` | 53,570,000.00 USD | 0.00 USD | 3,700.00 USD | `-22.56%` | `47.80` |
| `Live` | `Long` | `77.45` | 53,570,000.00 USD | 0.00 USD | 26,660.00 USD | `-22.46%` | `344.16` |
| `Live` | `Long` | `77.55` | 53,540,000.00 USD | 0.00 USD | 59,620.00 USD | `-22.36%` | `768.79` |
| `Live` | `Long` | `77.65` | 53,480,000.00 USD | 0.00 USD | 205,370.00 USD | `-22.26%` | `2,644.77` |
| `Live` | `Long` | `77.75` | 53,280,000.00 USD | 0.00 USD | 364,430.00 USD | `-22.16%` | `4,687.25` |
| `Live` | `Long` | `77.85` | 52,910,000.00 USD | 0.00 USD | 19,060.00 USD | `-22.06%` | `244.85` |
| `Live` | `Long` | `77.95` | 52,890,000.00 USD | 0.00 USD | 702,830.00 USD | `-21.96%` | `9,016.40` |
| `Live` | `Long` | `78.05` | 52,190,000.00 USD | 0.00 USD | 17,080.00 USD | `-21.86%` | `218.87` |
| `Live` | `Long` | `78.15` | 52,170,000.00 USD | 0.00 USD | 4,080,000.00 USD | `-21.76%` | `52,201.33` |
| `Live` | `Long` | `78.25` | 48,090,000.00 USD | 0.00 USD | 314,050.00 USD | `-21.66%` | `4,013.47` |
| `Live` | `Long` | `78.35` | 47,780,000.00 USD | 0.00 USD | 64,400.00 USD | `-21.56%` | `821.93` |
| `Live` | `Long` | `78.45` | 47,720,000.00 USD | 0.00 USD | 40,930.00 USD | `-21.46%` | `521.68` |
| `Live` | `Long` | `78.55` | 47,670,000.00 USD | 0.00 USD | 242,250.00 USD | `-21.36%` | `3,084.06` |
| `Live` | `Long` | `78.65` | 47,430,000.00 USD | 0.00 USD | 80,590.00 USD | `-21.26%` | `1,024.67` |
| `Live` | `Long` | `78.75` | 47,350,000.00 USD | 0.00 USD | 166,510.00 USD | `-21.16%` | `2,114.45` |
| `Live` | `Long` | `78.85` | 47,180,000.00 USD | 0.00 USD | 9,620.00 USD | `-21.06%` | `121.97` |
| `Live` | `Long` | `78.95` | 47,180,000.00 USD | 0.00 USD | 2,260.00 USD | `-20.96%` | `28.67` |
| `Live` | `Long` | `79.05` | 47,170,000.00 USD | 0.00 USD | 1,380.00 USD | `-20.86%` | `17.48` |
| `Live` | `Long` | `79.15` | 47,170,000.00 USD | 0.00 USD | 643,210.00 USD | `-20.76%` | `8,126.50` |
| `Live` | `Long` | `79.25` | 46,530,000.00 USD | 0.00 USD | 114,920.00 USD | `-20.66%` | `1,450.10` |
| `Live` | `Long` | `79.35` | 46,410,000.00 USD | 0.00 USD | 8,140.00 USD | `-20.56%` | `102.56` |
| `Live` | `Long` | `79.45` | 46,410,000.00 USD | 0.00 USD | 15,750.00 USD | `-20.46%` | `198.25` |
| `Live` | `Long` | `79.55` | 46,390,000.00 USD | 0.00 USD | 674.58 USD | `-20.36%` | `8.48` |
| `Live` | `Long` | `79.65` | 46,390,000.00 USD | 0.00 USD | 149.74 USD | `-20.26%` | `1.88` |
| `Live` | `Long` | `79.75` | 46,390,000.00 USD | 0.00 USD | 485.68 USD | `-20.16%` | `6.09` |
| `Live` | `Long` | `79.85` | 46,390,000.00 USD | 0.00 USD | 12,020.00 USD | `-20.06%` | `150.48` |
| `Live` | `Long` | `79.95` | 46,380,000.00 USD | 0.00 USD | 7,240.00 USD | `-19.96%` | `90.61` |
| `Live` | `Long` | `80.15` | 46,370,000.00 USD | 0.00 USD | 23,880.00 USD | `-19.76%` | `297.96` |
| `Live` | `Long` | `80.25` | 46,350,000.00 USD | 0.00 USD | 1,680,000.00 USD | `-19.66%` | `20,894.68` |
| `Live` | `Long` | `80.35` | 44,670,000.00 USD | 0.00 USD | 182,170.00 USD | `-19.56%` | `2,267.22` |
| `Live` | `Long` | `80.45` | 44,490,000.00 USD | 0.00 USD | 160,090.00 USD | `-19.46%` | `1,989.91` |
| `Live` | `Long` | `80.55` | 44,330,000.00 USD | 0.00 USD | 22,390.00 USD | `-19.36%` | `277.94` |
| `Live` | `Long` | `80.65` | 44,300,000.00 USD | 0.00 USD | 25,780.00 USD | `-19.26%` | `319.63` |
| `Live` | `Long` | `80.75` | 44,280,000.00 USD | 0.00 USD | 3,200.00 USD | `-19.16%` | `39.58` |
| `Live` | `Long` | `80.85` | 44,270,000.00 USD | 0.00 USD | 19,980.00 USD | `-19.06%` | `247.07` |
| `Live` | `Long` | `80.95` | 44,250,000.00 USD | 0.00 USD | 7,010.00 USD | `-18.96%` | `86.54` |
| `Live` | `Long` | `81.05` | 44,250,000.00 USD | 0.00 USD | 2,230,000.00 USD | `-18.86%` | `27,536.78` |
| `Live` | `Long` | `81.15` | 42,020,000.00 USD | 0.00 USD | 3,260.00 USD | `-18.75%` | `40.14` |
| `Live` | `Long` | `81.25` | 42,010,000.00 USD | 0.00 USD | 26,530.00 USD | `-18.65%` | `326.51` |
| `Live` | `Long` | `81.35` | 41,990,000.00 USD | 0.00 USD | 58,860.00 USD | `-18.55%` | `723.51` |
| `Live` | `Long` | `81.45` | 41,930,000.00 USD | 0.00 USD | 70,130.00 USD | `-18.45%` | `861.01` |
| `Live` | `Long` | `81.55` | 41,860,000.00 USD | 0.00 USD | 27,800.00 USD | `-18.35%` | `340.86` |
| `Live` | `Long` | `81.65` | 41,830,000.00 USD | 0.00 USD | 35,020.00 USD | `-18.25%` | `428.96` |
| `Live` | `Long` | `81.75` | 41,790,000.00 USD | 0.00 USD | 65,150.00 USD | `-18.15%` | `796.99` |
| `Live` | `Long` | `81.85` | 41,730,000.00 USD | 0.00 USD | 40,780.00 USD | `-18.05%` | `498.22` |
| `Live` | `Long` | `81.95` | 41,690,000.00 USD | 0.00 USD | 31,640.00 USD | `-17.95%` | `386.10` |
| `Live` | `Long` | `82.05` | 41,660,000.00 USD | 0.00 USD | 124,470.00 USD | `-17.85%` | `1,517.05` |
| `Live` | `Long` | `82.15` | 41,530,000.00 USD | 0.00 USD | 870,580.00 USD | `-17.75%` | `10,597.42` |
| `Live` | `Long` | `82.25` | 40,660,000.00 USD | 0.00 USD | 20,720.00 USD | `-17.65%` | `251.86` |
| `Live` | `Long` | `82.35` | 40,640,000.00 USD | 0.00 USD | 26,580.00 USD | `-17.55%` | `322.81` |
| `Live` | `Long` | `82.45` | 40,610,000.00 USD | 0.00 USD | 211,320.00 USD | `-17.45%` | `2,563.05` |
| `Live` | `Long` | `82.55` | 40,400,000.00 USD | 0.00 USD | 38,980.00 USD | `-17.35%` | `472.20` |
| `Live` | `Long` | `82.65` | 40,360,000.00 USD | 0.00 USD | 121,240.00 USD | `-17.25%` | `1,466.92` |
| `Live` | `Long` | `82.75` | 40,240,000.00 USD | 0.00 USD | 30,430.00 USD | `-17.15%` | `367.69` |
| `Live` | `Long` | `82.85` | 40,210,000.00 USD | 0.00 USD | 31,470.00 USD | `-17.05%` | `379.88` |
| `Live` | `Long` | `82.95` | 40,180,000.00 USD | 0.00 USD | 17,060.00 USD | `-16.95%` | `205.66` |
| `Live` | `Long` | `83.05` | 40,160,000.00 USD | 0.00 USD | 37,350.00 USD | `-16.85%` | `449.71` |
| `Live` | `Long` | `83.15` | 40,130,000.00 USD | 0.00 USD | 25,420.00 USD | `-16.75%` | `305.68` |
| `Live` | `Long` | `83.25` | 40,100,000.00 USD | 0.00 USD | 40,780.00 USD | `-16.65%` | `489.80` |
| `Live` | `Long` | `83.35` | 40,060,000.00 USD | 0.00 USD | 155,780.00 USD | `-16.55%` | `1,868.95` |
| `Live` | `Long` | `83.45` | 39,900,000.00 USD | 0.00 USD | 22,860.00 USD | `-16.45%` | `273.99` |
| `Live` | `Long` | `83.55` | 39,880,000.00 USD | 0.00 USD | 34,370.00 USD | `-16.35%` | `411.37` |
| `Live` | `Long` | `83.65` | 39,850,000.00 USD | 0.00 USD | 71,540.00 USD | `-16.25%` | `855.22` |
| `Live` | `Long` | `83.75` | 39,780,000.00 USD | 0.00 USD | 72,310.00 USD | `-16.15%` | `863.40` |
| `Live` | `Long` | `83.85` | 39,700,000.00 USD | 0.00 USD | 209,940.00 USD | `-16.05%` | `2,503.76` |
| `Live` | `Long` | `83.95` | 39,490,000.00 USD | 0.00 USD | 20,640.00 USD | `-15.95%` | `245.81` |
| `Live` | `Long` | `84.05` | 39,470,000.00 USD | 0.00 USD | 181,910.00 USD | `-15.85%` | `2,164.26` |
| `Live` | `Long` | `84.15` | 39,290,000.00 USD | 0.00 USD | 114,710.00 USD | `-15.75%` | `1,363.11` |
| `Live` | `Long` | `84.25` | 39,180,000.00 USD | 0.00 USD | 33,770.00 USD | `-15.65%` | `400.78` |
| `Live` | `Long` | `84.35` | 39,140,000.00 USD | 0.00 USD | 53,940.00 USD | `-15.55%` | `639.51` |
| `Live` | `Long` | `84.45` | 39,090,000.00 USD | 0.00 USD | 91,090.00 USD | `-15.45%` | `1,078.62` |
| `Live` | `Long` | `84.55` | 39,000,000.00 USD | 0.00 USD | 7,160.00 USD | `-15.35%` | `84.65` |
| `Live` | `Long` | `84.65` | 38,990,000.00 USD | 0.00 USD | 60,500.00 USD | `-15.25%` | `714.72` |
| `Live` | `Long` | `84.75` | 38,930,000.00 USD | 0.00 USD | 60,970.00 USD | `-15.15%` | `719.41` |
| `Live` | `Long` | `84.85` | 38,870,000.00 USD | 0.00 USD | 2,300.00 USD | `-15.05%` | `27.09` |
| `Live` | `Long` | `84.95` | 38,870,000.00 USD | 0.00 USD | 2,170.00 USD | `-14.95%` | `25.49` |
| `Live` | `Long` | `85.05` | 38,860,000.00 USD | 0.00 USD | 77,070.00 USD | `-14.85%` | `906.14` |
| `Live` | `Long` | `85.15` | 38,790,000.00 USD | 0.00 USD | 15,110.00 USD | `-14.75%` | `177.43` |
| `Live` | `Long` | `85.25` | 38,770,000.00 USD | 0.00 USD | 560,340.00 USD | `-14.65%` | `6,572.86` |
| `Live` | `Long` | `85.35` | 38,210,000.00 USD | 0.00 USD | 35,030.00 USD | `-14.55%` | `410.45` |
| `Live` | `Long` | `85.45` | 38,180,000.00 USD | 0.00 USD | 29,040.00 USD | `-14.45%` | `339.80` |
| `Live` | `Long` | `85.55` | 38,150,000.00 USD | 0.00 USD | 8,860.00 USD | `-14.35%` | `103.61` |
| `Live` | `Long` | `85.65` | 38,140,000.00 USD | 0.00 USD | 17,880.00 USD | `-14.25%` | `208.79` |
| `Live` | `Long` | `85.75` | 38,120,000.00 USD | 0.00 USD | 4,140.00 USD | `-14.15%` | `48.23` |
| `Live` | `Long` | `85.85` | 38,120,000.00 USD | 0.00 USD | 41,690.00 USD | `-14.05%` | `485.62` |
| `Live` | `Long` | `85.95` | 38,080,000.00 USD | 0.00 USD | 39,990.00 USD | `-13.95%` | `465.32` |
| `Live` | `Long` | `86.05` | 38,040,000.00 USD | 0.00 USD | 163,490.00 USD | `-13.85%` | `1,899.89` |
| `Live` | `Long` | `86.15` | 37,870,000.00 USD | 0.00 USD | 119,700.00 USD | `-13.75%` | `1,389.49` |
| `Live` | `Long` | `86.25` | 37,750,000.00 USD | 0.00 USD | 42,970.00 USD | `-13.65%` | `498.16` |
| `Live` | `Long` | `86.35` | 37,710,000.00 USD | 0.00 USD | 24,000.00 USD | `-13.55%` | `277.91` |
| `Live` | `Long` | `86.45` | 37,690,000.00 USD | 0.00 USD | 31,090.00 USD | `-13.45%` | `359.64` |
| `Live` | `Long` | `86.55` | 37,650,000.00 USD | 0.00 USD | 202,180.00 USD | `-13.35%` | `2,336.04` |
| `Live` | `Long` | `86.65` | 37,450,000.00 USD | 0.00 USD | 118,650.00 USD | `-13.25%` | `1,369.26` |
| `Live` | `Long` | `86.75` | 37,330,000.00 USD | 0.00 USD | 55,780.00 USD | `-13.15%` | `642.98` |
| `Live` | `Long` | `86.85` | 37,280,000.00 USD | 0.00 USD | 25,290.00 USD | `-13.05%` | `291.22` |
| `Live` | `Long` | `86.95` | 37,250,000.00 USD | 0.00 USD | 81,620.00 USD | `-12.95%` | `938.65` |
| `Live` | `Long` | `87.05` | 37,170,000.00 USD | 0.00 USD | 244,410.00 USD | `-12.85%` | `2,807.70` |
| `Live` | `Long` | `87.15` | 36,930,000.00 USD | 0.00 USD | 273,840.00 USD | `-12.75%` | `3,142.17` |
| `Live` | `Long` | `87.25` | 36,650,000.00 USD | 0.00 USD | 16,540.00 USD | `-12.65%` | `189.54` |
| `Live` | `Long` | `87.35` | 36,640,000.00 USD | 0.00 USD | 29,950.00 USD | `-12.55%` | `342.83` |
| `Live` | `Long` | `87.45` | 36,610,000.00 USD | 0.00 USD | 187,780.00 USD | `-12.45%` | `2,147.27` |
| `Live` | `Long` | `87.55` | 36,420,000.00 USD | 0.00 USD | 185,620.00 USD | `-12.35%` | `2,120.11` |
| `Live` | `Long` | `87.65` | 36,230,000.00 USD | 0.00 USD | 465,580.00 USD | `-12.25%` | `5,311.82` |
| `Live` | `Long` | `87.75` | 35,770,000.00 USD | 0.00 USD | 5,050.00 USD | `-12.15%` | `57.53` |
| `Live` | `Long` | `87.85` | 35,760,000.00 USD | 0.00 USD | 28,150.00 USD | `-12.05%` | `320.40` |
| `Live` | `Long` | `87.95` | 35,730,000.00 USD | 0.00 USD | 15,710.00 USD | `-11.95%` | `178.60` |
| `Live` | `Long` | `88.05` | 35,720,000.00 USD | 0.00 USD | 3,310,000.00 USD | `-11.85%` | `37,600.36` |
| `Live` | `Long` | `88.15` | 32,410,000.00 USD | 0.00 USD | 24,030.00 USD | `-11.75%` | `272.64` |
| `Live` | `Long` | `88.25` | 32,380,000.00 USD | 0.00 USD | 64,120.00 USD | `-11.65%` | `726.60` |
| `Live` | `Long` | `88.35` | 32,320,000.00 USD | 0.00 USD | 34,940.00 USD | `-11.55%` | `395.52` |
| `Live` | `Long` | `88.45` | 32,280,000.00 USD | 0.00 USD | 104,460.00 USD | `-11.45%` | `1,181.04` |
| `Live` | `Long` | `88.55` | 32,180,000.00 USD | 0.00 USD | 3,070.00 USD | `-11.35%` | `34.63` |
| `Live` | `Long` | `88.65` | 32,180,000.00 USD | 0.00 USD | 162,310.00 USD | `-11.25%` | `1,830.87` |
| `Live` | `Long` | `88.75` | 32,010,000.00 USD | 0.00 USD | 177,330.00 USD | `-11.15%` | `1,998.10` |
| `Live` | `Long` | `88.85` | 31,840,000.00 USD | 0.00 USD | 25,310.00 USD | `-11.05%` | `284.90` |
| `Live` | `Long` | `88.95` | 31,810,000.00 USD | 0.00 USD | 79,760.00 USD | `-10.95%` | `896.64` |
| `Live` | `Long` | `89.05` | 31,730,000.00 USD | 0.00 USD | 10,550.00 USD | `-10.85%` | `118.47` |
| `Live` | `Long` | `89.15` | 31,720,000.00 USD | 0.00 USD | 10,140.00 USD | `-10.75%` | `113.74` |
| `Live` | `Long` | `89.25` | 31,710,000.00 USD | 0.00 USD | 18,790.00 USD | `-10.65%` | `210.57` |
| `Live` | `Long` | `89.35` | 31,690,000.00 USD | 0.00 USD | 214,440.00 USD | `-10.55%` | `2,400.04` |
| `Live` | `Long` | `89.45` | 31,480,000.00 USD | 0.00 USD | 169,960.00 USD | `-10.45%` | `1,900.11` |
| `Live` | `Long` | `89.55` | 31,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | `-10.35%` | `14,633.66` |
| `Live` | `Long` | `89.65` | 30,000,000.00 USD | 0.00 USD | 5,080.00 USD | `-10.24%` | `56.72` |
| `Live` | `Long` | `89.75` | 29,990,000.00 USD | 0.00 USD | 81,270.00 USD | `-10.14%` | `905.52` |
| `Live` | `Long` | `89.85` | 29,910,000.00 USD | 0.00 USD | 39,690.00 USD | `-10.04%` | `441.75` |
| `Live` | `Long` | `89.95` | 29,870,000.00 USD | 0.00 USD | 27,000.00 USD | `-9.94%` | `300.14` |
| `Live` | `Long` | `90.05` | 29,840,000.00 USD | 0.00 USD | 8,210.00 USD | `-9.84%` | `91.19` |
| `Live` | `Long` | `90.15` | 29,840,000.00 USD | 0.00 USD | 23,430.00 USD | `-9.74%` | `259.86` |
| `Live` | `Long` | `90.25` | 29,810,000.00 USD | 0.00 USD | 10,570.00 USD | `-9.64%` | `117.15` |
| `Live` | `Long` | `90.35` | 29,800,000.00 USD | 0.00 USD | 35,550.00 USD | `-9.54%` | `393.48` |
| `Live` | `Long` | `90.45` | 29,770,000.00 USD | 0.00 USD | 37,560.00 USD | `-9.44%` | `415.26` |
| `Live` | `Long` | `90.55` | 29,730,000.00 USD | 0.00 USD | 8,220.00 USD | `-9.34%` | `90.81` |
| `Live` | `Long` | `90.65` | 29,720,000.00 USD | 0.00 USD | 87,230.00 USD | `-9.24%` | `962.30` |
| `Live` | `Long` | `90.75` | 29,630,000.00 USD | 0.00 USD | 52,590.00 USD | `-9.14%` | `579.53` |
| `Live` | `Long` | `90.85` | 29,580,000.00 USD | 0.00 USD | 45,990.00 USD | `-9.04%` | `506.21` |
| `Live` | `Long` | `90.95` | 29,540,000.00 USD | 0.00 USD | 10,090.00 USD | `-8.94%` | `110.99` |
| `Live` | `Long` | `91.05` | 29,520,000.00 USD | 0.00 USD | 492,790.00 USD | `-8.84%` | `5,412.33` |
| `Live` | `Long` | `91.15` | 29,030,000.00 USD | 0.00 USD | 280,380.00 USD | `-8.74%` | `3,076.08` |
| `Live` | `Long` | `91.25` | 28,750,000.00 USD | 0.00 USD | 39,810.00 USD | `-8.64%` | `436.31` |
| `Live` | `Long` | `91.35` | 28,710,000.00 USD | 0.00 USD | 82,210.00 USD | `-8.54%` | `899.93` |
| `Live` | `Long` | `91.45` | 28,630,000.00 USD | 0.00 USD | 365,890.00 USD | `-8.44%` | `4,000.95` |
| `Live` | `Long` | `91.55` | 28,260,000.00 USD | 0.00 USD | 1,410,000.00 USD | `-8.34%` | `15,436.63` |
| `Live` | `Long` | `91.65` | 26,850,000.00 USD | 0.00 USD | 17,090.00 USD | `-8.24%` | `186.42` |
| `Live` | `Long` | `91.75` | 26,830,000.00 USD | 0.00 USD | 309,530.00 USD | `-8.14%` | `3,373.63` |
| `Live` | `Long` | `91.85` | 26,520,000.00 USD | 0.00 USD | 77,180.00 USD | `-8.04%` | `840.29` |
| `Live` | `Long` | `91.95` | 26,450,000.00 USD | 0.00 USD | 112,500.00 USD | `-7.94%` | `1,223.45` |
| `Live` | `Long` | `92.05` | 26,330,000.00 USD | 0.00 USD | 17,200.00 USD | `-7.84%` | `186.88` |
| `Live` | `Long` | `92.15` | 26,320,000.00 USD | 0.00 USD | 1,090,000.00 USD | `-7.74%` | `11,858.61` |
| `Live` | `Long` | `92.25` | 25,220,000.00 USD | 0.00 USD | 149,610.00 USD | `-7.64%` | `1,621.79` |
| `Live` | `Long` | `92.35` | 25,070,000.00 USD | 0.00 USD | 46,550.00 USD | `-7.54%` | `504.08` |
| `Live` | `Long` | `92.45` | 25,030,000.00 USD | 0.00 USD | 156,810.00 USD | `-7.44%` | `1,696.15` |
| `Live` | `Long` | `92.55` | 24,870,000.00 USD | 0.00 USD | 114,460.00 USD | `-7.34%` | `1,236.70` |
| `Live` | `Long` | `92.65` | 24,760,000.00 USD | 0.00 USD | 191,670.00 USD | `-7.24%` | `2,068.73` |
| `Live` | `Long` | `92.75` | 24,570,000.00 USD | 0.00 USD | 425,980.00 USD | `-7.14%` | `4,592.83` |
| `Live` | `Long` | `92.85` | 24,140,000.00 USD | 0.00 USD | 367,830.00 USD | `-7.04%` | `3,961.60` |
| `Live` | `Long` | `92.95` | 23,770,000.00 USD | 0.00 USD | 22,550.00 USD | `-6.94%` | `242.65` |
| `Live` | `Long` | `93.05` | 23,750,000.00 USD | 0.00 USD | 81,780.00 USD | `-6.84%` | `878.83` |
| `Live` | `Long` | `93.15` | 23,670,000.00 USD | 0.00 USD | 75,520.00 USD | `-6.74%` | `810.74` |
| `Live` | `Long` | `93.25` | 23,590,000.00 USD | 0.00 USD | 296,810.00 USD | `-6.64%` | `3,182.97` |
| `Live` | `Long` | `93.35` | 23,290,000.00 USD | 0.00 USD | 132,180.00 USD | `-6.54%` | `1,415.91` |
| `Live` | `Long` | `93.45` | 23,160,000.00 USD | 0.00 USD | 21,870.00 USD | `-6.44%` | `234.04` |
| `Live` | `Long` | `93.55` | 23,140,000.00 USD | 0.00 USD | 341,510.00 USD | `-6.34%` | `3,650.60` |
| `Live` | `Long` | `93.65` | 22,800,000.00 USD | 0.00 USD | 47,710.00 USD | `-6.24%` | `509.47` |
| `Live` | `Long` | `93.75` | 22,750,000.00 USD | 0.00 USD | 91,550.00 USD | `-6.14%` | `976.51` |
| `Live` | `Long` | `93.85` | 22,660,000.00 USD | 0.00 USD | 120,450.00 USD | `-6.04%` | `1,283.42` |
| `Live` | `Long` | `93.95` | 22,540,000.00 USD | 0.00 USD | 1,950,000.00 USD | `-5.94%` | `20,799.90` |
| `Live` | `Long` | `94.05` | 20,590,000.00 USD | 0.00 USD | 186,970.00 USD | `-5.84%` | `1,987.94` |
| `Live` | `Long` | `94.15` | 20,400,000.00 USD | 0.00 USD | 78,960.00 USD | `-5.74%` | `838.61` |
| `Live` | `Long` | `94.25` | 20,320,000.00 USD | 0.00 USD | 1,090,000.00 USD | `-5.64%` | `11,529.38` |
| `Live` | `Long` | `94.35` | 19,230,000.00 USD | 0.00 USD | 33,820.00 USD | `-5.54%` | `358.40` |
| `Live` | `Long` | `94.45` | 19,200,000.00 USD | 0.00 USD | 926,780.00 USD | `-5.44%` | `9,812.44` |
| `Live` | `Long` | `94.55` | 18,270,000.00 USD | 0.00 USD | 262,610.00 USD | `-5.34%` | `2,777.52` |
| `Live` | `Long` | `94.65` | 18,010,000.00 USD | 0.00 USD | 202,690.00 USD | `-5.24%` | `2,141.45` |
| `Live` | `Long` | `94.75` | 17,810,000.00 USD | 0.00 USD | 47,830.00 USD | `-5.14%` | `504.78` |
| `Live` | `Long` | `94.85` | 17,760,000.00 USD | 0.00 USD | 83,350.00 USD | `-5.04%` | `878.73` |
| `Live` | `Long` | `94.95` | 17,680,000.00 USD | 0.00 USD | 82,180.00 USD | `-4.94%` | `865.51` |
| `Live` | `Long` | `95.05` | 17,590,000.00 USD | 0.00 USD | 207,190.00 USD | `-4.84%` | `2,179.85` |
| `Live` | `Long` | `95.15` | 17,390,000.00 USD | 0.00 USD | 16,510.00 USD | `-4.74%` | `173.50` |
| `Live` | `Long` | `95.25` | 17,370,000.00 USD | 0.00 USD | 309,400.00 USD | `-4.64%` | `3,248.26` |
| `Live` | `Long` | `95.35` | 17,060,000.00 USD | 0.00 USD | 35,320.00 USD | `-4.54%` | `370.45` |
| `Live` | `Long` | `95.45` | 17,030,000.00 USD | 0.00 USD | 166,630.00 USD | `-4.44%` | `1,745.74` |
| `Live` | `Long` | `95.55` | 16,860,000.00 USD | 0.00 USD | 202,790.00 USD | `-4.34%` | `2,122.36` |
| `Live` | `Long` | `95.65` | 16,660,000.00 USD | 0.00 USD | 166,370.00 USD | `-4.24%` | `1,739.36` |
| `Live` | `Long` | `95.75` | 16,490,000.00 USD | 0.00 USD | 89,790.00 USD | `-4.14%` | `937.71` |
| `Live` | `Long` | `95.85` | 16,400,000.00 USD | 0.00 USD | 35,590.00 USD | `-4.04%` | `371.27` |
| `Live` | `Long` | `95.95` | 16,360,000.00 USD | 0.00 USD | 633,290.00 USD | `-3.94%` | `6,600.19` |
| `Live` | `Long` | `96.05` | 15,730,000.00 USD | 0.00 USD | 73,770.00 USD | `-3.84%` | `768.01` |
| `Live` | `Long` | `96.15` | 15,660,000.00 USD | 0.00 USD | 614,360.00 USD | `-3.74%` | `6,389.65` |
| `Live` | `Long` | `96.25` | 15,040,000.00 USD | 0.00 USD | 162,540.00 USD | `-3.64%` | `1,688.69` |
| `Live` | `Long` | `96.35` | 14,880,000.00 USD | 0.00 USD | 12,030.00 USD | `-3.54%` | `124.90` |
| `Live` | `Long` | `96.45` | 14,870,000.00 USD | 0.00 USD | 101,960.00 USD | `-3.44%` | `1,057.11` |
| `Live` | `Long` | `96.55` | 14,770,000.00 USD | 0.00 USD | 106,550.00 USD | `-3.34%` | `1,103.60` |
| `Live` | `Long` | `96.65` | 14,660,000.00 USD | 0.00 USD | 49,990.00 USD | `-3.24%` | `517.27` |
| `Live` | `Long` | `96.75` | 14,610,000.00 USD | 0.00 USD | 341,460.00 USD | `-3.14%` | `3,529.27` |
| `Live` | `Long` | `96.85` | 14,270,000.00 USD | 0.00 USD | 23,740.00 USD | `-3.04%` | `245.11` |
| `Live` | `Long` | `96.95` | 14,240,000.00 USD | 0.00 USD | 23,640.00 USD | `-2.94%` | `243.80` |
| `Live` | `Long` | `97.05` | 14,220,000.00 USD | 0.00 USD | 452,710.00 USD | `-2.84%` | `4,664.74` |
| `Live` | `Long` | `97.15` | 13,770,000.00 USD | 0.00 USD | 252,820.00 USD | `-2.74%` | `2,602.33` |
| `Live` | `Long` | `97.25` | 13,520,000.00 USD | 0.00 USD | 33,050.00 USD | `-2.64%` | `339.85` |
| `Live` | `Long` | `97.35` | 13,480,000.00 USD | 0.00 USD | 153,020.00 USD | `-2.54%` | `1,571.83` |
| `Live` | `Long` | `97.45` | 13,330,000.00 USD | 0.00 USD | 420,520.00 USD | `-2.44%` | `4,315.25` |
| `Live` | `Short` | `97.55` | 115,160.00 USD | 115,160.00 USD | 0.00 USD | `-2.34%` | `1,180.57` |
| `Live` | `Long` | `97.65` | 12,910,000.00 USD | 0.00 USD | 517,090.00 USD | `-2.24%` | `5,295.34` |
| `Live` | `Long` | `97.75` | 12,390,000.00 USD | 0.00 USD | 334,790.00 USD | `-2.14%` | `3,424.92` |
| `Live` | `Long` | `97.85` | 12,060,000.00 USD | 0.00 USD | 128,480.00 USD | `-2.04%` | `1,313.00` |
| `Live` | `Long` | `97.95` | 11,930,000.00 USD | 0.00 USD | 333,740.00 USD | `-1.94%` | `3,407.26` |
| `Live` | `Long` | `98.05` | 11,590,000.00 USD | 0.00 USD | 9,630,000.00 USD | `-1.84%` | `98,193.42` |
| `Live` | `Long` | `98.15` | 1,970,000.00 USD | 0.00 USD | 204,770.00 USD | `-1.74%` | `2,086.25` |
| `Live` | `Long` | `98.25` | 1,760,000.00 USD | 0.00 USD | 543,670.00 USD | `-1.63%` | `5,533.56` |
| `Live` | `Long` | `98.35` | 1,220,000.00 USD | 0.00 USD | 103,360.00 USD | `-1.53%` | `1,050.91` |
| `Live` | `Long` | `98.45` | 1,110,000.00 USD | 0.00 USD | 252,890.00 USD | `-1.43%` | `2,568.67` |
| `Live` | `Long` | `98.55` | 861,890.00 USD | 0.00 USD | 58,520.00 USD | `-1.33%` | `593.83` |
| `Live` | `Long` | `98.65` | 803,370.00 USD | 0.00 USD | 472,720.00 USD | `-1.23%` | `4,791.94` |
| `Live` | `Long` | `98.75` | 330,640.00 USD | 0.00 USD | 31,490.00 USD | `-1.13%` | `318.93` |
| `Live` | `Long` | `98.85` | 299,150.00 USD | 0.00 USD | 65,440.00 USD | `-1.03%` | `662.01` |
| `Live` | `Long` | `98.95` | 233,710.00 USD | 0.00 USD | 12,570.00 USD | `-0.93%` | `126.99` |
| `Live` | `Long` | `99.05` | 221,140.00 USD | 0.00 USD | 31,910.00 USD | `-0.83%` | `322.16` |
| `Live` | `Long` | `99.15` | 189,230.00 USD | 0.00 USD | 13,880.00 USD | `-0.73%` | `139.98` |
| `Live` | `Long` | `99.25` | 175,350.00 USD | 0.00 USD | 1,400.00 USD | `-0.63%` | `14.13` |
| `Live` | `Long` | `99.35` | 173,950.00 USD | 0.00 USD | 90,510.00 USD | `-0.53%` | `910.98` |
| `Live` | `Long` | `99.45` | 83,440.00 USD | 0.00 USD | 1,030.00 USD | `-0.43%` | `10.36` |
| `Live` | `Long` | `99.55` | 82,410.00 USD | 0.00 USD | 34,660.00 USD | `-0.33%` | `348.13` |
| `Live` | `Long` | `99.65` | 47,760.00 USD | 0.00 USD | 14,550.00 USD | `-0.23%` | `146.06` |
| `Live` | `Long` | `99.75` | 33,200.00 USD | 0.00 USD | 11,930.00 USD | `-0.13%` | `119.62` |
| `Live` | `Long` | `99.85` | 21,270.00 USD | 0.00 USD | 21,270.00 USD | `-0.03%` | `213.03` |
| `Live` | `Short` | `100.05` | 118,750.00 USD | 3,580.00 USD | 0.00 USD | `+0.17%` | `35.81` |
| `Live` | `Short` | `100.25` | 118,960.00 USD | 211.53 USD | 0.00 USD | `+0.37%` | `2.11` |
| `Live` | `Short` | `100.55` | 142,180.00 USD | 23,220.00 USD | 0.00 USD | `+0.67%` | `230.92` |
| `Live` | `Short` | `101.45` | 143,130.00 USD | 953.63 USD | 0.00 USD | `+1.57%` | `9.40` |
| `Live` | `Short` | `101.55` | 143,600.00 USD | 468.15 USD | 0.00 USD | `+1.67%` | `4.61` |
| `Live` | `Short` | `101.65` | 144,020.00 USD | 416.76 USD | 0.00 USD | `+1.77%` | `4.10` |
| `Live` | `Short` | `101.85` | 144,230.00 USD | 211.85 USD | 0.00 USD | `+1.97%` | `2.08` |
| `Live` | `Short` | `102.25` | 144,730.00 USD | 505.11 USD | 0.00 USD | `+2.37%` | `4.94` |
| `Live` | `Short` | `102.45` | 161,620.00 USD | 16,890.00 USD | 0.00 USD | `+2.57%` | `164.87` |
| `Live` | `Short` | `102.55` | 164,930.00 USD | 3,300.00 USD | 0.00 USD | `+2.67%` | `32.19` |
| `Live` | `Short` | `102.65` | 169,230.00 USD | 4,300.00 USD | 0.00 USD | `+2.77%` | `41.92` |
| `Live` | `Short` | `102.75` | 238,240.00 USD | 69,020.00 USD | 0.00 USD | `+2.87%` | `671.69` |
| `Live` | `Short` | `102.85` | 324,840.00 USD | 86,600.00 USD | 0.00 USD | `+2.97%` | `841.98` |
| `Live` | `Short` | `102.95` | 327,710.00 USD | 2,870.00 USD | 0.00 USD | `+3.07%` | `27.90` |
| `Live` | `Short` | `103.05` | 350,560.00 USD | 22,850.00 USD | 0.00 USD | `+3.17%` | `221.69` |
| `Live` | `Short` | `103.15` | 352,310.00 USD | 1,750.00 USD | 0.00 USD | `+3.27%` | `17.00` |
| `Live` | `Short` | `103.25` | 353,780.00 USD | 1,470.00 USD | 0.00 USD | `+3.37%` | `14.24` |
| `Live` | `Short` | `103.35` | 354,480.00 USD | 691.41 USD | 0.00 USD | `+3.47%` | `6.69` |
| `Live` | `Short` | `103.55` | 363,280.00 USD | 8,800.00 USD | 0.00 USD | `+3.67%` | `85.01` |
| `Live` | `Short` | `103.75` | 367,270.00 USD | 3,990.00 USD | 0.00 USD | `+3.87%` | `38.47` |
| `Live` | `Short` | `103.85` | 396,190.00 USD | 28,920.00 USD | 0.00 USD | `+3.97%` | `278.46` |
| `Live` | `Short` | `103.95` | 406,250.00 USD | 10,060.00 USD | 0.00 USD | `+4.07%` | `96.78` |
| `Live` | `Short` | `104.05` | 407,830.00 USD | 1,590.00 USD | 0.00 USD | `+4.17%` | `15.25` |
| `Live` | `Short` | `104.15` | 410,160.00 USD | 2,330.00 USD | 0.00 USD | `+4.27%` | `22.36` |
| `Live` | `Short` | `104.25` | 410,490.00 USD | 325.26 USD | 0.00 USD | `+4.37%` | `3.12` |
| `Live` | `Short` | `104.35` | 412,500.00 USD | 2,010.00 USD | 0.00 USD | `+4.47%` | `19.30` |
| `Live` | `Short` | `104.45` | 424,640.00 USD | 12,140.00 USD | 0.00 USD | `+4.57%` | `116.19` |
| `Live` | `Short` | `104.55` | 428,890.00 USD | 4,250.00 USD | 0.00 USD | `+4.67%` | `40.68` |
| `Live` | `Short` | `104.65` | 1,060,000.00 USD | 631,520.00 USD | 0.00 USD | `+4.77%` | `6,034.63` |
| `Live` | `Short` | `104.75` | 1,120,000.00 USD | 59,710.00 USD | 0.00 USD | `+4.87%` | `570.06` |
| `Live` | `Short` | `104.85` | 1,140,000.00 USD | 16,470.00 USD | 0.00 USD | `+4.97%` | `157.07` |
| `Live` | `Short` | `104.95` | 1,140,000.00 USD | 1,030.00 USD | 0.00 USD | `+5.07%` | `9.79` |
| `Live` | `Short` | `105.05` | 1,150,000.00 USD | 16,290.00 USD | 0.00 USD | `+5.17%` | `155.06` |
| `Live` | `Short` | `105.15` | 1,160,000.00 USD | 4,320.00 USD | 0.00 USD | `+5.27%` | `41.12` |
| `Live` | `Short` | `105.25` | 1,170,000.00 USD | 7,300.00 USD | 0.00 USD | `+5.37%` | `69.36` |
| `Live` | `Short` | `105.45` | 1,170,000.00 USD | 8,610.00 USD | 0.00 USD | `+5.57%` | `81.61` |
| `Live` | `Short` | `105.55` | 1,180,000.00 USD | 4,180.00 USD | 0.00 USD | `+5.67%` | `39.61` |
| `Live` | `Short` | `105.75` | 1,180,000.00 USD | 1,460.00 USD | 0.00 USD | `+5.87%` | `13.83` |
| `Live` | `Short` | `105.95` | 1,180,000.00 USD | 2,020.00 USD | 0.00 USD | `+6.07%` | `19.03` |
| `Live` | `Short` | `106.05` | 1,190,000.00 USD | 4,790.00 USD | 0.00 USD | `+6.17%` | `45.14` |
| `Live` | `Short` | `106.45` | 1,200,000.00 USD | 10,970.00 USD | 0.00 USD | `+6.57%` | `103.05` |
| `Live` | `Short` | `106.85` | 1,200,000.00 USD | 771.46 USD | 0.00 USD | `+6.98%` | `7.22` |
| `Live` | `Short` | `106.95` | 1,200,000.00 USD | 543.31 USD | 0.00 USD | `+7.08%` | `5.08` |
| `Live` | `Short` | `107.05` | 1,210,000.00 USD | 12,960.00 USD | 0.00 USD | `+7.18%` | `121.06` |
| `Live` | `Short` | `107.15` | 1,250,000.00 USD | 35,700.00 USD | 0.00 USD | `+7.28%` | `333.15` |
| `Live` | `Short` | `107.25` | 1,250,000.00 USD | 2,690.00 USD | 0.00 USD | `+7.38%` | `25.10` |
| `Live` | `Short` | `107.35` | 1,460,000.00 USD | 212,780.00 USD | 0.00 USD | `+7.48%` | `1,982.14` |
| `Live` | `Short` | `107.45` | 1,520,000.00 USD | 55,230.00 USD | 0.00 USD | `+7.58%` | `514.03` |
| `Live` | `Short` | `107.55` | 1,520,000.00 USD | 3,570.00 USD | 0.00 USD | `+7.68%` | `33.15` |
| `Live` | `Short` | `107.65` | 1,520,000.00 USD | 1,770.00 USD | 0.00 USD | `+7.78%` | `16.48` |
| `Live` | `Short` | `107.75` | 1,530,000.00 USD | 5,840.00 USD | 0.00 USD | `+7.88%` | `54.18` |
| `Live` | `Short` | `107.85` | 1,530,000.00 USD | 1,480.00 USD | 0.00 USD | `+7.98%` | `13.72` |
| `Live` | `Short` | `108.05` | 1,530,000.00 USD | 1,080.00 USD | 0.00 USD | `+8.18%` | `10.04` |
| `Live` | `Short` | `108.15` | 1,530,000.00 USD | 863.04 USD | 0.00 USD | `+8.28%` | `7.98` |
| `Live` | `Short` | `108.25` | 1,530,000.00 USD | 546.66 USD | 0.00 USD | `+8.38%` | `5.05` |
| `Live` | `Short` | `108.35` | 1,540,000.00 USD | 4,430.00 USD | 0.00 USD | `+8.48%` | `40.88` |
| `Live` | `Short` | `108.45` | 1,660,000.00 USD | 121,890.00 USD | 0.00 USD | `+8.58%` | `1,123.94` |
| `Live` | `Short` | `108.55` | 1,660,000.00 USD | 117.23 USD | 0.00 USD | `+8.68%` | `1.08` |
| `Live` | `Short` | `108.65` | 1,720,000.00 USD | 64,720.00 USD | 0.00 USD | `+8.78%` | `595.69` |
| `Live` | `Short` | `108.75` | 1,730,000.00 USD | 9,470.00 USD | 0.00 USD | `+8.88%` | `87.09` |
| `Live` | `Short` | `108.85` | 1,730,000.00 USD | 333.08 USD | 0.00 USD | `+8.98%` | `3.06` |
| `Live` | `Short` | `108.95` | 1,740,000.00 USD | 2,620.00 USD | 0.00 USD | `+9.08%` | `24.06` |
| `Live` | `Short` | `109.15` | 1,780,000.00 USD | 44,720.00 USD | 0.00 USD | `+9.28%` | `409.75` |
| `Live` | `Short` | `109.25` | 1,780,000.00 USD | 1,170.00 USD | 0.00 USD | `+9.38%` | `10.74` |
| `Live` | `Short` | `109.35` | 1,790,000.00 USD | 7,560.00 USD | 0.00 USD | `+9.48%` | `69.13` |
| `Live` | `Short` | `109.45` | 1,890,000.00 USD | 103,840.00 USD | 0.00 USD | `+9.58%` | `948.78` |
| `Live` | `Short` | `109.55` | 1,890,000.00 USD | 106.26 USD | 0.00 USD | `+9.68%` | `0.97` |
| `Live` | `Short` | `109.65` | 1,950,000.00 USD | 53,730.00 USD | 0.00 USD | `+9.78%` | `490.05` |
| `Live` | `Short` | `109.75` | 1,950,000.00 USD | 231.57 USD | 0.00 USD | `+9.88%` | `2.11` |
| `Live` | `Short` | `109.85` | 1,950,000.00 USD | 848.04 USD | 0.00 USD | `+9.98%` | `7.72` |
| `Live` | `Short` | `109.95` | 1,950,000.00 USD | 1,590.00 USD | 0.00 USD | `+10.08%` | `14.45` |
| `Live` | `Short` | `110.05` | 1,950,000.00 USD | 2,910.00 USD | 0.00 USD | `+10.18%` | `26.47` |
| `Live` | `Short` | `110.15` | 1,950,000.00 USD | 194.97 USD | 0.00 USD | `+10.28%` | `1.77` |
| `Live` | `Short` | `110.25` | 1,950,000.00 USD | 324.13 USD | 0.00 USD | `+10.38%` | `2.94` |
| `Live` | `Short` | `110.35` | 2,100,000.00 USD | 148,440.00 USD | 0.00 USD | `+10.48%` | `1,345.14` |
| `Live` | `Short` | `110.45` | 2,120,000.00 USD | 16,940.00 USD | 0.00 USD | `+10.58%` | `153.41` |
| `Live` | `Short` | `110.55` | 2,120,000.00 USD | 203.41 USD | 0.00 USD | `+10.68%` | `1.84` |
| `Live` | `Short` | `110.65` | 2,120,000.00 USD | 219.09 USD | 0.00 USD | `+10.78%` | `1.98` |
| `Live` | `Short` | `110.75` | 2,130,000.00 USD | 7,600.00 USD | 0.00 USD | `+10.88%` | `68.66` |
| `Live` | `Short` | `110.85` | 2,130,000.00 USD | 103.09 USD | 0.00 USD | `+10.98%` | `0.93` |
| `Live` | `Short` | `110.95` | 2,140,000.00 USD | 15,300.00 USD | 0.00 USD | `+11.08%` | `137.93` |
| `Live` | `Short` | `111.05` | 2,150,000.00 USD | 6,860.00 USD | 0.00 USD | `+11.18%` | `61.80` |
| `Live` | `Short` | `111.15` | 2,150,000.00 USD | 1,710.00 USD | 0.00 USD | `+11.28%` | `15.37` |
| `Live` | `Short` | `111.35` | 4,500,000.00 USD | 2,350,000.00 USD | 0.00 USD | `+11.48%` | `21,120.10` |
| `Live` | `Short` | `111.45` | 4,500,000.00 USD | 841.45 USD | 0.00 USD | `+11.58%` | `7.55` |
| `Live` | `Short` | `111.55` | 4,500,000.00 USD | 311.22 USD | 0.00 USD | `+11.68%` | `2.79` |
| `Live` | `Short` | `111.75` | 4,620,000.00 USD | 114,530.00 USD | 0.00 USD | `+11.88%` | `1,024.87` |
| `Live` | `Short` | `111.85` | 4,640,000.00 USD | 17,210.00 USD | 0.00 USD | `+11.98%` | `153.88` |
| `Live` | `Short` | `111.95` | 4,640,000.00 USD | 1,460.00 USD | 0.00 USD | `+12.08%` | `13.00` |
| `Live` | `Short` | `112.05` | 4,640,000.00 USD | 216.26 USD | 0.00 USD | `+12.18%` | `1.93` |
| `Live` | `Short` | `112.25` | 4,640,000.00 USD | 1,370.00 USD | 0.00 USD | `+12.38%` | `12.22` |
| `Live` | `Short` | `112.55` | 4,640,000.00 USD | 844.13 USD | 0.00 USD | `+12.68%` | `7.50` |
| `Live` | `Short` | `112.75` | 4,640,000.00 USD | 110.50 USD | 0.00 USD | `+12.88%` | `0.98` |
| `Live` | `Short` | `113.05` | 4,740,000.00 USD | 103,600.00 USD | 0.00 USD | `+13.18%` | `916.44` |
| `Live` | `Short` | `113.15` | 4,750,000.00 USD | 10,200.00 USD | 0.00 USD | `+13.28%` | `90.17` |
| `Live` | `Short` | `113.25` | 4,750,000.00 USD | 114.38 USD | 0.00 USD | `+13.38%` | `1.01` |
| `Live` | `Short` | `113.55` | 4,760,000.00 USD | 10,470.00 USD | 0.00 USD | `+13.68%` | `92.17` |
| `Live` | `Short` | `113.65` | 4,770,000.00 USD | 3,220.00 USD | 0.00 USD | `+13.78%` | `28.37` |
| `Live` | `Short` | `113.75` | 4,770,000.00 USD | 2,130.00 USD | 0.00 USD | `+13.88%` | `18.69` |
| `Live` | `Short` | `113.85` | 4,780,000.00 USD | 14,390.00 USD | 0.00 USD | `+13.98%` | `126.38` |
| `Live` | `Short` | `113.95` | 4,810,000.00 USD | 21,840.00 USD | 0.00 USD | `+14.08%` | `191.69` |
| `Live` | `Short` | `114.05` | 4,830,000.00 USD | 23,300.00 USD | 0.00 USD | `+14.18%` | `204.29` |
| `Live` | `Short` | `114.15` | 4,830,000.00 USD | 1,960.00 USD | 0.00 USD | `+14.28%` | `17.21` |
| `Live` | `Short` | `114.25` | 4,830,000.00 USD | 2,150.00 USD | 0.00 USD | `+14.38%` | `18.80` |
| `Live` | `Short` | `114.45` | 4,840,000.00 USD | 9,310.00 USD | 0.00 USD | `+14.58%` | `81.32` |
| `Live` | `Short` | `114.85` | 4,890,000.00 USD | 51,610.00 USD | 0.00 USD | `+14.98%` | `449.38` |
| `Live` | `Short` | `114.95` | 4,910,000.00 USD | 15,310.00 USD | 0.00 USD | `+15.08%` | `133.16` |
| `Live` | `Short` | `115.05` | 5,480,000.00 USD | 569,550.00 USD | 0.00 USD | `+15.18%` | `4,950.49` |
| `Live` | `Short` | `115.15` | 6,360,000.00 USD | 877,850.00 USD | 0.00 USD | `+15.28%` | `7,623.52` |
| `Live` | `Short` | `115.25` | 6,380,000.00 USD | 18,240.00 USD | 0.00 USD | `+15.39%` | `158.28` |
| `Live` | `Short` | `115.35` | 6,780,000.00 USD | 408,270.00 USD | 0.00 USD | `+15.49%` | `3,539.42` |
| `Live` | `Short` | `115.55` | 6,830,000.00 USD | 46,710.00 USD | 0.00 USD | `+15.69%` | `404.24` |
| `Live` | `Short` | `115.75` | 6,830,000.00 USD | 160.89 USD | 0.00 USD | `+15.89%` | `1.39` |
| `Live` | `Short` | `115.85` | 6,830,000.00 USD | 289.62 USD | 0.00 USD | `+15.99%` | `2.50` |
| `Live` | `Short` | `116.05` | 6,840,000.00 USD | 4,450.00 USD | 0.00 USD | `+16.19%` | `38.34` |
| `Live` | `Short` | `116.15` | 6,860,000.00 USD | 22,160.00 USD | 0.00 USD | `+16.29%` | `190.76` |
| `Live` | `Short` | `116.25` | 6,860,000.00 USD | 5,870.00 USD | 0.00 USD | `+16.39%` | `50.46` |
| `Live` | `Short` | `116.35` | 6,950,000.00 USD | 90,140.00 USD | 0.00 USD | `+16.49%` | `774.73` |
| `Live` | `Short` | `116.55` | 6,960,000.00 USD | 2,040.00 USD | 0.00 USD | `+16.69%` | `17.52` |
| `Live` | `Short` | `116.65` | 6,960,000.00 USD | 555.25 USD | 0.00 USD | `+16.79%` | `4.76` |
| `Live` | `Short` | `116.75` | 6,990,000.00 USD | 31,980.00 USD | 0.00 USD | `+16.89%` | `273.89` |
| `Live` | `Short` | `116.85` | 7,250,000.00 USD | 261,600.00 USD | 0.00 USD | `+16.99%` | `2,238.73` |
| `Live` | `Short` | `117.05` | 11,770,000.00 USD | 4,520,000.00 USD | 0.00 USD | `+17.19%` | `38,587.61` |
| `Live` | `Short` | `117.15` | 11,820,000.00 USD | 51,230.00 USD | 0.00 USD | `+17.29%` | `437.30` |
| `Live` | `Short` | `117.25` | 11,820,000.00 USD | 157.12 USD | 0.00 USD | `+17.39%` | `1.34` |
| `Live` | `Short` | `117.45` | 11,820,000.00 USD | 128.02 USD | 0.00 USD | `+17.59%` | `1.09` |
| `Live` | `Short` | `117.75` | 11,820,000.00 USD | 2,720.00 USD | 0.00 USD | `+17.89%` | `23.07` |
| `Live` | `Short` | `117.85` | 11,820,000.00 USD | 584.54 USD | 0.00 USD | `+17.99%` | `4.96` |
| `Live` | `Short` | `117.95` | 11,830,000.00 USD | 12,060.00 USD | 0.00 USD | `+18.09%` | `102.22` |
| `Live` | `Short` | `118.45` | 11,870,000.00 USD | 32,620.00 USD | 0.00 USD | `+18.59%` | `275.43` |
| `Live` | `Short` | `118.55` | 11,870,000.00 USD | 1,110.00 USD | 0.00 USD | `+18.69%` | `9.38` |
| `Live` | `Short` | `118.75` | 11,870,000.00 USD | 309.94 USD | 0.00 USD | `+18.89%` | `2.61` |
| `Live` | `Short` | `118.95` | 11,870,000.00 USD | 1,780.00 USD | 0.00 USD | `+19.09%` | `15.00` |
| `Live` | `Short` | `119.15` | 11,870,000.00 USD | 3,520.00 USD | 0.00 USD | `+19.29%` | `29.52` |
| `Live` | `Short` | `119.25` | 11,930,000.00 USD | 58,110.00 USD | 0.00 USD | `+19.39%` | `487.29` |
| `Live` | `Short` | `119.45` | 11,930,000.00 USD | 115.87 USD | 0.00 USD | `+19.59%` | `0.97` |
| `Live` | `Short` | `119.55` | 11,930,000.00 USD | 1,070.00 USD | 0.00 USD | `+19.69%` | `8.96` |
| `Live` | `Short` | `119.65` | 12,020,000.00 USD | 90,800.00 USD | 0.00 USD | `+19.79%` | `758.90` |
| `Live` | `Short` | `119.75` | 12,020,000.00 USD | 374.82 USD | 0.00 USD | `+19.89%` | `3.13` |
| `Live` | `Short` | `119.95` | 12,200,000.00 USD | 178,050.00 USD | 0.00 USD | `+20.09%` | `1,484.34` |
| `Live` | `Short` | `120.15` | 12,210,000.00 USD | 4,930.00 USD | 0.00 USD | `+20.29%` | `41.00` |
| `Live` | `Short` | `120.35` | 12,210,000.00 USD | 145.62 USD | 0.00 USD | `+20.49%` | `1.21` |
| `Live` | `Short` | `120.55` | 12,210,000.00 USD | 2,520.00 USD | 0.00 USD | `+20.69%` | `20.94` |
| `Live` | `Short` | `120.95` | 12,240,000.00 USD | 28,790.00 USD | 0.00 USD | `+21.09%` | `238.04` |
| `Live` | `Short` | `121.25` | 12,240,000.00 USD | 414.68 USD | 0.00 USD | `+21.39%` | `3.42` |
| `Live` | `Short` | `121.45` | 12,280,000.00 USD | 45,000.00 USD | 0.00 USD | `+21.59%` | `370.50` |
| `Live` | `Short` | `121.55` | 12,290,000.00 USD | 5,940.00 USD | 0.00 USD | `+21.69%` | `48.87` |
| `Live` | `Short` | `121.65` | 12,310,000.00 USD | 16,300.00 USD | 0.00 USD | `+21.79%` | `133.95` |
| `Live` | `Short` | `121.75` | 12,330,000.00 USD | 19,900.00 USD | 0.00 USD | `+21.89%` | `163.43` |
| `Live` | `Short` | `122.05` | 12,380,000.00 USD | 56,710.00 USD | 0.00 USD | `+22.19%` | `464.61` |
| `Live` | `Short` | `122.15` | 12,380,000.00 USD | 169.79 USD | 0.00 USD | `+22.29%` | `1.39` |
| `Live` | `Short` | `122.25` | 12,380,000.00 USD | 2,200.00 USD | 0.00 USD | `+22.39%` | `17.99` |
| `Live` | `Short` | `122.45` | 12,400,000.00 USD | 20,160.00 USD | 0.00 USD | `+22.59%` | `164.61` |
| `Live` | `Short` | `122.65` | 12,400,000.00 USD | 116.52 USD | 0.00 USD | `+22.79%` | `0.95` |
| `Live` | `Short` | `122.95` | 12,410,000.00 USD | 2,790.00 USD | 0.00 USD | `+23.09%` | `22.66` |
| `Live` | `Short` | `123.25` | 12,410,000.00 USD | 483.14 USD | 0.00 USD | `+23.39%` | `3.92` |
| `Live` | `Short` | `123.35` | 12,410,000.00 USD | 2,330.00 USD | 0.00 USD | `+23.49%` | `18.92` |
| `Live` | `Short` | `123.45` | 12,410,000.00 USD | 2,520.00 USD | 0.00 USD | `+23.59%` | `20.44` |
| `Live` | `Short` | `123.55` | 12,420,000.00 USD | 3,430.00 USD | 0.00 USD | `+23.69%` | `27.73` |
| `Live` | `Short` | `124.05` | 12,420,000.00 USD | 586.76 USD | 0.00 USD | `+24.20%` | `4.73` |
| `Live` | `Short` | `124.15` | 12,430,000.00 USD | 11,520.00 USD | 0.00 USD | `+24.30%` | `92.78` |
| `Live` | `Short` | `124.25` | 12,450,000.00 USD | 17,600.00 USD | 0.00 USD | `+24.40%` | `141.62` |
| `Live` | `Short` | `124.45` | 12,450,000.00 USD | 3,080.00 USD | 0.00 USD | `+24.60%` | `24.76` |
| `Live` | `Short` | `124.55` | 13,100,000.00 USD | 649,140.00 USD | 0.00 USD | `+24.70%` | `5,211.89` |
| `Live` | `Short` | `124.65` | 13,100,000.00 USD | 675.60 USD | 0.00 USD | `+24.80%` | `5.42` |
| `Live` | `Short` | `124.75` | 13,110,000.00 USD | 7,200.00 USD | 0.00 USD | `+24.90%` | `57.71` |
| `Live` | `Short` | `124.95` | 13,120,000.00 USD | 14,160.00 USD | 0.00 USD | `+25.10%` | `113.36` |
| `Live` | `Short` | `125.35` | 13,130,000.00 USD | 6,470.00 USD | 0.00 USD | `+25.50%` | `51.58` |
| `Live` | `Short` | `125.65` | 13,130,000.00 USD | 487.52 USD | 0.00 USD | `+25.80%` | `3.88` |
| `Live` | `Short` | `125.75` | 13,130,000.00 USD | 1,930.00 USD | 0.00 USD | `+25.90%` | `15.31` |
| `Live` | `Short` | `125.85` | 13,130,000.00 USD | 6,200.00 USD | 0.00 USD | `+26.00%` | `49.29` |
| `Live` | `Short` | `125.95` | 13,140,000.00 USD | 110.84 USD | 0.00 USD | `+26.10%` | `0.88` |
| `Live` | `Short` | `126.05` | 13,140,000.00 USD | 810.50 USD | 0.00 USD | `+26.20%` | `6.43` |
| `Live` | `Short` | `126.15` | 26,060,000.00 USD | 12,930,000.00 USD | 0.00 USD | `+26.30%` | `102,478.61` |
| `Live` | `Short` | `126.35` | 26,060,000.00 USD | 305.77 USD | 0.00 USD | `+26.50%` | `2.42` |
| `Live` | `Short` | `126.45` | 26,080,000.00 USD | 11,380.00 USD | 0.00 USD | `+26.60%` | `90.00` |
| `Live` | `Short` | `126.65` | 26,110,000.00 USD | 31,220.00 USD | 0.00 USD | `+26.80%` | `246.51` |
| `Live` | `Short` | `126.85` | 26,110,000.00 USD | 1,710.00 USD | 0.00 USD | `+27.00%` | `13.48` |
| `Live` | `Short` | `126.95` | 26,120,000.00 USD | 9,460.00 USD | 0.00 USD | `+27.10%` | `74.51` |
| `Live` | `Short` | `127.05` | 26,120,000.00 USD | 2,030.00 USD | 0.00 USD | `+27.20%` | `16.01` |
| `Live` | `Short` | `127.25` | 26,120,000.00 USD | 2,480.00 USD | 0.00 USD | `+27.40%` | `19.52` |
| `Live` | `Short` | `127.35` | 26,140,000.00 USD | 16,190.00 USD | 0.00 USD | `+27.50%` | `127.13` |
| `Live` | `Short` | `127.65` | 26,830,000.00 USD | 694,870.00 USD | 0.00 USD | `+27.80%` | `5,443.55` |
| `Live` | `Short` | `127.85` | 26,880,000.00 USD | 44,240.00 USD | 0.00 USD | `+28.00%` | `346.03` |
| `Live` | `Short` | `127.95` | 26,890,000.00 USD | 10,510.00 USD | 0.00 USD | `+28.10%` | `82.13` |
| `Live` | `Short` | `128.05` | 27,000,000.00 USD | 116,200.00 USD | 0.00 USD | `+28.20%` | `907.49` |
| `Live` | `Short` | `128.35` | 27,000,000.00 USD | 195.09 USD | 0.00 USD | `+28.50%` | `1.52` |
| `Live` | `Short` | `128.45` | 27,870,000.00 USD | 863,880.00 USD | 0.00 USD | `+28.60%` | `6,725.38` |
| `Live` | `Short` | `128.65` | 32,470,000.00 USD | 4,600,000.00 USD | 0.00 USD | `+28.80%` | `35,787.14` |
| `Live` | `Short` | `128.75` | 32,490,000.00 USD | 18,730.00 USD | 0.00 USD | `+28.90%` | `145.45` |
| `Live` | `Short` | `128.85` | 32,530,000.00 USD | 43,250.00 USD | 0.00 USD | `+29.00%` | `335.67` |
| `Live` | `Short` | `129.25` | 32,570,000.00 USD | 32,480.00 USD | 0.00 USD | `+29.40%` | `251.27` |
| `Live` | `Short` | `129.35` | 32,570,000.00 USD | 888.63 USD | 0.00 USD | `+29.50%` | `6.87` |
| `Live` | `Short` | `129.45` | 32,570,000.00 USD | 2,990.00 USD | 0.00 USD | `+29.60%` | `23.12` |
| `Live` | `Short` | `129.55` | 32,640,000.00 USD | 65,100.00 USD | 0.00 USD | `+29.70%` | `502.50` |
| `Live` | `Short` | `129.75` | 32,670,000.00 USD | 38,040.00 USD | 0.00 USD | `+29.90%` | `293.19` |
| `Live` | `Short` | `129.85` | 37,600,000.00 USD | 4,930,000.00 USD | 0.00 USD | `+30.00%` | `37,961.58` |
| `Live` | `Short` | `130.25` | 37,650,000.00 USD | 46,990.00 USD | 0.00 USD | `+30.40%` | `360.76` |
| `Live` | `Short` | `130.35` | 37,650,000.00 USD | 1,040.00 USD | 0.00 USD | `+30.50%` | `8.00` |
| `Live` | `Short` | `130.55` | 37,660,000.00 USD | 4,970.00 USD | 0.00 USD | `+30.70%` | `38.04` |
| `Live` | `Short` | `130.65` | 38,730,000.00 USD | 1,080,000.00 USD | 0.00 USD | `+30.80%` | `8,241.07` |
| `Live` | `Short` | `130.85` | 39,240,000.00 USD | 504,660.00 USD | 0.00 USD | `+31.00%` | `3,856.76` |
| `Live` | `Short` | `130.95` | 39,240,000.00 USD | 2,070.00 USD | 0.00 USD | `+31.10%` | `15.84` |
| `Live` | `Short` | `131.05` | 39,240,000.00 USD | 188.71 USD | 0.00 USD | `+31.20%` | `1.44` |
| `Live` | `Short` | `131.25` | 39,240,000.00 USD | 1,560.00 USD | 0.00 USD | `+31.40%` | `11.87` |
| `Live` | `Short` | `131.45` | 39,240,000.00 USD | 715.09 USD | 0.00 USD | `+31.60%` | `5.44` |
| `Live` | `Short` | `131.55` | 39,240,000.00 USD | 171.02 USD | 0.00 USD | `+31.70%` | `1.30` |
| `Live` | `Short` | `131.85` | 39,250,000.00 USD | 5,820.00 USD | 0.00 USD | `+32.00%` | `44.14` |
| `Live` | `Short` | `132.15` | 39,250,000.00 USD | 325.09 USD | 0.00 USD | `+32.30%` | `2.46` |
| `Live` | `Short` | `132.25` | 39,300,000.00 USD | 47,650.00 USD | 0.00 USD | `+32.40%` | `360.32` |
| `Live` | `Short` | `132.35` | 39,300,000.00 USD | 5,320.00 USD | 0.00 USD | `+32.51%` | `40.23` |
| `Live` | `Short` | `132.45` | 39,310,000.00 USD | 8,530.00 USD | 0.00 USD | `+32.61%` | `64.37` |
| `Live` | `Short` | `132.55` | 39,310,000.00 USD | 196.17 USD | 0.00 USD | `+32.71%` | `1.48` |
| `Live` | `Short` | `132.65` | 39,310,000.00 USD | 240.10 USD | 0.00 USD | `+32.81%` | `1.81` |
| `Live` | `Short` | `132.85` | 39,360,000.00 USD | 49,280.00 USD | 0.00 USD | `+33.01%` | `370.98` |
| `Live` | `Short` | `133.05` | 39,370,000.00 USD | 5,730.00 USD | 0.00 USD | `+33.21%` | `43.05` |
| `Live` | `Short` | `133.15` | 39,370,000.00 USD | 9,170.00 USD | 0.00 USD | `+33.31%` | `68.89` |
| `Live` | `Short` | `133.55` | 39,370,000.00 USD | 186.97 USD | 0.00 USD | `+33.71%` | `1.40` |
| `Live` | `Short` | `133.65` | 39,380,000.00 USD | 8,400.00 USD | 0.00 USD | `+33.81%` | `62.84` |
| `Live` | `Short` | `133.75` | 39,530,000.00 USD | 151,500.00 USD | 0.00 USD | `+33.91%` | `1,132.73` |
| `Live` | `Short` | `133.95` | 39,530,000.00 USD | 503.65 USD | 0.00 USD | `+34.11%` | `3.76` |
| `Live` | `Short` | `134.05` | 39,540,000.00 USD | 142.09 USD | 0.00 USD | `+34.21%` | `1.06` |
| `Live` | `Short` | `134.25` | 39,630,000.00 USD | 92,140.00 USD | 0.00 USD | `+34.41%` | `686.32` |
| `Live` | `Short` | `134.85` | 39,650,000.00 USD | 18,510.00 USD | 0.00 USD | `+35.01%` | `137.24` |
| `Live` | `Short` | `135.15` | 40,180,000.00 USD | 532,900.00 USD | 0.00 USD | `+35.31%` | `3,943.04` |
| `Live` | `Short` | `135.25` | 40,180,000.00 USD | 1,560.00 USD | 0.00 USD | `+35.41%` | `11.52` |
| `Live` | `Short` | `135.35` | 40,180,000.00 USD | 246.34 USD | 0.00 USD | `+35.51%` | `1.82` |
| `Live` | `Short` | `135.45` | 40,180,000.00 USD | 746.33 USD | 0.00 USD | `+35.61%` | `5.51` |
| `Live` | `Short` | `135.85` | 40,180,000.00 USD | 3,250.00 USD | 0.00 USD | `+36.01%` | `23.94` |
| `Live` | `Short` | `135.95` | 40,180,000.00 USD | 504.37 USD | 0.00 USD | `+36.11%` | `3.71` |
| `Live` | `Short` | `136.15` | 40,230,000.00 USD | 48,850.00 USD | 0.00 USD | `+36.31%` | `358.80` |
| `Live` | `Short` | `136.45` | 40,230,000.00 USD | 608.57 USD | 0.00 USD | `+36.61%` | `4.46` |
| `Live` | `Short` | `136.55` | 40,230,000.00 USD | 136.55 USD | 0.00 USD | `+36.71%` | `1.00` |
| `Live` | `Short` | `136.65` | 40,240,000.00 USD | 7,940.00 USD | 0.00 USD | `+36.81%` | `58.14` |
| `Live` | `Short` | `136.85` | 40,380,000.00 USD | 133,160.00 USD | 0.00 USD | `+37.01%` | `973.04` |
| `Live` | `Short` | `137.05` | 40,380,000.00 USD | 1,640.00 USD | 0.00 USD | `+37.21%` | `12.00` |
| `Live` | `Short` | `137.55` | 40,380,000.00 USD | 1,650.00 USD | 0.00 USD | `+37.71%` | `12.02` |
| `Live` | `Short` | `137.75` | 40,380,000.00 USD | 212.13 USD | 0.00 USD | `+37.91%` | `1.54` |
| `Live` | `Short` | `138.05` | 40,380,000.00 USD | 1,270.00 USD | 0.00 USD | `+38.21%` | `9.20` |
| `Live` | `Short` | `138.15` | 40,500,000.00 USD | 115,290.00 USD | 0.00 USD | `+38.31%` | `834.51` |
| `Live` | `Short` | `138.35` | 40,510,000.00 USD | 18,980.00 USD | 0.00 USD | `+38.51%` | `137.20` |
| `Live` | `Short` | `138.45` | 40,650,000.00 USD | 132,700.00 USD | 0.00 USD | `+38.61%` | `958.49` |
| `Live` | `Short` | `138.75` | 42,730,000.00 USD | 2,080,000.00 USD | 0.00 USD | `+38.91%` | `15,001.76` |
| `Live` | `Short` | `138.95` | 42,730,000.00 USD | 459.92 USD | 0.00 USD | `+39.11%` | `3.31` |
| `Live` | `Short` | `139.15` | 42,730,000.00 USD | 552.43 USD | 0.00 USD | `+39.31%` | `3.97` |
| `Live` | `Short` | `139.25` | 42,800,000.00 USD | 66,520.00 USD | 0.00 USD | `+39.41%` | `477.67` |
| `Live` | `Short` | `139.65` | 42,820,000.00 USD | 22,260.00 USD | 0.00 USD | `+39.81%` | `159.43` |
| `Live` | `Short` | `139.85` | 43,880,000.00 USD | 1,060,000.00 USD | 0.00 USD | `+40.01%` | `7,609.58` |
| `Live` | `Short` | `140.05` | 43,880,000.00 USD | 116.24 USD | 0.00 USD | `+40.21%` | `0.83` |
| `Live` | `Short` | `140.45` | 43,890,000.00 USD | 4,870.00 USD | 0.00 USD | `+40.61%` | `34.66` |
| `Live` | `Short` | `140.55` | 43,900,000.00 USD | 7,330.00 USD | 0.00 USD | `+40.71%` | `52.16` |
| `Live` | `Short` | `140.75` | 44,110,000.00 USD | 210,790.00 USD | 0.00 USD | `+40.91%` | `1,497.60` |
| `Live` | `Short` | `140.95` | 44,110,000.00 USD | 1,940.00 USD | 0.00 USD | `+41.12%` | `13.73` |
| `Live` | `Short` | `141.05` | 44,110,000.00 USD | 125.53 USD | 0.00 USD | `+41.22%` | `0.89` |
| `Live` | `Short` | `141.15` | 44,110,000.00 USD | 927.36 USD | 0.00 USD | `+41.32%` | `6.57` |
| `Live` | `Short` | `141.35` | 44,110,000.00 USD | 210.61 USD | 0.00 USD | `+41.52%` | `1.49` |
| `Live` | `Short` | `141.45` | 44,360,000.00 USD | 247,540.00 USD | 0.00 USD | `+41.62%` | `1,750.00` |
| `Live` | `Short` | `141.55` | 44,360,000.00 USD | 236.39 USD | 0.00 USD | `+41.72%` | `1.67` |
| `Live` | `Short` | `141.65` | 44,360,000.00 USD | 2,140.00 USD | 0.00 USD | `+41.82%` | `15.11` |
| `Live` | `Short` | `141.75` | 44,360,000.00 USD | 239.56 USD | 0.00 USD | `+41.92%` | `1.69` |
| `Live` | `Short` | `142.15` | 44,440,000.00 USD | 80,180.00 USD | 0.00 USD | `+42.32%` | `564.06` |
| `Live` | `Short` | `142.45` | 44,440,000.00 USD | 151.00 USD | 0.00 USD | `+42.62%` | `1.06` |
| `Live` | `Short` | `142.75` | 44,440,000.00 USD | 847.93 USD | 0.00 USD | `+42.92%` | `5.94` |
| `Live` | `Short` | `143.25` | 44,460,000.00 USD | 15,400.00 USD | 0.00 USD | `+43.42%` | `107.50` |
| `Live` | `Short` | `143.35` | 44,480,000.00 USD | 22,260.00 USD | 0.00 USD | `+43.52%` | `155.27` |
| `Live` | `Short` | `143.55` | 44,620,000.00 USD | 143,550.00 USD | 0.00 USD | `+43.72%` | `1,000.00` |
| `Live` | `Short` | `143.75` | 44,620,000.00 USD | 1,340.00 USD | 0.00 USD | `+43.92%` | `9.31` |
| `Live` | `Short` | `143.85` | 44,650,000.00 USD | 29,340.00 USD | 0.00 USD | `+44.02%` | `203.98` |
| `Live` | `Short` | `144.05` | 44,660,000.00 USD | 3,750.00 USD | 0.00 USD | `+44.22%` | `26.00` |
| `Live` | `Short` | `144.25` | 44,660,000.00 USD | 7,270.00 USD | 0.00 USD | `+44.42%` | `50.42` |
| `Live` | `Short` | `144.35` | 44,660,000.00 USD | 114.04 USD | 0.00 USD | `+44.52%` | `0.79` |
| `Live` | `Short` | `144.45` | 44,740,000.00 USD | 78,000.00 USD | 0.00 USD | `+44.62%` | `539.99` |
| `Live` | `Short` | `144.65` | 44,740,000.00 USD | 2,330.00 USD | 0.00 USD | `+44.82%` | `16.10` |
| `Live` | `Short` | `144.95` | 44,750,000.00 USD | 2,090.00 USD | 0.00 USD | `+45.12%` | `14.41` |
| `Live` | `Short` | `145.15` | 44,750,000.00 USD | 1,760.00 USD | 0.00 USD | `+45.32%` | `12.12` |
| `Live` | `Short` | `145.35` | 44,750,000.00 USD | 5,340.00 USD | 0.00 USD | `+45.52%` | `36.73` |
| `Live` | `Short` | `145.65` | 45,610,000.00 USD | 857,010.00 USD | 0.00 USD | `+45.82%` | `5,884.06` |
| `Live` | `Short` | `145.85` | 45,620,000.00 USD | 5,850.00 USD | 0.00 USD | `+46.02%` | `40.09` |
| `Live` | `Short` | `145.95` | 45,620,000.00 USD | 820.24 USD | 0.00 USD | `+46.12%` | `5.62` |
| `Live` | `Short` | `146.15` | 45,710,000.00 USD | 88,760.00 USD | 0.00 USD | `+46.32%` | `607.33` |
| `Live` | `Short` | `146.25` | 45,710,000.00 USD | 2,770.00 USD | 0.00 USD | `+46.42%` | `18.95` |
| `Live` | `Short` | `146.35` | 45,720,000.00 USD | 7,330.00 USD | 0.00 USD | `+46.52%` | `50.10` |
| `Live` | `Short` | `146.55` | 45,720,000.00 USD | 2,690.00 USD | 0.00 USD | `+46.72%` | `18.37` |
| `Live` | `Short` | `146.65` | 46,310,000.00 USD | 587,730.00 USD | 0.00 USD | `+46.82%` | `4,007.68` |
| `Live` | `Short` | `146.75` | 46,310,000.00 USD | 1,880.00 USD | 0.00 USD | `+46.92%` | `12.80` |
| `Live` | `Short` | `146.95` | 46,310,000.00 USD | 3,070.00 USD | 0.00 USD | `+47.12%` | `20.88` |
| `Live` | `Short` | `147.05` | 46,310,000.00 USD | 166.17 USD | 0.00 USD | `+47.22%` | `1.13` |
| `Live` | `Short` | `147.15` | 46,310,000.00 USD | 1,730.00 USD | 0.00 USD | `+47.32%` | `11.75` |
| `Live` | `Short` | `147.35` | 46,320,000.00 USD | 5,770.00 USD | 0.00 USD | `+47.52%` | `39.15` |
| `Live` | `Short` | `147.45` | 46,320,000.00 USD | 204.96 USD | 0.00 USD | `+47.62%` | `1.39` |
| `Live` | `Short` | `147.55` | 46,410,000.00 USD | 94,970.00 USD | 0.00 USD | `+47.72%` | `643.67` |
| `Live` | `Short` | `147.65` | 46,410,000.00 USD | 558.12 USD | 0.00 USD | `+47.82%` | `3.78` |
| `Live` | `Short` | `147.85` | 46,410,000.00 USD | 300.14 USD | 0.00 USD | `+48.02%` | `2.03` |
| `Live` | `Short` | `148.15` | 47,790,000.00 USD | 1,380,000.00 USD | 0.00 USD | `+48.32%` | `9,288.19` |
| `Live` | `Short` | `148.35` | 48,240,000.00 USD | 445,050.00 USD | 0.00 USD | `+48.52%` | `3,000.00` |
| `Live` | `Short` | `148.45` | 48,240,000.00 USD | 163.29 USD | 0.00 USD | `+48.62%` | `1.10` |
| `Live` | `Short` | `148.55` | 48,580,000.00 USD | 344,780.00 USD | 0.00 USD | `+48.72%` | `2,321.00` |
| `Live` | `Short` | `148.65` | 48,580,000.00 USD | 709.06 USD | 0.00 USD | `+48.82%` | `4.77` |
| `Live` | `Short` | `148.75` | 48,670,000.00 USD | 91,450.00 USD | 0.00 USD | `+48.92%` | `614.80` |
| `Live` | `Short` | `148.95` | 48,670,000.00 USD | 1,460.00 USD | 0.00 USD | `+49.12%` | `9.81` |
| `Live` | `Short` | `149.15` | 48,670,000.00 USD | 343.04 USD | 0.00 USD | `+49.32%` | `2.30` |
| `Live` | `Short` | `149.45` | 48,680,000.00 USD | 1,490.00 USD | 0.00 USD | `+49.63%` | `10.00` |
| `Live` | `Short` | `149.55` | 48,680,000.00 USD | 116.65 USD | 0.00 USD | `+49.73%` | `0.78` |
| `Live` | `Short` | `149.65` | 48,690,000.00 USD | 16,900.00 USD | 0.00 USD | `+49.83%` | `112.95` |
| `Live` | `Short` | `149.75` | 48,690,000.00 USD | 724.79 USD | 0.00 USD | `+49.93%` | `4.84` |
| `Live` | `Short` | `149.85` | 48,730,000.00 USD | 37,240.00 USD | 0.00 USD | `+50.03%` | `248.53` |
| `Live` | `Short` | `149.95` | 48,730,000.00 USD | 178.44 USD | 0.00 USD | `+50.13%` | `1.19` |
| `Live` | `Short` | `150.05` | 48,730,000.00 USD | 2,930.00 USD | 0.00 USD | `+50.23%` | `19.54` |
| `Live` | `Short` | `150.25` | 48,760,000.00 USD | 29,740.00 USD | 0.00 USD | `+50.43%` | `197.92` |
| `Live` | `Short` | `150.65` | 48,770,000.00 USD | 2,910.00 USD | 0.00 USD | `+50.83%` | `19.33` |
| `Live` | `Short` | `151.15` | 48,770,000.00 USD | 2,770.00 USD | 0.00 USD | `+51.33%` | `18.34` |
| `Live` | `Short` | `151.25` | 48,860,000.00 USD | 86,240.00 USD | 0.00 USD | `+51.43%` | `570.19` |
| `Live` | `Short` | `151.45` | 48,860,000.00 USD | 8,830.00 USD | 0.00 USD | `+51.63%` | `58.32` |
| `Live` | `Short` | `151.65` | 48,870,000.00 USD | 409.46 USD | 0.00 USD | `+51.83%` | `2.70` |
| `Live` | `Short` | `151.75` | 48,870,000.00 USD | 2,280.00 USD | 0.00 USD | `+51.93%` | `15.05` |
| `Live` | `Short` | `151.85` | 48,870,000.00 USD | 6,670.00 USD | 0.00 USD | `+52.03%` | `43.91` |
| `Live` | `Short` | `151.95` | 48,880,000.00 USD | 1,920.00 USD | 0.00 USD | `+52.13%` | `12.64` |
| `Live` | `Short` | `152.15` | 48,880,000.00 USD | 200.84 USD | 0.00 USD | `+52.33%` | `1.32` |
| `Live` | `Short` | `152.25` | 49,180,000.00 USD | 304,500.00 USD | 0.00 USD | `+52.43%` | `2,000.00` |
| `Live` | `Short` | `152.35` | 49,570,000.00 USD | 384,300.00 USD | 0.00 USD | `+52.53%` | `2,522.49` |
| `Live` | `Short` | `152.45` | 49,570,000.00 USD | 3,150.00 USD | 0.00 USD | `+52.63%` | `20.65` |
| `Live` | `Short` | `152.55` | 50,150,000.00 USD | 585,740.00 USD | 0.00 USD | `+52.73%` | `3,839.64` |
| `Live` | `Short` | `152.75` | 50,160,000.00 USD | 1,570.00 USD | 0.00 USD | `+52.93%` | `10.30` |
| `Live` | `Short` | `153.05` | 50,390,000.00 USD | 230,640.00 USD | 0.00 USD | `+53.23%` | `1,506.95` |
| `Live` | `Short` | `153.35` | 50,390,000.00 USD | 2,300.00 USD | 0.00 USD | `+53.53%` | `15.00` |
| `Live` | `Short` | `153.65` | 50,440,000.00 USD | 51,450.00 USD | 0.00 USD | `+53.83%` | `334.86` |
| `Live` | `Short` | `153.75` | 50,440,000.00 USD | 1,270.00 USD | 0.00 USD | `+53.93%` | `8.29` |
| `Live` | `Short` | `153.85` | 50,480,000.00 USD | 43,120.00 USD | 0.00 USD | `+54.03%` | `280.29` |
| `Live` | `Short` | `154.05` | 50,490,000.00 USD | 5,930.00 USD | 0.00 USD | `+54.23%` | `38.50` |
| `Live` | `Short` | `154.25` | 50,490,000.00 USD | 2,340.00 USD | 0.00 USD | `+54.43%` | `15.20` |
| `Live` | `Short` | `154.45` | 50,500,000.00 USD | 4,240.00 USD | 0.00 USD | `+54.63%` | `27.45` |
| `Live` | `Short` | `154.55` | 50,500,000.00 USD | 363.19 USD | 0.00 USD | `+54.73%` | `2.35` |
| `Live` | `Short` | `155.15` | 55,320,000.00 USD | 4,820,000.00 USD | 0.00 USD | `+55.33%` | `31,095.84` |
| `Live` | `Short` | `155.55` | 55,330,000.00 USD | 8,050.00 USD | 0.00 USD | `+55.73%` | `51.72` |
| `Live` | `Short` | `156.25` | 55,370,000.00 USD | 39,850.00 USD | 0.00 USD | `+56.43%` | `255.07` |
| `Live` | `Short` | `156.35` | 55,370,000.00 USD | 3,320.00 USD | 0.00 USD | `+56.53%` | `21.26` |
| `Live` | `Short` | `156.45` | 56,740,000.00 USD | 1,370,000.00 USD | 0.00 USD | `+56.63%` | `8,752.28` |
| `Live` | `Short` | `156.95` | 57,880,000.00 USD | 1,140,000.00 USD | 0.00 USD | `+57.13%` | `7,259.71` |
| `Live` | `Short` | `157.15` | 57,950,000.00 USD | 66,400.00 USD | 0.00 USD | `+57.33%` | `422.50` |
| `Live` | `Short` | `157.25` | 57,950,000.00 USD | 190.27 USD | 0.00 USD | `+57.43%` | `1.21` |
| `Live` | `Short` | `157.45` | 57,950,000.00 USD | 1,880.00 USD | 0.00 USD | `+57.63%` | `11.95` |
| `Live` | `Short` | `157.55` | 57,980,000.00 USD | 30,560.00 USD | 0.00 USD | `+57.73%` | `194.00` |
| `Live` | `Short` | `157.65` | 57,980,000.00 USD | 2,390.00 USD | 0.00 USD | `+57.83%` | `15.15` |
| `Live` | `Short` | `157.75` | 58,080,000.00 USD | 93,830.00 USD | 0.00 USD | `+57.93%` | `594.80` |
| `Live` | `Short` | `157.95` | 58,390,000.00 USD | 315,900.00 USD | 0.00 USD | `+58.14%` | `2,000.00` |
| `Live` | `Short` | `158.15` | 58,390,000.00 USD | 120.19 USD | 0.00 USD | `+58.34%` | `0.76` |
| `Live` | `Short` | `158.35` | 58,480,000.00 USD | 88,130.00 USD | 0.00 USD | `+58.54%` | `556.55` |
| `Live` | `Short` | `158.75` | 58,490,000.00 USD | 13,730.00 USD | 0.00 USD | `+58.94%` | `86.48` |
| `Live` | `Short` | `158.85` | 58,500,000.00 USD | 794.25 USD | 0.00 USD | `+59.04%` | `5.00` |
| `Live` | `Short` | `158.95` | 58,520,000.00 USD | 26,450.00 USD | 0.00 USD | `+59.14%` | `166.39` |
| `Live` | `Short` | `159.05` | 58,570,000.00 USD | 44,690.00 USD | 0.00 USD | `+59.24%` | `281.00` |
| `Live` | `Short` | `159.15` | 58,820,000.00 USD | 249,820.00 USD | 0.00 USD | `+59.34%` | `1,569.69` |
| `Live` | `Short` | `159.25` | 58,840,000.00 USD | 27,920.00 USD | 0.00 USD | `+59.44%` | `175.30` |
| `Live` | `Short` | `159.65` | 58,850,000.00 USD | 2,080.00 USD | 0.00 USD | `+59.84%` | `13.01` |
| `Live` | `Short` | `159.95` | 58,850,000.00 USD | 6,100.00 USD | 0.00 USD | `+60.14%` | `38.15` |
| `Live` | `Short` | `160.15` | 59,540,000.00 USD | 683,000.00 USD | 0.00 USD | `+60.34%` | `4,264.75` |
| `Live` | `Short` | `160.25` | 59,570,000.00 USD | 32,970.00 USD | 0.00 USD | `+60.44%` | `205.77` |
| `Live` | `Short` | `160.35` | 59,690,000.00 USD | 118,850.00 USD | 0.00 USD | `+60.54%` | `741.18` |
| `Live` | `Short` | `160.85` | 59,690,000.00 USD | 318.48 USD | 0.00 USD | `+61.04%` | `1.98` |
| `Live` | `Short` | `161.05` | 59,690,000.00 USD | 2,240.00 USD | 0.00 USD | `+61.24%` | `13.93` |
| `Live` | `Short` | `161.35` | 59,690,000.00 USD | 2,160.00 USD | 0.00 USD | `+61.54%` | `13.37` |
| `Live` | `Short` | `161.55` | 59,730,000.00 USD | 41,510.00 USD | 0.00 USD | `+61.74%` | `256.95` |
| `Live` | `Short` | `161.65` | 59,730,000.00 USD | 119.62 USD | 0.00 USD | `+61.84%` | `0.74` |
| `Live` | `Short` | `161.85` | 59,880,000.00 USD | 142,330.00 USD | 0.00 USD | `+62.04%` | `879.39` |
| `Live` | `Short` | `161.95` | 60,020,000.00 USD | 145,330.00 USD | 0.00 USD | `+62.14%` | `897.35` |
| `Live` | `Short` | `162.05` | 60,020,000.00 USD | 304.65 USD | 0.00 USD | `+62.24%` | `1.88` |
| `Live` | `Short` | `162.45` | 60,020,000.00 USD | 2,270.00 USD | 0.00 USD | `+62.64%` | `14.00` |
| `Live` | `Short` | `162.55` | 60,020,000.00 USD | 650.20 USD | 0.00 USD | `+62.74%` | `4.00` |
| `Live` | `Short` | `163.45` | 60,030,000.00 USD | 8,110.00 USD | 0.00 USD | `+63.64%` | `49.61` |
| `Live` | `Short` | `163.65` | 60,050,000.00 USD | 21,930.00 USD | 0.00 USD | `+63.84%` | `134.01` |
| `Live` | `Short` | `163.75` | 60,060,000.00 USD | 1,310.00 USD | 0.00 USD | `+63.94%` | `8.00` |
| `Live` | `Short` | `163.85` | 60,060,000.00 USD | 5,140.00 USD | 0.00 USD | `+64.04%` | `31.39` |
| `Live` | `Short` | `164.75` | 60,270,000.00 USD | 207,840.00 USD | 0.00 USD | `+64.94%` | `1,261.56` |
| `Live` | `Short` | `164.85` | 60,270,000.00 USD | 1,680.00 USD | 0.00 USD | `+65.04%` | `10.17` |
| `Live` | `Short` | `165.15` | 60,270,000.00 USD | 198.18 USD | 0.00 USD | `+65.34%` | `1.20` |
| `Live` | `Short` | `165.45` | 60,420,000.00 USD | 144,260.00 USD | 0.00 USD | `+65.64%` | `871.95` |
| `Live` | `Short` | `165.85` | 96,980,000.00 USD | 36,560,000.00 USD | 0.00 USD | `+66.04%` | `220,440.19` |
| `Live` | `Short` | `166.25` | 97,170,000.00 USD | 190,590.00 USD | 0.00 USD | `+66.44%` | `1,146.40` |
| `Live` | `Short` | `166.35` | 97,170,000.00 USD | 1,230.00 USD | 0.00 USD | `+66.54%` | `7.37` |
| `Live` | `Short` | `167.25` | 97,170,000.00 USD | 319.45 USD | 0.00 USD | `+67.45%` | `1.91` |
| `Live` | `Short` | `167.35` | 97,190,000.00 USD | 19,220.00 USD | 0.00 USD | `+67.55%` | `114.86` |
| `Live` | `Short` | `167.45` | 103,140,000.00 USD | 5,950,000.00 USD | 0.00 USD | `+67.65%` | `35,529.12` |
| `Live` | `Short` | `167.65` | 103,140,000.00 USD | 115.68 USD | 0.00 USD | `+67.85%` | `0.69` |
| `Live` | `Short` | `167.75` | 103,140,000.00 USD | 1,890.00 USD | 0.00 USD | `+67.95%` | `11.27` |
| `Live` | `Short` | `167.85` | 103,140,000.00 USD | 3,460.00 USD | 0.00 USD | `+68.05%` | `20.63` |
| `Live` | `Short` | `167.95` | 103,140,000.00 USD | 2,780.00 USD | 0.00 USD | `+68.15%` | `16.57` |
| `Live` | `Short` | `168.35` | 103,160,000.00 USD | 19,740.00 USD | 0.00 USD | `+68.55%` | `117.24` |
| `Live` | `Short` | `168.45` | 104,280,000.00 USD | 1,110,000.00 USD | 0.00 USD | `+68.65%` | `6,615.62` |
| `Live` | `Short` | `168.65` | 104,600,000.00 USD | 325,850.00 USD | 0.00 USD | `+68.85%` | `1,932.10` |
| `Live` | `Short` | `169.95` | 104,710,000.00 USD | 101,970.00 USD | 0.00 USD | `+70.15%` | `600.00` |
| `Live` | `Short` | `171.45` | 104,710,000.00 USD | 111.44 USD | 0.00 USD | `+71.65%` | `0.65` |
| `Live` | `Short` | `171.75` | 104,710,000.00 USD | 3,320.00 USD | 0.00 USD | `+71.95%` | `19.33` |
| `Live` | `Short` | `171.95` | 104,710,000.00 USD | 398.92 USD | 0.00 USD | `+72.15%` | `2.32` |
| `Live` | `Short` | `172.45` | 104,760,000.00 USD | 51,970.00 USD | 0.00 USD | `+72.65%` | `301.36` |
| `Live` | `Short` | `172.85` | 104,770,000.00 USD | 10,200.00 USD | 0.00 USD | `+73.05%` | `59.00` |
| `Live` | `Short` | `173.45` | 104,790,000.00 USD | 16,540.00 USD | 0.00 USD | `+73.65%` | `95.36` |
| `Live` | `Short` | `173.85` | 104,790,000.00 USD | 695.40 USD | 0.00 USD | `+74.05%` | `4.00` |
| `Live` | `Short` | `174.05` | 104,890,000.00 USD | 104,430.00 USD | 0.00 USD | `+74.25%` | `600.00` |
| `Live` | `Short` | `174.25` | 105,140,000.00 USD | 245,010.00 USD | 0.00 USD | `+74.45%` | `1,406.07` |
| `Live` | `Short` | `174.35` | 105,340,000.00 USD | 205,490.00 USD | 0.00 USD | `+74.55%` | `1,178.60` |
| `Live` | `Short` | `174.55` | 105,350,000.00 USD | 1,650.00 USD | 0.00 USD | `+74.75%` | `9.45` |
| `Live` | `Short` | `174.75` | 105,350,000.00 USD | 146.79 USD | 0.00 USD | `+74.95%` | `0.84` |
| `Live` | `Short` | `175.05` | 105,350,000.00 USD | 175.05 USD | 0.00 USD | `+75.26%` | `1.00` |
| `Live` | `Short` | `175.15` | 105,350,000.00 USD | 1,320.00 USD | 0.00 USD | `+75.36%` | `7.52` |
| `Live` | `Short` | `175.35` | 105,350,000.00 USD | 119.24 USD | 0.00 USD | `+75.56%` | `0.68` |
| `Live` | `Short` | `175.55` | 105,350,000.00 USD | 158.00 USD | 0.00 USD | `+75.76%` | `0.90` |
| `Live` | `Short` | `175.75` | 105,350,000.00 USD | 263.62 USD | 0.00 USD | `+75.96%` | `1.50` |
| `Live` | `Short` | `176.05` | 105,370,000.00 USD | 24,820.00 USD | 0.00 USD | `+76.26%` | `140.96` |
| `Live` | `Short` | `176.25` | 105,370,000.00 USD | 625.69 USD | 0.00 USD | `+76.46%` | `3.55` |
| `Live` | `Short` | `176.45` | 105,370,000.00 USD | 520.53 USD | 0.00 USD | `+76.66%` | `2.95` |
| `Live` | `Short` | `176.55` | 105,380,000.00 USD | 3,530.00 USD | 0.00 USD | `+76.76%` | `20.00` |
| `Live` | `Short` | `176.65` | 105,380,000.00 USD | 2,070.00 USD | 0.00 USD | `+76.86%` | `11.72` |
| `Live` | `Short` | `177.95` | 105,460,000.00 USD | 80,850.00 USD | 0.00 USD | `+78.16%` | `454.35` |
| `Live` | `Short` | `178.25` | 105,460,000.00 USD | 1,610.00 USD | 0.00 USD | `+78.46%` | `9.06` |
| `Live` | `Short` | `178.35` | 105,470,000.00 USD | 3,130.00 USD | 0.00 USD | `+78.56%` | `17.54` |
| `Live` | `Short` | `178.85` | 105,470,000.00 USD | 132.35 USD | 0.00 USD | `+79.06%` | `0.74` |
| `Live` | `Short` | `179.05` | 108,440,000.00 USD | 2,970,000.00 USD | 0.00 USD | `+79.26%` | `16,603.11` |
| `Live` | `Short` | `179.15` | 108,440,000.00 USD | 2,110.00 USD | 0.00 USD | `+79.36%` | `11.80` |
| `Live` | `Short` | `179.35` | 108,440,000.00 USD | 473.48 USD | 0.00 USD | `+79.56%` | `2.64` |
| `Live` | `Short` | `179.95` | 108,460,000.00 USD | 15,590.00 USD | 0.00 USD | `+80.16%` | `86.63` |
| `Live` | `Short` | `180.05` | 108,460,000.00 USD | 2,360.00 USD | 0.00 USD | `+80.26%` | `13.10` |
| `Live` | `Short` | `180.35` | 108,470,000.00 USD | 7,470.00 USD | 0.00 USD | `+80.56%` | `41.43` |
| `Live` | `Short` | `180.55` | 108,470,000.00 USD | 3,970.00 USD | 0.00 USD | `+80.76%` | `22.01` |
| `Live` | `Short` | `180.95` | 108,470,000.00 USD | 334.76 USD | 0.00 USD | `+81.16%` | `1.85` |
| `Live` | `Short` | `181.55` | 108,470,000.00 USD | 254.17 USD | 0.00 USD | `+81.76%` | `1.40` |
| `Live` | `Short` | `181.65` | 108,480,000.00 USD | 5,150.00 USD | 0.00 USD | `+81.86%` | `28.34` |
| `Live` | `Short` | `182.05` | 108,480,000.00 USD | 964.87 USD | 0.00 USD | `+82.26%` | `5.30` |
| `Live` | `Short` | `182.15` | 108,480,000.00 USD | 3,990.00 USD | 0.00 USD | `+82.36%` | `21.93` |
| `Live` | `Short` | `182.25` | 108,770,000.00 USD | 291,600.00 USD | 0.00 USD | `+82.46%` | `1,600.00` |
| `Live` | `Short` | `182.55` | 108,780,000.00 USD | 5,110.00 USD | 0.00 USD | `+82.76%` | `28.00` |
| `Live` | `Short` | `182.85` | 108,780,000.00 USD | 618.03 USD | 0.00 USD | `+83.06%` | `3.38` |
| `Live` | `Short` | `183.15` | 108,780,000.00 USD | 1,310.00 USD | 0.00 USD | `+83.36%` | `7.13` |
| `Live` | `Short` | `183.35` | 108,780,000.00 USD | 5,500.00 USD | 0.00 USD | `+83.56%` | `30.00` |
| `Live` | `Short` | `184.55` | 109,150,000.00 USD | 369,100.00 USD | 0.00 USD | `+84.77%` | `2,000.00` |
| `Live` | `Short` | `184.95` | 109,320,000.00 USD | 165,440.00 USD | 0.00 USD | `+85.17%` | `894.52` |
| `Live` | `Short` | `185.15` | 109,320,000.00 USD | 3,690.00 USD | 0.00 USD | `+85.37%` | `19.95` |
| `Live` | `Short` | `185.25` | 109,320,000.00 USD | 737.29 USD | 0.00 USD | `+85.47%` | `3.98` |
| `Live` | `Short` | `185.45` | 109,330,000.00 USD | 2,770.00 USD | 0.00 USD | `+85.67%` | `14.94` |
| `Live` | `Short` | `185.65` | 109,330,000.00 USD | 137.38 USD | 0.00 USD | `+85.87%` | `0.74` |
| `Live` | `Short` | `185.75` | 109,350,000.00 USD | 19,050.00 USD | 0.00 USD | `+85.97%` | `102.58` |
| `Live` | `Short` | `186.35` | 109,530,000.00 USD | 181,490.00 USD | 0.00 USD | `+86.57%` | `973.91` |
| `Live` | `Short` | `186.45` | 109,530,000.00 USD | 231.20 USD | 0.00 USD | `+86.67%` | `1.24` |
| `Live` | `Short` | `186.75` | 109,530,000.00 USD | 115.78 USD | 0.00 USD | `+86.97%` | `0.62` |
| `Live` | `Short` | `187.45` | 109,530,000.00 USD | 2,110.00 USD | 0.00 USD | `+87.67%` | `11.24` |
| `Live` | `Short` | `187.95` | 109,570,000.00 USD | 39,010.00 USD | 0.00 USD | `+88.17%` | `207.53` |
| `Live` | `Short` | `188.25` | 109,590,000.00 USD | 19,000.00 USD | 0.00 USD | `+88.47%` | `100.93` |
| `Live` | `Short` | `188.35` | 109,610,000.00 USD | 19,090.00 USD | 0.00 USD | `+88.57%` | `101.38` |
| `Live` | `Short` | `188.55` | 109,610,000.00 USD | 231.92 USD | 0.00 USD | `+88.77%` | `1.23` |
| `Live` | `Short` | `188.95` | 109,610,000.00 USD | 1,450.00 USD | 0.00 USD | `+89.17%` | `7.69` |
| `Live` | `Short` | `189.05` | 109,750,000.00 USD | 137,350.00 USD | 0.00 USD | `+89.27%` | `726.51` |
| `Live` | `Short` | `189.25` | 109,810,000.00 USD | 64,800.00 USD | 0.00 USD | `+89.47%` | `342.41` |
| `Live` | `Short` | `189.95` | 110,100,000.00 USD | 284,930.00 USD | 0.00 USD | `+90.17%` | `1,500.00` |
| `Live` | `Short` | `190.05` | 110,880,000.00 USD | 788,710.00 USD | 0.00 USD | `+90.27%` | `4,150.00` |
| `Live` | `Short` | `190.15` | 111,170,000.00 USD | 286,480.00 USD | 0.00 USD | `+90.37%` | `1,506.60` |
| `Live` | `Short` | `190.65` | 111,230,000.00 USD | 57,200.00 USD | 0.00 USD | `+90.87%` | `300.00` |
| `Live` | `Short` | `190.85` | 111,230,000.00 USD | 534.38 USD | 0.00 USD | `+91.07%` | `2.80` |
| `Live` | `Short` | `190.95` | 124,790,000.00 USD | 13,570,000.00 USD | 0.00 USD | `+91.17%` | `71,044.42` |
| `Live` | `Short` | `191.95` | 124,790,000.00 USD | 322.48 USD | 0.00 USD | `+92.17%` | `1.68` |
| `Live` | `Short` | `192.25` | 124,800,000.00 USD | 336.44 USD | 0.00 USD | `+92.48%` | `1.75` |
| `Live` | `Short` | `192.75` | 124,880,000.00 USD | 88,240.00 USD | 0.00 USD | `+92.98%` | `457.80` |
| `Live` | `Short` | `193.05` | 124,890,000.00 USD | 7,410.00 USD | 0.00 USD | `+93.28%` | `38.40` |
| `Live` | `Short` | `193.15` | 124,890,000.00 USD | 1,190.00 USD | 0.00 USD | `+93.38%` | `6.16` |
| `Live` | `Short` | `193.45` | 124,900,000.00 USD | 12,910.00 USD | 0.00 USD | `+93.68%` | `66.76` |
| `Live` | `Short` | `193.55` | 125,020,000.00 USD | 114,580.00 USD | 0.00 USD | `+93.78%` | `592.00` |
| `Live` | `Short` | `193.65` | 125,020,000.00 USD | 4,750.00 USD | 0.00 USD | `+93.88%` | `24.54` |
| `Live` | `Short` | `193.85` | 125,040,000.00 USD | 15,590.00 USD | 0.00 USD | `+94.08%` | `80.44` |
| `Live` | `Short` | `194.25` | 125,040,000.00 USD | 3,710.00 USD | 0.00 USD | `+94.48%` | `19.12` |
| `Live` | `Short` | `194.55` | 125,050,000.00 USD | 8,670.00 USD | 0.00 USD | `+94.78%` | `44.54` |
| `Live` | `Short` | `194.65` | 125,190,000.00 USD | 136,260.00 USD | 0.00 USD | `+94.88%` | `700.00` |
| `Live` | `Short` | `194.75` | 125,190,000.00 USD | 266.81 USD | 0.00 USD | `+94.98%` | `1.37` |
| `Live` | `Short` | `195.05` | 125,200,000.00 USD | 9,500.00 USD | 0.00 USD | `+95.28%` | `48.71` |
| `Live` | `Short` | `195.25` | 125,210,000.00 USD | 13,690.00 USD | 0.00 USD | `+95.48%` | `70.12` |
| `Live` | `Short` | `195.35` | 125,260,000.00 USD | 48,840.00 USD | 0.00 USD | `+95.58%` | `250.00` |
| `Live` | `Short` | `195.75` | 125,270,000.00 USD | 9,790.00 USD | 0.00 USD | `+95.98%` | `50.00` |
| `Live` | `Short` | `196.05` | 125,270,000.00 USD | 4,080.00 USD | 0.00 USD | `+96.28%` | `20.81` |
| `Live` | `Short` | `196.15` | 125,280,000.00 USD | 415.84 USD | 0.00 USD | `+96.38%` | `2.12` |
| `Live` | `Short` | `196.25` | 125,280,000.00 USD | 3,470.00 USD | 0.00 USD | `+96.48%` | `17.68` |
| `Live` | `Short` | `196.45` | 125,280,000.00 USD | 4,350.00 USD | 0.00 USD | `+96.68%` | `22.16` |
| `Live` | `Short` | `196.75` | 125,280,000.00 USD | 127.89 USD | 0.00 USD | `+96.98%` | `0.65` |
| `Live` | `Short` | `196.95` | 125,290,000.00 USD | 2,000.00 USD | 0.00 USD | `+97.18%` | `10.17` |
| `Live` | `Short` | `197.15` | 125,290,000.00 USD | 193.21 USD | 0.00 USD | `+97.38%` | `0.98` |
| `Live` | `Short` | `197.35` | 125,290,000.00 USD | 6,310.00 USD | 0.00 USD | `+97.58%` | `31.95` |
| `Live` | `Short` | `197.65` | 125,580,000.00 USD | 292,380.00 USD | 0.00 USD | `+97.88%` | `1,479.30` |
| `Live` | `Short` | `198.05` | 125,590,000.00 USD | 1,580.00 USD | 0.00 USD | `+98.28%` | `7.99` |
| `Live` | `Short` | `198.15` | 125,810,000.00 USD | 223,280.00 USD | 0.00 USD | `+98.38%` | `1,126.81` |
| `Live` | `Short` | `198.25` | 125,820,000.00 USD | 12,030.00 USD | 0.00 USD | `+98.48%` | `60.68` |
| `Live` | `Short` | `198.35` | 125,820,000.00 USD | 396.70 USD | 0.00 USD | `+98.58%` | `2.00` |
| `Live` | `Short` | `198.45` | 125,840,000.00 USD | 16,790.00 USD | 0.00 USD | `+98.68%` | `84.60` |
| `Live` | `Short` | `198.55` | 125,840,000.00 USD | 1,950.00 USD | 0.00 USD | `+98.78%` | `9.83` |
| `Live` | `Short` | `198.85` | 125,920,000.00 USD | 78,030.00 USD | 0.00 USD | `+99.08%` | `392.40` |
| `Live` | `Short` | `199.05` | 125,920,000.00 USD | 1,520.00 USD | 0.00 USD | `+99.28%` | `7.65` |
| `Live` | `Short` | `199.15` | 125,920,000.00 USD | 2,550.00 USD | 0.00 USD | `+99.38%` | `12.80` |
| `Live` | `Short` | `199.35` | 125,920,000.00 USD | 139.55 USD | 0.00 USD | `+99.58%` | `0.70` |
| `Live` | `Short` | `199.55` | 125,930,000.00 USD | 8,130.00 USD | 0.00 USD | `+99.78%` | `40.72` |
| `Live` | `Short` | `199.65` | 125,940,000.00 USD | 8,020.00 USD | 0.00 USD | `+99.88%` | `40.15` |
| `Live` | `Short` | `199.75` | 125,970,000.00 USD | 27,860.00 USD | 0.00 USD | `+99.98%` | `139.45` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `23.05` | 10,430,000.00 USD | 0.00 USD | 14,770.00 USD | `-76.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.05` | 10,410,000.00 USD | 0.00 USD | 3,760.00 USD | `-74.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `26.15` | 10,410,000.00 USD | 0.00 USD | 103.82 USD | `-73.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `30.05` | 10,410,000.00 USD | 0.00 USD | 519.56 USD | `-69.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `30.35` | 10,410,000.00 USD | 0.00 USD | 499.56 USD | `-69.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `33.05` | 10,410,000.00 USD | 0.00 USD | 818.32 USD | `-66.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `34.85` | 10,410,000.00 USD | 0.00 USD | 1,340.00 USD | `-65.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.85` | 10,400,000.00 USD | 0.00 USD | 201.74 USD | `-62.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `38.65` | 10,400,000.00 USD | 0.00 USD | 206.00 USD | `-61.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.05` | 10,400,000.00 USD | 0.00 USD | 208.14 USD | `-60.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.55` | 10,400,000.00 USD | 0.00 USD | 3,460.00 USD | `-60.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.75` | 10,400,000.00 USD | 0.00 USD | 157.01 USD | `-60.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.05` | 10,400,000.00 USD | 0.00 USD | 418.92 USD | `-59.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.55` | 10,400,000.00 USD | 0.00 USD | 170,530.00 USD | `-57.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.75` | 10,230,000.00 USD | 0.00 USD | 105.00 USD | `-56.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.05` | 10,230,000.00 USD | 0.00 USD | 63,450.00 USD | `-54.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.75` | 10,170,000.00 USD | 0.00 USD | 251.05 USD | `-53.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.75` | 10,170,000.00 USD | 0.00 USD | 143.25 USD | `-52.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.85` | 10,170,000.00 USD | 0.00 USD | 191.40 USD | `-52.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.75` | 10,170,000.00 USD | 0.00 USD | 103.35 USD | `-51.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.05` | 10,170,000.00 USD | 0.00 USD | 5,250.00 USD | `-49.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.25` | 10,160,000.00 USD | 0.00 USD | 107.03 USD | `-49.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.55` | 10,160,000.00 USD | 0.00 USD | 102.62 USD | `-49.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.25` | 10,160,000.00 USD | 0.00 USD | 134.28 USD | `-48.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.65` | 10,160,000.00 USD | 0.00 USD | 3,950.00 USD | `-48.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.15` | 10,160,000.00 USD | 0.00 USD | 102.74 USD | `-47.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.55` | 10,160,000.00 USD | 0.00 USD | 126.12 USD | `-47.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.95` | 10,160,000.00 USD | 0.00 USD | 200.15 USD | `-46.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.15` | 10,160,000.00 USD | 0.00 USD | 24,450.00 USD | `-46.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.45` | 10,130,000.00 USD | 0.00 USD | 2,240.00 USD | `-46.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.05` | 10,130,000.00 USD | 0.00 USD | 641.57 USD | `-45.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.85` | 10,130,000.00 USD | 0.00 USD | 139.87 USD | `-45.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.05` | 10,130,000.00 USD | 0.00 USD | 209.19 USD | `-44.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.05` | 10,130,000.00 USD | 0.00 USD | 894.56 USD | `-43.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.15` | 10,130,000.00 USD | 0.00 USD | 4,930.00 USD | `-43.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.05` | 10,120,000.00 USD | 0.00 USD | 6,500.00 USD | `-42.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `58.05` | 10,120,000.00 USD | 0.00 USD | 158.48 USD | `-41.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.05` | 10,120,000.00 USD | 0.00 USD | 236.20 USD | `-40.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.35` | 10,110,000.00 USD | 0.00 USD | 200.01 USD | `-40.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.55` | 10,110,000.00 USD | 0.00 USD | 1,460.00 USD | `-40.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.95` | 10,110,000.00 USD | 0.00 USD | 9,040.00 USD | `-39.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.05` | 10,100,000.00 USD | 0.00 USD | 32,980.00 USD | `-39.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.25` | 10,070,000.00 USD | 0.00 USD | 488.63 USD | `-39.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.35` | 10,070,000.00 USD | 0.00 USD | 258.90 USD | `-39.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.45` | 10,070,000.00 USD | 0.00 USD | 6,200.00 USD | `-39.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.55` | 10,060,000.00 USD | 0.00 USD | 551.61 USD | `-39.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.05` | 10,060,000.00 USD | 0.00 USD | 18,360.00 USD | `-38.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.35` | 10,050,000.00 USD | 0.00 USD | 142.33 USD | `-38.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.45` | 10,050,000.00 USD | 0.00 USD | 100.78 USD | `-38.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.55` | 10,050,000.00 USD | 0.00 USD | 243.74 USD | `-38.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `62.05` | 10,040,000.00 USD | 0.00 USD | 4,640.00 USD | `-37.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `62.55` | 10,040,000.00 USD | 0.00 USD | 136.98 USD | `-37.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `63.05` | 10,040,000.00 USD | 0.00 USD | 12,950.00 USD | `-36.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `63.55` | 10,030,000.00 USD | 0.00 USD | 2,980.00 USD | `-36.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `63.95` | 10,020,000.00 USD | 0.00 USD | 222.55 USD | `-35.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `64.25` | 10,020,000.00 USD | 0.00 USD | 163.19 USD | `-35.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `64.85` | 10,020,000.00 USD | 0.00 USD | 129.70 USD | `-35.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `65.05` | 10,020,000.00 USD | 0.00 USD | 2,440.00 USD | `-34.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `65.15` | 10,020,000.00 USD | 0.00 USD | 2,190.00 USD | `-34.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `65.55` | 10,020,000.00 USD | 0.00 USD | 2,200.00 USD | `-34.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `66.05` | 10,020,000.00 USD | 0.00 USD | 7,100.00 USD | `-33.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `66.55` | 10,010,000.00 USD | 0.00 USD | 541.72 USD | `-33.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `67.05` | 10,010,000.00 USD | 0.00 USD | 335.25 USD | `-32.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `67.15` | 10,010,000.00 USD | 0.00 USD | 268.60 USD | `-32.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `67.85` | 10,010,000.00 USD | 0.00 USD | 303.29 USD | `-32.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.05` | 10,010,000.00 USD | 0.00 USD | 195.30 USD | `-31.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.55` | 10,010,000.00 USD | 0.00 USD | 5,610.00 USD | `-31.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.65` | 10,000,000.00 USD | 0.00 USD | 359.04 USD | `-31.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.75` | 10,000,000.00 USD | 0.00 USD | 1,200.00 USD | `-31.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.05` | 10,000,000.00 USD | 0.00 USD | 20,210.00 USD | `-30.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.15` | 9,980,000.00 USD | 0.00 USD | 172.18 USD | `-30.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.25` | 9,980,000.00 USD | 0.00 USD | 668.96 USD | `-30.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.65` | 9,980,000.00 USD | 0.00 USD | 107.96 USD | `-30.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.75` | 9,980,000.00 USD | 0.00 USD | 42,360.00 USD | `-30.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.85` | 9,940,000.00 USD | 0.00 USD | 365.32 USD | `-30.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.05` | 9,940,000.00 USD | 0.00 USD | 36,240.00 USD | `-29.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.25` | 9,900,000.00 USD | 0.00 USD | 5,270.00 USD | `-29.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.35` | 9,900,000.00 USD | 0.00 USD | 562.80 USD | `-29.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.55` | 9,900,000.00 USD | 0.00 USD | 681.51 USD | `-29.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.65` | 9,890,000.00 USD | 0.00 USD | 4,920.00 USD | `-29.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.75` | 9,890,000.00 USD | 0.00 USD | 2,790.00 USD | `-29.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.05` | 9,890,000.00 USD | 0.00 USD | 265.02 USD | `-28.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.45` | 9,890,000.00 USD | 0.00 USD | 289.37 USD | `-28.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.55` | 9,890,000.00 USD | 0.00 USD | 1,170.00 USD | `-28.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.65` | 9,880,000.00 USD | 0.00 USD | 913.54 USD | `-28.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.05` | 9,880,000.00 USD | 0.00 USD | 67,420.00 USD | `-27.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.55` | 9,820,000.00 USD | 0.00 USD | 19,560.00 USD | `-27.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.95` | 9,800,000.00 USD | 0.00 USD | 66,160.00 USD | `-26.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `73.45` | 9,730,000.00 USD | 0.00 USD | 139.56 USD | `-26.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.05` | 9,730,000.00 USD | 0.00 USD | 11,420.00 USD | `-25.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.35` | 9,720,000.00 USD | 0.00 USD | 1,660.00 USD | `-25.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.45` | 9,720,000.00 USD | 0.00 USD | 10,730.00 USD | `-25.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.55` | 9,710,000.00 USD | 0.00 USD | 331.00 USD | `-25.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.75` | 9,710,000.00 USD | 0.00 USD | 28,050.00 USD | `-25.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.05` | 9,680,000.00 USD | 0.00 USD | 18,850.00 USD | `-24.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.75` | 9,660,000.00 USD | 0.00 USD | 2,220.00 USD | `-24.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.95` | 9,660,000.00 USD | 0.00 USD | 277.98 USD | `-23.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.05` | 9,660,000.00 USD | 0.00 USD | 10,650.00 USD | `-23.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.15` | 9,650,000.00 USD | 0.00 USD | 254.34 USD | `-23.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.25` | 9,650,000.00 USD | 0.00 USD | 486.47 USD | `-23.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.55` | 9,650,000.00 USD | 0.00 USD | 4,340.00 USD | `-23.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.65` | 9,640,000.00 USD | 0.00 USD | 536.55 USD | `-23.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.75` | 9,640,000.00 USD | 0.00 USD | 251.74 USD | `-23.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.95` | 9,640,000.00 USD | 0.00 USD | 320.11 USD | `-22.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.05` | 9,640,000.00 USD | 0.00 USD | 8,880.00 USD | `-22.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.35` | 9,630,000.00 USD | 0.00 USD | 5,690.00 USD | `-22.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.95` | 9,630,000.00 USD | 0.00 USD | 155.12 USD | `-21.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.05` | 9,630,000.00 USD | 0.00 USD | 56,050.00 USD | `-21.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.15` | 9,570,000.00 USD | 0.00 USD | 6,240.00 USD | `-21.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.55` | 9,560,000.00 USD | 0.00 USD | 18,590.00 USD | `-21.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.75` | 9,540,000.00 USD | 0.00 USD | 379.58 USD | `-21.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.05` | 9,540,000.00 USD | 0.00 USD | 5,110.00 USD | `-20.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.15` | 9,540,000.00 USD | 0.00 USD | 381.50 USD | `-20.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.25` | 9,540,000.00 USD | 0.00 USD | 1,750.00 USD | `-20.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.45` | 9,540,000.00 USD | 0.00 USD | 5,850.00 USD | `-20.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.65` | 9,530,000.00 USD | 0.00 USD | 238.95 USD | `-20.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.95` | 9,530,000.00 USD | 0.00 USD | 808.29 USD | `-19.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.05` | 9,530,000.00 USD | 0.00 USD | 117,980.00 USD | `-19.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.05` | 9,410,000.00 USD | 0.00 USD | 1,620.00 USD | `-18.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.45` | 9,410,000.00 USD | 0.00 USD | 5,830.00 USD | `-18.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.65` | 9,400,000.00 USD | 0.00 USD | 160.03 USD | `-18.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.95` | 9,400,000.00 USD | 0.00 USD | 71,590.00 USD | `-17.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.05` | 9,330,000.00 USD | 0.00 USD | 12,020.00 USD | `-17.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.15` | 9,320,000.00 USD | 0.00 USD | 684.31 USD | `-17.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.35` | 9,320,000.00 USD | 0.00 USD | 264.34 USD | `-17.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.45` | 9,320,000.00 USD | 0.00 USD | 2,480.00 USD | `-17.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.75` | 9,320,000.00 USD | 0.00 USD | 12,040.00 USD | `-17.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.05` | 9,310,000.00 USD | 0.00 USD | 6,040.00 USD | `-16.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.15` | 9,300,000.00 USD | 0.00 USD | 239.47 USD | `-16.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.25` | 9,300,000.00 USD | 0.00 USD | 18,330.00 USD | `-16.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.45` | 9,280,000.00 USD | 0.00 USD | 45,830.00 USD | `-16.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.55` | 9,240,000.00 USD | 0.00 USD | 421.09 USD | `-16.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.65` | 9,230,000.00 USD | 0.00 USD | 1,370.00 USD | `-16.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.75` | 9,230,000.00 USD | 0.00 USD | 1,320.00 USD | `-16.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.95` | 9,230,000.00 USD | 0.00 USD | 426.47 USD | `-15.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.05` | 9,230,000.00 USD | 0.00 USD | 22,080.00 USD | `-15.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.25` | 9,210,000.00 USD | 0.00 USD | 2,690.00 USD | `-15.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.65` | 9,210,000.00 USD | 0.00 USD | 10,830.00 USD | `-15.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.75` | 9,200,000.00 USD | 0.00 USD | 306.80 USD | `-15.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.95` | 9,200,000.00 USD | 0.00 USD | 1,350.00 USD | `-14.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.05` | 9,190,000.00 USD | 0.00 USD | 167,210.00 USD | `-14.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.15` | 9,030,000.00 USD | 0.00 USD | 437.67 USD | `-14.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.25` | 9,030,000.00 USD | 0.00 USD | 1,320.00 USD | `-14.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.35` | 9,030,000.00 USD | 0.00 USD | 2,270.00 USD | `-14.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.45` | 9,020,000.00 USD | 0.00 USD | 120.48 USD | `-14.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.55` | 9,020,000.00 USD | 0.00 USD | 105.23 USD | `-14.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.65` | 9,020,000.00 USD | 0.00 USD | 310.05 USD | `-14.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.75` | 9,020,000.00 USD | 0.00 USD | 142.34 USD | `-14.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.85` | 9,020,000.00 USD | 0.00 USD | 1,370.00 USD | `-14.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.95` | 9,020,000.00 USD | 0.00 USD | 604.23 USD | `-13.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.05` | 9,020,000.00 USD | 0.00 USD | 5,710.00 USD | `-13.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.15` | 9,010,000.00 USD | 0.00 USD | 2,210.00 USD | `-13.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.25` | 9,010,000.00 USD | 0.00 USD | 538.20 USD | `-13.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.35` | 9,010,000.00 USD | 0.00 USD | 4,080.00 USD | `-13.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.45` | 9,010,000.00 USD | 0.00 USD | 212.67 USD | `-13.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.55` | 9,010,000.00 USD | 0.00 USD | 417.17 USD | `-13.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.65` | 9,010,000.00 USD | 0.00 USD | 305.87 USD | `-13.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.75` | 9,010,000.00 USD | 0.00 USD | 2,020.00 USD | `-13.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.85` | 9,000,000.00 USD | 0.00 USD | 1,300.00 USD | `-13.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.95` | 9,000,000.00 USD | 0.00 USD | 132.16 USD | `-12.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.05` | 9,000,000.00 USD | 0.00 USD | 220,400.00 USD | `-12.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.15` | 8,780,000.00 USD | 0.00 USD | 435.75 USD | `-12.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.25` | 8,780,000.00 USD | 0.00 USD | 8,200.00 USD | `-12.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.35` | 8,770,000.00 USD | 0.00 USD | 436.75 USD | `-12.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.45` | 8,770,000.00 USD | 0.00 USD | 730.21 USD | `-12.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.55` | 8,770,000.00 USD | 0.00 USD | 316.93 USD | `-12.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.65` | 8,770,000.00 USD | 0.00 USD | 2,880.00 USD | `-12.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.05` | 8,770,000.00 USD | 0.00 USD | 70,660.00 USD | `-11.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.15` | 8,700,000.00 USD | 0.00 USD | 833.02 USD | `-11.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.25` | 8,700,000.00 USD | 0.00 USD | 8,860.00 USD | `-11.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.35` | 8,690,000.00 USD | 0.00 USD | 26,510.00 USD | `-11.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.45` | 8,660,000.00 USD | 0.00 USD | 867.69 USD | `-11.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.55` | 8,660,000.00 USD | 0.00 USD | 7,610.00 USD | `-11.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.65` | 8,650,000.00 USD | 0.00 USD | 27,220.00 USD | `-11.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.75` | 8,630,000.00 USD | 0.00 USD | 53,250.00 USD | `-11.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.85` | 8,570,000.00 USD | 0.00 USD | 95,650.00 USD | `-11.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.95` | 8,480,000.00 USD | 0.00 USD | 141.43 USD | `-10.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.05` | 8,480,000.00 USD | 0.00 USD | 8,910.00 USD | `-10.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.15` | 8,470,000.00 USD | 0.00 USD | 6,470.00 USD | `-10.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.25` | 8,460,000.00 USD | 0.00 USD | 328.44 USD | `-10.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.35` | 8,460,000.00 USD | 0.00 USD | 615.62 USD | `-10.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.45` | 8,460,000.00 USD | 0.00 USD | 9,920.00 USD | `-10.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.55` | 8,450,000.00 USD | 0.00 USD | 348.35 USD | `-10.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.65` | 8,450,000.00 USD | 0.00 USD | 173.02 USD | `-10.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.75` | 8,450,000.00 USD | 0.00 USD | 14,640.00 USD | `-10.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.85` | 8,440,000.00 USD | 0.00 USD | 19,490.00 USD | `-10.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.95` | 8,420,000.00 USD | 0.00 USD | 9,100.00 USD | `-9.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.05` | 8,410,000.00 USD | 0.00 USD | 144,200.00 USD | `-9.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.15` | 8,260,000.00 USD | 0.00 USD | 180.30 USD | `-9.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.25` | 8,260,000.00 USD | 0.00 USD | 15,950.00 USD | `-9.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.45` | 8,250,000.00 USD | 0.00 USD | 4,900.00 USD | `-9.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.55` | 8,240,000.00 USD | 0.00 USD | 2,670.00 USD | `-9.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.65` | 8,240,000.00 USD | 0.00 USD | 342.66 USD | `-9.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.75` | 8,240,000.00 USD | 0.00 USD | 4,370.00 USD | `-9.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.95` | 8,240,000.00 USD | 0.00 USD | 3,520.00 USD | `-8.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.05` | 8,230,000.00 USD | 0.00 USD | 60,420.00 USD | `-8.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.15` | 8,170,000.00 USD | 0.00 USD | 1,620.00 USD | `-8.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.35` | 8,170,000.00 USD | 0.00 USD | 5,350.00 USD | `-8.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.45` | 8,160,000.00 USD | 0.00 USD | 107.00 USD | `-8.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.55` | 8,160,000.00 USD | 0.00 USD | 342,520.00 USD | `-8.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.65` | 7,820,000.00 USD | 0.00 USD | 16,300.00 USD | `-8.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.75` | 7,810,000.00 USD | 0.00 USD | 3,340.00 USD | `-8.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.85` | 7,800,000.00 USD | 0.00 USD | 411.49 USD | `-8.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.95` | 7,800,000.00 USD | 0.00 USD | 2,740.00 USD | `-7.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.05` | 7,800,000.00 USD | 0.00 USD | 25,400.00 USD | `-7.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.15` | 7,770,000.00 USD | 0.00 USD | 879.11 USD | `-7.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.25` | 7,770,000.00 USD | 0.00 USD | 139.30 USD | `-7.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.35` | 7,770,000.00 USD | 0.00 USD | 1,030.00 USD | `-7.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.45` | 7,770,000.00 USD | 0.00 USD | 129.43 USD | `-7.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.55` | 7,770,000.00 USD | 0.00 USD | 2,540.00 USD | `-7.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.65` | 7,770,000.00 USD | 0.00 USD | 176.03 USD | `-7.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.75` | 7,770,000.00 USD | 0.00 USD | 1,800.00 USD | `-7.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.85` | 7,770,000.00 USD | 0.00 USD | 29,340.00 USD | `-7.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.95` | 7,740,000.00 USD | 0.00 USD | 6,450.00 USD | `-6.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.05` | 7,730,000.00 USD | 0.00 USD | 8,390.00 USD | `-6.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.15` | 7,720,000.00 USD | 0.00 USD | 340.93 USD | `-6.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.25` | 7,720,000.00 USD | 0.00 USD | 749.73 USD | `-6.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.35` | 7,720,000.00 USD | 0.00 USD | 188.57 USD | `-6.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.45` | 7,720,000.00 USD | 0.00 USD | 19,080.00 USD | `-6.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.55` | 7,700,000.00 USD | 0.00 USD | 567,730.00 USD | `-6.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.65` | 7,140,000.00 USD | 0.00 USD | 448,790.00 USD | `-6.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.75` | 6,690,000.00 USD | 0.00 USD | 2,980.00 USD | `-6.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.85` | 6,680,000.00 USD | 0.00 USD | 747.98 USD | `-6.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.95` | 6,680,000.00 USD | 0.00 USD | 17,380.00 USD | `-5.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.05` | 6,670,000.00 USD | 0.00 USD | 530,360.00 USD | `-5.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.15` | 6,130,000.00 USD | 0.00 USD | 9,330.00 USD | `-5.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.25` | 6,130,000.00 USD | 0.00 USD | 175.30 USD | `-5.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.35` | 6,130,000.00 USD | 0.00 USD | 3,970.00 USD | `-5.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.45` | 6,120,000.00 USD | 0.00 USD | 425.03 USD | `-5.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.55` | 6,120,000.00 USD | 0.00 USD | 25,830.00 USD | `-5.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.65` | 6,100,000.00 USD | 0.00 USD | 4,640.00 USD | `-5.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.75` | 6,090,000.00 USD | 0.00 USD | 7,010.00 USD | `-5.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.85` | 6,080,000.00 USD | 0.00 USD | 12,900.00 USD | `-5.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.95` | 6,070,000.00 USD | 0.00 USD | 6,670.00 USD | `-4.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.05` | 6,060,000.00 USD | 0.00 USD | 220,060.00 USD | `-4.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.15` | 5,840,000.00 USD | 0.00 USD | 5,740.00 USD | `-4.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.25` | 5,840,000.00 USD | 0.00 USD | 1,160.00 USD | `-4.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.35` | 5,840,000.00 USD | 0.00 USD | 5,890.00 USD | `-4.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.45` | 5,830,000.00 USD | 0.00 USD | 8,920.00 USD | `-4.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.55` | 5,820,000.00 USD | 0.00 USD | 594,400.00 USD | `-4.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.65` | 5,230,000.00 USD | 0.00 USD | 4,500.00 USD | `-4.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.75` | 5,220,000.00 USD | 0.00 USD | 5,070.00 USD | `-4.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.85` | 5,220,000.00 USD | 0.00 USD | 31,790.00 USD | `-4.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.95` | 5,190,000.00 USD | 0.00 USD | 9,640.00 USD | `-3.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.05` | 5,180,000.00 USD | 0.00 USD | 639,110.00 USD | `-3.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.15` | 4,540,000.00 USD | 0.00 USD | 884.58 USD | `-3.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.25` | 4,540,000.00 USD | 0.00 USD | 27,450.00 USD | `-3.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.35` | 4,510,000.00 USD | 0.00 USD | 6,480.00 USD | `-3.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.45` | 4,500,000.00 USD | 0.00 USD | 487.07 USD | `-3.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.55` | 4,500,000.00 USD | 0.00 USD | 7,910.00 USD | `-3.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.65` | 4,490,000.00 USD | 0.00 USD | 341.17 USD | `-3.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.75` | 4,490,000.00 USD | 0.00 USD | 82,170.00 USD | `-3.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.85` | 4,410,000.00 USD | 0.00 USD | 16,590.00 USD | `-3.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.95` | 4,400,000.00 USD | 0.00 USD | 14,450.00 USD | `-2.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `97.05` | 4,380,000.00 USD | 0.00 USD | 171,340.00 USD | `-2.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `97.15` | 4,210,000.00 USD | 0.00 USD | 38,020.00 USD | `-2.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `97.25` | 4,170,000.00 USD | 0.00 USD | 21,610.00 USD | `-2.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `97.35` | 4,150,000.00 USD | 0.00 USD | 3,970.00 USD | `-2.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `97.45` | 4,150,000.00 USD | 0.00 USD | 1,890.00 USD | `-2.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `97.55` | 4,140,000.00 USD | 0.00 USD | 14,670.00 USD | `-2.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `97.65` | 4,130,000.00 USD | 0.00 USD | 24,710.00 USD | `-2.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `97.75` | 4,100,000.00 USD | 0.00 USD | 13,520.00 USD | `-2.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `97.85` | 4,090,000.00 USD | 0.00 USD | 56,580.00 USD | `-2.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `97.95` | 4,030,000.00 USD | 0.00 USD | 185,150.00 USD | `-1.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `98.05` | 3,850,000.00 USD | 0.00 USD | 408,220.00 USD | `-1.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `98.15` | 3,440,000.00 USD | 0.00 USD | 13,590.00 USD | `-1.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `98.25` | 3,430,000.00 USD | 0.00 USD | 70,980.00 USD | `-1.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `98.35` | 3,360,000.00 USD | 0.00 USD | 40,210.00 USD | `-1.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `98.45` | 3,320,000.00 USD | 0.00 USD | 174,360.00 USD | `-1.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `98.55` | 3,140,000.00 USD | 0.00 USD | 173,530.00 USD | `-1.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `98.65` | 2,970,000.00 USD | 0.00 USD | 2,030,000.00 USD | `-1.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `98.75` | 942,580.00 USD | 0.00 USD | 43,610.00 USD | `-1.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `98.85` | 898,960.00 USD | 0.00 USD | 74,350.00 USD | `-1.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `98.95` | 824,610.00 USD | 0.00 USD | 46,660.00 USD | `-0.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `99.05` | 777,950.00 USD | 0.00 USD | 172,220.00 USD | `-0.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `99.15` | 605,730.00 USD | 0.00 USD | 210,650.00 USD | `-0.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `99.25` | 395,080.00 USD | 0.00 USD | 38,490.00 USD | `-0.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `99.35` | 356,590.00 USD | 0.00 USD | 37,110.00 USD | `-0.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `99.45` | 319,480.00 USD | 0.00 USD | 114,220.00 USD | `-0.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `99.55` | 205,260.00 USD | 0.00 USD | 8,740.00 USD | `-0.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `99.65` | 196,520.00 USD | 0.00 USD | 12,050.00 USD | `-0.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `99.75` | 184,470.00 USD | 0.00 USD | 162,940.00 USD | `-0.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `99.85` | 21,540.00 USD | 0.00 USD | 21,540.00 USD | `-0.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.95` | 37,460.00 USD | 37,460.00 USD | 0.00 USD | `+0.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.05` | 40,250.00 USD | 2,780.00 USD | 0.00 USD | `+0.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.15` | 124,640.00 USD | 84,390.00 USD | 0.00 USD | `+0.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.25` | 142,670.00 USD | 18,030.00 USD | 0.00 USD | `+0.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.35` | 146,590.00 USD | 3,920.00 USD | 0.00 USD | `+0.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.45` | 151,250.00 USD | 4,670.00 USD | 0.00 USD | `+0.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.55` | 168,720.00 USD | 17,460.00 USD | 0.00 USD | `+0.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.65` | 178,910.00 USD | 10,190.00 USD | 0.00 USD | `+0.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.75` | 197,140.00 USD | 18,230.00 USD | 0.00 USD | `+0.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.85` | 199,700.00 USD | 2,560.00 USD | 0.00 USD | `+0.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.95` | 202,030.00 USD | 2,330.00 USD | 0.00 USD | `+1.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.05` | 220,950.00 USD | 18,920.00 USD | 0.00 USD | `+1.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.15` | 428,980.00 USD | 208,030.00 USD | 0.00 USD | `+1.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.25` | 432,010.00 USD | 3,030.00 USD | 0.00 USD | `+1.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.35` | 463,960.00 USD | 31,950.00 USD | 0.00 USD | `+1.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.45` | 492,730.00 USD | 28,770.00 USD | 0.00 USD | `+1.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.55` | 497,290.00 USD | 4,560.00 USD | 0.00 USD | `+1.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.65` | 498,360.00 USD | 1,060.00 USD | 0.00 USD | `+1.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.75` | 506,370.00 USD | 8,010.00 USD | 0.00 USD | `+1.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.85` | 509,650.00 USD | 3,280.00 USD | 0.00 USD | `+1.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.95` | 548,180.00 USD | 38,530.00 USD | 0.00 USD | `+2.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.05` | 560,740.00 USD | 12,560.00 USD | 0.00 USD | `+2.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.15` | 561,290.00 USD | 553.65 USD | 0.00 USD | `+2.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.25` | 571,050.00 USD | 9,760.00 USD | 0.00 USD | `+2.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.35` | 1,190,000.00 USD | 618,530.00 USD | 0.00 USD | `+2.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.45` | 1,240,000.00 USD | 54,320.00 USD | 0.00 USD | `+2.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.55` | 1,510,000.00 USD | 262,740.00 USD | 0.00 USD | `+2.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.65` | 1,510,000.00 USD | 7,920.00 USD | 0.00 USD | `+2.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.75` | 1,530,000.00 USD | 11,780.00 USD | 0.00 USD | `+2.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.85` | 1,550,000.00 USD | 21,080.00 USD | 0.00 USD | `+2.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.95` | 1,570,000.00 USD | 23,580.00 USD | 0.00 USD | `+3.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.05` | 1,610,000.00 USD | 40,860.00 USD | 0.00 USD | `+3.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.15` | 1,740,000.00 USD | 124,820.00 USD | 0.00 USD | `+3.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.25` | 1,740,000.00 USD | 3,310.00 USD | 0.00 USD | `+3.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.35` | 1,740,000.00 USD | 4,710.00 USD | 0.00 USD | `+3.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.45` | 1,750,000.00 USD | 7,750.00 USD | 0.00 USD | `+3.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.55` | 1,760,000.00 USD | 7,830.00 USD | 0.00 USD | `+3.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.65` | 1,760,000.00 USD | 2,660.00 USD | 0.00 USD | `+3.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.75` | 1,770,000.00 USD | 4,540.00 USD | 0.00 USD | `+3.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.85` | 1,810,000.00 USD | 44,740.00 USD | 0.00 USD | `+3.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.95` | 1,890,000.00 USD | 74,500.00 USD | 0.00 USD | `+4.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.05` | 1,930,000.00 USD | 39,070.00 USD | 0.00 USD | `+4.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.15` | 1,930,000.00 USD | 1,930.00 USD | 0.00 USD | `+4.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.25` | 1,950,000.00 USD | 17,430.00 USD | 0.00 USD | `+4.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.35` | 1,950,000.00 USD | 1,190.00 USD | 0.00 USD | `+4.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.45` | 1,960,000.00 USD | 13,040.00 USD | 0.00 USD | `+4.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.55` | 2,030,000.00 USD | 70,470.00 USD | 0.00 USD | `+4.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.65` | 2,140,000.00 USD | 108,300.00 USD | 0.00 USD | `+4.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.75` | 2,160,000.00 USD | 19,970.00 USD | 0.00 USD | `+4.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.85` | 2,160,000.00 USD | 5,900.00 USD | 0.00 USD | `+4.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.95` | 2,190,000.00 USD | 28,080.00 USD | 0.00 USD | `+5.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.05` | 2,460,000.00 USD | 263,770.00 USD | 0.00 USD | `+5.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.15` | 2,480,000.00 USD | 27,940.00 USD | 0.00 USD | `+5.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.25` | 2,490,000.00 USD | 2,180.00 USD | 0.00 USD | `+5.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.35` | 2,490,000.00 USD | 1,110.00 USD | 0.00 USD | `+5.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.45` | 2,520,000.00 USD | 35,000.00 USD | 0.00 USD | `+5.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.55` | 2,530,000.00 USD | 4,730.00 USD | 0.00 USD | `+5.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.65` | 2,530,000.00 USD | 395.13 USD | 0.00 USD | `+5.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.75` | 2,540,000.00 USD | 10,860.00 USD | 0.00 USD | `+5.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.85` | 2,550,000.00 USD | 15,720.00 USD | 0.00 USD | `+5.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.95` | 2,550,000.00 USD | 332.68 USD | 0.00 USD | `+6.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.05` | 2,600,000.00 USD | 50,060.00 USD | 0.00 USD | `+6.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.15` | 2,620,000.00 USD | 14,120.00 USD | 0.00 USD | `+6.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.25` | 2,620,000.00 USD | 2,370.00 USD | 0.00 USD | `+6.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.35` | 2,700,000.00 USD | 76,140.00 USD | 0.00 USD | `+6.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.45` | 2,720,000.00 USD | 26,380.00 USD | 0.00 USD | `+6.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.55` | 2,730,000.00 USD | 6,740.00 USD | 0.00 USD | `+6.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.65` | 2,750,000.00 USD | 20,390.00 USD | 0.00 USD | `+6.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.75` | 2,890,000.00 USD | 136,770.00 USD | 0.00 USD | `+6.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.85` | 2,890,000.00 USD | 1,000.00 USD | 0.00 USD | `+6.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.95` | 2,910,000.00 USD | 24,550.00 USD | 0.00 USD | `+7.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.05` | 2,930,000.00 USD | 14,630.00 USD | 0.00 USD | `+7.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.15` | 2,930,000.00 USD | 1,200.00 USD | 0.00 USD | `+7.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.25` | 2,950,000.00 USD | 21,470.00 USD | 0.00 USD | `+7.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.35` | 2,950,000.00 USD | 549.63 USD | 0.00 USD | `+7.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.45` | 2,960,000.00 USD | 6,670.00 USD | 0.00 USD | `+7.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.55` | 3,020,000.00 USD | 61,510.00 USD | 0.00 USD | `+7.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.65` | 3,080,000.00 USD | 65,480.00 USD | 0.00 USD | `+7.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.75` | 3,090,000.00 USD | 2,140.00 USD | 0.00 USD | `+7.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.85` | 3,090,000.00 USD | 5,100.00 USD | 0.00 USD | `+7.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.95` | 3,100,000.00 USD | 4,420.00 USD | 0.00 USD | `+8.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.05` | 3,230,000.00 USD | 130,930.00 USD | 0.00 USD | `+8.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.15` | 3,350,000.00 USD | 126,900.00 USD | 0.00 USD | `+8.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.25` | 3,350,000.00 USD | 1,240.00 USD | 0.00 USD | `+8.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.35` | 3,370,000.00 USD | 14,890.00 USD | 0.00 USD | `+8.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.45` | 3,370,000.00 USD | 3,920.00 USD | 0.00 USD | `+8.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.55` | 3,400,000.00 USD | 28,270.00 USD | 0.00 USD | `+8.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.65` | 3,400,000.00 USD | 2,310.00 USD | 0.00 USD | `+8.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.75` | 3,410,000.00 USD | 3,790.00 USD | 0.00 USD | `+8.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.85` | 3,410,000.00 USD | 4,570.00 USD | 0.00 USD | `+8.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.95` | 3,460,000.00 USD | 46,180.00 USD | 0.00 USD | `+9.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.05` | 3,490,000.00 USD | 35,950.00 USD | 0.00 USD | `+9.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.15` | 3,500,000.00 USD | 9,970.00 USD | 0.00 USD | `+9.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.25` | 7,640,000.00 USD | 4,140,000.00 USD | 0.00 USD | `+9.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.35` | 7,680,000.00 USD | 42,830.00 USD | 0.00 USD | `+9.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.45` | 7,700,000.00 USD | 18,910.00 USD | 0.00 USD | `+9.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.55` | 7,700,000.00 USD | 1,170.00 USD | 0.00 USD | `+9.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.65` | 7,710,000.00 USD | 5,300.00 USD | 0.00 USD | `+9.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.75` | 7,740,000.00 USD | 30,610.00 USD | 0.00 USD | `+9.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.85` | 7,760,000.00 USD | 21,030.00 USD | 0.00 USD | `+9.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.95` | 7,770,000.00 USD | 9,630.00 USD | 0.00 USD | `+10.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.05` | 8,630,000.00 USD | 860,300.00 USD | 0.00 USD | `+10.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.15` | 8,630,000.00 USD | 485.76 USD | 0.00 USD | `+10.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.25` | 8,640,000.00 USD | 8,640.00 USD | 0.00 USD | `+10.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.35` | 8,640,000.00 USD | 1,840.00 USD | 0.00 USD | `+10.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.45` | 8,640,000.00 USD | 1,720.00 USD | 0.00 USD | `+10.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.55` | 8,660,000.00 USD | 10,820.00 USD | 0.00 USD | `+10.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.65` | 8,660,000.00 USD | 3,030.00 USD | 0.00 USD | `+10.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.85` | 8,680,000.00 USD | 17,520.00 USD | 0.00 USD | `+10.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.95` | 9,130,000.00 USD | 454,790.00 USD | 0.00 USD | `+11.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.05` | 9,140,000.00 USD | 4,830.00 USD | 0.00 USD | `+11.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.15` | 9,140,000.00 USD | 1,300.00 USD | 0.00 USD | `+11.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.25` | 9,140,000.00 USD | 7,390.00 USD | 0.00 USD | `+11.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.45` | 9,150,000.00 USD | 1,520.00 USD | 0.00 USD | `+11.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.55` | 9,160,000.00 USD | 11,820.00 USD | 0.00 USD | `+11.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.65` | 9,160,000.00 USD | 106.07 USD | 0.00 USD | `+11.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.75` | 9,170,000.00 USD | 12,310.00 USD | 0.00 USD | `+11.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.85` | 9,180,000.00 USD | 6,140.00 USD | 0.00 USD | `+11.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.95` | 9,180,000.00 USD | 559.75 USD | 0.00 USD | `+12.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.05` | 9,280,000.00 USD | 101,480.00 USD | 0.00 USD | `+12.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.15` | 9,360,000.00 USD | 79,360.00 USD | 0.00 USD | `+12.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.25` | 9,360,000.00 USD | 4,960.00 USD | 0.00 USD | `+12.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.35` | 9,370,000.00 USD | 5,120.00 USD | 0.00 USD | `+12.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.45` | 9,380,000.00 USD | 7,870.00 USD | 0.00 USD | `+12.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.55` | 9,400,000.00 USD | 25,610.00 USD | 0.00 USD | `+12.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.65` | 9,410,000.00 USD | 4,240.00 USD | 0.00 USD | `+12.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.85` | 9,410,000.00 USD | 1,130.00 USD | 0.00 USD | `+12.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.05` | 9,590,000.00 USD | 183,810.00 USD | 0.00 USD | `+13.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.15` | 9,590,000.00 USD | 427.71 USD | 0.00 USD | `+13.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.25` | 9,590,000.00 USD | 1,380.00 USD | 0.00 USD | `+13.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.35` | 9,760,000.00 USD | 166,690.00 USD | 0.00 USD | `+13.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.45` | 9,760,000.00 USD | 655.74 USD | 0.00 USD | `+13.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.55` | 9,760,000.00 USD | 590.46 USD | 0.00 USD | `+13.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.65` | 9,760,000.00 USD | 230.71 USD | 0.00 USD | `+13.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.75` | 9,760,000.00 USD | 257.07 USD | 0.00 USD | `+13.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.85` | 9,760,000.00 USD | 4,540.00 USD | 0.00 USD | `+13.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.05` | 9,770,000.00 USD | 2,400.00 USD | 0.00 USD | `+14.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.15` | 9,780,000.00 USD | 11,410.00 USD | 0.00 USD | `+14.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.25` | 9,780,000.00 USD | 584.96 USD | 0.00 USD | `+14.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.35` | 9,790,000.00 USD | 9,320.00 USD | 0.00 USD | `+14.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.45` | 9,790,000.00 USD | 452.08 USD | 0.00 USD | `+14.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.55` | 9,790,000.00 USD | 5,340.00 USD | 0.00 USD | `+14.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.65` | 9,810,000.00 USD | 11,800.00 USD | 0.00 USD | `+14.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.75` | 9,810,000.00 USD | 1,010.00 USD | 0.00 USD | `+14.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.95` | 9,810,000.00 USD | 1,610.00 USD | 0.00 USD | `+15.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.05` | 9,910,000.00 USD | 99,450.00 USD | 0.00 USD | `+15.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.35` | 9,910,000.00 USD | 139.57 USD | 0.00 USD | `+15.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.45` | 9,920,000.00 USD | 16,270.00 USD | 0.00 USD | `+15.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.55` | 9,930,000.00 USD | 1,980.00 USD | 0.00 USD | `+15.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.85` | 9,930,000.00 USD | 579.25 USD | 0.00 USD | `+15.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.05` | 9,940,000.00 USD | 13,900.00 USD | 0.00 USD | `+16.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.15` | 9,940,000.00 USD | 1,700.00 USD | 0.00 USD | `+16.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.25` | 9,950,000.00 USD | 6,770.00 USD | 0.00 USD | `+16.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.45` | 9,960,000.00 USD | 6,860.00 USD | 0.00 USD | `+16.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.55` | 9,970,000.00 USD | 10,810.00 USD | 0.00 USD | `+16.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.65` | 9,970,000.00 USD | 1,100.00 USD | 0.00 USD | `+16.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.75` | 9,970,000.00 USD | 3,580.00 USD | 0.00 USD | `+16.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.85` | 9,970,000.00 USD | 234.87 USD | 0.00 USD | `+16.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.95` | 9,970,000.00 USD | 1,170.00 USD | 0.00 USD | `+17.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.05` | 9,980,000.00 USD | 3,850.00 USD | 0.00 USD | `+17.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.15` | 9,980,000.00 USD | 1,690.00 USD | 0.00 USD | `+17.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.25` | 9,980,000.00 USD | 349.40 USD | 0.00 USD | `+17.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.35` | 9,980,000.00 USD | 2,330.00 USD | 0.00 USD | `+17.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.45` | 10,060,000.00 USD | 80,010.00 USD | 0.00 USD | `+17.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.65` | 10,170,000.00 USD | 106,040.00 USD | 0.00 USD | `+17.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.75` | 10,170,000.00 USD | 5,920.00 USD | 0.00 USD | `+17.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.85` | 10,230,000.00 USD | 55,580.00 USD | 0.00 USD | `+17.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.05` | 10,290,000.00 USD | 62,380.00 USD | 0.00 USD | `+18.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.15` | 10,300,000.00 USD | 11,700.00 USD | 0.00 USD | `+18.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.25` | 10,310,000.00 USD | 3,090.00 USD | 0.00 USD | `+18.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.35` | 10,320,000.00 USD | 12,610.00 USD | 0.00 USD | `+18.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.45` | 10,320,000.00 USD | 1,780.00 USD | 0.00 USD | `+18.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.55` | 10,390,000.00 USD | 71,300.00 USD | 0.00 USD | `+18.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.65` | 10,390,000.00 USD | 593.25 USD | 0.00 USD | `+18.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.75` | 10,390,000.00 USD | 403.75 USD | 0.00 USD | `+18.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.85` | 10,410,000.00 USD | 13,560.00 USD | 0.00 USD | `+18.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.95` | 10,410,000.00 USD | 655.41 USD | 0.00 USD | `+19.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.05` | 10,460,000.00 USD | 55,170.00 USD | 0.00 USD | `+19.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.15` | 10,470,000.00 USD | 9,120.00 USD | 0.00 USD | `+19.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.25` | 10,470,000.00 USD | 2,050.00 USD | 0.00 USD | `+19.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.35` | 10,480,000.00 USD | 5,330.00 USD | 0.00 USD | `+19.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.45` | 10,480,000.00 USD | 3,580.00 USD | 0.00 USD | `+19.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.65` | 10,480,000.00 USD | 615.00 USD | 0.00 USD | `+19.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.75` | 10,610,000.00 USD | 125,660.00 USD | 0.00 USD | `+19.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.85` | 10,650,000.00 USD | 37,630.00 USD | 0.00 USD | `+19.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.95` | 10,650,000.00 USD | 458.21 USD | 0.00 USD | `+20.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.05` | 10,790,000.00 USD | 142,780.00 USD | 0.00 USD | `+20.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.15` | 10,790,000.00 USD | 414.52 USD | 0.00 USD | `+20.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.25` | 10,790,000.00 USD | 3,210.00 USD | 0.00 USD | `+20.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.35` | 10,800,000.00 USD | 7,850.00 USD | 0.00 USD | `+20.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.45` | 10,800,000.00 USD | 184.29 USD | 0.00 USD | `+20.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.55` | 10,800,000.00 USD | 964.40 USD | 0.00 USD | `+20.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.65` | 10,800,000.00 USD | 191.83 USD | 0.00 USD | `+20.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.75` | 10,800,000.00 USD | 2,150.00 USD | 0.00 USD | `+20.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.85` | 10,810,000.00 USD | 1,220.00 USD | 0.00 USD | `+20.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.05` | 10,830,000.00 USD | 21,080.00 USD | 0.00 USD | `+21.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.15` | 10,830,000.00 USD | 1,130.00 USD | 0.00 USD | `+21.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.25` | 10,840,000.00 USD | 9,390.00 USD | 0.00 USD | `+21.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.45` | 10,850,000.00 USD | 11,570.00 USD | 0.00 USD | `+21.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.55` | 10,860,000.00 USD | 9,300.00 USD | 0.00 USD | `+21.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.65` | 10,860,000.00 USD | 3,300.00 USD | 0.00 USD | `+21.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.75` | 10,860,000.00 USD | 2,450.00 USD | 0.00 USD | `+21.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.85` | 10,870,000.00 USD | 7,600.00 USD | 0.00 USD | `+21.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.95` | 10,880,000.00 USD | 12,910.00 USD | 0.00 USD | `+22.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.05` | 11,090,000.00 USD | 202,130.00 USD | 0.00 USD | `+22.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.15` | 11,090,000.00 USD | 3,370.00 USD | 0.00 USD | `+22.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.25` | 11,330,000.00 USD | 235,920.00 USD | 0.00 USD | `+22.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.35` | 11,380,000.00 USD | 52,640.00 USD | 0.00 USD | `+22.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.45` | 11,380,000.00 USD | 4,880.00 USD | 0.00 USD | `+22.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.55` | 11,390,000.00 USD | 7,020.00 USD | 0.00 USD | `+22.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.65` | 11,400,000.00 USD | 7,930.00 USD | 0.00 USD | `+22.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.75` | 11,400,000.00 USD | 1,340.00 USD | 0.00 USD | `+22.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.85` | 11,400,000.00 USD | 3,780.00 USD | 0.00 USD | `+22.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.95` | 11,410,000.00 USD | 9,310.00 USD | 0.00 USD | `+23.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.05` | 12,420,000.00 USD | 1,000,000.00 USD | 0.00 USD | `+23.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.15` | 12,420,000.00 USD | 1,260.00 USD | 0.00 USD | `+23.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.25` | 12,430,000.00 USD | 7,710.00 USD | 0.00 USD | `+23.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.35` | 12,430,000.00 USD | 8,590.00 USD | 0.00 USD | `+23.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.45` | 12,440,000.00 USD | 2,670.00 USD | 0.00 USD | `+23.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.55` | 12,440,000.00 USD | 632.58 USD | 0.00 USD | `+23.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.65` | 12,440,000.00 USD | 7,440.00 USD | 0.00 USD | `+23.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.85` | 12,460,000.00 USD | 11,530.00 USD | 0.00 USD | `+24.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.95` | 12,480,000.00 USD | 18,820.00 USD | 0.00 USD | `+24.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.05` | 12,590,000.00 USD | 111,940.00 USD | 0.00 USD | `+24.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.15` | 12,590,000.00 USD | 1,200.00 USD | 0.00 USD | `+24.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.25` | 12,590,000.00 USD | 144.13 USD | 0.00 USD | `+24.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.35` | 12,590,000.00 USD | 4,110.00 USD | 0.00 USD | `+24.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.45` | 12,590,000.00 USD | 1,370.00 USD | 0.00 USD | `+24.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.55` | 12,600,000.00 USD | 7,100.00 USD | 0.00 USD | `+24.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.65` | 12,610,000.00 USD | 6,610.00 USD | 0.00 USD | `+24.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.85` | 12,610,000.00 USD | 344.59 USD | 0.00 USD | `+25.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.95` | 12,640,000.00 USD | 33,280.00 USD | 0.00 USD | `+25.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.05` | 13,190,000.00 USD | 544,010.00 USD | 0.00 USD | `+25.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.15` | 13,190,000.00 USD | 680.82 USD | 0.00 USD | `+25.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.25` | 13,190,000.00 USD | 311.87 USD | 0.00 USD | `+25.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.35` | 13,190,000.00 USD | 1,310.00 USD | 0.00 USD | `+25.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.45` | 13,190,000.00 USD | 3,320.00 USD | 0.00 USD | `+25.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.55` | 13,230,000.00 USD | 41,310.00 USD | 0.00 USD | `+25.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.85` | 13,230,000.00 USD | 471.94 USD | 0.00 USD | `+26.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.95` | 13,230,000.00 USD | 209.08 USD | 0.00 USD | `+26.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.05` | 13,330,000.00 USD | 93,250.00 USD | 0.00 USD | `+26.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.15` | 13,340,000.00 USD | 12,800.00 USD | 0.00 USD | `+26.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.45` | 13,340,000.00 USD | 187.15 USD | 0.00 USD | `+26.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.65` | 13,340,000.00 USD | 3,550.00 USD | 0.00 USD | `+26.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.75` | 13,350,000.00 USD | 5,440.00 USD | 0.00 USD | `+26.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.05` | 13,540,000.00 USD | 192,050.00 USD | 0.00 USD | `+27.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.35` | 13,540,000.00 USD | 534.87 USD | 0.00 USD | `+27.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.45` | 13,560,000.00 USD | 15,320.00 USD | 0.00 USD | `+27.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.65` | 13,560,000.00 USD | 5,000.00 USD | 0.00 USD | `+27.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.75` | 13,560,000.00 USD | 362.81 USD | 0.00 USD | `+27.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.85` | 13,620,000.00 USD | 60,770.00 USD | 0.00 USD | `+28.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.95` | 13,620,000.00 USD | 482.37 USD | 0.00 USD | `+28.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.05` | 13,660,000.00 USD | 42,090.00 USD | 0.00 USD | `+28.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.15` | 13,670,000.00 USD | 3,010.00 USD | 0.00 USD | `+28.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.25` | 13,670,000.00 USD | 191.09 USD | 0.00 USD | `+28.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.85` | 13,670,000.00 USD | 132.72 USD | 0.00 USD | `+29.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.95` | 13,680,000.00 USD | 12,600.00 USD | 0.00 USD | `+29.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.05` | 13,740,000.00 USD | 63,620.00 USD | 0.00 USD | `+29.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.25` | 13,760,000.00 USD | 15,330.00 USD | 0.00 USD | `+29.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.45` | 13,760,000.00 USD | 401.29 USD | 0.00 USD | `+29.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.55` | 13,760,000.00 USD | 1,320.00 USD | 0.00 USD | `+29.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.75` | 13,760,000.00 USD | 882.30 USD | 0.00 USD | `+29.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.85` | 16,360,000.00 USD | 2,600,000.00 USD | 0.00 USD | `+30.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.05` | 16,390,000.00 USD | 30,560.00 USD | 0.00 USD | `+30.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.35` | 16,410,000.00 USD | 15,590.00 USD | 0.00 USD | `+30.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.45` | 16,410,000.00 USD | 4,090.00 USD | 0.00 USD | `+30.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.65` | 16,410,000.00 USD | 192.06 USD | 0.00 USD | `+30.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.75` | 16,410,000.00 USD | 3,150.00 USD | 0.00 USD | `+30.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.85` | 16,420,000.00 USD | 4,540.00 USD | 0.00 USD | `+31.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.95` | 16,430,000.00 USD | 10,140.00 USD | 0.00 USD | `+31.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.05` | 16,430,000.00 USD | 6,000.00 USD | 0.00 USD | `+31.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.15` | 16,440,000.00 USD | 5,950.00 USD | 0.00 USD | `+31.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.25` | 16,450,000.00 USD | 6,160.00 USD | 0.00 USD | `+31.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.65` | 16,610,000.00 USD | 160,920.00 USD | 0.00 USD | `+31.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.75` | 16,610,000.00 USD | 144.93 USD | 0.00 USD | `+31.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.05` | 16,620,000.00 USD | 12,390.00 USD | 0.00 USD | `+32.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.65` | 16,620,000.00 USD | 397.95 USD | 0.00 USD | `+32.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.85` | 16,630,000.00 USD | 9,310.00 USD | 0.00 USD | `+33.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.95` | 16,630,000.00 USD | 3,910.00 USD | 0.00 USD | `+33.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.05` | 16,640,000.00 USD | 6,700.00 USD | 0.00 USD | `+33.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.15` | 16,640,000.00 USD | 509.96 USD | 0.00 USD | `+33.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.25` | 16,640,000.00 USD | 191.88 USD | 0.00 USD | `+33.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.35` | 16,640,000.00 USD | 237.36 USD | 0.00 USD | `+33.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.55` | 16,640,000.00 USD | 1,210.00 USD | 0.00 USD | `+33.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.65` | 16,640,000.00 USD | 192.46 USD | 0.00 USD | `+33.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.75` | 16,640,000.00 USD | 112.35 USD | 0.00 USD | `+33.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.95` | 16,650,000.00 USD | 4,120.00 USD | 0.00 USD | `+34.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.05` | 16,700,000.00 USD | 54,080.00 USD | 0.00 USD | `+34.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.25` | 16,700,000.00 USD | 331.60 USD | 0.00 USD | `+34.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.55` | 16,900,000.00 USD | 195,540.00 USD | 0.00 USD | `+34.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.85` | 16,900,000.00 USD | 604.13 USD | 0.00 USD | `+35.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `135.05` | 16,960,000.00 USD | 67,100.00 USD | 0.00 USD | `+35.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `135.55` | 16,970,000.00 USD | 7,560.00 USD | 0.00 USD | `+35.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.05` | 16,970,000.00 USD | 1,890.00 USD | 0.00 USD | `+36.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.35` | 16,970,000.00 USD | 192.25 USD | 0.00 USD | `+36.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.45` | 16,970,000.00 USD | 465.29 USD | 0.00 USD | `+36.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.55` | 16,970,000.00 USD | 389.17 USD | 0.00 USD | `+36.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.85` | 16,980,000.00 USD | 826.57 USD | 0.00 USD | `+37.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.05` | 16,980,000.00 USD | 1,330.00 USD | 0.00 USD | `+37.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.25` | 16,980,000.00 USD | 2,630.00 USD | 0.00 USD | `+37.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.35` | 16,980,000.00 USD | 3,920.00 USD | 0.00 USD | `+37.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.65` | 17,010,000.00 USD | 26,260.00 USD | 0.00 USD | `+37.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.05` | 17,040,000.00 USD | 30,230.00 USD | 0.00 USD | `+38.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.45` | 17,040,000.00 USD | 692.25 USD | 0.00 USD | `+38.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.65` | 17,040,000.00 USD | 406.24 USD | 0.00 USD | `+38.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.85` | 23,780,000.00 USD | 6,740,000.00 USD | 0.00 USD | `+39.01%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `138.95` | 23,780,000.00 USD | 826.75 USD | 0.00 USD | `+39.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `139.05` | 25,990,000.00 USD | 2,200,000.00 USD | 0.00 USD | `+39.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `139.55` | 25,990,000.00 USD | 7,650.00 USD | 0.00 USD | `+39.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.05` | 26,220,000.00 USD | 228,360.00 USD | 0.00 USD | `+40.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.55` | 26,280,000.00 USD | 56,230.00 USD | 0.00 USD | `+40.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.75` | 26,280,000.00 USD | 990.88 USD | 0.00 USD | `+40.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `141.05` | 26,280,000.00 USD | 3,510.00 USD | 0.00 USD | `+41.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `141.25` | 26,290,000.00 USD | 6,190.00 USD | 0.00 USD | `+41.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `141.65` | 26,290,000.00 USD | 796.07 USD | 0.00 USD | `+41.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `142.05` | 26,290,000.00 USD | 826.73 USD | 0.00 USD | `+42.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `142.85` | 26,290,000.00 USD | 278.56 USD | 0.00 USD | `+43.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `142.95` | 26,640,000.00 USD | 346,420.00 USD | 0.00 USD | `+43.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `143.35` | 26,640,000.00 USD | 528.96 USD | 0.00 USD | `+43.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.05` | 26,650,000.00 USD | 8,310.00 USD | 0.00 USD | `+44.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.25` | 26,650,000.00 USD | 415.44 USD | 0.00 USD | `+44.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.35` | 26,900,000.00 USD | 252,610.00 USD | 0.00 USD | `+44.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.55` | 26,910,000.00 USD | 7,260.00 USD | 0.00 USD | `+44.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.75` | 26,910,000.00 USD | 791.78 USD | 0.00 USD | `+44.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `145.05` | 26,920,000.00 USD | 12,120.00 USD | 0.00 USD | `+45.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `145.25` | 26,920,000.00 USD | 209.16 USD | 0.00 USD | `+45.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `145.55` | 26,920,000.00 USD | 698.64 USD | 0.00 USD | `+45.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.05` | 27,110,000.00 USD | 192,080.00 USD | 0.00 USD | `+46.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.15` | 27,120,000.00 USD | 3,300.00 USD | 0.00 USD | `+46.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.25` | 27,120,000.00 USD | 1,020.00 USD | 0.00 USD | `+46.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.95` | 27,120,000.00 USD | 1,500.00 USD | 0.00 USD | `+47.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.05` | 27,160,000.00 USD | 37,700.00 USD | 0.00 USD | `+47.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.45` | 27,160,000.00 USD | 844.89 USD | 0.00 USD | `+47.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.85` | 27,160,000.00 USD | 4,610.00 USD | 0.00 USD | `+48.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.95` | 27,160,000.00 USD | 3,100.00 USD | 0.00 USD | `+48.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `148.05` | 28,490,000.00 USD | 1,330,000.00 USD | 0.00 USD | `+48.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `148.45` | 28,490,000.00 USD | 1,370.00 USD | 0.00 USD | `+48.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `148.55` | 28,490,000.00 USD | 773.95 USD | 0.00 USD | `+48.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `149.05` | 28,500,000.00 USD | 1,440.00 USD | 0.00 USD | `+49.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `149.15` | 29,010,000.00 USD | 510,120.00 USD | 0.00 USD | `+49.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.05` | 29,270,000.00 USD | 264,780.00 USD | 0.00 USD | `+50.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.25` | 29,270,000.00 USD | 1,200.00 USD | 0.00 USD | `+50.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.35` | 29,270,000.00 USD | 178.92 USD | 0.00 USD | `+50.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.55` | 29,270,000.00 USD | 1,360.00 USD | 0.00 USD | `+50.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.05` | 29,290,000.00 USD | 14,430.00 USD | 0.00 USD | `+51.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.25` | 29,290,000.00 USD | 2,000.00 USD | 0.00 USD | `+51.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.45` | 29,290,000.00 USD | 411.94 USD | 0.00 USD | `+51.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.95` | 29,300,000.00 USD | 10,230.00 USD | 0.00 USD | `+52.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `152.15` | 29,310,000.00 USD | 12,000.00 USD | 0.00 USD | `+52.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `153.15` | 29,320,000.00 USD | 10,620.00 USD | 0.00 USD | `+53.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `153.65` | 29,320,000.00 USD | 1,020.00 USD | 0.00 USD | `+53.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `154.55` | 29,340,000.00 USD | 12,000.00 USD | 0.00 USD | `+54.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `154.85` | 29,340,000.00 USD | 113.04 USD | 0.00 USD | `+55.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `154.95` | 29,340,000.00 USD | 156.50 USD | 0.00 USD | `+55.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `155.05` | 29,340,000.00 USD | 1,830.00 USD | 0.00 USD | `+55.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `155.85` | 29,350,000.00 USD | 11,850.00 USD | 0.00 USD | `+56.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `156.05` | 29,350,000.00 USD | 2,230.00 USD | 0.00 USD | `+56.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `158.05` | 29,360,000.00 USD | 6,480.00 USD | 0.00 USD | `+58.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `158.75` | 29,370,000.00 USD | 15,880.00 USD | 0.00 USD | `+58.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `159.15` | 29,370,000.00 USD | 813.26 USD | 0.00 USD | `+59.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `160.05` | 29,620,000.00 USD | 241,860.00 USD | 0.00 USD | `+60.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `161.05` | 29,620,000.00 USD | 281.84 USD | 0.00 USD | `+61.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `163.05` | 29,620,000.00 USD | 5,010.00 USD | 0.00 USD | `+63.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `165.05` | 29,700,000.00 USD | 82,530.00 USD | 0.00 USD | `+65.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `165.45` | 29,710,000.00 USD | 823.94 USD | 0.00 USD | `+65.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `166.45` | 29,710,000.00 USD | 211.39 USD | 0.00 USD | `+66.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `166.95` | 29,710,000.00 USD | 307.19 USD | 0.00 USD | `+67.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `167.05` | 29,710,000.00 USD | 593.03 USD | 0.00 USD | `+67.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `167.75` | 29,710,000.00 USD | 1,440.00 USD | 0.00 USD | `+67.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `168.05` | 29,710,000.00 USD | 5,550.00 USD | 0.00 USD | `+68.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `169.55` | 29,710,000.00 USD | 495.09 USD | 0.00 USD | `+69.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `169.95` | 29,710,000.00 USD | 912.63 USD | 0.00 USD | `+70.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `170.05` | 29,760,000.00 USD | 42,840.00 USD | 0.00 USD | `+70.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `171.55` | 29,760,000.00 USD | 686.20 USD | 0.00 USD | `+71.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `172.05` | 29,790,000.00 USD | 35,280.00 USD | 0.00 USD | `+72.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `172.45` | 29,790,000.00 USD | 703.60 USD | 0.00 USD | `+72.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `173.05` | 29,800,000.00 USD | 6,540.00 USD | 0.00 USD | `+73.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `175.05` | 29,850,000.00 USD | 52,520.00 USD | 0.00 USD | `+75.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `175.25` | 29,880,000.00 USD | 21,960.00 USD | 0.00 USD | `+75.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `176.55` | 29,880,000.00 USD | 1,450.00 USD | 0.00 USD | `+76.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `176.85` | 29,880,000.00 USD | 1,450.00 USD | 0.00 USD | `+77.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `177.05` | 29,880,000.00 USD | 2,140.00 USD | 0.00 USD | `+77.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `177.35` | 29,880,000.00 USD | 390.17 USD | 0.00 USD | `+77.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `178.55` | 29,880,000.00 USD | 2,990.00 USD | 0.00 USD | `+78.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `179.15` | 29,880,000.00 USD | 261.56 USD | 0.00 USD | `+79.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `179.85` | 29,880,000.00 USD | 109.71 USD | 0.00 USD | `+80.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `180.05` | 29,990,000.00 USD | 102,420.00 USD | 0.00 USD | `+80.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `181.05` | 29,990,000.00 USD | 2,370.00 USD | 0.00 USD | `+81.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `181.95` | 29,990,000.00 USD | 349.34 USD | 0.00 USD | `+82.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `182.45` | 30,010,000.00 USD | 19,620.00 USD | 0.00 USD | `+82.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `183.45` | 30,560,000.00 USD | 550,350.00 USD | 0.00 USD | `+83.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `185.05` | 30,590,000.00 USD | 29,420.00 USD | 0.00 USD | `+85.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `187.05` | 30,780,000.00 USD | 190,560.00 USD | 0.00 USD | `+87.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `188.05` | 30,920,000.00 USD | 141,190.00 USD | 0.00 USD | `+88.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `190.05` | 30,960,000.00 USD | 38,120.00 USD | 0.00 USD | `+90.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `190.35` | 30,960,000.00 USD | 744.27 USD | 0.00 USD | `+90.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `194.05` | 30,960,000.00 USD | 4,270.00 USD | 0.00 USD | `+94.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `195.05` | 30,970,000.00 USD | 1,760.00 USD | 0.00 USD | `+95.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `196.05` | 31,220,000.00 USD | 253,390.00 USD | 0.00 USD | `+96.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `197.05` | 31,310,000.00 USD | 93,860.00 USD | 0.00 USD | `+97.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `197.15` | 31,310,000.00 USD | 181.38 USD | 0.00 USD | `+97.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `197.35` | 31,310,000.00 USD | 339.44 USD | 0.00 USD | `+97.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `198.05` | 31,670,000.00 USD | 353,030.00 USD | 0.00 USD | `+98.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `198.45` | 31,670,000.00 USD | 299.66 USD | 0.00 USD | `+98.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `198.75` | 31,690,000.00 USD | 20,110.00 USD | 0.00 USD | `+98.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `199.05` | 31,710,000.00 USD | 28,060.00 USD | 0.00 USD | `+99.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `199.15` | 31,710,000.00 USD | 189.19 USD | 0.00 USD | `+99.38%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `88.80` | 105,180,000.00 USD | 0.00 USD | 105,180,000.00 USD | 152,930.00 USD | 55,430.00 USD | 172,220.00 USD |
| `7D` | `88.80` | 237,080,000.00 USD | 0.00 USD | 237,080,000.00 USD | 17,470.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `89.00` | 104,800,000.00 USD | 0.00 USD | 104,800,000.00 USD | 8,600.00 USD | 2,360.00 USD | 2,750.00 USD |
| `7D` | `89.00` | 237,070,000.00 USD | 0.00 USD | 237,070,000.00 USD | 331,760.00 USD | 289,350.00 USD | 291,430.00 USD |
| `1D` | `89.20` | 104,780,000.00 USD | 0.00 USD | 104,780,000.00 USD | 166,240.00 USD | 99,310.00 USD | 0.00 USD |
| `7D` | `89.20` | 236,150,000.00 USD | 0.00 USD | 236,150,000.00 USD | 8,180.00 USD | 10,750.00 USD | 1,670.00 USD |
| `1D` | `89.40` | 104,520,000.00 USD | 0.00 USD | 104,520,000.00 USD | 12,630.00 USD | 48,770.00 USD | 137,540.00 USD |
| `7D` | `89.40` | 236,130,000.00 USD | 0.00 USD | 236,130,000.00 USD | 33,150.00 USD | 11,770.00 USD | 136,900.00 USD |
| `1D` | `89.60` | 104,320,000.00 USD | 0.00 USD | 104,320,000.00 USD | 557,950.00 USD | 163,120.00 USD | 315,640.00 USD |
| `7D` | `89.60` | 235,950,000.00 USD | 0.00 USD | 235,950,000.00 USD | 684,220.00 USD | 270,260.00 USD | 723,370.00 USD |
| `1D` | `89.80` | 103,280,000.00 USD | 0.00 USD | 103,280,000.00 USD | 532,910.00 USD | 381,520.00 USD | 197,340.00 USD |
| `7D` | `89.80` | 234,270,000.00 USD | 0.00 USD | 234,270,000.00 USD | 425,950.00 USD | 283,370.00 USD | 291,850.00 USD |
| `1D` | `90.00` | 102,170,000.00 USD | 0.00 USD | 102,170,000.00 USD | 412,230.00 USD | 479,230.00 USD | 454,010.00 USD |
| `7D` | `90.00` | 233,270,000.00 USD | 0.00 USD | 233,270,000.00 USD | 374,600.00 USD | 545,850.00 USD | 1,090,000.00 USD |
| `1D` | `90.20` | 100,820,000.00 USD | 0.00 USD | 100,820,000.00 USD | 489,160.00 USD | 406,910.00 USD | 432,190.00 USD |
| `7D` | `90.20` | 231,260,000.00 USD | 0.00 USD | 231,260,000.00 USD | 1,250,000.00 USD | 573,800.00 USD | 724,920.00 USD |
| `1D` | `90.40` | 99,500,000.00 USD | 0.00 USD | 99,500,000.00 USD | 505,770.00 USD | 339,750.00 USD | 509,430.00 USD |
| `7D` | `90.40` | 228,700,000.00 USD | 0.00 USD | 228,700,000.00 USD | 796,240.00 USD | 30,920.00 USD | 694,770.00 USD |
| `1D` | `90.60` | 98,140,000.00 USD | 0.00 USD | 98,140,000.00 USD | 270,180.00 USD | 392,650.00 USD | 477,510.00 USD |
| `7D` | `90.60` | 227,180,000.00 USD | 0.00 USD | 227,180,000.00 USD | 978,100.00 USD | 994,460.00 USD | 1,140,000.00 USD |
| `1D` | `90.80` | 97,000,000.00 USD | 0.00 USD | 97,000,000.00 USD | 106,320.00 USD | 101,660.00 USD | 1,720.00 USD |
| `7D` | `90.80` | 224,070,000.00 USD | 0.00 USD | 224,070,000.00 USD | 1,210,000.00 USD | 685,900.00 USD | 1,080,000.00 USD |
| `1D` | `91.00` | 96,790,000.00 USD | 0.00 USD | 96,790,000.00 USD | 57,100.00 USD | 882.42 USD | 129,600.00 USD |
| `7D` | `91.00` | 221,080,000.00 USD | 0.00 USD | 221,080,000.00 USD | 1,190,000.00 USD | 575,820.00 USD | 295,620.00 USD |
| `1D` | `91.20` | 96,600,000.00 USD | 0.00 USD | 96,600,000.00 USD | 27,610.00 USD | 769.97 USD | 307.73 USD |
| `7D` | `91.20` | 219,030,000.00 USD | 0.00 USD | 219,030,000.00 USD | 946,940.00 USD | 807,150.00 USD | 576,400.00 USD |
| `1D` | `91.40` | 96,570,000.00 USD | 0.00 USD | 96,570,000.00 USD | 3,800.00 USD | 125,680.00 USD | 43,950.00 USD |
| `7D` | `91.40` | 216,700,000.00 USD | 0.00 USD | 216,700,000.00 USD | 1,180,000.00 USD | 1,000,000.00 USD | 1,140,000.00 USD |
| `1D` | `91.60` | 96,400,000.00 USD | 0.00 USD | 96,400,000.00 USD | 25,530.00 USD | 96,080.00 USD | 1,680.00 USD |
| `7D` | `91.60` | 213,370,000.00 USD | 0.00 USD | 213,370,000.00 USD | 500,280.00 USD | 295,810.00 USD | 827,850.00 USD |
| `1D` | `91.80` | 96,280,000.00 USD | 0.00 USD | 96,280,000.00 USD | 229,430.00 USD | 103,030.00 USD | 11,420.00 USD |
| `7D` | `91.80` | 211,750,000.00 USD | 0.00 USD | 211,750,000.00 USD | 932,400.00 USD | 581,530.00 USD | 688,730.00 USD |
| `1D` | `92.00` | 95,930,000.00 USD | 0.00 USD | 95,930,000.00 USD | 137,240.00 USD | 74,290.00 USD | 90,460.00 USD |
| `7D` | `92.00` | 209,550,000.00 USD | 0.00 USD | 209,550,000.00 USD | 681,440.00 USD | 586,560.00 USD | 471,340.00 USD |
| `1D` | `92.20` | 95,630,000.00 USD | 0.00 USD | 95,630,000.00 USD | 153,400.00 USD | 41,040.00 USD | 107,850.00 USD |
| `7D` | `92.20` | 207,810,000.00 USD | 0.00 USD | 207,810,000.00 USD | 210,560.00 USD | 354,230.00 USD | 294,010.00 USD |
| `1D` | `92.40` | 95,330,000.00 USD | 0.00 USD | 95,330,000.00 USD | 132,350.00 USD | 68,900.00 USD | 687,260.00 USD |
| `7D` | `92.40` | 206,950,000.00 USD | 0.00 USD | 206,950,000.00 USD | 415,170.00 USD | 289,690.00 USD | 1,210,000.00 USD |
| `1D` | `92.60` | 94,440,000.00 USD | 0.00 USD | 94,440,000.00 USD | 31,270.00 USD | 66,860.00 USD | 45,700.00 USD |
| `7D` | `92.60` | 205,040,000.00 USD | 0.00 USD | 205,040,000.00 USD | 175,470.00 USD | 267,710.00 USD | 636,520.00 USD |
| `1D` | `92.80` | 94,300,000.00 USD | 0.00 USD | 94,300,000.00 USD | 0.00 USD | 0.00 USD | 97,110.00 USD |
| `7D` | `92.80` | 203,960,000.00 USD | 0.00 USD | 203,960,000.00 USD | 92,010.00 USD | 62,840.00 USD | 69,630.00 USD |
| `7D` | `93.00` | 203,730,000.00 USD | 0.00 USD | 203,730,000.00 USD | 0.00 USD | 109,950.00 USD | 281,490.00 USD |
| `7D` | `93.20` | 203,340,000.00 USD | 0.00 USD | 203,340,000.00 USD | 54,470.00 USD | 4,160.00 USD | 49,310.00 USD |
| `7D` | `93.40` | 203,230,000.00 USD | 0.00 USD | 203,230,000.00 USD | 11,220.00 USD | 2,430.00 USD | 1,290.00 USD |
| `7D` | `93.60` | 203,220,000.00 USD | 0.00 USD | 203,220,000.00 USD | 238,200.00 USD | 299,520.00 USD | 114,860.00 USD |
| `7D` | `93.80` | 202,560,000.00 USD | 0.00 USD | 202,560,000.00 USD | 281,530.00 USD | 179,760.00 USD | 91,440.00 USD |
| `7D` | `94.00` | 202,010,000.00 USD | 0.00 USD | 202,010,000.00 USD | 78,790.00 USD | 153,680.00 USD | 64,980.00 USD |
| `7D` | `94.20` | 201,710,000.00 USD | 0.00 USD | 201,710,000.00 USD | 172,550.00 USD | 229,720.00 USD | 258,370.00 USD |
| `7D` | `94.40` | 201,050,000.00 USD | 0.00 USD | 201,050,000.00 USD | 109,990.00 USD | 0.00 USD | 184,090.00 USD |
| `1D` | `94.60` | 94,200,000.00 USD | 0.00 USD | 94,200,000.00 USD | 30,840.00 USD | 4,870.00 USD | 964.12 USD |
| `7D` | `94.60` | 200,760,000.00 USD | 0.00 USD | 200,760,000.00 USD | 79,030.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `94.80` | 94,160,000.00 USD | 0.00 USD | 94,160,000.00 USD | 372,980.00 USD | 184,890.00 USD | 434,110.00 USD |
| `7D` | `94.80` | 200,680,000.00 USD | 0.00 USD | 200,680,000.00 USD | 227,730.00 USD | 19,890.00 USD | 8,930.00 USD |
| `1D` | `95.00` | 93,170,000.00 USD | 0.00 USD | 93,170,000.00 USD | 519,290.00 USD | 215,610.00 USD | 157,740.00 USD |
| `7D` | `95.00` | 200,420,000.00 USD | 0.00 USD | 200,420,000.00 USD | 950,030.00 USD | 816,510.00 USD | 726,790.00 USD |
| `1D` | `95.20` | 92,280,000.00 USD | 0.00 USD | 92,280,000.00 USD | 26,240.00 USD | 97,140.00 USD | 6,080.00 USD |
| `7D` | `95.20` | 197,930,000.00 USD | 0.00 USD | 197,930,000.00 USD | 47,840.00 USD | 200,720.00 USD | 138,220.00 USD |
| `1D` | `95.40` | 92,150,000.00 USD | 0.00 USD | 92,150,000.00 USD | 333,560.00 USD | 304,630.00 USD | 344,280.00 USD |
| `7D` | `95.40` | 197,540,000.00 USD | 0.00 USD | 197,540,000.00 USD | 866,300.00 USD | 239,410.00 USD | 1,380,000.00 USD |
| `1D` | `95.60` | 91,170,000.00 USD | 0.00 USD | 91,170,000.00 USD | 1,190,000.00 USD | 706,940.00 USD | 1,270,000.00 USD |
| `7D` | `95.60` | 195,060,000.00 USD | 0.00 USD | 195,060,000.00 USD | 1,740,000.00 USD | 1,320,000.00 USD | 986,050.00 USD |
| `1D` | `95.80` | 88,000,000.00 USD | 0.00 USD | 88,000,000.00 USD | 1,840,000.00 USD | 1,400,000.00 USD | 797,660.00 USD |
| `7D` | `95.80` | 191,010,000.00 USD | 0.00 USD | 191,010,000.00 USD | 1,910,000.00 USD | 1,030,000.00 USD | 1,330,000.00 USD |
| `1D` | `96.00` | 83,950,000.00 USD | 0.00 USD | 83,950,000.00 USD | 1,760,000.00 USD | 1,380,000.00 USD | 1,360,000.00 USD |
| `7D` | `96.00` | 186,740,000.00 USD | 0.00 USD | 186,740,000.00 USD | 1,870,000.00 USD | 2,140,000.00 USD | 3,170,000.00 USD |
| `1D` | `96.20` | 79,450,000.00 USD | 0.00 USD | 79,450,000.00 USD | 1,970,000.00 USD | 1,310,000.00 USD | 1,250,000.00 USD |
| `7D` | `96.20` | 179,560,000.00 USD | 0.00 USD | 179,560,000.00 USD | 3,950,000.00 USD | 2,080,000.00 USD | 2,580,000.00 USD |
| `1D` | `96.40` | 74,930,000.00 USD | 0.00 USD | 74,930,000.00 USD | 1,540,000.00 USD | 1,270,000.00 USD | 1,590,000.00 USD |
| `7D` | `96.40` | 170,950,000.00 USD | 0.00 USD | 170,950,000.00 USD | 3,260,000.00 USD | 643,110.00 USD | 2,910,000.00 USD |
| `1D` | `96.60` | 70,530,000.00 USD | 0.00 USD | 70,530,000.00 USD | 1,770,000.00 USD | 848,780.00 USD | 1,800,000.00 USD |
| `7D` | `96.60` | 164,140,000.00 USD | 0.00 USD | 164,140,000.00 USD | 3,250,000.00 USD | 2,480,000.00 USD | 2,380,000.00 USD |
| `1D` | `96.80` | 66,110,000.00 USD | 0.00 USD | 66,110,000.00 USD | 404,810.00 USD | 1,110,000.00 USD | 736,900.00 USD |
| `7D` | `96.80` | 156,040,000.00 USD | 0.00 USD | 156,040,000.00 USD | 3,460,000.00 USD | 2,780,000.00 USD | 2,960,000.00 USD |
| `1D` | `97.00` | 63,860,000.00 USD | 0.00 USD | 63,860,000.00 USD | 1,350,000.00 USD | 545,540.00 USD | 485,650.00 USD |
| `7D` | `97.00` | 146,840,000.00 USD | 0.00 USD | 146,840,000.00 USD | 6,570,000.00 USD | 3,100,000.00 USD | 3,470,000.00 USD |
| `1D` | `97.20` | 61,480,000.00 USD | 0.00 USD | 61,480,000.00 USD | 362,430.00 USD | 201,180.00 USD | 336,920.00 USD |
| `7D` | `97.20` | 133,700,000.00 USD | 0.00 USD | 133,700,000.00 USD | 5,490,000.00 USD | 4,350,000.00 USD | 3,980,000.00 USD |
| `1D` | `97.40` | 60,580,000.00 USD | 0.00 USD | 60,580,000.00 USD | 845,630.00 USD | 872,410.00 USD | 824,120.00 USD |
| `7D` | `97.40` | 119,880,000.00 USD | 0.00 USD | 119,880,000.00 USD | 5,010,000.00 USD | 2,440,000.00 USD | 4,890,000.00 USD |
| `1D` | `97.60` | 58,040,000.00 USD | 0.00 USD | 58,040,000.00 USD | 3,860,000.00 USD | 1,700,000.00 USD | 4,280,000.00 USD |
| `7D` | `97.60` | 107,550,000.00 USD | 0.00 USD | 107,550,000.00 USD | 5,190,000.00 USD | 5,230,000.00 USD | 4,930,000.00 USD |
| `1D` | `97.80` | 48,200,000.00 USD | 0.00 USD | 48,200,000.00 USD | 4,070,000.00 USD | 3,990,000.00 USD | 1,820,000.00 USD |
| `7D` | `97.80` | 92,200,000.00 USD | 0.00 USD | 92,200,000.00 USD | 6,520,000.00 USD | 2,970,000.00 USD | 4,790,000.00 USD |
| `1D` | `98.00` | 38,330,000.00 USD | 0.00 USD | 38,330,000.00 USD | 6,210,000.00 USD | 4,020,000.00 USD | 3,710,000.00 USD |
| `7D` | `98.00` | 77,930,000.00 USD | 0.00 USD | 77,930,000.00 USD | 11,060,000.00 USD | 9,600,000.00 USD | 11,560,000.00 USD |
| `1D` | `98.20` | 24,400,000.00 USD | 0.00 USD | 24,400,000.00 USD | 4,520,000.00 USD | 3,300,000.00 USD | 2,700,000.00 USD |
| `7D` | `98.20` | 45,700,000.00 USD | 0.00 USD | 45,700,000.00 USD | 9,810,000.00 USD | 6,890,000.00 USD | 6,860,000.00 USD |
| `1D` | `98.40` | 13,860,000.00 USD | 0.00 USD | 13,860,000.00 USD | 1,860,000.00 USD | 3,980,000.00 USD | 5,720,000.00 USD |
| `7D` | `98.40` | 22,140,000.00 USD | 0.00 USD | 22,140,000.00 USD | 5,610,000.00 USD | 2,860,000.00 USD | 13,520,000.00 USD |
| `1D` | `98.60` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 0.00 USD | 2,270,000.00 USD | 3,570.00 USD |
| `7D` | `98.60` | 148,390.00 USD | 0.00 USD | 148,390.00 USD | 0.00 USD | 0.00 USD | 62,960.00 USD |
| `1D` | `98.80` | 28,590.00 USD | 0.00 USD | 28,590.00 USD | 0.00 USD | 7,070.00 USD | 0.00 USD |
| `7D` | `98.80` | 85,430.00 USD | 0.00 USD | 85,430.00 USD | 0.00 USD | 0.00 USD | 85,430.00 USD |
| `1D` | `99.00` | 21,520.00 USD | 0.00 USD | 21,520.00 USD | 20,350.00 USD | 0.00 USD | 1,180.00 USD |
| `7D` | `99.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `99.10` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `99.20` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 0.00 USD | 3,380.00 USD | 3,590,000.00 USD |
| `7D` | `99.20` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 1,610,000.00 USD | 0.00 USD |
| `1D` | `99.40` | 6,410,000.00 USD | 6,410,000.00 USD | 0.00 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `99.40` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 599,290.00 USD | 0.00 USD |
| `1D` | `99.60` | 12,790,000.00 USD | 12,790,000.00 USD | 0.00 USD | 1,340,000.00 USD | 3,320,000.00 USD | 1,730,000.00 USD |
| `7D` | `99.60` | 4,120,000.00 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 1,900,000.00 USD | 6,720.00 USD |
| `1D` | `99.80` | 19,510,000.00 USD | 19,510,000.00 USD | 0.00 USD | 1,070,000.00 USD | 2,490,000.00 USD | 3,150,000.00 USD |
| `7D` | `99.80` | 5,350,000.00 USD | 5,350,000.00 USD | 0.00 USD | 736,270.00 USD | 490,550.00 USD | 2,210.00 USD |
| `1D` | `100.00` | 23,710,000.00 USD | 23,710,000.00 USD | 0.00 USD | 2,080,000.00 USD | 854,340.00 USD | 1,270,000.00 USD |
| `7D` | `100.00` | 11,500,000.00 USD | 11,500,000.00 USD | 0.00 USD | 2,170,000.00 USD | 1,140,000.00 USD | 2,840,000.00 USD |
| `1D` | `100.20` | 24,100,000.00 USD | 24,100,000.00 USD | 0.00 USD | 0.00 USD | 379,260.00 USD | 11,440.00 USD |
| `1D` | `100.40` | 25,910,000.00 USD | 25,910,000.00 USD | 0.00 USD | 0.00 USD | 453,740.00 USD | 1,350,000.00 USD |
| `7D` | `100.40` | 15,270,000.00 USD | 15,270,000.00 USD | 0.00 USD | 865,170.00 USD | 68,710.00 USD | 2,830,000.00 USD |
| `1D` | `100.60` | 32,870,000.00 USD | 32,870,000.00 USD | 0.00 USD | 1,850,000.00 USD | 177,410.00 USD | 4,940,000.00 USD |
| `7D` | `100.60` | 17,040,000.00 USD | 17,040,000.00 USD | 0.00 USD | 46,010.00 USD | 245,560.00 USD | 1,480,000.00 USD |
| `1D` | `100.80` | 35,230,000.00 USD | 35,230,000.00 USD | 0.00 USD | 860,830.00 USD | 1,490,000.00 USD | 9,630.00 USD |
| `7D` | `100.80` | 18,490,000.00 USD | 18,490,000.00 USD | 0.00 USD | 455,470.00 USD | 990,760.00 USD | 0.00 USD |
| `1D` | `101.00` | 46,100,000.00 USD | 46,100,000.00 USD | 0.00 USD | 7,780,000.00 USD | 2,250,000.00 USD | 834,730.00 USD |
| `7D` | `101.00` | 32,770,000.00 USD | 32,770,000.00 USD | 0.00 USD | 2,990,000.00 USD | 6,130,000.00 USD | 5,160,000.00 USD |
| `1D` | `101.20` | 62,980,000.00 USD | 62,980,000.00 USD | 0.00 USD | 5,910,000.00 USD | 6,900,000.00 USD | 4,060,000.00 USD |
| `7D` | `101.20` | 47,480,000.00 USD | 47,480,000.00 USD | 0.00 USD | 6,220,000.00 USD | 3,670,000.00 USD | 4,820,000.00 USD |
| `1D` | `101.40` | 70,940,000.00 USD | 70,940,000.00 USD | 0.00 USD | 3,390,000.00 USD | 1,950,000.00 USD | 2,630,000.00 USD |
| `7D` | `101.40` | 63,280,000.00 USD | 63,280,000.00 USD | 0.00 USD | 4,720,000.00 USD | 28,510.00 USD | 11,050,000.00 USD |
| `1D` | `101.60` | 90,980,000.00 USD | 90,980,000.00 USD | 0.00 USD | 5,190,000.00 USD | 2,550,000.00 USD | 12,290,000.00 USD |
| `7D` | `101.60` | 73,130,000.00 USD | 73,130,000.00 USD | 0.00 USD | 3,650,000.00 USD | 0.00 USD | 6,200,000.00 USD |
| `1D` | `101.80` | 97,980,000.00 USD | 97,980,000.00 USD | 0.00 USD | 483,810.00 USD | 304,910.00 USD | 6,210,000.00 USD |
| `7D` | `101.80` | 82,550,000.00 USD | 82,550,000.00 USD | 0.00 USD | 3,050,000.00 USD | 453,970.00 USD | 5,920,000.00 USD |
| `1D` | `102.00` | 102,370,000.00 USD | 102,370,000.00 USD | 0.00 USD | 2,230,000.00 USD | 873,740.00 USD | 1,290,000.00 USD |
| `7D` | `102.00` | 86,710,000.00 USD | 86,710,000.00 USD | 0.00 USD | 1,810,000.00 USD | 503,680.00 USD | 1,840,000.00 USD |
| `1D` | `102.20` | 109,200,000.00 USD | 109,200,000.00 USD | 0.00 USD | 3,030,000.00 USD | 1,390,000.00 USD | 2,410,000.00 USD |
| `7D` | `102.20` | 93,410,000.00 USD | 93,410,000.00 USD | 0.00 USD | 2,390,000.00 USD | 803,220.00 USD | 3,520,000.00 USD |
| `1D` | `102.40` | 113,730,000.00 USD | 113,730,000.00 USD | 0.00 USD | 1,390,000.00 USD | 574,230.00 USD | 2,560,000.00 USD |
| `7D` | `102.40` | 98,120,000.00 USD | 98,120,000.00 USD | 0.00 USD | 1,760,000.00 USD | 299,640.00 USD | 2,650,000.00 USD |
| `1D` | `102.60` | 115,130,000.00 USD | 115,130,000.00 USD | 0.00 USD | 641,030.00 USD | 324,340.00 USD | 439,980.00 USD |
| `7D` | `102.60` | 100,590,000.00 USD | 100,590,000.00 USD | 0.00 USD | 1,450,000.00 USD | 979,270.00 USD | 37,570.00 USD |
| `1D` | `102.80` | 119,050,000.00 USD | 119,050,000.00 USD | 0.00 USD | 1,430,000.00 USD | 1,920,000.00 USD | 566,670.00 USD |
| `7D` | `102.80` | 108,650,000.00 USD | 108,650,000.00 USD | 0.00 USD | 7,780,000.00 USD | 4,830.00 USD | 277,920.00 USD |
| `1D` | `103.00` | 124,320,000.00 USD | 124,320,000.00 USD | 0.00 USD | 3,120,000.00 USD | 1,640,000.00 USD | 498,100.00 USD |
| `7D` | `103.00` | 124,710,000.00 USD | 124,710,000.00 USD | 0.00 USD | 12,220,000.00 USD | 284,250.00 USD | 3,550,000.00 USD |
| `1D` | `103.20` | 129,760,000.00 USD | 129,760,000.00 USD | 0.00 USD | 1,850,000.00 USD | 1,760,000.00 USD | 1,820,000.00 USD |
| `7D` | `103.20` | 138,310,000.00 USD | 138,310,000.00 USD | 0.00 USD | 12,970,000.00 USD | 4,380.00 USD | 631,060.00 USD |
| `1D` | `103.40` | 137,450,000.00 USD | 137,450,000.00 USD | 0.00 USD | 3,930,000.00 USD | 1,900,000.00 USD | 1,860,000.00 USD |
| `7D` | `103.40` | 154,270,000.00 USD | 154,270,000.00 USD | 0.00 USD | 12,450,000.00 USD | 233,330.00 USD | 3,280,000.00 USD |
| `1D` | `103.60` | 151,230,000.00 USD | 151,230,000.00 USD | 0.00 USD | 4,540,000.00 USD | 1,840,000.00 USD | 7,410,000.00 USD |
| `7D` | `103.60` | 172,660,000.00 USD | 172,660,000.00 USD | 0.00 USD | 11,460,000.00 USD | 1,720,000.00 USD | 5,210,000.00 USD |
| `1D` | `103.80` | 160,650,000.00 USD | 160,650,000.00 USD | 0.00 USD | 3,210,000.00 USD | 2,770,000.00 USD | 3,430,000.00 USD |
| `7D` | `103.80` | 185,050,000.00 USD | 185,050,000.00 USD | 0.00 USD | 7,960,000.00 USD | 1,880,000.00 USD | 2,550,000.00 USD |
| `1D` | `104.00` | 170,220,000.00 USD | 170,220,000.00 USD | 0.00 USD | 3,550,000.00 USD | 2,800,000.00 USD | 3,220,000.00 USD |
| `7D` | `104.00` | 214,200,000.00 USD | 214,200,000.00 USD | 0.00 USD | 11,880,000.00 USD | 7,160,000.00 USD | 10,110,000.00 USD |
| `1D` | `104.20` | 176,960,000.00 USD | 176,960,000.00 USD | 0.00 USD | 2,710,000.00 USD | 2,180,000.00 USD | 1,850,000.00 USD |
| `7D` | `104.20` | 236,010,000.00 USD | 236,010,000.00 USD | 0.00 USD | 8,520,000.00 USD | 7,010,000.00 USD | 6,280,000.00 USD |
| `1D` | `104.40` | 184,450,000.00 USD | 184,450,000.00 USD | 0.00 USD | 3,300,000.00 USD | 1,930,000.00 USD | 2,260,000.00 USD |
| `7D` | `104.40` | 252,990,000.00 USD | 252,990,000.00 USD | 0.00 USD | 5,100,000.00 USD | 3,700,000.00 USD | 8,170,000.00 USD |
| `1D` | `104.60` | 190,360,000.00 USD | 190,360,000.00 USD | 0.00 USD | 1,800,000.00 USD | 1,200,000.00 USD | 2,920,000.00 USD |
| `7D` | `104.60` | 270,550,000.00 USD | 270,550,000.00 USD | 0.00 USD | 7,180,000.00 USD | 3,550,000.00 USD | 6,830,000.00 USD |
| `1D` | `104.80` | 195,370,000.00 USD | 195,370,000.00 USD | 0.00 USD | 1,460,000.00 USD | 972,490.00 USD | 2,580,000.00 USD |
| `7D` | `104.80` | 287,680,000.00 USD | 287,680,000.00 USD | 0.00 USD | 5,170,000.00 USD | 4,150,000.00 USD | 7,820,000.00 USD |
| `1D` | `105.00` | 197,310,000.00 USD | 197,310,000.00 USD | 0.00 USD | 708,730.00 USD | 483,120.00 USD | 746,730.00 USD |
| `7D` | `105.00` | 304,810,000.00 USD | 304,810,000.00 USD | 0.00 USD | 5,730,000.00 USD | 5,070,000.00 USD | 6,330,000.00 USD |
| `1D` | `105.20` | 198,360,000.00 USD | 198,360,000.00 USD | 0.00 USD | 237,100.00 USD | 4,110.00 USD | 809,550.00 USD |
| `7D` | `105.20` | 317,520,000.00 USD | 317,520,000.00 USD | 0.00 USD | 5,340,000.00 USD | 4,850,000.00 USD | 2,530,000.00 USD |
| `1D` | `105.40` | 198,440,000.00 USD | 198,440,000.00 USD | 0.00 USD | 72,850.00 USD | 2,770.00 USD | 769.33 USD |
| `7D` | `105.40` | 329,470,000.00 USD | 329,470,000.00 USD | 0.00 USD | 2,960,000.00 USD | 4,450,000.00 USD | 4,540,000.00 USD |
| `1D` | `105.60` | 199,020,000.00 USD | 199,020,000.00 USD | 0.00 USD | 178,510.00 USD | 263,160.00 USD | 135,560.00 USD |
| `7D` | `105.60` | 346,690,000.00 USD | 346,690,000.00 USD | 0.00 USD | 5,650,000.00 USD | 5,760,000.00 USD | 5,810,000.00 USD |
| `1D` | `105.80` | 199,450,000.00 USD | 199,450,000.00 USD | 0.00 USD | 132,310.00 USD | 285,640.00 USD | 19,250.00 USD |
| `7D` | `105.80` | 357,450,000.00 USD | 357,450,000.00 USD | 0.00 USD | 3,540,000.00 USD | 3,020,000.00 USD | 4,200,000.00 USD |
| `1D` | `106.00` | 200,510,000.00 USD | 200,510,000.00 USD | 0.00 USD | 377,210.00 USD | 456,530.00 USD | 222,920.00 USD |
| `7D` | `106.00` | 367,430,000.00 USD | 367,430,000.00 USD | 0.00 USD | 4,000,000.00 USD | 2,430,000.00 USD | 3,550,000.00 USD |
| `1D` | `106.20` | 201,910,000.00 USD | 201,910,000.00 USD | 0.00 USD | 606,390.00 USD | 420,460.00 USD | 375,050.00 USD |
| `7D` | `106.20` | 381,580,000.00 USD | 381,580,000.00 USD | 0.00 USD | 6,780,000.00 USD | 3,540,000.00 USD | 3,830,000.00 USD |
| `1D` | `106.40` | 203,020,000.00 USD | 203,020,000.00 USD | 0.00 USD | 583,540.00 USD | 313,010.00 USD | 207,870.00 USD |
| `7D` | `106.40` | 389,120,000.00 USD | 389,120,000.00 USD | 0.00 USD | 3,240,000.00 USD | 2,670,000.00 USD | 1,630,000.00 USD |
| `1D` | `106.60` | 205,520,000.00 USD | 205,520,000.00 USD | 0.00 USD | 872,810.00 USD | 432,260.00 USD | 1,200,000.00 USD |
| `7D` | `106.60` | 398,190,000.00 USD | 398,190,000.00 USD | 0.00 USD | 2,470,000.00 USD | 2,230,000.00 USD | 4,380,000.00 USD |
| `1D` | `106.80` | 207,130,000.00 USD | 207,130,000.00 USD | 0.00 USD | 565,520.00 USD | 117,240.00 USD | 924,150.00 USD |
| `7D` | `106.80` | 404,080,000.00 USD | 404,080,000.00 USD | 0.00 USD | 1,340,000.00 USD | 1,750,000.00 USD | 2,800,000.00 USD |
| `1D` | `107.00` | 207,800,000.00 USD | 207,800,000.00 USD | 0.00 USD | 199,140.00 USD | 184,400.00 USD | 288,270.00 USD |
| `7D` | `107.00` | 409,640,000.00 USD | 409,640,000.00 USD | 0.00 USD | 1,370,000.00 USD | 1,260,000.00 USD | 2,930,000.00 USD |
| `1D` | `107.20` | 208,040,000.00 USD | 208,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 242,780.00 USD |
| `7D` | `107.20` | 411,360,000.00 USD | 411,360,000.00 USD | 0.00 USD | 866,170.00 USD | 389,810.00 USD | 461,600.00 USD |
| `7D` | `107.40` | 412,340,000.00 USD | 412,340,000.00 USD | 0.00 USD | 0.00 USD | 280,650.00 USD | 703,710.00 USD |
| `7D` | `107.60` | 412,710,000.00 USD | 412,710,000.00 USD | 0.00 USD | 213,520.00 USD | 0.00 USD | 154,920.00 USD |
| `7D` | `107.80` | 413,490,000.00 USD | 413,490,000.00 USD | 0.00 USD | 489,650.00 USD | 10,400.00 USD | 277,390.00 USD |
| `7D` | `108.00` | 413,520,000.00 USD | 413,520,000.00 USD | 0.00 USD | 25,580.00 USD | 6,070.00 USD | 5,560.00 USD |
| `7D` | `108.20` | 415,640,000.00 USD | 415,640,000.00 USD | 0.00 USD | 860,420.00 USD | 826,850.00 USD | 427,140.00 USD |
| `1D` | `108.40` | 208,060,000.00 USD | 208,060,000.00 USD | 0.00 USD | 12,330.00 USD | 1,950.00 USD | 0.00 USD |
| `7D` | `108.40` | 417,720,000.00 USD | 417,720,000.00 USD | 0.00 USD | 1,140,000.00 USD | 528,370.00 USD | 411,030.00 USD |
| `1D` | `108.60` | 208,420,000.00 USD | 208,420,000.00 USD | 0.00 USD | 140,590.00 USD | 53,480.00 USD | 172,220.00 USD |
| `7D` | `108.60` | 418,980,000.00 USD | 418,980,000.00 USD | 0.00 USD | 412,330.00 USD | 515,740.00 USD | 332,360.00 USD |
| `1D` | `108.80` | 208,440,000.00 USD | 208,440,000.00 USD | 0.00 USD | 8,600.00 USD | 2,360.00 USD | 2,750.00 USD |
| `7D` | `108.80` | 422,210,000.00 USD | 422,210,000.00 USD | 0.00 USD | 840,500.00 USD | 1,250,000.00 USD | 1,140,000.00 USD |
| `1D` | `109.00` | 208,700,000.00 USD | 208,700,000.00 USD | 0.00 USD | 166,240.00 USD | 99,310.00 USD | 0.00 USD |
| `7D` | `109.00` | 422,750,000.00 USD | 422,750,000.00 USD | 0.00 USD | 248,800.00 USD | 112,280.00 USD | 176,770.00 USD |
| `1D` | `109.20` | 208,900,000.00 USD | 208,900,000.00 USD | 0.00 USD | 12,630.00 USD | 48,770.00 USD | 137,540.00 USD |
| `7D` | `109.20` | 423,990,000.00 USD | 423,990,000.00 USD | 0.00 USD | 613,010.00 USD | 87,870.00 USD | 544,580.00 USD |
| `1D` | `109.40` | 209,040,000.00 USD | 209,040,000.00 USD | 0.00 USD | 123,410.00 USD | 7,590.00 USD | 2,610.00 USD |
| `7D` | `109.40` | 424,610,000.00 USD | 424,610,000.00 USD | 0.00 USD | 158,460.00 USD | 81,870.00 USD | 375,580.00 USD |
| `1D` | `109.60` | 209,940,000.00 USD | 209,940,000.00 USD | 0.00 USD | 434,540.00 USD | 155,520.00 USD | 313,030.00 USD |
| `7D` | `109.60` | 425,670,000.00 USD | 425,670,000.00 USD | 0.00 USD | 525,760.00 USD | 188,400.00 USD | 347,790.00 USD |
| `1D` | `109.80` | 211,050,000.00 USD | 211,050,000.00 USD | 0.00 USD | 532,910.00 USD | 381,520.00 USD | 197,340.00 USD |
| `7D` | `109.80` | 426,670,000.00 USD | 426,670,000.00 USD | 0.00 USD | 425,950.00 USD | 283,370.00 USD | 291,850.00 USD |
| `1D` | `110.00` | 212,400,000.00 USD | 212,400,000.00 USD | 0.00 USD | 412,230.00 USD | 479,230.00 USD | 454,010.00 USD |
| `7D` | `110.00` | 428,690,000.00 USD | 428,690,000.00 USD | 0.00 USD | 374,600.00 USD | 545,850.00 USD | 1,090,000.00 USD |
| `1D` | `110.20` | 213,730,000.00 USD | 213,730,000.00 USD | 0.00 USD | 489,160.00 USD | 406,910.00 USD | 432,190.00 USD |
| `7D` | `110.20` | 431,240,000.00 USD | 431,240,000.00 USD | 0.00 USD | 1,250,000.00 USD | 573,800.00 USD | 724,920.00 USD |
| `1D` | `110.40` | 215,080,000.00 USD | 215,080,000.00 USD | 0.00 USD | 505,770.00 USD | 339,750.00 USD | 509,430.00 USD |
| `7D` | `110.40` | 432,760,000.00 USD | 432,760,000.00 USD | 0.00 USD | 796,240.00 USD | 30,920.00 USD | 694,770.00 USD |
| `1D` | `110.60` | 215,540,000.00 USD | 215,540,000.00 USD | 0.00 USD | 110,850.00 USD | 104,840.00 USD | 240,140.00 USD |
| `7D` | `110.60` | 433,860,000.00 USD | 433,860,000.00 USD | 0.00 USD | 506,360.00 USD | 293,650.00 USD | 301,670.00 USD |
| `1D` | `110.80` | 216,220,000.00 USD | 216,220,000.00 USD | 0.00 USD | 159,320.00 USD | 287,810.00 USD | 237,370.00 USD |
| `7D` | `110.80` | 435,880,000.00 USD | 435,880,000.00 USD | 0.00 USD | 471,740.00 USD | 700,800.00 USD | 841,270.00 USD |
| `1D` | `111.00` | 216,430,000.00 USD | 216,430,000.00 USD | 0.00 USD | 106,320.00 USD | 101,660.00 USD | 1,720.00 USD |
| `7D` | `111.00` | 438,860,000.00 USD | 438,860,000.00 USD | 0.00 USD | 1,210,000.00 USD | 685,900.00 USD | 1,080,000.00 USD |
| `1D` | `111.20` | 216,620,000.00 USD | 216,620,000.00 USD | 0.00 USD | 57,100.00 USD | 882.42 USD | 129,600.00 USD |
| `7D` | `111.20` | 440,920,000.00 USD | 440,920,000.00 USD | 0.00 USD | 1,190,000.00 USD | 575,820.00 USD | 295,620.00 USD |
| `1D` | `111.40` | 216,650,000.00 USD | 216,650,000.00 USD | 0.00 USD | 27,610.00 USD | 769.97 USD | 307.73 USD |
| `7D` | `111.40` | 443,250,000.00 USD | 443,250,000.00 USD | 0.00 USD | 946,940.00 USD | 807,150.00 USD | 576,400.00 USD |
| `1D` | `111.60` | 216,770,000.00 USD | 216,770,000.00 USD | 0.00 USD | 0.00 USD | 77,530.00 USD | 42,830.00 USD |
| `7D` | `111.60` | 444,200,000.00 USD | 444,200,000.00 USD | 0.00 USD | 662,880.00 USD | 172,700.00 USD | 122,050.00 USD |
| `7D` | `111.80` | 446,570,000.00 USD | 446,570,000.00 USD | 0.00 USD | 515,920.00 USD | 829,010.00 USD | 1,020,000.00 USD |
| `7D` | `112.00` | 448,190,000.00 USD | 448,190,000.00 USD | 0.00 USD | 500,280.00 USD | 295,810.00 USD | 827,850.00 USD |
| `7D` | `112.20` | 450,400,000.00 USD | 450,400,000.00 USD | 0.00 USD | 932,400.00 USD | 581,530.00 USD | 688,730.00 USD |
| `7D` | `112.40` | 452,130,000.00 USD | 452,130,000.00 USD | 0.00 USD | 681,440.00 USD | 586,560.00 USD | 471,340.00 USD |
| `7D` | `112.60` | 452,990,000.00 USD | 452,990,000.00 USD | 0.00 USD | 210,560.00 USD | 354,230.00 USD | 294,010.00 USD |
| `7D` | `112.80` | 453,870,000.00 USD | 453,870,000.00 USD | 0.00 USD | 207,390.00 USD | 162,590.00 USD | 505,740.00 USD |
| `7D` | `113.00` | 454,910,000.00 USD | 454,910,000.00 USD | 0.00 USD | 207,780.00 USD | 127,100.00 USD | 702,160.00 USD |
| `7D` | `113.20` | 455,990,000.00 USD | 455,990,000.00 USD | 0.00 USD | 175,470.00 USD | 267,710.00 USD | 636,520.00 USD |
| `7D` | `113.40` | 456,210,000.00 USD | 456,210,000.00 USD | 0.00 USD | 92,010.00 USD | 62,840.00 USD | 69,630.00 USD |
| `7D` | `113.60` | 456,600,000.00 USD | 456,600,000.00 USD | 0.00 USD | 0.00 USD | 109,950.00 USD | 281,490.00 USD |
| `7D` | `113.80` | 456,600,000.00 USD | 456,600,000.00 USD | 0.00 USD | 2,370.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `114.00` | 456,700,000.00 USD | 456,700,000.00 USD | 0.00 USD | 48,760.00 USD | 0.00 USD | 49,310.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `6.21B` | Total OI Tokens: `62,736,628.1 SOL`
  * 1h OI Change: `-0.02%` | 4h OI Change: `-2.73%` | 24h OI Change: `-2.75%`
  * Exchange Breakdown: Binance=`1.09B` | Bybit=`623.50M` | OKX=`352.97M` | Hyperliquid=`562.49M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `174.29K` | Last 24h: `361.48K` | Last 3d: `1.27M` | Last 7d: `2.42M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0065%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0018%` | **USDT Bitget** | `0.0099%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `SOL` | `43.87%` | `56.13%` | `0.78` | 140,120,000.00 USD |
| `15M` | `Binance` | `44.83%` | `55.17%` | `0.81` | 49,130,000.00 USD |
| `15M` | `OKX` | `44.49%` | `55.51%` | `0.80` | 19,580,000.00 USD |
| `15M` | `Bybit` | `37.59%` | `62.41%` | `0.60` | 18,750,000.00 USD |
| `15M` | `KuCoin` | `40.02%` | `59.98%` | `0.67` | 2,210,000.00 USD |
| `15M` | `Gate` | `46.44%` | `53.56%` | `0.87` | 4,250,000.00 USD |
| `15M` | `Bitget` | `37.27%` | `62.73%` | `0.59` | 10,680,000.00 USD |
| `15M` | `BingX` | `47.37%` | `52.63%` | `0.90` | 2,470,000.00 USD |
| `15M` | `MEXC` | `53.92%` | `46.08%` | `1.17` | 16,230,000.00 USD |
| `15M` | `Bitunix` | `44.49%` | `55.51%` | `0.80` | 7,470,000.00 USD |
| `15M` | `Hyperliquid` | `32.87%` | `67.13%` | `0.49` | 4,730,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `51.23%` | `48.77%` | `1.05` | 503,620.00 USD |
| `15M` | `Crypto.com` | `41.94%` | `58.06%` | `0.72` | 191,940.00 USD |
| `15M` | `WhiteBIT` | `17.6%` | `82.4%` | `0.21` | 1,330,000.00 USD |
| `15M` | `HTX` | `42.6%` | `57.4%` | `0.74` | 101,490.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `59.57%` | `40.43%` | `1.47` | 734,280.00 USD |
| `15M` | `Aster` | `44.81%` | `55.19%` | `0.81` | 1,580,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `41.47%` | `58.53%` | `0.71` | 188,170.00 USD |
| `15M` | `Whale Positions` | `44.83%` | `55.17%` | `0.81` | 49,130,000.00 USD |
| `15M` | `Global Accounts` | `43.87%` | `56.13%` | `0.78` | 140,120,000.00 USD |
| `1H` | `SOL` | `44.73%` | `55.27%` | `0.81` | 693,650,000.00 USD |
| `1H` | `Binance` | `45.61%` | `54.39%` | `0.84` | 237,530,000.00 USD |
| `1H` | `OKX` | `44.74%` | `55.26%` | `0.81` | 94,020,000.00 USD |
| `1H` | `Bybit` | `36.79%` | `63.21%` | `0.58` | 90,760,000.00 USD |
| `1H` | `KuCoin` | `41.91%` | `58.09%` | `0.72` | 4,130,000.00 USD |
| `1H` | `Gate` | `48.54%` | `51.46%` | `0.94` | 47,380,000.00 USD |
| `1H` | `Bitget` | `38.76%` | `61.24%` | `0.63` | 31,380,000.00 USD |
| `1H` | `BingX` | `49.59%` | `50.41%` | `0.98` | 28,330,000.00 USD |
| `1H` | `MEXC` | `54.79%` | `45.21%` | `1.21` | 55,430,000.00 USD |
| `1H` | `Bitunix` | `43.14%` | `56.86%` | `0.76` | 37,440,000.00 USD |
| `1H` | `Hyperliquid` | `38.06%` | `61.94%` | `0.61` | 19,370,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `55.19%` | `44.81%` | `1.23` | 8,360,000.00 USD |
| `1H` | `Crypto.com` | `45.59%` | `54.41%` | `0.84` | 1,690,000.00 USD |
| `1H` | `WhiteBIT` | `28.34%` | `71.66%` | `0.40` | 5,030,000.00 USD |
| `1H` | `HTX` | `38.93%` | `61.07%` | `0.64` | 571,350.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `52.3%` | `47.7%` | `1.10` | 6,620,000.00 USD |
| `1H` | `Aster` | `45.57%` | `54.43%` | `0.84` | 5,950,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `43.02%` | `56.98%` | `0.76` | 19,640,000.00 USD |
| `1H` | `Whale Positions` | `45.61%` | `54.39%` | `0.84` | 237,530,000.00 USD |
| `1H` | `Global Accounts` | `44.73%` | `55.27%` | `0.81` | 693,650,000.00 USD |
| `4H` | `SOL` | `44.49%` | `55.51%` | `0.80` | 610,710,000.00 USD |
| `4H` | `Binance` | `45.04%` | `54.96%` | `0.82` | 204,910,000.00 USD |
| `4H` | `OKX` | `43.14%` | `56.86%` | `0.76` | 66,460,000.00 USD |
| `4H` | `Bybit` | `38.44%` | `61.56%` | `0.62` | 83,800,000.00 USD |
| `4H` | `KuCoin` | `43.2%` | `56.8%` | `0.76` | 6,390,000.00 USD |
| `4H` | `Gate` | `48.32%` | `51.68%` | `0.93` | 26,950,000.00 USD |
| `4H` | `Bitget` | `39.5%` | `60.5%` | `0.65` | 43,740,000.00 USD |
| `4H` | `BingX` | `51.27%` | `48.73%` | `1.05` | 16,190,000.00 USD |
| `4H` | `MEXC` | `53.32%` | `46.68%` | `1.14` | 73,940,000.00 USD |
| `4H` | `Bitunix` | `46.14%` | `53.86%` | `0.86` | 35,570,000.00 USD |
| `4H` | `Hyperliquid` | `36.81%` | `63.19%` | `0.58` | 11,930,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `52.54%` | `47.46%` | `1.11` | 2,530,000.00 USD |
| `4H` | `Crypto.com` | `45.83%` | `54.17%` | `0.85` | 879,650.00 USD |
| `4H` | `WhiteBIT` | `14.73%` | `85.27%` | `0.17` | 25,610,000.00 USD |
| `4H` | `HTX` | `36.13%` | `63.87%` | `0.57` | 535,700.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `44.02%` | `55.98%` | `0.79` | 3,450,000.00 USD |
| `4H` | `Aster` | `42.23%` | `57.77%` | `0.73` | 7,150,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `40.9%` | `59.1%` | `0.69` | 692,960.00 USD |
| `4H` | `Whale Positions` | `45.04%` | `54.96%` | `0.82` | 204,910,000.00 USD |
| `4H` | `Global Accounts` | `44.49%` | `55.51%` | `0.80` | 610,710,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `100.91` | `100.89` | `100.91` | `101.13` | `100.72` | 21,682,501.47 USD | 10,212,926.11 USD | 11,469,575.36 USD | -1,256,649.25 USD | `-5.80%` | `6B / 4S` |
| `0:00 UTC` | `101.07` | `101.03` | `101.07` | `101.19` | `100.90` | 11,845,890.84 USD | 5,647,320.15 USD | 6,198,570.68 USD | -551,250.53 USD | `-4.65%` | `2B / 1S` |
| `5:00 UTC` | `100.81` | `100.98` | `100.81` | `101.18` | `100.75` | 7,681,327.85 USD | 3,539,960.94 USD | 4,141,366.91 USD | -601,405.98 USD | `-7.83%` | `5B / 12S` |
| `0:00 UTC` | `100.38` | `100.47` | `100.38` | `100.81` | `100.30` | 26,755,803.01 USD | 9,721,488.50 USD | 17,034,314.50 USD | -7,312,826.00 USD | `-27.33%` | `0B / 21S` |
| `5:00 UTC` | `100.66` | `100.58` | `100.66` | `100.78` | `100.34` | 9,618,082.62 USD | 5,517,082.05 USD | 4,101,000.56 USD | 1,416,081.49 USD | `+14.72%` | `9B / 2S` |
| `0:00 UTC` | `100.38` | `100.40` | `100.38` | `100.62` | `100.25` | 9,521,682.83 USD | 4,738,635.78 USD | 4,783,047.06 USD | -44,411.28 USD | `-0.47%` | `0B / 7S` |
| `5:00 UTC` | `100.31` | `100.27` | `100.31` | `100.43` | `100.16` | 10,974,925.19 USD | 4,852,550.33 USD | 6,122,374.86 USD | -1,269,824.53 USD | `-11.57%` | `4B / 3S` |
| `0:00 UTC` | `100.10` | `100.18` | `100.10` | `100.38` | `100.09` | 16,033,450.26 USD | 8,994,633.57 USD | 7,038,816.68 USD | 1,955,816.89 USD | `+12.20%` | `5B / 2S` |
| `5:00 UTC` | `100.00` | `99.98` | `100.00` | `100.22` | `99.77` | 31,495,982.01 USD | 14,749,838.13 USD | 16,746,143.88 USD | -1,996,305.75 USD | `-6.34%` | `7B / 6S` |
| `0:00 UTC` | `99.50` | `99.07` | `99.50` | `99.91` | `98.34` | 114,746,491.70 USD | 44,262,158.82 USD | 70,484,332.88 USD | -26,222,174.06 USD | `-22.85%` | `5B / 20S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 18:37` | `Volume 500K SOL` | `Divergence` | **`BULLISH`** | Drop without taker selling | `101.13` | 0.00 USD | 0.00 USD |
| `10-28 17:45` | `Volume 500K SOL` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `101.76` | 0.00 USD | 0.00 USD |
| `10-28 15:32` | `Volume 500K SOL` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `102.87` | 99,000.00 USD | 0.00 USD |
| `10-28 13:57` | `Volume 500K SOL` | `Divergence` | **`BULLISH`** | Drop without taker selling | `102.88` | 0.00 USD | 0.00 USD |
| `10-28 13:30` | `Volume 500K SOL` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `102.22` | 103,000.00 USD | 0.00 USD |
| `10-28 10:59` | `Volume 500K SOL` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `101.76` | 110,000.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 3,120,000.00 USD | 9,690,000.00 USD | **`ACCUMULATION`** |
| `15m` | -5,120,000.00 USD | -69,180,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -3,810,000.00 USD | -68,490,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -2,110,000.00 USD | -69,920,000.00 USD | **`DISTRIBUTION`** |
| `2h` | 217,990.00 USD | -80,510,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -6,190,000.00 USD | -140,440,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 10,200,000.00 USD | -96,670,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 14,690,000.00 USD | -136,240,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 23,350,000.00 USD | -128,080,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 22,030,000.00 USD | -196,870,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 87,660,000.00 USD | -368,840,000.00 USD | **`DISTRIBUTION`** |
| `30d` | 62,860,000.00 USD | -1,940,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+3.12M` | 15m=`-5.12M` | 1h=`-2.11M` | 24h=`+22.03M`
* Futures Capital Netflows: 5m=`+9.69M` | 15m=`-69.18M` | 1h=`-69.92M` | 24h=`-196.87M`
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
  * `2026-10-30 01:36:09 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:09 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:50:09 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:50:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:51:09 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:51:09 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:51:09 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:51:09 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:51:09 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 20:51:09 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `99.04` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `98.11` (Risk Distance: `0.9349` pts)
  * +2.5R Take Profit: `101.38`
  * Mathematical Lot Sizing: **`10.69 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `101.20` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `102.13` (Risk Distance: `0.9349` pts)
  * +2.5R Take Profit: `98.86`
  * Mathematical Lot Sizing: **`10.69 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`99.69`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
