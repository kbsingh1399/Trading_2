# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAGSGD
**Canonical Key**: `XAGSGD` | **Broker Instrument**: `XAGSGD.pi` | **Asset Class**: `Forex Exotic`
**Timestamp**: `2026-10-30 03:37:25 IST` (`2026-10-29 22:07:25 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `66.79` | **Live Ask Quote**: `66.84` | **Mid Price**: `66.81`
- **Spread Points**: `51.00` | **Spread BPS**: `7.63 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `66.81` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `67.28` | Lower -3.00σ Band: `66.34`
  * Upper +2.51σ Band: `67.18` | Lower -2.51σ Band: `66.44`
  * Upper +2.01σ Band: `67.09` | Lower -2.01σ Band: `66.53`
  * Upper +2.00σ Band: `67.08` | Lower -2.00σ Band: `66.54`
  * Upper +1.28σ Band: `67.00` | Lower -1.28σ Band: `66.62`
  * Upper +1.00σ Band: `66.95` | Lower -1.00σ Band: `66.68`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`66.81` | EMA-20=`66.81` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`66.81` (Slope: `+0.0000`) | EMA-100=`66.81`
  * Institutional Anchors: EMA-144=`66.81` | EMA-200=`66.81` (Slope: `+0.0000`) | EMA-233=`66.81`
- **Range Boundaries**: 24H High=`67.48` | 24H Low=`66.14` | Weekly High=`68.15` | Weekly Low=`65.48`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `52.19` (Distance: `+0.04%`)
  * Point of Control (POC) = `52.13` (Distance: `+0.16%`)
  * Value Area Low (VAL) = `52.13` (Distance: `+0.16%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`52.92` | POC=`52.45` | VAL=`51.99`
  * Prior Day Extremes: PDH=`54.37` | PDL=`51.95` | PDC=`52.13`
  * Monday Range Blueprint: High=`54.39` | Mid=`53.69` | Low=`52.99`
  * Developing Weekly Value Area: Weekly VAH=`54.49` | Weekly POC=`53.89` | Weekly VAL=`53.18`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`52.22` | Low=`52.13`
  * London Session (08:00-16:00 UTC): High=`67.08` | Low=`66.54`
  * New York Session (13:00-21:00 UTC): High=`67.21` | Low=`66.41`
  * Initial Balance (First Hour): IB High=`67.01` | IB Low=`66.61`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `66.54` - `67.08`
  * Optimal Trade Entry (OTE 0.705): `66.95`
  * Structural Invalidation Anchor (0.786): `67.35`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `52.07` | `52.08` | `52.04` | `52.08` | `670` | 34,890.25 USD | 14,731.44 USD | `+42.22%` | -652,509.02 USD | `+0.75` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `52.08` | `52.08` | `52.02` | `52.07` | `782` | 40,717.96 USD | 9,254.08 USD | `+22.73%` | -643,254.94 USD | `+0.48` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `52.07` | `52.10` | `52.03` | `52.04` | `695` | 36,169.89 USD | -20,867.24 USD | `-57.69%` | -664,122.18 USD | `-0.67` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `51.97` | `52.04` | `51.95` | `51.99` | `2,105` | 109,443.16 USD | 7,980.23 USD | `+7.29%` | -1,752,782.40 USD | `+0.02` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `51.99` | `52.08` | `51.96` | `52.08` | `2,217` | 115,450.28 USD | 88,953.49 USD | `+77.05%` | -1,663,828.91 USD | `+0.67` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `52.08` | `52.10` | `51.99` | `52.00` | `2,318` | 120,533.68 USD | -96,314.30 USD | `-79.91%` | -1,760,143.21 USD | `-0.74` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `52.42` | `52.51` | `51.97` | `52.01` | `15,397` | 800,720.98 USD | -646,338.43 USD | `-80.72%` | -2,335,773.51 USD | `-1.42` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `52.01` | `52.12` | `51.95` | `52.08` | `9,961` | 518,719.08 USD | 235,233.07 USD | `+45.35%` | -2,100,540.44 USD | `+0.82` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `52.08` | `52.36` | `51.98` | `52.35` | `8,673` | 454,014.20 USD | 384,260.00 USD | `+84.64%` | -1,716,280.44 USD | `+1.13` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `52.74` | `53.07` | `52.30` | `52.37` | `60,050` | 3,144,818.50 USD | -2,040,047.85 USD | `-64.87%` | -5,225,084.59 USD | `-1.56` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.37` | `52.76` | `51.98` | `52.42` | `110,375` | 5,785,526.38 USD | 546,780.27 USD | `+9.45%` | -4,678,304.31 USD | `+1.74` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `52.42` | `52.51` | `51.95` | `52.13` | `45,007` | 2,346,304.92 USD | -993,310.91 USD | `-42.34%` | -5,671,615.22 USD | `-0.06` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `53.37` | `54.37` | `52.98` | `53.22` | `57,426` | 3,056,384.00 USD | -1,158,823.80 USD | `-37.91%` | -1,894,512.32 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `53.22` | `53.50` | `52.45` | `52.73` | `52,817` | 2,785,304.50 USD | -1,290,524.42 USD | `-46.33%` | -3,185,036.74 USD | `-0.97` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.74` | `53.07` | `52.30` | `52.37` | `60,050` | 3,144,818.50 USD | -2,040,047.85 USD | `-64.87%` | -5,225,084.59 USD | `-1.56` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.37` | `52.76` | `51.98` | `52.42` | `110,375` | 5,785,526.38 USD | 546,780.27 USD | `+9.45%` | -4,678,304.31 USD | `+1.74` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `52.42` | `52.51` | `51.95` | `52.13` | `45,007` | 2,346,304.92 USD | -993,310.91 USD | `-42.34%` | -5,671,615.22 USD | `-0.06` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| `BID` | `52.20` | `326.1900` | 17,028.75 USD | 132,898.80 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `52.20` | `1622.5100` | 84,701.51 USD | 217,600.32 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `52.20` | `609.5200` | 31,818.77 USD | 249,419.09 USD | `4 orders` | `-0.04%` | `-` |
| `BID` | `52.20` | `216.4700` | 11,299.95 USD | 260,719.04 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `52.20` | `379.6800` | 19,819.30 USD | 280,538.34 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `52.21` | `299.6900` | 15,648.01 USD | 84,421.76 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `52.21` | `124.8200` | 6,517.23 USD | 90,938.99 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `52.21` | `0.2000` | 10.44 USD | 90,949.43 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `52.21` | `32.9300` | 1,719.28 USD | 92,668.70 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `52.21` | `199.3700` | 10,408.91 USD | 103,077.61 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `52.21` | `161.8900` | 8,451.95 USD | 111,529.57 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `52.21` | `83.1400` | 4,340.49 USD | 115,870.06 USD | `1 orders` | `-0.03%` | `-` |
| `ASK` | `52.22` | `62.0600` | 3,241.02 USD | 14,819.38 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `52.22` | `221.7100` | 11,578.36 USD | 11,578.36 USD | `3 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `52.22` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 52.22` | `0.00%` | `-` |
| `BID` | `52.22` | `56.5800` | 2,954.72 USD | 2,954.72 USD | `2 orders` | `-0.00%` | `-` |
| `BID` | `52.22` | `72.0000` | 3,759.91 USD | 6,714.63 USD | `3 orders` | `-0.00%` | `-` |
| `BID` | `52.22` | `189.5600` | 9,898.82 USD | 16,613.46 USD | `2 orders` | `-0.00%` | `-` |
| `BID` | `52.22` | `198.5100` | 10,365.99 USD | 26,979.45 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `52.22` | `143.9900` | 7,518.87 USD | 34,498.32 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `52.22` | `125.7200` | 6,564.72 USD | 41,063.04 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `52.22` | `204.5600` | 10,681.30 USD | 51,744.35 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `52.22` | `326.1400` | 17,029.40 USD | 68,773.75 USD | `5 orders` | `-0.01%` | `-` |
| `ASK` | `52.23` | `1101.3600` | 57,529.54 USD | 164,398.83 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `52.23` | `845.0300` | 44,139.30 USD | 106,869.29 USD | `6 orders` | `+0.02%` | `-` |
| `ASK` | `52.23` | `120.1100` | 6,273.59 USD | 62,729.99 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `52.23` | `124.8200` | 6,519.47 USD | 56,456.40 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `52.23` | `313.3600` | 16,366.79 USD | 49,936.93 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `52.23` | `71.8400` | 3,752.13 USD | 33,570.14 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `52.23` | `124.9500` | 6,525.64 USD | 29,818.01 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `52.23` | `162.2400` | 8,472.98 USD | 23,292.37 USD | `2 orders` | `+0.00%` | `-` |
| `ASK` | `52.24` | `129.4900` | 6,765.21 USD | 332,966.52 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `52.24` | `220.9000` | 11,540.70 USD | 326,201.31 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `52.24` | `134.0400` | 7,002.65 USD | 314,660.61 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `52.24` | `181.5400` | 9,484.01 USD | 307,657.96 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `52.24` | `254.1500` | 13,277.05 USD | 298,173.95 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `52.24` | `1816.9700` | 94,916.70 USD | 284,896.90 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `52.24` | `120.1100` | 6,274.31 USD | 189,980.20 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `52.24` | `124.7500` | 6,516.57 USD | 183,705.90 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `52.24` | `244.8600` | 12,790.51 USD | 177,189.33 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `52.25` | `830.5000` | 43,390.30 USD | 376,356.82 USD | `2 orders` | `+0.04%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 03:35:39 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `116` | `0x5b5d...c060` | `SHORT` | 17,602,117.44 USD | `337,496.26` | `59.07` | `52.17` | `588.24` | 2,334,244.87 USD | `+13.26%` | `5X Cross` |
| `124` | `0x4692...164f` | `SHORT` | 16,200,363.15 USD | `310,619.56` | `53.32` | `52.17` | `250.29` | 360,821.31 USD | `+2.23%` | `5X Cross` |
| `186` | `0x49e9...e1d0` | `SHORT` | 11,288,663.94 USD | `216,444.52` | `55.61` | `52.17` | `94.52` | 746,879.02 USD | `+6.62%` | `4X Cross` |
| `210` | `0xacb6...efbd` | `SHORT` | 10,492,321.29 USD | `201,133.33` | `59.63` | `52.17` | `76.54` | 1,500,335.82 USD | `+14.30%` | `6X Cross` |
| `241` | `0xc26c...b8f4` | `LONG` | 9,464,224.15 USD | `181,463.41` | `55.43` | `52.17` | `0.000000` | -594,530.93 USD | `-6.28%` | `2X Cross` |
| `355` | `0xd8c5...99b0` | `SHORT` | 6,588,221.69 USD | `126,320.04` | `61.98` | `52.17` | `198.49` | 1,241,116.16 USD | `+18.84%` | `3X Cross` |
| `356` | `0x645b...87b8` | `LONG` | 6,587,695.96 USD | `126,309.96` | `56.63` | `52.17` | `0.000000` | -565,784.92 USD | `-8.59%` | `3X Cross` |
| `396` | `0xe9ff...5903` | `SHORT` | 5,893,310.55 USD | `112,996.08` | `60.07` | `52.17` | `199.26` | 894,640.25 USD | `+15.18%` | `5X Cross` |
| `419` | `0xfc66...ca06` | `SHORT` | 5,408,363.76 USD | `103,683.98` | `54.61` | `52.17` | `265.83` | 253,416.76 USD | `+4.69%` | `3X Cross` |
| `617` | `0x9aa5...58af` | `LONG` | 3,716,484.77 USD | `71,243.43` | `61.59` | `52.17` | `0.000000` | -671,672.75 USD | `-18.07%` | `20X Cross` |
| `740` | `0x2056...8396` | `LONG` | 3,129,300.00 USD | `60,000.00` | `66.92` | `52.17` | `21.34` | -886,027.14 USD | `-28.31%` | `10X Cross` |
| `770` | `0x354b...6425` | `LONG` | 3,007,768.42 USD | `57,669.80` | `52.37` | `52.17` | `0.000000` | -12,633.13 USD | `-0.42%` | `10X Cross` |
| `873` | `0x0242...ffa1` | `SHORT` | 2,603,403.92 USD | `49,916.67` | `56.48` | `52.17` | `341.28` | 215,727.94 USD | `+8.29%` | `10X Cross` |
| `884` | `0x960b...f0fc` | `LONG` | 2,579,479.90 USD | `49,457.96` | `55.82` | `52.17` | `0.000000` | -181,457.13 USD | `-7.03%` | `25X Cross` |
| `971` | `0x8b9d...7b28` | `LONG` | 2,337,768.08 USD | `44,823.47` | `58.35` | `52.17` | `0.000000` | -277,680.47 USD | `-11.88%` | `10X Cross` |
| `1063` | `0x5647...e7de` | `LONG` | 2,100,109.83 USD | `40,262.07` | `57.38` | `52.17` | `0.000000` | -210,127.77 USD | `-10.01%` | `20X Cross` |
| `1069` | `0xa2ce...3126` | `LONG` | 2,086,200.00 USD | `40,000.00` | `74.30` | `52.17` | `0.000000` | -885,855.49 USD | `-42.46%` | `20X Cross` |
| `1099` | `0xb078...de15` | `SHORT` | 2,034,045.52 USD | `39,000.01` | `52.58` | `52.17` | `195.94` | 16,473.43 USD | `+0.81%` | `8X Cross` |
| `1437` | `0x5a88...d997` | `LONG` | 1,564,650.00 USD | `30,000.00` | `59.50` | `52.17` | `40.07` | -220,237.59 USD | `-14.08%` | `25X Cross` |
| `1438` | `0x3678...b209` | `LONG` | 1,564,650.00 USD | `30,000.00` | `57.15` | `52.17` | `0.000000` | -149,850.00 USD | `-9.58%` | `20X Cross` |
| `1661` | `0x7ea9...fc7f` | `LONG` | 1,303,875.00 USD | `25,000.00` | `53.60` | `52.17` | `18.23` | -36,129.05 USD | `-2.77%` | `25X Cross` |
| `1782` | `0xf517...c032` | `LONG` | 1,180,137.26 USD | `22,627.50` | `66.29` | `52.17` | `0.000000` | -319,857.84 USD | `-27.10%` | `20X Cross` |
| `1905` | `0xcc9f...d218` | `LONG` | 1,070,251.89 USD | `20,520.60` | `52.63` | `52.17` | `26.86` | -9,656.16 USD | `-0.90%` | `2X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `65.51` | 14,313.28 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 14.31K USD at 65.5130 USD [API] | `2026-09-04 12:30:30` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`53.30` (Vol: 3,200,000.00 USD, Dist: `+1.99%`) | Long MP=`51.68` (Vol: 2,700,000.00 USD, Dist: `--1.11%`)
  * 48H Horizon: Short MP=`55.08` (Vol: 4,200,000.00 USD, Dist: `+5.40%`) | Long MP=`51.68` (Vol: 3,100,000.00 USD, Dist: `--1.11%`)
  * 3D Horizon: Short MP=`55.08` (Vol: 4,700,000.00 USD, Dist: `+5.40%`) | Long MP=`51.96` (Vol: 4,000,000.00 USD, Dist: `--0.58%`)
  * 7D Horizon: Short MP=`54.83` (Vol: 7,300,000.00 USD, Dist: `+4.91%`) | Long MP=`51.96` (Vol: 4,900,000.00 USD, Dist: `--0.58%`)
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
  * Current Rate: `9.06K` | Last 24h: `193.96K` | Last 3d: `450.64K` | Last 7d: `729.34K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `-` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `0.0000%` | **USDT BingX** | `-` |
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
  * Execution Entry: `52.13` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `50.85` (Risk Distance: `1.28` pts)
  * +2.5R Take Profit: `55.32`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.06 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `52.19` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `53.47` (Risk Distance: `1.28` pts)
  * +2.5R Take Profit: `49.00`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.06 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`67.35`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
