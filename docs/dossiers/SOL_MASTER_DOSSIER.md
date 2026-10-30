# 🏛️ SOVEREIGN CANDIDATE DOSSIER: SOL
**Canonical Key**: `SOL` | **Broker Instrument**: `SOLUSD.p` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 11:32:22 IST` (`2026-10-30 06:02:22 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `97.75` | **Live Ask Quote**: `97.98` | **Mid Price**: `97.87`
- **Spread Points**: `23.00` | **Spread BPS**: `23.50 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `94.99` | VWAP Z-Score: `+2.05` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.7569` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `67.11` (State: `OVERBOUGHT`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `99.46` | Lower -3.00σ Band: `90.51`
  * Upper +2.51σ Band: `98.73` | Lower -2.51σ Band: `91.24`
  * Upper +2.01σ Band: `97.98` | Lower -2.01σ Band: `91.99`
  * Upper +2.00σ Band: `97.97` | Lower -2.00σ Band: `92.00`
  * Upper +1.28σ Band: `96.89` | Lower -1.28σ Band: `93.08`
  * Upper +1.00σ Band: `96.48` | Lower -1.00σ Band: `93.49`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`97.05` | EMA-20=`96.45` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`97.02` (Slope: `+0.0000`) | EMA-100=`98.18`
  * Institutional Anchors: EMA-144=`98.76` | EMA-200=`99.22` (Slope: `-0.3190`) | EMA-233=`99.47`
- **Range Boundaries**: 24H High=`102.93` | 24H Low=`91.86` | Weekly High=`103.63` | Weekly Low=`91.86`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `97.70` (Distance: `+0.13%`)
  * Point of Control (POC) = `96.85` (Distance: `+1.02%`)
  * Value Area Low (VAL) = `94.45` (Distance: `+3.58%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`101.56` | POC=`99.94` | VAL=`98.94`
  * Prior Day Extremes: PDH=`102.93` | PDL=`94.56` | PDC=`95.94`
  * Monday Range Blueprint: High=`102.46` | Mid=`101.01` | Low=`99.56`
  * Developing Weekly Value Area: Weekly VAH=`101.86` | Weekly POC=`100.92` | Weekly VAL=`99.51`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`97.84` | Low=`91.86`
  * London Session (08:00-16:00 UTC): High=`98.28` | Low=`96.72`
  * New York Session (13:00-21:00 UTC): High=`98.45` | Low=`97.28`
  * Initial Balance (First Hour): IB High=`98.28` | IB Low=`96.72`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `97.47` - `98.26`
  * Optimal Trade Entry (OTE 0.705): `98.06`
  * Structural Invalidation Anchor (0.786): `98.65`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `98.01` | `98.30` | `97.88` | `98.09` | `96,600` | 9,477,121.37 USD | -443,670.24 USD | `-4.68%` | -201,802,264.63 USD | `-0.33` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `98.10` | `98.29` | `98.09` | `98.16` | `51,393` | 5,047,222.23 USD | -608,586.12 USD | `-12.06%` | -202,410,850.75 USD | `-0.39` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `98.16` | `98.33` | `98.07` | `98.27` | `33,773` | 3,315,967.23 USD | -384,064.21 USD | `-11.58%` | -202,794,914.97 USD | `-0.25` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `97.22` | `97.99` | `97.20` | `97.72` | `270,319` | 26,397,725.61 USD | 1,683,999.43 USD | `+6.38%` | -199,923,812.78 USD | `+0.49` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `97.71` | `98.06` | `97.67` | `98.02` | `162,341` | 15,892,962.27 USD | -1,434,781.61 USD | `-9.03%` | -201,358,594.39 USD | `-0.45` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `98.01` | `98.33` | `97.88` | `98.27` | `181,766` | 17,840,310.84 USD | -1,436,320.58 USD | `-8.05%` | -202,794,914.97 USD | `-0.59` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `95.37` | `97.23` | `95.32` | `97.19` | `1,022,478` | 98,533,717.92 USD | 8,813,441.74 USD | `+8.94%` | -198,203,367.78 USD | `+0.99` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `97.20` | `97.61` | `96.72` | `97.23` | `802,986` | 78,022,251.46 USD | -722,046.52 USD | `-0.93%` | -198,925,414.30 USD | `+0.50` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `97.22` | `98.33` | `97.20` | `98.27` | `614,426` | 60,130,998.72 USD | -1,187,102.76 USD | `-1.97%` | -200,112,517.05 USD | `+0.49` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `99.78` | `99.90` | `94.81` | `95.62` | `13,887,188` | 1,349,343,315.53 USD | -115,873,425.65 USD | `-8.59%` | -153,967,489.63 USD | `-1.67` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `95.62` | `97.23` | `92.25` | `97.19` | `7,753,327` | 731,973,529.17 USD | -43,261,246.83 USD | `-5.91%` | -197,228,736.47 USD | `-0.09` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `97.20` | `98.33` | `96.72` | `98.27` | `1,417,411` | 138,153,250.18 USD | -1,909,149.27 USD | `-1.38%` | -199,137,885.74 USD | `+0.78` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `100.34` | `102.70` | `100.03` | `102.66` | `4,178,003` | 423,242,147.26 USD | -1,557,927.33 USD | `-0.37%` | -5,851,281.21 USD | `+1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `102.66` | `103.16` | `99.76` | `99.78` | `3,108,106` | 314,906,395.99 USD | -32,242,782.78 USD | `-10.24%` | -38,094,063.99 USD | `-1.41` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `99.78` | `99.90` | `94.81` | `95.62` | `13,887,188` | 1,349,343,315.53 USD | -115,873,425.65 USD | `-8.59%` | -153,967,489.63 USD | `-1.67` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `95.62` | `97.23` | `92.25` | `97.19` | `7,753,327` | 731,973,529.17 USD | -43,261,246.83 USD | `-5.91%` | -197,228,736.47 USD | `-0.09` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `97.20` | `98.54` | `96.72` | `98.01` | `1,564,700` | 152,626,312.80 USD | -4,103,194.06 USD | `-2.69%` | -201,331,930.52 USD | `+0.74` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| --- | **`97.87`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `97.96` | `40.8300` | 3,999.87 USD | 226,124.82 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `97.96` | `40.8300` | 3,999.83 USD | 230,124.65 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `97.97` | `40.8200` | 3,999.34 USD | 91,466.41 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `97.97` | `40.8200` | 3,999.30 USD | 95,465.71 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `97.97` | `50.8200` | 4,978.99 USD | 100,444.70 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `97.97` | `40.8200` | 3,999.22 USD | 104,443.91 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `97.97` | `87.2000` | 8,543.07 USD | 112,986.99 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `97.97` | `40.8200` | 3,999.14 USD | 116,986.12 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `97.97` | `330.5900` | 32,387.57 USD | 149,373.69 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `97.97` | `249.9800` | 24,490.04 USD | 173,863.73 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `97.97` | `267.6600` | 26,221.85 USD | 200,085.58 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `97.97` | `184.1400` | 18,039.46 USD | 218,125.04 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `97.97` | `40.8300` | 3,999.91 USD | 222,124.95 USD | `1 orders` | `-0.02%` | `-` |
| `ASK` | `97.98` | `769.7600` | 75,424.93 USD | 75,424.93 USD | `6 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `97.98` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 97.98` | `0.00%` | `-` |
| `BID` | `97.98` | `326.1600` | 31,958.46 USD | 31,958.46 USD | `7 orders` | `-0.00%` | `-` |
| `BID` | `97.98` | `40.8200` | 3,999.67 USD | 35,958.13 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `97.98` | `40.9400` | 4,011.34 USD | 39,969.47 USD | `2 orders` | `-0.00%` | `-` |
| `BID` | `97.98` | `158.1900` | 15,499.46 USD | 55,468.93 USD | `3 orders` | `-0.00%` | `-` |
| `BID` | `97.98` | `40.8200` | 3,999.50 USD | 59,468.43 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `97.98` | `40.8200` | 3,999.42 USD | 63,467.85 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `97.98` | `244.9500` | 23,999.22 USD | 87,467.07 USD | `2 orders` | `-0.01%` | `-` |
| `ASK` | `97.99` | `133.3900` | 13,071.42 USD | 114,154.46 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `97.99` | `133.3900` | 13,071.29 USD | 101,083.04 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `97.99` | `128.4500` | 12,586.82 USD | 88,011.75 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `98.00` | `52.9100` | 5,185.44 USD | 150,322.86 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `98.00` | `7.6500` | 749.73 USD | 145,137.42 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `98.00` | `133.4000` | 13,073.47 USD | 144,387.69 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `98.00` | `142.7400` | 13,988.52 USD | 131,314.22 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `98.00` | `32.3600` | 3,171.25 USD | 117,325.70 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `98.01` | `19.1200` | 1,874.03 USD | 252,237.22 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `98.01` | `315.7400` | 30,946.62 USD | 250,363.19 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `98.01` | `10.0000` | 980.12 USD | 219,416.57 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `98.01` | `58.2800` | 5,712.08 USD | 218,436.45 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `98.01` | `154.1600` | 15,109.22 USD | 212,724.37 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `98.01` | `482.5300` | 47,292.28 USD | 197,615.15 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `98.02` | `46.8000` | 4,587.48 USD | 468,069.92 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `98.02` | `38.9600` | 3,818.86 USD | 463,482.44 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `98.02` | `1898.7100` | 186,107.76 USD | 459,663.58 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `98.02` | `171.5900` | 16,818.74 USD | 273,555.83 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `98.02` | `45.9100` | 4,499.87 USD | 256,737.09 USD | `1 orders` | `+0.03%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:24:14 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `11` | `0x5b5d...c060` | `SHORT` | 68,198,193.02 USD | `696,120.13` | `94.33` | `98.02` | `328.75` | -2,529,926.80 USD | `-3.71%` | `7X Cross` |
| `19` | `0x9c6a...a4ed` | `LONG` | 53,891,540.90 USD | `550,087.69` | `80.86` | `98.02` | `68.18` | 9,412,554.51 USD | `+17.47%` | `20X Cross` |
| `49` | `0xb83d...6e36` | `SHORT` | 25,406,049.13 USD | `259,338.02` | `91.42` | `98.02` | `612.91` | -1,697,235.09 USD | `-6.68%` | `5X Cross` |
| `80` | `0x3dc9...54b0` | `SHORT` | 21,563,098.62 USD | `220,000.19` | `105.90` | `98.02` | `173.77` | 1,736,008.65 USD | `+8.05%` | `20X Cross` |
| `110` | `0x9c89...600e` | `LONG` | 18,562,886.09 USD | `189,472.50` | `115.21` | `98.02` | `34.96` | -3,266,129.17 USD | `-17.59%` | `20X Cross` |
| `119` | `0x4a20...3c26` | `LONG` | 17,629,740.00 USD | `180,000.00` | `106.43` | `98.02` | `69.01` | -1,528,538.71 USD | `-8.67%` | `20X Cross` |
| `161` | `0xecb6...2b00` | `SHORT` | 12,831,507.71 USD | `130,915.05` | `101.34` | `98.02` | `333.13` | 434,977.54 USD | `+3.39%` | `20X Cross` |
| `223` | `0xb581...6f4f` | `LONG` | 9,797,400.00 USD | `100,000.00` | `112.81` | `98.02` | `0.000000` | -1,483,309.14 USD | `-15.14%` | `3X Cross` |
| `224` | `0xc63a...a3cd` | `LONG` | 9,791,600.00 USD | `100,000.00` | `112.22` | `98.02` | `0.000000` | -1,430,508.97 USD | `-14.61%` | `20X Cross` |
| `288` | `0x645b...87b8` | `SHORT` | 8,123,396.40 USD | `82,879.96` | `103.90` | `98.02` | `358.00` | 488,073.82 USD | `+6.01%` | `20X Cross` |
| `294` | `0xdb3a...cf3b` | `LONG` | 8,018,609.63 USD | `81,851.78` | `106.04` | `98.02` | `44.95` | -661,137.23 USD | `-8.25%` | `4X Cross` |
| `308` | `0xe927...98ef` | `LONG` | 7,642,050.00 USD | `78,000.00` | `96.34` | `98.02` | `38.45` | 127,908.52 USD | `+1.67%` | `3X Cross` |
| `316` | `0xca49...53c8` | `SHORT` | 7,244,831.34 USD | `73,943.45` | `110.70` | `98.02` | `297.29` | 940,790.92 USD | `+12.99%` | `20X Cross` |
| `323` | `0x8ae4...3d60` | `LONG` | 7,071,580.55 USD | `72,180.05` | `111.72` | `98.02` | `10.60` | -992,579.69 USD | `-14.04%` | `10X Cross` |
| `328` | `0xa0b7...6165` | `SHORT` | 6,960,321.29 USD | `71,044.42` | `107.87` | `98.02` | `190.91` | 703,145.91 USD | `+10.10%` | `2X Cross` |
| `344` | `0xf517...c032` | `SHORT` | 6,639,923.69 USD | `67,778.53` | `84.64` | `98.02` | `224.39` | -902,892.53 USD | `-13.60%` | `20X Cross` |
| `357` | `0x7a5a...0394` | `SHORT` | 6,464,664.31 USD | `65,989.53` | `99.29` | `98.02` | `125.38` | 87,176.88 USD | `+1.35%` | `10X Cross` |
| `404` | `0x7fda...17d1` | `SHORT` | 5,503,895.10 USD | `56,182.26` | `100.54` | `98.02` | `770.48` | 144,776.77 USD | `+2.63%` | `20X Cross` |
| `463` | `0x7e23...5a5a` | `LONG` | 4,757,627.12 USD | `48,564.56` | `105.17` | `98.02` | `57.00` | -349,942.04 USD | `-7.36%` | `5X Isolated` |
| `563` | `0xf899...88db` | `SHORT` | 3,989,082.88 USD | `40,716.81` | `88.40` | `98.02` | `117.23` | -389,810.01 USD | `-9.77%` | `20X Cross` |
| `580` | `0x2e2b...2fab` | `LONG` | 3,918,600.00 USD | `40,000.00` | `119.55` | `98.02` | `58.63` | -863,435.64 USD | `-22.03%` | `10X Cross` |
| `610` | `0x9c16...4a6f` | `SHORT` | 3,700,845.87 USD | `37,796.13` | `90.79` | `98.02` | `118.13` | -269,495.14 USD | `-7.28%` | `20X Cross` |
| `636` | `0x27b8...12fc` | `LONG` | 3,535,824.17 USD | `36,085.73` | `110.86` | `98.02` | `22.51` | -464,521.09 USD | `-13.14%` | `10X Cross` |
| `643` | `0x9946...0852` | `SHORT` | 3,486,400.32 USD | `35,590.04` | `111.00` | `98.02` | `140.63` | 464,186.43 USD | `+13.31%` | `20X Cross` |
| `652` | `0x3440...32c5` | `SHORT` | 3,445,455.50 USD | `35,170.27` | `95.02` | `98.02` | `160.93` | -103,532.45 USD | `-3.00%` | `20X Cross` |
| `665` | `0xa61c...66b9` | `LONG` | 3,373,793.12 USD | `34,438.76` | `102.78` | `98.02` | `0.000000` | -165,668.19 USD | `-4.91%` | `5X Cross` |
| `727` | `0x96a7...79df` | `LONG` | 3,135,008.00 USD | `32,000.00` | `74.39` | `98.02` | `0.000000` | 754,602.15 USD | `+24.07%` | `20X Cross` |
| `770` | `0xbe19...8bd1` | `SHORT` | 2,982,529.87 USD | `30,451.69` | `97.62` | `98.02` | `756.63` | -9,983.24 USD | `-0.33%` | `3X Cross` |
| `773` | `0x482b...cae4` | `SHORT` | 2,968,700.32 USD | `30,310.49` | `88.03` | `98.02` | `154.53` | -300,452.03 USD | `-10.12%` | `20X Cross` |
| `775` | `0x023a...2355` | `SHORT` | 2,962,310.45 USD | `30,223.34` | `101.18` | `98.02` | `269.87` | 95,561.69 USD | `+3.23%` | `20X Cross` |
| `783` | `0x610b...b613` | `LONG` | 2,903,404.87 USD | `29,634.14` | `101.23` | `98.02` | `70.40` | -96,594.48 USD | `-3.33%` | `3X Isolated` |
| `794` | `0x45d2...4029` | `SHORT` | 2,861,894.46 USD | `29,220.00` | `93.28` | `98.02` | `1539.67` | -136,118.48 USD | `-4.76%` | `20X Cross` |
| `844` | `0x458d...ab3b` | `LONG` | 2,682,949.73 USD | `27,385.03` | `117.17` | `98.02` | `81.08` | -525,712.79 USD | `-19.59%` | `3X Isolated` |
| `914` | `0x051c...693c` | `LONG` | 2,462,911.27 USD | `25,139.70` | `89.76` | `98.02` | `41.07` | 206,349.94 USD | `+8.38%` | `20X Cross` |
| `932` | `0xfc27...9d9d` | `SHORT` | 2,403,728.29 USD | `24,528.09` | `100.40` | `98.02` | `824.49` | 58,784.85 USD | `+2.45%` | `20X Cross` |
| `950` | `0x638f...f5f0` | `LONG` | 2,350,560.00 USD | `24,000.00` | `136.71` | `98.02` | `49.52` | -930,408.54 USD | `-39.58%` | `20X Cross` |
| `998` | `0x7277...0b98` | `SHORT` | 2,230,280.13 USD | `22,770.74` | `99.32` | `98.02` | `157.28` | 31,323.63 USD | `+1.40%` | `20X Cross` |
| `1003` | `0x7178...0854` | `LONG` | 2,208,734.62 USD | `22,545.24` | `110.94` | `98.02` | `38.50` | -292,409.86 USD | `-13.24%` | `10X Cross` |
| `1021` | `0x69cc...14fd` | `SHORT` | 2,125,885.80 USD | `21,701.57` | `99.01` | `98.02` | `466.80` | 22,766.95 USD | `+1.07%` | `20X Cross` |
| `1028` | `0x739c...cfb2` | `LONG` | 2,107,301.00 USD | `21,500.00` | `91.95` | `98.02` | `73.87` | 130,368.85 USD | `+6.19%` | `20X Cross` |
| `1094` | `0x7737...bf66` | `SHORT` | 1,997,005.97 USD | `20,384.06` | `102.94` | `98.02` | `949.34` | 101,335.92 USD | `+5.07%` | `10X Cross` |
| `1128` | `0xea00...a918` | `LONG` | 1,961,723.05 USD | `20,022.69` | `66.09` | `98.02` | `0.000000` | 638,414.45 USD | `+32.54%` | `20X Cross` |
| `1131` | `0x3fc5...c0c1` | `SHORT` | 1,959,980.00 USD | `20,000.00` | `98.28` | `98.02` | `179.91` | 5,579.84 USD | `+0.28%` | `20X Cross` |
| `1132` | `0xbfc7...80b4` | `SHORT` | 1,959,480.00 USD | `20,000.00` | `85.98` | `98.02` | `174.31` | -239,945.50 USD | `-12.25%` | `20X Cross` |
| `1133` | `0x251f...6e5d` | `LONG` | 1,959,300.00 USD | `20,000.00` | `101.15` | `98.02` | `66.54` | -63,797.77 USD | `-3.26%` | `20X Cross` |
| `1147` | `0x936c...bb0f` | `SHORT` | 1,927,351.22 USD | `19,664.04` | `105.57` | `98.02` | `511.07` | 148,610.96 USD | `+7.71%` | `20X Cross` |
| `1164` | `0x7160...d47c` | `LONG` | 1,903,861.61 USD | `19,434.10` | `105.03` | `98.02` | `75.39` | -137,359.68 USD | `-7.21%` | `20X Cross` |
| `1187` | `0xe097...d0fe` | `LONG` | 1,860,006.85 USD | `18,995.75` | `109.71` | `98.02` | `0.000000` | -223,990.04 USD | `-12.04%` | `20X Cross` |
| `1266` | `0xdf95...7d72` | `SHORT` | 1,744,635.04 USD | `17,802.58` | `104.53` | `98.02` | `2263.32` | 116,321.82 USD | `+6.67%` | `20X Cross` |
| `1276` | `0xe98b...8cd5` | `SHORT` | 1,726,539.21 USD | `17,622.89` | `187.95` | `98.02` | `262.21` | 1,585,681.52 USD | `+91.84%` | `20X Cross` |
| `1307` | `0xee2b...d67e` | `LONG` | 1,661,798.91 USD | `16,963.19` | `119.86` | `98.02` | `31.34` | -371,472.73 USD | `-22.35%` | `4X Cross` |
| `1309` | `0x123d...3bff` | `LONG` | 1,657,621.68 USD | `16,920.55` | `89.54` | `98.02` | `0.000000` | 142,627.93 USD | `+8.60%` | `10X Cross` |
| `1411` | `0x73d7...8be1` | `LONG` | 1,534,240.91 USD | `15,668.95` | `106.60` | `98.02` | `48.18` | -136,100.05 USD | `-8.87%` | `20X Cross` |
| `1425` | `0xc74a...ab93` | `LONG` | 1,522,126.72 USD | `15,536.82` | `64.06` | `98.02` | `54.89` | 526,897.88 USD | `+34.62%` | `5X Isolated` |
| `1472` | `0xb322...d51f` | `LONG` | 1,469,457.37 USD | `14,999.82` | `102.98` | `98.02` | `44.29` | -75,269.94 USD | `-5.12%` | `20X Cross` |
| `1473` | `0x5f10...d49d` | `LONG` | 1,469,145.00 USD | `15,000.00` | `96.35` | `98.02` | `70.98` | 23,843.84 USD | `+1.62%` | `20X Cross` |
| `1512` | `0xffb2...5ed6` | `LONG` | 1,421,019.79 USD | `14,504.05` | `117.89` | `98.02` | `85.31` | -288,884.92 USD | `-20.33%` | `20X Cross` |
| `1538` | `0x0d6a...ca57` | `LONG` | 1,391,754.47 USD | `14,206.65` | `110.41` | `98.02` | `91.60` | -176,835.89 USD | `-12.71%` | `5X Isolated` |
| `1744` | `0x5323...b23c` | `LONG` | 1,182,111.29 USD | `12,069.38` | `94.78` | `98.02` | `0.000000` | 38,171.92 USD | `+3.23%` | `5X Cross` |
| `1746` | `0x2814...9b08` | `LONG` | 1,181,034.40 USD | `12,061.71` | `96.37` | `98.02` | `93.93` | 18,695.65 USD | `+1.58%` | `20X Isolated` |
| `1823` | `0x7808...6e70` | `SHORT` | 1,125,521.90 USD | `11,488.27` | `97.15` | `98.02` | `151.23` | -9,459.68 USD | `-0.84%` | `10X Cross` |
| `1847` | `0x2482...0e55` | `LONG` | 1,113,272.30 USD | `11,363.98` | `122.03` | `98.02` | `88.83` | -273,429.62 USD | `-24.56%` | `20X Isolated` |
| `1878` | `0x45db...86eb` | `LONG` | 1,086,989.70 USD | `11,100.00` | `110.69` | `98.02` | `68.87` | -141,692.20 USD | `-13.04%` | `5X Cross` |
| `1901` | `0x1d04...7c43` | `LONG` | 1,059,243.26 USD | `10,811.76` | `111.55` | `98.02` | `16.64` | -146,818.23 USD | `-13.86%` | `6X Cross` |
| `1922` | `0x34e6...8d74` | `LONG` | 1,045,132.43 USD | `10,671.15` | `101.19` | `98.02` | `15.56` | -34,642.21 USD | `-3.31%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `99.41` | 140,129.08 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 140.13K USD at 99.4070 USD [API] | `2026-10-29 02:34:37` |
| `ANNOUNCEMENT` | `INFO` | `99.94` | 10,810.73 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 10.81K USD at 99.9420 USD [API] | `2026-10-29 01:49:05` |
| `ANNOUNCEMENT` | `INFO` | `99.94` | 88.95 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.09K USD at 99.9420 USD [API] | `2026-10-29 01:49:05` |
| `ANNOUNCEMENT` | `INFO` | `99.94` | 461.73 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.46K USD at 99.9420 USD [API] | `2026-10-29 01:49:05` |
| `ANNOUNCEMENT` | `INFO` | `99.94` | 1,731.99 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 1.73K USD at 99.9420 USD [API] | `2026-10-29 01:49:05` |
| `ANNOUNCEMENT` | `INFO` | `99.94` | 277.84 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.28K USD at 99.9420 USD [API] | `2026-10-29 01:49:05` |
| `ANNOUNCEMENT` | `INFO` | `99.94` | 11.99 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.01K USD at 99.9420 USD [API] | `2026-10-29 01:49:05` |
| `ANNOUNCEMENT` | `INFO` | `99.94` | 138.92 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.14K USD at 99.9420 USD [API] | `2026-10-29 01:49:05` |
| `ANNOUNCEMENT` | `INFO` | `99.94` | 3,773.81 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 3.77K USD at 99.9420 USD [API] | `2026-10-29 01:49:05` |
| `ANNOUNCEMENT` | `INFO` | `99.94` | 55.97 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.06K USD at 99.9420 USD [API] | `2026-10-29 01:49:05` |
| `ANNOUNCEMENT` | `INFO` | `99.94` | 36,008.10 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 36.01K USD at 99.9420 USD [API] | `2026-10-29 01:49:05` |
| `ANNOUNCEMENT` | `INFO` | `99.94` | 55.97 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.06K USD at 99.9420 USD [API] | `2026-10-29 01:49:05` |
| `ANNOUNCEMENT` | `INFO` | `99.94` | 1,439.16 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 1.44K USD at 99.9420 USD [API] | `2026-10-29 01:49:05` |
| `ANNOUNCEMENT` | `INFO` | `99.94` | 1,490.14 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 1.49K USD at 99.9420 USD [API] | `2026-10-29 01:49:05` |
| `ANNOUNCEMENT` | `INFO` | `99.94` | 321.81 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.32K USD at 99.9420 USD [API] | `2026-10-29 01:49:05` |
| `ANNOUNCEMENT` | `INFO` | `99.94` | 11.99 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.01K USD at 99.9420 USD [API] | `2026-10-29 01:49:05` |
| `ANNOUNCEMENT` | `INFO` | `100.06` | 23,677.20 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 23.68K USD at 100.0600 USD [API] | `2026-10-29 03:04:30` |
| `ANNOUNCEMENT` | `INFO` | `99.53` | 20.90 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.02K USD at 99.5350 USD [API] | `2026-10-29 02:05:43` |
| `ANNOUNCEMENT` | `INFO` | `99.53` | 91.57 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.09K USD at 99.5350 USD [API] | `2026-10-29 02:05:43` |
| `ANNOUNCEMENT` | `INFO` | `100.16` | 308.49 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.31K USD at 100.1600 USD [API] | `2026-10-29 01:48:26` |
| `ANNOUNCEMENT` | `INFO` | `100.14` | 1,574.20 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 1.57K USD at 100.1400 USD [API] | `2026-10-29 01:48:20` |
| `ANNOUNCEMENT` | `INFO` | `100.14` | 573.80 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.57K USD at 100.1400 USD [API] | `2026-10-29 01:48:20` |
| `ANNOUNCEMENT` | `INFO` | `100.14` | 2,545.56 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 2.55K USD at 100.1400 USD [API] | `2026-10-29 01:48:20` |
| `ANNOUNCEMENT` | `INFO` | `100.14` | 80.11 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.08K USD at 100.1400 USD [API] | `2026-10-29 01:48:20` |
| `ANNOUNCEMENT` | `INFO` | `100.86` | 2,586.05 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 2.59K USD at 100.8600 USD [API] | `2026-10-29 01:39:05` |
| `ANNOUNCEMENT` | `INFO` | `100.87` | 7,662.09 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 7.66K USD at 100.8700 USD [API] | `2026-10-29 01:39:05` |
| `ANNOUNCEMENT` | `INFO` | `100.96` | 6,720.91 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 6.72K USD at 100.9600 USD [API] | `2026-10-29 01:38:38` |
| `ANNOUNCEMENT` | `INFO` | `99.59` | 22,830.16 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 22.83K USD at 99.5950 USD [API] | `2026-10-29 03:39:17` |
| `ANNOUNCEMENT` | `INFO` | `66.74` | 98,718.18 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 98.72K USD at 66.7380 USD [API] | `2026-06-04 02:04:51` |
| `ANNOUNCEMENT` | `INFO` | `66.74` | 99,453.95 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 99.45K USD at 66.7400 USD [API] | `2026-06-04 02:04:51` |
| `ANNOUNCEMENT` | `INFO` | `66.74` | 96.11 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.10K USD at 66.7430 USD [API] | `2026-06-04 02:04:51` |
| `ANNOUNCEMENT` | `INFO` | `66.75` | 99,461.40 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 99.46K USD at 66.7450 USD [API] | `2026-06-04 02:04:51` |
| `ANNOUNCEMENT` | `INFO` | `66.75` | 166.87 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.17K USD at 66.7470 USD [API] | `2026-06-04 02:04:51` |
| `ANNOUNCEMENT` | `INFO` | `66.75` | 84,833.31 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 84.83K USD at 66.7490 USD [API] | `2026-06-04 02:04:51` |
| `ANNOUNCEMENT` | `INFO` | `67.08` | 14,650.93 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 14.65K USD at 67.0830 USD [API] | `2026-06-04 02:04:33` |
| `ANNOUNCEMENT` | `INFO` | `67.08` | 663.45 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.66K USD at 67.0830 USD [API] | `2026-06-04 02:04:33` |
| `ANNOUNCEMENT` | `INFO` | `67.08` | 663.46 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.66K USD at 67.0840 USD [API] | `2026-06-04 02:04:33` |
| `ANNOUNCEMENT` | `INFO` | `67.09` | 663.48 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.66K USD at 67.0860 USD [API] | `2026-06-04 02:04:33` |
| `ANNOUNCEMENT` | `INFO` | `67.09` | 663.50 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.66K USD at 67.0880 USD [API] | `2026-06-04 02:04:33` |
| `ANNOUNCEMENT` | `INFO` | `67.10` | 78,887.80 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 78.89K USD at 67.1020 USD [API] | `2026-06-04 02:04:33` |
| `ANNOUNCEMENT` | `INFO` | `67.54` | 2,413.20 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.41K USD at 67.5400 USD [API] | `2026-06-04 02:03:30` |
| `ANNOUNCEMENT` | `INFO` | `67.54` | 40,031.47 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 40.03K USD at 67.5420 USD [API] | `2026-06-04 02:03:30` |
| `ANNOUNCEMENT` | `INFO` | `67.54` | 664.62 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.66K USD at 67.5430 USD [API] | `2026-06-04 02:03:30` |
| `ANNOUNCEMENT` | `INFO` | `67.54` | 664.63 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.66K USD at 67.5440 USD [API] | `2026-06-04 02:03:30` |
| `ANNOUNCEMENT` | `INFO` | `67.55` | 1,253.64 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.25K USD at 67.5450 USD [API] | `2026-06-04 02:03:30` |
| `ANNOUNCEMENT` | `INFO` | `67.55` | 664.65 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.66K USD at 67.5460 USD [API] | `2026-06-04 02:03:30` |
| `ANNOUNCEMENT` | `INFO` | `67.55` | 5,844.43 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 5.84K USD at 67.5500 USD [API] | `2026-06-04 02:03:30` |
| `ANNOUNCEMENT` | `INFO` | `67.56` | 1,375.42 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.38K USD at 67.5550 USD [API] | `2026-06-04 02:03:30` |
| `ANNOUNCEMENT` | `INFO` | `67.57` | 262.85 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.26K USD at 67.5710 USD [API] | `2026-06-04 02:03:30` |
| `ANNOUNCEMENT` | `INFO` | `67.57` | 67,890.61 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 67.89K USD at 67.5710 USD [API] | `2026-06-04 02:03:30` |
| `ANNOUNCEMENT` | `INFO` | `67.92` | 3,330.26 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 3.33K USD at 67.9230 USD [API] | `2026-06-04 02:02:23` |
| `ANNOUNCEMENT` | `INFO` | `67.93` | 180.69 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.18K USD at 67.9270 USD [API] | `2026-06-04 02:02:23` |
| `ANNOUNCEMENT` | `INFO` | `67.93` | 96,159.56 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 96.16K USD at 67.9280 USD [API] | `2026-06-04 02:02:23` |
| `ANNOUNCEMENT` | `INFO` | `67.93` | 2,249.94 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.25K USD at 67.9330 USD [API] | `2026-06-04 02:02:23` |
| `ANNOUNCEMENT` | `INFO` | `67.93` | 49.59 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.05K USD at 67.9330 USD [API] | `2026-06-04 02:02:23` |
| `ANNOUNCEMENT` | `INFO` | `67.94` | 578.84 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.58K USD at 67.9390 USD [API] | `2026-06-04 02:02:23` |
| `ANNOUNCEMENT` | `INFO` | `67.94` | 416.49 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.42K USD at 67.9430 USD [API] | `2026-06-04 02:02:23` |
| `ANNOUNCEMENT` | `INFO` | `67.95` | 299.66 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.30K USD at 67.9500 USD [API] | `2026-06-04 02:02:23` |
| `ANNOUNCEMENT` | `INFO` | `67.95` | 11.55 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.01K USD at 67.9500 USD [API] | `2026-06-04 02:02:23` |
| `ANNOUNCEMENT` | `INFO` | `67.95` | 42.81 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.04K USD at 67.9500 USD [API] | `2026-06-04 02:02:23` |
| `ANNOUNCEMENT` | `INFO` | `67.95` | 1,161.98 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.16K USD at 67.9520 USD [API] | `2026-06-04 02:02:23` |
| `ANNOUNCEMENT` | `INFO` | `67.96` | 1,130.17 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.13K USD at 67.9600 USD [API] | `2026-06-04 02:02:23` |
| `ANNOUNCEMENT` | `INFO` | `67.96` | 19.71 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.02K USD at 67.9600 USD [API] | `2026-06-04 02:02:23` |
| `ANNOUNCEMENT` | `INFO` | `67.97` | 21.75 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.02K USD at 67.9700 USD [API] | `2026-06-04 02:02:23` |
| `ANNOUNCEMENT` | `INFO` | `67.97` | 377.91 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.38K USD at 67.9700 USD [API] | `2026-06-04 02:02:23` |
| `ANNOUNCEMENT` | `INFO` | `67.97` | 2,011.94 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.01K USD at 67.9710 USD [API] | `2026-06-04 02:02:23` |
| `ANNOUNCEMENT` | `INFO` | `67.98` | 1,137.24 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.14K USD at 67.9760 USD [API] | `2026-06-04 02:02:23` |
| `ANNOUNCEMENT` | `INFO` | `67.98` | 67.98 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.07K USD at 67.9800 USD [API] | `2026-06-04 02:02:23` |
| `ANNOUNCEMENT` | `INFO` | `67.99` | 190.36 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.19K USD at 67.9860 USD [API] | `2026-06-04 02:02:23` |
| `ANNOUNCEMENT` | `INFO` | `67.99` | 42,760.47 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 42.76K USD at 67.9860 USD [API] | `2026-06-04 02:02:23` |
| `ANNOUNCEMENT` | `INFO` | `68.41` | 3,761.65 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 3.76K USD at 68.4060 USD [API] | `2026-06-04 01:55:01` |
| `ANNOUNCEMENT` | `INFO` | `68.41` | 119,176.62 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 119.18K USD at 68.4070 USD [API] | `2026-06-04 01:55:01` |
| `ANNOUNCEMENT` | `INFO` | `68.41` | 19,940.93 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 19.94K USD at 68.4080 USD [API] | `2026-06-04 01:55:01` |
| `ANNOUNCEMENT` | `INFO` | `68.41` | 5,615.78 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 5.62K USD at 68.4100 USD [API] | `2026-06-04 01:55:01` |
| `ANNOUNCEMENT` | `INFO` | `68.41` | 15.05 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.02K USD at 68.4110 USD [API] | `2026-06-04 01:55:01` |
| `ANNOUNCEMENT` | `INFO` | `68.41` | 4,623.28 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 4.62K USD at 68.4120 USD [API] | `2026-06-04 01:55:01` |
| `ANNOUNCEMENT` | `INFO` | `68.41` | 410.48 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.41K USD at 68.4140 USD [API] | `2026-06-04 01:55:01` |
| `ANNOUNCEMENT` | `INFO` | `68.41` | 15.05 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.02K USD at 68.4140 USD [API] | `2026-06-04 01:55:01` |
| `ANNOUNCEMENT` | `INFO` | `68.42` | 28,938.08 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 28.94K USD at 68.4180 USD [API] | `2026-06-04 01:55:01` |
| `ANNOUNCEMENT` | `INFO` | `68.42` | 11.63 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.01K USD at 68.4180 USD [API] | `2026-06-04 01:55:01` |
| `ANNOUNCEMENT` | `INFO` | `68.42` | 5,688.44 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 5.69K USD at 68.4200 USD [API] | `2026-06-04 01:55:01` |
| `ANNOUNCEMENT` | `INFO` | `68.42` | 3,349.84 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 3.35K USD at 68.4200 USD [API] | `2026-06-04 01:55:01` |
| `ANNOUNCEMENT` | `INFO` | `99.65` | 27,695.61 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 27.70K USD at 99.6460 USD [API] | `2026-10-29 03:49:50` |
| `ANNOUNCEMENT` | `INFO` | `99.65` | 47,830.08 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 47.83K USD at 99.6460 USD [API] | `2026-10-29 03:49:50` |
| `ANNOUNCEMENT` | `INFO` | `99.56` | 26,848.61 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 26.85K USD at 99.5610 USD [API] | `2026-10-29 03:52:36` |
| `ANNOUNCEMENT` | `INFO` | `99.62` | 23,062.96 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 23.06K USD at 99.6240 USD [API] | `2026-10-29 03:58:36` |
| `ANNOUNCEMENT` | `INFO` | `100.37` | 105,923.47 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 105.92K USD at 100.3700 USD [API] | `2026-10-29 05:05:15` |
| `ANNOUNCEMENT` | `INFO` | `100.51` | 24,346.54 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 24.35K USD at 100.5100 USD [API] | `2026-10-29 05:07:49` |
| `ANNOUNCEMENT` | `INFO` | `138.54` | 7,909.25 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 7.91K USD at 138.5400 USD [API] | `2026-01-18 23:46:32` |
| `ANNOUNCEMENT` | `INFO` | `142.66` | 19,725.60 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 19.73K USD at 142.6600 USD [API] | `2026-01-15 15:25:17` |
| `ANNOUNCEMENT` | `INFO` | `120.55` | 2,728.05 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.73K USD at 120.5500 USD [API] | `2025-12-24 06:07:30` |
| `ANNOUNCEMENT` | `INFO` | `122.53` | 5,992.94 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 5.99K USD at 122.5300 USD [API] | `2025-12-23 14:38:40` |
| `ANNOUNCEMENT` | `INFO` | `128.41` | 8,136.06 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 8.14K USD at 128.4100 USD [API] | `2025-12-14 23:32:44` |
| `ANNOUNCEMENT` | `INFO` | `129.79` | 16,030.36 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 16.03K USD at 129.7900 USD [API] | `2025-12-07 14:24:22` |
| `ANNOUNCEMENT` | `INFO` | `129.79` | 13,999.15 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 14.00K USD at 129.7900 USD [API] | `2025-12-07 14:24:22` |
| `ANNOUNCEMENT` | `INFO` | `129.79` | 9,292.96 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 9.29K USD at 129.7900 USD [API] | `2025-12-07 14:24:22` |
| `ANNOUNCEMENT` | `INFO` | `139.31` | 983.53 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.98K USD at 139.3100 USD [API] | `2025-12-03 14:02:57` |
| `ANNOUNCEMENT` | `INFO` | `132.04` | 2,100.76 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.10K USD at 132.0400 USD [API] | `2025-11-19 17:19:49` |
| `ANNOUNCEMENT` | `INFO` | `136.22` | 934.47 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.93K USD at 136.2200 USD [API] | `2025-11-17 16:02:09` |
| `ANNOUNCEMENT` | `INFO` | `136.22` | 2,351.16 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.35K USD at 136.2200 USD [API] | `2025-11-17 16:02:09` |
| `ANNOUNCEMENT` | `INFO` | `136.23` | 1,219.26 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.22K USD at 136.2300 USD [API] | `2025-11-17 16:02:09` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`101.22` (Vol: 4,800,000.00 USD, Dist: `+3.06%`) | Long MP=`92.18` (Vol: 5,300,000.00 USD, Dist: `--6.15%`)
  * 48H Horizon: Short MP=`101.12` (Vol: 4,700,000.00 USD, Dist: `+2.96%`) | Long MP=`92.16` (Vol: 5,300,000.00 USD, Dist: `--6.17%`)
  * 3D Horizon: Short MP=`101.12` (Vol: 4,700,000.00 USD, Dist: `+2.96%`) | Long MP=`92.16` (Vol: 5,300,000.00 USD, Dist: `--6.17%`)
  * 7D Horizon: Short MP=`104.03` (Vol: 7,200,000.00 USD, Dist: `+5.92%`) | Long MP=`92.11` (Vol: 5,300,000.00 USD, Dist: `--6.22%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `19.75` | 14,120.00 USD | 123,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.85` | 1,100.00 USD | 123,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.55` | 4,790.00 USD | 123,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.15` | 10,580.00 USD | 123,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.35` | 1,780.00 USD | 123,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.45` | 381.81 USD | 123,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.55` | 246.96 USD | 123,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.75` | 4,630.00 USD | 123,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.85` | 5,130.00 USD | 123,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.05` | 1,100.00 USD | 123,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.25` | 132.39 USD | 123,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.45` | 111.13 USD | 123,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.55` | 359.00 USD | 123,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.75` | 820,950.00 USD | 123,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.95` | 13,280.00 USD | 122,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.15` | 243.31 USD | 122,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.35` | 1,170.00 USD | 122,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.45` | 1,380.00 USD | 122,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.65` | 10,610.00 USD | 122,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.85` | 9,650.00 USD | 122,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.05` | 5,170.00 USD | 122,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.15` | 1,860.00 USD | 122,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.25` | 21,710.00 USD | 122,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.45` | 1,220.00 USD | 122,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.65` | 5,050.00 USD | 122,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.05` | 3,390.00 USD | 122,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.15` | 2,010.00 USD | 122,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.45` | 305.40 USD | 122,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.55` | 107.05 USD | 122,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.95` | 2,930.00 USD | 122,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.05` | 155,010.00 USD | 122,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.25` | 837.90 USD | 122,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.35` | 475.09 USD | 122,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.65` | 412.28 USD | 122,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.95` | 10,840.00 USD | 122,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.15` | 382.00 USD | 122,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.25` | 1,170.00 USD | 122,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.35` | 595.96 USD | 122,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.45` | 686.25 USD | 122,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.55` | 142.16 USD | 122,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.85` | 412.18 USD | 122,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.05` | 2,740.00 USD | 122,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.25` | 87,290.00 USD | 122,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.35` | 9,480.00 USD | 122,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.45` | 15,020.00 USD | 122,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.85` | 2,310.00 USD | 122,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.95` | 424.41 USD | 122,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.05` | 9,880.00 USD | 122,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.15` | 9,830.00 USD | 121,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.35` | 260.04 USD | 121,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.45` | 33,030.00 USD | 121,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.75` | 1,680.00 USD | 121,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.95` | 45,160.00 USD | 121,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.05` | 3,010.00 USD | 121,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.15` | 66,180.00 USD | 121,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.25` | 9,160.00 USD | 121,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.55` | 3,210.00 USD | 121,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.65` | 233.86 USD | 121,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.85` | 157.64 USD | 121,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.05` | 621.00 USD | 121,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.15` | 7,320.00 USD | 121,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.25` | 160.62 USD | 121,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.45` | 408.54 USD | 121,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.75` | 158.75 USD | 121,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.85` | 68,610.00 USD | 121,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.95` | 791.72 USD | 121,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.05` | 24,380.00 USD | 121,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.25` | 564,040.00 USD | 121,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.35` | 815.87 USD | 121,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.55` | 1,070.00 USD | 121,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.85` | 9,710.00 USD | 121,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.95` | 920.62 USD | 121,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.05` | 177.81 USD | 121,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.45` | 753.29 USD | 121,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.55` | 493.52 USD | 121,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.95` | 226.11 USD | 121,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.25` | 397.98 USD | 121,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.35` | 2,150.00 USD | 121,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.65` | 486.14 USD | 121,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.75` | 1,610.00 USD | 121,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.85` | 41,820.00 USD | 121,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.95` | 6,620,000.00 USD | 121,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.15` | 17,050.00 USD | 114,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.25` | 1,010.00 USD | 114,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.35` | 48,090.00 USD | 114,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.55` | 3,030.00 USD | 114,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.65` | 1,980.00 USD | 114,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.75` | 5,720.00 USD | 114,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.95` | 557.94 USD | 114,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.05` | 7,160.00 USD | 114,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.15` | 50,400.00 USD | 114,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.25` | 1,400.00 USD | 114,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.35` | 5,280.00 USD | 114,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.45` | 2,410.00 USD | 114,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.55` | 1,060.00 USD | 114,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.65` | 38,560.00 USD | 114,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.75` | 1,400.00 USD | 114,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.95` | 1,660.00 USD | 114,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.05` | 16,570.00 USD | 114,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.25` | 373.62 USD | 114,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.35` | 21,230.00 USD | 114,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.55` | 4,200.00 USD | 114,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.65` | 2,430.00 USD | 114,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.75` | 10,380.00 USD | 114,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.85` | 105,670.00 USD | 114,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.95` | 10,170.00 USD | 114,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.05` | 2,240.00 USD | 114,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.15` | 642.83 USD | 114,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.35` | 769.30 USD | 114,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.45` | 3,000,000.00 USD | 114,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.55` | 1,060,000.00 USD | 111,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.75` | 736.64 USD | 110,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.85` | 4,270.00 USD | 110,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.95` | 607.62 USD | 110,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.05` | 54,500.00 USD | 110,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.15` | 1,710.00 USD | 109,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.35` | 3,640.00 USD | 109,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.45` | 1,080.00 USD | 109,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.65` | 1,560.00 USD | 109,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.75` | 159.00 USD | 109,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.85` | 3,260.00 USD | 109,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.05` | 52,780.00 USD | 109,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.15` | 2,510.00 USD | 109,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.25` | 12,710.00 USD | 109,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.35` | 328,990.00 USD | 109,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.55` | 3,160.00 USD | 109,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.75` | 288.51 USD | 109,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.85` | 2,770.00 USD | 109,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.95` | 9,790.00 USD | 109,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.05` | 4,600.00 USD | 109,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.15` | 2,930.00 USD | 109,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.25` | 2,840.00 USD | 109,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.35` | 2,990.00 USD | 109,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.45` | 1,590.00 USD | 109,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.55` | 234.76 USD | 109,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.65` | 770.11 USD | 109,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.75` | 588.26 USD | 109,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.85` | 1,020.00 USD | 109,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.95` | 48,400.00 USD | 109,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.05` | 470.12 USD | 109,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.15` | 22,560.00 USD | 109,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.25` | 1,070,000.00 USD | 109,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.35` | 6,110.00 USD | 108,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.45` | 8,190.00 USD | 108,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.55` | 1,750.00 USD | 108,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.85` | 44,250.00 USD | 108,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.15` | 11,750.00 USD | 108,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.25` | 1,080.00 USD | 108,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.35` | 5,420.00 USD | 108,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.45` | 440.15 USD | 108,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.65` | 5,530.00 USD | 108,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.85` | 69,970.00 USD | 108,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.95` | 242.16 USD | 108,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.05` | 11,220.00 USD | 108,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.25` | 6,110.00 USD | 108,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.35` | 667,940.00 USD | 108,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.45` | 10,180.00 USD | 107,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.55` | 17,870.00 USD | 107,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.65` | 410.78 USD | 107,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.75` | 1,790.00 USD | 107,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.85` | 3,670,000.00 USD | 107,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.95` | 42,870.00 USD | 103,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.15` | 179.70 USD | 103,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.35` | 35,740.00 USD | 103,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.45` | 19,500.00 USD | 103,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.55` | 8,480.00 USD | 103,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.65` | 471.56 USD | 103,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.75` | 10,360.00 USD | 103,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.85` | 4,010.00 USD | 103,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.95` | 26,070.00 USD | 103,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.05` | 281.83 USD | 103,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.15` | 161.53 USD | 103,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.45` | 824.95 USD | 103,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.55` | 522.76 USD | 103,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.65` | 542.07 USD | 103,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.75` | 1,240.00 USD | 103,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.85` | 544.40 USD | 103,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.95` | 3,870.00 USD | 103,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.15` | 10,780.00 USD | 103,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.25` | 3,220.00 USD | 103,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.35` | 970.20 USD | 103,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.45` | 270.47 USD | 103,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.55` | 106.04 USD | 103,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.65` | 103,030.00 USD | 103,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.75` | 804,840.00 USD | 103,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.85` | 8,130.00 USD | 102,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.95` | 2,260.00 USD | 102,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.05` | 13,300.00 USD | 102,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.15` | 6,440.00 USD | 102,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.25` | 2,430.00 USD | 102,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.35` | 6,050.00 USD | 102,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.45` | 2,930.00 USD | 102,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.55` | 97,250.00 USD | 102,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.65` | 9,680.00 USD | 102,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.75` | 1,860.00 USD | 102,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.85` | 14,260.00 USD | 102,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.95` | 1,640.00 USD | 102,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.05` | 1,120.00 USD | 102,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.15` | 5,010.00 USD | 102,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.25` | 21,480.00 USD | 102,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.35` | 585.29 USD | 102,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.45` | 16,830.00 USD | 102,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.55` | 889.42 USD | 102,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.65` | 8,890.00 USD | 102,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.75` | 201.99 USD | 102,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.85` | 1,250,000.00 USD | 102,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.95` | 170,350.00 USD | 101,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.05` | 9,870.00 USD | 101,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.15` | 11,970.00 USD | 101,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.25` | 8,890.00 USD | 101,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.35` | 2,410.00 USD | 101,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.45` | 3,820.00 USD | 101,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.55` | 12,510.00 USD | 101,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.65` | 843.83 USD | 101,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.75` | 12,040.00 USD | 101,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.85` | 19,710.00 USD | 101,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.95` | 5,530.00 USD | 101,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.05` | 2,680.00 USD | 101,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.15` | 2,620.00 USD | 101,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.25` | 2,440.00 USD | 101,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.35` | 10,640.00 USD | 101,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.45` | 8,510.00 USD | 101,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.55` | 135,270.00 USD | 101,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.65` | 7,950.00 USD | 100,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.75` | 26,840.00 USD | 100,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.85` | 43,180.00 USD | 100,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.95` | 473,530.00 USD | 100,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.05` | 31,030.00 USD | 100,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.15` | 101,420.00 USD | 100,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.25` | 1,760.00 USD | 100,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.35` | 28,410.00 USD | 100,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.45` | 1,140.00 USD | 100,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.55` | 11,110.00 USD | 100,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.65` | 2,900.00 USD | 100,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.75` | 68,980.00 USD | 100,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.85` | 27,520.00 USD | 100,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.95` | 2,210.00 USD | 100,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.05` | 17,340.00 USD | 100,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.15` | 2,670.00 USD | 100,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.25` | 24,460.00 USD | 100,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.35` | 2,240.00 USD | 100,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.45` | 47,590.00 USD | 100,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.55` | 43,790.00 USD | 99,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.65` | 230.70 USD | 99,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.75` | 3,600.00 USD | 99,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.85` | 18,710.00 USD | 99,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.95` | 60,360.00 USD | 99,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.05` | 1,650.00 USD | 99,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.15` | 14,640.00 USD | 99,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.25` | 5,360.00 USD | 99,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.35` | 12,060.00 USD | 99,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.45` | 1,840.00 USD | 99,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.55` | 60,580.00 USD | 99,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.65` | 10,920.00 USD | 99,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.75` | 15,140.00 USD | 99,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.85` | 858,930.00 USD | 99,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.95` | 142,480.00 USD | 98,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.05` | 552.70 USD | 98,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.15` | 1,160.00 USD | 98,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.25` | 2,010.00 USD | 98,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.35` | 43,510.00 USD | 98,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.45` | 145,980.00 USD | 98,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.55` | 5,090.00 USD | 98,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.65` | 11,490.00 USD | 98,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.75` | 92,400.00 USD | 98,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.85` | 8,360.00 USD | 98,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.95` | 8,640.00 USD | 98,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.05` | 5,640.00 USD | 98,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.15` | 38,930.00 USD | 98,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.25` | 13,300.00 USD | 98,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.35` | 38,470.00 USD | 98,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.45` | 35,560.00 USD | 98,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.55` | 5,930.00 USD | 98,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.65` | 18,370.00 USD | 98,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.75` | 11,350.00 USD | 98,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.85` | 122.80 USD | 98,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.95` | 14,320.00 USD | 98,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.05` | 2,770,000.00 USD | 98,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.15` | 5,380.00 USD | 95,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.25` | 2,930.00 USD | 95,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.35` | 7,120.00 USD | 95,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.45` | 19,200.00 USD | 95,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.55` | 1,390.00 USD | 95,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.65` | 23,520.00 USD | 95,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.75` | 36,550.00 USD | 95,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.85` | 21,950.00 USD | 95,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.95` | 1,680.00 USD | 95,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.05` | 4,710.00 USD | 95,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.15` | 185,300.00 USD | 95,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.25` | 16,420.00 USD | 95,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.35` | 4,670.00 USD | 95,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.45` | 23,520.00 USD | 95,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.55` | 2,970.00 USD | 95,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.65` | 2,350,000.00 USD | 95,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.75` | 195.64 USD | 92,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.85` | 6,130.00 USD | 92,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.95` | 1,090.00 USD | 92,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.05` | 37,600.00 USD | 92,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.15` | 4,760.00 USD | 92,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.25` | 613.24 USD | 92,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.35` | 63,190.00 USD | 92,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.45` | 4,230.00 USD | 92,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.55` | 8,770.00 USD | 92,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.65` | 4,020.00 USD | 92,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.75` | 13,130.00 USD | 92,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.85` | 21,560.00 USD | 92,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.95` | 37,240.00 USD | 92,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.05` | 24,200.00 USD | 92,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.15` | 35,140.00 USD | 92,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.25` | 20,970.00 USD | 92,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.35` | 9,880.00 USD | 92,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.55` | 101,570.00 USD | 92,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.65` | 711.42 USD | 92,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.75` | 5,300.00 USD | 92,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.85` | 28,860.00 USD | 92,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.95` | 59,450.00 USD | 92,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.05` | 4,230.00 USD | 92,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.15` | 23,090.00 USD | 92,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.25` | 4,630.00 USD | 92,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.35` | 11,940.00 USD | 92,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.45` | 20,920.00 USD | 92,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.55` | 25,430.00 USD | 92,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.65` | 18,880.00 USD | 92,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.75` | 33,410.00 USD | 92,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.85` | 7,540.00 USD | 92,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.95` | 4,260.00 USD | 92,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.05` | 9,000.00 USD | 92,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.15` | 40,890.00 USD | 92,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.25` | 1,800.00 USD | 92,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.35` | 17,900.00 USD | 92,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.45` | 27,890.00 USD | 92,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.55` | 133,130.00 USD | 92,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.65` | 2,480.00 USD | 91,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.75` | 4,190.00 USD | 91,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.85` | 70,890.00 USD | 91,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.95` | 65,880.00 USD | 91,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.05` | 22,540.00 USD | 91,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.15` | 81,250.00 USD | 91,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.25` | 16,050.00 USD | 91,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.45` | 291.24 USD | 91,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.55` | 49,290.00 USD | 91,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.65` | 3,600.00 USD | 91,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.75` | 32,540.00 USD | 91,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.85` | 40,280.00 USD | 91,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.95` | 2,280.00 USD | 91,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.25` | 4,450.00 USD | 91,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.35` | 2,750.00 USD | 91,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.45` | 4,320.00 USD | 91,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.55` | 30,840.00 USD | 91,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.65` | 2,220.00 USD | 91,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.75` | 97,290.00 USD | 91,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.85` | 396.23 USD | 91,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.95` | 209.79 USD | 91,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.05` | 247,180.00 USD | 91,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.15` | 11,480.00 USD | 91,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.25` | 15,120.00 USD | 91,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.35` | 56,990.00 USD | 91,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.45` | 3,130.00 USD | 91,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.55` | 10,470.00 USD | 91,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.65` | 58,270.00 USD | 90,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.75` | 5,070.00 USD | 90,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.85` | 63,890.00 USD | 90,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.95` | 5,780.00 USD | 90,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.05` | 25,140.00 USD | 90,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.15` | 1,880.00 USD | 90,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.25` | 43,960.00 USD | 90,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.35` | 1,600.00 USD | 90,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.45` | 10,990.00 USD | 90,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.55` | 54,650.00 USD | 90,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.65` | 17,700.00 USD | 90,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.75` | 43,110.00 USD | 90,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.85` | 1,910.00 USD | 90,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.95` | 937.30 USD | 90,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.05` | 33,520.00 USD | 90,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.15` | 418,020.00 USD | 90,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.25` | 1,350,000.00 USD | 90,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.35` | 1,450.00 USD | 88,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.45` | 21,630.00 USD | 88,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.55` | 55,000.00 USD | 88,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.65` | 128,820.00 USD | 88,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.75` | 32,130.00 USD | 88,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.85` | 7,630.00 USD | 88,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.95` | 3,680.00 USD | 88,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.05` | 13,800.00 USD | 88,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.15` | 37,490,000.00 USD | 88,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.25` | 13,650.00 USD | 51,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.35` | 4,710.00 USD | 51,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.45` | 19,210.00 USD | 51,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.55` | 3,890.00 USD | 51,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.65` | 19,990.00 USD | 51,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.75` | 148,840.00 USD | 51,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.85` | 7,320.00 USD | 50,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.95` | 828,230.00 USD | 50,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.05` | 12,430,000.00 USD | 50,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.15` | 10,190.00 USD | 37,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.25` | 8,660.00 USD | 37,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.35` | 119.28 USD | 37,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.45` | 42,250.00 USD | 37,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.55` | 10,140.00 USD | 37,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.65` | 964,080.00 USD | 37,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.75` | 432,400.00 USD | 36,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.85` | 32,380.00 USD | 36,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.95` | 8,800.00 USD | 36,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.05` | 682.99 USD | 36,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.15` | 4,120.00 USD | 36,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.25` | 73,070.00 USD | 36,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.35` | 2,140,000.00 USD | 36,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.45` | 118,170.00 USD | 33,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.55` | 417.66 USD | 33,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.65` | 1,110,000.00 USD | 33,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.75` | 12,120.00 USD | 32,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.85` | 12,050.00 USD | 32,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.95` | 5,630.00 USD | 32,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.05` | 32,040.00 USD | 32,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.15` | 76,320.00 USD | 32,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.25` | 3,410.00 USD | 32,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.35` | 62,910.00 USD | 32,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.45` | 24,590.00 USD | 32,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.55` | 41,780.00 USD | 32,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.65` | 894.91 USD | 32,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.75` | 38,870.00 USD | 32,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.85` | 2,130.00 USD | 32,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.95` | 12,710.00 USD | 32,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.05` | 8,090.00 USD | 32,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.15` | 134,310.00 USD | 32,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.25` | 269,050.00 USD | 32,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.35` | 28,860.00 USD | 31,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.45` | 1,840.00 USD | 31,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.55` | 16,340.00 USD | 31,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.65` | 38,620.00 USD | 31,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.75` | 3,550.00 USD | 31,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.85` | 188,230.00 USD | 31,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.95` | 7,040.00 USD | 31,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.05` | 8,140.00 USD | 31,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.15` | 19,790.00 USD | 31,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.25` | 28,370.00 USD | 31,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.35` | 3,900.00 USD | 31,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.45` | 18,450.00 USD | 31,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.55` | 14,850.00 USD | 31,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.65` | 37,850.00 USD | 31,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.75` | 74,890.00 USD | 31,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.85` | 36,100.00 USD | 31,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.95` | 74,150.00 USD | 31,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.05` | 23,760.00 USD | 31,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.15` | 31,600.00 USD | 31,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.25` | 50,170.00 USD | 31,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.35` | 24,480.00 USD | 31,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.45` | 27,100.00 USD | 31,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.55` | 38,530.00 USD | 31,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.65` | 99,800.00 USD | 31,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.75` | 32,790.00 USD | 31,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.85` | 31,980.00 USD | 31,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.95` | 17,910.00 USD | 30,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.05` | 44,640.00 USD | 30,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.15` | 3,120,000.00 USD | 30,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.25` | 10,380.00 USD | 27,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.35` | 247,040.00 USD | 27,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.45` | 42,370.00 USD | 27,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.55` | 28,520.00 USD | 27,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.65` | 130,250.00 USD | 27,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.75` | 64,900.00 USD | 27,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.85` | 3,990.00 USD | 27,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.95` | 25,630.00 USD | 27,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.05` | 12,340.00 USD | 27,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.15` | 4,370.00 USD | 27,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.25` | 2,070.00 USD | 27,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.35` | 62,610.00 USD | 27,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.45` | 32,740.00 USD | 27,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.55` | 130,100.00 USD | 27,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.65` | 179,000.00 USD | 26,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.75` | 11,340.00 USD | 26,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.85` | 252,770.00 USD | 26,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.95` | 28,980.00 USD | 26,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.05` | 87,490.00 USD | 26,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.15` | 85,130.00 USD | 26,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.25` | 25,340.00 USD | 26,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.35` | 10,160.00 USD | 26,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.45` | 46,840.00 USD | 26,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.55` | 16,110.00 USD | 26,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.75` | 14,690.00 USD | 26,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.85` | 68,550.00 USD | 26,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.95` | 185,210.00 USD | 26,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.05` | 21,860.00 USD | 25,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.15` | 63,710.00 USD | 25,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.25` | 47,380.00 USD | 25,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.35` | 50,680.00 USD | 25,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.45` | 26,080.00 USD | 25,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.55` | 5,740.00 USD | 25,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.65` | 32,590.00 USD | 25,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.75` | 61,050.00 USD | 25,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.85` | 66,850.00 USD | 25,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.95` | 1,740.00 USD | 25,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.05` | 16,530.00 USD | 25,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.15` | 610,370.00 USD | 25,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.25` | 41,700.00 USD | 24,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.35` | 28,820.00 USD | 24,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.45` | 11,580.00 USD | 24,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.55` | 3,180.00 USD | 24,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.65` | 15,720.00 USD | 24,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.75` | 126,320.00 USD | 24,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.85` | 42,840.00 USD | 24,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.95` | 48,790.00 USD | 24,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.05` | 40,950.00 USD | 24,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.15` | 37,150.00 USD | 24,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.25` | 57,490.00 USD | 24,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.35` | 115,070.00 USD | 24,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.45` | 11,320.00 USD | 24,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.55` | 5,880.00 USD | 24,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.65` | 25,050.00 USD | 24,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.75` | 24,950.00 USD | 24,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.85` | 439,440.00 USD | 24,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.95` | 10,620.00 USD | 23,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.05` | 2,230,000.00 USD | 23,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.15` | 128,110.00 USD | 21,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.25` | 27,510.00 USD | 21,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.35` | 56,470.00 USD | 21,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.45` | 57,090.00 USD | 21,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.55` | 67,100.00 USD | 21,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.65` | 15,400.00 USD | 21,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.75` | 18,650.00 USD | 21,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.85` | 66,670.00 USD | 21,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.95` | 100,270.00 USD | 21,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.05` | 117,060.00 USD | 21,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.15` | 808,500.00 USD | 21,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.25` | 386,630.00 USD | 20,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.35` | 162,500.00 USD | 19,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.45` | 205,600.00 USD | 19,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `82.50` | 171,440,000.00 USD | 171,440,000.00 USD | 71,680.00 USD | 3,750.00 USD | 2,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `82.55` | 31,430.00 USD | 19,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.65` | 99,560.00 USD | 19,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `82.70` | 171,360,000.00 USD | 171,360,000.00 USD | 0.00 USD | 54,980.00 USD | 140,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `82.75` | 754,130.00 USD | 19,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.85` | 20,580.00 USD | 18,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `82.90` | 171,170,000.00 USD | 171,170,000.00 USD | 1,670.00 USD | 2,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `82.95` | 17,100.00 USD | 18,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.05` | 118,100.00 USD | 18,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `83.10` | 171,160,000.00 USD | 171,160,000.00 USD | 1,690.00 USD | 48,940.00 USD | 642.56 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `83.15` | 11,130.00 USD | 18,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.25` | 194,580.00 USD | 18,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `83.30` | 171,110,000.00 USD | 171,110,000.00 USD | 3,730.00 USD | 93,000.00 USD | 56,580.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `83.35` | 287,260.00 USD | 18,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.45` | 29,160.00 USD | 17,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `83.50` | 170,960,000.00 USD | 170,960,000.00 USD | 6,440.00 USD | 791.58 USD | 41,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `83.55` | 10,990.00 USD | 17,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.65` | 68,280.00 USD | 17,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `83.70` | 170,910,000.00 USD | 170,910,000.00 USD | 0.00 USD | 68,140.00 USD | 85,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `83.75` | 90,040.00 USD | 17,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.85` | 12,240.00 USD | 17,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `83.90` | 170,750,000.00 USD | 170,750,000.00 USD | 2,640.00 USD | 0.00 USD | 70,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `83.95` | 30,940.00 USD | 17,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.05` | 299,000.00 USD | 17,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `84.10` | 170,680,000.00 USD | 170,680,000.00 USD | 0.00 USD | 14,010.00 USD | 8,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `84.15` | 65,900.00 USD | 17,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.25` | 46,040.00 USD | 17,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `84.30` | 170,660,000.00 USD | 170,660,000.00 USD | 0.00 USD | 26,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `84.35` | 25,180.00 USD | 17,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.45` | 86,620.00 USD | 17,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.55` | 2,300.00 USD | 17,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.65` | 102,150.00 USD | 17,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.75` | 289,410.00 USD | 17,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.85` | 94,810.00 USD | 16,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.95` | 1,360.00 USD | 16,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.05` | 27,810.00 USD | 16,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `85.10` | 170,630,000.00 USD | 170,630,000.00 USD | 0.00 USD | 204,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `85.15` | 7,810.00 USD | 16,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.25` | 626,910.00 USD | 16,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `85.30` | 170,430,000.00 USD | 170,430,000.00 USD | 0.00 USD | 13,630.00 USD | 186,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `85.35` | 21,600.00 USD | 16,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.45` | 1,290,000.00 USD | 15,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `85.50` | 170,230,000.00 USD | 170,230,000.00 USD | 0.00 USD | 12,950.00 USD | 6,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `85.55` | 9,600.00 USD | 14,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.65` | 42,860.00 USD | 14,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `85.70` | 170,210,000.00 USD | 170,210,000.00 USD | 0.00 USD | 0.00 USD | 189,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `85.75` | 10,890.00 USD | 14,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.85` | 87,080.00 USD | 14,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `85.90` | 170,020,000.00 USD | 170,020,000.00 USD | 0.00 USD | 260,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `85.95` | 361,960.00 USD | 14,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.05` | 256,680.00 USD | 14,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `86.10` | 169,760,000.00 USD | 169,760,000.00 USD | 0.00 USD | 0.00 USD | 195,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.15` | 55,020.00 USD | 13,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.25` | 36,410.00 USD | 13,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `86.30` | 169,560,000.00 USD | 169,560,000.00 USD | 0.00 USD | 323,360.00 USD | 4,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.35` | 3,990.00 USD | 13,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.45` | 108,330.00 USD | 13,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `86.50` | 169,240,000.00 USD | 169,240,000.00 USD | 0.00 USD | 0.00 USD | 4,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.55` | 60,400.00 USD | 13,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.65` | 201,760.00 USD | 13,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `86.70` | 169,230,000.00 USD | 169,230,000.00 USD | 0.00 USD | 11,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.75` | 37,320.00 USD | 13,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.85` | 78,680.00 USD | 13,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `86.90` | 169,220,000.00 USD | 169,220,000.00 USD | 263,340.00 USD | 309,680.00 USD | 297,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.95` | 167,620.00 USD | 13,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.05` | 57,090.00 USD | 13,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.10` | 173,020,000.00 USD | 173,020,000.00 USD | 316,760.00 USD | 433,420.00 USD | 423,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `87.10` | 168,350,000.00 USD | 168,350,000.00 USD | 0.00 USD | 5,620.00 USD | 6,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.15` | 45,680.00 USD | 13,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.25` | 26,840.00 USD | 13,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.30` | 171,850,000.00 USD | 171,850,000.00 USD | 61,200.00 USD | 207,830.00 USD | 156,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `87.30` | 168,340,000.00 USD | 168,340,000.00 USD | 0.00 USD | 204,790.00 USD | 288,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.35` | 77,770.00 USD | 13,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.45` | 210,950.00 USD | 12,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.50` | 171,420,000.00 USD | 171,420,000.00 USD | 10,160.00 USD | 72,180.00 USD | 69,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `87.50` | 167,840,000.00 USD | 167,840,000.00 USD | 24,350.00 USD | 24,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.55` | 194,880.00 USD | 12,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.65` | 123,610.00 USD | 12,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.70` | 171,270,000.00 USD | 171,270,000.00 USD | 8,600.00 USD | 247,780.00 USD | 247,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `87.70` | 167,800,000.00 USD | 167,800,000.00 USD | 0.00 USD | 290,940.00 USD | 415,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.75` | 27,360.00 USD | 12,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.85` | 60,260.00 USD | 12,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.90` | 170,770,000.00 USD | 170,770,000.00 USD | 133,480.00 USD | 427,430.00 USD | 915,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `87.90` | 167,090,000.00 USD | 167,090,000.00 USD | 0.00 USD | 307,460.00 USD | 242,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.95` | 8,810.00 USD | 12,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.05` | 161,140.00 USD | 12,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.10` | 169,290,000.00 USD | 169,290,000.00 USD | 0.00 USD | 0.00 USD | 230,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `88.10` | 166,540,000.00 USD | 166,540,000.00 USD | 0.00 USD | 0.00 USD | 12,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.15` | 23,910.00 USD | 12,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.25` | 49,740.00 USD | 12,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.30` | 169,060,000.00 USD | 169,060,000.00 USD | 83,370.00 USD | 73,830.00 USD | 136,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `88.30` | 166,530,000.00 USD | 166,530,000.00 USD | 0.00 USD | 20,610.00 USD | 331,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.35` | 95,640.00 USD | 12,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.45` | 69,660.00 USD | 12,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.50` | 168,770,000.00 USD | 168,770,000.00 USD | 0.00 USD | 99,900.00 USD | 1,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `88.50` | 166,170,000.00 USD | 166,170,000.00 USD | 0.00 USD | 0.00 USD | 3,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.55` | 242,620.00 USD | 11,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.65` | 97,760.00 USD | 11,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.70` | 168,660,000.00 USD | 168,660,000.00 USD | 204,330.00 USD | 124,180.00 USD | 415,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `88.70` | 166,170,000.00 USD | 166,170,000.00 USD | 224,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.75` | 155,750.00 USD | 11,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.85` | 1,100,000.00 USD | 11,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.90` | 167,920,000.00 USD | 167,920,000.00 USD | 143,140.00 USD | 62,660.00 USD | 226,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `88.90` | 165,950,000.00 USD | 165,950,000.00 USD | 17,470.00 USD | 3,730.00 USD | 3,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.95` | 33,030.00 USD | 10,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.05` | 49,580.00 USD | 10,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.10` | 167,490,000.00 USD | 167,490,000.00 USD | 160,900.00 USD | 83,520.00 USD | 11,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `89.10` | 165,920,000.00 USD | 165,920,000.00 USD | 350,210.00 USD | 291,000.00 USD | 601,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.15` | 124,300.00 USD | 10,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.25` | 33,540.00 USD | 10,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.30` | 167,230,000.00 USD | 167,230,000.00 USD | 221,290.00 USD | 284,680.00 USD | 5,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `89.30` | 164,680,000.00 USD | 164,680,000.00 USD | 679,190.00 USD | 22,080.00 USD | 27,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.35` | 80,890.00 USD | 10,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.45` | 451,080.00 USD | 10,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.50` | 166,720,000.00 USD | 166,720,000.00 USD | 4,870.00 USD | 50,620.00 USD | 278,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `89.50` | 163,950,000.00 USD | 163,950,000.00 USD | 184,930.00 USD | 91,380.00 USD | 512,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.55` | 121,590.00 USD | 9,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.65` | 29,100.00 USD | 9,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.70` | 166,390,000.00 USD | 166,390,000.00 USD | 190,910.00 USD | 107,730.00 USD | 426,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `89.70` | 163,160,000.00 USD | 163,160,000.00 USD | 780,700.00 USD | 225,300.00 USD | 472,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.75` | 148,760.00 USD | 9,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.85` | 50,000.00 USD | 9,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.90` | 165,660,000.00 USD | 165,660,000.00 USD | 301,540.00 USD | 255,100.00 USD | 381,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `89.90` | 161,680,000.00 USD | 161,680,000.00 USD | 446,430.00 USD | 563,970.00 USD | 807,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.95` | 70,760.00 USD | 9,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.05` | 31,350.00 USD | 9,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.10` | 164,720,000.00 USD | 164,720,000.00 USD | 1,210,000.00 USD | 1,030,000.00 USD | 836,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.10` | 159,860,000.00 USD | 159,860,000.00 USD | 967,200.00 USD | 633,920.00 USD | 879,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.15` | 72,970.00 USD | 9,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.25` | 27,570.00 USD | 9,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.30` | 161,650,000.00 USD | 161,650,000.00 USD | 773,740.00 USD | 563,210.00 USD | 477,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.30` | 157,380,000.00 USD | 157,380,000.00 USD | 936,750.00 USD | 342,020.00 USD | 802,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.35` | 77,200.00 USD | 9,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.45` | 29,160.00 USD | 8,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.50` | 159,830,000.00 USD | 159,830,000.00 USD | 683,680.00 USD | 538,340.00 USD | 964,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.50` | 155,300,000.00 USD | 155,300,000.00 USD | 1,100,000.00 USD | 823,160.00 USD | 860,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.55` | 25,420.00 USD | 8,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.65` | 132,120.00 USD | 8,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.70` | 157,650,000.00 USD | 157,650,000.00 USD | 628,630.00 USD | 803,190.00 USD | 388,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.70` | 152,520,000.00 USD | 152,520,000.00 USD | 742,490.00 USD | 700,720.00 USD | 1,440,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.75` | 88,240.00 USD | 8,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.85` | 950,960.00 USD | 8,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.90` | 155,830,000.00 USD | 155,830,000.00 USD | 673,680.00 USD | 420,760.00 USD | 83,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.90` | 149,640,000.00 USD | 149,640,000.00 USD | 1,350,000.00 USD | 997,660.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.95` | 19,210.00 USD | 7,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.05` | 435,870.00 USD | 7,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.10` | 154,650,000.00 USD | 154,650,000.00 USD | 436,270.00 USD | 732,110.00 USD | 474,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.10` | 146,260,000.00 USD | 146,260,000.00 USD | 2,350,000.00 USD | 578,750.00 USD | 895,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.15` | 295,530.00 USD | 7,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.25` | 31,690.00 USD | 6,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.30` | 153,010,000.00 USD | 153,010,000.00 USD | 150,320.00 USD | 221,290.00 USD | 448,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.30` | 142,440,000.00 USD | 142,440,000.00 USD | 1,080,000.00 USD | 810,610.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.35` | 50,530.00 USD | 6,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.45` | 541,180.00 USD | 6,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.50` | 152,180,000.00 USD | 152,180,000.00 USD | 850,930.00 USD | 781,420.00 USD | 655,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.50` | 139,460,000.00 USD | 139,460,000.00 USD | 705,000.00 USD | 1,710,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.55` | 1,230,000.00 USD | 6,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.65` | 1,460,000.00 USD | 5,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.70` | 149,900,000.00 USD | 149,900,000.00 USD | 268,750.00 USD | 463,180.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.70` | 135,750,000.00 USD | 135,750,000.00 USD | 538,680.00 USD | 342,840.00 USD | 781,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.75` | 230,810.00 USD | 3,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.85` | 248,720.00 USD | 3,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.90` | 148,000,000.00 USD | 148,000,000.00 USD | 1,280,000.00 USD | 813,050.00 USD | 663,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.90` | 134,090,000.00 USD | 134,090,000.00 USD | 1,020,000.00 USD | 838,200.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.95` | 86,310.00 USD | 3,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.05` | 206,110.00 USD | 3,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.10` | 145,250,000.00 USD | 145,250,000.00 USD | 2,310,000.00 USD | 2,670,000.00 USD | 565,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.10` | 131,000,000.00 USD | 131,000,000.00 USD | 3,150,000.00 USD | 1,400,000.00 USD | 278,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.15` | 158,880.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.25` | 241,900.00 USD | 2,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.30` | 139,700,000.00 USD | 139,700,000.00 USD | 720,590.00 USD | 799,660.00 USD | 1,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.30` | 126,170,000.00 USD | 126,170,000.00 USD | 375,130.00 USD | 487,150.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.35` | 313,050.00 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.45` | 131,560.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.50` | 136,770,000.00 USD | 136,770,000.00 USD | 1,140,000.00 USD | 703,500.00 USD | 2,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.50` | 123,780,000.00 USD | 123,780,000.00 USD | 260,510.00 USD | 1,320,000.00 USD | 1,770,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.55` | 3,490.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.65` | 38,450.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.70` | 132,580,000.00 USD | 132,580,000.00 USD | 982,240.00 USD | 1,110,000.00 USD | 1,700,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.70` | 120,430,000.00 USD | 120,430,000.00 USD | 148,000.00 USD | 1,830,000.00 USD | 1,610,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.75` | 316,620.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.85` | 11,850.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.90` | 128,790,000.00 USD | 128,790,000.00 USD | 3,020,000.00 USD | 1,870,000.00 USD | 2,470,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.90` | 116,850,000.00 USD | 116,850,000.00 USD | 371,030.00 USD | 783,070.00 USD | 954,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.95` | 5,720.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.05` | 25,790.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.10` | 121,430,000.00 USD | 121,430,000.00 USD | 2,030,000.00 USD | 3,210,000.00 USD | 1,730,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.10` | 114,740,000.00 USD | 114,740,000.00 USD | 31,020.00 USD | 686,660.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.15` | 175.12 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.25` | 38,840.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.30` | 114,460,000.00 USD | 114,460,000.00 USD | 2,250,000.00 USD | 2,580,000.00 USD | 1,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.30` | 113,000,000.00 USD | 113,000,000.00 USD | 96,300.00 USD | 0.00 USD | 1,420,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.35` | 12,570.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.45` | 739.19 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.50` | 108,370,000.00 USD | 108,370,000.00 USD | 2,930,000.00 USD | 2,280,000.00 USD | 2,260,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.50` | 111,480,000.00 USD | 111,480,000.00 USD | 399,000.00 USD | 2,880,000.00 USD | 3,050,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.55` | 20,610.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.65` | 697.69 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.70` | 100,910,000.00 USD | 100,910,000.00 USD | 551,230.00 USD | 3,170,000.00 USD | 867,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.70` | 105,160,000.00 USD | 105,160,000.00 USD | 7,450.00 USD | 2,970,000.00 USD | 1,700,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.75` | 9,050.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.90` | 96,310,000.00 USD | 96,310,000.00 USD | 1,590,000.00 USD | 790,210.00 USD | 1,380,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.90` | 100,480,000.00 USD | 100,480,000.00 USD | 2,670,000.00 USD | 30,170.00 USD | 3,410,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.95` | 1,130,000.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.10` | 92,550,000.00 USD | 92,550,000.00 USD | 545,380.00 USD | 851,000.00 USD | 2,460,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.10` | 94,370,000.00 USD | 94,370,000.00 USD | 175,750.00 USD | 2,120,000.00 USD | 2,230,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.15` | 3,990.00 USD | 404,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.25` | 15,100.00 USD | 400,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.30` | 88,690,000.00 USD | 88,690,000.00 USD | 2,130,000.00 USD | 1,080,000.00 USD | 371,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.30` | 89,840,000.00 USD | 89,840,000.00 USD | 0.00 USD | 159,070.00 USD | 839,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.35` | 2,100.00 USD | 385,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.45` | 202,480.00 USD | 383,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.50` | 85,110,000.00 USD | 85,110,000.00 USD | 795,850.00 USD | 1,250,000.00 USD | 645,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.50` | 88,840,000.00 USD | 88,840,000.00 USD | 183,750.00 USD | 496,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.55` | 3,080.00 USD | 180,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.65` | 19,410.00 USD | 177,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.70` | 82,420,000.00 USD | 82,420,000.00 USD | 1,360,000.00 USD | 571,830.00 USD | 399,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.70` | 88,160,000.00 USD | 88,160,000.00 USD | 1,600,000.00 USD | 99,300.00 USD | 3,360,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.75` | 53,170.00 USD | 158,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.85` | 15,620.00 USD | 104,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.90` | 80,080,000.00 USD | 80,080,000.00 USD | 2,720,000.00 USD | 434,700.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.90` | 83,100,000.00 USD | 83,100,000.00 USD | 3,170,000.00 USD | 4,260,000.00 USD | 47,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.95` | 61,600.00 USD | 89,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.05` | 7,780.00 USD | 27,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.10` | 75,710,000.00 USD | 75,710,000.00 USD | 2,150,000.00 USD | 1,390,000.00 USD | 27,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.10` | 75,620,000.00 USD | 75,620,000.00 USD | 198,380.00 USD | 199,180.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.15` | 19,930.00 USD | 19,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.30` | 72,150,000.00 USD | 72,150,000.00 USD | 87,330.00 USD | 494,560.00 USD | 3,370,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.30` | 75,210,000.00 USD | 75,210,000.00 USD | 678,330.00 USD | 1,060,000.00 USD | 1,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `95.50` | 68,200,000.00 USD | 68,200,000.00 USD | 291,230.00 USD | 1,570,000.00 USD | 1,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.50` | 71,780,000.00 USD | 71,780,000.00 USD | 2,000,000.00 USD | 3,870,000.00 USD | 4,440,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `95.70` | 64,930,000.00 USD | 64,930,000.00 USD | 1,710,000.00 USD | 2,150,000.00 USD | 5,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.70` | 61,480,000.00 USD | 61,480,000.00 USD | 5,540,000.00 USD | 4,060,000.00 USD | 4,180,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `95.90` | 55,680,000.00 USD | 55,680,000.00 USD | 997,860.00 USD | 953,770.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.90` | 47,690,000.00 USD | 47,690,000.00 USD | 2,130,000.00 USD | 344,240.00 USD | 689,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.10` | 52,040,000.00 USD | 52,040,000.00 USD | 1,770,000.00 USD | 2,040,000.00 USD | 3,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.10` | 44,520,000.00 USD | 44,520,000.00 USD | 3,460,000.00 USD | 811,100.00 USD | 8,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.30` | 45,010,000.00 USD | 45,010,000.00 USD | 4,480,000.00 USD | 5,140,000.00 USD | 848,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.30` | 32,170,000.00 USD | 32,170,000.00 USD | 2,740,000.00 USD | 1,700,000.00 USD | 6,490,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.50` | 34,540,000.00 USD | 34,540,000.00 USD | 2,840,000.00 USD | 1,260,000.00 USD | 3,870,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.50` | 21,250,000.00 USD | 21,250,000.00 USD | 0.00 USD | 0.00 USD | 24,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.70` | 26,580,000.00 USD | 26,580,000.00 USD | 1,420,000.00 USD | 2,230,000.00 USD | 956,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.70` | 21,220,000.00 USD | 21,220,000.00 USD | 0.00 USD | 14,450.00 USD | 2,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.90` | 21,970,000.00 USD | 21,970,000.00 USD | 0.00 USD | 1,360,000.00 USD | 4,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.90` | 18,860,000.00 USD | 18,860,000.00 USD | 0.00 USD | 2,310,000.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `97.10` | 15,700,000.00 USD | 15,700,000.00 USD | 3,190,000.00 USD | 2,570,000.00 USD | 1,930,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `97.10` | 15,340,000.00 USD | 15,340,000.00 USD | 0.00 USD | 1,350,000.00 USD | 4,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `97.30` | 8,010,000.00 USD | 8,010,000.00 USD | 1,030,000.00 USD | 1,270,000.00 USD | 873,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `97.30` | 9,710,000.00 USD | 9,710,000.00 USD | 0.00 USD | 16,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `97.50` | 4,840,000.00 USD | 4,840,000.00 USD | 534,370.00 USD | 1,320,000.00 USD | 1,760,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `97.50` | 9,690,000.00 USD | 9,690,000.00 USD | 0.00 USD | 110,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `97.70` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `97.70` | 9,580,000.00 USD | 9,580,000.00 USD | 3,880,000.00 USD | 1,750,000.00 USD | 3,950,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `97.90` | 2,450,000.00 USD | 2,450,000.00 USD | 2,400,000.00 USD | 48,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `97.90` | 4,900,000.00 USD | 4,900,000.00 USD | 2,400,000.00 USD | 48,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `97.90` | 13,610,000.00 USD | 13,610,000.00 USD | 11,920,000.00 USD | 1,690,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `97.90` | 27,210,000.00 USD | 27,210,000.00 USD | 11,920,000.00 USD | 1,690,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `97.95` | 746.38 USD | 746.38 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `98.05` | 487.31 USD | 1,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `98.10` | 7,930,000.00 USD | 7,930,000.00 USD | 215,860.00 USD | 0.00 USD | 2,810,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.10` | 37,090,000.00 USD | 37,090,000.00 USD | 9,870,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.15` | 4,510.00 USD | 5,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `98.25` | 1,080.00 USD | 6,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `98.30` | 15,990,000.00 USD | 15,990,000.00 USD | 1,990,000.00 USD | 20,470.00 USD | 6,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.30` | 49,490,000.00 USD | 49,490,000.00 USD | 1,640,000.00 USD | 5,130,000.00 USD | 5,630,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.35` | 151.46 USD | 6,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `98.50` | 26,350,000.00 USD | 26,350,000.00 USD | 295,480.00 USD | 3,460,000.00 USD | 6,600,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.50` | 59,620,000.00 USD | 59,620,000.00 USD | 1,320,000.00 USD | 6,930,000.00 USD | 1,880,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.55` | 5,930.00 USD | 12,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `98.65` | 9,740.00 USD | 22,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `98.70` | 42,010,000.00 USD | 42,010,000.00 USD | 980,300.00 USD | 5,100,000.00 USD | 9,580,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.70` | 64,610,000.00 USD | 64,610,000.00 USD | 742,060.00 USD | 1,370,000.00 USD | 2,880,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.75` | 1,150.00 USD | 23,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `98.85` | 168.05 USD | 23,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `98.90` | 49,550,000.00 USD | 49,550,000.00 USD | 635,820.00 USD | 2,590,000.00 USD | 4,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.90` | 69,460,000.00 USD | 69,460,000.00 USD | 57,310.00 USD | 1,660,000.00 USD | 3,120,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.95` | 1,350.00 USD | 25,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `99.05` | 3,900.00 USD | 29,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.10` | 59,130,000.00 USD | 59,130,000.00 USD | 1,710,000.00 USD | 2,910,000.00 USD | 4,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `99.10` | 75,860,000.00 USD | 75,860,000.00 USD | 179,190.00 USD | 2,070,000.00 USD | 4,150,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.15` | 1,110,000.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `99.25` | 8,190.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.30` | 68,240,000.00 USD | 68,240,000.00 USD | 3,530,000.00 USD | 3,300,000.00 USD | 2,270,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `99.30` | 82,610,000.00 USD | 82,610,000.00 USD | 798,000.00 USD | 3,060,000.00 USD | 2,890,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.35` | 122,930.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `99.45` | 16,700.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.50` | 73,520,000.00 USD | 73,520,000.00 USD | 1,380,000.00 USD | 3,290,000.00 USD | 619,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `99.50` | 86,850,000.00 USD | 86,850,000.00 USD | 2,240,000.00 USD | 1,490,000.00 USD | 504,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.55` | 9,000.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `99.65` | 3,000.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.70` | 96,380,000.00 USD | 96,380,000.00 USD | 4,390,000.00 USD | 7,320,000.00 USD | 11,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `99.70` | 90,560,000.00 USD | 90,560,000.00 USD | 0.00 USD | 2,490,000.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.75` | 4,160.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `99.85` | 9,130.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.90` | 104,390,000.00 USD | 104,390,000.00 USD | 555,210.00 USD | 1,500,000.00 USD | 5,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `99.90` | 98,700,000.00 USD | 98,700,000.00 USD | 2,860,000.00 USD | 1,420,000.00 USD | 3,850,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.95` | 1,100.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `100.05` | 1,550.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.10` | 109,650,000.00 USD | 109,650,000.00 USD | 2,030,000.00 USD | 2,360,000.00 USD | 877,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.10` | 104,480,000.00 USD | 104,480,000.00 USD | 48,160.00 USD | 1,210,000.00 USD | 4,520,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.15` | 11,860.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `100.25` | 188.47 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.30` | 114,780,000.00 USD | 114,780,000.00 USD | 300,700.00 USD | 2,120,000.00 USD | 2,710,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.30` | 108,090,000.00 USD | 108,090,000.00 USD | 883,050.00 USD | 1,600,000.00 USD | 1,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.35` | 4,300.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.50` | 122,430,000.00 USD | 122,430,000.00 USD | 2,200,000.00 USD | 1,260,000.00 USD | 4,200,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.50` | 116,550,000.00 USD | 116,550,000.00 USD | 2,640,000.00 USD | 765,300.00 USD | 5,050,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.55` | 11,120.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.70` | 129,750,000.00 USD | 129,750,000.00 USD | 1,940,000.00 USD | 2,250,000.00 USD | 3,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.70` | 118,980,000.00 USD | 118,980,000.00 USD | 504,370.00 USD | 1,900,000.00 USD | 23,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.75` | 19,590.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.90` | 135,700,000.00 USD | 135,700,000.00 USD | 1,760,000.00 USD | 2,410,000.00 USD | 1,790,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.90` | 132,080,000.00 USD | 132,080,000.00 USD | 3,480,000.00 USD | 3,730,000.00 USD | 5,890,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.95` | 498.69 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `101.05` | 320.33 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.10` | 149,570,000.00 USD | 149,570,000.00 USD | 8,660,000.00 USD | 2,680,000.00 USD | 2,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.10` | 141,850,000.00 USD | 141,850,000.00 USD | 3,020,000.00 USD | 3,990,000.00 USD | 2,760,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.15` | 24,720.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `101.25` | 769.50 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.30` | 159,770,000.00 USD | 159,770,000.00 USD | 3,460,000.00 USD | 3,950,000.00 USD | 2,800,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.30` | 163,230,000.00 USD | 163,230,000.00 USD | 7,710,000.00 USD | 4,690,000.00 USD | 8,980,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.45` | 118.70 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.50` | 175,920,000.00 USD | 175,920,000.00 USD | 3,050,000.00 USD | 3,960,000.00 USD | 9,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.50` | 178,500,000.00 USD | 178,500,000.00 USD | 2,950,000.00 USD | 738,480.00 USD | 11,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.55` | 66,130.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `101.65` | 5,330.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.70` | 185,620,000.00 USD | 185,620,000.00 USD | 2,320,000.00 USD | 703,520.00 USD | 6,670,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.70` | 188,480,000.00 USD | 188,480,000.00 USD | 2,950,000.00 USD | 484,140.00 USD | 6,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `101.90` | 191,190,000.00 USD | 191,190,000.00 USD | 2,100,000.00 USD | 823,320.00 USD | 2,650,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.90` | 197,180,000.00 USD | 197,180,000.00 USD | 3,710,000.00 USD | 867,880.00 USD | 4,120,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.05` | 8,970.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.10` | 197,200,000.00 USD | 197,200,000.00 USD | 2,830,000.00 USD | 1,270,000.00 USD | 1,900,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.10` | 202,830,000.00 USD | 202,830,000.00 USD | 1,470,000.00 USD | 159,070.00 USD | 4,030,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.25` | 1,170.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.30` | 202,100,000.00 USD | 202,100,000.00 USD | 1,650,000.00 USD | 1,450,000.00 USD | 1,800,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.30` | 208,890,000.00 USD | 208,890,000.00 USD | 2,700,000.00 USD | 807,930.00 USD | 2,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.35` | 11,300.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `102.45` | 175.19 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.50` | 206,420,000.00 USD | 206,420,000.00 USD | 1,510,000.00 USD | 785,070.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.50` | 212,540,000.00 USD | 212,540,000.00 USD | 1,240,000.00 USD | 1,280,000.00 USD | 1,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.65` | 1,500.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.70` | 208,310,000.00 USD | 208,310,000.00 USD | 1,110,000.00 USD | 661,840.00 USD | 121,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.70` | 213,340,000.00 USD | 213,340,000.00 USD | 766,460.00 USD | 14,010.00 USD | 16,660.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.75` | 3,070.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `102.85` | 7,350.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.90` | 212,850,000.00 USD | 212,850,000.00 USD | 1,510,000.00 USD | 1,530,000.00 USD | 1,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.90` | 234,630,000.00 USD | 234,630,000.00 USD | 17,210,000.00 USD | 294,050.00 USD | 3,780,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.95` | 4,150.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `103.05` | 1,760.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.10` | 217,800,000.00 USD | 217,800,000.00 USD | 2,380,000.00 USD | 1,360,000.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.10` | 240,860,000.00 USD | 240,860,000.00 USD | 4,750,000.00 USD | 140,720.00 USD | 1,340,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.15` | 11,000.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.30` | 219,620,000.00 USD | 219,620,000.00 USD | 334,720.00 USD | 717,010.00 USD | 769,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.30` | 256,540,000.00 USD | 256,540,000.00 USD | 15,130,000.00 USD | 133,780.00 USD | 417,110.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.35` | 907.41 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `103.45` | 3,300.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.50` | 226,210,000.00 USD | 226,210,000.00 USD | 1,770,000.00 USD | 1,090,000.00 USD | 3,730,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.50` | 278,950,000.00 USD | 278,950,000.00 USD | 13,780,000.00 USD | 1,770,000.00 USD | 6,860,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.55` | 1,440,000.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `103.65` | 4,360.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.70` | 231,420,000.00 USD | 231,420,000.00 USD | 1,610,000.00 USD | 971,510.00 USD | 2,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.70` | 291,170,000.00 USD | 291,170,000.00 USD | 8,190,000.00 USD | 1,320,000.00 USD | 2,710,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.75` | 262,190.00 USD | 3,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `103.85` | 13,560.00 USD | 3,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.90` | 237,230,000.00 USD | 237,230,000.00 USD | 2,080,000.00 USD | 2,200,000.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.90` | 309,210,000.00 USD | 309,210,000.00 USD | 9,120,000.00 USD | 2,880,000.00 USD | 6,040,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.95` | 1,490.00 USD | 3,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.05` | 1,400.00 USD | 3,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.10` | 244,330,000.00 USD | 244,330,000.00 USD | 2,850,000.00 USD | 1,270,000.00 USD | 2,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.10` | 338,140,000.00 USD | 338,140,000.00 USD | 11,570,000.00 USD | 8,350,000.00 USD | 9,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.15` | 1,180.00 USD | 3,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.25` | 426,950.00 USD | 3,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.30` | 248,240,000.00 USD | 248,240,000.00 USD | 1,400,000.00 USD | 1,440,000.00 USD | 1,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.30` | 359,720,000.00 USD | 359,720,000.00 USD | 7,320,000.00 USD | 6,380,000.00 USD | 7,870,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.35` | 13,740.00 USD | 3,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.45` | 20,910.00 USD | 3,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.50` | 252,340,000.00 USD | 252,340,000.00 USD | 1,430,000.00 USD | 1,220,000.00 USD | 1,450,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.50` | 371,740,000.00 USD | 371,740,000.00 USD | 4,410,000.00 USD | 2,350,000.00 USD | 5,270,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.55` | 10,810.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.65` | 925.11 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.70` | 258,130,000.00 USD | 258,130,000.00 USD | 1,720,000.00 USD | 982,920.00 USD | 3,090,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.70` | 391,930,000.00 USD | 391,930,000.00 USD | 6,680,000.00 USD | 4,660,000.00 USD | 8,860,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.75` | 199.02 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.90` | 259,610,000.00 USD | 259,610,000.00 USD | 486,940.00 USD | 283,560.00 USD | 706,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.90` | 412,800,000.00 USD | 412,800,000.00 USD | 5,970,000.00 USD | 5,350,000.00 USD | 9,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.95` | 125,660.00 USD | 3,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `105.05` | 329.86 USD | 3,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.10` | 261,450,000.00 USD | 261,450,000.00 USD | 299,230.00 USD | 436,680.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.10` | 425,610,000.00 USD | 425,610,000.00 USD | 5,580,000.00 USD | 4,400,000.00 USD | 2,830,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.15` | 6,410.00 USD | 3,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `105.25` | 1,040.00 USD | 3,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.30` | 261,640,000.00 USD | 261,640,000.00 USD | 94,380.00 USD | 96,460.00 USD | 1,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.30` | 429,950,000.00 USD | 429,950,000.00 USD | 2,410,000.00 USD | 1,310,000.00 USD | 623,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.35` | 1,650.00 USD | 3,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `105.45` | 529,050.00 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.50` | 262,250,000.00 USD | 262,250,000.00 USD | 245,610.00 USD | 180,000.00 USD | 186,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.50` | 448,330,000.00 USD | 448,330,000.00 USD | 5,600,000.00 USD | 5,850,000.00 USD | 6,930,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.55` | 8,190.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.70` | 262,470,000.00 USD | 262,470,000.00 USD | 65,040.00 USD | 150,210.00 USD | 3,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.70` | 460,070,000.00 USD | 460,070,000.00 USD | 3,430,000.00 USD | 3,740,000.00 USD | 4,570,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.75` | 247.45 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `105.85` | 91,370.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.90` | 263,520,000.00 USD | 263,520,000.00 USD | 171,160.00 USD | 683,690.00 USD | 193,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.90` | 468,960,000.00 USD | 468,960,000.00 USD | 3,110,000.00 USD | 1,880,000.00 USD | 3,900,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.95` | 592.26 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `106.05` | 33,380.00 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.10` | 264,910,000.00 USD | 264,910,000.00 USD | 706,860.00 USD | 457,510.00 USD | 226,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.10` | 479,560,000.00 USD | 479,560,000.00 USD | 4,910,000.00 USD | 2,870,000.00 USD | 2,820,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.25` | 191.25 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.30` | 266,060,000.00 USD | 266,060,000.00 USD | 281,270.00 USD | 484,380.00 USD | 391,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.30` | 487,960,000.00 USD | 487,960,000.00 USD | 3,400,000.00 USD | 2,850,000.00 USD | 2,150,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.35` | 252,220.00 USD | 4,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `106.45` | 32,940.00 USD | 4,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.50` | 266,750,000.00 USD | 266,750,000.00 USD | 229,790.00 USD | 216,810.00 USD | 239,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.50` | 492,670,000.00 USD | 492,670,000.00 USD | 1,520,000.00 USD | 1,440,000.00 USD | 1,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `106.70` | 268,880,000.00 USD | 268,880,000.00 USD | 565,590.00 USD | 249,950.00 USD | 1,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.70` | 500,760,000.00 USD | 500,760,000.00 USD | 1,820,000.00 USD | 2,330,000.00 USD | 3,940,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.75` | 397,560.00 USD | 5,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `106.85` | 480,860.00 USD | 5,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.90` | 269,350,000.00 USD | 269,350,000.00 USD | 10,160.00 USD | 156,020.00 USD | 305,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.90` | 505,820,000.00 USD | 505,820,000.00 USD | 789,400.00 USD | 1,150,000.00 USD | 3,120,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.95` | 651.33 USD | 5,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.05` | 17,260.00 USD | 5,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.10` | 270,400,000.00 USD | 270,400,000.00 USD | 97,170.00 USD | 366,280.00 USD | 580,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.10` | 509,930,000.00 USD | 509,930,000.00 USD | 1,630,000.00 USD | 799,480.00 USD | 1,680,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.15` | 3,060.00 USD | 5,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.25` | 47,370.00 USD | 5,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.30` | 270,760,000.00 USD | 270,760,000.00 USD | 82,550.00 USD | 174,420.00 USD | 110,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.30` | 510,380,000.00 USD | 510,380,000.00 USD | 0.00 USD | 451,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.35` | 766.48 USD | 5,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.45` | 32,580.00 USD | 5,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.50` | 271,870,000.00 USD | 271,870,000.00 USD | 50,930.00 USD | 253,000.00 USD | 805,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.50` | 511,620,000.00 USD | 511,620,000.00 USD | 5,920.00 USD | 286,950.00 USD | 946,020.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.55` | 221.55 USD | 5,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.65` | 1,820.00 USD | 5,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.70` | 272,100,000.00 USD | 272,100,000.00 USD | 0.00 USD | 0.00 USD | 230,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.70` | 512,600,000.00 USD | 512,600,000.00 USD | 523,660.00 USD | 10,400.00 USD | 444,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.85` | 143,340.00 USD | 5,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.90` | 272,400,000.00 USD | 272,400,000.00 USD | 83,370.00 USD | 73,830.00 USD | 136,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.90` | 513,120,000.00 USD | 513,120,000.00 USD | 173,590.00 USD | 20,610.00 USD | 331,480.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.05` | 1,080.00 USD | 5,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `108.10` | 272,500,000.00 USD | 272,500,000.00 USD | 0.00 USD | 99,900.00 USD | 1,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `108.10` | 513,380,000.00 USD | 513,380,000.00 USD | 5,950.00 USD | 248,110.00 USD | 7,130.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.15` | 1,150.00 USD | 5,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.25` | 116.91 USD | 5,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `108.30` | 272,530,000.00 USD | 272,530,000.00 USD | 33,880.00 USD | 1,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `108.30` | 514,510,000.00 USD | 514,510,000.00 USD | 303,300.00 USD | 464,990.00 USD | 359,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.35` | 3,470.00 USD | 5,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.45` | 111,070.00 USD | 6,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `108.50` | 273,230,000.00 USD | 273,230,000.00 USD | 163,220.00 USD | 122,230.00 USD | 413,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `108.50` | 514,910,000.00 USD | 514,910,000.00 USD | 395,570.00 USD | 3,960.00 USD | 2,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.55` | 117.23 USD | 6,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `108.60` | 273,350,000.00 USD | 273,350,000.00 USD | 118,190.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.65` | 22,400.00 USD | 6,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.70` | 516,790,000.00 USD | 516,790,000.00 USD | 557,190.00 USD | 529,990.00 USD | 792,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.85` | 3,230.00 USD | 6,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.90` | 518,230,000.00 USD | 518,230,000.00 USD | 363,550.00 USD | 494,000.00 USD | 580,220.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.95` | 3,170.00 USD | 6,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.05` | 163.58 USD | 6,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `109.10` | 519,060,000.00 USD | 519,060,000.00 USD | 289,830.00 USD | 185,250.00 USD | 354,460.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.15` | 2,120.00 USD | 6,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `109.30` | 520,220,000.00 USD | 520,220,000.00 USD | 503,000.00 USD | 91,380.00 USD | 569,620.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.35` | 247.13 USD | 6,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.45` | 342.58 USD | 6,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `109.50` | 520,460,000.00 USD | 520,460,000.00 USD | 230,320.00 USD | 4,290.00 USD | 5,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.55` | 356.04 USD | 6,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.65` | 42,030.00 USD | 6,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `109.70` | 521,650,000.00 USD | 521,650,000.00 USD | 550,380.00 USD | 185,990.00 USD | 444,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.85` | 459.17 USD | 6,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `109.90` | 523,450,000.00 USD | 523,450,000.00 USD | 446,430.00 USD | 547,840.00 USD | 807,700.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.95` | 301.26 USD | 6,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `110.10` | 525,820,000.00 USD | 525,820,000.00 USD | 967,200.00 USD | 531,910.00 USD | 868,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `110.15` | 3,170.00 USD | 6,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `110.30` | 527,900,000.00 USD | 527,900,000.00 USD | 936,750.00 USD | 342,020.00 USD | 802,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `110.35` | 158.90 USD | 6,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.45` | 143,390.00 USD | 6,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `110.50` | 528,380,000.00 USD | 528,380,000.00 USD | 246,210.00 USD | 10,300.00 USD | 225,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `110.55` | 580.39 USD | 6,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.65` | 10,240.00 USD | 6,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `110.70` | 530,570,000.00 USD | 530,570,000.00 USD | 793,510.00 USD | 765,020.00 USD | 634,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `110.75` | 575.90 USD | 6,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.85` | 1,090.00 USD | 6,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.95` | 5,040.00 USD | 6,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.15` | 1,710.00 USD | 6,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.35` | 390.84 USD | 6,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.45` | 1,390.00 USD | 6,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.75` | 169.86 USD | 6,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.85` | 44,370.00 USD | 6,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.95` | 260,360.00 USD | 6,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.15` | 291.59 USD | 6,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.35` | 1,910.00 USD | 6,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.45` | 8,710.00 USD | 6,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.55` | 844.13 USD | 6,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.65` | 707.44 USD | 6,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.75` | 118,640.00 USD | 6,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.85` | 108,760.00 USD | 6,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.05` | 406.98 USD | 6,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.15` | 9,560.00 USD | 6,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.25` | 3,840.00 USD | 6,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.35` | 1,240.00 USD | 6,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.45` | 3,480.00 USD | 6,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.55` | 102,780.00 USD | 6,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.65` | 3,220.00 USD | 6,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.75` | 303.71 USD | 6,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.85` | 104.74 USD | 6,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.95` | 21,840.00 USD | 6,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.05` | 31,740.00 USD | 7,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.25` | 2,150.00 USD | 7,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.45` | 3,310.00 USD | 7,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.05` | 569,710.00 USD | 7,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.15` | 1,100.00 USD | 7,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.35` | 14,710.00 USD | 7,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.45` | 906,520.00 USD | 8,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.55` | 43,020.00 USD | 8,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.75` | 160.89 USD | 8,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.85` | 4,340.00 USD | 8,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.05` | 4,450.00 USD | 8,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.25` | 180.19 USD | 8,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.35` | 4,960.00 USD | 8,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.55` | 2,040.00 USD | 8,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.65` | 113.15 USD | 8,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.85` | 99,900.00 USD | 8,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.05` | 156.85 USD | 8,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.15` | 89,950.00 USD | 8,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.25` | 4,770,000.00 USD | 13,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.35` | 11,840.00 USD | 13,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.45` | 1,500.00 USD | 13,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.55` | 1,920.00 USD | 13,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.75` | 10,360.00 USD | 13,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.85` | 555,010.00 USD | 14,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.95` | 44,800.00 USD | 14,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.15` | 4,480,000.00 USD | 18,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.45` | 53,770.00 USD | 18,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.55` | 1,110.00 USD | 18,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.75` | 309.94 USD | 18,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.95` | 10,930.00 USD | 18,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.15` | 2,350.00 USD | 18,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.25` | 28,090.00 USD | 18,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.35` | 70,380.00 USD | 18,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.75` | 261.06 USD | 18,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.85` | 485.39 USD | 18,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.95` | 96,050.00 USD | 18,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.05` | 452.59 USD | 18,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.15` | 2,980.00 USD | 18,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.45` | 145.74 USD | 18,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.55` | 1,190.00 USD | 18,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.65` | 869,200.00 USD | 19,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.95` | 13,290.00 USD | 19,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.15` | 316.20 USD | 19,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.55` | 5,940.00 USD | 19,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.75` | 105.92 USD | 19,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.05` | 56,150.00 USD | 19,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.15` | 819.63 USD | 19,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.25` | 2,330.00 USD | 19,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.45` | 17,500.00 USD | 19,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.55` | 1,580.00 USD | 19,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.65` | 840.15 USD | 19,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.85` | 342.75 USD | 19,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.95` | 2,170.00 USD | 19,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.25` | 188.57 USD | 19,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.35` | 127,060.00 USD | 20,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.45` | 1,960.00 USD | 20,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.95` | 9,140,000.00 USD | 29,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.05` | 586.76 USD | 29,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.15` | 121.67 USD | 29,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.25` | 23,360.00 USD | 29,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.35` | 114.40 USD | 29,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.55` | 3,080.00 USD | 29,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.65` | 675.60 USD | 29,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.75` | 51,550.00 USD | 29,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.95` | 2,800.00 USD | 29,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.05` | 208.83 USD | 29,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.35` | 6,780.00 USD | 29,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.45` | 5,910.00 USD | 29,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.55` | 4,610.00 USD | 29,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.65` | 851.91 USD | 29,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.75` | 4,600.00 USD | 29,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.95` | 110.84 USD | 29,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.15` | 1,280.00 USD | 29,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.35` | 4,090.00 USD | 29,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.45` | 253,020.00 USD | 29,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.55` | 318.91 USD | 29,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.65` | 31,130.00 USD | 29,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.85` | 3,870.00 USD | 29,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.05` | 2,030.00 USD | 29,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.35` | 16,190.00 USD | 29,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.55` | 1,650.00 USD | 29,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.65` | 4,840.00 USD | 29,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.75` | 720.51 USD | 29,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.85` | 388.66 USD | 29,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.95` | 10,510.00 USD | 29,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.05` | 116,190.00 USD | 29,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.15` | 6,410.00 USD | 29,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.35` | 195.09 USD | 29,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.65` | 788.62 USD | 29,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.75` | 18,730.00 USD | 29,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.85` | 41,020.00 USD | 29,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.15` | 55,570.00 USD | 29,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.25` | 730,990.00 USD | 30,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.35` | 68,800.00 USD | 30,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.55` | 910.74 USD | 30,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.75` | 2,210.00 USD | 30,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.85` | 490.83 USD | 30,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.15` | 13,190.00 USD | 30,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.35` | 145.99 USD | 30,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.85` | 503,820.00 USD | 31,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.95` | 2,070.00 USD | 31,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.05` | 188.71 USD | 31,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.25` | 1,560.00 USD | 31,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.35` | 855.09 USD | 31,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.45` | 219.52 USD | 31,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.75` | 3,600.00 USD | 31,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.85` | 3,100.00 USD | 31,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.95` | 240.15 USD | 31,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.05` | 11,940.00 USD | 31,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.15` | 325.09 USD | 31,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.55` | 8,730.00 USD | 31,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.65` | 630.09 USD | 31,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.75` | 66,380.00 USD | 31,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.85` | 49,280.00 USD | 31,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.05` | 30,050.00 USD | 31,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.15` | 8,440.00 USD | 31,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.35` | 47,960.00 USD | 31,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.65` | 156.37 USD | 31,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.75` | 151,200.00 USD | 31,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.95` | 2,110.00 USD | 31,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.05` | 12,620.00 USD | 31,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.25` | 36,990.00 USD | 31,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.95` | 4,040.00 USD | 31,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.45` | 6,410.00 USD | 31,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.85` | 3,250.00 USD | 31,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.95` | 504.37 USD | 31,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.05` | 1,400.00 USD | 31,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.55` | 136.55 USD | 31,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.65` | 1,110.00 USD | 31,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.75` | 14,700.00 USD | 31,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.95` | 34,240.00 USD | 31,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.05` | 836.00 USD | 31,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.15` | 809.19 USD | 31,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.45` | 696.87 USD | 31,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.65` | 2,050.00 USD | 31,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.85` | 105,020.00 USD | 31,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.95` | 2,820.00 USD | 31,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.05` | 1,270.00 USD | 31,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.15` | 41,450.00 USD | 31,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.25` | 45,220.00 USD | 31,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.45` | 50,490.00 USD | 31,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.75` | 2,360.00 USD | 31,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.95` | 653.06 USD | 31,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.05` | 13,180.00 USD | 31,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.15` | 552.43 USD | 31,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.25` | 392.69 USD | 31,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.45` | 253.80 USD | 31,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.55` | 2,170.00 USD | 31,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.65` | 8,990.00 USD | 31,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.75` | 136.95 USD | 31,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.95` | 394.66 USD | 31,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.05` | 116.24 USD | 31,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.25` | 625.51 USD | 31,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.35` | 12,760.00 USD | 31,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.45` | 4,870.00 USD | 31,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.55` | 702.75 USD | 31,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.65` | 26,180.00 USD | 31,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.75` | 67,230.00 USD | 32,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.95` | 1,940.00 USD | 32,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.05` | 5,020,000.00 USD | 37,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.35` | 210.61 USD | 37,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.45` | 2,190,000.00 USD | 39,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.55` | 236.39 USD | 39,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.75` | 27,660.00 USD | 39,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.85` | 916.35 USD | 39,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.95` | 112.14 USD | 39,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.45` | 151.00 USD | 39,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.65` | 2,150.00 USD | 39,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.75` | 368.30 USD | 39,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.15` | 1,330.00 USD | 39,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.35` | 22,260.00 USD | 39,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.45` | 2,830.00 USD | 39,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.65` | 23,220.00 USD | 39,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.75` | 2,690.00 USD | 39,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.85` | 597,720.00 USD | 39,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.05` | 3,750.00 USD | 39,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.55` | 105,540.00 USD | 40,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.65` | 1,240.00 USD | 40,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.95` | 87,650.00 USD | 40,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.15` | 1,760.00 USD | 40,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.45` | 30,330.00 USD | 40,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.85` | 6,340.00 USD | 40,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.15` | 88,760.00 USD | 40,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.25` | 2,770.00 USD | 40,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.35` | 7,330.00 USD | 40,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.45` | 439,350.00 USD | 40,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.55` | 1,280.00 USD | 40,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.65` | 587,730.00 USD | 41,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.85` | 2,120.00 USD | 41,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.95` | 3,070.00 USD | 41,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.05` | 1,570.00 USD | 41,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.15` | 1,730.00 USD | 41,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.35` | 169.45 USD | 41,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.45` | 204.96 USD | 41,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.55` | 1,000.00 USD | 41,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.65` | 237.72 USD | 41,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.85` | 300.14 USD | 41,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.95` | 78,960.00 USD | 41,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.15` | 518,630.00 USD | 41,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.45` | 163.29 USD | 41,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.55` | 350,430.00 USD | 42,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.65` | 1,110.00 USD | 42,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.75` | 2,390.00 USD | 42,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.85` | 91,370.00 USD | 42,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.95` | 527.28 USD | 42,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.05` | 160,350.00 USD | 42,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.15` | 1,120.00 USD | 42,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.25` | 1,390,000.00 USD | 43,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.45` | 16,290.00 USD | 43,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.55` | 116.65 USD | 43,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.65` | 16,030.00 USD | 43,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.95` | 178.44 USD | 43,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.05` | 2,930.00 USD | 43,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.25` | 123,390.00 USD | 44,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.75` | 346.72 USD | 44,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.85` | 19,690.00 USD | 44,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.15` | 5,960.00 USD | 44,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.35` | 1,740,000.00 USD | 45,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.45` | 8,830.00 USD | 45,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.65` | 29,420.00 USD | 45,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.95` | 1,110,000.00 USD | 46,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.25` | 44,800.00 USD | 47,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.35` | 286,550.00 USD | 47,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.45` | 3,150.00 USD | 47,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.55` | 423,220.00 USD | 47,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.75` | 1,570.00 USD | 47,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.05` | 44,580.00 USD | 47,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.15` | 1,060.00 USD | 47,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.35` | 2,300.00 USD | 47,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.55` | 1,490.00 USD | 47,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.65` | 8,340.00 USD | 47,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.95` | 766,050.00 USD | 48,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.05` | 223.37 USD | 48,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.15` | 1,230.00 USD | 48,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.25` | 2,340.00 USD | 48,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.45` | 4,240.00 USD | 48,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.55` | 363.19 USD | 48,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.65` | 4,690,000.00 USD | 53,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.35` | 118.07 USD | 53,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.55` | 267.55 USD | 53,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.05` | 7,800.00 USD | 53,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.35` | 197.00 USD | 53,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.45` | 303,040.00 USD | 53,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.75` | 327.61 USD | 53,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.85` | 18,370.00 USD | 53,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.15` | 49,270.00 USD | 53,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.55` | 236,620.00 USD | 53,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.65` | 654.25 USD | 53,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.75` | 92,600.00 USD | 53,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.05` | 312.94 USD | 53,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.25` | 528,060.00 USD | 54,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.55` | 1,410.00 USD | 54,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.95` | 27,860.00 USD | 54,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.05` | 45,350.00 USD | 54,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.45` | 80,530.00 USD | 54,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.65` | 1,760.00 USD | 54,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.85` | 497.13 USD | 54,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.15` | 683,000.00 USD | 55,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.35` | 655.83 USD | 55,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.65` | 321,300.00 USD | 55,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.95` | 141,540.00 USD | 55,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.05` | 2,240.00 USD | 55,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.15` | 85,850.00 USD | 55,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.35` | 5,680,000.00 USD | 61,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.55` | 410.34 USD | 61,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.95` | 144,610.00 USD | 61,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `162.05` | 113,440.00 USD | 61,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `162.65` | 107,780.00 USD | 61,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `162.95` | 1,350.00 USD | 61,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.05` | 16,310.00 USD | 61,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.35` | 1,060.00 USD | 61,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.65` | 3,080.00 USD | 61,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.85` | 786.48 USD | 61,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.95` | 206,830.00 USD | 62,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `164.25` | 614.30 USD | 62,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `164.95` | 17,050.00 USD | 62,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `165.15` | 198.18 USD | 62,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.05` | 830.25 USD | 62,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.15` | 7,650.00 USD | 62,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.25` | 14,070.00 USD | 62,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.65` | 67,790.00 USD | 62,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.75` | 3,440.00 USD | 62,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.25` | 274.29 USD | 62,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.65` | 115.68 USD | 62,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.75` | 1,890.00 USD | 62,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.05` | 273.92 USD | 62,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.35` | 19,740.00 USD | 62,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.65` | 325,850.00 USD | 62,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `169.25` | 3,270.00 USD | 62,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `169.85` | 180,350.00 USD | 62,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.45` | 111.44 USD | 62,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.55` | 20,420.00 USD | 62,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `172.45` | 79,660.00 USD | 62,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `172.85` | 200,310.00 USD | 63,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.05` | 204.20 USD | 63,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.25` | 1,190.00 USD | 63,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.45` | 52,230.00 USD | 63,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.85` | 695.40 USD | 63,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.15` | 104,490.00 USD | 63,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.25` | 245,010.00 USD | 63,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.35` | 205,490.00 USD | 63,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.75` | 146.79 USD | 63,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.05` | 38,510,000.00 USD | 102,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.45` | 119.31 USD | 102,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.55` | 105,720.00 USD | 102,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.75` | 20,140.00 USD | 102,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.85` | 1,300.00 USD | 102,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.05` | 3,520,000.00 USD | 105,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.25` | 625.69 USD | 105,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.45` | 3,650.00 USD | 105,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.65` | 26,250.00 USD | 105,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.85` | 2,800.00 USD | 105,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.35` | 4,430.00 USD | 105,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.65` | 142,760.00 USD | 106,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.95` | 1,380,000.00 USD | 107,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `178.15` | 46,610.00 USD | 107,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `178.55` | 4,950.00 USD | 107,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.35` | 2,960,000.00 USD | 110,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.75` | 154.59 USD | 110,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.05` | 116,670.00 USD | 110,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.45` | 245.41 USD | 110,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.55` | 38,150.00 USD | 110,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.75` | 146.41 USD | 110,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.95` | 10,720.00 USD | 110,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.25` | 18,120.00 USD | 110,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.55` | 254.17 USD | 110,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.95` | 3,640,000.00 USD | 114,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `182.15` | 3,990.00 USD | 114,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `182.95` | 788.51 USD | 114,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `183.55` | 73,420.00 USD | 114,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.25` | 1,680.00 USD | 114,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.75` | 7,650.00 USD | 114,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.95` | 165,230.00 USD | 114,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.05` | 53,160.00 USD | 114,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.25` | 737.29 USD | 114,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.35` | 10,940.00 USD | 114,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.45` | 2,770.00 USD | 114,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.55` | 1,220.00 USD | 114,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.65` | 137.38 USD | 114,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.75` | 390.07 USD | 114,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `186.15` | 247.58 USD | 114,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `186.85` | 2,190.00 USD | 114,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `186.95` | 4,110.00 USD | 114,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.45` | 232.44 USD | 114,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.75` | 2,820.00 USD | 114,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.85` | 1,560.00 USD | 114,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.55` | 1,020.00 USD | 114,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.65` | 29,340.00 USD | 114,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.75` | 2,470.00 USD | 114,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.95` | 1,450.00 USD | 114,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.25` | 456.09 USD | 114,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.85` | 189.85 USD | 114,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.95` | 284,930.00 USD | 114,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.05` | 1,010.00 USD | 114,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.15` | 148.32 USD | 114,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.45` | 236.16 USD | 114,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.85` | 5,410.00 USD | 114,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.95` | 13,950,000.00 USD | 128,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.25` | 62,750.00 USD | 128,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.95` | 322.48 USD | 128,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `192.35` | 192.35 USD | 128,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `192.95` | 9,320.00 USD | 128,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `193.25` | 1,380.00 USD | 128,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `193.55` | 114,580.00 USD | 129,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `19.75` | 123,230,000.00 USD | 0.00 USD | 14,120.00 USD | `-79.69%` | `714.78` |
| `Live` | `Long` | `19.85` | 123,220,000.00 USD | 0.00 USD | 1,100.00 USD | `-79.59%` | `55.25` |
| `Live` | `Long` | `20.55` | 123,210,000.00 USD | 0.00 USD | 4,790.00 USD | `-78.87%` | `233.31` |
| `Live` | `Long` | `21.15` | 123,210,000.00 USD | 0.00 USD | 10,580.00 USD | `-78.25%` | `500.00` |
| `Live` | `Long` | `21.35` | 123,200,000.00 USD | 0.00 USD | 1,780.00 USD | `-78.04%` | `83.55` |
| `Live` | `Long` | `21.45` | 123,200,000.00 USD | 0.00 USD | 381.81 USD | `-77.94%` | `17.80` |
| `Live` | `Long` | `21.55` | 123,200,000.00 USD | 0.00 USD | 246.96 USD | `-77.84%` | `11.46` |
| `Live` | `Long` | `21.75` | 123,200,000.00 USD | 0.00 USD | 4,630.00 USD | `-77.63%` | `212.70` |
| `Live` | `Long` | `21.85` | 123,190,000.00 USD | 0.00 USD | 5,130.00 USD | `-77.53%` | `234.80` |
| `Live` | `Long` | `22.05` | 123,190,000.00 USD | 0.00 USD | 1,100.00 USD | `-77.32%` | `50.00` |
| `Live` | `Long` | `22.25` | 123,190,000.00 USD | 0.00 USD | 132.39 USD | `-77.12%` | `5.95` |
| `Live` | `Long` | `22.45` | 123,190,000.00 USD | 0.00 USD | 111.13 USD | `-76.91%` | `4.95` |
| `Live` | `Long` | `22.55` | 123,190,000.00 USD | 0.00 USD | 359.00 USD | `-76.81%` | `15.92` |
| `Live` | `Long` | `22.75` | 123,190,000.00 USD | 0.00 USD | 820,950.00 USD | `-76.60%` | `36,085.73` |
| `Live` | `Long` | `22.95` | 122,360,000.00 USD | 0.00 USD | 13,280.00 USD | `-76.40%` | `578.65` |
| `Live` | `Long` | `23.15` | 122,350,000.00 USD | 0.00 USD | 243.31 USD | `-76.19%` | `10.51` |
| `Live` | `Long` | `23.35` | 122,350,000.00 USD | 0.00 USD | 1,170.00 USD | `-75.99%` | `50.00` |
| `Live` | `Long` | `23.45` | 122,350,000.00 USD | 0.00 USD | 1,380.00 USD | `-75.88%` | `58.86` |
| `Live` | `Long` | `23.65` | 122,350,000.00 USD | 0.00 USD | 10,610.00 USD | `-75.68%` | `448.61` |
| `Live` | `Long` | `23.85` | 122,340,000.00 USD | 0.00 USD | 9,650.00 USD | `-75.47%` | `404.81` |
| `Live` | `Long` | `24.05` | 122,330,000.00 USD | 0.00 USD | 5,170.00 USD | `-75.27%` | `214.84` |
| `Live` | `Long` | `24.15` | 122,320,000.00 USD | 0.00 USD | 1,860.00 USD | `-75.16%` | `77.00` |
| `Live` | `Long` | `24.25` | 122,320,000.00 USD | 0.00 USD | 21,710.00 USD | `-75.06%` | `895.32` |
| `Live` | `Long` | `24.45` | 122,300,000.00 USD | 0.00 USD | 1,220.00 USD | `-74.86%` | `50.00` |
| `Live` | `Long` | `24.65` | 122,300,000.00 USD | 0.00 USD | 5,050.00 USD | `-74.65%` | `204.86` |
| `Live` | `Long` | `25.05` | 122,290,000.00 USD | 0.00 USD | 3,390.00 USD | `-74.24%` | `135.17` |
| `Live` | `Long` | `25.15` | 122,290,000.00 USD | 0.00 USD | 2,010.00 USD | `-74.14%` | `80.00` |
| `Live` | `Long` | `25.45` | 122,290,000.00 USD | 0.00 USD | 305.40 USD | `-73.83%` | `12.00` |
| `Live` | `Long` | `25.55` | 122,290,000.00 USD | 0.00 USD | 107.05 USD | `-73.72%` | `4.19` |
| `Live` | `Long` | `25.95` | 122,290,000.00 USD | 0.00 USD | 2,930.00 USD | `-73.31%` | `113.00` |
| `Live` | `Long` | `26.05` | 122,280,000.00 USD | 0.00 USD | 155,010.00 USD | `-73.21%` | `5,950.44` |
| `Live` | `Long` | `26.25` | 122,130,000.00 USD | 0.00 USD | 837.90 USD | `-73.00%` | `31.92` |
| `Live` | `Long` | `26.35` | 122,130,000.00 USD | 0.00 USD | 475.09 USD | `-72.90%` | `18.03` |
| `Live` | `Long` | `26.65` | 122,130,000.00 USD | 0.00 USD | 412.28 USD | `-72.59%` | `15.47` |
| `Live` | `Long` | `26.95` | 122,130,000.00 USD | 0.00 USD | 10,840.00 USD | `-72.29%` | `402.05` |
| `Live` | `Long` | `27.15` | 122,120,000.00 USD | 0.00 USD | 382.00 USD | `-72.08%` | `14.07` |
| `Live` | `Long` | `27.25` | 122,120,000.00 USD | 0.00 USD | 1,170.00 USD | `-71.98%` | `43.06` |
| `Live` | `Long` | `27.35` | 122,120,000.00 USD | 0.00 USD | 595.96 USD | `-71.87%` | `21.79` |
| `Live` | `Long` | `27.45` | 122,110,000.00 USD | 0.00 USD | 686.25 USD | `-71.77%` | `25.00` |
| `Live` | `Long` | `27.55` | 122,110,000.00 USD | 0.00 USD | 142.16 USD | `-71.67%` | `5.16` |
| `Live` | `Long` | `27.85` | 122,110,000.00 USD | 0.00 USD | 412.18 USD | `-71.36%` | `14.80` |
| `Live` | `Long` | `28.05` | 122,110,000.00 USD | 0.00 USD | 2,740.00 USD | `-71.15%` | `97.63` |
| `Live` | `Long` | `28.25` | 122,110,000.00 USD | 0.00 USD | 87,290.00 USD | `-70.95%` | `3,090.00` |
| `Live` | `Long` | `28.35` | 122,020,000.00 USD | 0.00 USD | 9,480.00 USD | `-70.85%` | `334.22` |
| `Live` | `Long` | `28.45` | 122,010,000.00 USD | 0.00 USD | 15,020.00 USD | `-70.74%` | `527.99` |
| `Live` | `Long` | `28.85` | 122,000,000.00 USD | 0.00 USD | 2,310.00 USD | `-70.33%` | `80.00` |
| `Live` | `Long` | `28.95` | 122,000,000.00 USD | 0.00 USD | 424.41 USD | `-70.23%` | `14.66` |
| `Live` | `Long` | `29.05` | 122,000,000.00 USD | 0.00 USD | 9,880.00 USD | `-70.13%` | `340.00` |
| `Live` | `Long` | `29.15` | 121,990,000.00 USD | 0.00 USD | 9,830.00 USD | `-70.02%` | `337.19` |
| `Live` | `Long` | `29.35` | 121,980,000.00 USD | 0.00 USD | 260.04 USD | `-69.82%` | `8.86` |
| `Live` | `Long` | `29.45` | 121,980,000.00 USD | 0.00 USD | 33,030.00 USD | `-69.71%` | `1,121.64` |
| `Live` | `Long` | `29.75` | 121,940,000.00 USD | 0.00 USD | 1,680.00 USD | `-69.41%` | `56.43` |
| `Live` | `Long` | `29.95` | 121,940,000.00 USD | 0.00 USD | 45,160.00 USD | `-69.20%` | `1,508.00` |
| `Live` | `Long` | `30.05` | 121,900,000.00 USD | 0.00 USD | 3,010.00 USD | `-69.10%` | `100.04` |
| `Live` | `Long` | `30.15` | 121,890,000.00 USD | 0.00 USD | 66,180.00 USD | `-68.99%` | `2,195.00` |
| `Live` | `Long` | `30.25` | 121,830,000.00 USD | 0.00 USD | 9,160.00 USD | `-68.89%` | `302.84` |
| `Live` | `Long` | `30.55` | 121,820,000.00 USD | 0.00 USD | 3,210.00 USD | `-68.58%` | `104.93` |
| `Live` | `Long` | `30.65` | 121,810,000.00 USD | 0.00 USD | 233.86 USD | `-68.48%` | `7.63` |
| `Live` | `Long` | `30.85` | 121,810,000.00 USD | 0.00 USD | 157.64 USD | `-68.27%` | `5.11` |
| `Live` | `Long` | `31.05` | 121,810,000.00 USD | 0.00 USD | 621.00 USD | `-68.07%` | `20.00` |
| `Live` | `Long` | `31.15` | 121,810,000.00 USD | 0.00 USD | 7,320.00 USD | `-67.97%` | `235.00` |
| `Live` | `Long` | `31.25` | 121,810,000.00 USD | 0.00 USD | 160.62 USD | `-67.86%` | `5.14` |
| `Live` | `Long` | `31.45` | 121,810,000.00 USD | 0.00 USD | 408.54 USD | `-67.66%` | `12.99` |
| `Live` | `Long` | `31.75` | 121,810,000.00 USD | 0.00 USD | 158.75 USD | `-67.35%` | `5.00` |
| `Live` | `Long` | `31.85` | 121,810,000.00 USD | 0.00 USD | 68,610.00 USD | `-67.25%` | `2,154.01` |
| `Live` | `Long` | `31.95` | 121,740,000.00 USD | 0.00 USD | 791.72 USD | `-67.14%` | `24.78` |
| `Live` | `Long` | `32.05` | 121,740,000.00 USD | 0.00 USD | 24,380.00 USD | `-67.04%` | `760.54` |
| `Live` | `Long` | `32.25` | 121,710,000.00 USD | 0.00 USD | 564,040.00 USD | `-66.83%` | `17,489.75` |
| `Live` | `Long` | `32.35` | 121,150,000.00 USD | 0.00 USD | 815.87 USD | `-66.73%` | `25.22` |
| `Live` | `Long` | `32.55` | 121,150,000.00 USD | 0.00 USD | 1,070.00 USD | `-66.53%` | `32.75` |
| `Live` | `Long` | `32.85` | 121,150,000.00 USD | 0.00 USD | 9,710.00 USD | `-66.22%` | `295.71` |
| `Live` | `Long` | `32.95` | 121,140,000.00 USD | 0.00 USD | 920.62 USD | `-66.11%` | `27.94` |
| `Live` | `Long` | `33.05` | 121,140,000.00 USD | 0.00 USD | 177.81 USD | `-66.01%` | `5.38` |
| `Live` | `Long` | `33.45` | 121,130,000.00 USD | 0.00 USD | 753.29 USD | `-65.60%` | `22.52` |
| `Live` | `Long` | `33.55` | 121,130,000.00 USD | 0.00 USD | 493.52 USD | `-65.50%` | `14.71` |
| `Live` | `Long` | `33.95` | 121,130,000.00 USD | 0.00 USD | 226.11 USD | `-65.09%` | `6.66` |
| `Live` | `Long` | `34.25` | 121,130,000.00 USD | 0.00 USD | 397.98 USD | `-64.78%` | `11.62` |
| `Live` | `Long` | `34.35` | 121,130,000.00 USD | 0.00 USD | 2,150.00 USD | `-64.68%` | `62.57` |
| `Live` | `Long` | `34.65` | 121,130,000.00 USD | 0.00 USD | 486.14 USD | `-64.37%` | `14.03` |
| `Live` | `Long` | `34.75` | 121,130,000.00 USD | 0.00 USD | 1,610.00 USD | `-64.26%` | `46.46` |
| `Live` | `Long` | `34.85` | 121,130,000.00 USD | 0.00 USD | 41,820.00 USD | `-64.16%` | `1,200.00` |
| `Live` | `Long` | `34.95` | 121,090,000.00 USD | 0.00 USD | 6,620,000.00 USD | `-64.06%` | `189,472.50` |
| `Live` | `Long` | `35.15` | 114,460,000.00 USD | 0.00 USD | 17,050.00 USD | `-63.85%` | `484.95` |
| `Live` | `Long` | `35.25` | 114,450,000.00 USD | 0.00 USD | 1,010.00 USD | `-63.75%` | `28.60` |
| `Live` | `Long` | `35.35` | 114,450,000.00 USD | 0.00 USD | 48,090.00 USD | `-63.65%` | `1,360.52` |
| `Live` | `Long` | `35.55` | 114,400,000.00 USD | 0.00 USD | 3,030.00 USD | `-63.44%` | `85.14` |
| `Live` | `Long` | `35.65` | 114,400,000.00 USD | 0.00 USD | 1,980.00 USD | `-63.34%` | `55.47` |
| `Live` | `Long` | `35.75` | 114,390,000.00 USD | 0.00 USD | 5,720.00 USD | `-63.24%` | `160.13` |
| `Live` | `Long` | `35.95` | 114,390,000.00 USD | 0.00 USD | 557.94 USD | `-63.03%` | `15.52` |
| `Live` | `Long` | `36.05` | 114,390,000.00 USD | 0.00 USD | 7,160.00 USD | `-62.93%` | `198.58` |
| `Live` | `Long` | `36.15` | 114,380,000.00 USD | 0.00 USD | 50,400.00 USD | `-62.82%` | `1,394.27` |
| `Live` | `Long` | `36.25` | 114,330,000.00 USD | 0.00 USD | 1,400.00 USD | `-62.72%` | `38.75` |
| `Live` | `Long` | `36.35` | 114,330,000.00 USD | 0.00 USD | 5,280.00 USD | `-62.62%` | `145.32` |
| `Live` | `Long` | `36.45` | 114,320,000.00 USD | 0.00 USD | 2,410.00 USD | `-62.52%` | `66.24` |
| `Live` | `Long` | `36.55` | 114,320,000.00 USD | 0.00 USD | 1,060.00 USD | `-62.41%` | `29.10` |
| `Live` | `Long` | `36.65` | 114,320,000.00 USD | 0.00 USD | 38,560.00 USD | `-62.31%` | `1,052.17` |
| `Live` | `Long` | `36.75` | 114,280,000.00 USD | 0.00 USD | 1,400.00 USD | `-62.21%` | `38.16` |
| `Live` | `Long` | `36.95` | 114,280,000.00 USD | 0.00 USD | 1,660.00 USD | `-62.00%` | `45.00` |
| `Live` | `Long` | `37.05` | 114,280,000.00 USD | 0.00 USD | 16,570.00 USD | `-61.90%` | `447.21` |
| `Live` | `Long` | `37.25` | 114,260,000.00 USD | 0.00 USD | 373.62 USD | `-61.69%` | `10.03` |
| `Live` | `Long` | `37.35` | 114,260,000.00 USD | 0.00 USD | 21,230.00 USD | `-61.59%` | `568.54` |
| `Live` | `Long` | `37.55` | 114,240,000.00 USD | 0.00 USD | 4,200.00 USD | `-61.38%` | `111.94` |
| `Live` | `Long` | `37.65` | 114,240,000.00 USD | 0.00 USD | 2,430.00 USD | `-61.28%` | `64.52` |
| `Live` | `Long` | `37.75` | 114,230,000.00 USD | 0.00 USD | 10,380.00 USD | `-61.18%` | `274.93` |
| `Live` | `Long` | `37.85` | 114,220,000.00 USD | 0.00 USD | 105,670.00 USD | `-61.08%` | `2,791.94` |
| `Live` | `Long` | `37.95` | 114,120,000.00 USD | 0.00 USD | 10,170.00 USD | `-60.97%` | `268.07` |
| `Live` | `Long` | `38.05` | 114,110,000.00 USD | 0.00 USD | 2,240.00 USD | `-60.87%` | `58.76` |
| `Live` | `Long` | `38.15` | 114,100,000.00 USD | 0.00 USD | 642.83 USD | `-60.77%` | `16.85` |
| `Live` | `Long` | `38.35` | 114,100,000.00 USD | 0.00 USD | 769.30 USD | `-60.56%` | `20.06` |
| `Live` | `Long` | `38.45` | 114,100,000.00 USD | 0.00 USD | 3,000,000.00 USD | `-60.46%` | `78,000.00` |
| `Live` | `Long` | `38.55` | 111,100,000.00 USD | 0.00 USD | 1,060,000.00 USD | `-60.36%` | `27,545.24` |
| `Live` | `Long` | `38.75` | 110,040,000.00 USD | 0.00 USD | 736.64 USD | `-60.15%` | `19.01` |
| `Live` | `Long` | `38.85` | 110,040,000.00 USD | 0.00 USD | 4,270.00 USD | `-60.05%` | `109.96` |
| `Live` | `Long` | `38.95` | 110,040,000.00 USD | 0.00 USD | 607.62 USD | `-59.94%` | `15.60` |
| `Live` | `Long` | `39.05` | 110,040,000.00 USD | 0.00 USD | 54,500.00 USD | `-59.84%` | `1,395.55` |
| `Live` | `Long` | `39.15` | 109,980,000.00 USD | 0.00 USD | 1,710.00 USD | `-59.74%` | `43.67` |
| `Live` | `Long` | `39.35` | 109,980,000.00 USD | 0.00 USD | 3,640.00 USD | `-59.53%` | `92.49` |
| `Live` | `Long` | `39.45` | 109,980,000.00 USD | 0.00 USD | 1,080.00 USD | `-59.43%` | `27.50` |
| `Live` | `Long` | `39.65` | 109,980,000.00 USD | 0.00 USD | 1,560.00 USD | `-59.22%` | `39.31` |
| `Live` | `Long` | `39.75` | 109,970,000.00 USD | 0.00 USD | 159.00 USD | `-59.12%` | `4.00` |
| `Live` | `Long` | `39.85` | 109,970,000.00 USD | 0.00 USD | 3,260.00 USD | `-59.02%` | `81.86` |
| `Live` | `Long` | `40.05` | 109,970,000.00 USD | 0.00 USD | 52,780.00 USD | `-58.81%` | `1,317.77` |
| `Live` | `Long` | `40.15` | 109,920,000.00 USD | 0.00 USD | 2,510.00 USD | `-58.71%` | `62.48` |
| `Live` | `Long` | `40.25` | 109,920,000.00 USD | 0.00 USD | 12,710.00 USD | `-58.61%` | `315.72` |
| `Live` | `Long` | `40.35` | 109,900,000.00 USD | 0.00 USD | 328,990.00 USD | `-58.50%` | `8,153.29` |
| `Live` | `Long` | `40.55` | 109,570,000.00 USD | 0.00 USD | 3,160.00 USD | `-58.30%` | `77.90` |
| `Live` | `Long` | `40.75` | 109,570,000.00 USD | 0.00 USD | 288.51 USD | `-58.09%` | `7.08` |
| `Live` | `Long` | `40.85` | 109,570,000.00 USD | 0.00 USD | 2,770.00 USD | `-57.99%` | `67.92` |
| `Live` | `Long` | `40.95` | 109,570,000.00 USD | 0.00 USD | 9,790.00 USD | `-57.89%` | `239.18` |
| `Live` | `Long` | `41.05` | 109,560,000.00 USD | 0.00 USD | 4,600.00 USD | `-57.78%` | `112.05` |
| `Live` | `Long` | `41.15` | 109,550,000.00 USD | 0.00 USD | 2,930.00 USD | `-57.68%` | `71.14` |
| `Live` | `Long` | `41.25` | 109,550,000.00 USD | 0.00 USD | 2,840.00 USD | `-57.58%` | `68.93` |
| `Live` | `Long` | `41.35` | 109,550,000.00 USD | 0.00 USD | 2,990.00 USD | `-57.48%` | `72.40` |
| `Live` | `Long` | `41.45` | 109,540,000.00 USD | 0.00 USD | 1,590.00 USD | `-57.37%` | `38.32` |
| `Live` | `Long` | `41.55` | 109,540,000.00 USD | 0.00 USD | 234.76 USD | `-57.27%` | `5.65` |
| `Live` | `Long` | `41.65` | 109,540,000.00 USD | 0.00 USD | 770.11 USD | `-57.17%` | `18.49` |
| `Live` | `Long` | `41.75` | 109,540,000.00 USD | 0.00 USD | 588.26 USD | `-57.06%` | `14.09` |
| `Live` | `Long` | `41.85` | 109,540,000.00 USD | 0.00 USD | 1,020.00 USD | `-56.96%` | `24.39` |
| `Live` | `Long` | `41.95` | 109,540,000.00 USD | 0.00 USD | 48,400.00 USD | `-56.86%` | `1,153.84` |
| `Live` | `Long` | `42.05` | 109,490,000.00 USD | 0.00 USD | 470.12 USD | `-56.76%` | `11.18` |
| `Live` | `Long` | `42.15` | 109,490,000.00 USD | 0.00 USD | 22,560.00 USD | `-56.65%` | `535.13` |
| `Live` | `Long` | `42.25` | 109,470,000.00 USD | 0.00 USD | 1,070,000.00 USD | `-56.55%` | `25,284.04` |
| `Live` | `Long` | `42.35` | 108,400,000.00 USD | 0.00 USD | 6,110.00 USD | `-56.45%` | `144.25` |
| `Live` | `Long` | `42.45` | 108,390,000.00 USD | 0.00 USD | 8,190.00 USD | `-56.35%` | `193.00` |
| `Live` | `Long` | `42.55` | 108,390,000.00 USD | 0.00 USD | 1,750.00 USD | `-56.24%` | `41.04` |
| `Live` | `Long` | `42.85` | 108,380,000.00 USD | 0.00 USD | 44,250.00 USD | `-55.93%` | `1,032.68` |
| `Live` | `Long` | `43.15` | 108,340,000.00 USD | 0.00 USD | 11,750.00 USD | `-55.63%` | `272.22` |
| `Live` | `Long` | `43.25` | 108,330,000.00 USD | 0.00 USD | 1,080.00 USD | `-55.52%` | `25.00` |
| `Live` | `Long` | `43.35` | 108,330,000.00 USD | 0.00 USD | 5,420.00 USD | `-55.42%` | `125.05` |
| `Live` | `Long` | `43.45` | 108,320,000.00 USD | 0.00 USD | 440.15 USD | `-55.32%` | `10.13` |
| `Live` | `Long` | `43.65` | 108,320,000.00 USD | 0.00 USD | 5,530.00 USD | `-55.11%` | `126.59` |
| `Live` | `Long` | `43.85` | 108,320,000.00 USD | 0.00 USD | 69,970.00 USD | `-54.91%` | `1,595.58` |
| `Live` | `Long` | `43.95` | 108,250,000.00 USD | 0.00 USD | 242.16 USD | `-54.80%` | `5.51` |
| `Live` | `Long` | `44.05` | 108,250,000.00 USD | 0.00 USD | 11,220.00 USD | `-54.70%` | `254.69` |
| `Live` | `Long` | `44.25` | 108,230,000.00 USD | 0.00 USD | 6,110.00 USD | `-54.49%` | `138.09` |
| `Live` | `Long` | `44.35` | 108,230,000.00 USD | 0.00 USD | 667,940.00 USD | `-54.39%` | `15,060.63` |
| `Live` | `Long` | `44.45` | 107,560,000.00 USD | 0.00 USD | 10,180.00 USD | `-54.29%` | `229.02` |
| `Live` | `Long` | `44.55` | 107,550,000.00 USD | 0.00 USD | 17,870.00 USD | `-54.19%` | `401.03` |
| `Live` | `Long` | `44.65` | 107,530,000.00 USD | 0.00 USD | 410.78 USD | `-54.08%` | `9.20` |
| `Live` | `Long` | `44.75` | 107,530,000.00 USD | 0.00 USD | 1,790.00 USD | `-53.98%` | `39.98` |
| `Live` | `Long` | `44.85` | 107,530,000.00 USD | 0.00 USD | 3,670,000.00 USD | `-53.88%` | `81,862.42` |
| `Live` | `Long` | `44.95` | 103,860,000.00 USD | 0.00 USD | 42,870.00 USD | `-53.77%` | `953.79` |
| `Live` | `Long` | `45.15` | 103,820,000.00 USD | 0.00 USD | 179.70 USD | `-53.57%` | `3.98` |
| `Live` | `Long` | `45.35` | 103,820,000.00 USD | 0.00 USD | 35,740.00 USD | `-53.36%` | `788.07` |
| `Live` | `Long` | `45.45` | 103,780,000.00 USD | 0.00 USD | 19,500.00 USD | `-53.26%` | `429.15` |
| `Live` | `Long` | `45.55` | 103,760,000.00 USD | 0.00 USD | 8,480.00 USD | `-53.16%` | `186.26` |
| `Live` | `Long` | `45.65` | 103,750,000.00 USD | 0.00 USD | 471.56 USD | `-53.05%` | `10.33` |
| `Live` | `Long` | `45.75` | 103,750,000.00 USD | 0.00 USD | 10,360.00 USD | `-52.95%` | `226.46` |
| `Live` | `Long` | `45.85` | 103,740,000.00 USD | 0.00 USD | 4,010.00 USD | `-52.85%` | `87.46` |
| `Live` | `Long` | `45.95` | 103,740,000.00 USD | 0.00 USD | 26,070.00 USD | `-52.75%` | `567.34` |
| `Live` | `Long` | `46.05` | 103,710,000.00 USD | 0.00 USD | 281.83 USD | `-52.64%` | `6.12` |
| `Live` | `Long` | `46.15` | 103,710,000.00 USD | 0.00 USD | 161.53 USD | `-52.54%` | `3.50` |
| `Live` | `Long` | `46.45` | 103,710,000.00 USD | 0.00 USD | 824.95 USD | `-52.23%` | `17.76` |
| `Live` | `Long` | `46.55` | 103,710,000.00 USD | 0.00 USD | 522.76 USD | `-52.13%` | `11.23` |
| `Live` | `Long` | `46.65` | 103,710,000.00 USD | 0.00 USD | 542.07 USD | `-52.03%` | `11.62` |
| `Live` | `Long` | `46.75` | 103,710,000.00 USD | 0.00 USD | 1,240.00 USD | `-51.92%` | `26.61` |
| `Live` | `Long` | `46.85` | 103,710,000.00 USD | 0.00 USD | 544.40 USD | `-51.82%` | `11.62` |
| `Live` | `Long` | `46.95` | 103,710,000.00 USD | 0.00 USD | 3,870.00 USD | `-51.72%` | `82.49` |
| `Live` | `Long` | `47.15` | 103,700,000.00 USD | 0.00 USD | 10,780.00 USD | `-51.51%` | `228.65` |
| `Live` | `Long` | `47.25` | 103,690,000.00 USD | 0.00 USD | 3,220.00 USD | `-51.41%` | `68.21` |
| `Live` | `Long` | `47.35` | 103,690,000.00 USD | 0.00 USD | 970.20 USD | `-51.31%` | `20.49` |
| `Live` | `Long` | `47.45` | 103,690,000.00 USD | 0.00 USD | 270.47 USD | `-51.20%` | `5.70` |
| `Live` | `Long` | `47.55` | 103,690,000.00 USD | 0.00 USD | 106.04 USD | `-51.10%` | `2.23` |
| `Live` | `Long` | `47.65` | 103,690,000.00 USD | 0.00 USD | 103,030.00 USD | `-51.00%` | `2,162.14` |
| `Live` | `Long` | `47.75` | 103,580,000.00 USD | 0.00 USD | 804,840.00 USD | `-50.89%` | `16,855.35` |
| `Live` | `Long` | `47.85` | 102,780,000.00 USD | 0.00 USD | 8,130.00 USD | `-50.79%` | `169.89` |
| `Live` | `Long` | `47.95` | 102,770,000.00 USD | 0.00 USD | 2,260.00 USD | `-50.69%` | `47.05` |
| `Live` | `Long` | `48.05` | 102,770,000.00 USD | 0.00 USD | 13,300.00 USD | `-50.59%` | `276.89` |
| `Live` | `Long` | `48.15` | 102,760,000.00 USD | 0.00 USD | 6,440.00 USD | `-50.48%` | `133.71` |
| `Live` | `Long` | `48.25` | 102,750,000.00 USD | 0.00 USD | 2,430.00 USD | `-50.38%` | `50.45` |
| `Live` | `Long` | `48.35` | 102,750,000.00 USD | 0.00 USD | 6,050.00 USD | `-50.28%` | `125.05` |
| `Live` | `Long` | `48.45` | 102,740,000.00 USD | 0.00 USD | 2,930.00 USD | `-50.17%` | `60.44` |
| `Live` | `Long` | `48.55` | 102,740,000.00 USD | 0.00 USD | 97,250.00 USD | `-50.07%` | `2,003.13` |
| `Live` | `Long` | `48.65` | 102,640,000.00 USD | 0.00 USD | 9,680.00 USD | `-49.97%` | `198.99` |
| `Live` | `Long` | `48.75` | 102,630,000.00 USD | 0.00 USD | 1,860.00 USD | `-49.87%` | `38.17` |
| `Live` | `Long` | `48.85` | 102,630,000.00 USD | 0.00 USD | 14,260.00 USD | `-49.76%` | `291.88` |
| `Live` | `Long` | `48.95` | 102,620,000.00 USD | 0.00 USD | 1,640.00 USD | `-49.66%` | `33.41` |
| `Live` | `Long` | `49.05` | 102,610,000.00 USD | 0.00 USD | 1,120.00 USD | `-49.56%` | `22.86` |
| `Live` | `Long` | `49.15` | 102,610,000.00 USD | 0.00 USD | 5,010.00 USD | `-49.45%` | `102.01` |
| `Live` | `Long` | `49.25` | 102,610,000.00 USD | 0.00 USD | 21,480.00 USD | `-49.35%` | `436.05` |
| `Live` | `Long` | `49.35` | 102,590,000.00 USD | 0.00 USD | 585.29 USD | `-49.25%` | `11.86` |
| `Live` | `Long` | `49.45` | 102,590,000.00 USD | 0.00 USD | 16,830.00 USD | `-49.15%` | `340.38` |
| `Live` | `Long` | `49.55` | 102,570,000.00 USD | 0.00 USD | 889.42 USD | `-49.04%` | `17.95` |
| `Live` | `Long` | `49.65` | 102,570,000.00 USD | 0.00 USD | 8,890.00 USD | `-48.94%` | `179.12` |
| `Live` | `Long` | `49.75` | 102,560,000.00 USD | 0.00 USD | 201.99 USD | `-48.84%` | `4.06` |
| `Live` | `Long` | `49.85` | 102,560,000.00 USD | 0.00 USD | 1,250,000.00 USD | `-48.74%` | `25,007.72` |
| `Live` | `Long` | `49.95` | 101,310,000.00 USD | 0.00 USD | 170,350.00 USD | `-48.63%` | `3,410.46` |
| `Live` | `Long` | `50.05` | 101,140,000.00 USD | 0.00 USD | 9,870.00 USD | `-48.53%` | `197.25` |
| `Live` | `Long` | `50.15` | 101,130,000.00 USD | 0.00 USD | 11,970.00 USD | `-48.43%` | `238.71` |
| `Live` | `Long` | `50.25` | 101,120,000.00 USD | 0.00 USD | 8,890.00 USD | `-48.32%` | `176.89` |
| `Live` | `Long` | `50.35` | 101,110,000.00 USD | 0.00 USD | 2,410.00 USD | `-48.22%` | `47.91` |
| `Live` | `Long` | `50.45` | 101,110,000.00 USD | 0.00 USD | 3,820.00 USD | `-48.12%` | `75.77` |
| `Live` | `Long` | `50.55` | 101,100,000.00 USD | 0.00 USD | 12,510.00 USD | `-48.02%` | `247.47` |
| `Live` | `Long` | `50.65` | 101,090,000.00 USD | 0.00 USD | 843.83 USD | `-47.91%` | `16.66` |
| `Live` | `Long` | `50.75` | 101,090,000.00 USD | 0.00 USD | 12,040.00 USD | `-47.81%` | `237.21` |
| `Live` | `Long` | `50.85` | 101,080,000.00 USD | 0.00 USD | 19,710.00 USD | `-47.71%` | `387.64` |
| `Live` | `Long` | `50.95` | 101,060,000.00 USD | 0.00 USD | 5,530.00 USD | `-47.60%` | `108.48` |
| `Live` | `Long` | `51.05` | 101,050,000.00 USD | 0.00 USD | 2,680.00 USD | `-47.50%` | `52.57` |
| `Live` | `Long` | `51.15` | 101,050,000.00 USD | 0.00 USD | 2,620.00 USD | `-47.40%` | `51.22` |
| `Live` | `Long` | `51.25` | 101,050,000.00 USD | 0.00 USD | 2,440.00 USD | `-47.30%` | `47.61` |
| `Live` | `Long` | `51.35` | 101,050,000.00 USD | 0.00 USD | 10,640.00 USD | `-47.19%` | `207.26` |
| `Live` | `Long` | `51.45` | 101,040,000.00 USD | 0.00 USD | 8,510.00 USD | `-47.09%` | `165.46` |
| `Live` | `Long` | `51.55` | 101,030,000.00 USD | 0.00 USD | 135,270.00 USD | `-46.99%` | `2,623.99` |
| `Live` | `Long` | `51.65` | 100,890,000.00 USD | 0.00 USD | 7,950.00 USD | `-46.88%` | `153.89` |
| `Live` | `Long` | `51.75` | 100,880,000.00 USD | 0.00 USD | 26,840.00 USD | `-46.78%` | `518.71` |
| `Live` | `Long` | `51.85` | 100,860,000.00 USD | 0.00 USD | 43,180.00 USD | `-46.68%` | `832.75` |
| `Live` | `Long` | `51.95` | 100,810,000.00 USD | 0.00 USD | 473,530.00 USD | `-46.58%` | `9,115.05` |
| `Live` | `Long` | `52.05` | 100,340,000.00 USD | 0.00 USD | 31,030.00 USD | `-46.47%` | `596.12` |
| `Live` | `Long` | `52.15` | 100,310,000.00 USD | 0.00 USD | 101,420.00 USD | `-46.37%` | `1,944.73` |
| `Live` | `Long` | `52.25` | 100,210,000.00 USD | 0.00 USD | 1,760.00 USD | `-46.27%` | `33.59` |
| `Live` | `Long` | `52.35` | 100,210,000.00 USD | 0.00 USD | 28,410.00 USD | `-46.16%` | `542.67` |
| `Live` | `Long` | `52.45` | 100,180,000.00 USD | 0.00 USD | 1,140.00 USD | `-46.06%` | `21.69` |
| `Live` | `Long` | `52.55` | 100,180,000.00 USD | 0.00 USD | 11,110.00 USD | `-45.96%` | `211.45` |
| `Live` | `Long` | `52.65` | 100,170,000.00 USD | 0.00 USD | 2,900.00 USD | `-45.86%` | `55.00` |
| `Live` | `Long` | `52.75` | 100,160,000.00 USD | 0.00 USD | 68,980.00 USD | `-45.75%` | `1,307.77` |
| `Live` | `Long` | `52.85` | 100,090,000.00 USD | 0.00 USD | 27,520.00 USD | `-45.65%` | `520.74` |
| `Live` | `Long` | `52.95` | 100,070,000.00 USD | 0.00 USD | 2,210.00 USD | `-45.55%` | `41.82` |
| `Live` | `Long` | `53.05` | 100,060,000.00 USD | 0.00 USD | 17,340.00 USD | `-45.44%` | `326.84` |
| `Live` | `Long` | `53.15` | 100,050,000.00 USD | 0.00 USD | 2,670.00 USD | `-45.34%` | `50.29` |
| `Live` | `Long` | `53.25` | 100,040,000.00 USD | 0.00 USD | 24,460.00 USD | `-45.24%` | `459.29` |
| `Live` | `Long` | `53.35` | 100,020,000.00 USD | 0.00 USD | 2,240.00 USD | `-45.14%` | `41.93` |
| `Live` | `Long` | `53.45` | 100,020,000.00 USD | 0.00 USD | 47,590.00 USD | `-45.03%` | `890.33` |
| `Live` | `Long` | `53.55` | 99,970,000.00 USD | 0.00 USD | 43,790.00 USD | `-44.93%` | `817.76` |
| `Live` | `Long` | `53.65` | 99,930,000.00 USD | 0.00 USD | 230.70 USD | `-44.83%` | `4.30` |
| `Live` | `Long` | `53.75` | 99,930,000.00 USD | 0.00 USD | 3,600.00 USD | `-44.72%` | `67.00` |
| `Live` | `Long` | `53.85` | 99,920,000.00 USD | 0.00 USD | 18,710.00 USD | `-44.62%` | `347.49` |
| `Live` | `Long` | `53.95` | 99,900,000.00 USD | 0.00 USD | 60,360.00 USD | `-44.52%` | `1,118.77` |
| `Live` | `Long` | `54.05` | 99,840,000.00 USD | 0.00 USD | 1,650.00 USD | `-44.42%` | `30.49` |
| `Live` | `Long` | `54.15` | 99,840,000.00 USD | 0.00 USD | 14,640.00 USD | `-44.31%` | `270.39` |
| `Live` | `Long` | `54.25` | 99,830,000.00 USD | 0.00 USD | 5,360.00 USD | `-44.21%` | `98.83` |
| `Live` | `Long` | `54.35` | 99,820,000.00 USD | 0.00 USD | 12,060.00 USD | `-44.11%` | `221.83` |
| `Live` | `Long` | `54.45` | 99,810,000.00 USD | 0.00 USD | 1,840.00 USD | `-44.00%` | `33.83` |
| `Live` | `Long` | `54.55` | 99,810,000.00 USD | 0.00 USD | 60,580.00 USD | `-43.90%` | `1,110.45` |
| `Live` | `Long` | `54.65` | 99,750,000.00 USD | 0.00 USD | 10,920.00 USD | `-43.80%` | `199.82` |
| `Live` | `Long` | `54.75` | 99,740,000.00 USD | 0.00 USD | 15,140.00 USD | `-43.70%` | `276.50` |
| `Live` | `Long` | `54.85` | 99,720,000.00 USD | 0.00 USD | 858,930.00 USD | `-43.59%` | `15,659.66` |
| `Live` | `Long` | `54.95` | 98,860,000.00 USD | 0.00 USD | 142,480.00 USD | `-43.49%` | `2,592.93` |
| `Live` | `Long` | `55.05` | 98,720,000.00 USD | 0.00 USD | 552.70 USD | `-43.39%` | `10.04` |
| `Live` | `Long` | `55.15` | 98,720,000.00 USD | 0.00 USD | 1,160.00 USD | `-43.28%` | `21.07` |
| `Live` | `Long` | `55.25` | 98,720,000.00 USD | 0.00 USD | 2,010.00 USD | `-43.18%` | `36.31` |
| `Live` | `Long` | `55.35` | 98,720,000.00 USD | 0.00 USD | 43,510.00 USD | `-43.08%` | `786.16` |
| `Live` | `Long` | `55.45` | 98,670,000.00 USD | 0.00 USD | 145,980.00 USD | `-42.98%` | `2,632.66` |
| `Live` | `Long` | `55.55` | 98,530,000.00 USD | 0.00 USD | 5,090.00 USD | `-42.87%` | `91.69` |
| `Live` | `Long` | `55.65` | 98,520,000.00 USD | 0.00 USD | 11,490.00 USD | `-42.77%` | `206.41` |
| `Live` | `Long` | `55.75` | 98,510,000.00 USD | 0.00 USD | 92,400.00 USD | `-42.67%` | `1,657.32` |
| `Live` | `Long` | `55.85` | 98,420,000.00 USD | 0.00 USD | 8,360.00 USD | `-42.56%` | `149.77` |
| `Live` | `Long` | `55.95` | 98,410,000.00 USD | 0.00 USD | 8,640.00 USD | `-42.46%` | `154.35` |
| `Live` | `Long` | `56.05` | 98,400,000.00 USD | 0.00 USD | 5,640.00 USD | `-42.36%` | `100.70` |
| `Live` | `Long` | `56.15` | 98,390,000.00 USD | 0.00 USD | 38,930.00 USD | `-42.26%` | `693.27` |
| `Live` | `Long` | `56.25` | 98,360,000.00 USD | 0.00 USD | 13,300.00 USD | `-42.15%` | `236.52` |
| `Live` | `Long` | `56.35` | 98,340,000.00 USD | 0.00 USD | 38,470.00 USD | `-42.05%` | `682.61` |
| `Live` | `Long` | `56.45` | 98,300,000.00 USD | 0.00 USD | 35,560.00 USD | `-41.95%` | `629.97` |
| `Live` | `Long` | `56.55` | 98,270,000.00 USD | 0.00 USD | 5,930.00 USD | `-41.84%` | `104.86` |
| `Live` | `Long` | `56.65` | 98,260,000.00 USD | 0.00 USD | 18,370.00 USD | `-41.74%` | `324.25` |
| `Live` | `Long` | `56.75` | 98,240,000.00 USD | 0.00 USD | 11,350.00 USD | `-41.64%` | `200.01` |
| `Live` | `Long` | `56.85` | 98,230,000.00 USD | 0.00 USD | 122.80 USD | `-41.54%` | `2.16` |
| `Live` | `Long` | `56.95` | 98,230,000.00 USD | 0.00 USD | 14,320.00 USD | `-41.43%` | `251.38` |
| `Live` | `Long` | `57.05` | 98,220,000.00 USD | 0.00 USD | 2,770,000.00 USD | `-41.33%` | `48,627.98` |
| `Live` | `Long` | `57.15` | 95,440,000.00 USD | 0.00 USD | 5,380.00 USD | `-41.23%` | `94.22` |
| `Live` | `Long` | `57.25` | 95,440,000.00 USD | 0.00 USD | 2,930.00 USD | `-41.13%` | `51.15` |
| `Live` | `Long` | `57.35` | 95,440,000.00 USD | 0.00 USD | 7,120.00 USD | `-41.02%` | `124.09` |
| `Live` | `Long` | `57.45` | 95,430,000.00 USD | 0.00 USD | 19,200.00 USD | `-40.92%` | `334.25` |
| `Live` | `Long` | `57.55` | 95,410,000.00 USD | 0.00 USD | 1,390.00 USD | `-40.82%` | `24.22` |
| `Live` | `Long` | `57.65` | 95,410,000.00 USD | 0.00 USD | 23,520.00 USD | `-40.71%` | `407.99` |
| `Live` | `Long` | `57.75` | 95,380,000.00 USD | 0.00 USD | 36,550.00 USD | `-40.61%` | `632.87` |
| `Live` | `Long` | `57.85` | 95,350,000.00 USD | 0.00 USD | 21,950.00 USD | `-40.51%` | `379.47` |
| `Live` | `Long` | `57.95` | 95,330,000.00 USD | 0.00 USD | 1,680.00 USD | `-40.41%` | `29.05` |
| `Live` | `Long` | `58.05` | 95,320,000.00 USD | 0.00 USD | 4,710.00 USD | `-40.30%` | `81.10` |
| `Live` | `Long` | `58.15` | 95,320,000.00 USD | 0.00 USD | 185,300.00 USD | `-40.20%` | `3,186.57` |
| `Live` | `Long` | `58.25` | 95,130,000.00 USD | 0.00 USD | 16,420.00 USD | `-40.10%` | `281.87` |
| `Live` | `Long` | `58.35` | 95,120,000.00 USD | 0.00 USD | 4,670.00 USD | `-39.99%` | `80.09` |
| `Live` | `Long` | `58.45` | 95,110,000.00 USD | 0.00 USD | 23,520.00 USD | `-39.89%` | `402.33` |
| `Live` | `Long` | `58.55` | 95,090,000.00 USD | 0.00 USD | 2,970.00 USD | `-39.79%` | `50.81` |
| `Live` | `Long` | `58.65` | 95,090,000.00 USD | 0.00 USD | 2,350,000.00 USD | `-39.69%` | `40,007.13` |
| `Live` | `Long` | `58.75` | 92,740,000.00 USD | 0.00 USD | 195.64 USD | `-39.58%` | `3.33` |
| `Live` | `Long` | `58.85` | 92,740,000.00 USD | 0.00 USD | 6,130.00 USD | `-39.48%` | `104.08` |
| `Live` | `Long` | `58.95` | 92,730,000.00 USD | 0.00 USD | 1,090.00 USD | `-39.38%` | `18.45` |
| `Live` | `Long` | `59.05` | 92,730,000.00 USD | 0.00 USD | 37,600.00 USD | `-39.27%` | `636.80` |
| `Live` | `Long` | `59.15` | 92,700,000.00 USD | 0.00 USD | 4,760.00 USD | `-39.17%` | `80.44` |
| `Live` | `Long` | `59.25` | 92,690,000.00 USD | 0.00 USD | 613.24 USD | `-39.07%` | `10.35` |
| `Live` | `Long` | `59.35` | 92,690,000.00 USD | 0.00 USD | 63,190.00 USD | `-38.97%` | `1,064.76` |
| `Live` | `Long` | `59.45` | 92,630,000.00 USD | 0.00 USD | 4,230.00 USD | `-38.86%` | `71.12` |
| `Live` | `Long` | `59.55` | 92,620,000.00 USD | 0.00 USD | 8,770.00 USD | `-38.76%` | `147.21` |
| `Live` | `Long` | `59.65` | 92,610,000.00 USD | 0.00 USD | 4,020.00 USD | `-38.66%` | `67.43` |
| `Live` | `Long` | `59.75` | 92,610,000.00 USD | 0.00 USD | 13,130.00 USD | `-38.55%` | `219.76` |
| `Live` | `Long` | `59.85` | 92,600,000.00 USD | 0.00 USD | 21,560.00 USD | `-38.45%` | `360.29` |
| `Live` | `Long` | `59.95` | 92,580,000.00 USD | 0.00 USD | 37,240.00 USD | `-38.35%` | `621.17` |
| `Live` | `Long` | `60.05` | 92,540,000.00 USD | 0.00 USD | 24,200.00 USD | `-38.25%` | `403.00` |
| `Live` | `Long` | `60.15` | 92,510,000.00 USD | 0.00 USD | 35,140.00 USD | `-38.14%` | `584.16` |
| `Live` | `Long` | `60.25` | 92,480,000.00 USD | 0.00 USD | 20,970.00 USD | `-38.04%` | `348.11` |
| `Live` | `Long` | `60.35` | 92,460,000.00 USD | 0.00 USD | 9,880.00 USD | `-37.94%` | `163.70` |
| `Live` | `Long` | `60.55` | 92,450,000.00 USD | 0.00 USD | 101,570.00 USD | `-37.73%` | `1,677.46` |
| `Live` | `Long` | `60.65` | 92,350,000.00 USD | 0.00 USD | 711.42 USD | `-37.63%` | `11.73` |
| `Live` | `Long` | `60.75` | 92,350,000.00 USD | 0.00 USD | 5,300.00 USD | `-37.53%` | `87.26` |
| `Live` | `Long` | `60.85` | 92,340,000.00 USD | 0.00 USD | 28,860.00 USD | `-37.42%` | `474.33` |
| `Live` | `Long` | `60.95` | 92,310,000.00 USD | 0.00 USD | 59,450.00 USD | `-37.32%` | `975.33` |
| `Live` | `Long` | `61.05` | 92,250,000.00 USD | 0.00 USD | 4,230.00 USD | `-37.22%` | `69.34` |
| `Live` | `Long` | `61.15` | 92,250,000.00 USD | 0.00 USD | 23,090.00 USD | `-37.11%` | `377.55` |
| `Live` | `Long` | `61.25` | 92,220,000.00 USD | 0.00 USD | 4,630.00 USD | `-37.01%` | `75.67` |
| `Live` | `Long` | `61.35` | 92,220,000.00 USD | 0.00 USD | 11,940.00 USD | `-36.91%` | `194.54` |
| `Live` | `Long` | `61.45` | 92,210,000.00 USD | 0.00 USD | 20,920.00 USD | `-36.81%` | `340.48` |
| `Live` | `Long` | `61.55` | 92,190,000.00 USD | 0.00 USD | 25,430.00 USD | `-36.70%` | `413.21` |
| `Live` | `Long` | `61.65` | 92,160,000.00 USD | 0.00 USD | 18,880.00 USD | `-36.60%` | `306.22` |
| `Live` | `Long` | `61.75` | 92,140,000.00 USD | 0.00 USD | 33,410.00 USD | `-36.50%` | `541.00` |
| `Live` | `Long` | `61.85` | 92,110,000.00 USD | 0.00 USD | 7,540.00 USD | `-36.39%` | `121.89` |
| `Live` | `Long` | `61.95` | 92,100,000.00 USD | 0.00 USD | 4,260.00 USD | `-36.29%` | `68.75` |
| `Live` | `Long` | `62.05` | 92,100,000.00 USD | 0.00 USD | 9,000.00 USD | `-36.19%` | `145.05` |
| `Live` | `Long` | `62.15` | 92,090,000.00 USD | 0.00 USD | 40,890.00 USD | `-36.09%` | `657.88` |
| `Live` | `Long` | `62.25` | 92,050,000.00 USD | 0.00 USD | 1,800.00 USD | `-35.98%` | `28.90` |
| `Live` | `Long` | `62.35` | 92,050,000.00 USD | 0.00 USD | 17,900.00 USD | `-35.88%` | `287.05` |
| `Live` | `Long` | `62.45` | 92,030,000.00 USD | 0.00 USD | 27,890.00 USD | `-35.78%` | `446.59` |
| `Live` | `Long` | `62.55` | 92,000,000.00 USD | 0.00 USD | 133,130.00 USD | `-35.67%` | `2,128.40` |
| `Live` | `Long` | `62.65` | 91,870,000.00 USD | 0.00 USD | 2,480.00 USD | `-35.57%` | `39.62` |
| `Live` | `Long` | `62.75` | 91,860,000.00 USD | 0.00 USD | 4,190.00 USD | `-35.47%` | `66.80` |
| `Live` | `Long` | `62.85` | 91,860,000.00 USD | 0.00 USD | 70,890.00 USD | `-35.37%` | `1,127.98` |
| `Live` | `Long` | `62.95` | 91,790,000.00 USD | 0.00 USD | 65,880.00 USD | `-35.26%` | `1,046.52` |
| `Live` | `Long` | `63.05` | 91,720,000.00 USD | 0.00 USD | 22,540.00 USD | `-35.16%` | `357.54` |
| `Live` | `Long` | `63.15` | 91,700,000.00 USD | 0.00 USD | 81,250.00 USD | `-35.06%` | `1,286.67` |
| `Live` | `Long` | `63.25` | 91,620,000.00 USD | 0.00 USD | 16,050.00 USD | `-34.95%` | `253.76` |
| `Live` | `Long` | `63.45` | 91,600,000.00 USD | 0.00 USD | 291.24 USD | `-34.75%` | `4.59` |
| `Live` | `Long` | `63.55` | 91,600,000.00 USD | 0.00 USD | 49,290.00 USD | `-34.65%` | `775.56` |
| `Live` | `Long` | `63.65` | 91,550,000.00 USD | 0.00 USD | 3,600.00 USD | `-34.54%` | `56.54` |
| `Live` | `Long` | `63.75` | 91,550,000.00 USD | 0.00 USD | 32,540.00 USD | `-34.44%` | `510.36` |
| `Live` | `Long` | `63.85` | 91,520,000.00 USD | 0.00 USD | 40,280.00 USD | `-34.34%` | `630.78` |
| `Live` | `Long` | `63.95` | 91,480,000.00 USD | 0.00 USD | 2,280.00 USD | `-34.23%` | `35.70` |
| `Live` | `Long` | `64.25` | 91,480,000.00 USD | 0.00 USD | 4,450.00 USD | `-33.93%` | `69.19` |
| `Live` | `Long` | `64.35` | 91,470,000.00 USD | 0.00 USD | 2,750.00 USD | `-33.82%` | `42.67` |
| `Live` | `Long` | `64.45` | 91,470,000.00 USD | 0.00 USD | 4,320.00 USD | `-33.72%` | `67.00` |
| `Live` | `Long` | `64.55` | 91,460,000.00 USD | 0.00 USD | 30,840.00 USD | `-33.62%` | `477.70` |
| `Live` | `Long` | `64.65` | 91,430,000.00 USD | 0.00 USD | 2,220.00 USD | `-33.52%` | `34.28` |
| `Live` | `Long` | `64.75` | 91,430,000.00 USD | 0.00 USD | 97,290.00 USD | `-33.41%` | `1,502.50` |
| `Live` | `Long` | `64.85` | 91,330,000.00 USD | 0.00 USD | 396.23 USD | `-33.31%` | `6.11` |
| `Live` | `Long` | `64.95` | 91,330,000.00 USD | 0.00 USD | 209.79 USD | `-33.21%` | `3.23` |
| `Live` | `Long` | `65.05` | 91,330,000.00 USD | 0.00 USD | 247,180.00 USD | `-33.10%` | `3,799.85` |
| `Live` | `Long` | `65.15` | 91,090,000.00 USD | 0.00 USD | 11,480.00 USD | `-33.00%` | `176.25` |
| `Live` | `Long` | `65.25` | 91,070,000.00 USD | 0.00 USD | 15,120.00 USD | `-32.90%` | `231.74` |
| `Live` | `Long` | `65.35` | 91,060,000.00 USD | 0.00 USD | 56,990.00 USD | `-32.80%` | `872.07` |
| `Live` | `Long` | `65.45` | 91,000,000.00 USD | 0.00 USD | 3,130.00 USD | `-32.69%` | `47.89` |
| `Live` | `Long` | `65.55` | 91,000,000.00 USD | 0.00 USD | 10,470.00 USD | `-32.59%` | `159.76` |
| `Live` | `Long` | `65.65` | 90,990,000.00 USD | 0.00 USD | 58,270.00 USD | `-32.49%` | `887.62` |
| `Live` | `Long` | `65.75` | 90,930,000.00 USD | 0.00 USD | 5,070.00 USD | `-32.38%` | `77.05` |
| `Live` | `Long` | `65.85` | 90,930,000.00 USD | 0.00 USD | 63,890.00 USD | `-32.28%` | `970.25` |
| `Live` | `Long` | `65.95` | 90,860,000.00 USD | 0.00 USD | 5,780.00 USD | `-32.18%` | `87.71` |
| `Live` | `Long` | `66.05` | 90,860,000.00 USD | 0.00 USD | 25,140.00 USD | `-32.08%` | `380.68` |
| `Live` | `Long` | `66.15` | 90,830,000.00 USD | 0.00 USD | 1,880.00 USD | `-31.97%` | `28.39` |
| `Live` | `Long` | `66.25` | 90,830,000.00 USD | 0.00 USD | 43,960.00 USD | `-31.87%` | `663.55` |
| `Live` | `Long` | `66.35` | 90,780,000.00 USD | 0.00 USD | 1,600.00 USD | `-31.77%` | `24.08` |
| `Live` | `Long` | `66.45` | 90,780,000.00 USD | 0.00 USD | 10,990.00 USD | `-31.66%` | `165.37` |
| `Live` | `Long` | `66.55` | 90,770,000.00 USD | 0.00 USD | 54,650.00 USD | `-31.56%` | `821.26` |
| `Live` | `Long` | `66.65` | 90,720,000.00 USD | 0.00 USD | 17,700.00 USD | `-31.46%` | `265.59` |
| `Live` | `Long` | `66.75` | 90,700,000.00 USD | 0.00 USD | 43,110.00 USD | `-31.36%` | `645.77` |
| `Live` | `Long` | `66.85` | 90,660,000.00 USD | 0.00 USD | 1,910.00 USD | `-31.25%` | `28.53` |
| `Live` | `Long` | `66.95` | 90,650,000.00 USD | 0.00 USD | 937.30 USD | `-31.15%` | `14.00` |
| `Live` | `Long` | `67.05` | 90,650,000.00 USD | 0.00 USD | 33,520.00 USD | `-31.05%` | `499.98` |
| `Live` | `Long` | `67.15` | 90,620,000.00 USD | 0.00 USD | 418,020.00 USD | `-30.94%` | `6,225.24` |
| `Live` | `Long` | `67.25` | 90,200,000.00 USD | 0.00 USD | 1,350,000.00 USD | `-30.84%` | `20,057.75` |
| `Live` | `Long` | `67.35` | 88,850,000.00 USD | 0.00 USD | 1,450.00 USD | `-30.74%` | `21.51` |
| `Live` | `Long` | `67.45` | 88,850,000.00 USD | 0.00 USD | 21,630.00 USD | `-30.64%` | `320.66` |
| `Live` | `Long` | `67.55` | 88,830,000.00 USD | 0.00 USD | 55,000.00 USD | `-30.53%` | `814.14` |
| `Live` | `Long` | `67.65` | 88,780,000.00 USD | 0.00 USD | 128,820.00 USD | `-30.43%` | `1,904.16` |
| `Live` | `Long` | `67.75` | 88,650,000.00 USD | 0.00 USD | 32,130.00 USD | `-30.33%` | `474.25` |
| `Live` | `Long` | `67.85` | 88,610,000.00 USD | 0.00 USD | 7,630.00 USD | `-30.22%` | `112.45` |
| `Live` | `Long` | `67.95` | 88,610,000.00 USD | 0.00 USD | 3,680.00 USD | `-30.12%` | `54.10` |
| `Live` | `Long` | `68.05` | 88,600,000.00 USD | 0.00 USD | 13,800.00 USD | `-30.02%` | `202.72` |
| `Live` | `Long` | `68.15` | 88,590,000.00 USD | 0.00 USD | 37,490,000.00 USD | `-29.92%` | `550,115.14` |
| `Live` | `Long` | `68.25` | 51,100,000.00 USD | 0.00 USD | 13,650.00 USD | `-29.81%` | `199.93` |
| `Live` | `Long` | `68.35` | 51,090,000.00 USD | 0.00 USD | 4,710.00 USD | `-29.71%` | `68.97` |
| `Live` | `Long` | `68.45` | 51,080,000.00 USD | 0.00 USD | 19,210.00 USD | `-29.61%` | `280.66` |
| `Live` | `Long` | `68.55` | 51,060,000.00 USD | 0.00 USD | 3,890.00 USD | `-29.50%` | `56.68` |
| `Live` | `Long` | `68.65` | 51,060,000.00 USD | 0.00 USD | 19,990.00 USD | `-29.40%` | `291.19` |
| `Live` | `Long` | `68.75` | 51,040,000.00 USD | 0.00 USD | 148,840.00 USD | `-29.30%` | `2,164.93` |
| `Live` | `Long` | `68.85` | 50,890,000.00 USD | 0.00 USD | 7,320.00 USD | `-29.20%` | `106.31` |
| `Live` | `Long` | `68.95` | 50,880,000.00 USD | 0.00 USD | 828,230.00 USD | `-29.09%` | `12,012.04` |
| `Live` | `Long` | `69.05` | 50,050,000.00 USD | 0.00 USD | 12,430,000.00 USD | `-28.99%` | `180,063.48` |
| `Live` | `Long` | `69.15` | 37,620,000.00 USD | 0.00 USD | 10,190.00 USD | `-28.89%` | `147.31` |
| `Live` | `Long` | `69.25` | 37,610,000.00 USD | 0.00 USD | 8,660.00 USD | `-28.78%` | `125.10` |
| `Live` | `Long` | `69.35` | 37,600,000.00 USD | 0.00 USD | 119.28 USD | `-28.68%` | `1.72` |
| `Live` | `Long` | `69.45` | 37,600,000.00 USD | 0.00 USD | 42,250.00 USD | `-28.58%` | `608.28` |
| `Live` | `Long` | `69.55` | 37,560,000.00 USD | 0.00 USD | 10,140.00 USD | `-28.48%` | `145.82` |
| `Live` | `Long` | `69.65` | 37,550,000.00 USD | 0.00 USD | 964,080.00 USD | `-28.37%` | `13,841.71` |
| `Live` | `Long` | `69.75` | 36,580,000.00 USD | 0.00 USD | 432,400.00 USD | `-28.27%` | `6,199.29` |
| `Live` | `Long` | `69.85` | 36,150,000.00 USD | 0.00 USD | 32,380.00 USD | `-28.17%` | `463.52` |
| `Live` | `Long` | `69.95` | 36,120,000.00 USD | 0.00 USD | 8,800.00 USD | `-28.06%` | `125.81` |
| `Live` | `Long` | `70.05` | 36,110,000.00 USD | 0.00 USD | 682.99 USD | `-27.96%` | `9.75` |
| `Live` | `Long` | `70.15` | 36,110,000.00 USD | 0.00 USD | 4,120.00 USD | `-27.86%` | `58.77` |
| `Live` | `Long` | `70.25` | 36,110,000.00 USD | 0.00 USD | 73,070.00 USD | `-27.76%` | `1,040.09` |
| `Live` | `Long` | `70.35` | 36,030,000.00 USD | 0.00 USD | 2,140,000.00 USD | `-27.65%` | `30,396.92` |
| `Live` | `Long` | `70.45` | 33,890,000.00 USD | 0.00 USD | 118,170.00 USD | `-27.55%` | `1,677.31` |
| `Live` | `Long` | `70.55` | 33,780,000.00 USD | 0.00 USD | 417.66 USD | `-27.45%` | `5.92` |
| `Live` | `Long` | `70.65` | 33,780,000.00 USD | 0.00 USD | 1,110,000.00 USD | `-27.34%` | `15,691.73` |
| `Live` | `Long` | `70.75` | 32,670,000.00 USD | 0.00 USD | 12,120.00 USD | `-27.24%` | `171.29` |
| `Live` | `Long` | `70.85` | 32,650,000.00 USD | 0.00 USD | 12,050.00 USD | `-27.14%` | `170.08` |
| `Live` | `Long` | `70.95` | 32,640,000.00 USD | 0.00 USD | 5,630.00 USD | `-27.04%` | `79.38` |
| `Live` | `Long` | `71.05` | 32,640,000.00 USD | 0.00 USD | 32,040.00 USD | `-26.93%` | `451.01` |
| `Live` | `Long` | `71.15` | 32,610,000.00 USD | 0.00 USD | 76,320.00 USD | `-26.83%` | `1,072.62` |
| `Live` | `Long` | `71.25` | 32,530,000.00 USD | 0.00 USD | 3,410.00 USD | `-26.73%` | `47.92` |
| `Live` | `Long` | `71.35` | 32,530,000.00 USD | 0.00 USD | 62,910.00 USD | `-26.62%` | `881.74` |
| `Live` | `Long` | `71.45` | 32,460,000.00 USD | 0.00 USD | 24,590.00 USD | `-26.52%` | `344.18` |
| `Live` | `Long` | `71.55` | 32,440,000.00 USD | 0.00 USD | 41,780.00 USD | `-26.42%` | `583.97` |
| `Live` | `Long` | `71.65` | 32,400,000.00 USD | 0.00 USD | 894.91 USD | `-26.32%` | `12.49` |
| `Live` | `Long` | `71.75` | 32,400,000.00 USD | 0.00 USD | 38,870.00 USD | `-26.21%` | `541.78` |
| `Live` | `Long` | `71.85` | 32,360,000.00 USD | 0.00 USD | 2,130.00 USD | `-26.11%` | `29.71` |
| `Live` | `Long` | `71.95` | 32,350,000.00 USD | 0.00 USD | 12,710.00 USD | `-26.01%` | `176.62` |
| `Live` | `Long` | `72.05` | 32,340,000.00 USD | 0.00 USD | 8,090.00 USD | `-25.90%` | `112.26` |
| `Live` | `Long` | `72.15` | 32,330,000.00 USD | 0.00 USD | 134,310.00 USD | `-25.80%` | `1,861.58` |
| `Live` | `Long` | `72.25` | 32,200,000.00 USD | 0.00 USD | 269,050.00 USD | `-25.70%` | `3,723.83` |
| `Live` | `Long` | `72.35` | 31,930,000.00 USD | 0.00 USD | 28,860.00 USD | `-25.60%` | `398.85` |
| `Live` | `Long` | `72.45` | 31,900,000.00 USD | 0.00 USD | 1,840.00 USD | `-25.49%` | `25.36` |
| `Live` | `Long` | `72.55` | 31,900,000.00 USD | 0.00 USD | 16,340.00 USD | `-25.39%` | `225.23` |
| `Live` | `Long` | `72.65` | 31,880,000.00 USD | 0.00 USD | 38,620.00 USD | `-25.29%` | `531.64` |
| `Live` | `Long` | `72.75` | 31,840,000.00 USD | 0.00 USD | 3,550.00 USD | `-25.19%` | `48.83` |
| `Live` | `Long` | `72.85` | 31,840,000.00 USD | 0.00 USD | 188,230.00 USD | `-25.08%` | `2,583.75` |
| `Live` | `Long` | `72.95` | 31,650,000.00 USD | 0.00 USD | 7,040.00 USD | `-24.98%` | `96.54` |
| `Live` | `Long` | `73.05` | 31,650,000.00 USD | 0.00 USD | 8,140.00 USD | `-24.88%` | `111.45` |
| `Live` | `Long` | `73.15` | 31,640,000.00 USD | 0.00 USD | 19,790.00 USD | `-24.77%` | `270.52` |
| `Live` | `Long` | `73.25` | 31,620,000.00 USD | 0.00 USD | 28,370.00 USD | `-24.67%` | `387.27` |
| `Live` | `Long` | `73.35` | 31,590,000.00 USD | 0.00 USD | 3,900.00 USD | `-24.57%` | `53.16` |
| `Live` | `Long` | `73.45` | 31,590,000.00 USD | 0.00 USD | 18,450.00 USD | `-24.47%` | `251.23` |
| `Live` | `Long` | `73.55` | 31,570,000.00 USD | 0.00 USD | 14,850.00 USD | `-24.36%` | `201.89` |
| `Live` | `Long` | `73.65` | 31,550,000.00 USD | 0.00 USD | 37,850.00 USD | `-24.26%` | `513.85` |
| `Live` | `Long` | `73.75` | 31,510,000.00 USD | 0.00 USD | 74,890.00 USD | `-24.16%` | `1,015.39` |
| `Live` | `Long` | `73.85` | 31,440,000.00 USD | 0.00 USD | 36,100.00 USD | `-24.05%` | `488.81` |
| `Live` | `Long` | `73.95` | 31,400,000.00 USD | 0.00 USD | 74,150.00 USD | `-23.95%` | `1,002.74` |
| `Live` | `Long` | `74.05` | 31,330,000.00 USD | 0.00 USD | 23,760.00 USD | `-23.85%` | `320.93` |
| `Live` | `Long` | `74.15` | 31,310,000.00 USD | 0.00 USD | 31,600.00 USD | `-23.75%` | `426.22` |
| `Live` | `Long` | `74.25` | 31,270,000.00 USD | 0.00 USD | 50,170.00 USD | `-23.64%` | `675.67` |
| `Live` | `Long` | `74.35` | 31,220,000.00 USD | 0.00 USD | 24,480.00 USD | `-23.54%` | `329.28` |
| `Live` | `Long` | `74.45` | 31,200,000.00 USD | 0.00 USD | 27,100.00 USD | `-23.44%` | `364.04` |
| `Live` | `Long` | `74.55` | 31,170,000.00 USD | 0.00 USD | 38,530.00 USD | `-23.33%` | `516.83` |
| `Live` | `Long` | `74.65` | 31,130,000.00 USD | 0.00 USD | 99,800.00 USD | `-23.23%` | `1,336.97` |
| `Live` | `Long` | `74.75` | 31,030,000.00 USD | 0.00 USD | 32,790.00 USD | `-23.13%` | `438.71` |
| `Live` | `Long` | `74.85` | 31,000,000.00 USD | 0.00 USD | 31,980.00 USD | `-23.03%` | `427.31` |
| `Live` | `Long` | `74.95` | 30,970,000.00 USD | 0.00 USD | 17,910.00 USD | `-22.92%` | `238.95` |
| `Live` | `Long` | `75.05` | 30,950,000.00 USD | 0.00 USD | 44,640.00 USD | `-22.82%` | `594.76` |
| `Live` | `Long` | `75.15` | 30,910,000.00 USD | 0.00 USD | 3,120,000.00 USD | `-22.72%` | `41,469.10` |
| `Live` | `Long` | `75.25` | 27,790,000.00 USD | 0.00 USD | 10,380.00 USD | `-22.61%` | `137.92` |
| `Live` | `Long` | `75.35` | 27,780,000.00 USD | 0.00 USD | 247,040.00 USD | `-22.51%` | `3,278.58` |
| `Live` | `Long` | `75.45` | 27,530,000.00 USD | 0.00 USD | 42,370.00 USD | `-22.41%` | `561.54` |
| `Live` | `Long` | `75.55` | 27,490,000.00 USD | 0.00 USD | 28,520.00 USD | `-22.31%` | `377.53` |
| `Live` | `Long` | `75.65` | 27,460,000.00 USD | 0.00 USD | 130,250.00 USD | `-22.20%` | `1,721.70` |
| `Live` | `Long` | `75.75` | 27,330,000.00 USD | 0.00 USD | 64,900.00 USD | `-22.10%` | `856.80` |
| `Live` | `Long` | `75.85` | 27,270,000.00 USD | 0.00 USD | 3,990.00 USD | `-22.00%` | `52.63` |
| `Live` | `Long` | `75.95` | 27,260,000.00 USD | 0.00 USD | 25,630.00 USD | `-21.89%` | `337.43` |
| `Live` | `Long` | `76.05` | 27,240,000.00 USD | 0.00 USD | 12,340.00 USD | `-21.79%` | `162.23` |
| `Live` | `Long` | `76.15` | 27,220,000.00 USD | 0.00 USD | 4,370.00 USD | `-21.69%` | `57.43` |
| `Live` | `Long` | `76.25` | 27,220,000.00 USD | 0.00 USD | 2,070.00 USD | `-21.59%` | `27.09` |
| `Live` | `Long` | `76.35` | 27,220,000.00 USD | 0.00 USD | 62,610.00 USD | `-21.48%` | `820.04` |
| `Live` | `Long` | `76.45` | 27,160,000.00 USD | 0.00 USD | 32,740.00 USD | `-21.38%` | `428.30` |
| `Live` | `Long` | `76.55` | 27,120,000.00 USD | 0.00 USD | 130,100.00 USD | `-21.28%` | `1,699.53` |
| `Live` | `Long` | `76.65` | 26,990,000.00 USD | 0.00 USD | 179,000.00 USD | `-21.17%` | `2,335.30` |
| `Live` | `Long` | `76.75` | 26,810,000.00 USD | 0.00 USD | 11,340.00 USD | `-21.07%` | `147.80` |
| `Live` | `Long` | `76.85` | 26,800,000.00 USD | 0.00 USD | 252,770.00 USD | `-20.97%` | `3,289.09` |
| `Live` | `Long` | `76.95` | 26,550,000.00 USD | 0.00 USD | 28,980.00 USD | `-20.87%` | `376.65` |
| `Live` | `Long` | `77.05` | 26,520,000.00 USD | 0.00 USD | 87,490.00 USD | `-20.76%` | `1,135.45` |
| `Live` | `Long` | `77.15` | 26,430,000.00 USD | 0.00 USD | 85,130.00 USD | `-20.66%` | `1,103.49` |
| `Live` | `Long` | `77.25` | 26,350,000.00 USD | 0.00 USD | 25,340.00 USD | `-20.56%` | `328.02` |
| `Live` | `Long` | `77.35` | 26,320,000.00 USD | 0.00 USD | 10,160.00 USD | `-20.45%` | `131.34` |
| `Live` | `Long` | `77.45` | 26,310,000.00 USD | 0.00 USD | 46,840.00 USD | `-20.35%` | `604.72` |
| `Live` | `Long` | `77.55` | 26,270,000.00 USD | 0.00 USD | 16,110.00 USD | `-20.25%` | `207.79` |
| `Live` | `Long` | `77.75` | 26,250,000.00 USD | 0.00 USD | 14,690.00 USD | `-20.04%` | `188.89` |
| `Live` | `Long` | `77.85` | 26,230,000.00 USD | 0.00 USD | 68,550.00 USD | `-19.94%` | `880.58` |
| `Live` | `Long` | `77.95` | 26,170,000.00 USD | 0.00 USD | 185,210.00 USD | `-19.84%` | `2,376.06` |
| `Live` | `Long` | `78.05` | 25,980,000.00 USD | 0.00 USD | 21,860.00 USD | `-19.73%` | `280.05` |
| `Live` | `Long` | `78.15` | 25,960,000.00 USD | 0.00 USD | 63,710.00 USD | `-19.63%` | `815.26` |
| `Live` | `Long` | `78.25` | 25,900,000.00 USD | 0.00 USD | 47,380.00 USD | `-19.53%` | `605.48` |
| `Live` | `Long` | `78.35` | 25,850,000.00 USD | 0.00 USD | 50,680.00 USD | `-19.43%` | `646.85` |
| `Live` | `Long` | `78.45` | 25,800,000.00 USD | 0.00 USD | 26,080.00 USD | `-19.32%` | `332.40` |
| `Live` | `Long` | `78.55` | 25,770,000.00 USD | 0.00 USD | 5,740.00 USD | `-19.22%` | `73.09` |
| `Live` | `Long` | `78.65` | 25,770,000.00 USD | 0.00 USD | 32,590.00 USD | `-19.12%` | `414.43` |
| `Live` | `Long` | `78.75` | 25,730,000.00 USD | 0.00 USD | 61,050.00 USD | `-19.01%` | `775.20` |
| `Live` | `Long` | `78.85` | 25,670,000.00 USD | 0.00 USD | 66,850.00 USD | `-18.91%` | `847.77` |
| `Live` | `Long` | `78.95` | 25,610,000.00 USD | 0.00 USD | 1,740.00 USD | `-18.81%` | `22.05` |
| `Live` | `Long` | `79.05` | 25,600,000.00 USD | 0.00 USD | 16,530.00 USD | `-18.71%` | `209.06` |
| `Live` | `Long` | `79.15` | 25,590,000.00 USD | 0.00 USD | 610,370.00 USD | `-18.60%` | `7,711.54` |
| `Live` | `Long` | `79.25` | 24,980,000.00 USD | 0.00 USD | 41,700.00 USD | `-18.50%` | `526.15` |
| `Live` | `Long` | `79.35` | 24,930,000.00 USD | 0.00 USD | 28,820.00 USD | `-18.40%` | `363.18` |
| `Live` | `Long` | `79.45` | 24,910,000.00 USD | 0.00 USD | 11,580.00 USD | `-18.29%` | `145.81` |
| `Live` | `Long` | `79.55` | 24,890,000.00 USD | 0.00 USD | 3,180.00 USD | `-18.19%` | `40.00` |
| `Live` | `Long` | `79.65` | 24,890,000.00 USD | 0.00 USD | 15,720.00 USD | `-18.09%` | `197.39` |
| `Live` | `Long` | `79.75` | 24,880,000.00 USD | 0.00 USD | 126,320.00 USD | `-17.99%` | `1,583.90` |
| `Live` | `Long` | `79.85` | 24,750,000.00 USD | 0.00 USD | 42,840.00 USD | `-17.88%` | `536.47` |
| `Live` | `Long` | `79.95` | 24,710,000.00 USD | 0.00 USD | 48,790.00 USD | `-17.78%` | `610.24` |
| `Live` | `Long` | `80.05` | 24,660,000.00 USD | 0.00 USD | 40,950.00 USD | `-17.68%` | `511.50` |
| `Live` | `Long` | `80.15` | 24,620,000.00 USD | 0.00 USD | 37,150.00 USD | `-17.58%` | `463.46` |
| `Live` | `Long` | `80.25` | 24,580,000.00 USD | 0.00 USD | 57,490.00 USD | `-17.47%` | `716.34` |
| `Live` | `Long` | `80.35` | 24,520,000.00 USD | 0.00 USD | 115,070.00 USD | `-17.37%` | `1,432.12` |
| `Live` | `Long` | `80.45` | 24,410,000.00 USD | 0.00 USD | 11,320.00 USD | `-17.27%` | `140.77` |
| `Live` | `Long` | `80.55` | 24,400,000.00 USD | 0.00 USD | 5,880.00 USD | `-17.16%` | `72.98` |
| `Live` | `Long` | `80.65` | 24,390,000.00 USD | 0.00 USD | 25,050.00 USD | `-17.06%` | `310.54` |
| `Live` | `Long` | `80.75` | 24,360,000.00 USD | 0.00 USD | 24,950.00 USD | `-16.96%` | `308.96` |
| `Live` | `Long` | `80.85` | 24,340,000.00 USD | 0.00 USD | 439,440.00 USD | `-16.86%` | `5,435.26` |
| `Live` | `Long` | `80.95` | 23,900,000.00 USD | 0.00 USD | 10,620.00 USD | `-16.75%` | `131.18` |
| `Live` | `Long` | `81.05` | 23,890,000.00 USD | 0.00 USD | 2,230,000.00 USD | `-16.65%` | `27,462.57` |
| `Live` | `Long` | `81.15` | 21,660,000.00 USD | 0.00 USD | 128,110.00 USD | `-16.55%` | `1,578.71` |
| `Live` | `Long` | `81.25` | 21,540,000.00 USD | 0.00 USD | 27,510.00 USD | `-16.44%` | `338.58` |
| `Live` | `Long` | `81.35` | 21,510,000.00 USD | 0.00 USD | 56,470.00 USD | `-16.34%` | `694.17` |
| `Live` | `Long` | `81.45` | 21,450,000.00 USD | 0.00 USD | 57,090.00 USD | `-16.24%` | `700.89` |
| `Live` | `Long` | `81.55` | 21,390,000.00 USD | 0.00 USD | 67,100.00 USD | `-16.14%` | `822.81` |
| `Live` | `Long` | `81.65` | 21,330,000.00 USD | 0.00 USD | 15,400.00 USD | `-16.03%` | `188.66` |
| `Live` | `Long` | `81.75` | 21,310,000.00 USD | 0.00 USD | 18,650.00 USD | `-15.93%` | `228.11` |
| `Live` | `Long` | `81.85` | 21,290,000.00 USD | 0.00 USD | 66,670.00 USD | `-15.83%` | `814.52` |
| `Live` | `Long` | `81.95` | 21,230,000.00 USD | 0.00 USD | 100,270.00 USD | `-15.72%` | `1,223.49` |
| `Live` | `Long` | `82.05` | 21,130,000.00 USD | 0.00 USD | 117,060.00 USD | `-15.62%` | `1,426.69` |
| `Live` | `Long` | `82.15` | 21,010,000.00 USD | 0.00 USD | 808,500.00 USD | `-15.52%` | `9,841.72` |
| `Live` | `Long` | `82.25` | 20,200,000.00 USD | 0.00 USD | 386,630.00 USD | `-15.42%` | `4,700.61` |
| `Live` | `Long` | `82.35` | 19,810,000.00 USD | 0.00 USD | 162,500.00 USD | `-15.31%` | `1,973.27` |
| `Live` | `Long` | `82.45` | 19,650,000.00 USD | 0.00 USD | 205,600.00 USD | `-15.21%` | `2,493.68` |
| `Live` | `Long` | `82.55` | 19,450,000.00 USD | 0.00 USD | 31,430.00 USD | `-15.11%` | `380.77` |
| `Live` | `Long` | `82.65` | 19,410,000.00 USD | 0.00 USD | 99,560.00 USD | `-15.00%` | `1,204.63` |
| `Live` | `Long` | `82.75` | 19,320,000.00 USD | 0.00 USD | 754,130.00 USD | `-14.90%` | `9,113.41` |
| `Live` | `Long` | `82.85` | 18,560,000.00 USD | 0.00 USD | 20,580.00 USD | `-14.80%` | `248.41` |
| `Live` | `Long` | `82.95` | 18,540,000.00 USD | 0.00 USD | 17,100.00 USD | `-14.70%` | `206.14` |
| `Live` | `Long` | `83.05` | 18,520,000.00 USD | 0.00 USD | 118,100.00 USD | `-14.59%` | `1,422.09` |
| `Live` | `Long` | `83.15` | 18,410,000.00 USD | 0.00 USD | 11,130.00 USD | `-14.49%` | `133.82` |
| `Live` | `Long` | `83.25` | 18,390,000.00 USD | 0.00 USD | 194,580.00 USD | `-14.39%` | `2,337.30` |
| `Live` | `Long` | `83.35` | 18,200,000.00 USD | 0.00 USD | 287,260.00 USD | `-14.28%` | `3,446.46` |
| `Live` | `Long` | `83.45` | 17,910,000.00 USD | 0.00 USD | 29,160.00 USD | `-14.18%` | `349.42` |
| `Live` | `Long` | `83.55` | 17,880,000.00 USD | 0.00 USD | 10,990.00 USD | `-14.08%` | `131.53` |
| `Live` | `Long` | `83.65` | 17,870,000.00 USD | 0.00 USD | 68,280.00 USD | `-13.98%` | `816.25` |
| `Live` | `Long` | `83.75` | 17,800,000.00 USD | 0.00 USD | 90,040.00 USD | `-13.87%` | `1,075.16` |
| `Live` | `Long` | `83.85` | 17,710,000.00 USD | 0.00 USD | 12,240.00 USD | `-13.77%` | `145.97` |
| `Live` | `Long` | `83.95` | 17,700,000.00 USD | 0.00 USD | 30,940.00 USD | `-13.67%` | `368.54` |
| `Live` | `Long` | `84.05` | 17,670,000.00 USD | 0.00 USD | 299,000.00 USD | `-13.56%` | `3,557.44` |
| `Live` | `Long` | `84.15` | 17,370,000.00 USD | 0.00 USD | 65,900.00 USD | `-13.46%` | `783.09` |
| `Live` | `Long` | `84.25` | 17,310,000.00 USD | 0.00 USD | 46,040.00 USD | `-13.36%` | `546.41` |
| `Live` | `Long` | `84.35` | 17,260,000.00 USD | 0.00 USD | 25,180.00 USD | `-13.26%` | `298.47` |
| `Live` | `Long` | `84.45` | 17,230,000.00 USD | 0.00 USD | 86,620.00 USD | `-13.15%` | `1,025.66` |
| `Live` | `Long` | `84.55` | 17,150,000.00 USD | 0.00 USD | 2,300.00 USD | `-13.05%` | `27.26` |
| `Live` | `Long` | `84.65` | 17,150,000.00 USD | 0.00 USD | 102,150.00 USD | `-12.95%` | `1,206.79` |
| `Live` | `Long` | `84.75` | 17,040,000.00 USD | 0.00 USD | 289,410.00 USD | `-12.84%` | `3,414.86` |
| `Live` | `Long` | `84.85` | 16,750,000.00 USD | 0.00 USD | 94,810.00 USD | `-12.74%` | `1,117.34` |
| `Live` | `Long` | `84.95` | 16,660,000.00 USD | 0.00 USD | 1,360.00 USD | `-12.64%` | `15.98` |
| `Live` | `Long` | `85.05` | 16,660,000.00 USD | 0.00 USD | 27,810.00 USD | `-12.54%` | `326.96` |
| `Live` | `Long` | `85.15` | 16,630,000.00 USD | 0.00 USD | 7,810.00 USD | `-12.43%` | `91.74` |
| `Live` | `Long` | `85.25` | 16,620,000.00 USD | 0.00 USD | 626,910.00 USD | `-12.33%` | `7,353.84` |
| `Live` | `Long` | `85.35` | 16,000,000.00 USD | 0.00 USD | 21,600.00 USD | `-12.23%` | `253.12` |
| `Live` | `Long` | `85.45` | 15,970,000.00 USD | 0.00 USD | 1,290,000.00 USD | `-12.12%` | `15,133.10` |
| `Live` | `Long` | `85.55` | 14,680,000.00 USD | 0.00 USD | 9,600.00 USD | `-12.02%` | `112.21` |
| `Live` | `Long` | `85.65` | 14,670,000.00 USD | 0.00 USD | 42,860.00 USD | `-11.92%` | `500.36` |
| `Live` | `Long` | `85.75` | 14,630,000.00 USD | 0.00 USD | 10,890.00 USD | `-11.82%` | `127.03` |
| `Live` | `Long` | `85.85` | 14,620,000.00 USD | 0.00 USD | 87,080.00 USD | `-11.71%` | `1,014.38` |
| `Live` | `Long` | `85.95` | 14,530,000.00 USD | 0.00 USD | 361,960.00 USD | `-11.61%` | `4,211.33` |
| `Live` | `Long` | `86.05` | 14,170,000.00 USD | 0.00 USD | 256,680.00 USD | `-11.51%` | `2,982.96` |
| `Live` | `Long` | `86.15` | 13,910,000.00 USD | 0.00 USD | 55,020.00 USD | `-11.40%` | `638.69` |
| `Live` | `Long` | `86.25` | 13,860,000.00 USD | 0.00 USD | 36,410.00 USD | `-11.30%` | `422.09` |
| `Live` | `Long` | `86.35` | 13,820,000.00 USD | 0.00 USD | 3,990.00 USD | `-11.20%` | `46.24` |
| `Live` | `Long` | `86.45` | 13,820,000.00 USD | 0.00 USD | 108,330.00 USD | `-11.10%` | `1,253.13` |
| `Live` | `Long` | `86.55` | 13,710,000.00 USD | 0.00 USD | 60,400.00 USD | `-10.99%` | `697.88` |
| `Live` | `Long` | `86.65` | 13,650,000.00 USD | 0.00 USD | 201,760.00 USD | `-10.89%` | `2,328.45` |
| `Live` | `Long` | `86.75` | 13,450,000.00 USD | 0.00 USD | 37,320.00 USD | `-10.79%` | `430.23` |
| `Live` | `Long` | `86.85` | 13,410,000.00 USD | 0.00 USD | 78,680.00 USD | `-10.68%` | `905.91` |
| `Live` | `Long` | `86.95` | 13,330,000.00 USD | 0.00 USD | 167,620.00 USD | `-10.58%` | `1,927.73` |
| `Live` | `Long` | `87.05` | 13,160,000.00 USD | 0.00 USD | 57,090.00 USD | `-10.48%` | `655.80` |
| `Live` | `Long` | `87.15` | 13,100,000.00 USD | 0.00 USD | 45,680.00 USD | `-10.38%` | `524.20` |
| `Live` | `Long` | `87.25` | 13,060,000.00 USD | 0.00 USD | 26,840.00 USD | `-10.27%` | `307.67` |
| `Live` | `Long` | `87.35` | 13,030,000.00 USD | 0.00 USD | 77,770.00 USD | `-10.17%` | `890.30` |
| `Live` | `Long` | `87.45` | 12,950,000.00 USD | 0.00 USD | 210,950.00 USD | `-10.07%` | `2,412.27` |
| `Live` | `Long` | `87.55` | 12,740,000.00 USD | 0.00 USD | 194,880.00 USD | `-9.97%` | `2,225.95` |
| `Live` | `Long` | `87.65` | 12,550,000.00 USD | 0.00 USD | 123,610.00 USD | `-9.86%` | `1,410.24` |
| `Live` | `Long` | `87.75` | 12,430,000.00 USD | 0.00 USD | 27,360.00 USD | `-9.76%` | `311.76` |
| `Live` | `Long` | `87.85` | 12,400,000.00 USD | 0.00 USD | 60,260.00 USD | `-9.66%` | `685.99` |
| `Live` | `Long` | `87.95` | 12,340,000.00 USD | 0.00 USD | 8,810.00 USD | `-9.55%` | `100.20` |
| `Live` | `Long` | `88.05` | 12,330,000.00 USD | 0.00 USD | 161,140.00 USD | `-9.45%` | `1,830.09` |
| `Live` | `Long` | `88.15` | 12,170,000.00 USD | 0.00 USD | 23,910.00 USD | `-9.35%` | `271.24` |
| `Live` | `Long` | `88.25` | 12,140,000.00 USD | 0.00 USD | 49,740.00 USD | `-9.25%` | `563.61` |
| `Live` | `Long` | `88.35` | 12,090,000.00 USD | 0.00 USD | 95,640.00 USD | `-9.14%` | `1,082.49` |
| `Live` | `Long` | `88.45` | 12,000,000.00 USD | 0.00 USD | 69,660.00 USD | `-9.04%` | `787.51` |
| `Live` | `Long` | `88.55` | 11,930,000.00 USD | 0.00 USD | 242,620.00 USD | `-8.94%` | `2,739.96` |
| `Live` | `Long` | `88.65` | 11,690,000.00 USD | 0.00 USD | 97,760.00 USD | `-8.83%` | `1,102.79` |
| `Live` | `Long` | `88.75` | 11,590,000.00 USD | 0.00 USD | 155,750.00 USD | `-8.73%` | `1,754.91` |
| `Live` | `Long` | `88.85` | 11,430,000.00 USD | 0.00 USD | 1,100,000.00 USD | `-8.63%` | `12,343.65` |
| `Live` | `Long` | `88.95` | 10,340,000.00 USD | 0.00 USD | 33,030.00 USD | `-8.53%` | `371.32` |
| `Live` | `Long` | `89.05` | 10,300,000.00 USD | 0.00 USD | 49,580.00 USD | `-8.42%` | `556.76` |
| `Live` | `Long` | `89.15` | 10,250,000.00 USD | 0.00 USD | 124,300.00 USD | `-8.32%` | `1,394.32` |
| `Live` | `Long` | `89.25` | 10,130,000.00 USD | 0.00 USD | 33,540.00 USD | `-8.22%` | `375.85` |
| `Live` | `Long` | `89.35` | 10,100,000.00 USD | 0.00 USD | 80,890.00 USD | `-8.11%` | `905.30` |
| `Live` | `Long` | `89.45` | 10,010,000.00 USD | 0.00 USD | 451,080.00 USD | `-8.01%` | `5,042.86` |
| `Live` | `Long` | `89.55` | 9,560,000.00 USD | 0.00 USD | 121,590.00 USD | `-7.91%` | `1,357.82` |
| `Live` | `Long` | `89.65` | 9,440,000.00 USD | 0.00 USD | 29,100.00 USD | `-7.81%` | `324.64` |
| `Live` | `Long` | `89.75` | 9,410,000.00 USD | 0.00 USD | 148,760.00 USD | `-7.70%` | `1,657.44` |
| `Live` | `Long` | `89.85` | 9,260,000.00 USD | 0.00 USD | 50,000.00 USD | `-7.60%` | `556.50` |
| `Live` | `Long` | `89.95` | 9,210,000.00 USD | 0.00 USD | 70,760.00 USD | `-7.50%` | `786.67` |
| `Live` | `Long` | `90.05` | 9,140,000.00 USD | 0.00 USD | 31,350.00 USD | `-7.39%` | `348.16` |
| `Live` | `Long` | `90.15` | 9,110,000.00 USD | 0.00 USD | 72,970.00 USD | `-7.29%` | `809.48` |
| `Live` | `Long` | `90.25` | 9,040,000.00 USD | 0.00 USD | 27,570.00 USD | `-7.19%` | `305.45` |
| `Live` | `Long` | `90.35` | 9,010,000.00 USD | 0.00 USD | 77,200.00 USD | `-7.09%` | `854.48` |
| `Live` | `Long` | `90.45` | 8,930,000.00 USD | 0.00 USD | 29,160.00 USD | `-6.98%` | `322.43` |
| `Live` | `Long` | `90.55` | 8,900,000.00 USD | 0.00 USD | 25,420.00 USD | `-6.88%` | `280.75` |
| `Live` | `Long` | `90.65` | 8,880,000.00 USD | 0.00 USD | 132,120.00 USD | `-6.78%` | `1,457.43` |
| `Live` | `Long` | `90.75` | 8,750,000.00 USD | 0.00 USD | 88,240.00 USD | `-6.67%` | `972.32` |
| `Live` | `Long` | `90.85` | 8,660,000.00 USD | 0.00 USD | 950,960.00 USD | `-6.57%` | `10,467.39` |
| `Live` | `Long` | `90.95` | 7,710,000.00 USD | 0.00 USD | 19,210.00 USD | `-6.47%` | `211.24` |
| `Live` | `Long` | `91.05` | 7,690,000.00 USD | 0.00 USD | 435,870.00 USD | `-6.37%` | `4,787.17` |
| `Live` | `Long` | `91.15` | 7,250,000.00 USD | 0.00 USD | 295,530.00 USD | `-6.26%` | `3,242.21` |
| `Live` | `Long` | `91.25` | 6,960,000.00 USD | 0.00 USD | 31,690.00 USD | `-6.16%` | `347.30` |
| `Live` | `Long` | `91.35` | 6,930,000.00 USD | 0.00 USD | 50,530.00 USD | `-6.06%` | `553.12` |
| `Live` | `Long` | `91.45` | 6,880,000.00 USD | 0.00 USD | 541,180.00 USD | `-5.95%` | `5,917.75` |
| `Live` | `Long` | `91.55` | 6,330,000.00 USD | 0.00 USD | 1,230,000.00 USD | `-5.85%` | `13,429.28` |
| `Live` | `Long` | `91.65` | 5,100,000.00 USD | 0.00 USD | 1,460,000.00 USD | `-5.75%` | `15,978.36` |
| `Live` | `Long` | `91.75` | 3,640,000.00 USD | 0.00 USD | 230,810.00 USD | `-5.65%` | `2,515.60` |
| `Live` | `Long` | `91.85` | 3,410,000.00 USD | 0.00 USD | 248,720.00 USD | `-5.54%` | `2,707.90` |
| `Live` | `Long` | `91.95` | 3,160,000.00 USD | 0.00 USD | 86,310.00 USD | `-5.44%` | `938.67` |
| `Live` | `Long` | `92.05` | 3,070,000.00 USD | 0.00 USD | 206,110.00 USD | `-5.34%` | `2,239.15` |
| `Live` | `Long` | `92.15` | 2,870,000.00 USD | 0.00 USD | 158,880.00 USD | `-5.23%` | `1,724.14` |
| `Live` | `Long` | `92.25` | 2,710,000.00 USD | 0.00 USD | 241,900.00 USD | `-5.13%` | `2,622.20` |
| `Live` | `Long` | `92.35` | 2,470,000.00 USD | 0.00 USD | 313,050.00 USD | `-5.03%` | `3,389.81` |
| `Live` | `Long` | `92.45` | 2,150,000.00 USD | 0.00 USD | 131,560.00 USD | `-4.93%` | `1,423.03` |
| `Live` | `Long` | `92.55` | 2,020,000.00 USD | 0.00 USD | 3,490.00 USD | `-4.82%` | `37.76` |
| `Live` | `Long` | `92.65` | 2,020,000.00 USD | 0.00 USD | 38,450.00 USD | `-4.72%` | `415.04` |
| `Live` | `Long` | `92.75` | 1,980,000.00 USD | 0.00 USD | 316,620.00 USD | `-4.62%` | `3,413.68` |
| `Live` | `Long` | `92.85` | 1,660,000.00 USD | 0.00 USD | 11,850.00 USD | `-4.51%` | `127.59` |
| `Live` | `Long` | `92.95` | 1,650,000.00 USD | 0.00 USD | 5,720.00 USD | `-4.41%` | `61.49` |
| `Live` | `Long` | `93.05` | 1,650,000.00 USD | 0.00 USD | 25,790.00 USD | `-4.31%` | `277.19` |
| `Live` | `Long` | `93.15` | 1,620,000.00 USD | 0.00 USD | 175.12 USD | `-4.21%` | `1.88` |
| `Live` | `Long` | `93.25` | 1,620,000.00 USD | 0.00 USD | 38,840.00 USD | `-4.10%` | `416.49` |
| `Live` | `Long` | `93.35` | 1,580,000.00 USD | 0.00 USD | 12,570.00 USD | `-4.00%` | `134.70` |
| `Live` | `Long` | `93.45` | 1,570,000.00 USD | 0.00 USD | 739.19 USD | `-3.90%` | `7.91` |
| `Live` | `Long` | `93.55` | 1,570,000.00 USD | 0.00 USD | 20,610.00 USD | `-3.79%` | `220.36` |
| `Live` | `Long` | `93.65` | 1,550,000.00 USD | 0.00 USD | 697.69 USD | `-3.69%` | `7.45` |
| `Live` | `Long` | `93.75` | 1,550,000.00 USD | 0.00 USD | 9,050.00 USD | `-3.59%` | `96.49` |
| `Live` | `Long` | `93.95` | 1,540,000.00 USD | 0.00 USD | 1,130,000.00 USD | `-3.38%` | `12,070.62` |
| `Live` | `Long` | `94.15` | 404,270.00 USD | 0.00 USD | 3,990.00 USD | `-3.18%` | `42.43` |
| `Live` | `Long` | `94.25` | 400,280.00 USD | 0.00 USD | 15,100.00 USD | `-3.07%` | `160.23` |
| `Live` | `Long` | `94.35` | 385,170.00 USD | 0.00 USD | 2,100.00 USD | `-2.97%` | `22.27` |
| `Live` | `Long` | `94.45` | 383,070.00 USD | 0.00 USD | 202,480.00 USD | `-2.87%` | `2,143.78` |
| `Live` | `Long` | `94.55` | 180,590.00 USD | 0.00 USD | 3,080.00 USD | `-2.77%` | `32.60` |
| `Live` | `Long` | `94.65` | 177,510.00 USD | 0.00 USD | 19,410.00 USD | `-2.66%` | `205.10` |
| `Live` | `Long` | `94.75` | 158,100.00 USD | 0.00 USD | 53,170.00 USD | `-2.56%` | `561.21` |
| `Live` | `Long` | `94.85` | 104,920.00 USD | 0.00 USD | 15,620.00 USD | `-2.46%` | `164.65` |
| `Live` | `Long` | `94.95` | 89,310.00 USD | 0.00 USD | 61,600.00 USD | `-2.35%` | `648.77` |
| `Live` | `Long` | `95.05` | 27,710.00 USD | 0.00 USD | 7,780.00 USD | `-2.25%` | `81.85` |
| `Live` | `Long` | `95.15` | 19,930.00 USD | 0.00 USD | 19,930.00 USD | `-2.15%` | `209.42` |
| `Live` | `Short` | `97.95` | 746.38 USD | 746.38 USD | 0.00 USD | `+0.73%` | `7.62` |
| `Live` | `Short` | `98.05` | 1,230.00 USD | 487.31 USD | 0.00 USD | `+0.83%` | `4.97` |
| `Live` | `Short` | `98.15` | 5,750.00 USD | 4,510.00 USD | 0.00 USD | `+0.94%` | `46.00` |
| `Live` | `Short` | `98.25` | 6,820.00 USD | 1,080.00 USD | 0.00 USD | `+1.04%` | `10.95` |
| `Live` | `Short` | `98.35` | 6,980.00 USD | 151.46 USD | 0.00 USD | `+1.14%` | `1.54` |
| `Live` | `Short` | `98.55` | 12,910.00 USD | 5,930.00 USD | 0.00 USD | `+1.35%` | `60.17` |
| `Live` | `Short` | `98.65` | 22,640.00 USD | 9,740.00 USD | 0.00 USD | `+1.45%` | `98.70` |
| `Live` | `Short` | `98.75` | 23,790.00 USD | 1,150.00 USD | 0.00 USD | `+1.55%` | `11.60` |
| `Live` | `Short` | `98.85` | 23,960.00 USD | 168.05 USD | 0.00 USD | `+1.66%` | `1.70` |
| `Live` | `Short` | `98.95` | 25,300.00 USD | 1,350.00 USD | 0.00 USD | `+1.76%` | `13.61` |
| `Live` | `Short` | `99.05` | 29,210.00 USD | 3,900.00 USD | 0.00 USD | `+1.86%` | `39.41` |
| `Live` | `Short` | `99.15` | 1,140,000.00 USD | 1,110,000.00 USD | 0.00 USD | `+1.96%` | `11,235.53` |
| `Live` | `Short` | `99.25` | 1,150,000.00 USD | 8,190.00 USD | 0.00 USD | `+2.07%` | `82.53` |
| `Live` | `Short` | `99.35` | 1,270,000.00 USD | 122,930.00 USD | 0.00 USD | `+2.17%` | `1,237.34` |
| `Live` | `Short` | `99.45` | 1,290,000.00 USD | 16,700.00 USD | 0.00 USD | `+2.27%` | `167.93` |
| `Live` | `Short` | `99.55` | 1,300,000.00 USD | 9,000.00 USD | 0.00 USD | `+2.38%` | `90.43` |
| `Live` | `Short` | `99.65` | 1,300,000.00 USD | 3,000.00 USD | 0.00 USD | `+2.48%` | `30.14` |
| `Live` | `Short` | `99.75` | 1,310,000.00 USD | 4,160.00 USD | 0.00 USD | `+2.58%` | `41.75` |
| `Live` | `Short` | `99.85` | 1,320,000.00 USD | 9,130.00 USD | 0.00 USD | `+2.68%` | `91.45` |
| `Live` | `Short` | `99.95` | 1,320,000.00 USD | 1,100.00 USD | 0.00 USD | `+2.79%` | `11.03` |
| `Live` | `Short` | `100.05` | 1,320,000.00 USD | 1,550.00 USD | 0.00 USD | `+2.89%` | `15.51` |
| `Live` | `Short` | `100.15` | 1,330,000.00 USD | 11,860.00 USD | 0.00 USD | `+2.99%` | `118.40` |
| `Live` | `Short` | `100.25` | 1,330,000.00 USD | 188.47 USD | 0.00 USD | `+3.10%` | `1.88` |
| `Live` | `Short` | `100.35` | 1,340,000.00 USD | 4,300.00 USD | 0.00 USD | `+3.20%` | `42.82` |
| `Live` | `Short` | `100.55` | 1,350,000.00 USD | 11,120.00 USD | 0.00 USD | `+3.40%` | `110.61` |
| `Live` | `Short` | `100.75` | 1,370,000.00 USD | 19,590.00 USD | 0.00 USD | `+3.61%` | `194.44` |
| `Live` | `Short` | `100.95` | 1,370,000.00 USD | 498.69 USD | 0.00 USD | `+3.82%` | `4.94` |
| `Live` | `Short` | `101.05` | 1,370,000.00 USD | 320.33 USD | 0.00 USD | `+3.92%` | `3.17` |
| `Live` | `Short` | `101.15` | 1,390,000.00 USD | 24,720.00 USD | 0.00 USD | `+4.02%` | `244.39` |
| `Live` | `Short` | `101.25` | 1,390,000.00 USD | 769.50 USD | 0.00 USD | `+4.12%` | `7.60` |
| `Live` | `Short` | `101.45` | 1,390,000.00 USD | 118.70 USD | 0.00 USD | `+4.33%` | `1.17` |
| `Live` | `Short` | `101.55` | 1,460,000.00 USD | 66,130.00 USD | 0.00 USD | `+4.43%` | `651.24` |
| `Live` | `Short` | `101.65` | 1,460,000.00 USD | 5,330.00 USD | 0.00 USD | `+4.54%` | `52.40` |
| `Live` | `Short` | `102.05` | 1,470,000.00 USD | 8,970.00 USD | 0.00 USD | `+4.95%` | `87.85` |
| `Live` | `Short` | `102.25` | 1,470,000.00 USD | 1,170.00 USD | 0.00 USD | `+5.15%` | `11.44` |
| `Live` | `Short` | `102.35` | 1,490,000.00 USD | 11,300.00 USD | 0.00 USD | `+5.26%` | `110.38` |
| `Live` | `Short` | `102.45` | 1,490,000.00 USD | 175.19 USD | 0.00 USD | `+5.36%` | `1.71` |
| `Live` | `Short` | `102.65` | 1,490,000.00 USD | 1,500.00 USD | 0.00 USD | `+5.56%` | `14.63` |
| `Live` | `Short` | `102.75` | 1,490,000.00 USD | 3,070.00 USD | 0.00 USD | `+5.67%` | `29.85` |
| `Live` | `Short` | `102.85` | 1,500,000.00 USD | 7,350.00 USD | 0.00 USD | `+5.77%` | `71.51` |
| `Live` | `Short` | `102.95` | 1,500,000.00 USD | 4,150.00 USD | 0.00 USD | `+5.87%` | `40.32` |
| `Live` | `Short` | `103.05` | 1,500,000.00 USD | 1,760.00 USD | 0.00 USD | `+5.97%` | `17.12` |
| `Live` | `Short` | `103.15` | 1,510,000.00 USD | 11,000.00 USD | 0.00 USD | `+6.08%` | `106.62` |
| `Live` | `Short` | `103.35` | 1,520,000.00 USD | 907.41 USD | 0.00 USD | `+6.28%` | `8.78` |
| `Live` | `Short` | `103.45` | 1,520,000.00 USD | 3,300.00 USD | 0.00 USD | `+6.39%` | `31.94` |
| `Live` | `Short` | `103.55` | 2,960,000.00 USD | 1,440,000.00 USD | 0.00 USD | `+6.49%` | `13,897.41` |
| `Live` | `Short` | `103.65` | 2,960,000.00 USD | 4,360.00 USD | 0.00 USD | `+6.59%` | `42.09` |
| `Live` | `Short` | `103.75` | 3,220,000.00 USD | 262,190.00 USD | 0.00 USD | `+6.69%` | `2,527.14` |
| `Live` | `Short` | `103.85` | 3,240,000.00 USD | 13,560.00 USD | 0.00 USD | `+6.80%` | `130.56` |
| `Live` | `Short` | `103.95` | 3,240,000.00 USD | 1,490.00 USD | 0.00 USD | `+6.90%` | `14.32` |
| `Live` | `Short` | `104.05` | 3,240,000.00 USD | 1,400.00 USD | 0.00 USD | `+7.00%` | `13.47` |
| `Live` | `Short` | `104.15` | 3,240,000.00 USD | 1,180.00 USD | 0.00 USD | `+7.11%` | `11.34` |
| `Live` | `Short` | `104.25` | 3,670,000.00 USD | 426,950.00 USD | 0.00 USD | `+7.21%` | `4,095.47` |
| `Live` | `Short` | `104.35` | 3,680,000.00 USD | 13,740.00 USD | 0.00 USD | `+7.31%` | `131.64` |
| `Live` | `Short` | `104.45` | 3,700,000.00 USD | 20,910.00 USD | 0.00 USD | `+7.41%` | `200.19` |
| `Live` | `Short` | `104.55` | 3,710,000.00 USD | 10,810.00 USD | 0.00 USD | `+7.52%` | `103.37` |
| `Live` | `Short` | `104.65` | 3,720,000.00 USD | 925.11 USD | 0.00 USD | `+7.62%` | `8.84` |
| `Live` | `Short` | `104.75` | 3,720,000.00 USD | 199.02 USD | 0.00 USD | `+7.72%` | `1.90` |
| `Live` | `Short` | `104.95` | 3,840,000.00 USD | 125,660.00 USD | 0.00 USD | `+7.93%` | `1,197.29` |
| `Live` | `Short` | `105.05` | 3,840,000.00 USD | 329.86 USD | 0.00 USD | `+8.03%` | `3.14` |
| `Live` | `Short` | `105.15` | 3,850,000.00 USD | 6,410.00 USD | 0.00 USD | `+8.13%` | `60.95` |
| `Live` | `Short` | `105.25` | 3,850,000.00 USD | 1,040.00 USD | 0.00 USD | `+8.24%` | `9.84` |
| `Live` | `Short` | `105.35` | 3,850,000.00 USD | 1,650.00 USD | 0.00 USD | `+8.34%` | `15.68` |
| `Live` | `Short` | `105.45` | 4,380,000.00 USD | 529,050.00 USD | 0.00 USD | `+8.44%` | `5,017.10` |
| `Live` | `Short` | `105.55` | 4,390,000.00 USD | 8,190.00 USD | 0.00 USD | `+8.55%` | `77.55` |
| `Live` | `Short` | `105.75` | 4,390,000.00 USD | 247.45 USD | 0.00 USD | `+8.75%` | `2.34` |
| `Live` | `Short` | `105.85` | 4,480,000.00 USD | 91,370.00 USD | 0.00 USD | `+8.85%` | `863.23` |
| `Live` | `Short` | `105.95` | 4,480,000.00 USD | 592.26 USD | 0.00 USD | `+8.96%` | `5.59` |
| `Live` | `Short` | `106.05` | 4,510,000.00 USD | 33,380.00 USD | 0.00 USD | `+9.06%` | `314.77` |
| `Live` | `Short` | `106.25` | 4,510,000.00 USD | 191.25 USD | 0.00 USD | `+9.27%` | `1.80` |
| `Live` | `Short` | `106.35` | 4,770,000.00 USD | 252,220.00 USD | 0.00 USD | `+9.37%` | `2,371.56` |
| `Live` | `Short` | `106.45` | 4,800,000.00 USD | 32,940.00 USD | 0.00 USD | `+9.47%` | `309.43` |
| `Live` | `Short` | `106.75` | 5,200,000.00 USD | 397,560.00 USD | 0.00 USD | `+9.78%` | `3,724.17` |
| `Live` | `Short` | `106.85` | 5,680,000.00 USD | 480,860.00 USD | 0.00 USD | `+9.88%` | `4,500.31` |
| `Live` | `Short` | `106.95` | 5,680,000.00 USD | 651.33 USD | 0.00 USD | `+9.99%` | `6.09` |
| `Live` | `Short` | `107.05` | 5,690,000.00 USD | 17,260.00 USD | 0.00 USD | `+10.09%` | `161.19` |
| `Live` | `Short` | `107.15` | 5,700,000.00 USD | 3,060.00 USD | 0.00 USD | `+10.19%` | `28.58` |
| `Live` | `Short` | `107.25` | 5,750,000.00 USD | 47,370.00 USD | 0.00 USD | `+10.29%` | `441.68` |
| `Live` | `Short` | `107.35` | 5,750,000.00 USD | 766.48 USD | 0.00 USD | `+10.40%` | `7.14` |
| `Live` | `Short` | `107.45` | 5,780,000.00 USD | 32,580.00 USD | 0.00 USD | `+10.50%` | `303.18` |
| `Live` | `Short` | `107.55` | 5,780,000.00 USD | 221.55 USD | 0.00 USD | `+10.60%` | `2.06` |
| `Live` | `Short` | `107.65` | 5,780,000.00 USD | 1,820.00 USD | 0.00 USD | `+10.71%` | `16.87` |
| `Live` | `Short` | `107.85` | 5,920,000.00 USD | 143,340.00 USD | 0.00 USD | `+10.91%` | `1,329.08` |
| `Live` | `Short` | `108.05` | 5,930,000.00 USD | 1,080.00 USD | 0.00 USD | `+11.12%` | `10.04` |
| `Live` | `Short` | `108.15` | 5,930,000.00 USD | 1,150.00 USD | 0.00 USD | `+11.22%` | `10.66` |
| `Live` | `Short` | `108.25` | 5,930,000.00 USD | 116.91 USD | 0.00 USD | `+11.32%` | `1.08` |
| `Live` | `Short` | `108.35` | 5,930,000.00 USD | 3,470.00 USD | 0.00 USD | `+11.43%` | `32.00` |
| `Live` | `Short` | `108.45` | 6,040,000.00 USD | 111,070.00 USD | 0.00 USD | `+11.53%` | `1,024.14` |
| `Live` | `Short` | `108.55` | 6,040,000.00 USD | 117.23 USD | 0.00 USD | `+11.63%` | `1.08` |
| `Live` | `Short` | `108.65` | 6,060,000.00 USD | 22,400.00 USD | 0.00 USD | `+11.73%` | `206.20` |
| `Live` | `Short` | `108.85` | 6,070,000.00 USD | 3,230.00 USD | 0.00 USD | `+11.94%` | `29.68` |
| `Live` | `Short` | `108.95` | 6,070,000.00 USD | 3,170.00 USD | 0.00 USD | `+12.04%` | `29.10` |
| `Live` | `Short` | `109.05` | 6,070,000.00 USD | 163.58 USD | 0.00 USD | `+12.15%` | `1.50` |
| `Live` | `Short` | `109.15` | 6,070,000.00 USD | 2,120.00 USD | 0.00 USD | `+12.25%` | `19.46` |
| `Live` | `Short` | `109.35` | 6,070,000.00 USD | 247.13 USD | 0.00 USD | `+12.45%` | `2.26` |
| `Live` | `Short` | `109.45` | 6,070,000.00 USD | 342.58 USD | 0.00 USD | `+12.56%` | `3.13` |
| `Live` | `Short` | `109.55` | 6,070,000.00 USD | 356.04 USD | 0.00 USD | `+12.66%` | `3.25` |
| `Live` | `Short` | `109.65` | 6,120,000.00 USD | 42,030.00 USD | 0.00 USD | `+12.76%` | `383.35` |
| `Live` | `Short` | `109.85` | 6,120,000.00 USD | 459.17 USD | 0.00 USD | `+12.97%` | `4.18` |
| `Live` | `Short` | `109.95` | 6,120,000.00 USD | 301.26 USD | 0.00 USD | `+13.07%` | `2.74` |
| `Live` | `Short` | `110.15` | 6,120,000.00 USD | 3,170.00 USD | 0.00 USD | `+13.28%` | `28.78` |
| `Live` | `Short` | `110.35` | 6,120,000.00 USD | 158.90 USD | 0.00 USD | `+13.48%` | `1.44` |
| `Live` | `Short` | `110.45` | 6,260,000.00 USD | 143,390.00 USD | 0.00 USD | `+13.58%` | `1,298.27` |
| `Live` | `Short` | `110.55` | 6,260,000.00 USD | 580.39 USD | 0.00 USD | `+13.69%` | `5.25` |
| `Live` | `Short` | `110.65` | 6,270,000.00 USD | 10,240.00 USD | 0.00 USD | `+13.79%` | `92.54` |
| `Live` | `Short` | `110.75` | 6,270,000.00 USD | 575.90 USD | 0.00 USD | `+13.89%` | `5.20` |
| `Live` | `Short` | `110.85` | 6,280,000.00 USD | 1,090.00 USD | 0.00 USD | `+14.00%` | `9.87` |
| `Live` | `Short` | `110.95` | 6,280,000.00 USD | 5,040.00 USD | 0.00 USD | `+14.10%` | `45.39` |
| `Live` | `Short` | `111.15` | 6,280,000.00 USD | 1,710.00 USD | 0.00 USD | `+14.30%` | `15.37` |
| `Live` | `Short` | `111.35` | 6,280,000.00 USD | 390.84 USD | 0.00 USD | `+14.51%` | `3.51` |
| `Live` | `Short` | `111.45` | 6,280,000.00 USD | 1,390.00 USD | 0.00 USD | `+14.61%` | `12.45` |
| `Live` | `Short` | `111.75` | 6,280,000.00 USD | 169.86 USD | 0.00 USD | `+14.92%` | `1.52` |
| `Live` | `Short` | `111.85` | 6,330,000.00 USD | 44,370.00 USD | 0.00 USD | `+15.02%` | `396.66` |
| `Live` | `Short` | `111.95` | 6,590,000.00 USD | 260,360.00 USD | 0.00 USD | `+15.13%` | `2,325.72` |
| `Live` | `Short` | `112.15` | 6,590,000.00 USD | 291.59 USD | 0.00 USD | `+15.33%` | `2.60` |
| `Live` | `Short` | `112.35` | 6,590,000.00 USD | 1,910.00 USD | 0.00 USD | `+15.54%` | `17.00` |
| `Live` | `Short` | `112.45` | 6,600,000.00 USD | 8,710.00 USD | 0.00 USD | `+15.64%` | `77.45` |
| `Live` | `Short` | `112.55` | 6,600,000.00 USD | 844.13 USD | 0.00 USD | `+15.74%` | `7.50` |
| `Live` | `Short` | `112.65` | 6,600,000.00 USD | 707.44 USD | 0.00 USD | `+15.85%` | `6.28` |
| `Live` | `Short` | `112.75` | 6,720,000.00 USD | 118,640.00 USD | 0.00 USD | `+15.95%` | `1,052.24` |
| `Live` | `Short` | `112.85` | 6,830,000.00 USD | 108,760.00 USD | 0.00 USD | `+16.05%` | `963.76` |
| `Live` | `Short` | `113.05` | 6,830,000.00 USD | 406.98 USD | 0.00 USD | `+16.26%` | `3.60` |
| `Live` | `Short` | `113.15` | 6,840,000.00 USD | 9,560.00 USD | 0.00 USD | `+16.36%` | `84.51` |
| `Live` | `Short` | `113.25` | 6,840,000.00 USD | 3,840.00 USD | 0.00 USD | `+16.46%` | `33.89` |
| `Live` | `Short` | `113.35` | 6,840,000.00 USD | 1,240.00 USD | 0.00 USD | `+16.57%` | `10.94` |
| `Live` | `Short` | `113.45` | 6,850,000.00 USD | 3,480.00 USD | 0.00 USD | `+16.67%` | `30.65` |
| `Live` | `Short` | `113.55` | 6,950,000.00 USD | 102,780.00 USD | 0.00 USD | `+16.77%` | `905.15` |
| `Live` | `Short` | `113.65` | 6,950,000.00 USD | 3,220.00 USD | 0.00 USD | `+16.88%` | `28.37` |
| `Live` | `Short` | `113.75` | 6,950,000.00 USD | 303.71 USD | 0.00 USD | `+16.98%` | `2.67` |
| `Live` | `Short` | `113.85` | 6,950,000.00 USD | 104.74 USD | 0.00 USD | `+17.08%` | `0.92` |
| `Live` | `Short` | `113.95` | 6,980,000.00 USD | 21,840.00 USD | 0.00 USD | `+17.18%` | `191.69` |
| `Live` | `Short` | `114.05` | 7,010,000.00 USD | 31,740.00 USD | 0.00 USD | `+17.29%` | `278.26` |
| `Live` | `Short` | `114.25` | 7,010,000.00 USD | 2,150.00 USD | 0.00 USD | `+17.49%` | `18.80` |
| `Live` | `Short` | `114.45` | 7,010,000.00 USD | 3,310.00 USD | 0.00 USD | `+17.70%` | `28.93` |
| `Live` | `Short` | `115.05` | 7,580,000.00 USD | 569,710.00 USD | 0.00 USD | `+18.32%` | `4,951.89` |
| `Live` | `Short` | `115.15` | 7,580,000.00 USD | 1,100.00 USD | 0.00 USD | `+18.42%` | `9.52` |
| `Live` | `Short` | `115.35` | 7,600,000.00 USD | 14,710.00 USD | 0.00 USD | `+18.62%` | `127.54` |
| `Live` | `Short` | `115.45` | 8,500,000.00 USD | 906,520.00 USD | 0.00 USD | `+18.73%` | `7,852.04` |
| `Live` | `Short` | `115.55` | 8,550,000.00 USD | 43,020.00 USD | 0.00 USD | `+18.83%` | `372.33` |
| `Live` | `Short` | `115.75` | 8,550,000.00 USD | 160.89 USD | 0.00 USD | `+19.04%` | `1.39` |
| `Live` | `Short` | `115.85` | 8,550,000.00 USD | 4,340.00 USD | 0.00 USD | `+19.14%` | `37.50` |
| `Live` | `Short` | `116.05` | 8,560,000.00 USD | 4,450.00 USD | 0.00 USD | `+19.34%` | `38.34` |
| `Live` | `Short` | `116.25` | 8,560,000.00 USD | 180.19 USD | 0.00 USD | `+19.55%` | `1.55` |
| `Live` | `Short` | `116.35` | 8,560,000.00 USD | 4,960.00 USD | 0.00 USD | `+19.65%` | `42.60` |
| `Live` | `Short` | `116.55` | 8,560,000.00 USD | 2,040.00 USD | 0.00 USD | `+19.86%` | `17.52` |
| `Live` | `Short` | `116.65` | 8,560,000.00 USD | 113.15 USD | 0.00 USD | `+19.96%` | `0.97` |
| `Live` | `Short` | `116.85` | 8,660,000.00 USD | 99,900.00 USD | 0.00 USD | `+20.17%` | `854.97` |
| `Live` | `Short` | `117.05` | 8,660,000.00 USD | 156.85 USD | 0.00 USD | `+20.37%` | `1.34` |
| `Live` | `Short` | `117.15` | 8,750,000.00 USD | 89,950.00 USD | 0.00 USD | `+20.48%` | `767.80` |
| `Live` | `Short` | `117.25` | 13,530,000.00 USD | 4,770,000.00 USD | 0.00 USD | `+20.58%` | `40,716.81` |
| `Live` | `Short` | `117.35` | 13,540,000.00 USD | 11,840.00 USD | 0.00 USD | `+20.68%` | `100.91` |
| `Live` | `Short` | `117.45` | 13,540,000.00 USD | 1,500.00 USD | 0.00 USD | `+20.78%` | `12.80` |
| `Live` | `Short` | `117.55` | 13,540,000.00 USD | 1,920.00 USD | 0.00 USD | `+20.89%` | `16.32` |
| `Live` | `Short` | `117.75` | 13,550,000.00 USD | 10,360.00 USD | 0.00 USD | `+21.09%` | `87.98` |
| `Live` | `Short` | `117.85` | 14,110,000.00 USD | 555,010.00 USD | 0.00 USD | `+21.19%` | `4,709.47` |
| `Live` | `Short` | `117.95` | 14,150,000.00 USD | 44,800.00 USD | 0.00 USD | `+21.30%` | `379.78` |
| `Live` | `Short` | `118.15` | 18,630,000.00 USD | 4,480,000.00 USD | 0.00 USD | `+21.50%` | `37,886.13` |
| `Live` | `Short` | `118.45` | 18,680,000.00 USD | 53,770.00 USD | 0.00 USD | `+21.81%` | `453.91` |
| `Live` | `Short` | `118.55` | 18,680,000.00 USD | 1,110.00 USD | 0.00 USD | `+21.91%` | `9.38` |
| `Live` | `Short` | `118.75` | 18,680,000.00 USD | 309.94 USD | 0.00 USD | `+22.12%` | `2.61` |
| `Live` | `Short` | `118.95` | 18,700,000.00 USD | 10,930.00 USD | 0.00 USD | `+22.33%` | `91.90` |
| `Live` | `Short` | `119.15` | 18,700,000.00 USD | 2,350.00 USD | 0.00 USD | `+22.53%` | `19.76` |
| `Live` | `Short` | `119.25` | 18,730,000.00 USD | 28,090.00 USD | 0.00 USD | `+22.63%` | `235.57` |
| `Live` | `Short` | `119.35` | 18,800,000.00 USD | 70,380.00 USD | 0.00 USD | `+22.74%` | `589.72` |
| `Live` | `Short` | `119.75` | 18,800,000.00 USD | 261.06 USD | 0.00 USD | `+23.15%` | `2.18` |
| `Live` | `Short` | `119.85` | 18,800,000.00 USD | 485.39 USD | 0.00 USD | `+23.25%` | `4.05` |
| `Live` | `Short` | `119.95` | 18,890,000.00 USD | 96,050.00 USD | 0.00 USD | `+23.35%` | `800.76` |
| `Live` | `Short` | `120.05` | 18,890,000.00 USD | 452.59 USD | 0.00 USD | `+23.46%` | `3.77` |
| `Live` | `Short` | `120.15` | 18,900,000.00 USD | 2,980.00 USD | 0.00 USD | `+23.56%` | `24.83` |
| `Live` | `Short` | `120.45` | 18,900,000.00 USD | 145.74 USD | 0.00 USD | `+23.87%` | `1.21` |
| `Live` | `Short` | `120.55` | 18,900,000.00 USD | 1,190.00 USD | 0.00 USD | `+23.97%` | `9.86` |
| `Live` | `Short` | `120.65` | 19,770,000.00 USD | 869,200.00 USD | 0.00 USD | `+24.07%` | `7,204.35` |
| `Live` | `Short` | `120.95` | 19,780,000.00 USD | 13,290.00 USD | 0.00 USD | `+24.38%` | `109.91` |
| `Live` | `Short` | `121.15` | 19,780,000.00 USD | 316.20 USD | 0.00 USD | `+24.59%` | `2.61` |
| `Live` | `Short` | `121.55` | 19,790,000.00 USD | 5,940.00 USD | 0.00 USD | `+25.00%` | `48.87` |
| `Live` | `Short` | `121.75` | 19,790,000.00 USD | 105.92 USD | 0.00 USD | `+25.21%` | `0.87` |
| `Live` | `Short` | `122.05` | 19,840,000.00 USD | 56,150.00 USD | 0.00 USD | `+25.51%` | `460.06` |
| `Live` | `Short` | `122.15` | 19,840,000.00 USD | 819.63 USD | 0.00 USD | `+25.62%` | `6.71` |
| `Live` | `Short` | `122.25` | 19,850,000.00 USD | 2,330.00 USD | 0.00 USD | `+25.72%` | `19.10` |
| `Live` | `Short` | `122.45` | 19,860,000.00 USD | 17,500.00 USD | 0.00 USD | `+25.93%` | `142.95` |
| `Live` | `Short` | `122.55` | 19,870,000.00 USD | 1,580.00 USD | 0.00 USD | `+26.03%` | `12.89` |
| `Live` | `Short` | `122.65` | 19,870,000.00 USD | 840.15 USD | 0.00 USD | `+26.13%` | `6.85` |
| `Live` | `Short` | `122.85` | 19,870,000.00 USD | 342.75 USD | 0.00 USD | `+26.34%` | `2.79` |
| `Live` | `Short` | `122.95` | 19,870,000.00 USD | 2,170.00 USD | 0.00 USD | `+26.44%` | `17.66` |
| `Live` | `Short` | `123.25` | 19,870,000.00 USD | 188.57 USD | 0.00 USD | `+26.75%` | `1.53` |
| `Live` | `Short` | `123.35` | 20,000,000.00 USD | 127,060.00 USD | 0.00 USD | `+26.85%` | `1,030.10` |
| `Live` | `Short` | `123.45` | 20,000,000.00 USD | 1,960.00 USD | 0.00 USD | `+26.95%` | `15.87` |
| `Live` | `Short` | `123.95` | 29,140,000.00 USD | 9,140,000.00 USD | 0.00 USD | `+27.47%` | `73,749.04` |
| `Live` | `Short` | `124.05` | 29,140,000.00 USD | 586.76 USD | 0.00 USD | `+27.57%` | `4.73` |
| `Live` | `Short` | `124.15` | 29,140,000.00 USD | 121.67 USD | 0.00 USD | `+27.67%` | `0.98` |
| `Live` | `Short` | `124.25` | 29,160,000.00 USD | 23,360.00 USD | 0.00 USD | `+27.78%` | `188.01` |
| `Live` | `Short` | `124.35` | 29,160,000.00 USD | 114.40 USD | 0.00 USD | `+27.88%` | `0.92` |
| `Live` | `Short` | `124.55` | 29,170,000.00 USD | 3,080.00 USD | 0.00 USD | `+28.09%` | `24.76` |
| `Live` | `Short` | `124.65` | 29,170,000.00 USD | 675.60 USD | 0.00 USD | `+28.19%` | `5.42` |
| `Live` | `Short` | `124.75` | 29,220,000.00 USD | 51,550.00 USD | 0.00 USD | `+28.29%` | `413.23` |
| `Live` | `Short` | `124.95` | 29,220,000.00 USD | 2,800.00 USD | 0.00 USD | `+28.50%` | `22.41` |
| `Live` | `Short` | `125.05` | 29,220,000.00 USD | 208.83 USD | 0.00 USD | `+28.60%` | `1.67` |
| `Live` | `Short` | `125.35` | 29,230,000.00 USD | 6,780.00 USD | 0.00 USD | `+28.91%` | `54.05` |
| `Live` | `Short` | `125.45` | 29,230,000.00 USD | 5,910.00 USD | 0.00 USD | `+29.01%` | `47.15` |
| `Live` | `Short` | `125.55` | 29,240,000.00 USD | 4,610.00 USD | 0.00 USD | `+29.11%` | `36.71` |
| `Live` | `Short` | `125.65` | 29,240,000.00 USD | 851.91 USD | 0.00 USD | `+29.22%` | `6.78` |
| `Live` | `Short` | `125.75` | 29,240,000.00 USD | 4,600.00 USD | 0.00 USD | `+29.32%` | `36.61` |
| `Live` | `Short` | `125.95` | 29,240,000.00 USD | 110.84 USD | 0.00 USD | `+29.52%` | `0.88` |
| `Live` | `Short` | `126.15` | 29,250,000.00 USD | 1,280.00 USD | 0.00 USD | `+29.73%` | `10.16` |
| `Live` | `Short` | `126.35` | 29,250,000.00 USD | 4,090.00 USD | 0.00 USD | `+29.94%` | `32.36` |
| `Live` | `Short` | `126.45` | 29,500,000.00 USD | 253,020.00 USD | 0.00 USD | `+30.04%` | `2,000.93` |
| `Live` | `Short` | `126.55` | 29,500,000.00 USD | 318.91 USD | 0.00 USD | `+30.14%` | `2.52` |
| `Live` | `Short` | `126.65` | 29,530,000.00 USD | 31,130.00 USD | 0.00 USD | `+30.24%` | `245.77` |
| `Live` | `Short` | `126.85` | 29,540,000.00 USD | 3,870.00 USD | 0.00 USD | `+30.45%` | `30.49` |
| `Live` | `Short` | `127.05` | 29,540,000.00 USD | 2,030.00 USD | 0.00 USD | `+30.66%` | `16.01` |
| `Live` | `Short` | `127.35` | 29,560,000.00 USD | 16,190.00 USD | 0.00 USD | `+30.96%` | `127.13` |
| `Live` | `Short` | `127.55` | 29,560,000.00 USD | 1,650.00 USD | 0.00 USD | `+31.17%` | `12.93` |
| `Live` | `Short` | `127.65` | 29,560,000.00 USD | 4,840.00 USD | 0.00 USD | `+31.27%` | `37.89` |
| `Live` | `Short` | `127.75` | 29,560,000.00 USD | 720.51 USD | 0.00 USD | `+31.38%` | `5.64` |
| `Live` | `Short` | `127.85` | 29,560,000.00 USD | 388.66 USD | 0.00 USD | `+31.48%` | `3.04` |
| `Live` | `Short` | `127.95` | 29,570,000.00 USD | 10,510.00 USD | 0.00 USD | `+31.58%` | `82.13` |
| `Live` | `Short` | `128.05` | 29,690,000.00 USD | 116,190.00 USD | 0.00 USD | `+31.68%` | `907.38` |
| `Live` | `Short` | `128.15` | 29,700,000.00 USD | 6,410.00 USD | 0.00 USD | `+31.79%` | `50.00` |
| `Live` | `Short` | `128.35` | 29,700,000.00 USD | 195.09 USD | 0.00 USD | `+31.99%` | `1.52` |
| `Live` | `Short` | `128.65` | 29,700,000.00 USD | 788.62 USD | 0.00 USD | `+32.30%` | `6.13` |
| `Live` | `Short` | `128.75` | 29,720,000.00 USD | 18,730.00 USD | 0.00 USD | `+32.40%` | `145.45` |
| `Live` | `Short` | `128.85` | 29,760,000.00 USD | 41,020.00 USD | 0.00 USD | `+32.51%` | `318.39` |
| `Live` | `Short` | `129.15` | 29,810,000.00 USD | 55,570.00 USD | 0.00 USD | `+32.82%` | `430.25` |
| `Live` | `Short` | `129.25` | 30,540,000.00 USD | 730,990.00 USD | 0.00 USD | `+32.92%` | `5,655.66` |
| `Live` | `Short` | `129.35` | 30,610,000.00 USD | 68,800.00 USD | 0.00 USD | `+33.02%` | `531.88` |
| `Live` | `Short` | `129.55` | 30,610,000.00 USD | 910.74 USD | 0.00 USD | `+33.23%` | `7.03` |
| `Live` | `Short` | `129.75` | 30,620,000.00 USD | 2,210.00 USD | 0.00 USD | `+33.43%` | `17.05` |
| `Live` | `Short` | `129.85` | 30,620,000.00 USD | 490.83 USD | 0.00 USD | `+33.54%` | `3.78` |
| `Live` | `Short` | `130.15` | 30,630,000.00 USD | 13,190.00 USD | 0.00 USD | `+33.84%` | `101.38` |
| `Live` | `Short` | `130.35` | 30,630,000.00 USD | 145.99 USD | 0.00 USD | `+34.05%` | `1.12` |
| `Live` | `Short` | `130.85` | 31,130,000.00 USD | 503,820.00 USD | 0.00 USD | `+34.56%` | `3,850.39` |
| `Live` | `Short` | `130.95` | 31,140,000.00 USD | 2,070.00 USD | 0.00 USD | `+34.67%` | `15.84` |
| `Live` | `Short` | `131.05` | 31,140,000.00 USD | 188.71 USD | 0.00 USD | `+34.77%` | `1.44` |
| `Live` | `Short` | `131.25` | 31,140,000.00 USD | 1,560.00 USD | 0.00 USD | `+34.98%` | `11.87` |
| `Live` | `Short` | `131.35` | 31,140,000.00 USD | 855.09 USD | 0.00 USD | `+35.08%` | `6.51` |
| `Live` | `Short` | `131.45` | 31,140,000.00 USD | 219.52 USD | 0.00 USD | `+35.18%` | `1.67` |
| `Live` | `Short` | `131.75` | 31,140,000.00 USD | 3,600.00 USD | 0.00 USD | `+35.49%` | `27.29` |
| `Live` | `Short` | `131.85` | 31,150,000.00 USD | 3,100.00 USD | 0.00 USD | `+35.59%` | `23.54` |
| `Live` | `Short` | `131.95` | 31,150,000.00 USD | 240.15 USD | 0.00 USD | `+35.70%` | `1.82` |
| `Live` | `Short` | `132.05` | 31,160,000.00 USD | 11,940.00 USD | 0.00 USD | `+35.80%` | `90.43` |
| `Live` | `Short` | `132.15` | 31,160,000.00 USD | 325.09 USD | 0.00 USD | `+35.90%` | `2.46` |
| `Live` | `Short` | `132.55` | 31,170,000.00 USD | 8,730.00 USD | 0.00 USD | `+36.31%` | `65.85` |
| `Live` | `Short` | `132.65` | 31,170,000.00 USD | 630.09 USD | 0.00 USD | `+36.42%` | `4.75` |
| `Live` | `Short` | `132.75` | 31,230,000.00 USD | 66,380.00 USD | 0.00 USD | `+36.52%` | `500.00` |
| `Live` | `Short` | `132.85` | 31,280,000.00 USD | 49,280.00 USD | 0.00 USD | `+36.62%` | `370.98` |
| `Live` | `Short` | `133.05` | 31,310,000.00 USD | 30,050.00 USD | 0.00 USD | `+36.83%` | `225.86` |
| `Live` | `Short` | `133.15` | 31,320,000.00 USD | 8,440.00 USD | 0.00 USD | `+36.93%` | `63.42` |
| `Live` | `Short` | `133.35` | 31,370,000.00 USD | 47,960.00 USD | 0.00 USD | `+37.13%` | `359.64` |
| `Live` | `Short` | `133.65` | 31,370,000.00 USD | 156.37 USD | 0.00 USD | `+37.44%` | `1.17` |
| `Live` | `Short` | `133.75` | 31,520,000.00 USD | 151,200.00 USD | 0.00 USD | `+37.55%` | `1,130.50` |
| `Live` | `Short` | `133.95` | 31,520,000.00 USD | 2,110.00 USD | 0.00 USD | `+37.75%` | `15.73` |
| `Live` | `Short` | `134.05` | 31,540,000.00 USD | 12,620.00 USD | 0.00 USD | `+37.85%` | `94.18` |
| `Live` | `Short` | `134.25` | 31,570,000.00 USD | 36,990.00 USD | 0.00 USD | `+38.06%` | `275.56` |
| `Live` | `Short` | `134.95` | 31,580,000.00 USD | 4,040.00 USD | 0.00 USD | `+38.78%` | `29.93` |
| `Live` | `Short` | `135.45` | 31,580,000.00 USD | 6,410.00 USD | 0.00 USD | `+39.29%` | `47.30` |
| `Live` | `Short` | `135.85` | 31,590,000.00 USD | 3,250.00 USD | 0.00 USD | `+39.71%` | `23.94` |
| `Live` | `Short` | `135.95` | 31,590,000.00 USD | 504.37 USD | 0.00 USD | `+39.81%` | `3.71` |
| `Live` | `Short` | `136.05` | 31,590,000.00 USD | 1,400.00 USD | 0.00 USD | `+39.91%` | `10.26` |
| `Live` | `Short` | `136.55` | 31,590,000.00 USD | 136.55 USD | 0.00 USD | `+40.43%` | `1.00` |
| `Live` | `Short` | `136.65` | 31,590,000.00 USD | 1,110.00 USD | 0.00 USD | `+40.53%` | `8.14` |
| `Live` | `Short` | `136.75` | 31,600,000.00 USD | 14,700.00 USD | 0.00 USD | `+40.63%` | `107.50` |
| `Live` | `Short` | `136.95` | 31,640,000.00 USD | 34,240.00 USD | 0.00 USD | `+40.84%` | `250.00` |
| `Live` | `Short` | `137.05` | 31,640,000.00 USD | 836.00 USD | 0.00 USD | `+40.94%` | `6.10` |
| `Live` | `Short` | `137.15` | 31,640,000.00 USD | 809.19 USD | 0.00 USD | `+41.04%` | `5.90` |
| `Live` | `Short` | `137.45` | 31,640,000.00 USD | 696.87 USD | 0.00 USD | `+41.35%` | `5.07` |
| `Live` | `Short` | `137.65` | 31,640,000.00 USD | 2,050.00 USD | 0.00 USD | `+41.56%` | `14.87` |
| `Live` | `Short` | `137.85` | 31,750,000.00 USD | 105,020.00 USD | 0.00 USD | `+41.76%` | `761.84` |
| `Live` | `Short` | `137.95` | 31,750,000.00 USD | 2,820.00 USD | 0.00 USD | `+41.87%` | `20.42` |
| `Live` | `Short` | `138.05` | 31,750,000.00 USD | 1,270.00 USD | 0.00 USD | `+41.97%` | `9.20` |
| `Live` | `Short` | `138.15` | 31,790,000.00 USD | 41,450.00 USD | 0.00 USD | `+42.07%` | `300.00` |
| `Live` | `Short` | `138.25` | 31,840,000.00 USD | 45,220.00 USD | 0.00 USD | `+42.17%` | `327.11` |
| `Live` | `Short` | `138.45` | 31,890,000.00 USD | 50,490.00 USD | 0.00 USD | `+42.38%` | `364.66` |
| `Live` | `Short` | `138.75` | 31,890,000.00 USD | 2,360.00 USD | 0.00 USD | `+42.69%` | `17.04` |
| `Live` | `Short` | `138.95` | 31,890,000.00 USD | 653.06 USD | 0.00 USD | `+42.89%` | `4.70` |
| `Live` | `Short` | `139.05` | 31,910,000.00 USD | 13,180.00 USD | 0.00 USD | `+43.00%` | `94.76` |
| `Live` | `Short` | `139.15` | 31,910,000.00 USD | 552.43 USD | 0.00 USD | `+43.10%` | `3.97` |
| `Live` | `Short` | `139.25` | 31,910,000.00 USD | 392.69 USD | 0.00 USD | `+43.20%` | `2.82` |
| `Live` | `Short` | `139.45` | 31,910,000.00 USD | 253.80 USD | 0.00 USD | `+43.41%` | `1.82` |
| `Live` | `Short` | `139.55` | 31,910,000.00 USD | 2,170.00 USD | 0.00 USD | `+43.51%` | `15.56` |
| `Live` | `Short` | `139.65` | 31,920,000.00 USD | 8,990.00 USD | 0.00 USD | `+43.61%` | `64.35` |
| `Live` | `Short` | `139.75` | 31,920,000.00 USD | 136.95 USD | 0.00 USD | `+43.72%` | `0.98` |
| `Live` | `Short` | `139.95` | 31,920,000.00 USD | 394.66 USD | 0.00 USD | `+43.92%` | `2.82` |
| `Live` | `Short` | `140.05` | 31,920,000.00 USD | 116.24 USD | 0.00 USD | `+44.03%` | `0.83` |
| `Live` | `Short` | `140.25` | 31,920,000.00 USD | 625.51 USD | 0.00 USD | `+44.23%` | `4.46` |
| `Live` | `Short` | `140.35` | 31,930,000.00 USD | 12,760.00 USD | 0.00 USD | `+44.33%` | `90.91` |
| `Live` | `Short` | `140.45` | 31,940,000.00 USD | 4,870.00 USD | 0.00 USD | `+44.44%` | `34.66` |
| `Live` | `Short` | `140.55` | 31,940,000.00 USD | 702.75 USD | 0.00 USD | `+44.54%` | `5.00` |
| `Live` | `Short` | `140.65` | 31,960,000.00 USD | 26,180.00 USD | 0.00 USD | `+44.64%` | `186.17` |
| `Live` | `Short` | `140.75` | 32,030,000.00 USD | 67,230.00 USD | 0.00 USD | `+44.74%` | `477.67` |
| `Live` | `Short` | `140.95` | 32,030,000.00 USD | 1,940.00 USD | 0.00 USD | `+44.95%` | `13.73` |
| `Live` | `Short` | `141.05` | 37,060,000.00 USD | 5,020,000.00 USD | 0.00 USD | `+45.05%` | `35,611.87` |
| `Live` | `Short` | `141.35` | 37,060,000.00 USD | 210.61 USD | 0.00 USD | `+45.36%` | `1.49` |
| `Live` | `Short` | `141.45` | 39,250,000.00 USD | 2,190,000.00 USD | 0.00 USD | `+45.46%` | `15,496.11` |
| `Live` | `Short` | `141.55` | 39,250,000.00 USD | 236.39 USD | 0.00 USD | `+45.57%` | `1.67` |
| `Live` | `Short` | `141.75` | 39,280,000.00 USD | 27,660.00 USD | 0.00 USD | `+45.77%` | `195.13` |
| `Live` | `Short` | `141.85` | 39,280,000.00 USD | 916.35 USD | 0.00 USD | `+45.88%` | `6.46` |
| `Live` | `Short` | `141.95` | 39,280,000.00 USD | 112.14 USD | 0.00 USD | `+45.98%` | `0.79` |
| `Live` | `Short` | `142.45` | 39,280,000.00 USD | 151.00 USD | 0.00 USD | `+46.49%` | `1.06` |
| `Live` | `Short` | `142.65` | 39,280,000.00 USD | 2,150.00 USD | 0.00 USD | `+46.70%` | `15.09` |
| `Live` | `Short` | `142.75` | 39,280,000.00 USD | 368.30 USD | 0.00 USD | `+46.80%` | `2.58` |
| `Live` | `Short` | `143.15` | 39,280,000.00 USD | 1,330.00 USD | 0.00 USD | `+47.21%` | `9.31` |
| `Live` | `Short` | `143.35` | 39,300,000.00 USD | 22,260.00 USD | 0.00 USD | `+47.42%` | `155.27` |
| `Live` | `Short` | `143.45` | 39,310,000.00 USD | 2,830.00 USD | 0.00 USD | `+47.52%` | `19.75` |
| `Live` | `Short` | `143.65` | 39,330,000.00 USD | 23,220.00 USD | 0.00 USD | `+47.73%` | `161.66` |
| `Live` | `Short` | `143.75` | 39,330,000.00 USD | 2,690.00 USD | 0.00 USD | `+47.83%` | `18.73` |
| `Live` | `Short` | `143.85` | 39,930,000.00 USD | 597,720.00 USD | 0.00 USD | `+47.93%` | `4,155.17` |
| `Live` | `Short` | `144.05` | 39,930,000.00 USD | 3,750.00 USD | 0.00 USD | `+48.14%` | `26.00` |
| `Live` | `Short` | `144.55` | 40,040,000.00 USD | 105,540.00 USD | 0.00 USD | `+48.65%` | `730.14` |
| `Live` | `Short` | `144.65` | 40,040,000.00 USD | 1,240.00 USD | 0.00 USD | `+48.76%` | `8.60` |
| `Live` | `Short` | `144.95` | 40,130,000.00 USD | 87,650.00 USD | 0.00 USD | `+49.06%` | `604.67` |
| `Live` | `Short` | `145.15` | 40,130,000.00 USD | 1,760.00 USD | 0.00 USD | `+49.27%` | `12.12` |
| `Live` | `Short` | `145.45` | 40,160,000.00 USD | 30,330.00 USD | 0.00 USD | `+49.58%` | `208.52` |
| `Live` | `Short` | `145.85` | 40,170,000.00 USD | 6,340.00 USD | 0.00 USD | `+49.99%` | `43.45` |
| `Live` | `Short` | `146.15` | 40,250,000.00 USD | 88,760.00 USD | 0.00 USD | `+50.30%` | `607.33` |
| `Live` | `Short` | `146.25` | 40,260,000.00 USD | 2,770.00 USD | 0.00 USD | `+50.40%` | `18.95` |
| `Live` | `Short` | `146.35` | 40,260,000.00 USD | 7,330.00 USD | 0.00 USD | `+50.50%` | `50.10` |
| `Live` | `Short` | `146.45` | 40,700,000.00 USD | 439,350.00 USD | 0.00 USD | `+50.61%` | `3,000.00` |
| `Live` | `Short` | `146.55` | 40,710,000.00 USD | 1,280.00 USD | 0.00 USD | `+50.71%` | `8.75` |
| `Live` | `Short` | `146.65` | 41,290,000.00 USD | 587,730.00 USD | 0.00 USD | `+50.81%` | `4,007.68` |
| `Live` | `Short` | `146.85` | 41,300,000.00 USD | 2,120.00 USD | 0.00 USD | `+51.02%` | `14.41` |
| `Live` | `Short` | `146.95` | 41,300,000.00 USD | 3,070.00 USD | 0.00 USD | `+51.12%` | `20.88` |
| `Live` | `Short` | `147.05` | 41,300,000.00 USD | 1,570.00 USD | 0.00 USD | `+51.22%` | `10.70` |
| `Live` | `Short` | `147.15` | 41,300,000.00 USD | 1,730.00 USD | 0.00 USD | `+51.33%` | `11.75` |
| `Live` | `Short` | `147.35` | 41,300,000.00 USD | 169.45 USD | 0.00 USD | `+51.53%` | `1.15` |
| `Live` | `Short` | `147.45` | 41,300,000.00 USD | 204.96 USD | 0.00 USD | `+51.64%` | `1.39` |
| `Live` | `Short` | `147.55` | 41,300,000.00 USD | 1,000.00 USD | 0.00 USD | `+51.74%` | `6.78` |
| `Live` | `Short` | `147.65` | 41,300,000.00 USD | 237.72 USD | 0.00 USD | `+51.84%` | `1.61` |
| `Live` | `Short` | `147.85` | 41,300,000.00 USD | 300.14 USD | 0.00 USD | `+52.05%` | `2.03` |
| `Live` | `Short` | `147.95` | 41,380,000.00 USD | 78,960.00 USD | 0.00 USD | `+52.15%` | `533.72` |
| `Live` | `Short` | `148.15` | 41,900,000.00 USD | 518,630.00 USD | 0.00 USD | `+52.35%` | `3,500.69` |
| `Live` | `Short` | `148.45` | 41,900,000.00 USD | 163.29 USD | 0.00 USD | `+52.66%` | `1.10` |
| `Live` | `Short` | `148.55` | 42,250,000.00 USD | 350,430.00 USD | 0.00 USD | `+52.77%` | `2,359.00` |
| `Live` | `Short` | `148.65` | 42,250,000.00 USD | 1,110.00 USD | 0.00 USD | `+52.87%` | `7.50` |
| `Live` | `Short` | `148.75` | 42,260,000.00 USD | 2,390.00 USD | 0.00 USD | `+52.97%` | `16.06` |
| `Live` | `Short` | `148.85` | 42,350,000.00 USD | 91,370.00 USD | 0.00 USD | `+53.07%` | `613.85` |
| `Live` | `Short` | `148.95` | 42,350,000.00 USD | 527.28 USD | 0.00 USD | `+53.18%` | `3.54` |
| `Live` | `Short` | `149.05` | 42,510,000.00 USD | 160,350.00 USD | 0.00 USD | `+53.28%` | `1,075.79` |
| `Live` | `Short` | `149.15` | 42,510,000.00 USD | 1,120.00 USD | 0.00 USD | `+53.38%` | `7.50` |
| `Live` | `Short` | `149.25` | 43,890,000.00 USD | 1,390,000.00 USD | 0.00 USD | `+53.49%` | `9,282.33` |
| `Live` | `Short` | `149.45` | 43,910,000.00 USD | 16,290.00 USD | 0.00 USD | `+53.69%` | `109.00` |
| `Live` | `Short` | `149.55` | 43,910,000.00 USD | 116.65 USD | 0.00 USD | `+53.79%` | `0.78` |
| `Live` | `Short` | `149.65` | 43,930,000.00 USD | 16,030.00 USD | 0.00 USD | `+53.90%` | `107.15` |
| `Live` | `Short` | `149.95` | 43,930,000.00 USD | 178.44 USD | 0.00 USD | `+54.21%` | `1.19` |
| `Live` | `Short` | `150.05` | 43,930,000.00 USD | 2,930.00 USD | 0.00 USD | `+54.31%` | `19.54` |
| `Live` | `Short` | `150.25` | 44,050,000.00 USD | 123,390.00 USD | 0.00 USD | `+54.51%` | `821.21` |
| `Live` | `Short` | `150.75` | 44,050,000.00 USD | 346.72 USD | 0.00 USD | `+55.03%` | `2.30` |
| `Live` | `Short` | `150.85` | 44,070,000.00 USD | 19,690.00 USD | 0.00 USD | `+55.13%` | `130.55` |
| `Live` | `Short` | `151.15` | 44,080,000.00 USD | 5,960.00 USD | 0.00 USD | `+55.44%` | `39.42` |
| `Live` | `Short` | `151.35` | 45,820,000.00 USD | 1,740,000.00 USD | 0.00 USD | `+55.65%` | `11,488.27` |
| `Live` | `Short` | `151.45` | 45,830,000.00 USD | 8,830.00 USD | 0.00 USD | `+55.75%` | `58.32` |
| `Live` | `Short` | `151.65` | 45,860,000.00 USD | 29,420.00 USD | 0.00 USD | `+55.95%` | `194.00` |
| `Live` | `Short` | `151.95` | 46,960,000.00 USD | 1,110,000.00 USD | 0.00 USD | `+56.26%` | `7,284.27` |
| `Live` | `Short` | `152.25` | 47,010,000.00 USD | 44,800.00 USD | 0.00 USD | `+56.57%` | `294.23` |
| `Live` | `Short` | `152.35` | 47,290,000.00 USD | 286,550.00 USD | 0.00 USD | `+56.67%` | `1,880.87` |
| `Live` | `Short` | `152.45` | 47,300,000.00 USD | 3,150.00 USD | 0.00 USD | `+56.78%` | `20.65` |
| `Live` | `Short` | `152.55` | 47,720,000.00 USD | 423,220.00 USD | 0.00 USD | `+56.88%` | `2,774.28` |
| `Live` | `Short` | `152.75` | 47,720,000.00 USD | 1,570.00 USD | 0.00 USD | `+57.09%` | `10.30` |
| `Live` | `Short` | `153.05` | 47,770,000.00 USD | 44,580.00 USD | 0.00 USD | `+57.39%` | `291.26` |
| `Live` | `Short` | `153.15` | 47,770,000.00 USD | 1,060.00 USD | 0.00 USD | `+57.50%` | `6.95` |
| `Live` | `Short` | `153.35` | 47,770,000.00 USD | 2,300.00 USD | 0.00 USD | `+57.70%` | `15.00` |
| `Live` | `Short` | `153.55` | 47,770,000.00 USD | 1,490.00 USD | 0.00 USD | `+57.91%` | `9.68` |
| `Live` | `Short` | `153.65` | 47,780,000.00 USD | 8,340.00 USD | 0.00 USD | `+58.01%` | `54.29` |
| `Live` | `Short` | `153.95` | 48,550,000.00 USD | 766,050.00 USD | 0.00 USD | `+58.32%` | `4,975.95` |
| `Live` | `Short` | `154.05` | 48,550,000.00 USD | 223.37 USD | 0.00 USD | `+58.42%` | `1.45` |
| `Live` | `Short` | `154.15` | 48,550,000.00 USD | 1,230.00 USD | 0.00 USD | `+58.53%` | `7.95` |
| `Live` | `Short` | `154.25` | 48,550,000.00 USD | 2,340.00 USD | 0.00 USD | `+58.63%` | `15.20` |
| `Live` | `Short` | `154.45` | 48,550,000.00 USD | 4,240.00 USD | 0.00 USD | `+58.83%` | `27.45` |
| `Live` | `Short` | `154.55` | 48,550,000.00 USD | 363.19 USD | 0.00 USD | `+58.94%` | `2.35` |
| `Live` | `Short` | `154.65` | 53,240,000.00 USD | 4,690,000.00 USD | 0.00 USD | `+59.04%` | `30,313.50` |
| `Live` | `Short` | `155.35` | 53,240,000.00 USD | 118.07 USD | 0.00 USD | `+59.76%` | `0.76` |
| `Live` | `Short` | `155.55` | 53,240,000.00 USD | 267.55 USD | 0.00 USD | `+59.97%` | `1.72` |
| `Live` | `Short` | `156.05` | 53,250,000.00 USD | 7,800.00 USD | 0.00 USD | `+60.48%` | `50.00` |
| `Live` | `Short` | `156.35` | 53,250,000.00 USD | 197.00 USD | 0.00 USD | `+60.79%` | `1.26` |
| `Live` | `Short` | `156.45` | 53,550,000.00 USD | 303,040.00 USD | 0.00 USD | `+60.89%` | `1,936.99` |
| `Live` | `Short` | `156.75` | 53,550,000.00 USD | 327.61 USD | 0.00 USD | `+61.20%` | `2.09` |
| `Live` | `Short` | `156.85` | 53,570,000.00 USD | 18,370.00 USD | 0.00 USD | `+61.30%` | `117.09` |
| `Live` | `Short` | `157.15` | 53,620,000.00 USD | 49,270.00 USD | 0.00 USD | `+61.61%` | `313.50` |
| `Live` | `Short` | `157.55` | 53,860,000.00 USD | 236,620.00 USD | 0.00 USD | `+62.02%` | `1,501.89` |
| `Live` | `Short` | `157.65` | 53,860,000.00 USD | 654.25 USD | 0.00 USD | `+62.12%` | `4.15` |
| `Live` | `Short` | `157.75` | 53,950,000.00 USD | 92,600.00 USD | 0.00 USD | `+62.23%` | `587.00` |
| `Live` | `Short` | `158.05` | 53,950,000.00 USD | 312.94 USD | 0.00 USD | `+62.54%` | `1.98` |
| `Live` | `Short` | `158.25` | 54,480,000.00 USD | 528,060.00 USD | 0.00 USD | `+62.74%` | `3,336.89` |
| `Live` | `Short` | `158.55` | 54,480,000.00 USD | 1,410.00 USD | 0.00 USD | `+63.05%` | `8.89` |
| `Live` | `Short` | `158.95` | 54,510,000.00 USD | 27,860.00 USD | 0.00 USD | `+63.46%` | `175.30` |
| `Live` | `Short` | `159.05` | 54,550,000.00 USD | 45,350.00 USD | 0.00 USD | `+63.56%` | `285.11` |
| `Live` | `Short` | `159.45` | 54,640,000.00 USD | 80,530.00 USD | 0.00 USD | `+63.98%` | `505.07` |
| `Live` | `Short` | `159.65` | 54,640,000.00 USD | 1,760.00 USD | 0.00 USD | `+64.18%` | `11.01` |
| `Live` | `Short` | `159.85` | 54,640,000.00 USD | 497.13 USD | 0.00 USD | `+64.39%` | `3.11` |
| `Live` | `Short` | `160.15` | 55,320,000.00 USD | 683,000.00 USD | 0.00 USD | `+64.70%` | `4,264.75` |
| `Live` | `Short` | `160.35` | 55,320,000.00 USD | 655.83 USD | 0.00 USD | `+64.90%` | `4.09` |
| `Live` | `Short` | `160.65` | 55,640,000.00 USD | 321,300.00 USD | 0.00 USD | `+65.21%` | `2,000.00` |
| `Live` | `Short` | `160.95` | 55,780,000.00 USD | 141,540.00 USD | 0.00 USD | `+65.52%` | `879.39` |
| `Live` | `Short` | `161.05` | 55,790,000.00 USD | 2,240.00 USD | 0.00 USD | `+65.62%` | `13.93` |
| `Live` | `Short` | `161.15` | 55,870,000.00 USD | 85,850.00 USD | 0.00 USD | `+65.72%` | `532.74` |
| `Live` | `Short` | `161.35` | 61,550,000.00 USD | 5,680,000.00 USD | 0.00 USD | `+65.93%` | `35,179.78` |
| `Live` | `Short` | `161.55` | 61,550,000.00 USD | 410.34 USD | 0.00 USD | `+66.14%` | `2.54` |
| `Live` | `Short` | `161.95` | 61,690,000.00 USD | 144,610.00 USD | 0.00 USD | `+66.55%` | `892.95` |
| `Live` | `Short` | `162.05` | 61,810,000.00 USD | 113,440.00 USD | 0.00 USD | `+66.65%` | `700.00` |
| `Live` | `Short` | `162.65` | 61,910,000.00 USD | 107,780.00 USD | 0.00 USD | `+67.27%` | `662.62` |
| `Live` | `Short` | `162.95` | 61,920,000.00 USD | 1,350.00 USD | 0.00 USD | `+67.58%` | `8.29` |
| `Live` | `Short` | `163.05` | 61,930,000.00 USD | 16,310.00 USD | 0.00 USD | `+67.68%` | `100.00` |
| `Live` | `Short` | `163.35` | 61,930,000.00 USD | 1,060.00 USD | 0.00 USD | `+67.99%` | `6.49` |
| `Live` | `Short` | `163.65` | 61,940,000.00 USD | 3,080.00 USD | 0.00 USD | `+68.29%` | `18.80` |
| `Live` | `Short` | `163.85` | 61,940,000.00 USD | 786.48 USD | 0.00 USD | `+68.50%` | `4.80` |
| `Live` | `Short` | `163.95` | 62,140,000.00 USD | 206,830.00 USD | 0.00 USD | `+68.60%` | `1,261.56` |
| `Live` | `Short` | `164.25` | 62,140,000.00 USD | 614.30 USD | 0.00 USD | `+68.91%` | `3.74` |
| `Live` | `Short` | `164.95` | 62,160,000.00 USD | 17,050.00 USD | 0.00 USD | `+69.63%` | `103.36` |
| `Live` | `Short` | `165.15` | 62,160,000.00 USD | 198.18 USD | 0.00 USD | `+69.84%` | `1.20` |
| `Live` | `Short` | `166.05` | 62,160,000.00 USD | 830.25 USD | 0.00 USD | `+70.76%` | `5.00` |
| `Live` | `Short` | `166.15` | 62,170,000.00 USD | 7,650.00 USD | 0.00 USD | `+70.87%` | `46.03` |
| `Live` | `Short` | `166.25` | 62,180,000.00 USD | 14,070.00 USD | 0.00 USD | `+70.97%` | `84.61` |
| `Live` | `Short` | `166.65` | 62,250,000.00 USD | 67,790.00 USD | 0.00 USD | `+71.38%` | `406.80` |
| `Live` | `Short` | `166.75` | 62,260,000.00 USD | 3,440.00 USD | 0.00 USD | `+71.48%` | `20.63` |
| `Live` | `Short` | `167.25` | 62,260,000.00 USD | 274.29 USD | 0.00 USD | `+72.00%` | `1.64` |
| `Live` | `Short` | `167.65` | 62,260,000.00 USD | 115.68 USD | 0.00 USD | `+72.41%` | `0.69` |
| `Live` | `Short` | `167.75` | 62,260,000.00 USD | 1,890.00 USD | 0.00 USD | `+72.51%` | `11.27` |
| `Live` | `Short` | `168.05` | 62,260,000.00 USD | 273.92 USD | 0.00 USD | `+72.82%` | `1.63` |
| `Live` | `Short` | `168.35` | 62,280,000.00 USD | 19,740.00 USD | 0.00 USD | `+73.13%` | `117.24` |
| `Live` | `Short` | `168.65` | 62,600,000.00 USD | 325,850.00 USD | 0.00 USD | `+73.44%` | `1,932.10` |
| `Live` | `Short` | `169.25` | 62,610,000.00 USD | 3,270.00 USD | 0.00 USD | `+74.05%` | `19.33` |
| `Live` | `Short` | `169.85` | 62,790,000.00 USD | 180,350.00 USD | 0.00 USD | `+74.67%` | `1,061.79` |
| `Live` | `Short` | `171.45` | 62,790,000.00 USD | 111.44 USD | 0.00 USD | `+76.32%` | `0.65` |
| `Live` | `Short` | `171.55` | 62,810,000.00 USD | 20,420.00 USD | 0.00 USD | `+76.42%` | `119.02` |
| `Live` | `Short` | `172.45` | 62,890,000.00 USD | 79,660.00 USD | 0.00 USD | `+77.34%` | `461.92` |
| `Live` | `Short` | `172.85` | 63,090,000.00 USD | 200,310.00 USD | 0.00 USD | `+77.76%` | `1,158.88` |
| `Live` | `Short` | `173.05` | 63,090,000.00 USD | 204.20 USD | 0.00 USD | `+77.96%` | `1.18` |
| `Live` | `Short` | `173.25` | 63,090,000.00 USD | 1,190.00 USD | 0.00 USD | `+78.17%` | `6.88` |
| `Live` | `Short` | `173.45` | 63,140,000.00 USD | 52,230.00 USD | 0.00 USD | `+78.37%` | `301.13` |
| `Live` | `Short` | `173.85` | 63,140,000.00 USD | 695.40 USD | 0.00 USD | `+78.78%` | `4.00` |
| `Live` | `Short` | `174.15` | 63,250,000.00 USD | 104,490.00 USD | 0.00 USD | `+79.09%` | `600.00` |
| `Live` | `Short` | `174.25` | 63,490,000.00 USD | 245,010.00 USD | 0.00 USD | `+79.20%` | `1,406.07` |
| `Live` | `Short` | `174.35` | 63,700,000.00 USD | 205,490.00 USD | 0.00 USD | `+79.30%` | `1,178.60` |
| `Live` | `Short` | `174.75` | 63,700,000.00 USD | 146.79 USD | 0.00 USD | `+79.71%` | `0.84` |
| `Live` | `Short` | `175.05` | 102,210,000.00 USD | 38,510,000.00 USD | 0.00 USD | `+80.02%` | `220,000.19` |
| `Live` | `Short` | `175.45` | 102,210,000.00 USD | 119.31 USD | 0.00 USD | `+80.43%` | `0.68` |
| `Live` | `Short` | `175.55` | 102,310,000.00 USD | 105,720.00 USD | 0.00 USD | `+80.53%` | `602.22` |
| `Live` | `Short` | `175.75` | 102,330,000.00 USD | 20,140.00 USD | 0.00 USD | `+80.74%` | `114.57` |
| `Live` | `Short` | `175.85` | 102,340,000.00 USD | 1,300.00 USD | 0.00 USD | `+80.84%` | `7.37` |
| `Live` | `Short` | `176.05` | 105,860,000.00 USD | 3,520,000.00 USD | 0.00 USD | `+81.05%` | `20,000.00` |
| `Live` | `Short` | `176.25` | 105,860,000.00 USD | 625.69 USD | 0.00 USD | `+81.25%` | `3.55` |
| `Live` | `Short` | `176.45` | 105,860,000.00 USD | 3,650.00 USD | 0.00 USD | `+81.46%` | `20.70` |
| `Live` | `Short` | `176.65` | 105,890,000.00 USD | 26,250.00 USD | 0.00 USD | `+81.66%` | `148.60` |
| `Live` | `Short` | `176.85` | 105,890,000.00 USD | 2,800.00 USD | 0.00 USD | `+81.87%` | `15.84` |
| `Live` | `Short` | `177.35` | 105,890,000.00 USD | 4,430.00 USD | 0.00 USD | `+82.38%` | `25.00` |
| `Live` | `Short` | `177.65` | 106,040,000.00 USD | 142,760.00 USD | 0.00 USD | `+82.69%` | `803.59` |
| `Live` | `Short` | `177.95` | 107,410,000.00 USD | 1,380,000.00 USD | 0.00 USD | `+83.00%` | `7,740.00` |
| `Live` | `Short` | `178.15` | 107,460,000.00 USD | 46,610.00 USD | 0.00 USD | `+83.21%` | `261.63` |
| `Live` | `Short` | `178.55` | 107,470,000.00 USD | 4,950.00 USD | 0.00 USD | `+83.62%` | `27.73` |
| `Live` | `Short` | `179.35` | 110,430,000.00 USD | 2,960,000.00 USD | 0.00 USD | `+84.44%` | `16,513.36` |
| `Live` | `Short` | `179.75` | 110,430,000.00 USD | 154.59 USD | 0.00 USD | `+84.85%` | `0.86` |
| `Live` | `Short` | `180.05` | 110,540,000.00 USD | 116,670.00 USD | 0.00 USD | `+85.16%` | `648.01` |
| `Live` | `Short` | `180.45` | 110,540,000.00 USD | 245.41 USD | 0.00 USD | `+85.57%` | `1.36` |
| `Live` | `Short` | `180.55` | 110,580,000.00 USD | 38,150.00 USD | 0.00 USD | `+85.67%` | `211.32` |
| `Live` | `Short` | `180.75` | 110,580,000.00 USD | 146.41 USD | 0.00 USD | `+85.88%` | `0.81` |
| `Live` | `Short` | `180.95` | 110,590,000.00 USD | 10,720.00 USD | 0.00 USD | `+86.09%` | `59.24` |
| `Live` | `Short` | `181.25` | 110,610,000.00 USD | 18,120.00 USD | 0.00 USD | `+86.39%` | `100.00` |
| `Live` | `Short` | `181.55` | 110,610,000.00 USD | 254.17 USD | 0.00 USD | `+86.70%` | `1.40` |
| `Live` | `Short` | `181.95` | 114,250,000.00 USD | 3,640,000.00 USD | 0.00 USD | `+87.11%` | `20,000.00` |
| `Live` | `Short` | `182.15` | 114,250,000.00 USD | 3,990.00 USD | 0.00 USD | `+87.32%` | `21.93` |
| `Live` | `Short` | `182.95` | 114,260,000.00 USD | 788.51 USD | 0.00 USD | `+88.14%` | `4.31` |
| `Live` | `Short` | `183.55` | 114,330,000.00 USD | 73,420.00 USD | 0.00 USD | `+88.76%` | `400.00` |
| `Live` | `Short` | `184.25` | 114,330,000.00 USD | 1,680.00 USD | 0.00 USD | `+89.48%` | `9.12` |
| `Live` | `Short` | `184.75` | 114,340,000.00 USD | 7,650.00 USD | 0.00 USD | `+89.99%` | `41.43` |
| `Live` | `Short` | `184.95` | 114,500,000.00 USD | 165,230.00 USD | 0.00 USD | `+90.20%` | `893.35` |
| `Live` | `Short` | `185.05` | 114,560,000.00 USD | 53,160.00 USD | 0.00 USD | `+90.30%` | `287.30` |
| `Live` | `Short` | `185.25` | 114,560,000.00 USD | 737.29 USD | 0.00 USD | `+90.51%` | `3.98` |
| `Live` | `Short` | `185.35` | 114,570,000.00 USD | 10,940.00 USD | 0.00 USD | `+90.61%` | `59.00` |
| `Live` | `Short` | `185.45` | 114,570,000.00 USD | 2,770.00 USD | 0.00 USD | `+90.71%` | `14.94` |
| `Live` | `Short` | `185.55` | 114,570,000.00 USD | 1,220.00 USD | 0.00 USD | `+90.82%` | `6.56` |
| `Live` | `Short` | `185.65` | 114,570,000.00 USD | 137.38 USD | 0.00 USD | `+90.92%` | `0.74` |
| `Live` | `Short` | `185.75` | 114,570,000.00 USD | 390.07 USD | 0.00 USD | `+91.02%` | `2.10` |
| `Live` | `Short` | `186.15` | 114,570,000.00 USD | 247.58 USD | 0.00 USD | `+91.43%` | `1.33` |
| `Live` | `Short` | `186.85` | 114,580,000.00 USD | 2,190.00 USD | 0.00 USD | `+92.15%` | `11.72` |
| `Live` | `Short` | `186.95` | 114,580,000.00 USD | 4,110.00 USD | 0.00 USD | `+92.26%` | `22.01` |
| `Live` | `Short` | `187.45` | 114,580,000.00 USD | 232.44 USD | 0.00 USD | `+92.77%` | `1.24` |
| `Live` | `Short` | `187.75` | 114,580,000.00 USD | 2,820.00 USD | 0.00 USD | `+93.08%` | `15.00` |
| `Live` | `Short` | `187.85` | 114,580,000.00 USD | 1,560.00 USD | 0.00 USD | `+93.18%` | `8.32` |
| `Live` | `Short` | `188.55` | 114,590,000.00 USD | 1,020.00 USD | 0.00 USD | `+93.90%` | `5.41` |
| `Live` | `Short` | `188.65` | 114,610,000.00 USD | 29,340.00 USD | 0.00 USD | `+94.00%` | `155.55` |
| `Live` | `Short` | `188.75` | 114,620,000.00 USD | 2,470.00 USD | 0.00 USD | `+94.11%` | `13.11` |
| `Live` | `Short` | `188.95` | 114,620,000.00 USD | 1,450.00 USD | 0.00 USD | `+94.31%` | `7.69` |
| `Live` | `Short` | `189.25` | 114,620,000.00 USD | 456.09 USD | 0.00 USD | `+94.62%` | `2.41` |
| `Live` | `Short` | `189.85` | 114,620,000.00 USD | 189.85 USD | 0.00 USD | `+95.24%` | `1.00` |
| `Live` | `Short` | `189.95` | 114,900,000.00 USD | 284,930.00 USD | 0.00 USD | `+95.34%` | `1,500.00` |
| `Live` | `Short` | `190.05` | 114,910,000.00 USD | 1,010.00 USD | 0.00 USD | `+95.44%` | `5.30` |
| `Live` | `Short` | `190.15` | 114,910,000.00 USD | 148.32 USD | 0.00 USD | `+95.55%` | `0.78` |
| `Live` | `Short` | `190.45` | 114,910,000.00 USD | 236.16 USD | 0.00 USD | `+95.86%` | `1.24` |
| `Live` | `Short` | `190.85` | 114,910,000.00 USD | 5,410.00 USD | 0.00 USD | `+96.27%` | `28.34` |
| `Live` | `Short` | `190.95` | 128,860,000.00 USD | 13,950,000.00 USD | 0.00 USD | `+96.37%` | `73,044.42` |
| `Live` | `Short` | `191.25` | 128,920,000.00 USD | 62,750.00 USD | 0.00 USD | `+96.68%` | `328.11` |
| `Live` | `Short` | `191.95` | 128,920,000.00 USD | 322.48 USD | 0.00 USD | `+97.40%` | `1.68` |
| `Live` | `Short` | `192.35` | 128,920,000.00 USD | 192.35 USD | 0.00 USD | `+97.81%` | `1.00` |
| `Live` | `Short` | `192.95` | 128,930,000.00 USD | 9,320.00 USD | 0.00 USD | `+98.43%` | `48.28` |
| `Live` | `Short` | `193.25` | 128,930,000.00 USD | 1,380.00 USD | 0.00 USD | `+98.74%` | `7.13` |
| `Live` | `Short` | `193.55` | 129,050,000.00 USD | 114,580.00 USD | 0.00 USD | `+99.04%` | `592.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `23.05` | 11,470,000.00 USD | 0.00 USD | 13,940.00 USD | `-76.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `30.35` | 11,460,000.00 USD | 0.00 USD | 499.56 USD | `-68.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `32.05` | 11,460,000.00 USD | 0.00 USD | 1,230.00 USD | `-67.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `33.05` | 11,460,000.00 USD | 0.00 USD | 818.32 USD | `-66.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `34.85` | 11,460,000.00 USD | 0.00 USD | 1,340.00 USD | `-64.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `36.05` | 11,460,000.00 USD | 0.00 USD | 2,160.00 USD | `-62.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `36.45` | 11,450,000.00 USD | 0.00 USD | 434.85 USD | `-62.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `38.05` | 11,450,000.00 USD | 0.00 USD | 267.87 USD | `-60.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.05` | 11,450,000.00 USD | 0.00 USD | 208.14 USD | `-59.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.55` | 11,450,000.00 USD | 0.00 USD | 3,460.00 USD | `-59.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.75` | 11,450,000.00 USD | 0.00 USD | 157.01 USD | `-59.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.05` | 11,450,000.00 USD | 0.00 USD | 1,050.00 USD | `-58.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `41.75` | 11,450,000.00 USD | 0.00 USD | 120.66 USD | `-57.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.15` | 11,450,000.00 USD | 0.00 USD | 121.81 USD | `-56.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.55` | 11,450,000.00 USD | 0.00 USD | 170,530.00 USD | `-56.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.75` | 11,280,000.00 USD | 0.00 USD | 105.00 USD | `-55.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.05` | 11,280,000.00 USD | 0.00 USD | 59,730.00 USD | `-53.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.75` | 11,220,000.00 USD | 0.00 USD | 251.05 USD | `-51.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.75` | 11,220,000.00 USD | 0.00 USD | 143.25 USD | `-50.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.85` | 11,220,000.00 USD | 0.00 USD | 191.40 USD | `-50.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.05` | 11,220,000.00 USD | 0.00 USD | 50,240.00 USD | `-50.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.55` | 11,170,000.00 USD | 0.00 USD | 664.65 USD | `-50.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.75` | 11,170,000.00 USD | 0.00 USD | 103.35 USD | `-49.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.05` | 11,170,000.00 USD | 0.00 USD | 4,660.00 USD | `-48.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.25` | 11,160,000.00 USD | 0.00 USD | 107.03 USD | `-48.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.55` | 11,160,000.00 USD | 0.00 USD | 102.62 USD | `-48.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.25` | 11,160,000.00 USD | 0.00 USD | 134.28 USD | `-47.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.65` | 11,160,000.00 USD | 0.00 USD | 3,950.00 USD | `-46.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.15` | 11,160,000.00 USD | 0.00 USD | 102.74 USD | `-46.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.55` | 11,160,000.00 USD | 0.00 USD | 126.12 USD | `-45.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.95` | 11,160,000.00 USD | 0.00 USD | 200.15 USD | `-45.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.15` | 11,160,000.00 USD | 0.00 USD | 24,450.00 USD | `-45.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.45` | 11,130,000.00 USD | 0.00 USD | 1,660.00 USD | `-45.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.05` | 11,130,000.00 USD | 0.00 USD | 641.57 USD | `-44.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.85` | 11,130,000.00 USD | 0.00 USD | 139.87 USD | `-43.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.05` | 11,130,000.00 USD | 0.00 USD | 209.19 USD | `-43.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.05` | 11,130,000.00 USD | 0.00 USD | 894.56 USD | `-42.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.15` | 11,130,000.00 USD | 0.00 USD | 4,930.00 USD | `-42.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.05` | 11,120,000.00 USD | 0.00 USD | 6,960.00 USD | `-41.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.35` | 11,120,000.00 USD | 0.00 USD | 265.53 USD | `-41.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `58.05` | 11,120,000.00 USD | 0.00 USD | 158.48 USD | `-40.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `58.15` | 11,120,000.00 USD | 0.00 USD | 3,820.00 USD | `-40.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `58.25` | 11,110,000.00 USD | 0.00 USD | 428.72 USD | `-40.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.05` | 11,110,000.00 USD | 0.00 USD | 295.25 USD | `-39.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.35` | 11,110,000.00 USD | 0.00 USD | 200.01 USD | `-38.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.55` | 11,110,000.00 USD | 0.00 USD | 1,460.00 USD | `-38.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.95` | 11,110,000.00 USD | 0.00 USD | 9,040.00 USD | `-38.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.05` | 11,100,000.00 USD | 0.00 USD | 35,050.00 USD | `-38.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.15` | 11,070,000.00 USD | 0.00 USD | 2,820.00 USD | `-38.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.25` | 11,060,000.00 USD | 0.00 USD | 488.63 USD | `-38.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.35` | 11,060,000.00 USD | 0.00 USD | 258.90 USD | `-37.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.45` | 11,060,000.00 USD | 0.00 USD | 206.13 USD | `-37.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.55` | 11,060,000.00 USD | 0.00 USD | 724.78 USD | `-37.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.05` | 11,060,000.00 USD | 0.00 USD | 14,350.00 USD | `-37.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.35` | 11,050,000.00 USD | 0.00 USD | 142.33 USD | `-36.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.45` | 11,050,000.00 USD | 0.00 USD | 100.78 USD | `-36.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.55` | 11,050,000.00 USD | 0.00 USD | 243.74 USD | `-36.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `62.05` | 11,050,000.00 USD | 0.00 USD | 6,720.00 USD | `-36.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `62.55` | 11,040,000.00 USD | 0.00 USD | 136.98 USD | `-35.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `63.05` | 11,040,000.00 USD | 0.00 USD | 9,990.00 USD | `-35.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `63.55` | 11,030,000.00 USD | 0.00 USD | 2,980.00 USD | `-34.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `63.95` | 11,030,000.00 USD | 0.00 USD | 222.55 USD | `-34.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `64.25` | 11,030,000.00 USD | 0.00 USD | 163.19 USD | `-33.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `64.85` | 11,030,000.00 USD | 0.00 USD | 129.70 USD | `-33.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `65.05` | 11,030,000.00 USD | 0.00 USD | 2,440.00 USD | `-33.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `65.15` | 11,020,000.00 USD | 0.00 USD | 2,190.00 USD | `-33.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `65.55` | 11,020,000.00 USD | 0.00 USD | 2,200.00 USD | `-32.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `66.05` | 11,020,000.00 USD | 0.00 USD | 9,140.00 USD | `-32.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `66.55` | 11,010,000.00 USD | 0.00 USD | 541.72 USD | `-31.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `67.05` | 11,010,000.00 USD | 0.00 USD | 335.25 USD | `-31.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `67.15` | 11,010,000.00 USD | 0.00 USD | 268.60 USD | `-30.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.05` | 11,010,000.00 USD | 0.00 USD | 195.30 USD | `-30.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.45` | 11,010,000.00 USD | 0.00 USD | 7,600.00 USD | `-29.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.55` | 11,000,000.00 USD | 0.00 USD | 5,610.00 USD | `-29.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.65` | 11,000,000.00 USD | 0.00 USD | 359.04 USD | `-29.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.75` | 11,000,000.00 USD | 0.00 USD | 1,200.00 USD | `-29.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.05` | 10,990,000.00 USD | 0.00 USD | 11,360.00 USD | `-28.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.15` | 10,980,000.00 USD | 0.00 USD | 172.18 USD | `-28.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.25` | 10,980,000.00 USD | 0.00 USD | 668.96 USD | `-28.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.65` | 10,980,000.00 USD | 0.00 USD | 107.96 USD | `-28.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.75` | 10,980,000.00 USD | 0.00 USD | 42,360.00 USD | `-28.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.85` | 10,940,000.00 USD | 0.00 USD | 365.32 USD | `-28.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.95` | 10,940,000.00 USD | 0.00 USD | 1,510.00 USD | `-28.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.05` | 10,940,000.00 USD | 0.00 USD | 43,920.00 USD | `-27.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.25` | 10,890,000.00 USD | 0.00 USD | 5,270.00 USD | `-27.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.35` | 10,890,000.00 USD | 0.00 USD | 562.80 USD | `-27.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.55` | 10,890,000.00 USD | 0.00 USD | 681.51 USD | `-27.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.65` | 10,890,000.00 USD | 0.00 USD | 4,920.00 USD | `-27.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.75` | 10,880,000.00 USD | 0.00 USD | 2,790.00 USD | `-27.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.05` | 10,880,000.00 USD | 0.00 USD | 265.02 USD | `-26.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.35` | 10,880,000.00 USD | 0.00 USD | 32,440.00 USD | `-26.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.45` | 10,850,000.00 USD | 0.00 USD | 289.37 USD | `-26.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.55` | 10,850,000.00 USD | 0.00 USD | 1,170.00 USD | `-26.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.65` | 10,850,000.00 USD | 0.00 USD | 1,930.00 USD | `-26.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.75` | 10,840,000.00 USD | 0.00 USD | 235.34 USD | `-26.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.05` | 10,840,000.00 USD | 0.00 USD | 2,300.00 USD | `-25.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.55` | 10,840,000.00 USD | 0.00 USD | 19,560.00 USD | `-25.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.65` | 10,820,000.00 USD | 0.00 USD | 14,530.00 USD | `-25.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.95` | 10,810,000.00 USD | 0.00 USD | 66,160.00 USD | `-24.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `73.05` | 10,740,000.00 USD | 0.00 USD | 7,970.00 USD | `-24.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `73.35` | 10,730,000.00 USD | 0.00 USD | 733.50 USD | `-24.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `73.45` | 10,730,000.00 USD | 0.00 USD | 139.56 USD | `-24.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.05` | 10,730,000.00 USD | 0.00 USD | 510.95 USD | `-23.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.25` | 10,730,000.00 USD | 0.00 USD | 414.31 USD | `-23.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.35` | 10,730,000.00 USD | 0.00 USD | 1,660.00 USD | `-23.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.45` | 10,730,000.00 USD | 0.00 USD | 10,730.00 USD | `-23.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.55` | 10,720,000.00 USD | 0.00 USD | 1,820.00 USD | `-23.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.75` | 10,720,000.00 USD | 0.00 USD | 28,050.00 USD | `-23.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.05` | 10,690,000.00 USD | 0.00 USD | 30,040.00 USD | `-22.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.35` | 10,660,000.00 USD | 0.00 USD | 153.71 USD | `-22.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.45` | 10,660,000.00 USD | 0.00 USD | 163.73 USD | `-22.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.75` | 10,660,000.00 USD | 0.00 USD | 2,220.00 USD | `-22.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.95` | 10,660,000.00 USD | 0.00 USD | 277.98 USD | `-21.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.05` | 10,660,000.00 USD | 0.00 USD | 8,680.00 USD | `-21.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.15` | 10,650,000.00 USD | 0.00 USD | 254.34 USD | `-21.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.25` | 10,650,000.00 USD | 0.00 USD | 486.47 USD | `-21.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.35` | 10,650,000.00 USD | 0.00 USD | 358.84 USD | `-21.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.55` | 10,650,000.00 USD | 0.00 USD | 4,340.00 USD | `-21.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.65` | 10,640,000.00 USD | 0.00 USD | 536.55 USD | `-21.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.75` | 10,640,000.00 USD | 0.00 USD | 251.74 USD | `-21.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.05` | 10,640,000.00 USD | 0.00 USD | 2,160.00 USD | `-20.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.35` | 10,640,000.00 USD | 0.00 USD | 5,690.00 USD | `-20.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.45` | 10,630,000.00 USD | 0.00 USD | 1,020.00 USD | `-20.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.95` | 10,630,000.00 USD | 0.00 USD | 155.12 USD | `-19.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.05` | 10,630,000.00 USD | 0.00 USD | 56,850.00 USD | `-19.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.15` | 10,580,000.00 USD | 0.00 USD | 738.52 USD | `-19.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.55` | 10,570,000.00 USD | 0.00 USD | 18,590.00 USD | `-19.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.65` | 10,560,000.00 USD | 0.00 USD | 116.40 USD | `-19.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.75` | 10,560,000.00 USD | 0.00 USD | 379.58 USD | `-19.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.05` | 10,560,000.00 USD | 0.00 USD | 5,300.00 USD | `-18.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.15` | 10,550,000.00 USD | 0.00 USD | 201.04 USD | `-18.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.25` | 10,550,000.00 USD | 0.00 USD | 2,140.00 USD | `-18.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.45` | 10,550,000.00 USD | 0.00 USD | 5,850.00 USD | `-18.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.65` | 10,540,000.00 USD | 0.00 USD | 238.95 USD | `-18.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.75` | 10,540,000.00 USD | 0.00 USD | 1,330.00 USD | `-17.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.85` | 10,540,000.00 USD | 0.00 USD | 289.06 USD | `-17.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.95` | 10,540,000.00 USD | 0.00 USD | 808.29 USD | `-17.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.05` | 10,540,000.00 USD | 0.00 USD | 37,100.00 USD | `-17.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.15` | 10,500,000.00 USD | 0.00 USD | 8,360.00 USD | `-17.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.35` | 10,490,000.00 USD | 0.00 USD | 359.97 USD | `-17.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.45` | 10,490,000.00 USD | 0.00 USD | 8,770.00 USD | `-17.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.55` | 10,480,000.00 USD | 0.00 USD | 1,280.00 USD | `-17.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.65` | 10,480,000.00 USD | 0.00 USD | 1,280.00 USD | `-17.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.75` | 10,480,000.00 USD | 0.00 USD | 22,780.00 USD | `-16.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.85` | 10,460,000.00 USD | 0.00 USD | 341.19 USD | `-16.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.05` | 10,460,000.00 USD | 0.00 USD | 1,620.00 USD | `-16.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.25` | 10,460,000.00 USD | 0.00 USD | 959.56 USD | `-16.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.45` | 10,460,000.00 USD | 0.00 USD | 5,830.00 USD | `-16.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.55` | 10,450,000.00 USD | 0.00 USD | 572.48 USD | `-16.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.65` | 10,450,000.00 USD | 0.00 USD | 806.70 USD | `-16.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.75` | 10,450,000.00 USD | 0.00 USD | 1,390.00 USD | `-15.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.85` | 10,450,000.00 USD | 0.00 USD | 818.50 USD | `-15.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.95` | 10,450,000.00 USD | 0.00 USD | 70,900.00 USD | `-15.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.05` | 10,380,000.00 USD | 0.00 USD | 3,220.00 USD | `-15.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.15` | 10,370,000.00 USD | 0.00 USD | 684.31 USD | `-15.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.25` | 10,370,000.00 USD | 0.00 USD | 486.92 USD | `-15.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.35` | 10,370,000.00 USD | 0.00 USD | 386.22 USD | `-15.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.45` | 10,370,000.00 USD | 0.00 USD | 3,190.00 USD | `-15.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.65` | 10,370,000.00 USD | 0.00 USD | 267,390.00 USD | `-15.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.75` | 10,100,000.00 USD | 0.00 USD | 1,660.00 USD | `-14.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.85` | 10,100,000.00 USD | 0.00 USD | 3,270.00 USD | `-14.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.95` | 10,100,000.00 USD | 0.00 USD | 945.63 USD | `-14.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.05` | 10,090,000.00 USD | 0.00 USD | 310,300.00 USD | `-14.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.15` | 9,780,000.00 USD | 0.00 USD | 239.47 USD | `-14.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.25` | 9,780,000.00 USD | 0.00 USD | 18,330.00 USD | `-14.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.45` | 9,770,000.00 USD | 0.00 USD | 168.57 USD | `-14.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.55` | 9,770,000.00 USD | 0.00 USD | 107,330.00 USD | `-14.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.65` | 9,660,000.00 USD | 0.00 USD | 1,100.00 USD | `-13.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.75` | 9,660,000.00 USD | 0.00 USD | 1,320.00 USD | `-13.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.95` | 9,660,000.00 USD | 0.00 USD | 4,550.00 USD | `-13.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.05` | 9,650,000.00 USD | 0.00 USD | 33,500.00 USD | `-13.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.15` | 9,620,000.00 USD | 0.00 USD | 25,220.00 USD | `-13.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.25` | 9,590,000.00 USD | 0.00 USD | 2,690.00 USD | `-13.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.45` | 9,590,000.00 USD | 0.00 USD | 965.26 USD | `-13.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.55` | 9,590,000.00 USD | 0.00 USD | 651.04 USD | `-13.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.65` | 9,590,000.00 USD | 0.00 USD | 858.35 USD | `-12.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.75` | 9,590,000.00 USD | 0.00 USD | 306.80 USD | `-12.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.95` | 9,590,000.00 USD | 0.00 USD | 137.62 USD | `-12.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.05` | 9,590,000.00 USD | 0.00 USD | 236,040.00 USD | `-12.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.15` | 9,350,000.00 USD | 0.00 USD | 1,290.00 USD | `-12.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.25` | 9,350,000.00 USD | 0.00 USD | 1,320.00 USD | `-12.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.35` | 9,350,000.00 USD | 0.00 USD | 39,110.00 USD | `-12.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.45` | 9,310,000.00 USD | 0.00 USD | 120.48 USD | `-12.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.55` | 9,310,000.00 USD | 0.00 USD | 105.23 USD | `-12.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.65` | 9,310,000.00 USD | 0.00 USD | 310.05 USD | `-11.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.75` | 9,310,000.00 USD | 0.00 USD | 1,410.00 USD | `-11.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.85` | 9,310,000.00 USD | 0.00 USD | 360.57 USD | `-11.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.95` | 9,310,000.00 USD | 0.00 USD | 731.43 USD | `-11.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.05` | 9,310,000.00 USD | 0.00 USD | 13,340.00 USD | `-11.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.15` | 9,290,000.00 USD | 0.00 USD | 2,210.00 USD | `-11.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.25` | 9,290,000.00 USD | 0.00 USD | 163.88 USD | `-11.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.35` | 9,290,000.00 USD | 0.00 USD | 4,080.00 USD | `-11.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.45` | 9,290,000.00 USD | 0.00 USD | 1,550.00 USD | `-11.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.55` | 9,290,000.00 USD | 0.00 USD | 417.17 USD | `-10.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.65` | 9,280,000.00 USD | 0.00 USD | 220,550.00 USD | `-10.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.75` | 9,060,000.00 USD | 0.00 USD | 3,060.00 USD | `-10.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.85` | 9,060,000.00 USD | 0.00 USD | 788.60 USD | `-10.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.95` | 9,060,000.00 USD | 0.00 USD | 132.16 USD | `-10.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.05` | 9,060,000.00 USD | 0.00 USD | 280,590.00 USD | `-10.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.15` | 8,780,000.00 USD | 0.00 USD | 23,550.00 USD | `-10.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.25` | 8,760,000.00 USD | 0.00 USD | 8,200.00 USD | `-10.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.35` | 8,750,000.00 USD | 0.00 USD | 127.53 USD | `-10.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.45` | 8,750,000.00 USD | 0.00 USD | 730.21 USD | `-10.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.55` | 8,750,000.00 USD | 0.00 USD | 7,840.00 USD | `-9.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.65` | 8,740,000.00 USD | 0.00 USD | 2,300.00 USD | `-9.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.85` | 8,740,000.00 USD | 0.00 USD | 131.78 USD | `-9.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.95` | 8,740,000.00 USD | 0.00 USD | 104,230.00 USD | `-9.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.05` | 8,630,000.00 USD | 0.00 USD | 125,980.00 USD | `-9.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.15` | 8,510,000.00 USD | 0.00 USD | 2,470.00 USD | `-9.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.25` | 8,500,000.00 USD | 0.00 USD | 3,070.00 USD | `-9.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.35` | 8,500,000.00 USD | 0.00 USD | 38,020.00 USD | `-9.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.45` | 8,460,000.00 USD | 0.00 USD | 1,100.00 USD | `-9.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.55` | 8,460,000.00 USD | 0.00 USD | 32,280.00 USD | `-8.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.65` | 8,430,000.00 USD | 0.00 USD | 27,220.00 USD | `-8.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.75` | 8,400,000.00 USD | 0.00 USD | 53,390.00 USD | `-8.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.85` | 8,350,000.00 USD | 0.00 USD | 91,430.00 USD | `-8.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.95` | 8,260,000.00 USD | 0.00 USD | 141.43 USD | `-8.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.05` | 8,260,000.00 USD | 0.00 USD | 18,290.00 USD | `-8.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.15` | 8,240,000.00 USD | 0.00 USD | 6,840.00 USD | `-8.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.25` | 8,230,000.00 USD | 0.00 USD | 1,340.00 USD | `-8.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.35` | 8,230,000.00 USD | 0.00 USD | 4,360.00 USD | `-8.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.45` | 8,230,000.00 USD | 0.00 USD | 5,280.00 USD | `-8.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.55` | 8,220,000.00 USD | 0.00 USD | 644.76 USD | `-7.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.65` | 8,220,000.00 USD | 0.00 USD | 297.64 USD | `-7.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.75` | 8,220,000.00 USD | 0.00 USD | 262.97 USD | `-7.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.85` | 8,220,000.00 USD | 0.00 USD | 17,650.00 USD | `-7.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.95` | 8,200,000.00 USD | 0.00 USD | 89,440.00 USD | `-7.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.05` | 8,110,000.00 USD | 0.00 USD | 2,370,000.00 USD | `-7.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.15` | 5,740,000.00 USD | 0.00 USD | 1,250.00 USD | `-7.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.25` | 5,740,000.00 USD | 0.00 USD | 12,170.00 USD | `-7.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.45` | 5,730,000.00 USD | 0.00 USD | 5,010.00 USD | `-6.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.55` | 5,720,000.00 USD | 0.00 USD | 13,500.00 USD | `-6.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.65` | 5,710,000.00 USD | 0.00 USD | 75,820.00 USD | `-6.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.75` | 5,630,000.00 USD | 0.00 USD | 4,980.00 USD | `-6.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.85` | 5,630,000.00 USD | 0.00 USD | 6,580.00 USD | `-6.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.95` | 5,620,000.00 USD | 0.00 USD | 15,580.00 USD | `-6.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.05` | 5,610,000.00 USD | 0.00 USD | 642,030.00 USD | `-6.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.15` | 4,960,000.00 USD | 0.00 USD | 1,240.00 USD | `-6.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.25` | 4,960,000.00 USD | 0.00 USD | 6,310.00 USD | `-6.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.35` | 4,960,000.00 USD | 0.00 USD | 17,720.00 USD | `-6.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.45` | 4,940,000.00 USD | 0.00 USD | 1,800.00 USD | `-5.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.55` | 4,940,000.00 USD | 0.00 USD | 451,280.00 USD | `-5.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.65` | 4,490,000.00 USD | 0.00 USD | 44,430.00 USD | `-5.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.75` | 4,440,000.00 USD | 0.00 USD | 5,710.00 USD | `-5.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.85` | 4,440,000.00 USD | 0.00 USD | 42,300.00 USD | `-5.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.95` | 4,390,000.00 USD | 0.00 USD | 32,120.00 USD | `-5.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.05` | 4,360,000.00 USD | 0.00 USD | 341,040.00 USD | `-5.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.15` | 4,020,000.00 USD | 0.00 USD | 49,960.00 USD | `-5.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.25` | 3,970,000.00 USD | 0.00 USD | 2,170.00 USD | `-5.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.35` | 3,970,000.00 USD | 0.00 USD | 912,240.00 USD | `-5.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.45` | 3,060,000.00 USD | 0.00 USD | 10,200.00 USD | `-4.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.55` | 3,050,000.00 USD | 0.00 USD | 17,280.00 USD | `-4.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.65` | 3,030,000.00 USD | 0.00 USD | 51,600.00 USD | `-4.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.75` | 2,980,000.00 USD | 0.00 USD | 2,020.00 USD | `-4.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.85` | 2,980,000.00 USD | 0.00 USD | 32,500.00 USD | `-4.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.95` | 2,940,000.00 USD | 0.00 USD | 21,710.00 USD | `-4.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.05` | 2,920,000.00 USD | 0.00 USD | 23,030.00 USD | `-4.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.15` | 2,900,000.00 USD | 0.00 USD | 136,280.00 USD | `-4.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.25` | 2,760,000.00 USD | 0.00 USD | 50,820.00 USD | `-4.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.35` | 2,710,000.00 USD | 0.00 USD | 3,350.00 USD | `-4.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.45` | 2,710,000.00 USD | 0.00 USD | 1,830.00 USD | `-3.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.55` | 2,710,000.00 USD | 0.00 USD | 1,510.00 USD | `-3.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.65` | 2,700,000.00 USD | 0.00 USD | 8,670.00 USD | `-3.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.75` | 2,700,000.00 USD | 0.00 USD | 2,340.00 USD | `-3.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.85` | 2,690,000.00 USD | 0.00 USD | 1,570.00 USD | `-3.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.95` | 2,690,000.00 USD | 0.00 USD | 3,800.00 USD | `-3.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.05` | 2,690,000.00 USD | 0.00 USD | 401,480.00 USD | `-3.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.15` | 2,290,000.00 USD | 0.00 USD | 15,780.00 USD | `-3.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.25` | 2,270,000.00 USD | 0.00 USD | 7,420.00 USD | `-3.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.35` | 2,260,000.00 USD | 0.00 USD | 2,030.00 USD | `-2.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.45` | 2,260,000.00 USD | 0.00 USD | 53,810.00 USD | `-2.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.55` | 2,210,000.00 USD | 0.00 USD | 10,380.00 USD | `-2.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.65` | 2,200,000.00 USD | 0.00 USD | 12,970.00 USD | `-2.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.75` | 2,180,000.00 USD | 0.00 USD | 20,190.00 USD | `-2.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.85` | 2,160,000.00 USD | 0.00 USD | 9,990.00 USD | `-2.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.95` | 2,150,000.00 USD | 0.00 USD | 8,370.00 USD | `-2.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.05` | 2,150,000.00 USD | 0.00 USD | 2,980.00 USD | `-2.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.15` | 2,140,000.00 USD | 0.00 USD | 42,510.00 USD | `-2.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.25` | 2,100,000.00 USD | 0.00 USD | 1,470.00 USD | `-2.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.35` | 2,100,000.00 USD | 0.00 USD | 4,370.00 USD | `-1.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.45` | 2,090,000.00 USD | 0.00 USD | 198,270.00 USD | `-1.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.55` | 1,900,000.00 USD | 0.00 USD | 155,200.00 USD | `-1.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.65` | 1,740,000.00 USD | 0.00 USD | 14,790.00 USD | `-1.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.75` | 1,730,000.00 USD | 0.00 USD | 12,880.00 USD | `-1.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.85` | 1,710,000.00 USD | 0.00 USD | 27,520.00 USD | `-1.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.95` | 1,690,000.00 USD | 0.00 USD | 8,990.00 USD | `-1.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.05` | 1,680,000.00 USD | 0.00 USD | 19,840.00 USD | `-1.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.15` | 1,660,000.00 USD | 0.00 USD | 1,550.00 USD | `-1.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.25` | 1,650,000.00 USD | 0.00 USD | 189,760.00 USD | `-1.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.35` | 1,470,000.00 USD | 0.00 USD | 43,540.00 USD | `-0.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.45` | 1,420,000.00 USD | 0.00 USD | 515.04 USD | `-0.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.55` | 1,420,000.00 USD | 0.00 USD | 11,410.00 USD | `-0.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.65` | 1,410,000.00 USD | 0.00 USD | 1,000.00 USD | `-0.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.75` | 1,410,000.00 USD | 0.00 USD | 4,690.00 USD | `-0.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.85` | 1,400,000.00 USD | 0.00 USD | 3,670.00 USD | `-0.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.95` | 1,400,000.00 USD | 0.00 USD | 21,960.00 USD | `-0.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `97.05` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | `-0.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `97.15` | 129.21 USD | 0.00 USD | 129.21 USD | `-0.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.25` | 1,860.00 USD | 1,860.00 USD | 0.00 USD | `+0.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.35` | 10,010.00 USD | 8,150.00 USD | 0.00 USD | `+0.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.45` | 37,340.00 USD | 27,330.00 USD | 0.00 USD | `+0.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.55` | 53,830.00 USD | 16,490.00 USD | 0.00 USD | `+0.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.65` | 60,340.00 USD | 6,510.00 USD | 0.00 USD | `+0.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.75` | 66,160.00 USD | 5,820.00 USD | 0.00 USD | `+0.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.85` | 68,170.00 USD | 2,010.00 USD | 0.00 USD | `+0.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.95` | 69,160.00 USD | 996.15 USD | 0.00 USD | `+0.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.05` | 528,980.00 USD | 459,820.00 USD | 0.00 USD | `+0.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.15` | 530,240.00 USD | 1,260.00 USD | 0.00 USD | `+0.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.25` | 541,030.00 USD | 10,780.00 USD | 0.00 USD | `+1.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.35` | 547,440.00 USD | 6,420.00 USD | 0.00 USD | `+1.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.45` | 618,900.00 USD | 71,460.00 USD | 0.00 USD | `+1.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.55` | 638,170.00 USD | 19,270.00 USD | 0.00 USD | `+1.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.65` | 638,770.00 USD | 600.78 USD | 0.00 USD | `+1.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.75` | 714,120.00 USD | 75,340.00 USD | 0.00 USD | `+1.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.85` | 719,310.00 USD | 5,190.00 USD | 0.00 USD | `+1.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.95` | 724,280.00 USD | 4,980.00 USD | 0.00 USD | `+1.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.05` | 896,830.00 USD | 172,550.00 USD | 0.00 USD | `+1.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.15` | 908,090.00 USD | 11,260.00 USD | 0.00 USD | `+1.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.25` | 908,280.00 USD | 191.55 USD | 0.00 USD | `+2.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.35` | 936,120.00 USD | 27,840.00 USD | 0.00 USD | `+2.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.45` | 948,920.00 USD | 12,800.00 USD | 0.00 USD | `+2.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.55` | 954,180.00 USD | 5,260.00 USD | 0.00 USD | `+2.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.65` | 966,350.00 USD | 12,170.00 USD | 0.00 USD | `+2.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.75` | 967,180.00 USD | 829.92 USD | 0.00 USD | `+2.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.85` | 971,160.00 USD | 3,980.00 USD | 0.00 USD | `+2.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.95` | 1,010,000.00 USD | 40,120.00 USD | 0.00 USD | `+2.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.05` | 2,400,000.00 USD | 1,390,000.00 USD | 0.00 USD | `+2.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.15` | 2,410,000.00 USD | 9,920.00 USD | 0.00 USD | `+2.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.25` | 2,420,000.00 USD | 4,920.00 USD | 0.00 USD | `+3.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.35` | 2,420,000.00 USD | 266.93 USD | 0.00 USD | `+3.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.45` | 2,420,000.00 USD | 2,410.00 USD | 0.00 USD | `+3.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.55` | 2,420,000.00 USD | 2,490.00 USD | 0.00 USD | `+3.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.65` | 2,450,000.00 USD | 22,050.00 USD | 0.00 USD | `+3.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.75` | 2,450,000.00 USD | 826.15 USD | 0.00 USD | `+3.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.85` | 2,450,000.00 USD | 1,540.00 USD | 0.00 USD | `+3.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.95` | 2,460,000.00 USD | 9,530.00 USD | 0.00 USD | `+3.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.05` | 2,490,000.00 USD | 36,140.00 USD | 0.00 USD | `+3.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.15` | 2,500,000.00 USD | 4,670.00 USD | 0.00 USD | `+4.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.25` | 2,510,000.00 USD | 7,110.00 USD | 0.00 USD | `+4.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.35` | 2,520,000.00 USD | 11,250.00 USD | 0.00 USD | `+4.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.45` | 2,520,000.00 USD | 1,990.00 USD | 0.00 USD | `+4.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.55` | 2,890,000.00 USD | 374,470.00 USD | 0.00 USD | `+4.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.65` | 2,890,000.00 USD | 762.38 USD | 0.00 USD | `+4.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.75` | 2,900,000.00 USD | 417.17 USD | 0.00 USD | `+4.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.85` | 2,900,000.00 USD | 2,210.00 USD | 0.00 USD | `+4.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.95` | 2,900,000.00 USD | 7,640.00 USD | 0.00 USD | `+4.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.05` | 3,970,000.00 USD | 1,060,000.00 USD | 0.00 USD | `+4.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.15` | 3,970,000.00 USD | 2,450.00 USD | 0.00 USD | `+5.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.25` | 3,980,000.00 USD | 7,120.00 USD | 0.00 USD | `+5.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.35` | 3,980,000.00 USD | 4,930.00 USD | 0.00 USD | `+5.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.45` | 3,990,000.00 USD | 7,280.00 USD | 0.00 USD | `+5.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.55` | 4,000,000.00 USD | 11,660.00 USD | 0.00 USD | `+5.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.65` | 4,270,000.00 USD | 265,320.00 USD | 0.00 USD | `+5.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.75` | 4,270,000.00 USD | 1,280.00 USD | 0.00 USD | `+5.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.85` | 4,270,000.00 USD | 4,390.00 USD | 0.00 USD | `+5.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.95` | 4,280,000.00 USD | 5,370.00 USD | 0.00 USD | `+5.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.05` | 4,310,000.00 USD | 35,600.00 USD | 0.00 USD | `+5.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.15` | 4,320,000.00 USD | 2,010.00 USD | 0.00 USD | `+6.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.25` | 4,380,000.00 USD | 64,080.00 USD | 0.00 USD | `+6.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.35` | 4,380,000.00 USD | 4,260.00 USD | 0.00 USD | `+6.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.45` | 4,390,000.00 USD | 3,860.00 USD | 0.00 USD | `+6.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.55` | 4,400,000.00 USD | 6,440.00 USD | 0.00 USD | `+6.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.65` | 4,400,000.00 USD | 2,660.00 USD | 0.00 USD | `+6.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.75` | 4,400,000.00 USD | 611.09 USD | 0.00 USD | `+6.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.85` | 4,620,000.00 USD | 218,150.00 USD | 0.00 USD | `+6.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.95` | 4,670,000.00 USD | 54,180.00 USD | 0.00 USD | `+6.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.05` | 4,690,000.00 USD | 21,390.00 USD | 0.00 USD | `+7.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.15` | 4,690,000.00 USD | 1,720.00 USD | 0.00 USD | `+7.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.25` | 4,690,000.00 USD | 519.17 USD | 0.00 USD | `+7.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.35` | 4,690,000.00 USD | 146.09 USD | 0.00 USD | `+7.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.45` | 4,790,000.00 USD | 94,960.00 USD | 0.00 USD | `+7.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.55` | 4,820,000.00 USD | 26,540.00 USD | 0.00 USD | `+7.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.65` | 4,820,000.00 USD | 2,650.00 USD | 0.00 USD | `+7.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.75` | 4,820,000.00 USD | 1,900.00 USD | 0.00 USD | `+7.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.85` | 4,830,000.00 USD | 5,900.00 USD | 0.00 USD | `+7.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.95` | 4,850,000.00 USD | 26,100.00 USD | 0.00 USD | `+7.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.05` | 4,900,000.00 USD | 44,180.00 USD | 0.00 USD | `+8.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.15` | 4,930,000.00 USD | 31,990.00 USD | 0.00 USD | `+8.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.25` | 4,930,000.00 USD | 1,010.00 USD | 0.00 USD | `+8.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.35` | 4,930,000.00 USD | 1,090.00 USD | 0.00 USD | `+8.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.45` | 4,930,000.00 USD | 266.79 USD | 0.00 USD | `+8.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.55` | 4,930,000.00 USD | 3,620.00 USD | 0.00 USD | `+8.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.65` | 4,930,000.00 USD | 235.60 USD | 0.00 USD | `+8.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.75` | 4,940,000.00 USD | 549.90 USD | 0.00 USD | `+8.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.85` | 4,950,000.00 USD | 10,600.00 USD | 0.00 USD | `+8.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.95` | 4,950,000.00 USD | 206.60 USD | 0.00 USD | `+8.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.05` | 4,970,000.00 USD | 19,890.00 USD | 0.00 USD | `+9.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.15` | 4,970,000.00 USD | 7,080.00 USD | 0.00 USD | `+9.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.25` | 4,970,000.00 USD | 758.62 USD | 0.00 USD | `+9.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.35` | 4,980,000.00 USD | 7,980.00 USD | 0.00 USD | `+9.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.45` | 5,010,000.00 USD | 26,170.00 USD | 0.00 USD | `+9.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.55` | 5,020,000.00 USD | 6,950.00 USD | 0.00 USD | `+9.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.65` | 5,020,000.00 USD | 355.14 USD | 0.00 USD | `+9.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.75` | 5,130,000.00 USD | 110,530.00 USD | 0.00 USD | `+9.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.85` | 5,130,000.00 USD | 1,400.00 USD | 0.00 USD | `+9.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.95` | 5,130,000.00 USD | 725.12 USD | 0.00 USD | `+9.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.05` | 5,270,000.00 USD | 142,930.00 USD | 0.00 USD | `+10.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.15` | 5,270,000.00 USD | 1,200.00 USD | 0.00 USD | `+10.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.25` | 5,290,000.00 USD | 20,190.00 USD | 0.00 USD | `+10.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.35` | 5,290,000.00 USD | 698.85 USD | 0.00 USD | `+10.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.45` | 5,300,000.00 USD | 8,930.00 USD | 0.00 USD | `+10.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.55` | 5,350,000.00 USD | 52,130.00 USD | 0.00 USD | `+10.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.65` | 5,420,000.00 USD | 65,380.00 USD | 0.00 USD | `+10.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.75` | 5,420,000.00 USD | 536.60 USD | 0.00 USD | `+10.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.85` | 5,430,000.00 USD | 11,350.00 USD | 0.00 USD | `+10.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.95` | 5,440,000.00 USD | 9,120.00 USD | 0.00 USD | `+11.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.05` | 5,520,000.00 USD | 83,710.00 USD | 0.00 USD | `+11.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.15` | 5,590,000.00 USD | 68,190.00 USD | 0.00 USD | `+11.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.35` | 5,600,000.00 USD | 7,140.00 USD | 0.00 USD | `+11.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.45` | 5,600,000.00 USD | 2,580.00 USD | 0.00 USD | `+11.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.55` | 5,610,000.00 USD | 5,430.00 USD | 0.00 USD | `+11.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.65` | 5,610,000.00 USD | 666.02 USD | 0.00 USD | `+11.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.75` | 5,610,000.00 USD | 1,030.00 USD | 0.00 USD | `+11.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.85` | 5,610,000.00 USD | 1,430.00 USD | 0.00 USD | `+11.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.95` | 5,700,000.00 USD | 92,840.00 USD | 0.00 USD | `+12.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.05` | 5,780,000.00 USD | 72,930.00 USD | 0.00 USD | `+12.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.15` | 5,790,000.00 USD | 8,620.00 USD | 0.00 USD | `+12.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.25` | 9,390,000.00 USD | 3,610,000.00 USD | 0.00 USD | `+12.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.35` | 9,420,000.00 USD | 25,320.00 USD | 0.00 USD | `+12.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.45` | 9,420,000.00 USD | 5,880.00 USD | 0.00 USD | `+12.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.55` | 9,430,000.00 USD | 1,070.00 USD | 0.00 USD | `+12.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.65` | 9,430,000.00 USD | 5,410.00 USD | 0.00 USD | `+12.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.75` | 9,430,000.00 USD | 1,370.00 USD | 0.00 USD | `+12.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.85` | 9,430,000.00 USD | 1,430.00 USD | 0.00 USD | `+12.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.95` | 9,430,000.00 USD | 357.34 USD | 0.00 USD | `+13.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.05` | 9,970,000.00 USD | 539,620.00 USD | 0.00 USD | `+13.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.15` | 9,970,000.00 USD | 1,030.00 USD | 0.00 USD | `+13.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.25` | 9,980,000.00 USD | 3,230.00 USD | 0.00 USD | `+13.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.35` | 9,980,000.00 USD | 1,610.00 USD | 0.00 USD | `+13.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.45` | 9,980,000.00 USD | 1,580.00 USD | 0.00 USD | `+13.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.55` | 9,990,000.00 USD | 10,280.00 USD | 0.00 USD | `+13.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.65` | 9,990,000.00 USD | 3,030.00 USD | 0.00 USD | `+13.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.85` | 10,010,000.00 USD | 17,740.00 USD | 0.00 USD | `+14.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.95` | 10,090,000.00 USD | 74,410.00 USD | 0.00 USD | `+14.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.05` | 10,160,000.00 USD | 71,520.00 USD | 0.00 USD | `+14.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.15` | 10,160,000.00 USD | 1,300.00 USD | 0.00 USD | `+14.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.25` | 10,170,000.00 USD | 5,910.00 USD | 0.00 USD | `+14.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.45` | 10,170,000.00 USD | 585.11 USD | 0.00 USD | `+14.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.55` | 10,170,000.00 USD | 852.24 USD | 0.00 USD | `+14.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.65` | 10,190,000.00 USD | 22,910.00 USD | 0.00 USD | `+14.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.75` | 10,190,000.00 USD | 2,420.00 USD | 0.00 USD | `+14.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.85` | 10,190,000.00 USD | 2,330.00 USD | 0.00 USD | `+15.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.05` | 10,210,000.00 USD | 17,800.00 USD | 0.00 USD | `+15.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.15` | 10,260,000.00 USD | 49,680.00 USD | 0.00 USD | `+15.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.25` | 10,270,000.00 USD | 4,960.00 USD | 0.00 USD | `+15.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.35` | 10,270,000.00 USD | 6,270.00 USD | 0.00 USD | `+15.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.45` | 10,270,000.00 USD | 843.38 USD | 0.00 USD | `+15.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.55` | 10,310,000.00 USD | 36,280.00 USD | 0.00 USD | `+15.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.65` | 10,320,000.00 USD | 6,150.00 USD | 0.00 USD | `+15.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.85` | 10,320,000.00 USD | 586.82 USD | 0.00 USD | `+16.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.05` | 10,400,000.00 USD | 78,560.00 USD | 0.00 USD | `+16.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.25` | 10,400,000.00 USD | 473.38 USD | 0.00 USD | `+16.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.35` | 10,430,000.00 USD | 35,070.00 USD | 0.00 USD | `+16.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.45` | 10,430,000.00 USD | 655.74 USD | 0.00 USD | `+16.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.55` | 10,440,000.00 USD | 4,470.00 USD | 0.00 USD | `+16.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.65` | 10,440,000.00 USD | 395.50 USD | 0.00 USD | `+16.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.75` | 10,440,000.00 USD | 257.07 USD | 0.00 USD | `+16.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.85` | 10,440,000.00 USD | 4,540.00 USD | 0.00 USD | `+17.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.05` | 10,440,000.00 USD | 1,970.00 USD | 0.00 USD | `+17.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.15` | 10,460,000.00 USD | 11,410.00 USD | 0.00 USD | `+17.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.25` | 10,460,000.00 USD | 907.14 USD | 0.00 USD | `+17.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.35` | 10,460,000.00 USD | 740.99 USD | 0.00 USD | `+17.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.45` | 10,460,000.00 USD | 343.35 USD | 0.00 USD | `+17.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.55` | 10,460,000.00 USD | 1,640.00 USD | 0.00 USD | `+17.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.65` | 10,460,000.00 USD | 105.48 USD | 0.00 USD | `+17.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.75` | 10,460,000.00 USD | 1,010.00 USD | 0.00 USD | `+18.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.95` | 10,460,000.00 USD | 2,520.00 USD | 0.00 USD | `+18.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.05` | 10,540,000.00 USD | 79,820.00 USD | 0.00 USD | `+18.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.35` | 10,540,000.00 USD | 309.14 USD | 0.00 USD | `+18.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.45` | 10,540,000.00 USD | 346.35 USD | 0.00 USD | `+18.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.55` | 10,550,000.00 USD | 2,440.00 USD | 0.00 USD | `+18.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.75` | 10,550,000.00 USD | 121.54 USD | 0.00 USD | `+19.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.85` | 10,550,000.00 USD | 579.25 USD | 0.00 USD | `+19.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.05` | 10,550,000.00 USD | 6,180.00 USD | 0.00 USD | `+19.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.15` | 10,550,000.00 USD | 1,740.00 USD | 0.00 USD | `+19.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.25` | 10,560,000.00 USD | 1,920.00 USD | 0.00 USD | `+19.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.45` | 10,560,000.00 USD | 2,870.00 USD | 0.00 USD | `+19.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.55` | 10,570,000.00 USD | 10,810.00 USD | 0.00 USD | `+19.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.65` | 10,570,000.00 USD | 1,100.00 USD | 0.00 USD | `+19.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.75` | 10,570,000.00 USD | 3,580.00 USD | 0.00 USD | `+20.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.85` | 10,570,000.00 USD | 234.87 USD | 0.00 USD | `+20.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.95` | 10,590,000.00 USD | 12,860.00 USD | 0.00 USD | `+20.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.05` | 10,590,000.00 USD | 3,740.00 USD | 0.00 USD | `+20.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.15` | 10,590,000.00 USD | 584.58 USD | 0.00 USD | `+20.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.25` | 10,590,000.00 USD | 1,740.00 USD | 0.00 USD | `+20.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.35` | 10,600,000.00 USD | 2,330.00 USD | 0.00 USD | `+20.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.45` | 10,710,000.00 USD | 118,690.00 USD | 0.00 USD | `+20.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.65` | 10,820,000.00 USD | 106,330.00 USD | 0.00 USD | `+20.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.75` | 10,830,000.00 USD | 5,920.00 USD | 0.00 USD | `+21.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.85` | 10,880,000.00 USD | 55,580.00 USD | 0.00 USD | `+21.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.05` | 10,950,000.00 USD | 70,920.00 USD | 0.00 USD | `+21.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.15` | 10,960,000.00 USD | 3,980.00 USD | 0.00 USD | `+21.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.25` | 10,960,000.00 USD | 4,460.00 USD | 0.00 USD | `+21.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.35` | 10,960,000.00 USD | 127.82 USD | 0.00 USD | `+21.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.45` | 10,960,000.00 USD | 707.15 USD | 0.00 USD | `+21.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.55` | 10,960,000.00 USD | 1,260.00 USD | 0.00 USD | `+21.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.65` | 10,970,000.00 USD | 2,970.00 USD | 0.00 USD | `+22.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.75` | 10,970,000.00 USD | 403.75 USD | 0.00 USD | `+22.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.85` | 10,980,000.00 USD | 15,940.00 USD | 0.00 USD | `+22.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.95` | 11,030,000.00 USD | 42,290.00 USD | 0.00 USD | `+22.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.05` | 11,090,000.00 USD | 65,030.00 USD | 0.00 USD | `+22.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.15` | 11,100,000.00 USD | 8,120.00 USD | 0.00 USD | `+22.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.25` | 11,100,000.00 USD | 1,850.00 USD | 0.00 USD | `+22.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.35` | 11,100,000.00 USD | 4,150.00 USD | 0.00 USD | `+22.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.45` | 11,110,000.00 USD | 3,580.00 USD | 0.00 USD | `+22.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.65` | 11,110,000.00 USD | 615.00 USD | 0.00 USD | `+23.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.75` | 11,230,000.00 USD | 125,500.00 USD | 0.00 USD | `+23.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.85` | 11,270,000.00 USD | 37,630.00 USD | 0.00 USD | `+23.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.95` | 11,270,000.00 USD | 458.21 USD | 0.00 USD | `+23.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.05` | 11,450,000.00 USD | 180,350.00 USD | 0.00 USD | `+23.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.15` | 11,450,000.00 USD | 414.52 USD | 0.00 USD | `+23.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.25` | 11,460,000.00 USD | 3,210.00 USD | 0.00 USD | `+23.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.35` | 11,460,000.00 USD | 7,850.00 USD | 0.00 USD | `+23.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.45` | 11,460,000.00 USD | 184.29 USD | 0.00 USD | `+23.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.55` | 11,470,000.00 USD | 904.13 USD | 0.00 USD | `+23.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.65` | 11,470,000.00 USD | 191.83 USD | 0.00 USD | `+24.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.75` | 11,470,000.00 USD | 2,150.00 USD | 0.00 USD | `+24.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.85` | 11,470,000.00 USD | 663.47 USD | 0.00 USD | `+24.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.05` | 11,490,000.00 USD | 20,810.00 USD | 0.00 USD | `+24.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.15` | 11,490,000.00 USD | 122.36 USD | 0.00 USD | `+24.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.25` | 11,500,000.00 USD | 11,200.00 USD | 0.00 USD | `+24.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.45` | 11,510,000.00 USD | 11,570.00 USD | 0.00 USD | `+24.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.55` | 11,520,000.00 USD | 7,860.00 USD | 0.00 USD | `+25.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.65` | 11,520,000.00 USD | 2,070.00 USD | 0.00 USD | `+25.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.75` | 11,520,000.00 USD | 2,450.00 USD | 0.00 USD | `+25.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.85` | 11,530,000.00 USD | 1,480.00 USD | 0.00 USD | `+25.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.95` | 11,610,000.00 USD | 80,260.00 USD | 0.00 USD | `+25.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.05` | 11,800,000.00 USD | 194,050.00 USD | 0.00 USD | `+25.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.15` | 11,800,000.00 USD | 1,000.00 USD | 0.00 USD | `+25.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.25` | 12,040,000.00 USD | 234,430.00 USD | 0.00 USD | `+25.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.35` | 12,090,000.00 USD | 52,330.00 USD | 0.00 USD | `+25.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.45` | 12,090,000.00 USD | 3,060.00 USD | 0.00 USD | `+25.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.55` | 12,100,000.00 USD | 7,020.00 USD | 0.00 USD | `+26.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.65` | 12,110,000.00 USD | 11,000.00 USD | 0.00 USD | `+26.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.75` | 12,110,000.00 USD | 235.68 USD | 0.00 USD | `+26.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.85` | 12,110,000.00 USD | 3,850.00 USD | 0.00 USD | `+26.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.95` | 12,130,000.00 USD | 16,430.00 USD | 0.00 USD | `+26.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.05` | 13,140,000.00 USD | 1,010,000.00 USD | 0.00 USD | `+26.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.15` | 13,140,000.00 USD | 252.46 USD | 0.00 USD | `+26.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.25` | 13,150,000.00 USD | 7,710.00 USD | 0.00 USD | `+26.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.35` | 13,150,000.00 USD | 6,790.00 USD | 0.00 USD | `+26.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.45` | 13,160,000.00 USD | 2,670.00 USD | 0.00 USD | `+26.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.55` | 13,160,000.00 USD | 632.58 USD | 0.00 USD | `+27.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.65` | 13,170,000.00 USD | 15,370.00 USD | 0.00 USD | `+27.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.85` | 13,180,000.00 USD | 5,530.00 USD | 0.00 USD | `+27.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.95` | 13,200,000.00 USD | 18,470.00 USD | 0.00 USD | `+27.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.05` | 13,210,000.00 USD | 11,030.00 USD | 0.00 USD | `+27.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.15` | 13,210,000.00 USD | 1,320.00 USD | 0.00 USD | `+27.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.25` | 13,210,000.00 USD | 151.59 USD | 0.00 USD | `+27.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.35` | 13,210,000.00 USD | 4,240.00 USD | 0.00 USD | `+27.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.45` | 13,210,000.00 USD | 1,370.00 USD | 0.00 USD | `+27.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.55` | 13,220,000.00 USD | 9,270.00 USD | 0.00 USD | `+28.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.65` | 13,230,000.00 USD | 6,610.00 USD | 0.00 USD | `+28.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.85` | 13,230,000.00 USD | 596.78 USD | 0.00 USD | `+28.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.95` | 13,240,000.00 USD | 10,310.00 USD | 0.00 USD | `+28.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.05` | 13,790,000.00 USD | 546,780.00 USD | 0.00 USD | `+28.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.15` | 13,790,000.00 USD | 603.22 USD | 0.00 USD | `+28.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.25` | 13,790,000.00 USD | 311.87 USD | 0.00 USD | `+28.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.35` | 13,800,000.00 USD | 6,780.00 USD | 0.00 USD | `+28.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.45` | 13,800,000.00 USD | 993.56 USD | 0.00 USD | `+29.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.55` | 13,810,000.00 USD | 16,280.00 USD | 0.00 USD | `+29.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.85` | 13,810,000.00 USD | 471.94 USD | 0.00 USD | `+29.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.95` | 13,810,000.00 USD | 209.08 USD | 0.00 USD | `+29.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.05` | 13,970,000.00 USD | 151,060.00 USD | 0.00 USD | `+29.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.15` | 13,970,000.00 USD | 189.23 USD | 0.00 USD | `+29.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.45` | 13,970,000.00 USD | 187.15 USD | 0.00 USD | `+30.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.65` | 13,970,000.00 USD | 3,550.00 USD | 0.00 USD | `+30.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.75` | 13,980,000.00 USD | 7,460.00 USD | 0.00 USD | `+30.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.05` | 14,170,000.00 USD | 190,580.00 USD | 0.00 USD | `+30.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.35` | 14,170,000.00 USD | 534.87 USD | 0.00 USD | `+30.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.45` | 14,170,000.00 USD | 4,620.00 USD | 0.00 USD | `+31.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.65` | 14,180,000.00 USD | 5,000.00 USD | 0.00 USD | `+31.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.75` | 14,180,000.00 USD | 362.81 USD | 0.00 USD | `+31.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.85` | 14,240,000.00 USD | 60,770.00 USD | 0.00 USD | `+31.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.95` | 14,240,000.00 USD | 482.37 USD | 0.00 USD | `+31.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.05` | 14,240,000.00 USD | 3,700.00 USD | 0.00 USD | `+31.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.15` | 14,250,000.00 USD | 3,010.00 USD | 0.00 USD | `+31.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.25` | 14,250,000.00 USD | 191.09 USD | 0.00 USD | `+31.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.65` | 14,290,000.00 USD | 41,130.00 USD | 0.00 USD | `+32.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.95` | 14,300,000.00 USD | 12,600.00 USD | 0.00 USD | `+32.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.05` | 14,350,000.00 USD | 50,720.00 USD | 0.00 USD | `+32.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.15` | 14,350,000.00 USD | 229.89 USD | 0.00 USD | `+32.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.25` | 14,370,000.00 USD | 15,330.00 USD | 0.00 USD | `+32.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.45` | 14,370,000.00 USD | 401.29 USD | 0.00 USD | `+33.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.55` | 14,370,000.00 USD | 1,320.00 USD | 0.00 USD | `+33.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.65` | 14,370,000.00 USD | 152.99 USD | 0.00 USD | `+33.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.75` | 14,370,000.00 USD | 153.10 USD | 0.00 USD | `+33.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.85` | 14,370,000.00 USD | 116.87 USD | 0.00 USD | `+33.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.05` | 14,420,000.00 USD | 50,760.00 USD | 0.00 USD | `+33.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.35` | 14,420,000.00 USD | 1,760.00 USD | 0.00 USD | `+34.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.45` | 14,420,000.00 USD | 4,090.00 USD | 0.00 USD | `+34.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.65` | 14,420,000.00 USD | 192.06 USD | 0.00 USD | `+34.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.75` | 14,430,000.00 USD | 3,150.00 USD | 0.00 USD | `+34.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.85` | 14,430,000.00 USD | 2,620.00 USD | 0.00 USD | `+34.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.95` | 14,440,000.00 USD | 10,140.00 USD | 0.00 USD | `+34.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.05` | 14,450,000.00 USD | 6,000.00 USD | 0.00 USD | `+34.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.15` | 14,450,000.00 USD | 5,950.00 USD | 0.00 USD | `+34.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.25` | 14,460,000.00 USD | 8,820.00 USD | 0.00 USD | `+34.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.45` | 14,460,000.00 USD | 135.39 USD | 0.00 USD | `+35.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.65` | 14,620,000.00 USD | 160,920.00 USD | 0.00 USD | `+35.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.75` | 14,620,000.00 USD | 144.93 USD | 0.00 USD | `+35.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.05` | 14,630,000.00 USD | 12,390.00 USD | 0.00 USD | `+35.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.65` | 14,640,000.00 USD | 397.95 USD | 0.00 USD | `+36.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.85` | 14,640,000.00 USD | 9,310.00 USD | 0.00 USD | `+36.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.95` | 14,650,000.00 USD | 3,910.00 USD | 0.00 USD | `+36.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.05` | 14,650,000.00 USD | 267.43 USD | 0.00 USD | `+36.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.15` | 14,650,000.00 USD | 509.96 USD | 0.00 USD | `+36.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.25` | 14,650,000.00 USD | 191.88 USD | 0.00 USD | `+37.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.35` | 14,650,000.00 USD | 237.36 USD | 0.00 USD | `+37.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.55` | 14,650,000.00 USD | 1,210.00 USD | 0.00 USD | `+37.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.65` | 14,650,000.00 USD | 192.46 USD | 0.00 USD | `+37.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.75` | 14,650,000.00 USD | 112.35 USD | 0.00 USD | `+37.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.95` | 14,660,000.00 USD | 4,490.00 USD | 0.00 USD | `+37.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.05` | 14,710,000.00 USD | 54,080.00 USD | 0.00 USD | `+37.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.25` | 14,710,000.00 USD | 331.60 USD | 0.00 USD | `+38.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.55` | 14,980,000.00 USD | 270,270.00 USD | 0.00 USD | `+38.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.85` | 14,980,000.00 USD | 668.86 USD | 0.00 USD | `+38.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `135.05` | 15,100,000.00 USD | 116,220.00 USD | 0.00 USD | `+38.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `135.55` | 15,100,000.00 USD | 7,560.00 USD | 0.00 USD | `+39.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.05` | 15,110,000.00 USD | 1,890.00 USD | 0.00 USD | `+39.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.35` | 15,110,000.00 USD | 192.25 USD | 0.00 USD | `+40.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.45` | 15,110,000.00 USD | 465.29 USD | 0.00 USD | `+40.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.55` | 15,110,000.00 USD | 389.17 USD | 0.00 USD | `+40.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.85` | 15,110,000.00 USD | 826.57 USD | 0.00 USD | `+40.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.05` | 15,110,000.00 USD | 231.61 USD | 0.00 USD | `+40.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.25` | 15,110,000.00 USD | 2,910.00 USD | 0.00 USD | `+41.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.35` | 15,120,000.00 USD | 3,920.00 USD | 0.00 USD | `+41.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.65` | 15,140,000.00 USD | 26,260.00 USD | 0.00 USD | `+41.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.75` | 15,140,000.00 USD | 133.62 USD | 0.00 USD | `+41.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.05` | 15,160,000.00 USD | 18,910.00 USD | 0.00 USD | `+41.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.45` | 15,160,000.00 USD | 692.25 USD | 0.00 USD | `+42.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.65` | 15,160,000.00 USD | 406.24 USD | 0.00 USD | `+42.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.85` | 21,910,000.00 USD | 6,740,000.00 USD | 0.00 USD | `+42.79%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `138.95` | 21,910,000.00 USD | 826.75 USD | 0.00 USD | `+42.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `139.05` | 24,100,000.00 USD | 2,190,000.00 USD | 0.00 USD | `+43.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `139.55` | 24,100,000.00 USD | 5,920.00 USD | 0.00 USD | `+43.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.05` | 24,230,000.00 USD | 128,430.00 USD | 0.00 USD | `+44.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.45` | 24,240,000.00 USD | 12,120.00 USD | 0.00 USD | `+44.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.55` | 24,340,000.00 USD | 98,400.00 USD | 0.00 USD | `+44.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.75` | 24,340,000.00 USD | 990.88 USD | 0.00 USD | `+44.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `141.05` | 24,360,000.00 USD | 11,640.00 USD | 0.00 USD | `+45.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `141.25` | 24,360,000.00 USD | 6,190.00 USD | 0.00 USD | `+45.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `141.65` | 24,360,000.00 USD | 796.07 USD | 0.00 USD | `+45.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `142.05` | 24,360,000.00 USD | 826.73 USD | 0.00 USD | `+46.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `142.85` | 24,360,000.00 USD | 278.56 USD | 0.00 USD | `+46.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `142.95` | 24,690,000.00 USD | 329,100.00 USD | 0.00 USD | `+47.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `143.05` | 24,770,000.00 USD | 72,610.00 USD | 0.00 USD | `+47.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `143.15` | 24,780,000.00 USD | 16,980.00 USD | 0.00 USD | `+47.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `143.35` | 24,780,000.00 USD | 528.96 USD | 0.00 USD | `+47.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.05` | 24,790,000.00 USD | 6,330.00 USD | 0.00 USD | `+48.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.25` | 24,790,000.00 USD | 415.44 USD | 0.00 USD | `+48.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.35` | 25,070,000.00 USD | 282,520.00 USD | 0.00 USD | `+48.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.55` | 25,080,000.00 USD | 7,260.00 USD | 0.00 USD | `+48.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.75` | 25,080,000.00 USD | 791.78 USD | 0.00 USD | `+48.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `145.05` | 25,120,000.00 USD | 36,040.00 USD | 0.00 USD | `+49.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `145.25` | 25,120,000.00 USD | 209.16 USD | 0.00 USD | `+49.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `145.55` | 25,120,000.00 USD | 698.64 USD | 0.00 USD | `+49.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.05` | 25,310,000.00 USD | 190,100.00 USD | 0.00 USD | `+50.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.15` | 25,310,000.00 USD | 3,300.00 USD | 0.00 USD | `+50.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.25` | 25,310,000.00 USD | 1,020.00 USD | 0.00 USD | `+50.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.95` | 25,310,000.00 USD | 1,500.00 USD | 0.00 USD | `+51.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.05` | 25,350,000.00 USD | 37,700.00 USD | 0.00 USD | `+51.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.45` | 25,350,000.00 USD | 844.89 USD | 0.00 USD | `+51.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.85` | 25,360,000.00 USD | 4,610.00 USD | 0.00 USD | `+52.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.95` | 25,360,000.00 USD | 3,100.00 USD | 0.00 USD | `+52.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `148.05` | 26,700,000.00 USD | 1,340,000.00 USD | 0.00 USD | `+52.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `148.45` | 26,700,000.00 USD | 1,370.00 USD | 0.00 USD | `+52.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `148.55` | 26,700,000.00 USD | 4,760.00 USD | 0.00 USD | `+52.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `149.05` | 26,700,000.00 USD | 549.99 USD | 0.00 USD | `+53.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `149.15` | 27,210,000.00 USD | 510,120.00 USD | 0.00 USD | `+53.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.05` | 27,470,000.00 USD | 254,780.00 USD | 0.00 USD | `+54.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.25` | 27,470,000.00 USD | 1,200.00 USD | 0.00 USD | `+54.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.35` | 27,470,000.00 USD | 178.92 USD | 0.00 USD | `+54.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.55` | 27,470,000.00 USD | 1,360.00 USD | 0.00 USD | `+54.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.05` | 27,490,000.00 USD | 14,430.00 USD | 0.00 USD | `+55.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.25` | 27,490,000.00 USD | 2,000.00 USD | 0.00 USD | `+55.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.45` | 27,490,000.00 USD | 411.94 USD | 0.00 USD | `+55.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `153.15` | 27,500,000.00 USD | 10,620.00 USD | 0.00 USD | `+57.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `153.65` | 27,500,000.00 USD | 1,020.00 USD | 0.00 USD | `+58.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `154.55` | 27,510,000.00 USD | 12,000.00 USD | 0.00 USD | `+58.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `154.85` | 27,510,000.00 USD | 113.04 USD | 0.00 USD | `+59.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `155.05` | 27,510,000.00 USD | 1,830.00 USD | 0.00 USD | `+59.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `155.35` | 27,540,000.00 USD | 22,680.00 USD | 0.00 USD | `+59.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `155.85` | 27,550,000.00 USD | 16,970.00 USD | 0.00 USD | `+60.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `156.05` | 27,560,000.00 USD | 2,230.00 USD | 0.00 USD | `+60.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `158.05` | 27,560,000.00 USD | 6,640.00 USD | 0.00 USD | `+62.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `158.75` | 27,580,000.00 USD | 15,880.00 USD | 0.00 USD | `+63.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `159.15` | 27,580,000.00 USD | 692.30 USD | 0.00 USD | `+63.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `159.95` | 27,590,000.00 USD | 5,620.00 USD | 0.00 USD | `+64.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `160.05` | 27,670,000.00 USD | 89,040.00 USD | 0.00 USD | `+64.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `161.05` | 27,670,000.00 USD | 281.84 USD | 0.00 USD | `+65.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `163.05` | 27,680,000.00 USD | 4,080.00 USD | 0.00 USD | `+67.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `165.05` | 27,760,000.00 USD | 82,530.00 USD | 0.00 USD | `+69.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `165.45` | 27,760,000.00 USD | 823.94 USD | 0.00 USD | `+70.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `166.45` | 27,760,000.00 USD | 211.39 USD | 0.00 USD | `+71.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `166.95` | 27,760,000.00 USD | 307.19 USD | 0.00 USD | `+71.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `167.05` | 27,760,000.00 USD | 593.03 USD | 0.00 USD | `+71.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `167.75` | 27,760,000.00 USD | 1,440.00 USD | 0.00 USD | `+72.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `168.05` | 27,770,000.00 USD | 5,720.00 USD | 0.00 USD | `+72.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `169.55` | 27,770,000.00 USD | 495.09 USD | 0.00 USD | `+74.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `169.95` | 27,770,000.00 USD | 912.63 USD | 0.00 USD | `+74.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `170.05` | 27,820,000.00 USD | 43,480.00 USD | 0.00 USD | `+74.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `171.55` | 27,820,000.00 USD | 686.20 USD | 0.00 USD | `+76.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `172.05` | 27,850,000.00 USD | 35,280.00 USD | 0.00 USD | `+76.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `172.45` | 27,850,000.00 USD | 703.60 USD | 0.00 USD | `+77.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `173.05` | 27,850,000.00 USD | 3,160.00 USD | 0.00 USD | `+77.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `174.85` | 27,860,000.00 USD | 1,430.00 USD | 0.00 USD | `+79.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `175.05` | 27,910,000.00 USD | 52,520.00 USD | 0.00 USD | `+80.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `175.25` | 27,930,000.00 USD | 21,960.00 USD | 0.00 USD | `+80.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `176.85` | 27,930,000.00 USD | 1,450.00 USD | 0.00 USD | `+81.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `177.05` | 27,930,000.00 USD | 885.25 USD | 0.00 USD | `+82.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `178.55` | 27,940,000.00 USD | 2,990.00 USD | 0.00 USD | `+83.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `179.15` | 27,940,000.00 USD | 261.56 USD | 0.00 USD | `+84.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `180.05` | 28,020,000.00 USD | 80,290.00 USD | 0.00 USD | `+85.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `181.05` | 28,020,000.00 USD | 2,520.00 USD | 0.00 USD | `+86.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `181.95` | 28,020,000.00 USD | 349.34 USD | 0.00 USD | `+87.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `182.45` | 28,040,000.00 USD | 19,620.00 USD | 0.00 USD | `+87.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `183.45` | 28,590,000.00 USD | 550,350.00 USD | 0.00 USD | `+88.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `185.05` | 28,620,000.00 USD | 29,610.00 USD | 0.00 USD | `+90.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `187.05` | 28,780,000.00 USD | 165,580.00 USD | 0.00 USD | `+92.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `188.05` | 28,930,000.00 USD | 141,190.00 USD | 0.00 USD | `+93.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `190.05` | 28,960,000.00 USD | 35,880.00 USD | 0.00 USD | `+95.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `190.35` | 28,960,000.00 USD | 744.27 USD | 0.00 USD | `+95.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `190.65` | 28,970,000.00 USD | 7,750.00 USD | 0.00 USD | `+96.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `194.05` | 28,970,000.00 USD | 4,270.00 USD | 0.00 USD | `+99.56%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `82.50` | 171,440,000.00 USD | 0.00 USD | 171,440,000.00 USD | 71,680.00 USD | 3,750.00 USD | 2,420.00 USD |
| `7D` | `82.70` | 171,360,000.00 USD | 0.00 USD | 171,360,000.00 USD | 0.00 USD | 54,980.00 USD | 140,740.00 USD |
| `7D` | `82.90` | 171,170,000.00 USD | 0.00 USD | 171,170,000.00 USD | 1,670.00 USD | 2,080.00 USD | 0.00 USD |
| `7D` | `83.10` | 171,160,000.00 USD | 0.00 USD | 171,160,000.00 USD | 1,690.00 USD | 48,940.00 USD | 642.56 USD |
| `7D` | `83.30` | 171,110,000.00 USD | 0.00 USD | 171,110,000.00 USD | 3,730.00 USD | 93,000.00 USD | 56,580.00 USD |
| `7D` | `83.50` | 170,960,000.00 USD | 0.00 USD | 170,960,000.00 USD | 6,440.00 USD | 791.58 USD | 41,020.00 USD |
| `7D` | `83.70` | 170,910,000.00 USD | 0.00 USD | 170,910,000.00 USD | 0.00 USD | 68,140.00 USD | 85,660.00 USD |
| `7D` | `83.90` | 170,750,000.00 USD | 0.00 USD | 170,750,000.00 USD | 2,640.00 USD | 0.00 USD | 70,110.00 USD |
| `7D` | `84.10` | 170,680,000.00 USD | 0.00 USD | 170,680,000.00 USD | 0.00 USD | 14,010.00 USD | 8,980.00 USD |
| `7D` | `84.30` | 170,660,000.00 USD | 0.00 USD | 170,660,000.00 USD | 0.00 USD | 26,170.00 USD | 0.00 USD |
| `7D` | `85.10` | 170,630,000.00 USD | 0.00 USD | 170,630,000.00 USD | 0.00 USD | 204,940.00 USD | 0.00 USD |
| `7D` | `85.30` | 170,430,000.00 USD | 0.00 USD | 170,430,000.00 USD | 0.00 USD | 13,630.00 USD | 186,170.00 USD |
| `7D` | `85.50` | 170,230,000.00 USD | 0.00 USD | 170,230,000.00 USD | 0.00 USD | 12,950.00 USD | 6,140.00 USD |
| `7D` | `85.70` | 170,210,000.00 USD | 0.00 USD | 170,210,000.00 USD | 0.00 USD | 0.00 USD | 189,820.00 USD |
| `7D` | `85.90` | 170,020,000.00 USD | 0.00 USD | 170,020,000.00 USD | 0.00 USD | 260,960.00 USD | 0.00 USD |
| `7D` | `86.10` | 169,760,000.00 USD | 0.00 USD | 169,760,000.00 USD | 0.00 USD | 0.00 USD | 195,220.00 USD |
| `7D` | `86.30` | 169,560,000.00 USD | 0.00 USD | 169,560,000.00 USD | 0.00 USD | 323,360.00 USD | 4,140.00 USD |
| `7D` | `86.50` | 169,240,000.00 USD | 0.00 USD | 169,240,000.00 USD | 0.00 USD | 0.00 USD | 4,340.00 USD |
| `7D` | `86.70` | 169,230,000.00 USD | 0.00 USD | 169,230,000.00 USD | 0.00 USD | 11,140.00 USD | 0.00 USD |
| `7D` | `86.90` | 169,220,000.00 USD | 0.00 USD | 169,220,000.00 USD | 263,340.00 USD | 309,680.00 USD | 297,340.00 USD |
| `1D` | `87.10` | 173,020,000.00 USD | 0.00 USD | 173,020,000.00 USD | 316,760.00 USD | 433,420.00 USD | 423,350.00 USD |
| `7D` | `87.10` | 168,350,000.00 USD | 0.00 USD | 168,350,000.00 USD | 0.00 USD | 5,620.00 USD | 6,820.00 USD |
| `1D` | `87.30` | 171,850,000.00 USD | 0.00 USD | 171,850,000.00 USD | 61,200.00 USD | 207,830.00 USD | 156,230.00 USD |
| `7D` | `87.30` | 168,340,000.00 USD | 0.00 USD | 168,340,000.00 USD | 0.00 USD | 204,790.00 USD | 288,100.00 USD |
| `1D` | `87.50` | 171,420,000.00 USD | 0.00 USD | 171,420,000.00 USD | 10,160.00 USD | 72,180.00 USD | 69,020.00 USD |
| `7D` | `87.50` | 167,840,000.00 USD | 0.00 USD | 167,840,000.00 USD | 24,350.00 USD | 24,850.00 USD | 0.00 USD |
| `1D` | `87.70` | 171,270,000.00 USD | 0.00 USD | 171,270,000.00 USD | 8,600.00 USD | 247,780.00 USD | 247,620.00 USD |
| `7D` | `87.70` | 167,800,000.00 USD | 0.00 USD | 167,800,000.00 USD | 0.00 USD | 290,940.00 USD | 415,730.00 USD |
| `1D` | `87.90` | 170,770,000.00 USD | 0.00 USD | 170,770,000.00 USD | 133,480.00 USD | 427,430.00 USD | 915,480.00 USD |
| `7D` | `87.90` | 167,090,000.00 USD | 0.00 USD | 167,090,000.00 USD | 0.00 USD | 307,460.00 USD | 242,310.00 USD |
| `1D` | `88.10` | 169,290,000.00 USD | 0.00 USD | 169,290,000.00 USD | 0.00 USD | 0.00 USD | 230,360.00 USD |
| `7D` | `88.10` | 166,540,000.00 USD | 0.00 USD | 166,540,000.00 USD | 0.00 USD | 0.00 USD | 12,670.00 USD |
| `1D` | `88.30` | 169,060,000.00 USD | 0.00 USD | 169,060,000.00 USD | 83,370.00 USD | 73,830.00 USD | 136,810.00 USD |
| `7D` | `88.30` | 166,530,000.00 USD | 0.00 USD | 166,530,000.00 USD | 0.00 USD | 20,610.00 USD | 331,480.00 USD |
| `1D` | `88.50` | 168,770,000.00 USD | 0.00 USD | 168,770,000.00 USD | 0.00 USD | 99,900.00 USD | 1,320.00 USD |
| `7D` | `88.50` | 166,170,000.00 USD | 0.00 USD | 166,170,000.00 USD | 0.00 USD | 0.00 USD | 3,910.00 USD |
| `1D` | `88.70` | 168,660,000.00 USD | 0.00 USD | 168,660,000.00 USD | 204,330.00 USD | 124,180.00 USD | 415,440.00 USD |
| `7D` | `88.70` | 166,170,000.00 USD | 0.00 USD | 166,170,000.00 USD | 224,230.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `88.90` | 167,920,000.00 USD | 0.00 USD | 167,920,000.00 USD | 143,140.00 USD | 62,660.00 USD | 226,460.00 USD |
| `7D` | `88.90` | 165,950,000.00 USD | 0.00 USD | 165,950,000.00 USD | 17,470.00 USD | 3,730.00 USD | 3,570.00 USD |
| `1D` | `89.10` | 167,490,000.00 USD | 0.00 USD | 167,490,000.00 USD | 160,900.00 USD | 83,520.00 USD | 11,880.00 USD |
| `7D` | `89.10` | 165,920,000.00 USD | 0.00 USD | 165,920,000.00 USD | 350,210.00 USD | 291,000.00 USD | 601,650.00 USD |
| `1D` | `89.30` | 167,230,000.00 USD | 0.00 USD | 167,230,000.00 USD | 221,290.00 USD | 284,680.00 USD | 5,050.00 USD |
| `7D` | `89.30` | 164,680,000.00 USD | 0.00 USD | 164,680,000.00 USD | 679,190.00 USD | 22,080.00 USD | 27,480.00 USD |
| `1D` | `89.50` | 166,720,000.00 USD | 0.00 USD | 166,720,000.00 USD | 4,870.00 USD | 50,620.00 USD | 278,210.00 USD |
| `7D` | `89.50` | 163,950,000.00 USD | 0.00 USD | 163,950,000.00 USD | 184,930.00 USD | 91,380.00 USD | 512,480.00 USD |
| `1D` | `89.70` | 166,390,000.00 USD | 0.00 USD | 166,390,000.00 USD | 190,910.00 USD | 107,730.00 USD | 426,480.00 USD |
| `7D` | `89.70` | 163,160,000.00 USD | 0.00 USD | 163,160,000.00 USD | 780,700.00 USD | 225,300.00 USD | 472,550.00 USD |
| `1D` | `89.90` | 165,660,000.00 USD | 0.00 USD | 165,660,000.00 USD | 301,540.00 USD | 255,100.00 USD | 381,220.00 USD |
| `7D` | `89.90` | 161,680,000.00 USD | 0.00 USD | 161,680,000.00 USD | 446,430.00 USD | 563,970.00 USD | 807,700.00 USD |
| `1D` | `90.10` | 164,720,000.00 USD | 0.00 USD | 164,720,000.00 USD | 1,210,000.00 USD | 1,030,000.00 USD | 836,810.00 USD |
| `7D` | `90.10` | 159,860,000.00 USD | 0.00 USD | 159,860,000.00 USD | 967,200.00 USD | 633,920.00 USD | 879,080.00 USD |
| `1D` | `90.30` | 161,650,000.00 USD | 0.00 USD | 161,650,000.00 USD | 773,740.00 USD | 563,210.00 USD | 477,760.00 USD |
| `7D` | `90.30` | 157,380,000.00 USD | 0.00 USD | 157,380,000.00 USD | 936,750.00 USD | 342,020.00 USD | 802,010.00 USD |
| `1D` | `90.50` | 159,830,000.00 USD | 0.00 USD | 159,830,000.00 USD | 683,680.00 USD | 538,340.00 USD | 964,440.00 USD |
| `7D` | `90.50` | 155,300,000.00 USD | 0.00 USD | 155,300,000.00 USD | 1,100,000.00 USD | 823,160.00 USD | 860,530.00 USD |
| `1D` | `90.70` | 157,650,000.00 USD | 0.00 USD | 157,650,000.00 USD | 628,630.00 USD | 803,190.00 USD | 388,680.00 USD |
| `7D` | `90.70` | 152,520,000.00 USD | 0.00 USD | 152,520,000.00 USD | 742,490.00 USD | 700,720.00 USD | 1,440,000.00 USD |
| `1D` | `90.90` | 155,830,000.00 USD | 0.00 USD | 155,830,000.00 USD | 673,680.00 USD | 420,760.00 USD | 83,650.00 USD |
| `7D` | `90.90` | 149,640,000.00 USD | 0.00 USD | 149,640,000.00 USD | 1,350,000.00 USD | 997,660.00 USD | 1,020,000.00 USD |
| `1D` | `91.10` | 154,650,000.00 USD | 0.00 USD | 154,650,000.00 USD | 436,270.00 USD | 732,110.00 USD | 474,290.00 USD |
| `7D` | `91.10` | 146,260,000.00 USD | 0.00 USD | 146,260,000.00 USD | 2,350,000.00 USD | 578,750.00 USD | 895,510.00 USD |
| `1D` | `91.30` | 153,010,000.00 USD | 0.00 USD | 153,010,000.00 USD | 150,320.00 USD | 221,290.00 USD | 448,730.00 USD |
| `7D` | `91.30` | 142,440,000.00 USD | 0.00 USD | 142,440,000.00 USD | 1,080,000.00 USD | 810,610.00 USD | 1,090,000.00 USD |
| `1D` | `91.50` | 152,180,000.00 USD | 0.00 USD | 152,180,000.00 USD | 850,930.00 USD | 781,420.00 USD | 655,960.00 USD |
| `7D` | `91.50` | 139,460,000.00 USD | 0.00 USD | 139,460,000.00 USD | 705,000.00 USD | 1,710,000.00 USD | 1,290,000.00 USD |
| `1D` | `91.70` | 149,900,000.00 USD | 0.00 USD | 149,900,000.00 USD | 268,750.00 USD | 463,180.00 USD | 1,160,000.00 USD |
| `7D` | `91.70` | 135,750,000.00 USD | 0.00 USD | 135,750,000.00 USD | 538,680.00 USD | 342,840.00 USD | 781,330.00 USD |
| `1D` | `91.90` | 148,000,000.00 USD | 0.00 USD | 148,000,000.00 USD | 1,280,000.00 USD | 813,050.00 USD | 663,410.00 USD |
| `7D` | `91.90` | 134,090,000.00 USD | 0.00 USD | 134,090,000.00 USD | 1,020,000.00 USD | 838,200.00 USD | 1,230,000.00 USD |
| `1D` | `92.10` | 145,250,000.00 USD | 0.00 USD | 145,250,000.00 USD | 2,310,000.00 USD | 2,670,000.00 USD | 565,160.00 USD |
| `7D` | `92.10` | 131,000,000.00 USD | 0.00 USD | 131,000,000.00 USD | 3,150,000.00 USD | 1,400,000.00 USD | 278,960.00 USD |
| `1D` | `92.30` | 139,700,000.00 USD | 0.00 USD | 139,700,000.00 USD | 720,590.00 USD | 799,660.00 USD | 1,410,000.00 USD |
| `7D` | `92.30` | 126,170,000.00 USD | 0.00 USD | 126,170,000.00 USD | 375,130.00 USD | 487,150.00 USD | 1,530,000.00 USD |
| `1D` | `92.50` | 136,770,000.00 USD | 0.00 USD | 136,770,000.00 USD | 1,140,000.00 USD | 703,500.00 USD | 2,340,000.00 USD |
| `7D` | `92.50` | 123,780,000.00 USD | 0.00 USD | 123,780,000.00 USD | 260,510.00 USD | 1,320,000.00 USD | 1,770,000.00 USD |
| `1D` | `92.70` | 132,580,000.00 USD | 0.00 USD | 132,580,000.00 USD | 982,240.00 USD | 1,110,000.00 USD | 1,700,000.00 USD |
| `7D` | `92.70` | 120,430,000.00 USD | 0.00 USD | 120,430,000.00 USD | 148,000.00 USD | 1,830,000.00 USD | 1,610,000.00 USD |
| `1D` | `92.90` | 128,790,000.00 USD | 0.00 USD | 128,790,000.00 USD | 3,020,000.00 USD | 1,870,000.00 USD | 2,470,000.00 USD |
| `7D` | `92.90` | 116,850,000.00 USD | 0.00 USD | 116,850,000.00 USD | 371,030.00 USD | 783,070.00 USD | 954,800.00 USD |
| `1D` | `93.10` | 121,430,000.00 USD | 0.00 USD | 121,430,000.00 USD | 2,030,000.00 USD | 3,210,000.00 USD | 1,730,000.00 USD |
| `7D` | `93.10` | 114,740,000.00 USD | 0.00 USD | 114,740,000.00 USD | 31,020.00 USD | 686,660.00 USD | 1,020,000.00 USD |
| `1D` | `93.30` | 114,460,000.00 USD | 0.00 USD | 114,460,000.00 USD | 2,250,000.00 USD | 2,580,000.00 USD | 1,250,000.00 USD |
| `7D` | `93.30` | 113,000,000.00 USD | 0.00 USD | 113,000,000.00 USD | 96,300.00 USD | 0.00 USD | 1,420,000.00 USD |
| `1D` | `93.50` | 108,370,000.00 USD | 0.00 USD | 108,370,000.00 USD | 2,930,000.00 USD | 2,280,000.00 USD | 2,260,000.00 USD |
| `7D` | `93.50` | 111,480,000.00 USD | 0.00 USD | 111,480,000.00 USD | 399,000.00 USD | 2,880,000.00 USD | 3,050,000.00 USD |
| `1D` | `93.70` | 100,910,000.00 USD | 0.00 USD | 100,910,000.00 USD | 551,230.00 USD | 3,170,000.00 USD | 867,680.00 USD |
| `7D` | `93.70` | 105,160,000.00 USD | 0.00 USD | 105,160,000.00 USD | 7,450.00 USD | 2,970,000.00 USD | 1,700,000.00 USD |
| `1D` | `93.90` | 96,310,000.00 USD | 0.00 USD | 96,310,000.00 USD | 1,590,000.00 USD | 790,210.00 USD | 1,380,000.00 USD |
| `7D` | `93.90` | 100,480,000.00 USD | 0.00 USD | 100,480,000.00 USD | 2,670,000.00 USD | 30,170.00 USD | 3,410,000.00 USD |
| `1D` | `94.10` | 92,550,000.00 USD | 0.00 USD | 92,550,000.00 USD | 545,380.00 USD | 851,000.00 USD | 2,460,000.00 USD |
| `7D` | `94.10` | 94,370,000.00 USD | 0.00 USD | 94,370,000.00 USD | 175,750.00 USD | 2,120,000.00 USD | 2,230,000.00 USD |
| `1D` | `94.30` | 88,690,000.00 USD | 0.00 USD | 88,690,000.00 USD | 2,130,000.00 USD | 1,080,000.00 USD | 371,610.00 USD |
| `7D` | `94.30` | 89,840,000.00 USD | 0.00 USD | 89,840,000.00 USD | 0.00 USD | 159,070.00 USD | 839,350.00 USD |
| `1D` | `94.50` | 85,110,000.00 USD | 0.00 USD | 85,110,000.00 USD | 795,850.00 USD | 1,250,000.00 USD | 645,220.00 USD |
| `7D` | `94.50` | 88,840,000.00 USD | 0.00 USD | 88,840,000.00 USD | 183,750.00 USD | 496,790.00 USD | 0.00 USD |
| `1D` | `94.70` | 82,420,000.00 USD | 0.00 USD | 82,420,000.00 USD | 1,360,000.00 USD | 571,830.00 USD | 399,800.00 USD |
| `7D` | `94.70` | 88,160,000.00 USD | 0.00 USD | 88,160,000.00 USD | 1,600,000.00 USD | 99,300.00 USD | 3,360,000.00 USD |
| `1D` | `94.90` | 80,080,000.00 USD | 0.00 USD | 80,080,000.00 USD | 2,720,000.00 USD | 434,700.00 USD | 1,220,000.00 USD |
| `7D` | `94.90` | 83,100,000.00 USD | 0.00 USD | 83,100,000.00 USD | 3,170,000.00 USD | 4,260,000.00 USD | 47,940.00 USD |
| `1D` | `95.10` | 75,710,000.00 USD | 0.00 USD | 75,710,000.00 USD | 2,150,000.00 USD | 1,390,000.00 USD | 27,360.00 USD |
| `7D` | `95.10` | 75,620,000.00 USD | 0.00 USD | 75,620,000.00 USD | 198,380.00 USD | 199,180.00 USD | 17,980.00 USD |
| `1D` | `95.30` | 72,150,000.00 USD | 0.00 USD | 72,150,000.00 USD | 87,330.00 USD | 494,560.00 USD | 3,370,000.00 USD |
| `7D` | `95.30` | 75,210,000.00 USD | 0.00 USD | 75,210,000.00 USD | 678,330.00 USD | 1,060,000.00 USD | 1,680,000.00 USD |
| `1D` | `95.50` | 68,200,000.00 USD | 0.00 USD | 68,200,000.00 USD | 291,230.00 USD | 1,570,000.00 USD | 1,410,000.00 USD |
| `7D` | `95.50` | 71,780,000.00 USD | 0.00 USD | 71,780,000.00 USD | 2,000,000.00 USD | 3,870,000.00 USD | 4,440,000.00 USD |
| `1D` | `95.70` | 64,930,000.00 USD | 0.00 USD | 64,930,000.00 USD | 1,710,000.00 USD | 2,150,000.00 USD | 5,390,000.00 USD |
| `7D` | `95.70` | 61,480,000.00 USD | 0.00 USD | 61,480,000.00 USD | 5,540,000.00 USD | 4,060,000.00 USD | 4,180,000.00 USD |
| `1D` | `95.90` | 55,680,000.00 USD | 0.00 USD | 55,680,000.00 USD | 997,860.00 USD | 953,770.00 USD | 1,690,000.00 USD |
| `7D` | `95.90` | 47,690,000.00 USD | 0.00 USD | 47,690,000.00 USD | 2,130,000.00 USD | 344,240.00 USD | 689,060.00 USD |
| `1D` | `96.10` | 52,040,000.00 USD | 0.00 USD | 52,040,000.00 USD | 1,770,000.00 USD | 2,040,000.00 USD | 3,220,000.00 USD |
| `7D` | `96.10` | 44,520,000.00 USD | 0.00 USD | 44,520,000.00 USD | 3,460,000.00 USD | 811,100.00 USD | 8,080,000.00 USD |
| `1D` | `96.30` | 45,010,000.00 USD | 0.00 USD | 45,010,000.00 USD | 4,480,000.00 USD | 5,140,000.00 USD | 848,070.00 USD |
| `7D` | `96.30` | 32,170,000.00 USD | 0.00 USD | 32,170,000.00 USD | 2,740,000.00 USD | 1,700,000.00 USD | 6,490,000.00 USD |
| `1D` | `96.50` | 34,540,000.00 USD | 0.00 USD | 34,540,000.00 USD | 2,840,000.00 USD | 1,260,000.00 USD | 3,870,000.00 USD |
| `7D` | `96.50` | 21,250,000.00 USD | 0.00 USD | 21,250,000.00 USD | 0.00 USD | 0.00 USD | 24,800.00 USD |
| `1D` | `96.70` | 26,580,000.00 USD | 0.00 USD | 26,580,000.00 USD | 1,420,000.00 USD | 2,230,000.00 USD | 956,820.00 USD |
| `7D` | `96.70` | 21,220,000.00 USD | 0.00 USD | 21,220,000.00 USD | 0.00 USD | 14,450.00 USD | 2,350,000.00 USD |
| `1D` | `96.90` | 21,970,000.00 USD | 0.00 USD | 21,970,000.00 USD | 0.00 USD | 1,360,000.00 USD | 4,910,000.00 USD |
| `7D` | `96.90` | 18,860,000.00 USD | 0.00 USD | 18,860,000.00 USD | 0.00 USD | 2,310,000.00 USD | 1,210,000.00 USD |
| `1D` | `97.10` | 15,700,000.00 USD | 0.00 USD | 15,700,000.00 USD | 3,190,000.00 USD | 2,570,000.00 USD | 1,930,000.00 USD |
| `7D` | `97.10` | 15,340,000.00 USD | 0.00 USD | 15,340,000.00 USD | 0.00 USD | 1,350,000.00 USD | 4,290,000.00 USD |
| `1D` | `97.30` | 8,010,000.00 USD | 0.00 USD | 8,010,000.00 USD | 1,030,000.00 USD | 1,270,000.00 USD | 873,300.00 USD |
| `7D` | `97.30` | 9,710,000.00 USD | 0.00 USD | 9,710,000.00 USD | 0.00 USD | 16,130.00 USD | 0.00 USD |
| `1D` | `97.50` | 4,840,000.00 USD | 0.00 USD | 4,840,000.00 USD | 534,370.00 USD | 1,320,000.00 USD | 1,760,000.00 USD |
| `7D` | `97.50` | 9,690,000.00 USD | 0.00 USD | 9,690,000.00 USD | 0.00 USD | 110,360.00 USD | 0.00 USD |
| `1D` | `97.70` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 1,230,000.00 USD |
| `7D` | `97.70` | 9,580,000.00 USD | 0.00 USD | 9,580,000.00 USD | 3,880,000.00 USD | 1,750,000.00 USD | 3,950,000.00 USD |
| `1D` | `97.90` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 2,400,000.00 USD | 48,560.00 USD | 0.00 USD |
| `1D` | `97.90` | 4,900,000.00 USD | 4,900,000.00 USD | 0.00 USD | 2,400,000.00 USD | 48,560.00 USD | 0.00 USD |
| `7D` | `97.90` | 13,610,000.00 USD | 13,610,000.00 USD | 0.00 USD | 11,920,000.00 USD | 1,690,000.00 USD | 0.00 USD |
| `7D` | `97.90` | 27,210,000.00 USD | 27,210,000.00 USD | 0.00 USD | 11,920,000.00 USD | 1,690,000.00 USD | 0.00 USD |
| `1D` | `98.10` | 7,930,000.00 USD | 7,930,000.00 USD | 0.00 USD | 215,860.00 USD | 0.00 USD | 2,810,000.00 USD |
| `7D` | `98.10` | 37,090,000.00 USD | 37,090,000.00 USD | 0.00 USD | 9,870,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `98.30` | 15,990,000.00 USD | 15,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 20,470.00 USD | 6,060,000.00 USD |
| `7D` | `98.30` | 49,490,000.00 USD | 49,490,000.00 USD | 0.00 USD | 1,640,000.00 USD | 5,130,000.00 USD | 5,630,000.00 USD |
| `1D` | `98.50` | 26,350,000.00 USD | 26,350,000.00 USD | 0.00 USD | 295,480.00 USD | 3,460,000.00 USD | 6,600,000.00 USD |
| `7D` | `98.50` | 59,620,000.00 USD | 59,620,000.00 USD | 0.00 USD | 1,320,000.00 USD | 6,930,000.00 USD | 1,880,000.00 USD |
| `1D` | `98.70` | 42,010,000.00 USD | 42,010,000.00 USD | 0.00 USD | 980,300.00 USD | 5,100,000.00 USD | 9,580,000.00 USD |
| `7D` | `98.70` | 64,610,000.00 USD | 64,610,000.00 USD | 0.00 USD | 742,060.00 USD | 1,370,000.00 USD | 2,880,000.00 USD |
| `1D` | `98.90` | 49,550,000.00 USD | 49,550,000.00 USD | 0.00 USD | 635,820.00 USD | 2,590,000.00 USD | 4,320,000.00 USD |
| `7D` | `98.90` | 69,460,000.00 USD | 69,460,000.00 USD | 0.00 USD | 57,310.00 USD | 1,660,000.00 USD | 3,120,000.00 USD |
| `1D` | `99.10` | 59,130,000.00 USD | 59,130,000.00 USD | 0.00 USD | 1,710,000.00 USD | 2,910,000.00 USD | 4,950,000.00 USD |
| `7D` | `99.10` | 75,860,000.00 USD | 75,860,000.00 USD | 0.00 USD | 179,190.00 USD | 2,070,000.00 USD | 4,150,000.00 USD |
| `1D` | `99.30` | 68,240,000.00 USD | 68,240,000.00 USD | 0.00 USD | 3,530,000.00 USD | 3,300,000.00 USD | 2,270,000.00 USD |
| `7D` | `99.30` | 82,610,000.00 USD | 82,610,000.00 USD | 0.00 USD | 798,000.00 USD | 3,060,000.00 USD | 2,890,000.00 USD |
| `1D` | `99.50` | 73,520,000.00 USD | 73,520,000.00 USD | 0.00 USD | 1,380,000.00 USD | 3,290,000.00 USD | 619,030.00 USD |
| `7D` | `99.50` | 86,850,000.00 USD | 86,850,000.00 USD | 0.00 USD | 2,240,000.00 USD | 1,490,000.00 USD | 504,960.00 USD |
| `1D` | `99.70` | 96,380,000.00 USD | 96,380,000.00 USD | 0.00 USD | 4,390,000.00 USD | 7,320,000.00 USD | 11,140,000.00 USD |
| `7D` | `99.70` | 90,560,000.00 USD | 90,560,000.00 USD | 0.00 USD | 0.00 USD | 2,490,000.00 USD | 1,220,000.00 USD |
| `1D` | `99.90` | 104,390,000.00 USD | 104,390,000.00 USD | 0.00 USD | 555,210.00 USD | 1,500,000.00 USD | 5,960,000.00 USD |
| `7D` | `99.90` | 98,700,000.00 USD | 98,700,000.00 USD | 0.00 USD | 2,860,000.00 USD | 1,420,000.00 USD | 3,850,000.00 USD |
| `1D` | `100.10` | 109,650,000.00 USD | 109,650,000.00 USD | 0.00 USD | 2,030,000.00 USD | 2,360,000.00 USD | 877,830.00 USD |
| `7D` | `100.10` | 104,480,000.00 USD | 104,480,000.00 USD | 0.00 USD | 48,160.00 USD | 1,210,000.00 USD | 4,520,000.00 USD |
| `1D` | `100.30` | 114,780,000.00 USD | 114,780,000.00 USD | 0.00 USD | 300,700.00 USD | 2,120,000.00 USD | 2,710,000.00 USD |
| `7D` | `100.30` | 108,090,000.00 USD | 108,090,000.00 USD | 0.00 USD | 883,050.00 USD | 1,600,000.00 USD | 1,130,000.00 USD |
| `1D` | `100.50` | 122,430,000.00 USD | 122,430,000.00 USD | 0.00 USD | 2,200,000.00 USD | 1,260,000.00 USD | 4,200,000.00 USD |
| `7D` | `100.50` | 116,550,000.00 USD | 116,550,000.00 USD | 0.00 USD | 2,640,000.00 USD | 765,300.00 USD | 5,050,000.00 USD |
| `1D` | `100.70` | 129,750,000.00 USD | 129,750,000.00 USD | 0.00 USD | 1,940,000.00 USD | 2,250,000.00 USD | 3,130,000.00 USD |
| `7D` | `100.70` | 118,980,000.00 USD | 118,980,000.00 USD | 0.00 USD | 504,370.00 USD | 1,900,000.00 USD | 23,970.00 USD |
| `1D` | `100.90` | 135,700,000.00 USD | 135,700,000.00 USD | 0.00 USD | 1,760,000.00 USD | 2,410,000.00 USD | 1,790,000.00 USD |
| `7D` | `100.90` | 132,080,000.00 USD | 132,080,000.00 USD | 0.00 USD | 3,480,000.00 USD | 3,730,000.00 USD | 5,890,000.00 USD |
| `1D` | `101.10` | 149,570,000.00 USD | 149,570,000.00 USD | 0.00 USD | 8,660,000.00 USD | 2,680,000.00 USD | 2,520,000.00 USD |
| `7D` | `101.10` | 141,850,000.00 USD | 141,850,000.00 USD | 0.00 USD | 3,020,000.00 USD | 3,990,000.00 USD | 2,760,000.00 USD |
| `1D` | `101.30` | 159,770,000.00 USD | 159,770,000.00 USD | 0.00 USD | 3,460,000.00 USD | 3,950,000.00 USD | 2,800,000.00 USD |
| `7D` | `101.30` | 163,230,000.00 USD | 163,230,000.00 USD | 0.00 USD | 7,710,000.00 USD | 4,690,000.00 USD | 8,980,000.00 USD |
| `1D` | `101.50` | 175,920,000.00 USD | 175,920,000.00 USD | 0.00 USD | 3,050,000.00 USD | 3,960,000.00 USD | 9,140,000.00 USD |
| `7D` | `101.50` | 178,500,000.00 USD | 178,500,000.00 USD | 0.00 USD | 2,950,000.00 USD | 738,480.00 USD | 11,580,000.00 USD |
| `1D` | `101.70` | 185,620,000.00 USD | 185,620,000.00 USD | 0.00 USD | 2,320,000.00 USD | 703,520.00 USD | 6,670,000.00 USD |
| `7D` | `101.70` | 188,480,000.00 USD | 188,480,000.00 USD | 0.00 USD | 2,950,000.00 USD | 484,140.00 USD | 6,550,000.00 USD |
| `1D` | `101.90` | 191,190,000.00 USD | 191,190,000.00 USD | 0.00 USD | 2,100,000.00 USD | 823,320.00 USD | 2,650,000.00 USD |
| `7D` | `101.90` | 197,180,000.00 USD | 197,180,000.00 USD | 0.00 USD | 3,710,000.00 USD | 867,880.00 USD | 4,120,000.00 USD |
| `1D` | `102.10` | 197,200,000.00 USD | 197,200,000.00 USD | 0.00 USD | 2,830,000.00 USD | 1,270,000.00 USD | 1,900,000.00 USD |
| `7D` | `102.10` | 202,830,000.00 USD | 202,830,000.00 USD | 0.00 USD | 1,470,000.00 USD | 159,070.00 USD | 4,030,000.00 USD |
| `1D` | `102.30` | 202,100,000.00 USD | 202,100,000.00 USD | 0.00 USD | 1,650,000.00 USD | 1,450,000.00 USD | 1,800,000.00 USD |
| `7D` | `102.30` | 208,890,000.00 USD | 208,890,000.00 USD | 0.00 USD | 2,700,000.00 USD | 807,930.00 USD | 2,550,000.00 USD |
| `1D` | `102.50` | 206,420,000.00 USD | 206,420,000.00 USD | 0.00 USD | 1,510,000.00 USD | 785,070.00 USD | 2,030,000.00 USD |
| `7D` | `102.50` | 212,540,000.00 USD | 212,540,000.00 USD | 0.00 USD | 1,240,000.00 USD | 1,280,000.00 USD | 1,130,000.00 USD |
| `1D` | `102.70` | 208,310,000.00 USD | 208,310,000.00 USD | 0.00 USD | 1,110,000.00 USD | 661,840.00 USD | 121,020.00 USD |
| `7D` | `102.70` | 213,340,000.00 USD | 213,340,000.00 USD | 0.00 USD | 766,460.00 USD | 14,010.00 USD | 16,660.00 USD |
| `1D` | `102.90` | 212,850,000.00 USD | 212,850,000.00 USD | 0.00 USD | 1,510,000.00 USD | 1,530,000.00 USD | 1,490,000.00 USD |
| `7D` | `102.90` | 234,630,000.00 USD | 234,630,000.00 USD | 0.00 USD | 17,210,000.00 USD | 294,050.00 USD | 3,780,000.00 USD |
| `1D` | `103.10` | 217,800,000.00 USD | 217,800,000.00 USD | 0.00 USD | 2,380,000.00 USD | 1,360,000.00 USD | 1,220,000.00 USD |
| `7D` | `103.10` | 240,860,000.00 USD | 240,860,000.00 USD | 0.00 USD | 4,750,000.00 USD | 140,720.00 USD | 1,340,000.00 USD |
| `1D` | `103.30` | 219,620,000.00 USD | 219,620,000.00 USD | 0.00 USD | 334,720.00 USD | 717,010.00 USD | 769,510.00 USD |
| `7D` | `103.30` | 256,540,000.00 USD | 256,540,000.00 USD | 0.00 USD | 15,130,000.00 USD | 133,780.00 USD | 417,110.00 USD |
| `1D` | `103.50` | 226,210,000.00 USD | 226,210,000.00 USD | 0.00 USD | 1,770,000.00 USD | 1,090,000.00 USD | 3,730,000.00 USD |
| `7D` | `103.50` | 278,950,000.00 USD | 278,950,000.00 USD | 0.00 USD | 13,780,000.00 USD | 1,770,000.00 USD | 6,860,000.00 USD |
| `1D` | `103.70` | 231,420,000.00 USD | 231,420,000.00 USD | 0.00 USD | 1,610,000.00 USD | 971,510.00 USD | 2,620,000.00 USD |
| `7D` | `103.70` | 291,170,000.00 USD | 291,170,000.00 USD | 0.00 USD | 8,190,000.00 USD | 1,320,000.00 USD | 2,710,000.00 USD |
| `1D` | `103.90` | 237,230,000.00 USD | 237,230,000.00 USD | 0.00 USD | 2,080,000.00 USD | 2,200,000.00 USD | 1,530,000.00 USD |
| `7D` | `103.90` | 309,210,000.00 USD | 309,210,000.00 USD | 0.00 USD | 9,120,000.00 USD | 2,880,000.00 USD | 6,040,000.00 USD |
| `1D` | `104.10` | 244,330,000.00 USD | 244,330,000.00 USD | 0.00 USD | 2,850,000.00 USD | 1,270,000.00 USD | 2,990,000.00 USD |
| `7D` | `104.10` | 338,140,000.00 USD | 338,140,000.00 USD | 0.00 USD | 11,570,000.00 USD | 8,350,000.00 USD | 9,010,000.00 USD |
| `1D` | `104.30` | 248,240,000.00 USD | 248,240,000.00 USD | 0.00 USD | 1,400,000.00 USD | 1,440,000.00 USD | 1,070,000.00 USD |
| `7D` | `104.30` | 359,720,000.00 USD | 359,720,000.00 USD | 0.00 USD | 7,320,000.00 USD | 6,380,000.00 USD | 7,870,000.00 USD |
| `1D` | `104.50` | 252,340,000.00 USD | 252,340,000.00 USD | 0.00 USD | 1,430,000.00 USD | 1,220,000.00 USD | 1,450,000.00 USD |
| `7D` | `104.50` | 371,740,000.00 USD | 371,740,000.00 USD | 0.00 USD | 4,410,000.00 USD | 2,350,000.00 USD | 5,270,000.00 USD |
| `1D` | `104.70` | 258,130,000.00 USD | 258,130,000.00 USD | 0.00 USD | 1,720,000.00 USD | 982,920.00 USD | 3,090,000.00 USD |
| `7D` | `104.70` | 391,930,000.00 USD | 391,930,000.00 USD | 0.00 USD | 6,680,000.00 USD | 4,660,000.00 USD | 8,860,000.00 USD |
| `1D` | `104.90` | 259,610,000.00 USD | 259,610,000.00 USD | 0.00 USD | 486,940.00 USD | 283,560.00 USD | 706,500.00 USD |
| `7D` | `104.90` | 412,800,000.00 USD | 412,800,000.00 USD | 0.00 USD | 5,970,000.00 USD | 5,350,000.00 USD | 9,550,000.00 USD |
| `1D` | `105.10` | 261,450,000.00 USD | 261,450,000.00 USD | 0.00 USD | 299,230.00 USD | 436,680.00 USD | 1,100,000.00 USD |
| `7D` | `105.10` | 425,610,000.00 USD | 425,610,000.00 USD | 0.00 USD | 5,580,000.00 USD | 4,400,000.00 USD | 2,830,000.00 USD |
| `1D` | `105.30` | 261,640,000.00 USD | 261,640,000.00 USD | 0.00 USD | 94,380.00 USD | 96,460.00 USD | 1,240.00 USD |
| `7D` | `105.30` | 429,950,000.00 USD | 429,950,000.00 USD | 0.00 USD | 2,410,000.00 USD | 1,310,000.00 USD | 623,960.00 USD |
| `1D` | `105.50` | 262,250,000.00 USD | 262,250,000.00 USD | 0.00 USD | 245,610.00 USD | 180,000.00 USD | 186,400.00 USD |
| `7D` | `105.50` | 448,330,000.00 USD | 448,330,000.00 USD | 0.00 USD | 5,600,000.00 USD | 5,850,000.00 USD | 6,930,000.00 USD |
| `1D` | `105.70` | 262,470,000.00 USD | 262,470,000.00 USD | 0.00 USD | 65,040.00 USD | 150,210.00 USD | 3,480.00 USD |
| `7D` | `105.70` | 460,070,000.00 USD | 460,070,000.00 USD | 0.00 USD | 3,430,000.00 USD | 3,740,000.00 USD | 4,570,000.00 USD |
| `1D` | `105.90` | 263,520,000.00 USD | 263,520,000.00 USD | 0.00 USD | 171,160.00 USD | 683,690.00 USD | 193,630.00 USD |
| `7D` | `105.90` | 468,960,000.00 USD | 468,960,000.00 USD | 0.00 USD | 3,110,000.00 USD | 1,880,000.00 USD | 3,900,000.00 USD |
| `1D` | `106.10` | 264,910,000.00 USD | 264,910,000.00 USD | 0.00 USD | 706,860.00 USD | 457,510.00 USD | 226,230.00 USD |
| `7D` | `106.10` | 479,560,000.00 USD | 479,560,000.00 USD | 0.00 USD | 4,910,000.00 USD | 2,870,000.00 USD | 2,820,000.00 USD |
| `1D` | `106.30` | 266,060,000.00 USD | 266,060,000.00 USD | 0.00 USD | 281,270.00 USD | 484,380.00 USD | 391,880.00 USD |
| `7D` | `106.30` | 487,960,000.00 USD | 487,960,000.00 USD | 0.00 USD | 3,400,000.00 USD | 2,850,000.00 USD | 2,150,000.00 USD |
| `1D` | `106.50` | 266,750,000.00 USD | 266,750,000.00 USD | 0.00 USD | 229,790.00 USD | 216,810.00 USD | 239,170.00 USD |
| `7D` | `106.50` | 492,670,000.00 USD | 492,670,000.00 USD | 0.00 USD | 1,520,000.00 USD | 1,440,000.00 USD | 1,750,000.00 USD |
| `1D` | `106.70` | 268,880,000.00 USD | 268,880,000.00 USD | 0.00 USD | 565,590.00 USD | 249,950.00 USD | 1,320,000.00 USD |
| `7D` | `106.70` | 500,760,000.00 USD | 500,760,000.00 USD | 0.00 USD | 1,820,000.00 USD | 2,330,000.00 USD | 3,940,000.00 USD |
| `1D` | `106.90` | 269,350,000.00 USD | 269,350,000.00 USD | 0.00 USD | 10,160.00 USD | 156,020.00 USD | 305,180.00 USD |
| `7D` | `106.90` | 505,820,000.00 USD | 505,820,000.00 USD | 0.00 USD | 789,400.00 USD | 1,150,000.00 USD | 3,120,000.00 USD |
| `1D` | `107.10` | 270,400,000.00 USD | 270,400,000.00 USD | 0.00 USD | 97,170.00 USD | 366,280.00 USD | 580,410.00 USD |
| `7D` | `107.10` | 509,930,000.00 USD | 509,930,000.00 USD | 0.00 USD | 1,630,000.00 USD | 799,480.00 USD | 1,680,000.00 USD |
| `1D` | `107.30` | 270,760,000.00 USD | 270,760,000.00 USD | 0.00 USD | 82,550.00 USD | 174,420.00 USD | 110,290.00 USD |
| `7D` | `107.30` | 510,380,000.00 USD | 510,380,000.00 USD | 0.00 USD | 0.00 USD | 451,690.00 USD | 0.00 USD |
| `1D` | `107.50` | 271,870,000.00 USD | 271,870,000.00 USD | 0.00 USD | 50,930.00 USD | 253,000.00 USD | 805,190.00 USD |
| `7D` | `107.50` | 511,620,000.00 USD | 511,620,000.00 USD | 0.00 USD | 5,920.00 USD | 286,950.00 USD | 946,020.00 USD |
| `1D` | `107.70` | 272,100,000.00 USD | 272,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 230,360.00 USD |
| `7D` | `107.70` | 512,600,000.00 USD | 512,600,000.00 USD | 0.00 USD | 523,660.00 USD | 10,400.00 USD | 444,980.00 USD |
| `1D` | `107.90` | 272,400,000.00 USD | 272,400,000.00 USD | 0.00 USD | 83,370.00 USD | 73,830.00 USD | 136,810.00 USD |
| `7D` | `107.90` | 513,120,000.00 USD | 513,120,000.00 USD | 0.00 USD | 173,590.00 USD | 20,610.00 USD | 331,480.00 USD |
| `1D` | `108.10` | 272,500,000.00 USD | 272,500,000.00 USD | 0.00 USD | 0.00 USD | 99,900.00 USD | 1,320.00 USD |
| `7D` | `108.10` | 513,380,000.00 USD | 513,380,000.00 USD | 0.00 USD | 5,950.00 USD | 248,110.00 USD | 7,130.00 USD |
| `1D` | `108.30` | 272,530,000.00 USD | 272,530,000.00 USD | 0.00 USD | 33,880.00 USD | 1,950.00 USD | 0.00 USD |
| `7D` | `108.30` | 514,510,000.00 USD | 514,510,000.00 USD | 0.00 USD | 303,300.00 USD | 464,990.00 USD | 359,500.00 USD |
| `1D` | `108.50` | 273,230,000.00 USD | 273,230,000.00 USD | 0.00 USD | 163,220.00 USD | 122,230.00 USD | 413,910.00 USD |
| `7D` | `108.50` | 514,910,000.00 USD | 514,910,000.00 USD | 0.00 USD | 395,570.00 USD | 3,960.00 USD | 2,900.00 USD |
| `1D` | `108.60` | 273,350,000.00 USD | 273,350,000.00 USD | 0.00 USD | 118,190.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `108.70` | 516,790,000.00 USD | 516,790,000.00 USD | 0.00 USD | 557,190.00 USD | 529,990.00 USD | 792,670.00 USD |
| `7D` | `108.90` | 518,230,000.00 USD | 518,230,000.00 USD | 0.00 USD | 363,550.00 USD | 494,000.00 USD | 580,220.00 USD |
| `7D` | `109.10` | 519,060,000.00 USD | 519,060,000.00 USD | 0.00 USD | 289,830.00 USD | 185,250.00 USD | 354,460.00 USD |
| `7D` | `109.30` | 520,220,000.00 USD | 520,220,000.00 USD | 0.00 USD | 503,000.00 USD | 91,380.00 USD | 569,620.00 USD |
| `7D` | `109.50` | 520,460,000.00 USD | 520,460,000.00 USD | 0.00 USD | 230,320.00 USD | 4,290.00 USD | 5,670.00 USD |
| `7D` | `109.70` | 521,650,000.00 USD | 521,650,000.00 USD | 0.00 USD | 550,380.00 USD | 185,990.00 USD | 444,420.00 USD |
| `7D` | `109.90` | 523,450,000.00 USD | 523,450,000.00 USD | 0.00 USD | 446,430.00 USD | 547,840.00 USD | 807,700.00 USD |
| `7D` | `110.10` | 525,820,000.00 USD | 525,820,000.00 USD | 0.00 USD | 967,200.00 USD | 531,910.00 USD | 868,690.00 USD |
| `7D` | `110.30` | 527,900,000.00 USD | 527,900,000.00 USD | 0.00 USD | 936,750.00 USD | 342,020.00 USD | 802,010.00 USD |
| `7D` | `110.50` | 528,380,000.00 USD | 528,380,000.00 USD | 0.00 USD | 246,210.00 USD | 10,300.00 USD | 225,600.00 USD |
| `7D` | `110.70` | 530,570,000.00 USD | 530,570,000.00 USD | 0.00 USD | 793,510.00 USD | 765,020.00 USD | 634,930.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `5.71B` | Total OI Tokens: `58,238,413.5 SOL`
  * 1h OI Change: `-0.30%` | 4h OI Change: `-0.94%` | 24h OI Change: `-10.82%`
  * Exchange Breakdown: Binance=`986.64M` | Bybit=`632.34M` | OKX=`395.86M` | Hyperliquid=`530.23M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-146.13K` | Last 24h: `286.77K` | Last 3d: `1.17M` | Last 7d: `2.35M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0045%` | **USDT OKX** | `-0.0285%` |
| **USDT Bybit** | `-0.0145%` | **USDT KuCoin** | `-0.0064%` |
| **USDT MEXC** | `0.0045%` | **USDT BingX** | `0.0046%` |
| **USDT Gate** | `-0.0114%` | **USDT Bitget** | `-0.0069%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `SOL` | `42.02%` | `57.98%` | `0.72` | 88,590,000.00 USD |
| `15M` | `Binance` | `44.43%` | `55.57%` | `0.80` | 22,130,000.00 USD |
| `15M` | `OKX` | `47.18%` | `52.82%` | `0.89` | 18,840,000.00 USD |
| `15M` | `Bybit` | `45.36%` | `54.64%` | `0.83` | 10,160,000.00 USD |
| `15M` | `KuCoin` | `44.91%` | `55.09%` | `0.82` | 368,140.00 USD |
| `15M` | `Gate` | `60.48%` | `39.52%` | `1.53` | 5,930,000.00 USD |
| `15M` | `Bitget` | `23.89%` | `76.11%` | `0.31` | 4,990,000.00 USD |
| `15M` | `BingX` | `37.14%` | `62.86%` | `0.59` | 4,250,000.00 USD |
| `15M` | `MEXC` | `18.72%` | `81.28%` | `0.23` | 10,200,000.00 USD |
| `15M` | `Bitunix` | `43.36%` | `56.64%` | `0.77` | 5,880,000.00 USD |
| `15M` | `Hyperliquid` | `42.78%` | `57.22%` | `0.75` | 2,730,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `37.87%` | `62.13%` | `0.61` | 601,950.00 USD |
| `15M` | `Crypto.com` | `49.63%` | `50.37%` | `0.99` | 126,740.00 USD |
| `15M` | `WhiteBIT` | `99.09%` | `0.91%` | `108.89` | 670,570.00 USD |
| `15M` | `HTX` | `39.96%` | `60.04%` | `0.67` | 132,860.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `34.55%` | `65.45%` | `0.53` | 671,070.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `55.79%` | `44.21%` | `1.26` | 913,800.00 USD |
| `15M` | `Whale Positions` | `44.43%` | `55.57%` | `0.80` | 22,130,000.00 USD |
| `15M` | `Global Accounts` | `42.02%` | `57.98%` | `0.72` | 88,590,000.00 USD |
| `1H` | `SOL` | `53.08%` | `46.92%` | `1.13` | 100,150,000.00 USD |
| `1H` | `Binance` | `57.12%` | `42.88%` | `1.33` | 30,730,000.00 USD |
| `1H` | `OKX` | `48.8%` | `51.2%` | `0.95` | 14,920,000.00 USD |
| `1H` | `Bybit` | `54.81%` | `45.19%` | `1.21` | 13,190,000.00 USD |
| `1H` | `KuCoin` | `49.01%` | `50.99%` | `0.96` | 1,130,000.00 USD |
| `1H` | `Gate` | `60.85%` | `39.15%` | `1.55` | 5,370,000.00 USD |
| `1H` | `Bitget` | `54.41%` | `45.59%` | `1.19` | 6,410,000.00 USD |
| `1H` | `BingX` | `10.52%` | `89.48%` | `0.12` | 3,710,000.00 USD |
| `1H` | `MEXC` | `52.31%` | `47.69%` | `1.10` | 17,010,000.00 USD |
| `1H` | `Bitunix` | `54.17%` | `45.83%` | `1.18` | 3,340,000.00 USD |
| `1H` | `Hyperliquid` | `45.57%` | `54.43%` | `0.84` | 1,980,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `75.62%` | `24.38%` | `3.10` | 602,030.00 USD |
| `1H` | `Crypto.com` | `62.52%` | `37.48%` | `1.67` | 160,870.00 USD |
| `1H` | `WhiteBIT` | `91.32%` | `8.68%` | `10.52` | 1,030,000.00 USD |
| `1H` | `HTX` | `85.04%` | `14.96%` | `5.68` | 60,790.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `46.9%` | `53.1%` | `0.88` | 413,440.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `49.14%` | `50.86%` | `0.97` | 100,450.00 USD |
| `1H` | `Whale Positions` | `57.12%` | `42.88%` | `1.33` | 30,730,000.00 USD |
| `1H` | `Global Accounts` | `53.08%` | `46.92%` | `1.13` | 100,150,000.00 USD |
| `4H` | `SOL` | `52.19%` | `47.81%` | `1.09` | 1,330,000,000.00 USD |
| `4H` | `Binance` | `52.87%` | `47.13%` | `1.12` | 422,070,000.00 USD |
| `4H` | `OKX` | `56.16%` | `43.84%` | `1.28` | 265,310,000.00 USD |
| `4H` | `Bybit` | `51.6%` | `48.4%` | `1.07` | 137,610,000.00 USD |
| `4H` | `KuCoin` | `53.98%` | `46.02%` | `1.17` | 13,320,000.00 USD |
| `4H` | `Gate` | `50.86%` | `49.14%` | `1.04` | 87,490,000.00 USD |
| `4H` | `Bitget` | `52.68%` | `47.32%` | `1.11` | 52,010,000.00 USD |
| `4H` | `BingX` | `49.31%` | `50.69%` | `0.97` | 51,350,000.00 USD |
| `4H` | `MEXC` | `40.78%` | `59.22%` | `0.69` | 110,400,000.00 USD |
| `4H` | `Bitunix` | `50.29%` | `49.71%` | `1.01` | 74,850,000.00 USD |
| `4H` | `Hyperliquid` | `50.89%` | `49.11%` | `1.04` | 63,520,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `51.18%` | `48.82%` | `1.05` | 9,420,000.00 USD |
| `4H` | `Crypto.com` | `54.31%` | `45.69%` | `1.19` | 2,170,000.00 USD |
| `4H` | `WhiteBIT` | `83.15%` | `16.85%` | `4.93` | 13,750,000.00 USD |
| `4H` | `HTX` | `60.02%` | `39.98%` | `1.50` | 2,590,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `34.53%` | `65.47%` | `0.53` | 669,560.00 USD |
| `4H` | `Aster` | `55.87%` | `44.13%` | `1.27` | 12,100,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `49.9%` | `50.1%` | `1.00` | 15,610,000.00 USD |
| `4H` | `Whale Positions` | `52.87%` | `47.13%` | `1.12` | 422,070,000.00 USD |
| `4H` | `Global Accounts` | `52.19%` | `47.81%` | `1.09` | 1,330,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `97.05` | `97.07` | `97.05` | `97.23` | `96.88` | 23,273,914.74 USD | 12,919,268.61 USD | 10,354,646.13 USD | 2,564,622.48 USD | `+11.02%` | `2B / 3S` |
| `0:00 UTC` | `97.00` | `96.93` | `97.00` | `97.28` | `96.72` | 29,456,364.14 USD | 16,744,830.08 USD | 12,711,534.06 USD | 4,033,296.02 USD | `+13.69%` | `9B / 4S` |
| `5:00 UTC` | `97.16` | `97.32` | `97.16` | `97.62` | `97.06` | 19,813,374.49 USD | 9,462,479.38 USD | 10,350,895.11 USD | -888,415.74 USD | `-4.48%` | `5B / 3S` |
| `0:00 UTC` | `97.27` | `97.32` | `97.27` | `97.50` | `97.16` | 16,828,074.52 USD | 7,221,424.98 USD | 9,606,649.54 USD | -2,385,224.56 USD | `-14.17%` | `3B / 6S` |
| `5:00 UTC` | `97.34` | `97.32` | `97.34` | `97.41` | `97.22` | 11,924,438.31 USD | 5,221,368.03 USD | 6,703,070.27 USD | -1,481,702.24 USD | `-12.43%` | `0B / 0S` |
| `0:00 UTC` | `97.75` | `97.66` | `97.75` | `98.00` | `97.20` | 26,397,725.62 USD | 14,040,862.52 USD | 12,356,863.09 USD | 1,683,999.43 USD | `+6.38%` | `10B / 3S` |
| `5:00 UTC` | `98.00` | `97.90` | `98.00` | `98.06` | `97.68` | 15,892,962.27 USD | 7,229,090.33 USD | 8,663,871.94 USD | -1,434,781.61 USD | `-9.03%` | `2B / 4S` |
| `0:00 UTC` | `98.22` | `98.16` | `98.22` | `98.35` | `97.88` | 18,936,666.93 USD | 8,858,429.68 USD | 10,078,237.25 USD | -1,219,807.57 USD | `-6.44%` | `5B / 6S` |
| `5:00 UTC` | `98.05` | `98.14` | `98.05` | `98.55` | `97.84` | 22,589,286.35 USD | 8,455,263.03 USD | 14,134,023.31 USD | -5,678,760.28 USD | `-25.14%` | `6B / 22S` |
| `0:00 UTC` | `98.00` | `98.00` | `98.00` | `98.06` | `97.94` | 529,794.69 USD | 493,313.42 USD | 36,481.26 USD | 456,832.16 USD | `+86.23%` | `6B / 0S` |

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
| `5m` | 361,000.00 USD | -2,620,000.00 USD | **`DISTRIBUTION`** |
| `15m` | 1,020,000.00 USD | 550,230.00 USD | **`ACCUMULATION`** |
| `30m` | 1,310,000.00 USD | -1,710,000.00 USD | **`DISTRIBUTION`** |
| `1h` | 5,550,000.00 USD | 460,380.00 USD | **`ACCUMULATION`** |
| `2h` | 5,960,000.00 USD | 10,400,000.00 USD | **`ACCUMULATION`** |
| `4h` | 8,820,000.00 USD | 59,180,000.00 USD | **`ACCUMULATION`** |
| `6h` | 9,830,000.00 USD | -40,640,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -21,760,000.00 USD | -287,100,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -58,150,000.00 USD | -347,980,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -34,670,000.00 USD | -398,240,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 32,830,000.00 USD | -660,860,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -69,590.00 USD | -2,170,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+361.00K` | 15m=`+1.02M` | 1h=`+5.55M` | 24h=`-34.67M`
* Futures Capital Netflows: 5m=`-2.62M` | 15m=`+550.23K` | 1h=`+460.38K` | 24h=`-398.24M`
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
  * `2026-10-30 11:03:56 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:28:56 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:27:56 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:27:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 11:27:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:29:56 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:29:56 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:29:56 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `94.45` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `93.20` (Risk Distance: `1.25` pts)
  * +2.5R Take Profit: `97.58`
  * Mathematical Lot Sizing: **`7.97 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `97.70` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `98.95` (Risk Distance: `1.25` pts)
  * +2.5R Take Profit: `94.57`
  * Mathematical Lot Sizing: **`7.97 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`98.65`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
