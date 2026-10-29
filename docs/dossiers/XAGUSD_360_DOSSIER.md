# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAGUSD
**Canonical Key**: `XAGUSD` | **Broker Instrument**: `XAGUSD.pi` | **Asset Class**: `Precious Metal`
**Timestamp**: `2026-10-29 23:49:57 IST` (`2026-10-29 18:19:57 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `52.11` | **Live Ask Quote**: `52.17` | **Mid Price**: `52.14`
- **Spread Points**: `58.00` | **Spread BPS**: `11.12 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `52.78` | VWAP Z-Score: `-1.26` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.2298` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `38.71` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `54.38` | Lower -3.00σ Band: `51.18`
  * Upper +2.51σ Band: `54.12` | Lower -2.51σ Band: `51.44`
  * Upper +2.01σ Band: `53.85` | Lower -2.01σ Band: `51.71`
  * Upper +2.00σ Band: `53.85` | Lower -2.00σ Band: `51.71`
  * Upper +1.28σ Band: `53.46` | Lower -1.28σ Band: `52.10`
  * Upper +1.00σ Band: `53.31` | Lower -1.00σ Band: `52.25`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`52.22` | EMA-20=`52.34` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`52.60` (Slope: `+0.0000`) | EMA-100=`52.95`
  * Institutional Anchors: EMA-144=`53.12` | EMA-200=`53.28` (Slope: `-0.2330`) | EMA-233=`53.35`
- **Range Boundaries**: 24H High=`54.61` | 24H Low=`51.97` | Weekly High=`54.61` | Weekly Low=`51.97`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `52.98` (Distance: `-1.62%`)
  * Point of Control (POC) = `52.45` (Distance: `-0.63%`)
  * Value Area Low (VAL) = `51.99` (Distance: `+0.26%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`54.10` | POC=`53.83` | VAL=`53.54`
  * Prior Day Extremes: PDH=`54.61` | PDL=`53.28` | PDC=`53.94`
  * Monday Range Blueprint: High=`54.39` | Mid=`53.69` | Low=`52.99`
  * Developing Weekly Value Area: Weekly VAH=`54.48` | Weekly POC=`53.88` | Weekly VAL=`53.24`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`54.37` | Low=`52.98`
  * London Session (08:00-16:00 UTC): High=`53.50` | Low=`52.30`
  * New York Session (13:00-21:00 UTC): High=`53.07` | Low=`51.98`
  * Initial Balance (First Hour): IB High=`53.50` | IB Low=`52.73`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `51.93` - `52.35`
  * Optimal Trade Entry (OTE 0.705): `52.24`
  * Structural Invalidation Anchor (0.786): `52.56`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `52.44` | `52.48` | `52.38` | `52.42` | `1,967` | 103,110.14 USD | -15,573.93 USD | `-15.10%` | -533,645.67 USD | `-0.24` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `52.42` | `52.49` | `52.40` | `52.46` | `1,614` | 84,665.60 USD | 27,780.90 USD | `+32.81%` | -505,864.77 USD | `+0.29` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `52.46` | `52.51` | `52.38` | `52.39` | `1,475` | 77,276.72 USD | -54,637.06 USD | `-70.70%` | -560,501.83 USD | `-0.69` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `52.70` | `52.76` | `52.45` | `52.61` | `7,582` | 398,896.60 USD | -52,795.14 USD | `-13.24%` | -1,096,767.93 USD | `-0.18` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `52.61` | `52.62` | `52.38` | `52.46` | `5,790` | 303,726.03 USD | -150,581.47 USD | `-49.58%` | -1,247,349.40 USD | `-0.60` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `52.46` | `52.51` | `52.38` | `52.45` | `4,685` | 245,728.25 USD | -3,839.50 USD | `-1.56%` | -1,251,188.90 USD | `+0.11` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `52.37` | `52.61` | `51.98` | `52.24` | `41,435` | 2,164,605.83 USD | -391,069.83 USD | `-18.07%` | -1,511,737.72 USD | `-0.66` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `52.24` | `52.76` | `52.03` | `52.61` | `32,755` | 1,723,273.30 USD | 951,587.73 USD | `+55.22%` | -560,149.99 USD | `+1.89` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `52.61` | `52.65` | `52.32` | `52.51` | `20,260` | 1,063,771.56 USD | -103,422.23 USD | `-9.72%` | -663,572.22 USD | `-0.19` | **`BEARISH`** | `DELTA ALIGNED` |
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
| `BID` | `52.12` | `360.6900` | 18,800.97 USD | 889,503.78 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `52.12` | `3.9000` | 203.28 USD | 889,707.06 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `52.12` | `130.5300` | 6,803.62 USD | 896,510.68 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `52.12` | `1801.8300` | 93,914.98 USD | 990,425.66 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `52.12` | `6467.2600` | 337,073.59 USD | 1,327,499.25 USD | `7 orders` | `-0.04%` | `-` |
| `BID` | `52.13` | `88.1300` | 4,594.66 USD | 166,354.01 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `52.13` | `1136.7400` | 59,262.80 USD | 225,616.81 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `52.13` | `212.4000` | 11,073.05 USD | 236,689.86 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `52.13` | `46.4800` | 2,423.10 USD | 239,112.95 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `52.13` | `198.3600` | 10,340.51 USD | 249,453.46 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `52.13` | `6420.9100` | 334,715.62 USD | 584,169.08 USD | `5 orders` | `-0.02%` | `-` |
| `BID` | `52.13` | `4943.5400` | 257,696.85 USD | 841,865.93 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `52.13` | `255.7200` | 13,329.92 USD | 855,195.85 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `52.13` | `297.4900` | 15,506.96 USD | 870,702.81 USD | `3 orders` | `-0.03%` | `-` |
| `ASK` | `52.14` | `68.7000` | 3,582.29 USD | 16,444.34 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `52.14` | `175.3500` | 9,143.28 USD | 12,862.04 USD | `2 orders` | `+0.00%` | `-` |
| `ASK` | `52.14` | `71.3200` | 3,718.77 USD | 3,718.77 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `52.14` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 52.14` | `0.00%` | `-` |
| `BID` | `52.14` | `67.3900` | 3,513.78 USD | 3,513.78 USD | `2 orders` | `-0.00%` | `-` |
| `BID` | `52.14` | `193.1000` | 10,068.23 USD | 13,582.02 USD | `2 orders` | `-0.00%` | `-` |
| `BID` | `52.14` | `70.1300` | 3,656.51 USD | 17,238.52 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `52.14` | `171.1600` | 8,923.94 USD | 26,162.46 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `52.14` | `1054.8600` | 54,997.24 USD | 81,159.70 USD | `6 orders` | `-0.01%` | `-` |
| `BID` | `52.14` | `1545.9500` | 80,599.65 USD | 161,759.35 USD | `2 orders` | `-0.01%` | `-` |
| `ASK` | `52.15` | `107.3700` | 5,599.77 USD | 264,607.57 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `52.15` | `2798.6400` | 145,957.47 USD | 259,007.80 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `52.15` | `65.3300` | 3,407.09 USD | 113,050.32 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `52.15` | `709.1900` | 36,984.97 USD | 109,643.23 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `52.15` | `709.3600` | 36,993.12 USD | 72,658.27 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `52.15` | `77.1800` | 4,024.86 USD | 35,665.14 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `52.15` | `54.8800` | 2,861.88 USD | 31,640.28 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `52.15` | `38.4900` | 2,007.14 USD | 28,778.40 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `52.15` | `130.5300` | 6,806.62 USD | 26,771.26 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `52.15` | `67.5100` | 3,520.31 USD | 19,964.64 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `52.16` | `1638.3700` | 85,459.02 USD | 1,413,839.28 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `52.16` | `9063.7300` | 472,764.16 USD | 1,328,380.26 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `52.16` | `474.0700` | 24,727.02 USD | 855,616.11 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `52.16` | `10555.4900` | 550,553.25 USD | 830,889.09 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `52.16` | `184.0400` | 9,598.97 USD | 280,335.84 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `52.16` | `41.0800` | 2,142.57 USD | 270,736.87 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `52.16` | `76.4400` | 3,986.73 USD | 268,594.30 USD | `2 orders` | `+0.03%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 23:45:33 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `115` | `0x5b5d...c060` | `SHORT` | 17,391,476.00 USD | `333,790.30` | `59.15` | `52.10` | `529.71` | 2,351,557.95 USD | `+13.52%` | `5X Cross` |
| `124` | `0x4692...164f` | `SHORT` | 16,298,735.56 USD | `312,853.63` | `53.40` | `52.10` | `239.81` | 406,639.17 USD | `+2.49%` | `5X Cross` |
| `178` | `0x49e9...e1d0` | `SHORT` | 11,735,172.88 USD | `225,264.86` | `55.61` | `52.10` | `88.40` | 790,831.01 USD | `+6.74%` | `4X Cross` |
| `211` | `0xacb6...efbd` | `SHORT` | 10,477,035.16 USD | `201,133.33` | `59.63` | `52.10` | `76.58` | 1,515,621.96 USD | `+14.47%` | `6X Cross` |
| `246` | `0xc26c...b8f4` | `LONG` | 9,454,788.05 USD | `181,463.41` | `55.43` | `52.10` | `0.000000` | -603,967.03 USD | `-6.39%` | `2X Cross` |
| `368` | `0xd8c5...99b0` | `SHORT` | 6,580,895.12 USD | `126,320.04` | `61.98` | `52.10` | `195.04` | 1,248,442.72 USD | `+18.97%` | `3X Cross` |
| `369` | `0x645b...87b8` | `LONG` | 6,578,579.93 USD | `126,275.60` | `56.64` | `52.10` | `0.000000` | -573,113.78 USD | `-8.71%` | `3X Cross` |
| `402` | `0xe9ff...5903` | `SHORT` | 5,887,999.74 USD | `112,996.08` | `60.07` | `52.10` | `196.90` | 899,951.07 USD | `+15.28%` | `5X Cross` |
| `429` | `0xfc66...ca06` | `SHORT` | 5,512,949.34 USD | `105,820.86` | `54.61` | `52.10` | `448.25` | 265,517.92 USD | `+4.82%` | `3X Cross` |
| `539` | `0x354b...6425` | `LONG` | 4,254,802.15 USD | `81,678.61` | `52.45` | `52.10` | `0.000000` | -29,083.27 USD | `-0.68%` | `10X Cross` |
| `583` | `0x4e23...20c3` | `SHORT` | 3,973,436.64 USD | `76,258.26` | `52.44` | `52.10` | `219.61` | 25,775.29 USD | `+0.65%` | `16X Cross` |
| `627` | `0x9aa5...58af` | `LONG` | 3,712,138.92 USD | `71,243.43` | `61.59` | `52.10` | `0.000000` | -676,018.60 USD | `-18.21%` | `20X Cross` |
| `746` | `0x2056...8396` | `LONG` | 3,126,300.00 USD | `60,000.00` | `66.92` | `52.10` | `21.34` | -889,027.14 USD | `-28.44%` | `10X Cross` |
| `877` | `0x0242...ffa1` | `SHORT` | 2,600,259.17 USD | `49,916.67` | `56.48` | `52.10` | `279.60` | 218,872.69 USD | `+8.42%` | `10X Cross` |
| `886` | `0x960b...f0fc` | `LONG` | 2,577,007.01 USD | `49,457.96` | `55.82` | `52.10` | `0.000000` | -183,930.02 USD | `-7.14%` | `25X Cross` |
| `982` | `0x8b9d...7b28` | `LONG` | 2,335,213.14 USD | `44,823.47` | `58.35` | `52.10` | `0.000000` | -280,235.40 USD | `-12.00%` | `10X Cross` |
| `1068` | `0x5647...e7de` | `LONG` | 2,097,251.23 USD | `40,262.07` | `57.38` | `52.10` | `0.000000` | -212,986.37 USD | `-10.16%` | `20X Cross` |
| `1076` | `0xa2ce...3126` | `LONG` | 2,083,920.00 USD | `40,000.00` | `74.30` | `52.10` | `0.000000` | -888,135.49 USD | `-42.62%` | `20X Cross` |
| `1453` | `0x3678...b209` | `LONG` | 1,562,910.00 USD | `30,000.00` | `57.15` | `52.10` | `0.000000` | -151,590.00 USD | `-9.70%` | `20X Cross` |
| `1454` | `0x5a88...d997` | `LONG` | 1,562,850.00 USD | `30,000.00` | `59.50` | `52.10` | `37.36` | -222,037.59 USD | `-14.21%` | `25X Cross` |
| `1679` | `0x7ea9...fc7f` | `LONG` | 1,302,450.00 USD | `25,000.00` | `53.60` | `52.10` | `18.30` | -37,554.05 USD | `-2.88%` | `25X Cross` |
| `1713` | `0xce97...7e78` | `LONG` | 1,278,416.34 USD | `24,541.51` | `52.30` | `52.10` | `0.000000` | -5,068.44 USD | `-0.40%` | `5X Cross` |
| `1797` | `0xf517...c032` | `LONG` | 1,179,005.89 USD | `22,627.50` | `66.29` | `52.10` | `0.000000` | -320,989.22 USD | `-27.23%` | `20X Cross` |
| `1915` | `0xcc9f...d218` | `LONG` | 1,068,918.05 USD | `20,520.60` | `52.63` | `52.10` | `26.86` | -10,990.00 USD | `-1.03%` | `2X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `81.27` | 429.11 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 0.43K USD at 81.2710 USD [API] | `2026-02-01 23:01:26` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`53.86` (Vol: 3,800,000.00 USD, Dist: `+3.10%`) | Long MP=`51.93` (Vol: 3,400,000.00 USD, Dist: `--0.59%`)
  * 48H Horizon: Short MP=`54.97` (Vol: 4,800,000.00 USD, Dist: `+5.22%`) | Long MP=`51.70` (Vol: 3,300,000.00 USD, Dist: `--1.03%`)
  * 3D Horizon: Short MP=`55.10` (Vol: 5,400,000.00 USD, Dist: `+5.48%`) | Long MP=`51.93` (Vol: 5,700,000.00 USD, Dist: `--0.59%`)
  * 7D Horizon: Short MP=`55.10` (Vol: 8,800,000.00 USD, Dist: `+5.47%`) | Long MP=`51.93` (Vol: 6,900,000.00 USD, Dist: `--0.60%`)
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
  * Current Rate: `57.94K` | Last 24h: `163.44K` | Last 3d: `421.23K` | Last 7d: `760.43K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `-` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `0.0096%` | **USDT BingX** | `-` |
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
  * `2026-10-29 23:30:59 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:25:59 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:03:59 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:59 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 22:54:59 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:44:59 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:40:59 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:39:59 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 23:39:59 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 23:39:59 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 23:39:59 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:41:59 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:41:59 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 19:41:59 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:41:59 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `51.63` (Risk Distance: `0.3627` pts)
  * +2.5R Take Profit: `52.90`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.02 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `52.98` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `53.35` (Risk Distance: `0.3627` pts)
  * +2.5R Take Profit: `52.08`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.02 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`52.56`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
