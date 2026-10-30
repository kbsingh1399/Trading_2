# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAGSGD
**Canonical Key**: `XAGSGD` | **Broker Instrument**: `XAGSGD.pi` | **Asset Class**: `Forex Exotic`
**Timestamp**: `2026-10-30 11:05:06 IST` (`2026-10-30 05:35:06 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `66.05` | **Live Ask Quote**: `66.08` | **Mid Price**: `66.06`
- **Spread Points**: `30.00` | **Spread BPS**: `4.54 bps` (Charter Threshold: `5.00 bps`)
- **Gate 1 Clearance**: **`PASS`** | **Execution Posture**: `PASSIVE LIMIT ONLY` | **Order Type Allowed**: `BUY_LIMIT / SELL_LIMIT`
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
  * Session VWAP: `51.46` | VWAP Z-Score: `+0.80` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.2332` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `51.31` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `52.05` | Lower -3.00σ Band: `50.87`
  * Upper +2.51σ Band: `51.96` | Lower -2.51σ Band: `50.96`
  * Upper +2.01σ Band: `51.86` | Lower -2.01σ Band: `51.06`
  * Upper +2.00σ Band: `51.86` | Lower -2.00σ Band: `51.06`
  * Upper +1.28σ Band: `51.71` | Lower -1.28σ Band: `51.21`
  * Upper +1.00σ Band: `51.66` | Lower -1.00σ Band: `51.26`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`51.42` | EMA-20=`51.50` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`51.81` (Slope: `+0.0000`) | EMA-100=`52.24`
  * Institutional Anchors: EMA-144=`52.51` | EMA-200=`52.76` (Slope: `-0.3334`) | EMA-233=`52.92`
- **Range Boundaries**: 24H High=`53.50` | 24H Low=`51.08` | Weekly High=`54.61` | Weekly Low=`51.08`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `51.63` (Distance: `+0.08%`)
  * Point of Control (POC) = `51.40` (Distance: `+0.53%`)
  * Value Area Low (VAL) = `51.15` (Distance: `+1.02%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`52.92` | POC=`52.45` | VAL=`51.99`
  * Prior Day Extremes: PDH=`54.37` | PDL=`51.95` | PDC=`52.13`
  * Monday Range Blueprint: High=`54.39` | Mid=`53.69` | Low=`52.99`
  * Developing Weekly Value Area: Weekly VAH=`54.53` | Weekly POC=`53.89` | Weekly VAL=`52.78`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`52.22` | Low=`51.08`
  * London Session (08:00-16:00 UTC): High=`51.79` | Low=`51.36`
  * New York Session (13:00-21:00 UTC): High=`66.46` | Low=`65.67`
  * Initial Balance (First Hour): IB High=`51.79` | IB Low=`51.36`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `65.80` - `66.33`
  * Optimal Trade Entry (OTE 0.705): `66.20`
  * Structural Invalidation Anchor (0.786): `66.59`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `51.53` | `51.55` | `51.50` | `51.53` | `1,105` | 56,943.97 USD | 6,391.67 USD | `+11.22%` | -903,284.24 USD | `+0.26` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `51.53` | `51.54` | `51.44` | `51.45` | `953` | 49,035.66 USD | -38,925.22 USD | `-79.38%` | -942,209.46 USD | `-0.34` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `51.45` | `51.47` | `51.27` | `51.37` | `2,121` | 108,951.53 USD | -23,535.65 USD | `-21.60%` | -965,745.11 USD | `-0.16` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `51.55` | `51.62` | `51.39` | `51.59` | `6,105` | 314,987.47 USD | 151,410.29 USD | `+48.07%` | -1,883,619.59 USD | `+1.13` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `51.59` | `51.63` | `51.44` | `51.45` | `3,156` | 162,388.82 USD | -132,316.82 USD | `-81.48%` | -2,015,936.41 USD | `-0.71` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `51.45` | `51.50` | `51.27` | `51.43` | `5,158` | 265,281.10 USD | 42,307.76 USD | `+15.95%` | -1,973,628.65 USD | `+0.42` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `51.92` | `52.06` | `51.73` | `51.78` | `13,804` | 714,757.32 USD | -415,480.10 USD | `-58.13%` | -2,210,138.85 USD | `-0.85` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `51.78` | `51.80` | `51.09` | `51.55` | `37,249` | 1,920,036.95 USD | -43,513.59 USD | `-2.27%` | -2,253,652.43 USD | `+0.15` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `51.55` | `51.63` | `51.24` | `51.37` | `18,586` | 954,818.58 USD | -375,019.18 USD | `-39.28%` | -2,628,671.62 USD | `-0.77` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.42` | `52.51` | `51.95` | `52.13` | `45,007` | 2,346,304.92 USD | -993,310.91 USD | `-42.34%` | -3,777,102.90 USD | `-0.05` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.14` | `52.22` | `51.73` | `51.78` | `24,880` | 1,288,261.52 USD | -1,001,103.02 USD | `-77.71%` | -4,778,205.92 USD | `-0.05` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `51.78` | `51.80` | `51.08` | `51.36` | `77,852` | 3,998,478.72 USD | -1,594,400.32 USD | `-39.88%` | -6,372,606.24 USD | `-0.66` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.74` | `53.07` | `52.30` | `52.37` | `60,050` | 3,144,818.50 USD | -2,040,047.85 USD | `-64.87%` | -3,330,572.26 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.37` | `52.76` | `51.98` | `52.42` | `110,375` | 5,785,526.38 USD | 546,780.27 USD | `+9.45%` | -2,783,791.99 USD | `+1.36` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `52.42` | `52.51` | `51.95` | `52.13` | `45,007` | 2,346,304.92 USD | -993,310.91 USD | `-42.34%` | -3,777,102.90 USD | `-0.05` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.14` | `52.22` | `51.73` | `51.78` | `24,880` | 1,288,261.52 USD | -1,001,103.02 USD | `-77.71%` | -4,778,205.92 USD | `-0.05` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `51.78` | `51.80` | `51.08` | `51.36` | `77,852` | 3,998,478.72 USD | -1,594,400.32 USD | `-39.88%` | -6,372,606.24 USD | `-0.66` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| `BID` | `51.69` | `161.1500` | 8,330.49 USD | 571,725.79 USD | `4 orders` | `-0.04%` | `-` |
| `BID` | `51.69` | `222.7400` | 11,514.10 USD | 583,239.89 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `51.69` | `223.6100` | 11,558.85 USD | 594,798.74 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `51.69` | `1.3100` | 67.72 USD | 594,866.45 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `51.69` | `283.7200` | 14,665.49 USD | 609,531.94 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `51.69` | `471.5800` | 24,375.03 USD | 633,906.97 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `51.70` | `11.6400` | 601.85 USD | 144,107.50 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `51.70` | `2511.8200` | 129,868.63 USD | 273,976.13 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `51.70` | `152.9100` | 7,905.75 USD | 281,881.88 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `51.70` | `50.5900` | 2,615.55 USD | 284,497.44 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `51.70` | `476.7900` | 24,650.04 USD | 309,147.48 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `51.70` | `175.5700` | 9,076.62 USD | 318,224.10 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `51.70` | `4566.7100` | 236,080.64 USD | 554,304.74 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `51.70` | `175.8500` | 9,090.57 USD | 563,395.30 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `51.71` | `435.0800` | 22,499.73 USD | 22,499.73 USD | `2 orders` | `-0.00%` | `-` |
| `BID` | `51.71` | `413.5900` | 21,387.57 USD | 43,887.29 USD | `5 orders` | `-0.01%` | `-` |
| `BID` | `51.71` | `1524.8700` | 78,852.55 USD | 122,739.85 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `51.71` | `142.7000` | 7,379.02 USD | 130,118.86 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `51.71` | `108.3000` | 5,599.87 USD | 135,718.73 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `51.71` | `150.6000` | 7,786.92 USD | 143,505.65 USD | `2 orders` | `-0.02%` | `-` |
| `ASK` | `51.72` | `28.1000` | 1,453.44 USD | 17,908.70 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `51.72` | `77.4800` | 4,007.50 USD | 16,455.26 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `51.72` | `65.5200` | 3,388.69 USD | 12,447.76 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `51.72` | `139.9700` | 7,239.11 USD | 9,059.06 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `51.72` | `35.1900` | 1,819.96 USD | 1,819.96 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `51.72` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 51.72` | `0.00%` | `-` |
| `ASK` | `51.73` | `763.8600` | 39,518.30 USD | 383,526.73 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `51.73` | `3111.4600` | 160,968.27 USD | 344,008.44 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `51.73` | `229.1800` | 11,856.17 USD | 183,040.17 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `51.73` | `135.3400` | 7,001.41 USD | 171,184.00 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `51.73` | `763.0000` | 39,470.75 USD | 164,182.59 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `51.73` | `99.6600` | 5,155.41 USD | 124,711.83 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `51.73` | `136.7200` | 7,072.39 USD | 119,556.42 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `51.73` | `224.6400` | 11,620.18 USD | 112,484.03 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `51.73` | `98.9600` | 5,118.90 USD | 100,863.86 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `51.73` | `1504.7800` | 77,836.25 USD | 95,744.95 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `51.74` | `87.5500` | 4,529.92 USD | 810,084.43 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `51.74` | `1960.1900` | 101,420.23 USD | 805,554.51 USD | `3 orders` | `+0.05%` | `-` |
| `ASK` | `51.74` | `695.1800` | 35,967.92 USD | 704,134.28 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `51.74` | `5414.1800` | 280,118.84 USD | 668,166.36 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `51.74` | `87.3800` | 4,520.78 USD | 388,047.51 USD | `1 orders` | `+0.04%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:04:06 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `117` | `0x5b5d...c060` | `SHORT` | 17,836,650.06 USD | `346,127.65` | `58.90` | `51.52` | `524.35` | 2,549,710.03 USD | `+14.29%` | `5X Cross` |
| `124` | `0x4692...164f` | `SHORT` | 15,995,148.89 USD | `310,392.55` | `52.89` | `51.52` | `253.69` | 422,189.09 USD | `+2.64%` | `5X Cross` |
| `206` | `0xacb6...efbd` | `SHORT` | 10,364,199.36 USD | `201,133.33` | `59.63` | `51.52` | `76.82` | 1,628,457.75 USD | `+15.71%` | `6X Cross` |
| `240` | `0xc26c...b8f4` | `LONG` | 9,351,172.44 USD | `181,463.41` | `55.43` | `51.52` | `0.000000` | -707,582.64 USD | `-7.57%` | `2X Cross` |
| `284` | `0x49e9...e1d0` | `SHORT` | 8,239,328.32 USD | `159,887.61` | `55.44` | `51.52` | `102.54` | 624,427.39 USD | `+7.58%` | `4X Cross` |
| `356` | `0x645b...87b8` | `LONG` | 6,593,839.93 USD | `127,956.22` | `56.57` | `51.52` | `0.000000` | -644,602.64 USD | `-9.78%` | `3X Cross` |
| `359` | `0xd8c5...99b0` | `SHORT` | 6,509,524.30 USD | `126,320.04` | `61.98` | `51.52` | `199.09` | 1,319,813.55 USD | `+20.28%` | `3X Cross` |
| `390` | `0xe9ff...5903` | `SHORT` | 5,820,880.07 USD | `112,996.08` | `60.07` | `51.52` | `178.40` | 967,070.74 USD | `+16.61%` | `5X Cross` |
| `617` | `0x9aa5...58af` | `LONG` | 3,671,102.70 USD | `71,243.43` | `61.59` | `51.52` | `0.000000` | -717,054.82 USD | `-19.53%` | `20X Cross` |
| `747` | `0x2056...8396` | `LONG` | 3,091,920.00 USD | `60,000.00` | `66.92` | `51.52` | `21.35` | -923,407.14 USD | `-29.87%` | `10X Cross` |
| `834` | `0x354b...6425` | `SHORT` | 2,740,090.94 USD | `53,172.61` | `51.37` | `51.52` | `252.92` | -8,670.94 USD | `-0.32%` | `10X Cross` |
| `880` | `0x0242...ffa1` | `SHORT` | 2,572,305.84 USD | `49,916.67` | `56.48` | `51.52` | `315.97` | 246,826.03 USD | `+9.60%` | `10X Cross` |
| `889` | `0x960b...f0fc` | `LONG` | 2,548,667.59 USD | `49,457.96` | `55.82` | `51.52` | `0.000000` | -212,269.43 USD | `-8.33%` | `25X Cross` |
| `973` | `0x8b9d...7b28` | `LONG` | 2,309,036.23 USD | `44,823.47` | `58.35` | `51.52` | `0.000000` | -306,412.31 USD | `-13.27%` | `10X Cross` |
| `1055` | `0x5647...e7de` | `LONG` | 2,074,583.68 USD | `40,262.07` | `57.38` | `51.52` | `0.000000` | -235,653.92 USD | `-11.36%` | `20X Cross` |
| `1062` | `0xa2ce...3126` | `LONG` | 2,060,560.00 USD | `40,000.00` | `74.30` | `51.52` | `0.000000` | -911,495.49 USD | `-44.24%` | `20X Cross` |
| `1090` | `0xb078...de15` | `SHORT` | 2,009,748.52 USD | `39,000.01` | `52.58` | `51.52` | `203.05` | 40,770.44 USD | `+2.03%` | `8X Cross` |
| `1412` | `0x3678...b209` | `LONG` | 1,545,960.00 USD | `30,000.00` | `57.15` | `51.52` | `0.000000` | -168,540.00 USD | `-10.90%` | `20X Cross` |
| `1413` | `0x5a88...d997` | `LONG` | 1,545,690.00 USD | `30,000.00` | `59.50` | `51.52` | `38.04` | -239,197.59 USD | `-15.48%` | `25X Cross` |
| `1648` | `0x7ea9...fc7f` | `LONG` | 1,287,850.00 USD | `25,000.00` | `53.60` | `51.52` | `35.19` | -52,154.05 USD | `-4.05%` | `25X Cross` |
| `1786` | `0xf517...c032` | `LONG` | 1,165,972.45 USD | `22,627.50` | `66.29` | `51.52` | `0.000000` | -334,022.66 USD | `-28.65%` | `20X Cross` |
| `1793` | `0x24fb...ed0f` | `LONG` | 1,161,898.27 USD | `22,555.00` | `51.37` | `51.52` | `0.000000` | 3,231.69 USD | `+0.28%` | `20X Cross` |
| `1821` | `0xce97...7e78` | `LONG` | 1,141,924.89 USD | `22,160.82` | `51.51` | `51.52` | `0.000000` | 350.98 USD | `+0.03%` | `5X Cross` |
| `1917` | `0xcc9f...d218` | `LONG` | 1,057,406.00 USD | `20,520.60` | `52.63` | `51.52` | `26.86` | -22,502.05 USD | `-2.13%` | `2X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `53.10` | 5,409.62 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Short: 5.41K USD at 53.0980 USD [API] | `2026-10-29 03:22:16` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`53.36` (Vol: 4,300,000.00 USD, Dist: `+3.53%`) | Long MP=`51.16` (Vol: 1,900,000.00 USD, Dist: `--0.75%`)
  * 48H Horizon: Short MP=`54.84` (Vol: 4,200,000.00 USD, Dist: `+6.41%`) | Long MP=`51.17` (Vol: 2,500,000.00 USD, Dist: `--0.72%`)
  * 3D Horizon: Short MP=`55.09` (Vol: 5,200,000.00 USD, Dist: `+6.89%`) | Long MP=`51.17` (Vol: 2,900,000.00 USD, Dist: `--0.72%`)
  * 7D Horizon: Short MP=`55.09` (Vol: 7,800,000.00 USD, Dist: `+6.89%`) | Long MP=`51.17` (Vol: 2,900,000.00 USD, Dist: `--0.72%`)
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
  * Current Rate: `7.74K` | Last 24h: `209.74K` | Last 3d: `432.77K` | Last 7d: `624.53K`
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
  * `2026-10-30 10:58:46 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:58:46 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:57:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:57:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:57:46 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:59:46 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:59:46 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:59:46 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:59:46 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 05:59:46 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:59:46 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:59:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:59:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:59:46 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:59:46 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `51.15` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `50.83` (Risk Distance: `0.3248` pts)
  * +2.5R Take Profit: `51.96`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.02 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `51.63` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `51.95` (Risk Distance: `0.3248` pts)
  * +2.5R Take Profit: `50.82`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.02 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`66.59`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
