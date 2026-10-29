# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAGEUR
**Canonical Key**: `XAGEUR` | **Broker Instrument**: `XAGEUR.pi` | **Asset Class**: `Forex Cross`
**Timestamp**: `2026-10-30 01:39:06 IST` (`2026-10-29 20:09:06 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `52.24` | **Live Ask Quote**: `52.28` | **Mid Price**: `52.26`
- **Spread Points**: `36.00` | **Spread BPS**: `6.89 bps` (Charter Threshold: `5.00 bps`)
- **Gate 1 Clearance**: **`SPREAD_DISQUALIFIED`** | **Execution Posture**: `DISQUALIFIED` | **Order Type Allowed**: `NONE`
- **True Broker Contract Specifications**:
  * Contract Size: `5,000.0` | Digits: `3` | Point: `0.001`
  * Point Value (1.0 Lot): `5.00 USD` | Point Value (0.01 Lot): `0.0500 USD`
  * Allowed Lot Sizing: Min Lot=`0.01` | Step Lot=`0.01` | Max Lot=`20.00`
- **Solvency Defense Ladder**:
  * Hard Floor Stop: `4,775.00 USD` (Zero Open Risk) | Operating Defense Buffer: `4,795.00 USD` (Capital Preservation Mode)
  * Kernel Admission Floor: `4,795.00 USD` (`min(balance, equity) - StressedLoss - 2.00 >= 4,795.00 USD`)
- **Pipeline Health (23_Master_Pipeline_Telemetry.parquet)**: Status=`HEALTHY` | Latency=`4.2 ms` | RAM Usage=`385.0 MB`

---

## 2. Technical Profile, VWAP Dispersion Grid & BTC Ribbon
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Session Anchor & Volatility**:
  * Session VWAP: `52.75` | VWAP Z-Score: `-0.73` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.1970` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `52.51` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `54.37` | Lower -3.00σ Band: `51.12`
  * Upper +2.51σ Band: `54.10` | Lower -2.51σ Band: `51.39`
  * Upper +2.01σ Band: `53.83` | Lower -2.01σ Band: `51.66`
  * Upper +2.00σ Band: `53.83` | Lower -2.00σ Band: `51.66`
  * Upper +1.28σ Band: `53.44` | Lower -1.28σ Band: `52.05`
  * Upper +1.00σ Band: `53.29` | Lower -1.00σ Band: `52.20`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`52.16` | EMA-20=`52.23` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`52.48` (Slope: `+0.0000`) | EMA-100=`52.83`
  * Institutional Anchors: EMA-144=`53.03` | EMA-200=`53.20` (Slope: `-0.2611`) | EMA-233=`53.28`
- **Range Boundaries**: 24H High=`54.61` | 24H Low=`51.95` | Weekly High=`54.61` | Weekly Low=`51.95`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `52.94` (Distance: `-1.27%`)
  * Point of Control (POC) = `52.45` (Distance: `-0.35%`)
  * Value Area Low (VAL) = `51.99` (Distance: `+0.55%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`54.10` | POC=`53.83` | VAL=`53.54`
  * Prior Day Extremes: PDH=`54.61` | PDL=`53.28` | PDC=`53.94`
  * Monday Range Blueprint: High=`54.39` | Mid=`53.69` | Low=`52.99`
  * Developing Weekly Value Area: Weekly VAH=`54.49` | Weekly POC=`53.89` | Weekly VAL=`53.22`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`54.37` | Low=`52.98`
  * London Session (08:00-16:00 UTC): High=`53.50` | Low=`52.30`
  * New York Session (13:00-21:00 UTC): High=`53.07` | Low=`51.98`
  * Initial Balance (First Hour): IB High=`53.50` | IB Low=`52.73`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `52.05` - `52.47`
  * Optimal Trade Entry (OTE 0.705): `52.37`
  * Structural Invalidation Anchor (0.786): `52.68`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `52.38` | `52.39` | `52.27` | `52.30` | `964` | 50,422.02 USD | -27,011.80 USD | `-53.57%` | -622,975.79 USD | `-0.51` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `52.30` | `52.44` | `52.30` | `52.42` | `768` | 40,256.26 USD | 31,895.34 USD | `+79.23%` | -591,080.44 USD | `+0.71` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `52.42` | `52.45` | `52.38` | `52.40` | `1,171` | 61,363.91 USD | -14,758.41 USD | `-24.05%` | -605,838.85 USD | `-0.32` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `52.40` | `52.43` | `52.29` | `52.40` | `3,701` | 193,925.00 USD | 50,559.02 USD | `+26.07%` | -1,298,017.73 USD | `+0.34` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `52.40` | `52.46` | `52.27` | `52.42` | `2,743` | 143,779.83 USD | 44,357.61 USD | `+30.85%` | -1,253,660.13 USD | `+0.27` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `52.42` | `52.51` | `52.26` | `52.28` | `3,526` | 184,335.75 USD | -129,855.96 USD | `-70.45%` | -1,383,516.08 USD | `-0.52` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `52.61` | `52.65` | `52.32` | `52.51` | `20,260` | 1,063,771.56 USD | -103,422.23 USD | `-9.72%` | -813,873.69 USD | `-0.19` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `52.51` | `52.51` | `52.26` | `52.42` | `15,925` | 834,740.72 USD | -28,381.18 USD | `-3.40%` | -842,254.87 USD | `+0.15` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `52.42` | `52.51` | `51.97` | `52.01` | `15,397` | 800,720.98 USD | -646,338.43 USD | `-80.72%` | -1,488,593.30 USD | `-1.42` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.74` | `53.07` | `52.30` | `52.37` | `60,050` | 3,144,818.50 USD | -2,040,047.85 USD | `-64.87%` | -5,225,084.59 USD | `-1.56` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.37` | `52.76` | `51.98` | `52.42` | `110,375` | 5,785,526.38 USD | 546,780.27 USD | `+9.45%` | -4,678,304.31 USD | `+1.74` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `52.42` | `52.51` | `51.95` | `52.26` | `35,244` | 1,841,675.22 USD | -173,990.71 USD | `-9.45%` | -4,852,295.02 USD | `+0.77` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `53.37` | `54.37` | `52.98` | `53.22` | `57,426` | 3,056,384.00 USD | -1,158,823.80 USD | `-37.91%` | -1,894,512.32 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `53.22` | `53.50` | `52.45` | `52.73` | `52,817` | 2,785,304.50 USD | -1,290,524.42 USD | `-46.33%` | -3,185,036.74 USD | `-0.97` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.74` | `53.07` | `52.30` | `52.37` | `60,050` | 3,144,818.50 USD | -2,040,047.85 USD | `-64.87%` | -5,225,084.59 USD | `-1.56` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.37` | `52.76` | `51.98` | `52.42` | `110,375` | 5,785,526.38 USD | 546,780.27 USD | `+9.45%` | -4,678,304.31 USD | `+1.74` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `52.42` | `52.51` | `51.95` | `52.26` | `35,244` | 1,841,675.22 USD | -173,990.71 USD | `-9.45%` | -4,852,295.02 USD | `+0.77` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `BID/ASK` | None | `0.0000` | 0.00 USD | `0.00%` | Unarmored | `0.0%` | Interbank L2 | NONE |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `52.28` | `39.3100` | 2,055.32 USD | 829,601.63 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `52.28` | `1057.0300` | 55,265.76 USD | 884,867.39 USD | `4 orders` | `-0.04%` | `-` |
| `BID` | `52.29` | `110.8300` | 5,795.74 USD | 236,208.00 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `52.29` | `3238.2300` | 169,336.76 USD | 405,544.77 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `52.29` | `89.8900` | 4,700.44 USD | 410,245.20 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `52.29` | `107.2900` | 5,610.19 USD | 415,855.40 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `52.29` | `67.7000` | 3,539.97 USD | 419,395.36 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `52.29` | `110.8400` | 5,795.60 USD | 425,190.97 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `52.29` | `5683.7100` | 297,184.14 USD | 722,375.11 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `52.29` | `2011.4600` | 105,171.20 USD | 827,546.31 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `52.30` | `39.8200` | 2,082.79 USD | 3,946.45 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `52.30` | `263.0900` | 13,760.66 USD | 17,707.11 USD | `3 orders` | `-0.00%` | `-` |
| `BID` | `52.30` | `211.3400` | 11,053.72 USD | 28,760.82 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `52.30` | `27.6300` | 1,445.10 USD | 30,205.93 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `52.30` | `55.1800` | 2,885.97 USD | 33,091.90 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `52.30` | `2141.1200` | 111,978.43 USD | 145,070.33 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `52.30` | `37.7000` | 1,971.63 USD | 147,041.97 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `52.30` | `541.2500` | 28,305.75 USD | 175,347.72 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `52.30` | `1052.9600` | 55,064.54 USD | 230,412.26 USD | `3 orders` | `-0.02%` | `-` |
| `ASK` | `52.31` | `6319.0500` | 330,581.10 USD | 574,170.25 USD | `5 orders` | `+0.02%` | `-` |
| `ASK` | `52.31` | `2078.3100` | 108,724.71 USD | 243,589.15 USD | `5 orders` | `+0.01%` | `-` |
| `ASK` | `52.31` | `1138.5900` | 59,563.06 USD | 134,864.44 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `52.31` | `583.3700` | 30,517.25 USD | 75,301.38 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `52.31` | `147.7800` | 7,730.52 USD | 44,784.13 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `52.31` | `131.4300` | 6,875.10 USD | 37,053.61 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `52.31` | `486.4800` | 25,447.28 USD | 30,178.50 USD | `4 orders` | `+0.00%` | `-` |
| `ASK` | `52.31` | `52.8900` | 2,766.57 USD | 4,731.22 USD | `2 orders` | `+0.00%` | `-` |
| `ASK` | `52.31` | `37.5600` | 1,964.65 USD | 1,964.65 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `52.31` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 52.31` | `0.00%` | `-` |
| `BID` | `52.31` | `35.6300` | 1,863.66 USD | 1,863.66 USD | `1 orders` | `-0.00%` | `-` |
| `ASK` | `52.32` | `779.2600` | 40,774.00 USD | 1,311,688.79 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `52.32` | `42.1000` | 2,202.80 USD | 1,270,914.79 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `52.32` | `8841.5200` | 462,606.01 USD | 1,268,711.99 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `52.32` | `211.4800` | 11,064.85 USD | 806,105.98 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `52.32` | `2683.0000` | 140,374.56 USD | 795,041.13 USD | `7 orders` | `+0.03%` | `-` |
| `ASK` | `52.32` | `35.0800` | 1,835.35 USD | 654,666.57 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `52.32` | `1066.3100` | 55,787.21 USD | 652,831.22 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `52.32` | `167.6300` | 8,769.90 USD | 597,044.02 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `52.32` | `269.5900` | 14,103.87 USD | 588,274.12 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `52.33` | `2.7300` | 142.85 USD | 1,323,052.73 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `52.33` | `214.4500` | 11,221.10 USD | 1,322,909.88 USD | `3 orders` | `+0.04%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:33:46 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `115` | `0x5b5d...c060` | `SHORT` | 17,481,265.59 USD | `333,790.30` | `59.15` | `52.31` | `559.32` | 2,261,768.36 USD | `+12.94%` | `5X Cross` |
| `123` | `0x4692...164f` | `SHORT` | 16,204,093.18 USD | `309,776.39` | `53.35` | `52.31` | `249.73` | 321,148.55 USD | `+1.98%` | `5X Cross` |
| `174` | `0x49e9...e1d0` | `SHORT` | 11,725,051.32 USD | `224,132.65` | `55.61` | `52.31` | `94.42` | 737,995.28 USD | `+6.29%` | `4X Cross` |
| `208` | `0xacb6...efbd` | `SHORT` | 10,524,703.76 USD | `201,133.33` | `59.63` | `52.31` | `76.44` | 1,467,953.36 USD | `+13.95%` | `6X Cross` |
| `245` | `0xc26c...b8f4` | `LONG` | 9,503,601.71 USD | `181,463.41` | `55.43` | `52.31` | `0.000000` | -555,153.37 USD | `-5.84%` | `2X Cross` |
| `367` | `0xd8c5...99b0` | `SHORT` | 6,614,496.25 USD | `126,320.04` | `61.98` | `52.31` | `199.32` | 1,214,841.59 USD | `+18.37%` | `3X Cross` |
| `368` | `0x645b...87b8` | `LONG` | 6,607,779.25 USD | `126,309.96` | `56.63` | `52.31` | `0.000000` | -545,701.64 USD | `-8.26%` | `3X Cross` |
| `402` | `0xe9ff...5903` | `SHORT` | 5,911,163.93 USD | `112,996.08` | `60.07` | `52.31` | `197.74` | 876,786.87 USD | `+14.83%` | `5X Cross` |
| `432` | `0xfc66...ca06` | `SHORT` | 5,425,471.62 USD | `103,683.98` | `54.61` | `52.31` | `438.81` | 236,308.90 USD | `+4.36%` | `3X Cross` |
| `592` | `0x354b...6425` | `LONG` | 3,880,431.22 USD | `74,182.86` | `52.41` | `52.31` | `0.000000` | -7,264.10 USD | `-0.19%` | `10X Cross` |
| `618` | `0x9aa5...58af` | `LONG` | 3,727,242.53 USD | `71,243.43` | `61.59` | `52.31` | `0.000000` | -660,915.00 USD | `-17.73%` | `20X Cross` |
| `742` | `0x2056...8396` | `LONG` | 3,139,020.00 USD | `60,000.00` | `66.92` | `52.31` | `21.34` | -876,307.14 USD | `-27.92%` | `10X Cross` |
| `867` | `0x4e23...20c3` | `SHORT` | 2,644,794.31 USD | `50,540.69` | `52.44` | `52.31` | `305.63` | 5,711.10 USD | `+0.22%` | `16X Cross` |
| `875` | `0x0242...ffa1` | `SHORT` | 2,611,440.51 USD | `49,916.67` | `56.48` | `52.31` | `328.74` | 207,691.36 USD | `+7.95%` | `10X Cross` |
| `880` | `0x960b...f0fc` | `LONG` | 2,587,195.35 USD | `49,457.96` | `55.82` | `52.31` | `0.000000` | -173,741.68 USD | `-6.72%` | `25X Cross` |
| `963` | `0x8b9d...7b28` | `LONG` | 2,344,939.83 USD | `44,823.47` | `58.35` | `52.31` | `0.000000` | -270,508.71 USD | `-11.54%` | `10X Cross` |
| `1060` | `0x5647...e7de` | `LONG` | 2,106,390.72 USD | `40,262.07` | `57.38` | `52.31` | `0.000000` | -203,846.88 USD | `-9.68%` | `20X Cross` |
| `1069` | `0xa2ce...3126` | `LONG` | 2,092,600.00 USD | `40,000.00` | `74.30` | `52.31` | `0.000000` | -879,455.49 USD | `-42.03%` | `20X Cross` |
| `1447` | `0x3678...b209` | `LONG` | 1,570,980.00 USD | `30,000.00` | `57.15` | `52.31` | `0.000000` | -143,520.00 USD | `-9.14%` | `20X Cross` |
| `1448` | `0x5a88...d997` | `LONG` | 1,570,890.00 USD | `30,000.00` | `59.50` | `52.31` | `38.46` | -213,997.59 USD | `-13.62%` | `25X Cross` |
| `1666` | `0x7ea9...fc7f` | `LONG` | 1,307,875.00 USD | `25,000.00` | `53.60` | `52.29` | `18.23` | -32,129.05 USD | `-2.46%` | `25X Cross` |
| `1791` | `0xf517...c032` | `LONG` | 1,183,938.68 USD | `22,627.50` | `66.29` | `52.29` | `0.000000` | -316,056.42 USD | `-26.70%` | `20X Cross` |
| `1916` | `0xcc9f...d218` | `LONG` | 1,073,781.44 USD | `20,520.60` | `52.63` | `52.29` | `26.86` | -6,126.61 USD | `-0.57%` | `2X Isolated` |
| `2029` | `0xce97...7e78` | `LONG` | 1,002,050.54 USD | `19,149.78` | `52.21` | `52.29` | `0.000000` | 2,166.94 USD | `+0.22%` | `5X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `81.27` | 429.11 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 0.43K USD at 81.2710 USD [API] | `2026-02-01 23:01:26` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`53.52` (Vol: 3,600,000.00 USD, Dist: `+2.39%`) | Long MP=`51.68` (Vol: 2,700,000.00 USD, Dist: `--1.13%`)
  * 48H Horizon: Short MP=`55.08` (Vol: 4,200,000.00 USD, Dist: `+5.38%`) | Long MP=`51.68` (Vol: 3,100,000.00 USD, Dist: `--1.13%`)
  * 3D Horizon: Short MP=`55.08` (Vol: 4,700,000.00 USD, Dist: `+5.38%`) | Long MP=`51.96` (Vol: 4,000,000.00 USD, Dist: `--0.60%`)
  * 7D Horizon: Short MP=`54.83` (Vol: 7,300,000.00 USD, Dist: `+4.89%`) | Long MP=`51.96` (Vol: 4,900,000.00 USD, Dist: `--0.60%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Matrix | Interbank Flow | - | - | - | - | - | - | Interbank Tier |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Map | Near Money | - | - | - | - | 0.00% | - |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Stops | Clear | - | - | - | 0.00% | SAFE (No Un-Swept Clusters) |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Exchange | Baseline | - | - | - | - | - | - |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `56.39K` | Last 24h: `193.96K` | Last 3d: `450.64K` | Last 7d: `729.34K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `-` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `0.0101%` | **USDT BingX** | `-` |
| **USDT Gate** | `-` | **USDT Bitget** | `-` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Multi-TF | Interbank Desk | 50.0% | 50.0% | 1.00 | Normal Balanced Liquidity |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 15m Bar | Interbank Tick Flow | - | - | - | - | - | - | - | - | 0.00% | Balanced Interbank Imbalance |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `2026-10-28 21:11:32 IST` | `Auction` | `AUCTION_ROTATIONAL_BALANCE` | **`BEARISH (BELOW PIVOT)`** | SILVER (XAGUSD.pi) Metal Auction: ROTATI | `53.72` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `15m` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `30m` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `1h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `2h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `4h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `6h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `8h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `12h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `24h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `1w` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `30d` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |

* Spot Capital Netflows: 5m=`-` | 15m=`-` | 1h=`-` | 24h=`-`
* Futures Capital Netflows: 5m=`-` | 15m=`-` | 1h=`-` | 24h=`-`
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
  * `2026-10-30 00:58:24 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:48:24 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:28:24 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:28:24 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:29:24 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:29:24 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:29:24 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:29:24 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:29:24 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:29:24 IST`: [think.ing.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `51.99` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `51.70` (Risk Distance: `0.2904` pts)
  * +2.5R Take Profit: `52.71`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.01 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `52.94` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `53.23` (Risk Distance: `0.2904` pts)
  * +2.5R Take Profit: `52.21`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.01 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`52.68`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
