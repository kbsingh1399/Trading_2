# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAGSGD
**Canonical Key**: `XAGSGD` | **Broker Instrument**: `XAGSGD.pi` | **Asset Class**: `Forex Exotic`
**Timestamp**: `2026-10-30 16:55:01 IST` (`2026-10-30 11:25:01 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `64.35` | **Live Ask Quote**: `64.37` | **Mid Price**: `64.36`
- **Spread Points**: `15.00` | **Spread BPS**: `2.33 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `51.16` | VWAP Z-Score: `-1.93` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.1809` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `29.66` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `52.33` | Lower -3.00σ Band: `49.99`
  * Upper +2.51σ Band: `52.14` | Lower -2.51σ Band: `50.18`
  * Upper +2.01σ Band: `51.95` | Lower -2.01σ Band: `50.38`
  * Upper +2.00σ Band: `51.94` | Lower -2.00σ Band: `50.38`
  * Upper +1.28σ Band: `51.66` | Lower -1.28σ Band: `50.66`
  * Upper +1.00σ Band: `51.55` | Lower -1.00σ Band: `50.77`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`50.59` | EMA-20=`50.74` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`51.15` (Slope: `+0.0000`) | EMA-100=`51.68`
  * Institutional Anchors: EMA-144=`52.03` | EMA-200=`52.38` (Slope: `-0.4155`) | EMA-233=`52.59`
- **Range Boundaries**: 24H High=`53.07` | 24H Low=`50.40` | Weekly High=`54.61` | Weekly Low=`50.40`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `52.07` (Distance: `-3.26%`)
  * Point of Control (POC) = `51.41` (Distance: `-2.01%`)
  * Value Area Low (VAL) = `50.85` (Distance: `-0.95%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`52.92` | POC=`52.45` | VAL=`51.99`
  * Prior Day Extremes: PDH=`54.37` | PDL=`51.95` | PDC=`52.13`
  * Monday Range Blueprint: High=`54.39` | Mid=`53.69` | Low=`52.99`
  * Developing Weekly Value Area: Weekly VAH=`54.51` | Weekly POC=`53.89` | Weekly VAL=`52.64`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`52.22` | Low=`51.08`
  * London Session (08:00-16:00 UTC): High=`51.79` | Low=`50.35`
  * New York Session (13:00-21:00 UTC): High=`50.77` | Low=`50.35`
  * Initial Balance (First Hour): IB High=`51.79` | IB Low=`50.87`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `64.10` - `64.62`
  * Optimal Trade Entry (OTE 0.705): `64.49`
  * Structural Invalidation Anchor (0.786): `64.87`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `50.61` | `50.71` | `50.57` | `50.64` | `2,114` | 107,046.62 USD | 9,041.10 USD | `+8.45%` | -1,295,766.97 USD | `+0.53` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `50.64` | `50.67` | `50.56` | `50.60` | `1,311` | 66,332.67 USD | -22,627.50 USD | `-34.11%` | -1,318,394.47 USD | `-0.41` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `50.60` | `50.66` | `50.56` | `50.64` | `1,281` | 64,872.40 USD | 32,111.84 USD | `+49.50%` | -1,286,282.63 USD | `+1.36` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `50.65` | `50.74` | `50.57` | `50.67` | `2,542` | 128,813.31 USD | 22,485.16 USD | `+17.46%` | -1,942,678.16 USD | `+0.47` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `50.67` | `50.71` | `50.40` | `50.61` | `3,016` | 152,627.70 USD | 7,116.08 USD | `+4.66%` | -1,935,562.08 USD | `+0.31` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `50.61` | `50.71` | `50.56` | `50.64` | `4,706` | 238,321.25 USD | 35,593.43 USD | `+14.94%` | -1,899,968.65 USD | `+0.51` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `51.08` | `51.12` | `50.66` | `50.78` | `20,835` | 1,057,959.63 USD | -603,060.14 USD | `-57.00%` | -2,722,809.76 USD | `-1.27` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `50.78` | `50.87` | `50.40` | `50.61` | `11,199` | 566,736.59 USD | -139,241.32 USD | `-24.57%` | -2,862,051.08 USD | `+0.02` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `50.61` | `50.93` | `50.56` | `50.89` | `14,682` | 747,196.34 USD | 590,853.63 USD | `+79.08%` | -2,271,197.45 USD | `+1.75` | **`BULLISH`** | `AGGRESSIVE BUYING` |
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
| `BID` | `50.38` | `3988.0300` | 200,936.89 USD | 724,584.65 USD | `6 orders` | `-0.03%` | `-` |
| `BID` | `50.38` | `56.1000` | 2,826.54 USD | 727,411.19 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `50.38` | `193.3100` | 9,739.54 USD | 737,150.73 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `50.38` | `4418.0800` | 222,587.29 USD | 959,738.02 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `50.38` | `229.3500` | 11,554.65 USD | 971,292.67 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `50.38` | `142.0700` | 7,157.34 USD | 978,450.01 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `50.39` | `114.5000` | 5,770.11 USD | 62,611.76 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `50.39` | `2182.0600` | 109,960.55 USD | 172,572.31 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `50.39` | `408.4400` | 20,582.11 USD | 193,154.42 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `50.39` | `274.3300` | 13,823.76 USD | 206,978.19 USD | `5 orders` | `-0.02%` | `-` |
| `BID` | `50.39` | `79.9200` | 4,027.17 USD | 211,005.35 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `50.39` | `295.5300` | 14,890.87 USD | 225,896.22 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `50.39` | `5909.4100` | 297,751.53 USD | 523,647.76 USD | `4 orders` | `-0.03%` | `-` |
| `ASK` | `50.40` | `36.5100` | 1,840.21 USD | 1,840.21 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `50.40` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 50.40` | `0.00%` | `-` |
| `BID` | `50.40` | `73.8300` | 3,721.18 USD | 3,721.18 USD | `2 orders` | `-0.00%` | `-` |
| `BID` | `50.40` | `69.7000` | 3,512.95 USD | 7,234.13 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `50.40` | `182.4500` | 9,195.48 USD | 16,429.61 USD | `2 orders` | `-0.00%` | `-` |
| `BID` | `50.40` | `44.4600` | 2,240.74 USD | 18,670.35 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `50.40` | `182.4500` | 9,195.12 USD | 27,865.46 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `50.40` | `574.7600` | 28,965.60 USD | 56,831.07 USD | `6 orders` | `-0.01%` | `-` |
| `BID` | `50.40` | `0.2100` | 10.58 USD | 56,841.65 USD | `1 orders` | `-0.01%` | `-` |
| `ASK` | `50.41` | `247.7400` | 12,489.81 USD | 299,845.26 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `50.41` | `79.1800` | 3,991.78 USD | 287,355.45 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `50.41` | `3445.3200` | 173,688.92 USD | 283,363.67 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `50.41` | `158.4900` | 7,989.64 USD | 109,674.75 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `50.41` | `80.6800` | 4,067.00 USD | 101,685.11 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `50.41` | `136.6800` | 6,889.63 USD | 97,618.11 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `50.41` | `61.1500` | 3,082.33 USD | 90,728.48 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `50.41` | `1702.3300` | 85,805.94 USD | 87,646.16 USD | `3 orders` | `+0.00%` | `-` |
| `ASK` | `50.42` | `193.8900` | 9,776.71 USD | 976,167.07 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `50.42` | `5740.5000` | 289,447.49 USD | 966,390.36 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `50.42` | `5951.3400` | 300,072.51 USD | 676,942.86 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `50.42` | `387.2000` | 19,522.62 USD | 376,870.35 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `50.42` | `519.6200` | 26,198.72 USD | 357,347.73 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `50.42` | `198.3900` | 10,002.43 USD | 331,149.01 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `50.42` | `54.6400` | 2,754.78 USD | 321,146.58 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `50.42` | `367.8700` | 18,546.53 USD | 318,391.79 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `50.43` | `5907.7800` | 297,923.44 USD | 1,349,038.51 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `50.43` | `930.9800` | 46,947.46 USD | 1,051,115.07 USD | `3 orders` | `+0.05%` | `-` |
| `ASK` | `50.43` | `555.2800` | 28,000.55 USD | 1,004,167.61 USD | `1 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:52:59 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `117` | `0x5b5d...c060` | `SHORT` | 17,462,486.07 USD | `346,127.65` | `58.90` | `50.48` | `489.88` | 2,923,874.02 USD | `+16.74%` | `5X Cross` |
| `126` | `0x4692...164f` | `SHORT` | 15,601,716.69 USD | `309,165.28` | `52.13` | `50.48` | `260.63` | 513,585.10 USD | `+3.29%` | `5X Cross` |
| `208` | `0xacb6...efbd` | `SHORT` | 10,148,383.30 USD | `201,133.33` | `59.63` | `50.48` | `77.15` | 1,844,273.82 USD | `+18.17%` | `6X Cross` |
| `246` | `0xc26c...b8f4` | `LONG` | 9,155,010.50 USD | `181,463.41` | `55.43` | `50.48` | `0.000000` | -903,744.58 USD | `-9.87%` | `2X Cross` |
| `279` | `0x49e9...e1d0` | `SHORT` | 8,365,064.92 USD | `165,789.30` | `55.17` | `50.48` | `99.85` | 782,370.10 USD | `+9.35%` | `4X Cross` |
| `362` | `0x645b...87b8` | `LONG` | 6,486,833.69 USD | `128,576.91` | `56.54` | `50.48` | `0.000000` | -783,235.55 USD | `-12.07%` | `3X Cross` |
| `363` | `0xd8c5...99b0` | `SHORT` | 6,372,972.34 USD | `126,320.04` | `61.98` | `50.48` | `198.35` | 1,456,365.51 USD | `+22.85%` | `3X Cross` |
| `396` | `0xe9ff...5903` | `SHORT` | 5,701,104.22 USD | `112,996.08` | `60.07` | `50.48` | `171.01` | 1,086,846.58 USD | `+19.06%` | `5X Cross` |
| `669` | `0xfc66...ca06` | `SHORT` | 3,366,758.75 USD | `66,716.05` | `50.61` | `50.48` | `329.17` | 9,575.71 USD | `+0.28%` | `7X Cross` |
| `760` | `0x2056...8396` | `LONG` | 3,027,180.00 USD | `60,000.00` | `66.92` | `50.48` | `21.36` | -988,147.14 USD | `-32.64%` | `10X Cross` |
| `762` | `0x9aa5...58af` | `LONG` | 3,020,921.81 USD | `59,872.40` | `61.59` | `50.48` | `0.000000` | -666,850.13 USD | `-22.07%` | `20X Cross` |
| `884` | `0x0242...ffa1` | `SHORT` | 2,518,994.83 USD | `49,916.67` | `56.48` | `50.48` | `334.01` | 300,137.03 USD | `+11.91%` | `10X Cross` |
| `894` | `0x960b...f0fc` | `LONG` | 2,495,203.54 USD | `49,457.96` | `55.82` | `50.48` | `0.000000` | -265,733.49 USD | `-10.65%` | `25X Cross` |
| `978` | `0x8b9d...7b28` | `LONG` | 2,261,747.47 USD | `44,823.47` | `58.35` | `50.48` | `0.000000` | -353,701.07 USD | `-15.64%` | `10X Cross` |
| `1068` | `0x5647...e7de` | `LONG` | 2,031,664.31 USD | `40,262.07` | `57.38` | `50.48` | `0.000000` | -278,573.29 USD | `-13.71%` | `20X Cross` |
| `1079` | `0xa2ce...3126` | `LONG` | 2,018,320.00 USD | `40,000.00` | `74.30` | `50.48` | `0.000000` | -953,735.49 USD | `-47.25%` | `20X Cross` |
| `1109` | `0xb078...de15` | `SHORT` | 1,967,589.50 USD | `39,000.01` | `52.58` | `50.48` | `206.30` | 82,929.45 USD | `+4.21%` | `8X Cross` |
| `1437` | `0x5a88...d997` | `LONG` | 1,513,560.00 USD | `30,000.00` | `59.50` | `50.48` | `38.16` | -271,327.59 USD | `-17.93%` | `25X Cross` |
| `1438` | `0x3678...b209` | `LONG` | 1,513,530.00 USD | `30,000.00` | `57.15` | `50.48` | `0.000000` | -200,970.00 USD | `-13.28%` | `20X Cross` |
| `1637` | `0xed62...e004` | `SHORT` | 1,294,595.36 USD | `25,660.45` | `50.81` | `50.48` | `54.73` | 9,212.10 USD | `+0.71%` | `25X Cross` |
| `1670` | `0x7ea9...fc7f` | `LONG` | 1,261,450.00 USD | `25,000.00` | `53.60` | `50.48` | `35.39` | -78,554.05 USD | `-6.23%` | `25X Cross` |
| `1728` | `0x24fb...ed0f` | `LONG` | 1,216,566.49 USD | `24,110.00` | `51.32` | `50.48` | `0.000000` | -20,724.59 USD | `-1.70%` | `20X Cross` |
| `1814` | `0xf517...c032` | `LONG` | 1,141,693.14 USD | `22,627.50` | `66.29` | `50.48` | `0.000000` | -358,301.96 USD | `-31.38%` | `20X Cross` |
| `1864` | `0x9e11...22a3` | `LONG` | 1,107,197.14 USD | `21,945.99` | `50.67` | `50.48` | `34.46` | -4,725.26 USD | `-0.43%` | `3X Isolated` |
| `1915` | `0xce97...7e78` | `LONG` | 1,053,094.42 USD | `20,871.54` | `50.74` | `50.48` | `0.000000` | -5,939.11 USD | `-0.56%` | `5X Cross` |
| `1941` | `0xcc9f...d218` | `LONG` | 1,035,387.39 USD | `20,520.60` | `52.63` | `50.48` | `26.87` | -44,520.66 USD | `-4.30%` | `2X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `77.50` | 38,750.00 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 38.75K USD at 77.5000 USD [API] | `2026-01-30 18:21:38` |
| `ANNOUNCEMENT` | `INFO` | `80.86` | 2,533.31 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 2.53K USD at 80.8590 USD [API] | `2026-01-30 18:17:17` |
| `ANNOUNCEMENT` | `INFO` | `80.86` | 4,990.62 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 4.99K USD at 80.8590 USD [API] | `2026-01-30 18:17:17` |
| `ANNOUNCEMENT` | `INFO` | `80.86` | 55.79 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 0.06K USD at 80.8610 USD [API] | `2026-01-30 18:17:17` |
| `ANNOUNCEMENT` | `INFO` | `80.87` | 7,164.82 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 7.16K USD at 80.8670 USD [API] | `2026-01-30 18:17:17` |
| `ANNOUNCEMENT` | `INFO` | `80.88` | 25,691.71 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 25.69K USD at 80.8780 USD [API] | `2026-01-30 18:17:17` |
| `ANNOUNCEMENT` | `INFO` | `84.07` | 1,894.12 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 1.89K USD at 84.0710 USD [API] | `2026-01-30 18:09:32` |
| `ANNOUNCEMENT` | `INFO` | `84.07` | 280.81 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 0.28K USD at 84.0740 USD [API] | `2026-01-30 18:09:32` |
| `ANNOUNCEMENT` | `INFO` | `84.08` | 300.16 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 0.30K USD at 84.0780 USD [API] | `2026-01-30 18:09:32` |
| `ANNOUNCEMENT` | `INFO` | `84.08` | 16,982.48 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 16.98K USD at 84.0800 USD [API] | `2026-01-30 18:09:32` |
| `ANNOUNCEMENT` | `INFO` | `84.08` | 2,932.75 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 2.93K USD at 84.0810 USD [API] | `2026-01-30 18:09:32` |
| `ANNOUNCEMENT` | `INFO` | `84.08` | 219.45 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 0.22K USD at 84.0820 USD [API] | `2026-01-30 18:09:32` |
| `ANNOUNCEMENT` | `INFO` | `84.08` | 315.31 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 0.32K USD at 84.0820 USD [API] | `2026-01-30 18:09:32` |
| `ANNOUNCEMENT` | `INFO` | `84.09` | 2,609.34 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 2.61K USD at 84.0910 USD [API] | `2026-01-30 18:09:32` |
| `ANNOUNCEMENT` | `INFO` | `84.09` | 4,204.55 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 4.20K USD at 84.0910 USD [API] | `2026-01-30 18:09:32` |
| `ANNOUNCEMENT` | `INFO` | `84.09` | 301.89 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 0.30K USD at 84.0910 USD [API] | `2026-01-30 18:09:32` |
| `ANNOUNCEMENT` | `INFO` | `84.09` | 433.91 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 0.43K USD at 84.0910 USD [API] | `2026-01-30 18:09:32` |
| `ANNOUNCEMENT` | `INFO` | `84.09` | 420.46 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 0.42K USD at 84.0920 USD [API] | `2026-01-30 18:09:32` |
| `ANNOUNCEMENT` | `INFO` | `84.09` | 11,147.37 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 11.15K USD at 84.0930 USD [API] | `2026-01-30 18:09:32` |
| `ANNOUNCEMENT` | `INFO` | `86.18` | 14,853.47 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 14.85K USD at 86.1770 USD [API] | `2026-01-30 17:53:32` |
| `ANNOUNCEMENT` | `INFO` | `86.18` | 24,224.35 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 24.22K USD at 86.1770 USD [API] | `2026-01-30 17:53:32` |
| `ANNOUNCEMENT` | `INFO` | `86.19` | 4,011.24 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 4.01K USD at 86.1890 USD [API] | `2026-01-30 17:53:32` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`52.71` (Vol: 3,600,000.00 USD, Dist: `+4.03%`) | Long MP=`50.23` (Vol: 3,100,000.00 USD, Dist: `--0.86%`)
  * 48H Horizon: Short MP=`54.87` (Vol: 4,200,000.00 USD, Dist: `+8.28%`) | Long MP=`50.60` (Vol: 2,100,000.00 USD, Dist: `--0.13%`)
  * 3D Horizon: Short MP=`54.97` (Vol: 5,200,000.00 USD, Dist: `+8.49%`) | Long MP=`50.60` (Vol: 2,100,000.00 USD, Dist: `--0.13%`)
  * 7D Horizon: Short MP=`55.07` (Vol: 7,100,000.00 USD, Dist: `+8.69%`) | Long MP=`50.60` (Vol: 2,100,000.00 USD, Dist: `--0.13%`)
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
  * Current Rate: `47.93K` | Last 24h: `158.28K` | Last 3d: `386.46K` | Last 7d: `548.84K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `-` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `0.0097%` | **USDT BingX** | `-` |
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
  * `2026-10-30 16:36:03 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:26:03 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:50:03 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:49:03 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)


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
  * Execution Entry: `50.85` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `50.62` (Risk Distance: `0.2396` pts)
  * +2.5R Take Profit: `51.45`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.01 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `52.07` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `52.31` (Risk Distance: `0.2396` pts)
  * +2.5R Take Profit: `51.47`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.01 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`64.87`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
