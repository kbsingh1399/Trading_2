# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAGAUD
**Canonical Key**: `XAGAUD` | **Broker Instrument**: `XAGAUD.pi` | **Asset Class**: `Forex Cross`
**Timestamp**: `2026-10-30 01:29:57 IST` (`2026-10-29 19:59:57 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `52.26` | **Live Ask Quote**: `52.29` | **Mid Price**: `52.27`
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
  * Session VWAP: `52.75` | VWAP Z-Score: `-1.15` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.1929` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `43.70` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `54.37` | Lower -3.00σ Band: `51.12`
  * Upper +2.51σ Band: `54.11` | Lower -2.51σ Band: `51.39`
  * Upper +2.01σ Band: `53.84` | Lower -2.01σ Band: `51.66`
  * Upper +2.00σ Band: `53.83` | Lower -2.00σ Band: `51.67`
  * Upper +1.28σ Band: `53.44` | Lower -1.28σ Band: `52.06`
  * Upper +1.00σ Band: `53.29` | Lower -1.00σ Band: `52.21`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`52.11` | EMA-20=`52.21` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`52.48` (Slope: `+0.0000`) | EMA-100=`52.84`
  * Institutional Anchors: EMA-144=`53.04` | EMA-200=`53.21` (Slope: `-0.2620`) | EMA-233=`53.29`
- **Range Boundaries**: 24H High=`54.61` | 24H Low=`51.95` | Weekly High=`54.61` | Weekly Low=`51.95`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `52.96` (Distance: `-1.28%`)
  * Point of Control (POC) = `52.45` (Distance: `-0.34%`)
  * Value Area Low (VAL) = `51.99` (Distance: `+0.56%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `52.06` - `52.48`
  * Optimal Trade Entry (OTE 0.705): `52.38`
  * Structural Invalidation Anchor (0.786): `52.69`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `52.40` | `52.43` | `52.34` | `52.34` | `1,390` | 72,759.55 USD | -49,033.61 USD | `-67.39%` | -631,417.17 USD | `-0.93` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `52.34` | `52.36` | `52.29` | `52.34` | `1,176` | 61,554.19 USD | 11,597.17 USD | `+18.84%` | -619,820.01 USD | `+0.36` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `52.34` | `52.43` | `52.34` | `52.40` | `1,135` | 59,471.73 USD | 25,259.50 USD | `+42.47%` | -594,560.51 USD | `+0.58` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `52.51` | `52.51` | `52.26` | `52.39` | `5,381` | 281,915.97 USD | -53,564.03 USD | `-19.00%` | -1,383,024.73 USD | `-0.09` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `52.39` | `52.48` | `52.35` | `52.40` | `4,100` | 214,823.60 USD | -25,957.85 USD | `-12.08%` | -1,408,982.58 USD | `+0.01` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `52.40` | `52.43` | `52.29` | `52.40` | `3,701` | 193,925.00 USD | 50,559.02 USD | `+26.07%` | -1,358,423.56 USD | `+0.34` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `52.24` | `52.76` | `52.03` | `52.61` | `32,755` | 1,723,273.30 USD | 951,587.73 USD | `+55.22%` | -679,727.93 USD | `+1.89` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `52.61` | `52.65` | `52.32` | `52.51` | `20,260` | 1,063,771.56 USD | -103,422.23 USD | `-9.72%` | -783,150.17 USD | `-0.19` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `52.51` | `52.51` | `52.26` | `52.42` | `15,925` | 834,740.72 USD | -28,381.18 USD | `-3.40%` | -811,531.35 USD | `+0.15` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `53.22` | `53.50` | `52.45` | `52.73` | `52,817` | 2,785,304.50 USD | -1,290,524.42 USD | `-46.33%` | -2,786,118.52 USD | `-0.89` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.74` | `53.07` | `52.30` | `52.37` | `60,050` | 3,144,818.50 USD | -2,040,047.85 USD | `-64.87%` | -4,826,166.37 USD | `-1.34` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.37` | `52.76` | `51.98` | `52.42` | `110,375` | 5,785,526.38 USD | 546,780.27 USD | `+9.45%` | -4,279,386.10 USD | `+1.36` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `53.52` | `54.09` | `53.37` | `53.37` | `22,849` | 1,219,382.58 USD | -735,688.52 USD | `-60.33%` | -336,770.30 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `53.37` | `54.37` | `52.98` | `53.22` | `57,426` | 3,056,384.00 USD | -1,158,823.80 USD | `-37.91%` | -1,495,594.11 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `53.22` | `53.50` | `52.45` | `52.73` | `52,817` | 2,785,304.50 USD | -1,290,524.42 USD | `-46.33%` | -2,786,118.52 USD | `-0.89` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.74` | `53.07` | `52.30` | `52.37` | `60,050` | 3,144,818.50 USD | -2,040,047.85 USD | `-64.87%` | -4,826,166.37 USD | `-1.34` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.37` | `52.76` | `51.98` | `52.42` | `110,375` | 5,785,526.38 USD | 546,780.27 USD | `+9.45%` | -4,279,386.10 USD | `+1.36` | **`BULLISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:23:08 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `116` | `0x5b5d...c060` | `SHORT` | 17,459,569.22 USD | `333,790.30` | `59.15` | `52.31` | `535.09` | 2,283,464.73 USD | `+13.08%` | `5X Cross` |
| `124` | `0x4692...164f` | `SHORT` | 16,296,304.96 USD | `311,551.13` | `53.35` | `52.31` | `239.12` | 326,019.44 USD | `+2.00%` | `5X Cross` |
| `175` | `0x49e9...e1d0` | `SHORT` | 11,723,706.52 USD | `224,132.65` | `55.61` | `52.31` | `88.47` | 739,340.07 USD | `+6.31%` | `4X Cross` |
| `207` | `0xacb6...efbd` | `SHORT` | 10,521,485.63 USD | `201,133.33` | `59.63` | `52.31` | `76.44` | 1,471,171.49 USD | `+13.98%` | `6X Cross` |
| `247` | `0xc26c...b8f4` | `LONG` | 9,491,806.59 USD | `181,463.41` | `55.43` | `52.31` | `0.000000` | -566,948.49 USD | `-5.97%` | `2X Cross` |
| `362` | `0xd8c5...99b0` | `SHORT` | 6,607,422.33 USD | `126,320.04` | `61.98` | `52.31` | `194.31` | 1,221,915.51 USD | `+18.49%` | `3X Cross` |
| `363` | `0x645b...87b8` | `LONG` | 6,606,895.08 USD | `126,309.96` | `56.63` | `52.31` | `0.000000` | -546,585.81 USD | `-8.27%` | `3X Cross` |
| `400` | `0xe9ff...5903` | `SHORT` | 5,911,954.91 USD | `112,996.08` | `60.07` | `52.31` | `196.62` | 875,995.90 USD | `+14.82%` | `5X Cross` |
| `431` | `0xfc66...ca06` | `SHORT` | 5,423,397.94 USD | `103,683.98` | `54.61` | `52.31` | `435.05` | 238,382.58 USD | `+4.40%` | `3X Cross` |
| `630` | `0x9aa5...58af` | `LONG` | 3,726,815.07 USD | `71,243.43` | `61.59` | `52.31` | `0.000000` | -661,342.46 USD | `-17.75%` | `20X Cross` |
| `733` | `0x354b...6425` | `LONG` | 3,205,571.73 USD | `61,283.80` | `52.42` | `52.31` | `0.000000` | -7,166.92 USD | `-0.22%` | `10X Cross` |
| `752` | `0x2056...8396` | `LONG` | 3,138,660.00 USD | `60,000.00` | `66.92` | `52.31` | `21.34` | -876,667.14 USD | `-27.93%` | `10X Cross` |
| `867` | `0x4e23...20c3` | `SHORT` | 2,643,783.49 USD | `50,540.69` | `52.44` | `52.31` | `304.67` | 6,721.91 USD | `+0.25%` | `16X Cross` |
| `874` | `0x0242...ffa1` | `SHORT` | 2,611,190.92 USD | `49,916.67` | `56.48` | `52.31` | `276.36` | 207,940.94 USD | `+7.96%` | `10X Cross` |
| `881` | `0x960b...f0fc` | `LONG` | 2,586,997.51 USD | `49,457.96` | `55.82` | `52.31` | `0.000000` | -173,939.52 USD | `-6.72%` | `25X Cross` |
| `972` | `0x8b9d...7b28` | `LONG` | 2,345,163.95 USD | `44,823.47` | `58.35` | `52.31` | `0.000000` | -270,284.59 USD | `-11.53%` | `10X Cross` |
| `1068` | `0x5647...e7de` | `LONG` | 2,105,988.10 USD | `40,262.07` | `57.38` | `52.31` | `0.000000` | -204,249.50 USD | `-9.70%` | `20X Cross` |
| `1076` | `0xa2ce...3126` | `LONG` | 2,092,800.00 USD | `40,000.00` | `74.30` | `52.31` | `0.000000` | -879,255.49 USD | `-42.01%` | `20X Cross` |
| `1445` | `0x5a88...d997` | `LONG` | 1,569,210.00 USD | `30,000.00` | `59.50` | `52.31` | `37.83` | -215,677.59 USD | `-13.74%` | `25X Cross` |
| `1446` | `0x3678...b209` | `LONG` | 1,569,210.00 USD | `30,000.00` | `57.15` | `52.31` | `0.000000` | -145,290.00 USD | `-9.26%` | `20X Cross` |
| `1676` | `0x7ea9...fc7f` | `LONG` | 1,308,000.00 USD | `25,000.00` | `53.60` | `52.31` | `18.25` | -32,004.05 USD | `-2.45%` | `25X Cross` |
| `1790` | `0xce97...7e78` | `LONG` | 1,192,810.59 USD | `22,802.29` | `52.21` | `52.31` | `0.000000` | 2,268.19 USD | `+0.19%` | `5X Cross` |
| `1802` | `0xf517...c032` | `LONG` | 1,183,667.15 USD | `22,627.50` | `66.29` | `52.31` | `0.000000` | -316,327.95 USD | `-26.72%` | `20X Cross` |
| `1918` | `0xcc9f...d218` | `LONG` | 1,073,453.11 USD | `20,520.60` | `52.63` | `52.31` | `26.86` | -6,454.94 USD | `-0.60%` | `2X Isolated` |

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
  * Current Rate: `65.78K` | Last 24h: `163.44K` | Last 3d: `421.23K` | Last 7d: `760.43K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `-` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `0.0113%` | **USDT BingX** | `-` |
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
  * Spread-Padded Stop Loss: `51.70` (Risk Distance: `0.2855` pts)
  * +2.5R Take Profit: `52.70`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.01 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `52.96` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `53.24` (Risk Distance: `0.2855` pts)
  * +2.5R Take Profit: `52.24`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.01 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`52.69`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
