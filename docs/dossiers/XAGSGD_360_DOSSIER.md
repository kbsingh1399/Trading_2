# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAGSGD
**Canonical Key**: `XAGSGD` | **Broker Instrument**: `XAGSGD.pi` | **Asset Class**: `Forex Exotic`
**Timestamp**: `2026-10-30 02:39:45 IST` (`2026-10-29 21:09:45 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `66.73` | **Live Ask Quote**: `66.81` | **Mid Price**: `66.77`
- **Spread Points**: `72.00` | **Spread BPS**: `10.78 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `52.73` | VWAP Z-Score: `-1.01` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.1854` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `46.36` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `54.35` | Lower -3.00σ Band: `51.11`
  * Upper +2.51σ Band: `54.09` | Lower -2.51σ Band: `51.38`
  * Upper +2.01σ Band: `53.82` | Lower -2.01σ Band: `51.65`
  * Upper +2.00σ Band: `53.81` | Lower -2.00σ Band: `51.65`
  * Upper +1.28σ Band: `53.42` | Lower -1.28σ Band: `52.04`
  * Upper +1.00σ Band: `53.27` | Lower -1.00σ Band: `52.19`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`52.20` | EMA-20=`52.23` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`52.45` (Slope: `+0.0000`) | EMA-100=`52.80`
  * Institutional Anchors: EMA-144=`53.00` | EMA-200=`53.18` (Slope: `-0.2508`) | EMA-233=`53.26`
- **Range Boundaries**: 24H High=`54.61` | 24H Low=`51.95` | Weekly High=`54.61` | Weekly Low=`51.95`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `52.92` (Distance: `-1.43%`)
  * Point of Control (POC) = `52.45` (Distance: `-0.55%`)
  * Value Area Low (VAL) = `51.99` (Distance: `+0.35%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`54.10` | POC=`53.83` | VAL=`53.54`
  * Prior Day Extremes: PDH=`54.61` | PDL=`53.28` | PDC=`53.94`
  * Monday Range Blueprint: High=`54.39` | Mid=`53.69` | Low=`52.99`
  * Developing Weekly Value Area: Weekly VAH=`54.49` | Weekly POC=`53.89` | Weekly VAL=`53.18`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`54.37` | Low=`52.98`
  * London Session (08:00-16:00 UTC): High=`53.50` | Low=`52.30`
  * New York Session (13:00-21:00 UTC): High=`53.07` | Low=`51.98`
  * Initial Balance (First Hour): IB High=`53.50` | IB Low=`52.73`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `66.50` - `67.04`
  * Optimal Trade Entry (OTE 0.705): `66.90`
  * Structural Invalidation Anchor (0.786): `67.30`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `52.02` | `52.05` | `51.99` | `52.01` | `1,031` | 53,617.16 USD | -20,216.30 USD | `-37.70%` | -617,366.28 USD | `-0.24` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `52.01` | `52.06` | `51.99` | `52.05` | `1,109` | 57,722.34 USD | 37,804.07 USD | `+65.49%` | -579,562.21 USD | `+1.53` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `52.05` | `52.10` | `52.03` | `52.10` | `876` | 45,636.10 USD | 34,709.14 USD | `+76.06%` | -544,853.07 USD | `+1.31` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `52.23` | `52.26` | `51.98` | `52.07` | `4,678` | 243,574.10 USD | -116,968.14 USD | `-48.02%` | -1,396,211.64 USD | `-0.46` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `52.07` | `52.12` | `51.97` | `52.01` | `3,883` | 201,935.42 USD | -89,675.27 USD | `-44.41%` | -1,485,886.91 USD | `-0.33` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `52.01` | `52.12` | `51.99` | `52.11` | `2,857` | 148,866.84 USD | 118,862.67 USD | `+79.84%` | -1,367,024.24 USD | `+0.78` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `52.51` | `52.51` | `52.26` | `52.42` | `15,925` | 834,740.72 USD | -28,381.18 USD | `-3.40%` | -226,622.82 USD | `+0.15` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `52.42` | `52.51` | `51.97` | `52.01` | `15,397` | 800,720.98 USD | -646,338.43 USD | `-80.72%` | -872,961.26 USD | `-1.42` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `52.01` | `52.12` | `51.95` | `52.08` | `9,961` | 518,719.08 USD | 235,233.07 USD | `+45.35%` | -637,728.19 USD | `+0.82` | **`BULLISH`** | `AGGRESSIVE BUYING` |
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
| `BID` | `52.12` | `286.2000` | 14,918.17 USD | 139,524.81 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `52.12` | `588.2700` | 30,662.40 USD | 170,187.20 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `52.12` | `84.2600` | 4,391.80 USD | 174,579.00 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `52.13` | `206.2400` | 10,752.32 USD | 88,574.06 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `52.13` | `256.7000` | 13,382.80 USD | 101,956.86 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `52.13` | `155.0500` | 8,083.22 USD | 110,040.08 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `52.13` | `44.4000` | 2,314.66 USD | 112,354.74 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `52.13` | `10.0000` | 521.31 USD | 112,876.05 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `52.13` | `25.2100` | 1,314.20 USD | 114,190.25 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `52.13` | `165.0000` | 8,601.28 USD | 122,791.53 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `52.13` | `34.8200` | 1,815.10 USD | 124,606.63 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `52.14` | `129.8800` | 6,772.46 USD | 41,364.95 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `52.14` | `129.8800` | 6,772.33 USD | 48,137.29 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `52.14` | `129.8800` | 6,772.07 USD | 54,909.36 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `52.14` | `154.9100` | 8,077.01 USD | 62,986.37 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `52.14` | `198.0900` | 10,328.21 USD | 73,314.58 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `52.14` | `86.4500` | 4,507.16 USD | 77,821.74 USD | `1 orders` | `-0.03%` | `-` |
| `ASK` | `52.15` | `160.2400` | 8,357.16 USD | 37,005.69 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `52.15` | `47.8300` | 2,494.48 USD | 28,648.53 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `52.15` | `309.7600` | 16,154.29 USD | 26,154.06 USD | `2 orders` | `+0.00%` | `-` |
| `ASK` | `52.15` | `191.7500` | 9,999.76 USD | 9,999.76 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `52.15` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 52.15` | `0.00%` | `-` |
| `BID` | `52.15` | `477.7100` | 24,912.10 USD | 24,912.10 USD | `5 orders` | `-0.00%` | `-` |
| `BID` | `52.15` | `9.9400` | 518.34 USD | 25,430.44 USD | `3 orders` | `-0.00%` | `-` |
| `BID` | `52.15` | `175.7000` | 9,162.05 USD | 34,592.49 USD | `2 orders` | `-0.01%` | `-` |
| `ASK` | `52.16` | `130.1900` | 6,791.36 USD | 87,047.55 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `52.16` | `3.9000` | 203.44 USD | 80,256.19 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `52.16` | `33.7100` | 1,758.41 USD | 80,052.75 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `52.16` | `174.5300` | 9,103.83 USD | 78,294.34 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `52.16` | `40.9200` | 2,134.43 USD | 69,190.51 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `52.16` | `97.5200` | 5,086.64 USD | 67,056.08 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `52.16` | `0.2000` | 10.43 USD | 61,969.43 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `52.16` | `198.8700` | 10,372.66 USD | 61,959.00 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `52.16` | `78.3100` | 4,084.41 USD | 51,586.34 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `52.16` | `40.8100` | 2,128.49 USD | 47,501.93 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `52.16` | `160.4400` | 8,367.75 USD | 45,373.44 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `52.17` | `164.0600` | 8,559.01 USD | 137,914.50 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `52.17` | `5.1400` | 268.15 USD | 129,355.49 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `52.17` | `160.2500` | 8,359.92 USD | 129,087.35 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `52.17` | `456.3800` | 23,807.98 USD | 120,727.42 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `52.17` | `189.2400` | 9,871.89 USD | 96,919.45 USD | `2 orders` | `+0.03%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:35:51 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `113` | `0x5b5d...c060` | `SHORT` | 17,407,164.14 USD | `333,790.30` | `59.15` | `52.15` | `605.71` | 2,335,869.81 USD | `+13.42%` | `5X Cross` |
| `122` | `0x4692...164f` | `SHORT` | 16,194,062.32 USD | `310,528.52` | `53.32` | `52.15` | `249.53` | 363,040.04 USD | `+2.24%` | `5X Cross` |
| `174` | `0x49e9...e1d0` | `SHORT` | 11,287,581.72 USD | `216,444.52` | `55.61` | `52.15` | `93.05` | 747,961.24 USD | `+6.63%` | `4X Cross` |
| `201` | `0xacb6...efbd` | `SHORT` | 10,488,700.89 USD | `201,133.33` | `59.63` | `52.15` | `76.58` | 1,503,956.22 USD | `+14.34%` | `6X Cross` |
| `238` | `0xc26c...b8f4` | `LONG` | 9,460,231.95 USD | `181,463.41` | `55.43` | `52.15` | `0.000000` | -598,523.13 USD | `-6.33%` | `2X Cross` |
| `351` | `0x645b...87b8` | `LONG` | 6,587,064.41 USD | `126,309.96` | `56.63` | `52.15` | `0.000000` | -566,416.47 USD | `-8.60%` | `3X Cross` |
| `352` | `0xd8c5...99b0` | `SHORT` | 6,585,442.65 USD | `126,320.04` | `61.98` | `52.15` | `198.48` | 1,243,895.20 USD | `+18.89%` | `3X Cross` |
| `394` | `0xe9ff...5903` | `SHORT` | 5,892,745.57 USD | `112,996.08` | `60.07` | `52.15` | `199.25` | 895,205.23 USD | `+15.19%` | `5X Cross` |
| `419` | `0xfc66...ca06` | `SHORT` | 5,407,119.56 USD | `103,683.98` | `54.61` | `52.15` | `445.62` | 254,660.97 USD | `+4.71%` | `3X Cross` |
| `614` | `0x9aa5...58af` | `LONG` | 3,715,202.39 USD | `71,243.43` | `61.59` | `52.15` | `0.000000` | -672,955.14 USD | `-18.11%` | `20X Cross` |
| `726` | `0x2056...8396` | `LONG` | 3,128,040.00 USD | `60,000.00` | `66.92` | `52.15` | `21.34` | -887,287.14 USD | `-28.37%` | `10X Cross` |
| `761` | `0x354b...6425` | `LONG` | 3,007,480.07 USD | `57,669.80` | `52.37` | `52.15` | `0.000000` | -12,921.48 USD | `-0.43%` | `10X Cross` |
| `864` | `0x0242...ffa1` | `SHORT` | 2,602,305.76 USD | `49,916.67` | `56.48` | `52.15` | `331.77` | 216,826.11 USD | `+8.33%` | `10X Cross` |
| `871` | `0x960b...f0fc` | `LONG` | 2,578,391.83 USD | `49,457.96` | `55.82` | `52.15` | `0.000000` | -182,545.20 USD | `-7.08%` | `25X Cross` |
| `954` | `0x8b9d...7b28` | `LONG` | 2,337,543.96 USD | `44,823.47` | `58.35` | `52.15` | `0.000000` | -277,904.58 USD | `-11.89%` | `10X Cross` |
| `1044` | `0x5647...e7de` | `LONG` | 2,099,465.64 USD | `40,262.07` | `57.38` | `52.15` | `0.000000` | -210,771.96 USD | `-10.04%` | `20X Cross` |
| `1050` | `0xa2ce...3126` | `LONG` | 2,086,000.00 USD | `40,000.00` | `74.30` | `52.15` | `0.000000` | -886,055.49 USD | `-42.48%` | `20X Cross` |
| `1075` | `0xb078...de15` | `SHORT` | 2,033,850.52 USD | `39,000.01` | `52.58` | `52.15` | `207.43` | 16,668.43 USD | `+0.82%` | `8X Cross` |
| `1415` | `0x5a88...d997` | `LONG` | 1,564,200.00 USD | `30,000.00` | `59.50` | `52.15` | `40.40` | -220,687.59 USD | `-14.11%` | `25X Cross` |
| `1416` | `0x3678...b209` | `LONG` | 1,564,170.00 USD | `30,000.00` | `57.15` | `52.15` | `0.000000` | -150,330.00 USD | `-9.61%` | `20X Cross` |
| `1623` | `0x7ea9...fc7f` | `LONG` | 1,303,750.00 USD | `25,000.00` | `53.60` | `52.15` | `18.20` | -36,254.05 USD | `-2.78%` | `25X Cross` |
| `1741` | `0xf517...c032` | `LONG` | 1,179,978.87 USD | `22,627.50` | `66.29` | `52.15` | `0.000000` | -320,016.23 USD | `-27.12%` | `20X Cross` |
| `1868` | `0xcc9f...d218` | `LONG` | 1,070,108.25 USD | `20,520.60` | `52.63` | `52.15` | `26.86` | -9,799.80 USD | `-0.92%` | `2X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`53.30` (Vol: 3,200,000.00 USD, Dist: `+1.87%`) | Long MP=`51.68` (Vol: 2,700,000.00 USD, Dist: `--1.22%`)
  * 48H Horizon: Short MP=`55.08` (Vol: 4,200,000.00 USD, Dist: `+5.28%`) | Long MP=`51.68` (Vol: 3,100,000.00 USD, Dist: `--1.22%`)
  * 3D Horizon: Short MP=`55.08` (Vol: 4,700,000.00 USD, Dist: `+5.28%`) | Long MP=`51.96` (Vol: 4,000,000.00 USD, Dist: `--0.70%`)
  * 7D Horizon: Short MP=`54.83` (Vol: 7,300,000.00 USD, Dist: `+4.79%`) | Long MP=`51.96` (Vol: 4,900,000.00 USD, Dist: `--0.69%`)
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
  * Current Rate: `24.07K` | Last 24h: `193.96K` | Last 3d: `450.64K` | Last 7d: `729.34K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `-` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `0.0013%` | **USDT BingX** | `-` |
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
  * `2026-10-30 02:15:26 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:35:26 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:31:26 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:31:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:30:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:32:26 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:32:26 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:32:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:32:26 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `51.66` (Risk Distance: `0.3305` pts)
  * +2.5R Take Profit: `52.81`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.02 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `52.92` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `53.25` (Risk Distance: `0.3305` pts)
  * +2.5R Take Profit: `52.10`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.02 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`67.30`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
