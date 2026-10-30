# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAGSGD
**Canonical Key**: `XAGSGD` | **Broker Instrument**: `XAGSGD.pi` | **Asset Class**: `Forex Exotic`
**Timestamp**: `2026-10-30 10:49:58 IST` (`2026-10-30 05:19:58 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `65.82` | **Live Ask Quote**: `65.85` | **Mid Price**: `65.84`
- **Spread Points**: `28.00` | **Spread BPS**: `4.25 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `65.84` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `66.30` | Lower -3.00σ Band: `65.38`
  * Upper +2.51σ Band: `66.20` | Lower -2.51σ Band: `65.48`
  * Upper +2.01σ Band: `66.11` | Lower -2.01σ Band: `65.56`
  * Upper +2.00σ Band: `66.10` | Lower -2.00σ Band: `65.57`
  * Upper +1.28σ Band: `66.02` | Lower -1.28σ Band: `65.65`
  * Upper +1.00σ Band: `65.97` | Lower -1.00σ Band: `65.71`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`65.84` | EMA-20=`65.84` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`65.84` (Slope: `+0.0000`) | EMA-100=`65.84`
  * Institutional Anchors: EMA-144=`65.84` | EMA-200=`65.84` (Slope: `+0.0000`) | EMA-233=`65.84`
- **Range Boundaries**: 24H High=`66.50` | 24H Low=`65.18` | Weekly High=`67.15` | Weekly Low=`64.52`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `51.63` (Distance: `-0.24%`)
  * Point of Control (POC) = `51.39` (Distance: `+0.22%`)
  * Value Area Low (VAL) = `51.16` (Distance: `+0.69%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`52.92` | POC=`52.45` | VAL=`51.99`
  * Prior Day Extremes: PDH=`54.37` | PDL=`51.95` | PDC=`52.13`
  * Monday Range Blueprint: High=`54.39` | Mid=`53.69` | Low=`52.99`
  * Developing Weekly Value Area: Weekly VAH=`54.53` | Weekly POC=`53.89` | Weekly VAL=`52.81`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`52.22` | Low=`51.08`
  * London Session (08:00-16:00 UTC): High=`51.56` | Low=`51.36`
  * New York Session (13:00-21:00 UTC): High=`66.23` | Low=`65.44`
  * Initial Balance (First Hour): IB High=`51.56` | IB Low=`51.36`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `65.57` - `66.10`
  * Optimal Trade Entry (OTE 0.705): `65.97`
  * Structural Invalidation Anchor (0.786): `66.36`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `51.55` | `51.58` | `51.44` | `51.45` | `2,227` | 114,583.60 USD | -84,535.46 USD | `-73.78%` | -984,643.98 USD | `-0.94` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `51.45` | `51.61` | `51.39` | `51.55` | `2,154` | 111,047.32 USD | 51,521.95 USD | `+46.40%` | -933,122.02 USD | `+0.83` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `51.55` | `51.62` | `51.51` | `51.59` | `1,724` | 88,949.78 USD | 38,067.49 USD | `+42.80%` | -895,054.53 USD | `+0.61` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `51.47` | `51.50` | `51.19` | `51.26` | `9,598` | 491,945.49 USD | -321,286.88 USD | `-65.31%` | -2,292,742.04 USD | `-2.08` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `51.26` | `51.63` | `51.10` | `51.55` | `6,872` | 354,224.11 USD | 217,547.07 USD | `+61.42%` | -2,075,194.97 USD | `+1.71` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `51.55` | `51.62` | `51.39` | `51.59` | `6,105` | 314,987.47 USD | 151,410.29 USD | `+48.07%` | -1,923,784.68 USD | `+1.13` | **`BULLISH`** | `AGGRESSIVE BUYING` |
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
| `BID` | `51.50` | `587.6100` | 30,264.27 USD | 933,142.11 USD | `4 orders` | `-0.04%` | `-` |
| `BID` | `51.50` | `5465.8500` | 281,507.67 USD | 1,214,649.79 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `51.50` | `681.8600` | 35,117.15 USD | 1,249,766.94 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `51.50` | `87.2900` | 4,495.44 USD | 1,254,262.37 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `51.50` | `154.0300` | 7,932.39 USD | 1,262,194.77 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `51.51` | `59.3200` | 3,055.81 USD | 120,666.72 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `51.51` | `493.2100` | 25,406.73 USD | 146,073.45 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `51.51` | `66.5200` | 3,426.58 USD | 149,500.02 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `51.51` | `4094.3800` | 210,905.61 USD | 360,405.63 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `51.51` | `85.9600` | 4,427.80 USD | 364,833.43 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `51.51` | `10310.4300` | 531,049.01 USD | 895,882.44 USD | `6 orders` | `-0.04%` | `-` |
| `BID` | `51.51` | `135.8200` | 6,995.41 USD | 902,877.85 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `51.52` | `19.6000` | 1,009.89 USD | 1,022.26 USD | `2 orders` | `-0.00%` | `-` |
| `BID` | `51.52` | `1699.6100` | 87,565.61 USD | 88,587.86 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `51.52` | `88.7200` | 4,570.85 USD | 93,158.72 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `51.52` | `157.4100` | 8,109.61 USD | 101,268.32 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `51.52` | `64.3000` | 3,312.61 USD | 104,580.93 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `51.52` | `144.2300` | 7,430.30 USD | 112,011.23 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `51.52` | `108.7000` | 5,599.68 USD | 117,610.91 USD | `1 orders` | `-0.02%` | `-` |
| `ASK` | `51.53` | `86.5700` | 4,461.38 USD | 128,659.40 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `51.53` | `1858.0200` | 95,751.20 USD | 124,198.02 USD | `6 orders` | `+0.01%` | `-` |
| `ASK` | `51.53` | `106.9100` | 5,509.39 USD | 28,446.82 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `51.53` | `27.6100` | 1,422.80 USD | 22,937.42 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `51.53` | `27.6100` | 1,422.74 USD | 21,514.63 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `51.53` | `170.0400` | 8,761.99 USD | 20,091.88 USD | `3 orders` | `+0.00%` | `-` |
| `ASK` | `51.53` | `134.1500` | 6,912.48 USD | 11,329.89 USD | `2 orders` | `+0.00%` | `-` |
| `ASK` | `51.53` | `85.7300` | 4,417.41 USD | 4,417.41 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `51.53` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 51.53` | `0.00%` | `-` |
| `BID` | `51.53` | `0.2400` | 12.37 USD | 12.37 USD | `1 orders` | `-0.00%` | `-` |
| `ASK` | `51.54` | `37.3500` | 1,925.17 USD | 311,049.98 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `51.54` | `164.9100` | 8,499.79 USD | 309,124.81 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `51.54` | `3093.0800` | 159,420.44 USD | 300,625.02 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `51.54` | `15.6700` | 807.63 USD | 141,204.59 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `51.54` | `27.6100` | 1,422.99 USD | 140,396.95 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `51.54` | `29.0100` | 1,495.12 USD | 138,973.96 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `51.54` | `85.1800` | 4,389.92 USD | 137,478.85 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `51.54` | `85.9500` | 4,429.52 USD | 133,088.92 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `51.55` | `142.2700` | 7,334.30 USD | 930,976.94 USD | `3 orders` | `+0.05%` | `-` |
| `ASK` | `51.55` | `11718.2500` | 604,075.79 USD | 923,642.64 USD | `4 orders` | `+0.05%` | `-` |
| `ASK` | `51.55` | `85.9500` | 4,430.38 USD | 319,566.85 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `51.55` | `79.2800` | 4,086.49 USD | 315,136.47 USD | `1 orders` | `+0.04%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:43:23 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `117` | `0x5b5d...c060` | `SHORT` | 17,830,419.76 USD | `346,127.65` | `58.90` | `51.50` | `524.81` | 2,555,940.33 USD | `+14.33%` | `5X Cross` |
| `124` | `0x4692...164f` | `SHORT` | 15,990,452.59 USD | `310,427.92` | `52.90` | `51.50` | `253.65` | 429,762.18 USD | `+2.69%` | `5X Cross` |
| `206` | `0xacb6...efbd` | `SHORT` | 10,361,182.36 USD | `201,133.33` | `59.63` | `51.50` | `76.83` | 1,631,474.75 USD | `+15.75%` | `6X Cross` |
| `240` | `0xc26c...b8f4` | `LONG` | 9,347,906.10 USD | `181,463.41` | `55.43` | `51.50` | `0.000000` | -710,848.98 USD | `-7.60%` | `2X Cross` |
| `285` | `0x49e9...e1d0` | `SHORT` | 8,236,450.34 USD | `159,887.61` | `55.44` | `51.50` | `102.51` | 627,305.37 USD | `+7.62%` | `4X Cross` |
| `356` | `0x645b...87b8` | `LONG` | 6,591,152.85 USD | `127,956.22` | `56.57` | `51.50` | `0.000000` | -647,289.72 USD | `-9.82%` | `3X Cross` |
| `359` | `0xd8c5...99b0` | `SHORT` | 6,507,250.54 USD | `126,320.04` | `61.98` | `51.50` | `199.12` | 1,322,087.31 USD | `+20.32%` | `3X Cross` |
| `389` | `0xe9ff...5903` | `SHORT` | 5,820,993.06 USD | `112,996.08` | `60.07` | `51.50` | `178.35` | 966,957.74 USD | `+16.61%` | `5X Cross` |
| `616` | `0x9aa5...58af` | `LONG` | 3,669,820.32 USD | `71,243.43` | `61.59` | `51.50` | `0.000000` | -718,337.20 USD | `-19.57%` | `20X Cross` |
| `744` | `0x2056...8396` | `LONG` | 3,090,660.00 USD | `60,000.00` | `66.92` | `51.50` | `21.35` | -924,667.14 USD | `-29.92%` | `10X Cross` |
| `813` | `0x354b...6425` | `SHORT` | 2,808,922.42 USD | `54,527.36` | `51.37` | `51.50` | `247.70` | -7,910.37 USD | `-0.28%` | `10X Cross` |
| `881` | `0x0242...ffa1` | `SHORT` | 2,571,257.59 USD | `49,916.67` | `56.48` | `51.50` | `316.86` | 247,874.28 USD | `+9.64%` | `10X Cross` |
| `889` | `0x960b...f0fc` | `LONG` | 2,547,777.35 USD | `49,457.96` | `55.82` | `51.50` | `0.000000` | -213,159.68 USD | `-8.37%` | `25X Cross` |
| `973` | `0x8b9d...7b28` | `LONG` | 2,309,081.06 USD | `44,823.47` | `58.35` | `51.50` | `0.000000` | -306,367.49 USD | `-13.27%` | `10X Cross` |
| `1053` | `0x5647...e7de` | `LONG` | 2,074,060.27 USD | `40,262.07` | `57.38` | `51.50` | `0.000000` | -236,177.33 USD | `-11.39%` | `20X Cross` |
| `1061` | `0xa2ce...3126` | `LONG` | 2,060,600.00 USD | `40,000.00` | `74.30` | `51.50` | `0.000000` | -911,455.49 USD | `-44.23%` | `20X Cross` |
| `1091` | `0xb078...de15` | `SHORT` | 2,009,046.52 USD | `39,000.01` | `52.58` | `51.50` | `203.33` | 41,472.44 USD | `+2.06%` | `8X Cross` |
| `1413` | `0x5a88...d997` | `LONG` | 1,545,420.00 USD | `30,000.00` | `59.50` | `51.50` | `38.08` | -239,467.59 USD | `-15.50%` | `25X Cross` |
| `1414` | `0x3678...b209` | `LONG` | 1,545,420.00 USD | `30,000.00` | `57.15` | `51.50` | `0.000000` | -169,080.00 USD | `-10.94%` | `20X Cross` |
| `1646` | `0x7ea9...fc7f` | `LONG` | 1,287,825.00 USD | `25,000.00` | `53.60` | `51.50` | `35.19` | -52,179.05 USD | `-4.05%` | `25X Cross` |
| `1748` | `0x24fb...ed0f` | `LONG` | 1,190,511.65 USD | `23,110.00` | `51.37` | `51.50` | `0.000000` | 3,334.32 USD | `+0.28%` | `20X Cross` |
| `1788` | `0xf517...c032` | `LONG` | 1,165,565.15 USD | `22,627.50` | `66.29` | `51.50` | `0.000000` | -334,429.95 USD | `-28.69%` | `20X Cross` |
| `1822` | `0xce97...7e78` | `LONG` | 1,143,515.50 USD | `22,198.15` | `51.51` | `51.50` | `0.000000` | 18.60 USD | `+0.00%` | `5X Cross` |
| `1918` | `0xcc9f...d218` | `LONG` | 1,057,098.19 USD | `20,520.60` | `52.63` | `51.50` | `26.86` | -22,809.86 USD | `-2.16%` | `2X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


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
  * Current Rate: `8.18K` | Last 24h: `209.74K` | Last 3d: `432.77K` | Last 7d: `624.53K`
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
  * `2026-10-30 09:50:40 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:48:40 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:47:40 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:47:40 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:47:40 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:49:40 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:49:40 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:49:40 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:49:40 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `51.16` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `49.91` (Risk Distance: `1.24` pts)
  * +2.5R Take Profit: `54.26`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.06 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `51.63` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `52.87` (Risk Distance: `1.24` pts)
  * +2.5R Take Profit: `48.52`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.06 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`66.36`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
