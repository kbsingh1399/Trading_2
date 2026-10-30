# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAGAUD
**Canonical Key**: `XAGAUD` | **Broker Instrument**: `XAGAUD.pi` | **Asset Class**: `Forex Cross`
**Timestamp**: `2026-10-30 15:48:21 IST` (`2026-10-30 10:18:21 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `72.01` | **Live Ask Quote**: `72.06` | **Mid Price**: `72.04`
- **Spread Points**: `50.00` | **Spread BPS**: `6.94 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `51.22` | VWAP Z-Score: `-1.28` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.1967` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `39.57` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `52.29` | Lower -3.00σ Band: `50.14`
  * Upper +2.51σ Band: `52.12` | Lower -2.51σ Band: `50.31`
  * Upper +2.01σ Band: `51.94` | Lower -2.01σ Band: `50.49`
  * Upper +2.00σ Band: `51.94` | Lower -2.00σ Band: `50.50`
  * Upper +1.28σ Band: `51.68` | Lower -1.28σ Band: `50.76`
  * Upper +1.00σ Band: `51.58` | Lower -1.00σ Band: `50.86`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`50.78` | EMA-20=`50.90` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`51.29` (Slope: `+0.0000`) | EMA-100=`51.81`
  * Institutional Anchors: EMA-144=`52.13` | EMA-200=`52.46` (Slope: `-0.4171`) | EMA-233=`52.66`
- **Range Boundaries**: 24H High=`53.07` | 24H Low=`50.40` | Weekly High=`54.61` | Weekly Low=`50.40`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `52.07` (Distance: `-2.70%`)
  * Point of Control (POC) = `51.44` (Distance: `-1.51%`)
  * Value Area Low (VAL) = `50.92` (Distance: `-0.50%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`52.92` | POC=`52.45` | VAL=`51.99`
  * Prior Day Extremes: PDH=`54.37` | PDL=`51.95` | PDC=`52.13`
  * Monday Range Blueprint: High=`54.39` | Mid=`53.69` | Low=`52.99`
  * Developing Weekly Value Area: Weekly VAH=`54.51` | Weekly POC=`53.87` | Weekly VAL=`52.66`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`52.22` | Low=`51.08`
  * London Session (08:00-16:00 UTC): High=`51.79` | Low=`50.40`
  * New York Session (13:00-21:00 UTC): High=`50.77` | Low=`50.63`
  * Initial Balance (First Hour): IB High=`51.79` | IB Low=`50.87`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `71.75` - `72.33`
  * Optimal Trade Entry (OTE 0.705): `72.18`
  * Structural Invalidation Anchor (0.786): `72.62`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `50.82` | `50.85` | `50.66` | `50.84` | `1,841` | 93,605.65 USD | 48,015.33 USD | `+51.30%` | -1,207,213.15 USD | `+1.87` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `50.84` | `50.90` | `50.79` | `50.82` | `1,545` | 78,516.90 USD | -25,261.96 USD | `-32.17%` | -1,232,475.11 USD | `-0.26` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `50.82` | `50.85` | `50.72` | `50.78` | `1,254` | 63,675.61 USD | -14,123.54 USD | `-22.18%` | -1,246,598.65 USD | `+0.06` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `50.96` | `51.04` | `50.76` | `50.82` | `5,604` | 284,817.70 USD | -149,453.81 USD | `-52.47%` | -1,929,253.97 USD | `-1.14` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `50.82` | `50.90` | `50.66` | `50.78` | `4,640` | 235,609.92 USD | -25,313.46 USD | `-10.74%` | -1,954,567.43 USD | `-0.03` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `50.78` | `50.82` | `50.68` | `50.79` | `3,277` | 166,435.55 USD | 54,875.49 USD | `+32.97%` | -1,899,691.94 USD | `+0.78` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `51.36` | `51.79` | `50.87` | `51.08` | `15,419` | 787,556.26 USD | -339,906.20 USD | `-43.16%` | -2,034,303.71 USD | `-0.64` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `51.08` | `51.12` | `50.66` | `50.78` | `20,835` | 1,057,959.63 USD | -603,060.14 USD | `-57.00%` | -2,637,363.85 USD | `-1.27` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `50.78` | `50.87` | `50.40` | `50.61` | `11,199` | 566,736.59 USD | -139,241.32 USD | `-24.57%` | -2,776,605.17 USD | `+0.02` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.14` | `52.22` | `51.73` | `51.78` | `24,880` | 1,288,261.52 USD | -1,001,103.02 USD | `-77.71%` | -3,487,681.50 USD | `-0.14` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `51.78` | `51.80` | `51.08` | `51.36` | `77,852` | 3,998,478.72 USD | -1,594,400.32 USD | `-39.88%` | -5,082,081.83 USD | `-0.66` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `51.36` | `51.79` | `50.40` | `50.89` | `62,135` | 3,162,174.42 USD | -1,002,113.55 USD | `-31.69%` | -6,084,195.37 USD | `+0.01` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.37` | `52.76` | `51.98` | `52.42` | `110,375` | 5,785,526.38 USD | 546,780.27 USD | `+9.45%` | -1,493,267.57 USD | `+1.00` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `52.42` | `52.51` | `51.95` | `52.13` | `45,007` | 2,346,304.92 USD | -993,310.91 USD | `-42.34%` | -2,486,578.48 USD | `-0.15` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.14` | `52.22` | `51.73` | `51.78` | `24,880` | 1,288,261.52 USD | -1,001,103.02 USD | `-77.71%` | -3,487,681.50 USD | `-0.14` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `51.78` | `51.80` | `51.08` | `51.36` | `77,852` | 3,998,478.72 USD | -1,594,400.32 USD | `-39.88%` | -5,082,081.83 USD | `-0.66` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `51.36` | `51.79` | `50.40` | `50.89` | `62,135` | 3,162,174.42 USD | -1,002,113.55 USD | `-31.69%` | -6,084,195.37 USD | `+0.01` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| `BID` | `50.67` | `88.4400` | 4,481.70 USD | 343,618.68 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `50.67` | `167.7400` | 8,499.72 USD | 352,118.40 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `50.67` | `88.4400` | 4,481.34 USD | 356,599.74 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `50.67` | `6159.4500` | 312,099.33 USD | 668,699.07 USD | `4 orders` | `-0.05%` | `-` |
| `BID` | `50.67` | `304.5300` | 15,430.23 USD | 684,129.30 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `50.67` | `7.4900` | 379.50 USD | 684,508.81 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `50.67` | `66.3400` | 3,361.25 USD | 687,870.06 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `50.67` | `10.0000` | 506.66 USD | 688,376.72 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `50.68` | `36.5200` | 1,850.94 USD | 17,519.18 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `50.68` | `67.2900` | 3,410.39 USD | 20,929.58 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `50.68` | `64.5600` | 3,271.97 USD | 24,201.54 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `50.68` | `37.0900` | 1,879.72 USD | 26,081.26 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `50.68` | `233.8300` | 11,850.27 USD | 37,931.53 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `50.68` | `5683.7100` | 288,039.06 USD | 325,970.59 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `50.68` | `259.6000` | 13,155.75 USD | 339,126.34 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `50.68` | `0.2100` | 10.64 USD | 339,136.98 USD | `1 orders` | `-0.03%` | `-` |
| `ASK` | `50.69` | `2147.7800` | 108,879.56 USD | 108,879.56 USD | `9 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `50.69` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 50.69` | `0.00%` | `-` |
| `BID` | `50.69` | `1.3100` | 66.41 USD | 66.41 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `50.69` | `0.2100` | 10.65 USD | 77.05 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `50.69` | `174.2400` | 8,831.70 USD | 8,908.76 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `50.69` | `133.3600` | 6,759.48 USD | 15,668.24 USD | `2 orders` | `-0.01%` | `-` |
| `ASK` | `50.70` | `40.4000` | 2,048.48 USD | 481,253.89 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `50.70` | `408.3200` | 20,703.46 USD | 479,205.41 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `50.70` | `197.2600` | 10,001.67 USD | 458,501.95 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `50.70` | `5850.8300` | 296,648.78 USD | 448,500.28 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `50.70` | `63.9500` | 3,242.33 USD | 151,851.50 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `50.70` | `65.3700` | 3,314.26 USD | 148,609.17 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `50.70` | `122.2700` | 6,198.97 USD | 145,294.91 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `50.70` | `351.4700` | 17,818.83 USD | 139,095.94 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `50.70` | `95.1800` | 4,825.25 USD | 121,277.12 USD | `4 orders` | `+0.00%` | `-` |
| `ASK` | `50.70` | `149.3700` | 7,572.31 USD | 116,451.87 USD | `2 orders` | `+0.00%` | `-` |
| `ASK` | `50.71` | `210.6900` | 10,684.93 USD | 872,741.30 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `50.71` | `228.7300` | 11,599.58 USD | 862,056.36 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `50.71` | `6747.8300` | 342,195.95 USD | 850,456.78 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `50.71` | `431.7000` | 21,891.94 USD | 508,260.82 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `50.71` | `88.4400` | 4,484.70 USD | 486,368.89 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `50.71` | `12.4300` | 630.29 USD | 481,884.18 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `50.72` | `6346.7500` | 321,900.81 USD | 1,406,413.45 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `50.72` | `4027.7400` | 204,278.92 USD | 1,084,512.64 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `50.72` | `147.7300` | 7,492.42 USD | 880,233.72 USD | `3 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 15:40:55 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `116` | `0x5b5d...c060` | `SHORT` | 17,525,135.17 USD | `346,127.65` | `58.90` | `50.63` | `503.57` | 2,861,224.92 USD | `+16.33%` | `5X Cross` |
| `122` | `0x4692...164f` | `SHORT` | 15,722,796.98 USD | `310,530.83` | `52.29` | `50.63` | `258.65` | 513,997.04 USD | `+3.27%` | `5X Cross` |
| `206` | `0xacb6...efbd` | `SHORT` | 10,186,397.50 USD | `201,133.33` | `59.63` | `50.63` | `77.05` | 1,806,259.62 USD | `+17.73%` | `6X Cross` |
| `240` | `0xc26c...b8f4` | `LONG` | 9,187,855.38 USD | `181,463.41` | `55.43` | `50.63` | `0.000000` | -870,899.70 USD | `-9.48%` | `2X Cross` |
| `276` | `0x49e9...e1d0` | `SHORT` | 8,394,011.86 USD | `165,778.17` | `55.18` | `50.63` | `99.31` | 752,860.23 USD | `+8.97%` | `4X Cross` |
| `354` | `0x645b...87b8` | `LONG` | 6,510,106.11 USD | `128,576.91` | `56.54` | `50.63` | `0.000000` | -759,963.13 USD | `-11.67%` | `3X Cross` |
| `361` | `0xd8c5...99b0` | `SHORT` | 6,396,088.91 USD | `126,320.04` | `61.98` | `50.63` | `198.78` | 1,433,248.94 USD | `+22.41%` | `3X Cross` |
| `395` | `0xe9ff...5903` | `SHORT` | 5,720,313.55 USD | `112,996.08` | `60.07` | `50.63` | `175.04` | 1,067,637.25 USD | `+18.66%` | `5X Cross` |
| `675` | `0x354b...6425` | `SHORT` | 3,307,283.76 USD | `65,317.45` | `51.01` | `50.63` | `218.26` | 24,346.45 USD | `+0.74%` | `10X Cross` |
| `683` | `0x9aa5...58af` | `LONG` | 3,256,680.05 USD | `64,299.00` | `61.59` | `50.63` | `0.000000` | -703,743.26 USD | `-21.61%` | `20X Cross` |
| `750` | `0x2056...8396` | `LONG` | 3,038,040.00 USD | `60,000.00` | `66.92` | `50.63` | `21.36` | -977,287.14 USD | `-32.17%` | `10X Cross` |
| `874` | `0x0242...ffa1` | `SHORT` | 2,527,380.84 USD | `49,916.67` | `56.48` | `50.63` | `331.48` | 291,751.03 USD | `+11.54%` | `10X Cross` |
| `880` | `0x960b...f0fc` | `LONG` | 2,504,155.43 USD | `49,457.96` | `55.82` | `50.63` | `0.000000` | -256,781.60 USD | `-10.25%` | `25X Cross` |
| `970` | `0x8b9d...7b28` | `LONG` | 2,269,188.17 USD | `44,823.47` | `58.35` | `50.63` | `0.000000` | -346,260.38 USD | `-15.26%` | `10X Cross` |
| `1056` | `0x5647...e7de` | `LONG` | 2,039,072.54 USD | `40,262.07` | `57.38` | `50.63` | `0.000000` | -271,165.06 USD | `-13.30%` | `20X Cross` |
| `1067` | `0xa2ce...3126` | `LONG` | 2,025,000.00 USD | `40,000.00` | `74.30` | `50.63` | `0.000000` | -947,055.49 USD | `-46.77%` | `20X Cross` |
| `1094` | `0xb078...de15` | `SHORT` | 1,974,648.51 USD | `39,000.01` | `52.58` | `50.63` | `200.49` | 75,870.45 USD | `+3.84%` | `8X Cross` |
| `1424` | `0x3678...b209` | `LONG` | 1,519,020.00 USD | `30,000.00` | `57.15` | `50.63` | `0.000000` | -195,480.00 USD | `-12.87%` | `20X Cross` |
| `1425` | `0x5a88...d997` | `LONG` | 1,518,990.00 USD | `30,000.00` | `59.50` | `50.63` | `38.47` | -265,897.59 USD | `-17.50%` | `25X Cross` |
| `1616` | `0xed62...e004` | `SHORT` | 1,299,291.23 USD | `25,660.45` | `50.81` | `50.63` | `54.72` | 4,516.24 USD | `+0.35%` | `25X Cross` |
| `1649` | `0x7ea9...fc7f` | `LONG` | 1,265,625.00 USD | `25,000.00` | `53.60` | `50.63` | `35.33` | -74,379.05 USD | `-5.88%` | `25X Cross` |
| `1794` | `0xf517...c032` | `LONG` | 1,146,014.99 USD | `22,627.50` | `66.29` | `50.63` | `0.000000` | -353,980.11 USD | `-30.89%` | `20X Cross` |
| `1800` | `0x24fb...ed0f` | `LONG` | 1,141,846.88 USD | `22,555.00` | `51.37` | `50.63` | `0.000000` | -16,819.70 USD | `-1.47%` | `20X Cross` |
| `1839` | `0x9e11...22a3` | `LONG` | 1,111,169.37 USD | `21,945.99` | `50.67` | `50.63` | `34.46` | -753.03 USD | `-0.07%` | `3X Isolated` |
| `1921` | `0xcc9f...d218` | `LONG` | 1,039,265.79 USD | `20,520.60` | `52.63` | `50.63` | `26.87` | -40,642.26 USD | `-3.91%` | `2X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`52.71` (Vol: 3,600,000.00 USD, Dist: `+4.01%`) | Long MP=`50.59` (Vol: 2,100,000.00 USD, Dist: `--0.17%`)
  * 48H Horizon: Short MP=`54.87` (Vol: 4,200,000.00 USD, Dist: `+8.26%`) | Long MP=`50.60` (Vol: 2,100,000.00 USD, Dist: `--0.15%`)
  * 3D Horizon: Short MP=`54.97` (Vol: 5,200,000.00 USD, Dist: `+8.46%`) | Long MP=`50.60` (Vol: 2,100,000.00 USD, Dist: `--0.15%`)
  * 7D Horizon: Short MP=`55.07` (Vol: 7,700,000.00 USD, Dist: `+8.67%`) | Long MP=`50.60` (Vol: 2,100,000.00 USD, Dist: `--0.15%`)
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
  * Current Rate: `44.14K` | Last 24h: `158.28K` | Last 3d: `386.46K` | Last 7d: `548.84K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `-` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `0.0077%` | **USDT BingX** | `-` |
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
  * `2026-10-30 15:33:17 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:17 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:18:17 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:12:17 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:45:17 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 15:45:17 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:45:17 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 15:45:17 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
  * Execution Entry: `50.92` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `50.61` (Risk Distance: `0.3110` pts)
  * +2.5R Take Profit: `51.70`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.02 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `52.07` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `52.38` (Risk Distance: `0.3110` pts)
  * +2.5R Take Profit: `51.29`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.02 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`72.62`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
