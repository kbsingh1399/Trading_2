# 🏛️ SOVEREIGN CANDIDATE DOSSIER: SUI
**Canonical Key**: `SUI` | **Broker Instrument**: `SUIUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 03:04:03 IST` (`2026-10-29 21:34:03 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.9100` | **Live Ask Quote**: `0.9102` | **Mid Price**: `0.9101`
- **Spread Points**: `0.000182` | **Spread BPS**: `2.00 bps` (Charter Threshold: `12.00 bps`)
- **Gate 1 Clearance**: **`PASS`** | **Execution Posture**: `PASSIVE_MAKER_LIMIT_ONLY` | **Order Type Allowed**: `LIMIT_ONLY`
- **True Broker Contract Specifications**:
  * Contract Size: `1.0` | Digits: `4` | Point: `0.0001`
  * Point Value (1.0 Lot): `0.00 USD` | Point Value (0.01 Lot): `0.0000 USD`
  * Allowed Lot Sizing: Min Lot=`0.01` | Step Lot=`0.01` | Max Lot=`20.00`
- **Solvency Defense Ladder**:
  * Hard Floor Stop: `4,775.00 USD` (Zero Open Risk) | Operating Defense Buffer: `4,795.00 USD` (Capital Preservation Mode)
  * Kernel Admission Floor: `4,795.00 USD` (`min(balance, equity) - StressedLoss - 2.00 >= 4,795.00 USD`)
- **Pipeline Health (23_Master_Pipeline_Telemetry.parquet)**: Status=`HEALTHY` | Latency=`4.2 ms` | RAM Usage=`385.0 MB`

---

## 2. Technical Profile, VWAP Dispersion Grid & BTC Ribbon
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Session Anchor & Volatility**:
  * Session VWAP: `0.9101` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.9165` | Lower -3.00σ Band: `0.9037`
  * Upper +2.51σ Band: `0.9151` | Lower -2.51σ Band: `0.9051`
  * Upper +2.01σ Band: `0.9139` | Lower -2.01σ Band: `0.9063`
  * Upper +2.00σ Band: `0.9137` | Lower -2.00σ Band: `0.9065`
  * Upper +1.28σ Band: `0.9126` | Lower -1.28σ Band: `0.9075`
  * Upper +1.00σ Band: `0.9119` | Lower -1.00σ Band: `0.9083`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.9101` | EMA-20=`0.9101` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.9101` (Slope: `+0.0000`) | EMA-100=`0.9101`
  * Institutional Anchors: EMA-144=`0.9101` | EMA-200=`0.9101` (Slope: `+0.0000`) | EMA-233=`0.9101`
- **Range Boundaries**: 24H High=`0.9192` | 24H Low=`0.9010` | Weekly High=`0.9283` | Weekly Low=`0.8919`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.9128` (Distance: `+0.00%`)
  * Point of Control (POC) = `0.9101` (Distance: `+0.00%`)
  * Value Area Low (VAL) = `0.9074` (Distance: `+0.00%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`NEUTRAL`** | Market Regime: `BALANCED_AUCTION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.9137` | POC=`0.9101` | VAL=`0.9065`
  * Prior Day Extremes: PDH=`0.9156` | PDL=`0.9046` | PDC=`0.9101`
  * Monday Range Blueprint: High=`0.9146` | Mid=`0.9101` | Low=`0.9055`
  * Developing Weekly Value Area: Weekly VAH=`0.9174` | Weekly POC=`0.9101` | Weekly VAL=`0.9028`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.9119` | Low=`0.9083`
  * London Session (08:00-16:00 UTC): High=`0.9137` | Low=`0.9065`
  * New York Session (13:00-21:00 UTC): High=`0.9156` | Low=`0.9046`
  * Initial Balance (First Hour): IB High=`0.9128` | IB Low=`0.9074`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.9065` - `0.9137`
  * Optimal Trade Entry (OTE 0.705): `0.9119`
  * Structural Invalidation Anchor (0.786): `0.9174`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.8733` | `0.8843` | `0.8714` | `0.8843` | `4,479,079` | 3,936,932.03 USD | 168,584.34 USD | `+4.28%` | -16,403,475.50 USD | `+0.43` | **`BULLISH`** | `NEUTRAL CHOP` |
| `5m` | `0.8842` | `0.8854` | `0.8811` | `0.8852` | `4,045,456` | 3,574,067.82 USD | -108,935.22 USD | `-3.05%` | -16,512,410.72 USD | `+0.18` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.8853` | `0.8864` | `0.8850` | `0.8851` | `294,417` | 260,735.00 USD | -66,569.04 USD | `-25.53%` | -16,578,979.77 USD | `+0.23` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.8779` | `0.8897` | `0.8574` | `0.8737` | `29,477,241` | 25,765,113.89 USD | -841,441.70 USD | `-3.27%` | -15,913,850.80 USD | `-0.35` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `0.8736` | `0.8854` | `0.8692` | `0.8852` | `14,286,164` | 12,554,511.67 USD | 69,899.48 USD | `+0.56%` | -15,843,951.33 USD | `+0.46` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `0.8853` | `0.8860` | `0.8850` | `0.8860` | `119,501` | 105,787.43 USD | -13,490.54 USD | `-12.75%` | -15,857,441.87 USD | `+0.34` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.9311` | `0.9338` | `0.9274` | `0.9295` | `5,959,668` | 5,545,537.10 USD | -24,776.87 USD | `-0.45%` | -9,951,062.67 USD | `+0.35` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.9294` | `0.9303` | `0.8574` | `0.8737` | `71,708,417` | 63,836,842.40 USD | -6,009,876.59 USD | `-9.41%` | -15,960,939.26 USD | `-3.07` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.8736` | `0.8864` | `0.8692` | `0.8850` | `14,633,853` | 12,862,396.01 USD | -11,572.22 USD | `-0.09%` | -15,972,511.48 USD | `+0.33` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9221` | `0.9548` | `0.9166` | `0.9539` | `53,988,780` | 50,583,791.87 USD | 2,028,716.92 USD | `+4.01%` | -6,589,251.83 USD | `+0.90` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9539` | `0.9617` | `0.9250` | `0.9295` | `47,160,892` | 44,338,664.22 USD | -2,573,311.69 USD | `-5.80%` | -9,162,563.53 USD | `-0.20` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9294` | `0.9303` | `0.8574` | `0.8850` | `86,342,270` | 76,699,238.41 USD | -6,021,448.81 USD | `-7.85%` | -15,184,012.34 USD | `-0.94` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9043` | `0.9222` | `0.9010` | `0.9063` | `37,205,563` | 33,852,646.16 USD | 118,750.50 USD | `+0.35%` | -8,478,733.68 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9064` | `0.9286` | `0.9052` | `0.9221` | `31,513,227` | 28,896,267.25 USD | -139,235.07 USD | `-0.48%` | -8,617,968.75 USD | `+0.68` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9221` | `0.9548` | `0.9166` | `0.9539` | `53,988,780` | 50,583,791.87 USD | 2,028,716.92 USD | `+4.01%` | -6,589,251.83 USD | `+0.90` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9539` | `0.9617` | `0.9250` | `0.9295` | `47,160,892` | 44,338,664.22 USD | -2,573,311.69 USD | `-5.80%` | -9,162,563.53 USD | `-0.20` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9294` | `0.9303` | `0.8574` | `0.8850` | `86,342,270` | 76,699,238.41 USD | -6,021,448.81 USD | `-7.85%` | -15,184,012.34 USD | `-0.94` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`0.9101`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `0.8933` | `2354.8000` | 2,103.66 USD | 53,088.10 USD | `1 orders` | `-0.10%` | `-` |
| `BID` | `0.8933` | `18216.8000` | 16,272.89 USD | 69,360.98 USD | `1 orders` | `-0.11%` | `-` |
| `BID` | `0.8933` | `2379.5000` | 2,125.54 USD | 71,486.52 USD | `1 orders` | `-0.11%` | `-` |
| `BID` | `0.8933` | `2488.3000` | 2,222.70 USD | 73,709.22 USD | `1 orders` | `-0.11%` | `-` |
| `BID` | `0.8934` | `5850.7000` | 5,227.13 USD | 46,756.09 USD | `3 orders` | `-0.09%` | `-` |
| `BID` | `0.8934` | `2379.5000` | 2,125.87 USD | 48,881.96 USD | `1 orders` | `-0.09%` | `-` |
| `BID` | `0.8934` | `2353.4000` | 2,102.48 USD | 50,984.44 USD | `1 orders` | `-0.10%` | `-` |
| `BID` | `0.8935` | `2380.1000` | 2,126.67 USD | 34,419.39 USD | `1 orders` | `-0.08%` | `-` |
| `BID` | `0.8935` | `7956.9000` | 7,109.57 USD | 41,528.95 USD | `2 orders` | `-0.08%` | `-` |
| `BID` | `0.8936` | `1040.5000` | 929.82 USD | 22,989.00 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `0.8936` | `2380.2000` | 2,126.95 USD | 25,115.95 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `0.8936` | `2379.5000` | 2,126.30 USD | 27,242.25 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `0.8936` | `1175.9000` | 1,050.76 USD | 28,293.01 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `0.8936` | `4476.1000` | 3,999.71 USD | 32,292.72 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `0.8937` | `11206.8000` | 10,015.74 USD | 22,059.18 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `0.8938` | `2000.0000` | 1,787.60 USD | 12,043.44 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.8940` | `400.0000` | 357.60 USD | 1,359.11 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.8940` | `4350.1000` | 3,888.86 USD | 5,247.97 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.8940` | `5601.9000` | 5,007.87 USD | 10,255.84 USD | `1 orders` | `-0.03%` | `-` |
| `MID_SPREAD` | `0.8942` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 0.89` | `0.00%` | `-` |
| `BID` | `0.8942` | `1120.0000` | 1,001.50 USD | 1,001.50 USD | `1 orders` | `-0.00%` | `-` |
| `ASK` | `0.8943` | `1337.0000` | 1,195.72 USD | 14,945.97 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `0.8943` | `2674.0000` | 2,391.41 USD | 13,750.25 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `0.8943` | `2674.0000` | 2,391.38 USD | 11,358.84 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `0.8943` | `2674.0000` | 2,391.36 USD | 8,967.45 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `0.8943` | `2674.0000` | 2,391.33 USD | 6,576.09 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `0.8943` | `2674.0000` | 2,391.30 USD | 4,184.76 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `0.8943` | `2005.5000` | 1,793.46 USD | 1,793.46 USD | `3 orders` | `+0.00%` | `-` |
| `ASK` | `0.8944` | `1119.7000` | 1,001.52 USD | 59,122.35 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.8944` | `29482.3000` | 26,370.15 USD | 58,120.84 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `0.8944` | `1041.5000` | 931.55 USD | 31,750.69 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `0.8944` | `2353.4000` | 2,104.90 USD | 30,819.14 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.8944` | `15394.2000` | 13,768.26 USD | 28,714.23 USD | `8 orders` | `+0.02%` | `-` |
| `ASK` | `0.8945` | `2353.4000` | 2,105.23 USD | 74,100.75 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.8945` | `3936.8000` | 3,521.59 USD | 71,995.52 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `0.8945` | `3394.6000` | 3,036.47 USD | 68,473.93 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.8945` | `2353.4000` | 2,105.07 USD | 65,437.46 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.8945` | `4706.8000` | 4,210.04 USD | 63,332.40 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.8946` | `2488.3000` | 2,226.16 USD | 95,734.10 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.8946` | `10304.7000` | 9,218.69 USD | 93,507.94 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `0.8946` | `11389.4000` | 10,188.50 USD | 84,289.26 USD | `1 orders` | `+0.04%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:55:39 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `670` | `0xb83d...6e36` | `SHORT` | 3,411,415.76 USD | `3,817,609.40` | `1.11` | `0.8895` | `37.42` | 807,319.56 USD | `+23.67%` | `3X Cross` |
| `1011` | `0xa2ce...3126` | `LONG` | 2,223,859.25 USD | `2,500,010.40` | `0.8597` | `0.8895` | `0.000000` | 74,652.72 USD | `+3.36%` | `10X Cross` |
| `1518` | `0x9946...0852` | `SHORT` | 1,461,121.96 USD | `1,632,538.50` | `1.08` | `0.8895` | `1.75` | 300,627.17 USD | `+20.58%` | `10X Cross` |
| `1837` | `0x9aa5...58af` | `SHORT` | 1,129,659.63 USD | `1,288,168.80` | `1.14` | `0.8895` | `7.84` | 338,033.26 USD | `+29.92%` | `10X Cross` |
| `1905` | `0x9df2...c665` | `SHORT` | 1,066,104.00 USD | `1,200,000.00` | `0.7465` | `0.8895` | `26.00` | -170,251.60 USD | `-15.97%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.9816` | 154.30 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.15K USD at 0.9816 USD [API] | `2026-09-21 08:38:19` |
| `ANNOUNCEMENT` | `INFO` | `0.9230` | 5,007.28 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 5.01K USD at 0.9230 USD [API] | `2026-10-28 13:20:03` |
| `ANNOUNCEMENT` | `INFO` | `0.9224` | 5,007.13 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 5.01K USD at 0.9224 USD [API] | `2026-10-28 13:30:10` |
| `ANNOUNCEMENT` | `INFO` | `0.9190` | 5,958.72 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 5.96K USD at 0.9190 USD [API] | `2026-10-28 13:52:39` |
| `ANNOUNCEMENT` | `INFO` | `0.9208` | 5,007.16 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 5.01K USD at 0.9208 USD [API] | `2026-10-28 14:42:33` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.9709` (Vol: 378,700.00 USD, Dist: `+5.85%`) | Long MP=`0.8890` (Vol: 711,300.00 USD, Dist: `--3.07%`)
  * 48H Horizon: Short MP=`0.9706` (Vol: 230,000.00 USD, Dist: `+5.82%`) | Long MP=`0.8887` (Vol: 546,500.00 USD, Dist: `--3.11%`)
  * 3D Horizon: Short MP=`0.9706` (Vol: 230,000.00 USD, Dist: `+5.82%`) | Long MP=`0.8887` (Vol: 859,700.00 USD, Dist: `--3.11%`)
  * 7D Horizon: Short MP=`0.9685` (Vol: 565,100.00 USD, Dist: `+5.59%`) | Long MP=`0.8890` (Vol: 1,100,000.00 USD, Dist: `--3.08%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.1945` | 1,410.00 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1955` | 2,410.00 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1995` | 256.00 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2045` | 204.50 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2135` | 4,040.00 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2195` | 852.58 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2265` | 220.32 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2355` | 1,030.00 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2385` | 156.36 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2505` | 2,540.00 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2525` | 3,940.00 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2645` | 2,610.00 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2685` | 106.16 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2725` | 1,910.00 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2735` | 248.34 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2755` | 178.91 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2785` | 3,630.00 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2795` | 24,070.00 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2885` | 29,070.00 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2945` | 687.92 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2965` | 593.12 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2975` | 4,330.00 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3035` | 124.25 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3115` | 373.46 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3155` | 195.04 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3245` | 202.81 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3415` | 203.91 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3445` | 103.35 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3455` | 338.66 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3465` | 3,470.00 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3505` | 1,020.00 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3585` | 28,450.00 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3665` | 274.88 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3685` | 2,940.00 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3705` | 413.14 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3725` | 4,260.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3785` | 861.39 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3795` | 278.02 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3825` | 6,500.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3845` | 1,750.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3875` | 27,120.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3895` | 2,980.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3905` | 191.54 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3925` | 5,030.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3945` | 754.48 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4035` | 935.03 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4045` | 5,520.00 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4055` | 735.13 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4235` | 467.50 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4295` | 300.65 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4345` | 765.59 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4385` | 122.91 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4415` | 49,780.00 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4435` | 10,840.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4455` | 574.83 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4465` | 19,600.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4525` | 5,660.00 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4535` | 702.74 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4595` | 295.78 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4755` | 500.27 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4785` | 110.10 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4835` | 174.01 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4865` | 201.07 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4885` | 6,570.00 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4895` | 646.73 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4915` | 3,370.00 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4935` | 1,500.00 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4945` | 3,820.00 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4955` | 211.88 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4965` | 259.97 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4985` | 216.75 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5015` | 212.49 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5025` | 1,330.00 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5055` | 211.25 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5085` | 2,540.00 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5095` | 195.75 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5155` | 1,240.00 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5165` | 15,330.00 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5175` | 213.68 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5185` | 121.74 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5205` | 864.13 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5245` | 5,280.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5255` | 31,530.00 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5275` | 348.36 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5285` | 2,590.00 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5295` | 123,640.00 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5325` | 2,680.00 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5345` | 417.12 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5365` | 131.55 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5375` | 7,850.00 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5395` | 319.98 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5405` | 7,090.00 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5425` | 269.13 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5445` | 230.32 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5455` | 5,930.00 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5465` | 272.87 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5475` | 1,240.00 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5495` | 28,790.00 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5505` | 248.06 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5515` | 160.93 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5525` | 582.56 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5535` | 271.88 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5545` | 531.60 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5555` | 7,950.00 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5585` | 141.97 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5595` | 304.93 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5605` | 441.84 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5625` | 18,470.00 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5635` | 195.93 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5655` | 8,190.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5665` | 570.01 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5675` | 1,560.00 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5695` | 973.22 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5725` | 139.23 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5735` | 182.72 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5745` | 144.03 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5755` | 1,010.00 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5765` | 1,150.00 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5775` | 497.75 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5785` | 119.34 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5795` | 212.85 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5805` | 1,410.00 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5825` | 6,470.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5835` | 1,750.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5855` | 2,640.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5865` | 466.85 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5875` | 969.32 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5885` | 311.14 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5925` | 994.16 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5935` | 132.41 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5945` | 8,600.00 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5965` | 5,540.00 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5995` | 151.97 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6005` | 6,840.00 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6025` | 432.35 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6055` | 238.51 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6075` | 851.05 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6085` | 272.24 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6105` | 2,750.00 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6115` | 6,780.00 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6125` | 768.01 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6135` | 245.40 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6145` | 3,430.00 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6155` | 935.13 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6165` | 29,900.00 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6175` | 2,600.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6185` | 4,400.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6195` | 1,050.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6215` | 8,420.00 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6245` | 619.32 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6255` | 32,070.00 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6285` | 102.45 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6305` | 319.35 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6315` | 13,570.00 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6335` | 16,340.00 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6345` | 450.05 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6365` | 3,060.00 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6375` | 130.62 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6395` | 244.03 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6405` | 939.17 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6415` | 86,920.00 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6425` | 1,260.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6435` | 657.79 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6445` | 65,790.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6455` | 14,370.00 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6465` | 146.76 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6475` | 8,240.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6485` | 668.34 USD | 3,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6495` | 325,470.00 USD | 3,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6505` | 631.12 USD | 3,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6515` | 403,320.00 USD | 3,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6535` | 126,530.00 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6545` | 1,150.00 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6555` | 1,170.00 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6565` | 8,270.00 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6575` | 13,280.00 USD | 2,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6585` | 2,970.00 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6595` | 329.75 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6615` | 126,890.00 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6625` | 788.97 USD | 2,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6645` | 448.54 USD | 2,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6675` | 5,280.00 USD | 2,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6685` | 2,810.00 USD | 2,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6705` | 2,290.00 USD | 2,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6715` | 8,500.00 USD | 2,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6725` | 1,450.00 USD | 2,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6735` | 27,680.00 USD | 2,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6745` | 6,520.00 USD | 2,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6755` | 111.59 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6765` | 1,040.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6785` | 250.77 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6795` | 5,620.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6805` | 1,600.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6815` | 3,380.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6825` | 15,920.00 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6835` | 11,170.00 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6845` | 5,790.00 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6875` | 2,380.00 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6885` | 83,790.00 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6895` | 2,110.00 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6905` | 3,360.00 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6915` | 8,970.00 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6935` | 2,980.00 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6945` | 722.28 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6965` | 704.37 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6975` | 2,400.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6985` | 1,930.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6995` | 879.97 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7015` | 383.72 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7045` | 759.59 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7055` | 115.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7065` | 769.59 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7075` | 787.73 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7085` | 3,890.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7095` | 2,720.00 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7105` | 3,530.00 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7115` | 4,090.00 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7125` | 156.39 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7175` | 8,820.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7195` | 11,720.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7205` | 120.54 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7225` | 652.13 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7255` | 2,660.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7265` | 1,060.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7275` | 762.57 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7285` | 214.03 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7295` | 375.98 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7305` | 119.88 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7315` | 31,890.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7325` | 907.93 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7345` | 2,340.00 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7355` | 51,920.00 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7365` | 6,900.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7375` | 203.11 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7385` | 5,940.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7405` | 3,530.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7415` | 382.61 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7425` | 784,090.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7445` | 105.64 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7455` | 1,990.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7475` | 103,310.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7485` | 105.91 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7495` | 599.60 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7515` | 1,210.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7525` | 106.03 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7535` | 2,020.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7545` | 16,010.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7575` | 1,900.00 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7585` | 36,710.00 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7595` | 4,500.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7615` | 351.43 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7630` | 17,170,000.00 USD | 17,170,000.00 USD | 37,590.00 USD | 14,770.00 USD | 1,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7635` | 5,110.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7645` | 3,510.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7650` | 17,120,000.00 USD | 17,120,000.00 USD | 556.58 USD | 23,090.00 USD | 10,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7655` | 320,960.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7660` | 4,110,000.00 USD | 4,110,000.00 USD | 0.00 USD | 101.33 USD | 4,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7665` | 1,260.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7670` | 17,080,000.00 USD | 17,080,000.00 USD | 1,280.00 USD | 177.87 USD | 18,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7675` | 10,510.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7685` | 499.99 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7690` | 17,060,000.00 USD | 17,060,000.00 USD | 182.28 USD | 161.63 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7695` | 144,250.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7705` | 13,980.00 USD | 892,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7710` | 17,060,000.00 USD | 17,060,000.00 USD | 7,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7715` | 338.38 USD | 878,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7725` | 2,360.00 USD | 878,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7735` | 4,570.00 USD | 875,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7765` | 4,630.00 USD | 871,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7785` | 7,000.00 USD | 866,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7790` | 17,050,000.00 USD | 17,050,000.00 USD | 0.00 USD | 5,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7795` | 338.69 USD | 859,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7800` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 7,100.00 USD | 22,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7810` | 17,050,000.00 USD | 17,050,000.00 USD | 0.00 USD | 185.50 USD | 5,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7815` | 4,160.00 USD | 859,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7830` | 17,040,000.00 USD | 17,040,000.00 USD | 0.00 USD | 0.00 USD | 5,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7835` | 1,060.00 USD | 855,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7850` | 17,040,000.00 USD | 17,040,000.00 USD | 0.00 USD | 0.00 USD | 13,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7855` | 3,020.00 USD | 853,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7865` | 2,870.00 USD | 850,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7870` | 17,030,000.00 USD | 17,030,000.00 USD | 0.00 USD | 14,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7875` | 15,190.00 USD | 848,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7880` | 4,070,000.00 USD | 4,070,000.00 USD | 26,800.00 USD | 572.15 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7895` | 44,370.00 USD | 832,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7900` | 4,050,000.00 USD | 4,050,000.00 USD | 0.00 USD | 5,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7905` | 3,670.00 USD | 788,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7910` | 17,010,000.00 USD | 17,010,000.00 USD | 0.00 USD | 18,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7915` | 1,290.00 USD | 784,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7920` | 4,040,000.00 USD | 4,040,000.00 USD | 0.00 USD | 731.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7925` | 385.87 USD | 783,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7930` | 16,990,000.00 USD | 16,990,000.00 USD | 0.00 USD | 0.00 USD | 41,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.7940` | 4,040,000.00 USD | 4,040,000.00 USD | 0.00 USD | 4,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7945` | 9,190.00 USD | 783,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7950` | 16,950,000.00 USD | 16,950,000.00 USD | 9,530.00 USD | 5,600.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7955` | 23,720.00 USD | 773,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7960` | 4,040,000.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 11,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7970` | 16,930,000.00 USD | 16,930,000.00 USD | 9,860.00 USD | 0.00 USD | 9,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7975` | 1,170.00 USD | 750,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7980` | 4,020,000.00 USD | 4,020,000.00 USD | 2,830.00 USD | 8,900.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7985` | 1,840.00 USD | 749,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7990` | 16,910,000.00 USD | 16,910,000.00 USD | 488.55 USD | 0.00 USD | 8,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7995` | 2,580.00 USD | 747,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8000` | 4,010,000.00 USD | 4,010,000.00 USD | 0.00 USD | 11,260.00 USD | 16,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8005` | 635.04 USD | 744,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8010` | 16,900,000.00 USD | 16,900,000.00 USD | 1,890.00 USD | 14,760.00 USD | 35,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8015` | 6,810.00 USD | 744,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8035` | 316.42 USD | 737,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8045` | 41,410.00 USD | 736,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8050` | 16,840,000.00 USD | 16,840,000.00 USD | 0.00 USD | 15,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8055` | 1,610.00 USD | 695,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8060` | 3,980,000.00 USD | 3,980,000.00 USD | 12,740.00 USD | 12,320.00 USD | 14,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8075` | 1,220.00 USD | 693,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8085` | 22,460.00 USD | 692,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8100` | 3,950,000.00 USD | 3,950,000.00 USD | 12,970.00 USD | 5,430.00 USD | 19,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8105` | 2,250.00 USD | 670,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8110` | 16,830,000.00 USD | 16,830,000.00 USD | 57,370.00 USD | 6,420.00 USD | 38,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8115` | 3,050.00 USD | 667,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8120` | 3,910,000.00 USD | 3,910,000.00 USD | 27,480.00 USD | 1,350.00 USD | 5,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8125` | 2,480.00 USD | 664,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8130` | 16,730,000.00 USD | 16,730,000.00 USD | 45,800.00 USD | 16,750.00 USD | 12,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8135` | 11,260.00 USD | 662,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8140` | 3,870,000.00 USD | 3,870,000.00 USD | 44,940.00 USD | 23,740.00 USD | 22,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8145` | 277.42 USD | 651,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8150` | 16,650,000.00 USD | 16,650,000.00 USD | 135,770.00 USD | 50,280.00 USD | 125,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8155` | 8,160.00 USD | 650,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8160` | 3,780,000.00 USD | 3,780,000.00 USD | 111,700.00 USD | 22,860.00 USD | 149,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8165` | 1,440.00 USD | 642,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8170` | 16,340,000.00 USD | 16,340,000.00 USD | 91,050.00 USD | 23,590.00 USD | 77,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8175` | 103,450.00 USD | 641,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8180` | 3,500,000.00 USD | 3,500,000.00 USD | 11,610.00 USD | 20,880.00 USD | 20,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8185` | 2,070.00 USD | 537,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8190` | 16,150,000.00 USD | 16,150,000.00 USD | 195,400.00 USD | 52,010.00 USD | 46,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8195` | 29,980.00 USD | 535,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8200` | 3,440,000.00 USD | 3,440,000.00 USD | 13,230.00 USD | 16,660.00 USD | 36,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8205` | 2,280.00 USD | 505,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8210` | 15,850,000.00 USD | 15,850,000.00 USD | 138,580.00 USD | 56,860.00 USD | 152,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8215` | 6,900.00 USD | 503,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8220` | 3,380,000.00 USD | 3,380,000.00 USD | 12,100.00 USD | 19,830.00 USD | 30,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8225` | 2,570.00 USD | 496,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8230` | 15,510,000.00 USD | 15,510,000.00 USD | 37,880.00 USD | 34,380.00 USD | 63,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8235` | 216.00 USD | 494,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8240` | 3,320,000.00 USD | 3,320,000.00 USD | 21,120.00 USD | 16,100.00 USD | 20,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8245` | 1,140.00 USD | 493,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8250` | 15,370,000.00 USD | 15,370,000.00 USD | 187,510.00 USD | 27,530.00 USD | 128,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8255` | 4,550.00 USD | 492,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8260` | 3,260,000.00 USD | 3,260,000.00 USD | 16,150.00 USD | 3,800.00 USD | 14,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8270` | 15,030,000.00 USD | 15,030,000.00 USD | 144,410.00 USD | 51,050.00 USD | 61,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8275` | 11,410.00 USD | 488,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8280` | 3,230,000.00 USD | 3,230,000.00 USD | 22,620.00 USD | 12,830.00 USD | 33,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8285` | 126,740.00 USD | 476,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8290` | 14,770,000.00 USD | 14,770,000.00 USD | 89,470.00 USD | 40,370.00 USD | 82,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8295` | 32,530.00 USD | 349,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8300` | 3,160,000.00 USD | 3,160,000.00 USD | 13,880.00 USD | 9,690.00 USD | 25,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8305` | 1,880.00 USD | 317,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8310` | 14,560,000.00 USD | 14,560,000.00 USD | 36,870.00 USD | 30,800.00 USD | 23,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8320` | 3,110,000.00 USD | 3,110,000.00 USD | 19,130.00 USD | 29,090.00 USD | 67,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8325` | 20,930.00 USD | 315,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8330` | 14,470,000.00 USD | 14,470,000.00 USD | 150,740.00 USD | 85,780.00 USD | 198,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8335` | 234.71 USD | 294,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8340` | 2,990,000.00 USD | 2,990,000.00 USD | 49,780.00 USD | 16,200.00 USD | 43,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8350` | 14,030,000.00 USD | 14,030,000.00 USD | 74,030.00 USD | 14,320.00 USD | 83,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8355` | 17,770.00 USD | 294,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8360` | 2,880,000.00 USD | 2,880,000.00 USD | 72,180.00 USD | 21,090.00 USD | 20,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8370` | 13,860,000.00 USD | 13,860,000.00 USD | 146,890.00 USD | 59,030.00 USD | 103,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8375` | 2,420.00 USD | 276,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8380` | 2,770,000.00 USD | 2,770,000.00 USD | 29,780.00 USD | 12,720.00 USD | 28,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8385` | 75,120.00 USD | 274,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8390` | 13,550,000.00 USD | 13,550,000.00 USD | 24,790.00 USD | 86,060.00 USD | 76,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8395` | 26,770.00 USD | 199,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8400` | 2,700,000.00 USD | 2,700,000.00 USD | 80,010.00 USD | 25,720.00 USD | 33,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8405` | 1,320.00 USD | 172,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8410` | 13,360,000.00 USD | 13,360,000.00 USD | 55,190.00 USD | 40,110.00 USD | 27,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8415` | 48,540.00 USD | 170,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8420` | 2,560,000.00 USD | 2,560,000.00 USD | 43,150.00 USD | 35,080.00 USD | 22,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8425` | 2,230.00 USD | 122,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8430` | 13,240,000.00 USD | 13,240,000.00 USD | 81,850.00 USD | 84,470.00 USD | 30,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8435` | 6,280.00 USD | 120,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8440` | 2,460,000.00 USD | 2,460,000.00 USD | 21,450.00 USD | 12,010.00 USD | 291.54 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8445` | 133.18 USD | 113,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8450` | 13,040,000.00 USD | 13,040,000.00 USD | 43,800.00 USD | 55,690.00 USD | 114,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8455` | 6,340.00 USD | 113,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8460` | 2,420,000.00 USD | 2,420,000.00 USD | 3,860.00 USD | 23,780.00 USD | 40,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8465` | 15,830.00 USD | 107,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8470` | 12,830,000.00 USD | 12,830,000.00 USD | 27,720.00 USD | 4,350.00 USD | 31,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8475` | 28,990.00 USD | 91,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8480` | 2,350,000.00 USD | 2,350,000.00 USD | 46,950.00 USD | 35,940.00 USD | 44,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8485` | 1,890.00 USD | 62,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8490` | 12,760,000.00 USD | 12,760,000.00 USD | 45,210.00 USD | 30,580.00 USD | 46,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8495` | 5,290.00 USD | 60,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8500` | 2,230,000.00 USD | 2,230,000.00 USD | 52,130.00 USD | 51,210.00 USD | 155,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8505` | 958.26 USD | 55,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8510` | 12,640,000.00 USD | 12,640,000.00 USD | 95,990.00 USD | 42,650.00 USD | 42,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8515` | 1,220.00 USD | 54,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8520` | 1,970,000.00 USD | 1,970,000.00 USD | 72,560.00 USD | 50,510.00 USD | 39,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8530` | 12,460,000.00 USD | 12,460,000.00 USD | 30,570.00 USD | 50,890.00 USD | 24,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8535` | 15,640.00 USD | 53,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8540` | 1,810,000.00 USD | 1,810,000.00 USD | 56,450.00 USD | 44,760.00 USD | 65,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8550` | 12,350,000.00 USD | 12,350,000.00 USD | 78,320.00 USD | 63,400.00 USD | 98,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8555` | 17,220.00 USD | 37,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8560` | 1,640,000.00 USD | 1,640,000.00 USD | 28,740.00 USD | 27,040.00 USD | 10,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8565` | 15,610.00 USD | 20,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8570` | 12,110,000.00 USD | 12,110,000.00 USD | 99,680.00 USD | 166,050.00 USD | 6,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8580` | 1,570,000.00 USD | 1,570,000.00 USD | 185,330.00 USD | 34,130.00 USD | 114.50 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8585` | 2,200.00 USD | 4,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8590` | 11,840,000.00 USD | 11,840,000.00 USD | 51,400.00 USD | 12,270.00 USD | 17,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8595` | 1,550.00 USD | 2,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8600` | 1,350,000.00 USD | 1,350,000.00 USD | 32,470.00 USD | 33,380.00 USD | 636.30 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8610` | 11,760,000.00 USD | 11,760,000.00 USD | 36,870.00 USD | 94,130.00 USD | 32,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8620` | 1,290,000.00 USD | 1,290,000.00 USD | 6,610.00 USD | 4,970.00 USD | 666.95 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8630` | 11,600,000.00 USD | 11,600,000.00 USD | 30,710.00 USD | 13,800.00 USD | 176,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8640` | 1,270,000.00 USD | 1,270,000.00 USD | 40,460.00 USD | 34,720.00 USD | 53,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8650` | 11,380,000.00 USD | 11,380,000.00 USD | 235,900.00 USD | 16,780.00 USD | 98,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8660` | 1,150,000.00 USD | 1,150,000.00 USD | 184,320.00 USD | 33,670.00 USD | 271.63 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8670` | 11,020,000.00 USD | 11,020,000.00 USD | 159,120.00 USD | 41,080.00 USD | 58,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8680` | 926,930.00 USD | 926,930.00 USD | 49,450.00 USD | 48,790.00 USD | 58,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8685` | 265.76 USD | 1,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8690` | 10,770,000.00 USD | 10,770,000.00 USD | 182,190.00 USD | 9,930.00 USD | 195,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8695` | 798.46 USD | 798.46 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8700` | 770,310.00 USD | 770,310.00 USD | 59,260.00 USD | 6,380.00 USD | 898.09 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8710` | 10,380,000.00 USD | 10,380,000.00 USD | 604,760.00 USD | 13,020.00 USD | 402,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8720` | 703,770.00 USD | 703,770.00 USD | 1,300.00 USD | 54,700.00 USD | 308,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8730` | 9,360,000.00 USD | 9,360,000.00 USD | 333,320.00 USD | 78,000.00 USD | 392,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8740` | 338,870.00 USD | 338,870.00 USD | 0.00 USD | 19,580.00 USD | 45,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8750` | 8,560,000.00 USD | 8,560,000.00 USD | 643,280.00 USD | 118,620.00 USD | 323,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8760` | 273,710.00 USD | 273,710.00 USD | 3,590.00 USD | 34,150.00 USD | 178,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8770` | 7,470,000.00 USD | 7,470,000.00 USD | 398,780.00 USD | 14,470.00 USD | 3,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8780` | 57,060.00 USD | 57,060.00 USD | 5,990.00 USD | 0.00 USD | 305.84 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8790` | 7,050,000.00 USD | 7,050,000.00 USD | 296,940.00 USD | 15,310.00 USD | 3,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8800` | 50,760.00 USD | 50,760.00 USD | 7,330.00 USD | 0.00 USD | 722.37 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8810` | 6,740,000.00 USD | 6,740,000.00 USD | 629,340.00 USD | 11,380.00 USD | 576.82 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8820` | 42,710.00 USD | 42,710.00 USD | 37,490.00 USD | 0.00 USD | 305.55 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8830` | 6,100,000.00 USD | 6,100,000.00 USD | 782,180.00 USD | 10,580.00 USD | 10,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8840` | 4,920.00 USD | 4,920.00 USD | 0.00 USD | 0.00 USD | 1,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8850` | 5,290,000.00 USD | 5,290,000.00 USD | 502,690.00 USD | 14,390.00 USD | 7,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8860` | 3,090.00 USD | 3,090.00 USD | 0.00 USD | 0.00 USD | 745.79 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8870` | 4,770,000.00 USD | 4,770,000.00 USD | 619,260.00 USD | 2,410.00 USD | 3,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8890` | 4,140,000.00 USD | 4,140,000.00 USD | 1,530,000.00 USD | 3,210.00 USD | 5,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8900` | 2,350.00 USD | 2,350.00 USD | 2,250.00 USD | 0.00 USD | 95.14 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8910` | 2,600,000.00 USD | 2,600,000.00 USD | 806,690.00 USD | 8,230.00 USD | 4,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8920` | 186,590.00 USD | 186,590.00 USD | 186,330.00 USD | 0.00 USD | 255.50 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8920` | 373,180.00 USD | 373,180.00 USD | 186,330.00 USD | 0.00 USD | 255.50 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8930` | 1,780,000.00 USD | 1,780,000.00 USD | 1,770,000.00 USD | 7,680.00 USD | 728.40 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.8935` | 3,590.00 USD | 3,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.8940` | 466,140.00 USD | 466,140.00 USD | 92,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8950` | 744,960.00 USD | 744,960.00 USD | 738,790.00 USD | 2,700.00 USD | 3,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8950` | 1,490,000.00 USD | 1,490,000.00 USD | 738,790.00 USD | 2,700.00 USD | 3,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8960` | 466,950.00 USD | 466,950.00 USD | 0.00 USD | 0.00 USD | 808.94 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8970` | 2,160,000.00 USD | 2,160,000.00 USD | 659,500.00 USD | 10,620.00 USD | 890.55 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8980` | 468,010.00 USD | 468,010.00 USD | 851.50 USD | 0.00 USD | 207.32 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8990` | 2,600,000.00 USD | 2,600,000.00 USD | 308,910.00 USD | 3,220.00 USD | 129,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9000` | 694,340.00 USD | 694,340.00 USD | 73,470.00 USD | 68,700.00 USD | 84,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9010` | 2,750,000.00 USD | 2,750,000.00 USD | 130,380.00 USD | 15,640.00 USD | 816.88 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9020` | 1,090,000.00 USD | 1,090,000.00 USD | 112,580.00 USD | 96,290.00 USD | 183,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9025` | 818.48 USD | 4,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9030` | 2,840,000.00 USD | 2,840,000.00 USD | 5,880.00 USD | 78,550.00 USD | 5,760.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9035` | 9,040.00 USD | 13,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9040` | 1,320,000.00 USD | 1,320,000.00 USD | 46,130.00 USD | 124,850.00 USD | 58,160.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9045` | 191.39 USD | 13,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9050` | 2,960,000.00 USD | 2,960,000.00 USD | 122,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9055` | 61,580.00 USD | 75,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9060` | 1,410,000.00 USD | 1,410,000.00 USD | 76,970.00 USD | 17,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9070` | 3,300,000.00 USD | 3,300,000.00 USD | 341,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9075` | 717.74 USD | 75,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9080` | 1,640,000.00 USD | 1,640,000.00 USD | 92,600.00 USD | 55,120.00 USD | 81,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9090` | 3,650,000.00 USD | 3,650,000.00 USD | 53,970.00 USD | 108,380.00 USD | 179,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9100` | 1,760,000.00 USD | 1,760,000.00 USD | 96,000.00 USD | 25,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9110` | 3,960,000.00 USD | 3,960,000.00 USD | 212,760.00 USD | 103,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9120` | 1,840,000.00 USD | 1,840,000.00 USD | 25,050.00 USD | 53,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9130` | 4,080,000.00 USD | 4,080,000.00 USD | 80,230.00 USD | 34,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9140` | 2,090,000.00 USD | 2,090,000.00 USD | 79,560.00 USD | 25,930.00 USD | 142,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9150` | 4,250,000.00 USD | 4,250,000.00 USD | 111,690.00 USD | 0.00 USD | 64,730.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9155` | 150.14 USD | 76,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9160` | 2,270,000.00 USD | 2,270,000.00 USD | 74,950.00 USD | 35,490.00 USD | 71,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9170` | 4,380,000.00 USD | 4,380,000.00 USD | 123,530.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9180` | 2,330,000.00 USD | 2,330,000.00 USD | 38,060.00 USD | 24,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9190` | 4,650,000.00 USD | 4,650,000.00 USD | 257,890.00 USD | 13,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9195` | 36,140.00 USD | 112,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9200` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 8,860.00 USD | 32,760.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9205` | 12,970.00 USD | 125,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9210` | 4,860,000.00 USD | 4,860,000.00 USD | 128,930.00 USD | 16,660.00 USD | 63,810.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9215` | 2,090.00 USD | 127,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9220` | 2,780,000.00 USD | 2,780,000.00 USD | 124,570.00 USD | 61,670.00 USD | 219,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9230` | 5,310,000.00 USD | 5,310,000.00 USD | 51,510.00 USD | 64,540.00 USD | 341,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9235` | 234.48 USD | 127,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9240` | 3,240,000.00 USD | 3,240,000.00 USD | 217,830.00 USD | 59,780.00 USD | 184,790.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9245` | 4,390.00 USD | 131,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9250` | 5,480,000.00 USD | 5,480,000.00 USD | 52,570.00 USD | 41,710.00 USD | 67,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9255` | 9,870.00 USD | 141,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9260` | 3,480,000.00 USD | 3,480,000.00 USD | 63,790.00 USD | 80,680.00 USD | 92,700.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9265` | 7,270.00 USD | 149,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9270` | 5,810,000.00 USD | 5,810,000.00 USD | 209,950.00 USD | 36,910.00 USD | 89,770.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9275` | 31,110.00 USD | 180,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9280` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 63,360.00 USD | 59,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9285` | 1,360.00 USD | 181,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9290` | 5,860,000.00 USD | 5,860,000.00 USD | 0.00 USD | 51,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9295` | 62,570.00 USD | 244,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9300` | 3,780,000.00 USD | 3,780,000.00 USD | 39,620.00 USD | 57,070.00 USD | 79,160.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9305` | 3,830.00 USD | 247,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9310` | 6,260,000.00 USD | 6,260,000.00 USD | 177,720.00 USD | 46,670.00 USD | 166,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9320` | 3,970,000.00 USD | 3,970,000.00 USD | 128,960.00 USD | 29,480.00 USD | 35,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9330` | 6,370,000.00 USD | 6,370,000.00 USD | 0.00 USD | 50,420.00 USD | 63,160.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9335` | 116.31 USD | 248,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9340` | 3,980,000.00 USD | 3,980,000.00 USD | 2,150.00 USD | 857.80 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9345` | 2,100.00 USD | 250,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9350` | 6,480,000.00 USD | 6,480,000.00 USD | 53,950.00 USD | 52,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9360` | 4,140,000.00 USD | 4,140,000.00 USD | 25,730.00 USD | 33,250.00 USD | 107,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9365` | 1,750.00 USD | 251,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9370` | 6,770,000.00 USD | 6,770,000.00 USD | 251,760.00 USD | 0.00 USD | 41,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9380` | 4,820,000.00 USD | 4,820,000.00 USD | 262,840.00 USD | 118,850.00 USD | 293,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9390` | 7,150,000.00 USD | 7,150,000.00 USD | 82,760.00 USD | 33,320.00 USD | 263,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9400` | 5,000,000.00 USD | 5,000,000.00 USD | 119,220.00 USD | 1,710.00 USD | 67,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9410` | 7,270,000.00 USD | 7,270,000.00 USD | 123,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9420` | 5,030,000.00 USD | 5,030,000.00 USD | 9,740.00 USD | 0.00 USD | 17,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9430` | 7,370,000.00 USD | 7,370,000.00 USD | 0.00 USD | 62,100.00 USD | 33,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9440` | 5,180,000.00 USD | 5,180,000.00 USD | 2,290.00 USD | 75,230.00 USD | 73,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9450` | 7,700,000.00 USD | 7,700,000.00 USD | 0.00 USD | 244,270.00 USD | 90,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9460` | 5,460,000.00 USD | 5,460,000.00 USD | 59,870.00 USD | 33,530.00 USD | 184,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9470` | 7,910,000.00 USD | 7,910,000.00 USD | 0.00 USD | 0.00 USD | 210,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9480` | 5,670,000.00 USD | 5,670,000.00 USD | 89,360.00 USD | 67,670.00 USD | 56,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9490` | 8,140,000.00 USD | 8,140,000.00 USD | 0.00 USD | 107,340.00 USD | 118,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9500` | 5,800,000.00 USD | 5,800,000.00 USD | 17,970.00 USD | 36,000.00 USD | 69,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9510` | 8,960,000.00 USD | 8,960,000.00 USD | 2,840.00 USD | 87,720.00 USD | 732,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9520` | 6,070,000.00 USD | 6,070,000.00 USD | 52,120.00 USD | 28,040.00 USD | 196,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9530` | 8,960,000.00 USD | 8,960,000.00 USD | 0.00 USD | 1,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9540` | 6,290,000.00 USD | 6,290,000.00 USD | 62,990.00 USD | 74,340.00 USD | 78,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9550` | 9,100,000.00 USD | 9,100,000.00 USD | 71,910.00 USD | 1,290.00 USD | 60,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9560` | 6,360,000.00 USD | 6,360,000.00 USD | 24,450.00 USD | 33,820.00 USD | 15,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9570` | 9,570,000.00 USD | 9,570,000.00 USD | 463,830.00 USD | 2,240.00 USD | 2,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9580` | 6,390,000.00 USD | 6,390,000.00 USD | 689.00 USD | 26,200.00 USD | 159.08 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9590` | 10,130,000.00 USD | 10,130,000.00 USD | 562,050.00 USD | 1,040.00 USD | 3,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9600` | 6,650,000.00 USD | 6,650,000.00 USD | 111,160.00 USD | 66,100.00 USD | 82,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9610` | 11,500,000.00 USD | 11,500,000.00 USD | 698,570.00 USD | 190,470.00 USD | 479,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9620` | 7,340,000.00 USD | 7,340,000.00 USD | 315,960.00 USD | 137,300.00 USD | 239,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9630` | 13,010,000.00 USD | 13,010,000.00 USD | 579,300.00 USD | 301,610.00 USD | 624,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9640` | 7,990,000.00 USD | 7,990,000.00 USD | 334,070.00 USD | 117,160.00 USD | 197,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9650` | 14,570,000.00 USD | 14,570,000.00 USD | 857,470.00 USD | 301,210.00 USD | 408,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9660` | 8,490,000.00 USD | 8,490,000.00 USD | 243,570.00 USD | 139,760.00 USD | 120,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9670` | 16,710,000.00 USD | 16,710,000.00 USD | 889,580.00 USD | 544,430.00 USD | 706,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9675` | 3,160.00 USD | 255,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9680` | 9,040,000.00 USD | 9,040,000.00 USD | 199,180.00 USD | 70,260.00 USD | 280,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9690` | 18,100,000.00 USD | 18,100,000.00 USD | 596,350.00 USD | 343,680.00 USD | 447,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9700` | 9,580,000.00 USD | 9,580,000.00 USD | 257,240.00 USD | 106,690.00 USD | 174,530.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9705` | 65,060.00 USD | 320,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9710` | 19,200,000.00 USD | 19,200,000.00 USD | 645,500.00 USD | 305,860.00 USD | 143,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9720` | 9,930,000.00 USD | 9,930,000.00 USD | 122,820.00 USD | 90,440.00 USD | 138,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9730` | 19,990,000.00 USD | 19,990,000.00 USD | 456,990.00 USD | 160,420.00 USD | 172,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9740` | 10,090,000.00 USD | 10,090,000.00 USD | 81,230.00 USD | 31,010.00 USD | 39,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9750` | 20,680,000.00 USD | 20,680,000.00 USD | 201,510.00 USD | 293,590.00 USD | 194,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9760` | 10,230,000.00 USD | 10,230,000.00 USD | 31,860.00 USD | 33,470.00 USD | 76,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9765` | 214.44 USD | 320,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9770` | 21,720,000.00 USD | 21,720,000.00 USD | 329,170.00 USD | 211,000.00 USD | 503,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9775` | 100.88 USD | 320,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9780` | 10,350,000.00 USD | 10,350,000.00 USD | 4,640.00 USD | 25,130.00 USD | 91,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9790` | 22,460,000.00 USD | 22,460,000.00 USD | 411,780.00 USD | 99,560.00 USD | 223,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9800` | 10,590,000.00 USD | 10,590,000.00 USD | 65,550.00 USD | 48,270.00 USD | 127,720.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9805` | 1,050.00 USD | 321,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9810` | 22,970,000.00 USD | 22,970,000.00 USD | 264,890.00 USD | 83,040.00 USD | 166,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9820` | 10,800,000.00 USD | 10,800,000.00 USD | 132,760.00 USD | 29,280.00 USD | 44,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9830` | 23,550,000.00 USD | 23,550,000.00 USD | 260,850.00 USD | 115,290.00 USD | 200,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9840` | 10,940,000.00 USD | 10,940,000.00 USD | 58,950.00 USD | 68,840.00 USD | 18,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9845` | 10,440.00 USD | 331,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9850` | 23,960,000.00 USD | 23,960,000.00 USD | 234,160.00 USD | 58,210.00 USD | 117,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9860` | 11,170,000.00 USD | 11,170,000.00 USD | 83,160.00 USD | 43,210.00 USD | 100,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9870` | 24,450,000.00 USD | 24,450,000.00 USD | 248,980.00 USD | 191,820.00 USD | 57,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9875` | 732.03 USD | 332,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9880` | 11,320,000.00 USD | 11,320,000.00 USD | 82,930.00 USD | 16,000.00 USD | 49,360.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9885` | 4,930.00 USD | 337,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9890` | 24,750,000.00 USD | 24,750,000.00 USD | 194,850.00 USD | 78,280.00 USD | 18,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9900` | 11,490,000.00 USD | 11,490,000.00 USD | 87,940.00 USD | 35,060.00 USD | 51,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9905` | 1,570.00 USD | 339,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9910` | 25,120,000.00 USD | 25,120,000.00 USD | 198,890.00 USD | 89,640.00 USD | 84,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9920` | 11,600,000.00 USD | 11,600,000.00 USD | 62,110.00 USD | 27,720.00 USD | 21,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9925` | 2,420.00 USD | 341,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9930` | 25,480,000.00 USD | 25,480,000.00 USD | 228,340.00 USD | 63,950.00 USD | 72,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9940` | 11,770,000.00 USD | 11,770,000.00 USD | 60,860.00 USD | 36,590.00 USD | 70,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9950` | 25,800,000.00 USD | 25,800,000.00 USD | 48,120.00 USD | 138,500.00 USD | 125,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9960` | 11,800,000.00 USD | 11,800,000.00 USD | 6,270.00 USD | 5,900.00 USD | 20,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9965` | 125.66 USD | 341,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9970` | 26,450,000.00 USD | 26,450,000.00 USD | 215,040.00 USD | 81,210.00 USD | 360,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9980` | 12,080,000.00 USD | 12,080,000.00 USD | 110,050.00 USD | 20,740.00 USD | 149,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9990` | 26,740,000.00 USD | 26,740,000.00 USD | 145,170.00 USD | 35,870.00 USD | 101,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 12,140,000.00 USD | 12,140,000.00 USD | 17,400.00 USD | 21,440.00 USD | 16,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 27,180,000.00 USD | 27,180,000.00 USD | 202,970.00 USD | 57,170.00 USD | 183,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 12,210,000.00 USD | 12,210,000.00 USD | 15,000.00 USD | 17,420.00 USD | 36,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 27,680,000.00 USD | 27,680,000.00 USD | 226,340.00 USD | 61,540.00 USD | 206,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 12,280,000.00 USD | 12,280,000.00 USD | 15,370.00 USD | 21,270.00 USD | 30,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 27,830,000.00 USD | 27,830,000.00 USD | 51,930.00 USD | 39,560.00 USD | 66,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 12,310,000.00 USD | 12,310,000.00 USD | 9,400.00 USD | 14,230.00 USD | 8,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 28,320,000.00 USD | 28,320,000.00 USD | 256,020.00 USD | 15,900.00 USD | 212,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 12,350,000.00 USD | 12,350,000.00 USD | 18,940.00 USD | 9,170.00 USD | 12,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 28,920,000.00 USD | 28,920,000.00 USD | 247,480.00 USD | 105,290.00 USD | 248,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 12,390,000.00 USD | 12,390,000.00 USD | 17,560.00 USD | 5,290.00 USD | 14,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 29,870,000.00 USD | 29,870,000.00 USD | 457,740.00 USD | 174,650.00 USD | 316,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 12,450,000.00 USD | 12,450,000.00 USD | 21,660.00 USD | 13,540.00 USD | 33,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 30,580,000.00 USD | 30,580,000.00 USD | 188,370.00 USD | 177,300.00 USD | 345,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 12,500,000.00 USD | 12,500,000.00 USD | 13,360.00 USD | 10,400.00 USD | 25,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 31,030,000.00 USD | 31,030,000.00 USD | 263,990.00 USD | 59,720.00 USD | 126,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.02` | 170.40 USD | 341,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.02` | 12,540,000.00 USD | 12,540,000.00 USD | 22,200.00 USD | 10,550.00 USD | 6,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 31,830,000.00 USD | 31,830,000.00 USD | 339,650.00 USD | 97,830.00 USD | 359,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 12,570,000.00 USD | 12,570,000.00 USD | 18,050.00 USD | 4,150.00 USD | 133.18 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 32,660,000.00 USD | 32,660,000.00 USD | 291,360.00 USD | 74,810.00 USD | 467,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 12,660,000.00 USD | 12,660,000.00 USD | 31,730.00 USD | 13,020.00 USD | 44,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 33,090,000.00 USD | 33,090,000.00 USD | 153,580.00 USD | 41,370.00 USD | 235,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 12,740,000.00 USD | 12,740,000.00 USD | 49,170.00 USD | 12,160.00 USD | 20,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 33,410,000.00 USD | 33,410,000.00 USD | 151,650.00 USD | 60,000.00 USD | 103,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 12,810,000.00 USD | 12,810,000.00 USD | 29,780.00 USD | 12,720.00 USD | 28,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 33,630,000.00 USD | 33,630,000.00 USD | 75,770.00 USD | 54,210.00 USD | 94,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 12,880,000.00 USD | 12,880,000.00 USD | 17,840.00 USD | 16,400.00 USD | 33,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 33,880,000.00 USD | 33,880,000.00 USD | 104,260.00 USD | 35,230.00 USD | 111,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 12,890,000.00 USD | 12,890,000.00 USD | 550.85 USD | 116.87 USD | 11,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 34,090,000.00 USD | 34,090,000.00 USD | 85,920.00 USD | 56,310.00 USD | 67,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 12,920,000.00 USD | 12,920,000.00 USD | 8,830.00 USD | 12,110.00 USD | 10,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 34,520,000.00 USD | 34,520,000.00 USD | 197,430.00 USD | 78,810.00 USD | 156,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 12,950,000.00 USD | 12,950,000.00 USD | 19,720.00 USD | 7,410.00 USD | 0.35 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 34,850,000.00 USD | 34,850,000.00 USD | 57,570.00 USD | 103,690.00 USD | 163,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 12,960,000.00 USD | 12,960,000.00 USD | 439.80 USD | 4,130.00 USD | 13,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 35,040,000.00 USD | 35,040,000.00 USD | 112,550.00 USD | 13,040.00 USD | 63,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 13,030,000.00 USD | 13,030,000.00 USD | 18,450.00 USD | 7,120.00 USD | 43,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 35,430,000.00 USD | 35,430,000.00 USD | 176,150.00 USD | 41,220.00 USD | 181,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 35,740,000.00 USD | 35,740,000.00 USD | 112,210.00 USD | 19,230.00 USD | 175,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.04` | 155.92 USD | 342,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.04` | 139.22 USD | 342,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.04` | 35,970,000.00 USD | 35,970,000.00 USD | 104,270.00 USD | 53,470.00 USD | 72,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 36,060,000.00 USD | 36,060,000.00 USD | 18,340.00 USD | 49,420.00 USD | 23,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 36,150,000.00 USD | 36,150,000.00 USD | 68,630.00 USD | 17,210.00 USD | 4,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 36,260,000.00 USD | 36,260,000.00 USD | 78,420.00 USD | 30,790.00 USD | 829.98 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 36,340,000.00 USD | 36,340,000.00 USD | 35,930.00 USD | 20,630.00 USD | 16,040.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 597.52 USD | 342,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 36,360,000.00 USD | 36,360,000.00 USD | 22,610.00 USD | 0.00 USD | 135.33 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 2,390.00 USD | 345,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 36,440,000.00 USD | 36,440,000.00 USD | 8,370.00 USD | 47,690.00 USD | 28,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 317.52 USD | 345,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 36,500,000.00 USD | 36,500,000.00 USD | 2,990.00 USD | 11,060.00 USD | 45,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.06` | 217.64 USD | 345,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.06` | 36,510,000.00 USD | 36,510,000.00 USD | 6,580.00 USD | 2,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 36,510,000.00 USD | 36,510,000.00 USD | 0.00 USD | 194.87 USD | 173.28 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 36,550,000.00 USD | 36,550,000.00 USD | 17,530.00 USD | 3,870.00 USD | 11,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 36,560,000.00 USD | 36,560,000.00 USD | 10,210.00 USD | 0.00 USD | 647.09 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 36,560,000.00 USD | 36,560,000.00 USD | 6,770.00 USD | 1,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 36,570,000.00 USD | 36,570,000.00 USD | 0.00 USD | 1,120.00 USD | 74.53 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 36,600,000.00 USD | 36,600,000.00 USD | 2,410.00 USD | 12,740.00 USD | 17,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.08` | 3,690.00 USD | 349,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.08` | 5,700.00 USD | 355,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.08` | 3,580.00 USD | 358,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.08` | 166.43 USD | 358,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.09` | 5,550.00 USD | 364,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.10` | 324.90 USD | 364,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.10` | 277.22 USD | 364,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.13` | 23,310.00 USD | 388,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.18` | 5,060.00 USD | 393,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.20` | 1,450.00 USD | 394,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.20` | 253.69 USD | 395,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.21` | 147.43 USD | 395,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.22` | 4,440.00 USD | 399,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.23` | 380.84 USD | 400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.25` | 2,850.00 USD | 402,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.26` | 2,670.00 USD | 405,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.28` | 2,300.00 USD | 407,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.28` | 39,880.00 USD | 447,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.29` | 226.80 USD | 447,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.30` | 114.40 USD | 448,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.30` | 1,070.00 USD | 449,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.30` | 635.85 USD | 449,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.31` | 9,950.00 USD | 459,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.31` | 1,020.00 USD | 460,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.31` | 31,530.00 USD | 492,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.33` | 6,340.00 USD | 498,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.33` | 21,970.00 USD | 520,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.33` | 358.30 USD | 520,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.33` | 1,520.00 USD | 522,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.34` | 2,190.00 USD | 524,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.34` | 6,860.00 USD | 531,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.34` | 21,400.00 USD | 552,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.37` | 358,280.00 USD | 911,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.41` | 4,450.00 USD | 915,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.44` | 402.08 USD | 916,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.44` | 288.68 USD | 916,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.50` | 9,760.00 USD | 926,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.51` | 4,020.00 USD | 930,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 144.34 USD | 930,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.58` | 133.21 USD | 930,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.58` | 17,930.00 USD | 948,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.60` | 9,580.00 USD | 957,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 21,330.00 USD | 979,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 36,530.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 39,140.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.68` | 2,280.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.69` | 440.71 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.69` | 292,630.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.70` | 167.09 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.71` | 205.67 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.72` | 9,700.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.73` | 226.05 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 560.67 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 2,080.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.1945` | 4,620,000.00 USD | 0.00 USD | 1,410.00 USD | `-77.74%` | `7,229.50` |
| `Live` | `Long` | `0.1955` | 4,620,000.00 USD | 0.00 USD | 2,410.00 USD | `-77.62%` | `12,310.50` |
| `Live` | `Long` | `0.1995` | 4,610,000.00 USD | 0.00 USD | 256.00 USD | `-77.16%` | `1,283.20` |
| `Live` | `Long` | `0.2045` | 4,610,000.00 USD | 0.00 USD | 204.50 USD | `-76.59%` | `1,000.00` |
| `Live` | `Long` | `0.2135` | 4,610,000.00 USD | 0.00 USD | 4,040.00 USD | `-75.56%` | `18,919.90` |
| `Live` | `Long` | `0.2195` | 4,610,000.00 USD | 0.00 USD | 852.58 USD | `-74.88%` | `3,884.20` |
| `Live` | `Long` | `0.2265` | 4,610,000.00 USD | 0.00 USD | 220.32 USD | `-74.07%` | `972.70` |
| `Live` | `Long` | `0.2355` | 4,610,000.00 USD | 0.00 USD | 1,030.00 USD | `-73.04%` | `4,353.10` |
| `Live` | `Long` | `0.2385` | 4,610,000.00 USD | 0.00 USD | 156.36 USD | `-72.70%` | `655.60` |
| `Live` | `Long` | `0.2505` | 4,610,000.00 USD | 0.00 USD | 2,540.00 USD | `-71.33%` | `10,152.10` |
| `Live` | `Long` | `0.2525` | 4,600,000.00 USD | 0.00 USD | 3,940.00 USD | `-71.10%` | `15,622.00` |
| `Live` | `Long` | `0.2645` | 4,600,000.00 USD | 0.00 USD | 2,610.00 USD | `-69.72%` | `9,865.70` |
| `Live` | `Long` | `0.2685` | 4,600,000.00 USD | 0.00 USD | 106.16 USD | `-69.27%` | `395.40` |
| `Live` | `Long` | `0.2725` | 4,600,000.00 USD | 0.00 USD | 1,910.00 USD | `-68.81%` | `7,000.00` |
| `Live` | `Long` | `0.2735` | 4,590,000.00 USD | 0.00 USD | 248.34 USD | `-68.69%` | `908.00` |
| `Live` | `Long` | `0.2755` | 4,590,000.00 USD | 0.00 USD | 178.91 USD | `-68.47%` | `649.40` |
| `Live` | `Long` | `0.2785` | 4,590,000.00 USD | 0.00 USD | 3,630.00 USD | `-68.12%` | `13,023.80` |
| `Live` | `Long` | `0.2795` | 4,590,000.00 USD | 0.00 USD | 24,070.00 USD | `-68.01%` | `86,117.40` |
| `Live` | `Long` | `0.2885` | 4,570,000.00 USD | 0.00 USD | 29,070.00 USD | `-66.98%` | `100,768.40` |
| `Live` | `Long` | `0.2945` | 4,540,000.00 USD | 0.00 USD | 687.92 USD | `-66.29%` | `2,335.90` |
| `Live` | `Long` | `0.2965` | 4,540,000.00 USD | 0.00 USD | 593.12 USD | `-66.06%` | `2,000.40` |
| `Live` | `Long` | `0.2975` | 4,540,000.00 USD | 0.00 USD | 4,330.00 USD | `-65.95%` | `14,561.30` |
| `Live` | `Long` | `0.3035` | 4,530,000.00 USD | 0.00 USD | 124.25 USD | `-65.26%` | `409.40` |
| `Live` | `Long` | `0.3115` | 4,530,000.00 USD | 0.00 USD | 373.46 USD | `-64.34%` | `1,198.90` |
| `Live` | `Long` | `0.3155` | 4,530,000.00 USD | 0.00 USD | 195.04 USD | `-63.89%` | `618.20` |
| `Live` | `Long` | `0.3245` | 4,530,000.00 USD | 0.00 USD | 202.81 USD | `-62.86%` | `625.00` |
| `Live` | `Long` | `0.3415` | 4,530,000.00 USD | 0.00 USD | 203.91 USD | `-60.91%` | `597.10` |
| `Live` | `Long` | `0.3445` | 4,530,000.00 USD | 0.00 USD | 103.35 USD | `-60.57%` | `300.00` |
| `Live` | `Long` | `0.3455` | 4,530,000.00 USD | 0.00 USD | 338.66 USD | `-60.45%` | `980.20` |
| `Live` | `Long` | `0.3465` | 4,530,000.00 USD | 0.00 USD | 3,470.00 USD | `-60.34%` | `10,000.00` |
| `Live` | `Long` | `0.3505` | 4,530,000.00 USD | 0.00 USD | 1,020.00 USD | `-59.88%` | `2,908.00` |
| `Live` | `Long` | `0.3585` | 4,530,000.00 USD | 0.00 USD | 28,450.00 USD | `-58.97%` | `79,368.10` |
| `Live` | `Long` | `0.3665` | 4,500,000.00 USD | 0.00 USD | 274.88 USD | `-58.05%` | `750.00` |
| `Live` | `Long` | `0.3685` | 4,500,000.00 USD | 0.00 USD | 2,940.00 USD | `-57.82%` | `7,985.90` |
| `Live` | `Long` | `0.3705` | 4,490,000.00 USD | 0.00 USD | 413.14 USD | `-57.59%` | `1,115.10` |
| `Live` | `Long` | `0.3725` | 4,490,000.00 USD | 0.00 USD | 4,260.00 USD | `-57.36%` | `11,446.70` |
| `Live` | `Long` | `0.3785` | 4,490,000.00 USD | 0.00 USD | 861.39 USD | `-56.68%` | `2,275.80` |
| `Live` | `Long` | `0.3795` | 4,490,000.00 USD | 0.00 USD | 278.02 USD | `-56.56%` | `732.60` |
| `Live` | `Long` | `0.3825` | 4,490,000.00 USD | 0.00 USD | 6,500.00 USD | `-56.22%` | `17,000.00` |
| `Live` | `Long` | `0.3845` | 4,480,000.00 USD | 0.00 USD | 1,750.00 USD | `-55.99%` | `4,562.20` |
| `Live` | `Long` | `0.3875` | 4,480,000.00 USD | 0.00 USD | 27,120.00 USD | `-55.65%` | `70,000.00` |
| `Live` | `Long` | `0.3895` | 4,450,000.00 USD | 0.00 USD | 2,980.00 USD | `-55.42%` | `7,661.70` |
| `Live` | `Long` | `0.3905` | 4,450,000.00 USD | 0.00 USD | 191.54 USD | `-55.30%` | `490.50` |
| `Live` | `Long` | `0.3925` | 4,450,000.00 USD | 0.00 USD | 5,030.00 USD | `-55.07%` | `12,808.60` |
| `Live` | `Long` | `0.3945` | 4,440,000.00 USD | 0.00 USD | 754.48 USD | `-54.84%` | `1,912.50` |
| `Live` | `Long` | `0.4035` | 4,440,000.00 USD | 0.00 USD | 935.03 USD | `-53.81%` | `2,317.30` |
| `Live` | `Long` | `0.4045` | 4,440,000.00 USD | 0.00 USD | 5,520.00 USD | `-53.70%` | `13,640.50` |
| `Live` | `Long` | `0.4055` | 4,440,000.00 USD | 0.00 USD | 735.13 USD | `-53.59%` | `1,812.90` |
| `Live` | `Long` | `0.4235` | 4,440,000.00 USD | 0.00 USD | 467.50 USD | `-51.53%` | `1,103.90` |
| `Live` | `Long` | `0.4295` | 4,440,000.00 USD | 0.00 USD | 300.65 USD | `-50.84%` | `700.00` |
| `Live` | `Long` | `0.4345` | 4,440,000.00 USD | 0.00 USD | 765.59 USD | `-50.27%` | `1,762.00` |
| `Live` | `Long` | `0.4385` | 4,440,000.00 USD | 0.00 USD | 122.91 USD | `-49.81%` | `280.30` |
| `Live` | `Long` | `0.4415` | 4,440,000.00 USD | 0.00 USD | 49,780.00 USD | `-49.46%` | `112,757.90` |
| `Live` | `Long` | `0.4435` | 4,390,000.00 USD | 0.00 USD | 10,840.00 USD | `-49.24%` | `24,432.10` |
| `Live` | `Long` | `0.4455` | 4,370,000.00 USD | 0.00 USD | 574.83 USD | `-49.01%` | `1,290.30` |
| `Live` | `Long` | `0.4465` | 4,370,000.00 USD | 0.00 USD | 19,600.00 USD | `-48.89%` | `43,906.00` |
| `Live` | `Long` | `0.4525` | 4,350,000.00 USD | 0.00 USD | 5,660.00 USD | `-48.21%` | `12,500.00` |
| `Live` | `Long` | `0.4535` | 4,350,000.00 USD | 0.00 USD | 702.74 USD | `-48.09%` | `1,549.60` |
| `Live` | `Long` | `0.4595` | 4,350,000.00 USD | 0.00 USD | 295.78 USD | `-47.40%` | `643.70` |
| `Live` | `Long` | `0.4755` | 4,350,000.00 USD | 0.00 USD | 500.27 USD | `-45.57%` | `1,052.10` |
| `Live` | `Long` | `0.4785` | 4,350,000.00 USD | 0.00 USD | 110.10 USD | `-45.23%` | `230.10` |
| `Live` | `Long` | `0.4835` | 4,350,000.00 USD | 0.00 USD | 174.01 USD | `-44.66%` | `359.90` |
| `Live` | `Long` | `0.4865` | 4,350,000.00 USD | 0.00 USD | 201.07 USD | `-44.31%` | `413.30` |
| `Live` | `Long` | `0.4885` | 4,350,000.00 USD | 0.00 USD | 6,570.00 USD | `-44.09%` | `13,442.10` |
| `Live` | `Long` | `0.4895` | 4,340,000.00 USD | 0.00 USD | 646.73 USD | `-43.97%` | `1,321.20` |
| `Live` | `Long` | `0.4915` | 4,340,000.00 USD | 0.00 USD | 3,370.00 USD | `-43.74%` | `6,848.70` |
| `Live` | `Long` | `0.4935` | 4,340,000.00 USD | 0.00 USD | 1,500.00 USD | `-43.51%` | `3,043.40` |
| `Live` | `Long` | `0.4945` | 4,330,000.00 USD | 0.00 USD | 3,820.00 USD | `-43.40%` | `7,724.00` |
| `Live` | `Long` | `0.4955` | 4,330,000.00 USD | 0.00 USD | 211.88 USD | `-43.28%` | `427.60` |
| `Live` | `Long` | `0.4965` | 4,330,000.00 USD | 0.00 USD | 259.97 USD | `-43.17%` | `523.60` |
| `Live` | `Long` | `0.4985` | 4,330,000.00 USD | 0.00 USD | 216.75 USD | `-42.94%` | `434.80` |
| `Live` | `Long` | `0.5015` | 4,330,000.00 USD | 0.00 USD | 212.49 USD | `-42.60%` | `423.70` |
| `Live` | `Long` | `0.5025` | 4,330,000.00 USD | 0.00 USD | 1,330.00 USD | `-42.48%` | `2,652.40` |
| `Live` | `Long` | `0.5055` | 4,330,000.00 USD | 0.00 USD | 211.25 USD | `-42.14%` | `417.90` |
| `Live` | `Long` | `0.5085` | 4,330,000.00 USD | 0.00 USD | 2,540.00 USD | `-41.80%` | `5,000.00` |
| `Live` | `Long` | `0.5095` | 4,330,000.00 USD | 0.00 USD | 195.75 USD | `-41.68%` | `384.20` |
| `Live` | `Long` | `0.5155` | 4,330,000.00 USD | 0.00 USD | 1,240.00 USD | `-40.99%` | `2,409.50` |
| `Live` | `Long` | `0.5165` | 4,320,000.00 USD | 0.00 USD | 15,330.00 USD | `-40.88%` | `29,690.00` |
| `Live` | `Long` | `0.5175` | 4,310,000.00 USD | 0.00 USD | 213.68 USD | `-40.77%` | `412.90` |
| `Live` | `Long` | `0.5185` | 4,310,000.00 USD | 0.00 USD | 121.74 USD | `-40.65%` | `234.80` |
| `Live` | `Long` | `0.5205` | 4,310,000.00 USD | 0.00 USD | 864.13 USD | `-40.42%` | `1,660.20` |
| `Live` | `Long` | `0.5245` | 4,310,000.00 USD | 0.00 USD | 5,280.00 USD | `-39.96%` | `10,075.20` |
| `Live` | `Long` | `0.5255` | 4,300,000.00 USD | 0.00 USD | 31,530.00 USD | `-39.85%` | `60,000.00` |
| `Live` | `Long` | `0.5275` | 4,270,000.00 USD | 0.00 USD | 348.36 USD | `-39.62%` | `660.40` |
| `Live` | `Long` | `0.5285` | 4,270,000.00 USD | 0.00 USD | 2,590.00 USD | `-39.51%` | `4,897.40` |
| `Live` | `Long` | `0.5295` | 4,270,000.00 USD | 0.00 USD | 123,640.00 USD | `-39.39%` | `233,498.70` |
| `Live` | `Long` | `0.5325` | 4,140,000.00 USD | 0.00 USD | 2,680.00 USD | `-39.05%` | `5,038.10` |
| `Live` | `Long` | `0.5345` | 4,140,000.00 USD | 0.00 USD | 417.12 USD | `-38.82%` | `780.40` |
| `Live` | `Long` | `0.5365` | 4,140,000.00 USD | 0.00 USD | 131.55 USD | `-38.59%` | `245.20` |
| `Live` | `Long` | `0.5375` | 4,140,000.00 USD | 0.00 USD | 7,850.00 USD | `-38.48%` | `14,603.90` |
| `Live` | `Long` | `0.5395` | 4,130,000.00 USD | 0.00 USD | 319.98 USD | `-38.25%` | `593.10` |
| `Live` | `Long` | `0.5405` | 4,130,000.00 USD | 0.00 USD | 7,090.00 USD | `-38.13%` | `13,118.90` |
| `Live` | `Long` | `0.5425` | 4,130,000.00 USD | 0.00 USD | 269.13 USD | `-37.90%` | `496.10` |
| `Live` | `Long` | `0.5445` | 4,130,000.00 USD | 0.00 USD | 230.32 USD | `-37.68%` | `423.00` |
| `Live` | `Long` | `0.5455` | 4,130,000.00 USD | 0.00 USD | 5,930.00 USD | `-37.56%` | `10,862.70` |
| `Live` | `Long` | `0.5465` | 4,120,000.00 USD | 0.00 USD | 272.87 USD | `-37.45%` | `499.30` |
| `Live` | `Long` | `0.5475` | 4,120,000.00 USD | 0.00 USD | 1,240.00 USD | `-37.33%` | `2,257.90` |
| `Live` | `Long` | `0.5495` | 4,120,000.00 USD | 0.00 USD | 28,790.00 USD | `-37.10%` | `52,392.10` |
| `Live` | `Long` | `0.5505` | 4,090,000.00 USD | 0.00 USD | 248.06 USD | `-36.99%` | `450.60` |
| `Live` | `Long` | `0.5515` | 4,090,000.00 USD | 0.00 USD | 160.93 USD | `-36.87%` | `291.80` |
| `Live` | `Long` | `0.5525` | 4,090,000.00 USD | 0.00 USD | 582.56 USD | `-36.76%` | `1,054.40` |
| `Live` | `Long` | `0.5535` | 4,090,000.00 USD | 0.00 USD | 271.88 USD | `-36.65%` | `491.20` |
| `Live` | `Long` | `0.5545` | 4,090,000.00 USD | 0.00 USD | 531.60 USD | `-36.53%` | `958.70` |
| `Live` | `Long` | `0.5555` | 4,090,000.00 USD | 0.00 USD | 7,950.00 USD | `-36.42%` | `14,310.10` |
| `Live` | `Long` | `0.5585` | 4,080,000.00 USD | 0.00 USD | 141.97 USD | `-36.07%` | `254.20` |
| `Live` | `Long` | `0.5595` | 4,080,000.00 USD | 0.00 USD | 304.93 USD | `-35.96%` | `545.00` |
| `Live` | `Long` | `0.5605` | 4,080,000.00 USD | 0.00 USD | 441.84 USD | `-35.84%` | `788.30` |
| `Live` | `Long` | `0.5625` | 4,080,000.00 USD | 0.00 USD | 18,470.00 USD | `-35.61%` | `32,832.10` |
| `Live` | `Long` | `0.5635` | 4,060,000.00 USD | 0.00 USD | 195.93 USD | `-35.50%` | `347.70` |
| `Live` | `Long` | `0.5655` | 4,060,000.00 USD | 0.00 USD | 8,190.00 USD | `-35.27%` | `14,484.70` |
| `Live` | `Long` | `0.5665` | 4,050,000.00 USD | 0.00 USD | 570.01 USD | `-35.16%` | `1,006.20` |
| `Live` | `Long` | `0.5675` | 4,050,000.00 USD | 0.00 USD | 1,560.00 USD | `-35.04%` | `2,747.00` |
| `Live` | `Long` | `0.5695` | 4,050,000.00 USD | 0.00 USD | 973.22 USD | `-34.81%` | `1,708.90` |
| `Live` | `Long` | `0.5725` | 4,050,000.00 USD | 0.00 USD | 139.23 USD | `-34.47%` | `243.20` |
| `Live` | `Long` | `0.5735` | 4,050,000.00 USD | 0.00 USD | 182.72 USD | `-34.36%` | `318.60` |
| `Live` | `Long` | `0.5745` | 4,050,000.00 USD | 0.00 USD | 144.03 USD | `-34.24%` | `250.70` |
| `Live` | `Long` | `0.5755` | 4,050,000.00 USD | 0.00 USD | 1,010.00 USD | `-34.13%` | `1,759.90` |
| `Live` | `Long` | `0.5765` | 4,050,000.00 USD | 0.00 USD | 1,150.00 USD | `-34.01%` | `1,994.20` |
| `Live` | `Long` | `0.5775` | 4,050,000.00 USD | 0.00 USD | 497.75 USD | `-33.90%` | `861.90` |
| `Live` | `Long` | `0.5785` | 4,050,000.00 USD | 0.00 USD | 119.34 USD | `-33.78%` | `206.30` |
| `Live` | `Long` | `0.5795` | 4,050,000.00 USD | 0.00 USD | 212.85 USD | `-33.67%` | `367.30` |
| `Live` | `Long` | `0.5805` | 4,050,000.00 USD | 0.00 USD | 1,410.00 USD | `-33.55%` | `2,422.00` |
| `Live` | `Long` | `0.5825` | 4,040,000.00 USD | 0.00 USD | 6,470.00 USD | `-33.33%` | `11,099.00` |
| `Live` | `Long` | `0.5835` | 4,040,000.00 USD | 0.00 USD | 1,750.00 USD | `-33.21%` | `3,000.00` |
| `Live` | `Long` | `0.5855` | 4,040,000.00 USD | 0.00 USD | 2,640.00 USD | `-32.98%` | `4,508.30` |
| `Live` | `Long` | `0.5865` | 4,030,000.00 USD | 0.00 USD | 466.85 USD | `-32.87%` | `796.00` |
| `Live` | `Long` | `0.5875` | 4,030,000.00 USD | 0.00 USD | 969.32 USD | `-32.75%` | `1,649.90` |
| `Live` | `Long` | `0.5885` | 4,030,000.00 USD | 0.00 USD | 311.14 USD | `-32.64%` | `528.70` |
| `Live` | `Long` | `0.5925` | 4,030,000.00 USD | 0.00 USD | 994.16 USD | `-32.18%` | `1,677.90` |
| `Live` | `Long` | `0.5935` | 4,030,000.00 USD | 0.00 USD | 132.41 USD | `-32.07%` | `223.10` |
| `Live` | `Long` | `0.5945` | 4,030,000.00 USD | 0.00 USD | 8,600.00 USD | `-31.95%` | `14,462.30` |
| `Live` | `Long` | `0.5965` | 4,020,000.00 USD | 0.00 USD | 5,540.00 USD | `-31.72%` | `9,295.80` |
| `Live` | `Long` | `0.5995` | 4,020,000.00 USD | 0.00 USD | 151.97 USD | `-31.38%` | `253.50` |
| `Live` | `Long` | `0.6005` | 4,020,000.00 USD | 0.00 USD | 6,840.00 USD | `-31.27%` | `11,390.00` |
| `Live` | `Long` | `0.6025` | 4,010,000.00 USD | 0.00 USD | 432.35 USD | `-31.04%` | `717.60` |
| `Live` | `Long` | `0.6055` | 4,010,000.00 USD | 0.00 USD | 238.51 USD | `-30.69%` | `393.90` |
| `Live` | `Long` | `0.6075` | 4,010,000.00 USD | 0.00 USD | 851.05 USD | `-30.46%` | `1,400.90` |
| `Live` | `Long` | `0.6085` | 4,010,000.00 USD | 0.00 USD | 272.24 USD | `-30.35%` | `447.40` |
| `Live` | `Long` | `0.6105` | 4,010,000.00 USD | 0.00 USD | 2,750.00 USD | `-30.12%` | `4,500.00` |
| `Live` | `Long` | `0.6115` | 4,000,000.00 USD | 0.00 USD | 6,780.00 USD | `-30.01%` | `11,093.80` |
| `Live` | `Long` | `0.6125` | 4,000,000.00 USD | 0.00 USD | 768.01 USD | `-29.89%` | `1,253.90` |
| `Live` | `Long` | `0.6135` | 4,000,000.00 USD | 0.00 USD | 245.40 USD | `-29.78%` | `400.00` |
| `Live` | `Long` | `0.6145` | 4,000,000.00 USD | 0.00 USD | 3,430.00 USD | `-29.66%` | `5,579.50` |
| `Live` | `Long` | `0.6155` | 3,990,000.00 USD | 0.00 USD | 935.13 USD | `-29.55%` | `1,519.30` |
| `Live` | `Long` | `0.6165` | 3,990,000.00 USD | 0.00 USD | 29,900.00 USD | `-29.43%` | `48,503.10` |
| `Live` | `Long` | `0.6175` | 3,960,000.00 USD | 0.00 USD | 2,600.00 USD | `-29.32%` | `4,205.30` |
| `Live` | `Long` | `0.6185` | 3,960,000.00 USD | 0.00 USD | 4,400.00 USD | `-29.21%` | `7,107.00` |
| `Live` | `Long` | `0.6195` | 3,960,000.00 USD | 0.00 USD | 1,050.00 USD | `-29.09%` | `1,700.60` |
| `Live` | `Long` | `0.6215` | 3,950,000.00 USD | 0.00 USD | 8,420.00 USD | `-28.86%` | `13,552.00` |
| `Live` | `Long` | `0.6245` | 3,950,000.00 USD | 0.00 USD | 619.32 USD | `-28.52%` | `991.70` |
| `Live` | `Long` | `0.6255` | 3,950,000.00 USD | 0.00 USD | 32,070.00 USD | `-28.40%` | `51,265.70` |
| `Live` | `Long` | `0.6285` | 3,910,000.00 USD | 0.00 USD | 102.45 USD | `-28.06%` | `163.00` |
| `Live` | `Long` | `0.6305` | 3,910,000.00 USD | 0.00 USD | 319.35 USD | `-27.83%` | `506.50` |
| `Live` | `Long` | `0.6315` | 3,910,000.00 USD | 0.00 USD | 13,570.00 USD | `-27.72%` | `21,483.80` |
| `Live` | `Long` | `0.6335` | 3,900,000.00 USD | 0.00 USD | 16,340.00 USD | `-27.49%` | `25,791.20` |
| `Live` | `Long` | `0.6345` | 3,880,000.00 USD | 0.00 USD | 450.05 USD | `-27.37%` | `709.30` |
| `Live` | `Long` | `0.6365` | 3,880,000.00 USD | 0.00 USD | 3,060.00 USD | `-27.14%` | `4,804.70` |
| `Live` | `Long` | `0.6375` | 3,880,000.00 USD | 0.00 USD | 130.62 USD | `-27.03%` | `204.90` |
| `Live` | `Long` | `0.6395` | 3,880,000.00 USD | 0.00 USD | 244.03 USD | `-26.80%` | `381.60` |
| `Live` | `Long` | `0.6405` | 3,880,000.00 USD | 0.00 USD | 939.17 USD | `-26.69%` | `1,466.30` |
| `Live` | `Long` | `0.6415` | 3,880,000.00 USD | 0.00 USD | 86,920.00 USD | `-26.57%` | `135,497.00` |
| `Live` | `Long` | `0.6425` | 3,790,000.00 USD | 0.00 USD | 1,260.00 USD | `-26.46%` | `1,956.60` |
| `Live` | `Long` | `0.6435` | 3,790,000.00 USD | 0.00 USD | 657.79 USD | `-26.34%` | `1,022.20` |
| `Live` | `Long` | `0.6445` | 3,790,000.00 USD | 0.00 USD | 65,790.00 USD | `-26.23%` | `102,072.40` |
| `Live` | `Long` | `0.6455` | 3,720,000.00 USD | 0.00 USD | 14,370.00 USD | `-26.11%` | `22,268.90` |
| `Live` | `Long` | `0.6465` | 3,710,000.00 USD | 0.00 USD | 146.76 USD | `-26.00%` | `227.00` |
| `Live` | `Long` | `0.6475` | 3,710,000.00 USD | 0.00 USD | 8,240.00 USD | `-25.89%` | `12,723.20` |
| `Live` | `Long` | `0.6485` | 3,700,000.00 USD | 0.00 USD | 668.34 USD | `-25.77%` | `1,030.60` |
| `Live` | `Long` | `0.6495` | 3,700,000.00 USD | 0.00 USD | 325,470.00 USD | `-25.66%` | `501,111.00` |
| `Live` | `Long` | `0.6505` | 3,370,000.00 USD | 0.00 USD | 631.12 USD | `-25.54%` | `970.20` |
| `Live` | `Long` | `0.6515` | 3,370,000.00 USD | 0.00 USD | 403,320.00 USD | `-25.43%` | `619,065.10` |
| `Live` | `Long` | `0.6535` | 2,970,000.00 USD | 0.00 USD | 126,530.00 USD | `-25.20%` | `193,618.10` |
| `Live` | `Long` | `0.6545` | 2,840,000.00 USD | 0.00 USD | 1,150.00 USD | `-25.08%` | `1,761.60` |
| `Live` | `Long` | `0.6555` | 2,840,000.00 USD | 0.00 USD | 1,170.00 USD | `-24.97%` | `1,777.80` |
| `Live` | `Long` | `0.6565` | 2,840,000.00 USD | 0.00 USD | 8,270.00 USD | `-24.86%` | `12,591.20` |
| `Live` | `Long` | `0.6575` | 2,830,000.00 USD | 0.00 USD | 13,280.00 USD | `-24.74%` | `20,198.10` |
| `Live` | `Long` | `0.6585` | 2,820,000.00 USD | 0.00 USD | 2,970.00 USD | `-24.63%` | `4,508.30` |
| `Live` | `Long` | `0.6595` | 2,820,000.00 USD | 0.00 USD | 329.75 USD | `-24.51%` | `500.00` |
| `Live` | `Long` | `0.6615` | 2,820,000.00 USD | 0.00 USD | 126,890.00 USD | `-24.28%` | `191,817.10` |
| `Live` | `Long` | `0.6625` | 2,690,000.00 USD | 0.00 USD | 788.97 USD | `-24.17%` | `1,190.90` |
| `Live` | `Long` | `0.6645` | 2,690,000.00 USD | 0.00 USD | 448.54 USD | `-23.94%` | `675.00` |
| `Live` | `Long` | `0.6675` | 2,690,000.00 USD | 0.00 USD | 5,280.00 USD | `-23.60%` | `7,907.60` |
| `Live` | `Long` | `0.6685` | 2,680,000.00 USD | 0.00 USD | 2,810.00 USD | `-23.48%` | `4,203.00` |
| `Live` | `Long` | `0.6705` | 2,680,000.00 USD | 0.00 USD | 2,290.00 USD | `-23.25%` | `3,411.50` |
| `Live` | `Long` | `0.6715` | 2,680,000.00 USD | 0.00 USD | 8,500.00 USD | `-23.14%` | `12,661.20` |
| `Live` | `Long` | `0.6725` | 2,670,000.00 USD | 0.00 USD | 1,450.00 USD | `-23.02%` | `2,162.40` |
| `Live` | `Long` | `0.6735` | 2,670,000.00 USD | 0.00 USD | 27,680.00 USD | `-22.91%` | `41,094.80` |
| `Live` | `Long` | `0.6745` | 2,640,000.00 USD | 0.00 USD | 6,520.00 USD | `-22.80%` | `9,673.20` |
| `Live` | `Long` | `0.6755` | 2,630,000.00 USD | 0.00 USD | 111.59 USD | `-22.68%` | `165.20` |
| `Live` | `Long` | `0.6765` | 2,630,000.00 USD | 0.00 USD | 1,040.00 USD | `-22.57%` | `1,539.20` |
| `Live` | `Long` | `0.6785` | 2,630,000.00 USD | 0.00 USD | 250.77 USD | `-22.34%` | `369.60` |
| `Live` | `Long` | `0.6795` | 2,630,000.00 USD | 0.00 USD | 5,620.00 USD | `-22.22%` | `8,270.70` |
| `Live` | `Long` | `0.6805` | 2,630,000.00 USD | 0.00 USD | 1,600.00 USD | `-22.11%` | `2,348.00` |
| `Live` | `Long` | `0.6815` | 2,630,000.00 USD | 0.00 USD | 3,380.00 USD | `-21.99%` | `4,954.70` |
| `Live` | `Long` | `0.6825` | 2,620,000.00 USD | 0.00 USD | 15,920.00 USD | `-21.88%` | `23,330.00` |
| `Live` | `Long` | `0.6835` | 2,610,000.00 USD | 0.00 USD | 11,170.00 USD | `-21.77%` | `16,336.60` |
| `Live` | `Long` | `0.6845` | 2,600,000.00 USD | 0.00 USD | 5,790.00 USD | `-21.65%` | `8,455.80` |
| `Live` | `Long` | `0.6875` | 2,590,000.00 USD | 0.00 USD | 2,380.00 USD | `-21.31%` | `3,458.70` |
| `Live` | `Long` | `0.6885` | 2,590,000.00 USD | 0.00 USD | 83,790.00 USD | `-21.19%` | `121,695.30` |
| `Live` | `Long` | `0.6895` | 2,500,000.00 USD | 0.00 USD | 2,110.00 USD | `-21.08%` | `3,065.00` |
| `Live` | `Long` | `0.6905` | 2,500,000.00 USD | 0.00 USD | 3,360.00 USD | `-20.96%` | `4,864.60` |
| `Live` | `Long` | `0.6915` | 2,500,000.00 USD | 0.00 USD | 8,970.00 USD | `-20.85%` | `12,967.20` |
| `Live` | `Long` | `0.6935` | 2,490,000.00 USD | 0.00 USD | 2,980.00 USD | `-20.62%` | `4,299.80` |
| `Live` | `Long` | `0.6945` | 2,490,000.00 USD | 0.00 USD | 722.28 USD | `-20.51%` | `1,040.00` |
| `Live` | `Long` | `0.6965` | 2,490,000.00 USD | 0.00 USD | 704.37 USD | `-20.28%` | `1,011.30` |
| `Live` | `Long` | `0.6975` | 2,480,000.00 USD | 0.00 USD | 2,400.00 USD | `-20.16%` | `3,440.40` |
| `Live` | `Long` | `0.6985` | 2,480,000.00 USD | 0.00 USD | 1,930.00 USD | `-20.05%` | `2,759.10` |
| `Live` | `Long` | `0.6995` | 2,480,000.00 USD | 0.00 USD | 879.97 USD | `-19.93%` | `1,258.00` |
| `Live` | `Long` | `0.7015` | 2,480,000.00 USD | 0.00 USD | 383.72 USD | `-19.70%` | `547.00` |
| `Live` | `Long` | `0.7045` | 2,480,000.00 USD | 0.00 USD | 759.59 USD | `-19.36%` | `1,078.20` |
| `Live` | `Long` | `0.7055` | 2,480,000.00 USD | 0.00 USD | 115.00 USD | `-19.25%` | `163.00` |
| `Live` | `Long` | `0.7065` | 2,480,000.00 USD | 0.00 USD | 769.59 USD | `-19.13%` | `1,089.30` |
| `Live` | `Long` | `0.7075` | 2,480,000.00 USD | 0.00 USD | 787.73 USD | `-19.02%` | `1,113.40` |
| `Live` | `Long` | `0.7085` | 2,480,000.00 USD | 0.00 USD | 3,890.00 USD | `-18.90%` | `5,484.60` |
| `Live` | `Long` | `0.7095` | 2,470,000.00 USD | 0.00 USD | 2,720.00 USD | `-18.79%` | `3,833.70` |
| `Live` | `Long` | `0.7105` | 2,470,000.00 USD | 0.00 USD | 3,530.00 USD | `-18.67%` | `4,964.90` |
| `Live` | `Long` | `0.7115` | 2,470,000.00 USD | 0.00 USD | 4,090.00 USD | `-18.56%` | `5,749.90` |
| `Live` | `Long` | `0.7125` | 2,460,000.00 USD | 0.00 USD | 156.39 USD | `-18.45%` | `219.50` |
| `Live` | `Long` | `0.7175` | 2,460,000.00 USD | 0.00 USD | 8,820.00 USD | `-17.87%` | `12,295.90` |
| `Live` | `Long` | `0.7195` | 2,450,000.00 USD | 0.00 USD | 11,720.00 USD | `-17.64%` | `16,293.90` |
| `Live` | `Long` | `0.7205` | 2,440,000.00 USD | 0.00 USD | 120.54 USD | `-17.53%` | `167.30` |
| `Live` | `Long` | `0.7225` | 2,440,000.00 USD | 0.00 USD | 652.13 USD | `-17.30%` | `902.60` |
| `Live` | `Long` | `0.7255` | 2,440,000.00 USD | 0.00 USD | 2,660.00 USD | `-16.96%` | `3,662.80` |
| `Live` | `Long` | `0.7265` | 2,440,000.00 USD | 0.00 USD | 1,060.00 USD | `-16.84%` | `1,453.70` |
| `Live` | `Long` | `0.7275` | 2,440,000.00 USD | 0.00 USD | 762.57 USD | `-16.73%` | `1,048.20` |
| `Live` | `Long` | `0.7285` | 2,440,000.00 USD | 0.00 USD | 214.03 USD | `-16.61%` | `293.80` |
| `Live` | `Long` | `0.7295` | 2,440,000.00 USD | 0.00 USD | 375.98 USD | `-16.50%` | `515.40` |
| `Live` | `Long` | `0.7305` | 2,440,000.00 USD | 0.00 USD | 119.88 USD | `-16.39%` | `164.10` |
| `Live` | `Long` | `0.7315` | 2,440,000.00 USD | 0.00 USD | 31,890.00 USD | `-16.27%` | `43,601.40` |
| `Live` | `Long` | `0.7325` | 2,400,000.00 USD | 0.00 USD | 907.93 USD | `-16.16%` | `1,239.50` |
| `Live` | `Long` | `0.7345` | 2,400,000.00 USD | 0.00 USD | 2,340.00 USD | `-15.93%` | `3,185.40` |
| `Live` | `Long` | `0.7355` | 2,400,000.00 USD | 0.00 USD | 51,920.00 USD | `-15.81%` | `70,595.50` |
| `Live` | `Long` | `0.7365` | 2,350,000.00 USD | 0.00 USD | 6,900.00 USD | `-15.70%` | `9,366.00` |
| `Live` | `Long` | `0.7375` | 2,340,000.00 USD | 0.00 USD | 203.11 USD | `-15.58%` | `275.40` |
| `Live` | `Long` | `0.7385` | 2,340,000.00 USD | 0.00 USD | 5,940.00 USD | `-15.47%` | `8,037.10` |
| `Live` | `Long` | `0.7405` | 2,340,000.00 USD | 0.00 USD | 3,530.00 USD | `-15.24%` | `4,766.70` |
| `Live` | `Long` | `0.7415` | 2,330,000.00 USD | 0.00 USD | 382.61 USD | `-15.13%` | `516.00` |
| `Live` | `Long` | `0.7425` | 2,330,000.00 USD | 0.00 USD | 784,090.00 USD | `-15.01%` | `1,056,015.30` |
| `Live` | `Long` | `0.7445` | 1,550,000.00 USD | 0.00 USD | 105.64 USD | `-14.78%` | `141.90` |
| `Live` | `Long` | `0.7455` | 1,550,000.00 USD | 0.00 USD | 1,990.00 USD | `-14.67%` | `2,666.60` |
| `Live` | `Long` | `0.7475` | 1,550,000.00 USD | 0.00 USD | 103,310.00 USD | `-14.44%` | `138,200.90` |
| `Live` | `Long` | `0.7485` | 1,440,000.00 USD | 0.00 USD | 105.91 USD | `-14.32%` | `141.50` |
| `Live` | `Long` | `0.7495` | 1,440,000.00 USD | 0.00 USD | 599.60 USD | `-14.21%` | `800.00` |
| `Live` | `Long` | `0.7515` | 1,440,000.00 USD | 0.00 USD | 1,210.00 USD | `-13.98%` | `1,613.50` |
| `Live` | `Long` | `0.7525` | 1,440,000.00 USD | 0.00 USD | 106.03 USD | `-13.87%` | `140.90` |
| `Live` | `Long` | `0.7535` | 1,440,000.00 USD | 0.00 USD | 2,020.00 USD | `-13.75%` | `2,674.80` |
| `Live` | `Long` | `0.7545` | 1,440,000.00 USD | 0.00 USD | 16,010.00 USD | `-13.64%` | `21,222.10` |
| `Live` | `Long` | `0.7575` | 1,420,000.00 USD | 0.00 USD | 1,900.00 USD | `-13.29%` | `2,514.80` |
| `Live` | `Long` | `0.7585` | 1,420,000.00 USD | 0.00 USD | 36,710.00 USD | `-13.18%` | `48,399.00` |
| `Live` | `Long` | `0.7595` | 1,380,000.00 USD | 0.00 USD | 4,500.00 USD | `-13.07%` | `5,928.80` |
| `Live` | `Long` | `0.7615` | 1,380,000.00 USD | 0.00 USD | 351.43 USD | `-12.84%` | `461.50` |
| `Live` | `Long` | `0.7635` | 1,380,000.00 USD | 0.00 USD | 5,110.00 USD | `-12.61%` | `6,696.30` |
| `Live` | `Long` | `0.7645` | 1,370,000.00 USD | 0.00 USD | 3,510.00 USD | `-12.49%` | `4,596.60` |
| `Live` | `Long` | `0.7655` | 1,370,000.00 USD | 0.00 USD | 320,960.00 USD | `-12.38%` | `419,277.50` |
| `Live` | `Long` | `0.7665` | 1,050,000.00 USD | 0.00 USD | 1,260.00 USD | `-12.26%` | `1,649.10` |
| `Live` | `Long` | `0.7675` | 1,050,000.00 USD | 0.00 USD | 10,510.00 USD | `-12.15%` | `13,688.30` |
| `Live` | `Long` | `0.7685` | 1,040,000.00 USD | 0.00 USD | 499.99 USD | `-12.04%` | `650.60` |
| `Live` | `Long` | `0.7695` | 1,040,000.00 USD | 0.00 USD | 144,250.00 USD | `-11.92%` | `187,459.50` |
| `Live` | `Long` | `0.7705` | 892,380.00 USD | 0.00 USD | 13,980.00 USD | `-11.81%` | `18,144.90` |
| `Live` | `Long` | `0.7715` | 878,400.00 USD | 0.00 USD | 338.38 USD | `-11.69%` | `438.60` |
| `Live` | `Long` | `0.7725` | 878,060.00 USD | 0.00 USD | 2,360.00 USD | `-11.58%` | `3,051.60` |
| `Live` | `Long` | `0.7735` | 875,710.00 USD | 0.00 USD | 4,570.00 USD | `-11.46%` | `5,912.10` |
| `Live` | `Long` | `0.7765` | 871,130.00 USD | 0.00 USD | 4,630.00 USD | `-11.12%` | `5,964.40` |
| `Live` | `Long` | `0.7785` | 866,500.00 USD | 0.00 USD | 7,000.00 USD | `-10.89%` | `8,985.30` |
| `Live` | `Long` | `0.7795` | 859,510.00 USD | 0.00 USD | 338.69 USD | `-10.78%` | `434.50` |
| `Live` | `Long` | `0.7815` | 859,170.00 USD | 0.00 USD | 4,160.00 USD | `-10.55%` | `5,325.20` |
| `Live` | `Long` | `0.7835` | 855,010.00 USD | 0.00 USD | 1,060.00 USD | `-10.32%` | `1,349.40` |
| `Live` | `Long` | `0.7855` | 853,950.00 USD | 0.00 USD | 3,020.00 USD | `-10.09%` | `3,840.20` |
| `Live` | `Long` | `0.7865` | 850,930.00 USD | 0.00 USD | 2,870.00 USD | `-9.98%` | `3,651.90` |
| `Live` | `Long` | `0.7875` | 848,060.00 USD | 0.00 USD | 15,190.00 USD | `-9.86%` | `19,293.30` |
| `Live` | `Long` | `0.7895` | 832,870.00 USD | 0.00 USD | 44,370.00 USD | `-9.63%` | `56,205.30` |
| `Live` | `Long` | `0.7905` | 788,490.00 USD | 0.00 USD | 3,670.00 USD | `-9.52%` | `4,637.40` |
| `Live` | `Long` | `0.7915` | 784,830.00 USD | 0.00 USD | 1,290.00 USD | `-9.40%` | `1,623.50` |
| `Live` | `Long` | `0.7925` | 783,540.00 USD | 0.00 USD | 385.87 USD | `-9.29%` | `486.90` |
| `Live` | `Long` | `0.7945` | 783,160.00 USD | 0.00 USD | 9,190.00 USD | `-9.06%` | `11,570.20` |
| `Live` | `Long` | `0.7955` | 773,960.00 USD | 0.00 USD | 23,720.00 USD | `-8.95%` | `29,814.10` |
| `Live` | `Long` | `0.7975` | 750,250.00 USD | 0.00 USD | 1,170.00 USD | `-8.72%` | `1,464.30` |
| `Live` | `Long` | `0.7985` | 749,080.00 USD | 0.00 USD | 1,840.00 USD | `-8.60%` | `2,300.00` |
| `Live` | `Long` | `0.7995` | 747,240.00 USD | 0.00 USD | 2,580.00 USD | `-8.49%` | `3,228.10` |
| `Live` | `Long` | `0.8005` | 744,660.00 USD | 0.00 USD | 635.04 USD | `-8.37%` | `793.30` |
| `Live` | `Long` | `0.8015` | 744,030.00 USD | 0.00 USD | 6,810.00 USD | `-8.26%` | `8,499.50` |
| `Live` | `Long` | `0.8035` | 737,210.00 USD | 0.00 USD | 316.42 USD | `-8.03%` | `393.80` |
| `Live` | `Long` | `0.8045` | 736,900.00 USD | 0.00 USD | 41,410.00 USD | `-7.92%` | `51,472.10` |
| `Live` | `Long` | `0.8055` | 695,490.00 USD | 0.00 USD | 1,610.00 USD | `-7.80%` | `2,000.00` |
| `Live` | `Long` | `0.8075` | 693,880.00 USD | 0.00 USD | 1,220.00 USD | `-7.57%` | `1,515.40` |
| `Live` | `Long` | `0.8085` | 692,650.00 USD | 0.00 USD | 22,460.00 USD | `-7.46%` | `27,784.20` |
| `Live` | `Long` | `0.8105` | 670,190.00 USD | 0.00 USD | 2,250.00 USD | `-7.23%` | `2,779.70` |
| `Live` | `Long` | `0.8115` | 667,940.00 USD | 0.00 USD | 3,050.00 USD | `-7.11%` | `3,753.20` |
| `Live` | `Long` | `0.8125` | 664,890.00 USD | 0.00 USD | 2,480.00 USD | `-7.00%` | `3,054.20` |
| `Live` | `Long` | `0.8135` | 662,410.00 USD | 0.00 USD | 11,260.00 USD | `-6.88%` | `13,843.50` |
| `Live` | `Long` | `0.8145` | 651,150.00 USD | 0.00 USD | 277.42 USD | `-6.77%` | `340.60` |
| `Live` | `Long` | `0.8155` | 650,870.00 USD | 0.00 USD | 8,160.00 USD | `-6.66%` | `10,000.00` |
| `Live` | `Long` | `0.8165` | 642,720.00 USD | 0.00 USD | 1,440.00 USD | `-6.54%` | `1,758.20` |
| `Live` | `Long` | `0.8175` | 641,280.00 USD | 0.00 USD | 103,450.00 USD | `-6.43%` | `126,546.30` |
| `Live` | `Long` | `0.8185` | 537,830.00 USD | 0.00 USD | 2,070.00 USD | `-6.31%` | `2,529.70` |
| `Live` | `Long` | `0.8195` | 535,760.00 USD | 0.00 USD | 29,980.00 USD | `-6.20%` | `36,587.30` |
| `Live` | `Long` | `0.8205` | 505,770.00 USD | 0.00 USD | 2,280.00 USD | `-6.08%` | `2,781.50` |
| `Live` | `Long` | `0.8215` | 503,490.00 USD | 0.00 USD | 6,900.00 USD | `-5.97%` | `8,399.30` |
| `Live` | `Long` | `0.8225` | 496,590.00 USD | 0.00 USD | 2,570.00 USD | `-5.85%` | `3,128.70` |
| `Live` | `Long` | `0.8235` | 494,020.00 USD | 0.00 USD | 216.00 USD | `-5.74%` | `262.30` |
| `Live` | `Long` | `0.8245` | 493,800.00 USD | 0.00 USD | 1,140.00 USD | `-5.63%` | `1,388.70` |
| `Live` | `Long` | `0.8255` | 492,660.00 USD | 0.00 USD | 4,550.00 USD | `-5.51%` | `5,515.80` |
| `Live` | `Long` | `0.8275` | 488,100.00 USD | 0.00 USD | 11,410.00 USD | `-5.28%` | `13,785.20` |
| `Live` | `Long` | `0.8285` | 476,700.00 USD | 0.00 USD | 126,740.00 USD | `-5.17%` | `152,975.80` |
| `Live` | `Long` | `0.8295` | 349,960.00 USD | 0.00 USD | 32,530.00 USD | `-5.05%` | `39,217.20` |
| `Live` | `Long` | `0.8305` | 317,430.00 USD | 0.00 USD | 1,880.00 USD | `-4.94%` | `2,268.50` |
| `Live` | `Long` | `0.8325` | 315,540.00 USD | 0.00 USD | 20,930.00 USD | `-4.71%` | `25,145.00` |
| `Live` | `Long` | `0.8335` | 294,610.00 USD | 0.00 USD | 234.71 USD | `-4.60%` | `281.60` |
| `Live` | `Long` | `0.8355` | 294,370.00 USD | 0.00 USD | 17,770.00 USD | `-4.37%` | `21,269.40` |
| `Live` | `Long` | `0.8375` | 276,600.00 USD | 0.00 USD | 2,420.00 USD | `-4.14%` | `2,888.90` |
| `Live` | `Long` | `0.8385` | 274,180.00 USD | 0.00 USD | 75,120.00 USD | `-4.02%` | `89,586.40` |
| `Live` | `Long` | `0.8395` | 199,070.00 USD | 0.00 USD | 26,770.00 USD | `-3.91%` | `31,885.00` |
| `Live` | `Long` | `0.8405` | 172,300.00 USD | 0.00 USD | 1,320.00 USD | `-3.79%` | `1,571.70` |
| `Live` | `Long` | `0.8415` | 170,980.00 USD | 0.00 USD | 48,540.00 USD | `-3.68%` | `57,683.50` |
| `Live` | `Long` | `0.8425` | 122,440.00 USD | 0.00 USD | 2,230.00 USD | `-3.57%` | `2,645.50` |
| `Live` | `Long` | `0.8435` | 120,210.00 USD | 0.00 USD | 6,280.00 USD | `-3.45%` | `7,446.40` |
| `Live` | `Long` | `0.8445` | 113,930.00 USD | 0.00 USD | 133.18 USD | `-3.34%` | `157.70` |
| `Live` | `Long` | `0.8455` | 113,790.00 USD | 0.00 USD | 6,340.00 USD | `-3.22%` | `7,494.00` |
| `Live` | `Long` | `0.8465` | 107,460.00 USD | 0.00 USD | 15,830.00 USD | `-3.11%` | `18,696.70` |
| `Live` | `Long` | `0.8475` | 91,630.00 USD | 0.00 USD | 28,990.00 USD | `-2.99%` | `34,202.20` |
| `Live` | `Long` | `0.8485` | 62,640.00 USD | 0.00 USD | 1,890.00 USD | `-2.88%` | `2,222.00` |
| `Live` | `Long` | `0.8495` | 60,760.00 USD | 0.00 USD | 5,290.00 USD | `-2.76%` | `6,230.00` |
| `Live` | `Long` | `0.8505` | 55,470.00 USD | 0.00 USD | 958.26 USD | `-2.65%` | `1,126.70` |
| `Live` | `Long` | `0.8515` | 54,510.00 USD | 0.00 USD | 1,220.00 USD | `-2.54%` | `1,433.90` |
| `Live` | `Long` | `0.8535` | 53,290.00 USD | 0.00 USD | 15,640.00 USD | `-2.31%` | `18,326.40` |
| `Live` | `Long` | `0.8555` | 37,650.00 USD | 0.00 USD | 17,220.00 USD | `-2.08%` | `20,123.80` |
| `Live` | `Long` | `0.8565` | 20,430.00 USD | 0.00 USD | 15,610.00 USD | `-1.96%` | `18,227.90` |
| `Live` | `Long` | `0.8585` | 4,820.00 USD | 0.00 USD | 2,200.00 USD | `-1.73%` | `2,567.10` |
| `Live` | `Long` | `0.8595` | 2,610.00 USD | 0.00 USD | 1,550.00 USD | `-1.62%` | `1,803.60` |
| `Live` | `Long` | `0.8685` | 1,060.00 USD | 0.00 USD | 265.76 USD | `-0.59%` | `306.00` |
| `Live` | `Long` | `0.8695` | 798.46 USD | 0.00 USD | 798.46 USD | `-0.48%` | `918.30` |
| `Live` | `Short` | `0.8935` | 3,590.00 USD | 3,590.00 USD | 0.00 USD | `+2.27%` | `4,019.80` |
| `Live` | `Short` | `0.9025` | 4,410.00 USD | 818.48 USD | 0.00 USD | `+3.30%` | `906.90` |
| `Live` | `Short` | `0.9035` | 13,450.00 USD | 9,040.00 USD | 0.00 USD | `+3.42%` | `10,000.00` |
| `Live` | `Short` | `0.9045` | 13,640.00 USD | 191.39 USD | 0.00 USD | `+3.53%` | `211.60` |
| `Live` | `Short` | `0.9055` | 75,210.00 USD | 61,580.00 USD | 0.00 USD | `+3.65%` | `68,002.30` |
| `Live` | `Short` | `0.9075` | 75,930.00 USD | 717.74 USD | 0.00 USD | `+3.87%` | `790.90` |
| `Live` | `Short` | `0.9155` | 76,080.00 USD | 150.14 USD | 0.00 USD | `+4.79%` | `164.00` |
| `Live` | `Short` | `0.9195` | 112,220.00 USD | 36,140.00 USD | 0.00 USD | `+5.25%` | `39,300.80` |
| `Live` | `Short` | `0.9205` | 125,190.00 USD | 12,970.00 USD | 0.00 USD | `+5.36%` | `14,093.60` |
| `Live` | `Short` | `0.9215` | 127,280.00 USD | 2,090.00 USD | 0.00 USD | `+5.48%` | `2,265.40` |
| `Live` | `Short` | `0.9235` | 127,510.00 USD | 234.48 USD | 0.00 USD | `+5.71%` | `253.90` |
| `Live` | `Short` | `0.9245` | 131,900.00 USD | 4,390.00 USD | 0.00 USD | `+5.82%` | `4,744.30` |
| `Live` | `Short` | `0.9255` | 141,770.00 USD | 9,870.00 USD | 0.00 USD | `+5.93%` | `10,668.20` |
| `Live` | `Short` | `0.9265` | 149,040.00 USD | 7,270.00 USD | 0.00 USD | `+6.05%` | `7,843.80` |
| `Live` | `Short` | `0.9275` | 180,150.00 USD | 31,110.00 USD | 0.00 USD | `+6.16%` | `33,540.90` |
| `Live` | `Short` | `0.9285` | 181,500.00 USD | 1,360.00 USD | 0.00 USD | `+6.28%` | `1,460.00` |
| `Live` | `Short` | `0.9295` | 244,070.00 USD | 62,570.00 USD | 0.00 USD | `+6.39%` | `67,316.00` |
| `Live` | `Short` | `0.9305` | 247,900.00 USD | 3,830.00 USD | 0.00 USD | `+6.51%` | `4,111.50` |
| `Live` | `Short` | `0.9335` | 248,020.00 USD | 116.31 USD | 0.00 USD | `+6.85%` | `124.60` |
| `Live` | `Short` | `0.9345` | 250,120.00 USD | 2,100.00 USD | 0.00 USD | `+6.97%` | `2,252.30` |
| `Live` | `Short` | `0.9365` | 251,870.00 USD | 1,750.00 USD | 0.00 USD | `+7.19%` | `1,866.80` |
| `Live` | `Short` | `0.9675` | 255,030.00 USD | 3,160.00 USD | 0.00 USD | `+10.74%` | `3,266.70` |
| `Live` | `Short` | `0.9705` | 320,090.00 USD | 65,060.00 USD | 0.00 USD | `+11.09%` | `67,040.50` |
| `Live` | `Short` | `0.9765` | 320,310.00 USD | 214.44 USD | 0.00 USD | `+11.77%` | `219.60` |
| `Live` | `Short` | `0.9775` | 320,410.00 USD | 100.88 USD | 0.00 USD | `+11.89%` | `103.20` |
| `Live` | `Short` | `0.9805` | 321,460.00 USD | 1,050.00 USD | 0.00 USD | `+12.23%` | `1,068.70` |
| `Live` | `Short` | `0.9845` | 331,900.00 USD | 10,440.00 USD | 0.00 USD | `+12.69%` | `10,608.60` |
| `Live` | `Short` | `0.9875` | 332,630.00 USD | 732.03 USD | 0.00 USD | `+13.03%` | `741.30` |
| `Live` | `Short` | `0.9885` | 337,560.00 USD | 4,930.00 USD | 0.00 USD | `+13.15%` | `4,982.50` |
| `Live` | `Short` | `0.9905` | 339,130.00 USD | 1,570.00 USD | 0.00 USD | `+13.37%` | `1,586.00` |
| `Live` | `Short` | `0.9925` | 341,540.00 USD | 2,420.00 USD | 0.00 USD | `+13.60%` | `2,434.50` |
| `Live` | `Short` | `0.9965` | 341,670.00 USD | 125.66 USD | 0.00 USD | `+14.06%` | `126.10` |
| `Live` | `Short` | `1.02` | 341,840.00 USD | 170.40 USD | 0.00 USD | `+16.24%` | `167.80` |
| `Live` | `Short` | `1.04` | 342,000.00 USD | 155.92 USD | 0.00 USD | `+18.98%` | `150.00` |
| `Live` | `Short` | `1.04` | 342,140.00 USD | 139.22 USD | 0.00 USD | `+19.10%` | `133.80` |
| `Live` | `Short` | `1.05` | 342,730.00 USD | 597.52 USD | 0.00 USD | `+20.24%` | `568.80` |
| `Live` | `Short` | `1.05` | 345,120.00 USD | 2,390.00 USD | 0.00 USD | `+20.36%` | `2,272.10` |
| `Live` | `Short` | `1.05` | 345,440.00 USD | 317.52 USD | 0.00 USD | `+20.59%` | `301.40` |
| `Live` | `Short` | `1.06` | 345,660.00 USD | 217.64 USD | 0.00 USD | `+20.81%` | `206.20` |
| `Live` | `Short` | `1.08` | 349,350.00 USD | 3,690.00 USD | 0.00 USD | `+23.22%` | `3,432.40` |
| `Live` | `Short` | `1.08` | 355,050.00 USD | 5,700.00 USD | 0.00 USD | `+23.56%` | `5,278.70` |
| `Live` | `Short` | `1.08` | 358,630.00 USD | 3,580.00 USD | 0.00 USD | `+23.68%` | `3,315.70` |
| `Live` | `Short` | `1.08` | 358,800.00 USD | 166.43 USD | 0.00 USD | `+24.02%` | `153.60` |
| `Live` | `Short` | `1.09` | 364,350.00 USD | 5,550.00 USD | 0.00 USD | `+24.71%` | `5,095.60` |
| `Live` | `Short` | `1.10` | 364,680.00 USD | 324.90 USD | 0.00 USD | `+25.85%` | `295.50` |
| `Live` | `Short` | `1.10` | 364,950.00 USD | 277.22 USD | 0.00 USD | `+25.97%` | `251.90` |
| `Live` | `Short` | `1.13` | 388,260.00 USD | 23,310.00 USD | 0.00 USD | `+28.94%` | `20,691.10` |
| `Live` | `Short` | `1.18` | 393,320.00 USD | 5,060.00 USD | 0.00 USD | `+35.47%` | `4,273.60` |
| `Live` | `Short` | `1.20` | 394,770.00 USD | 1,450.00 USD | 0.00 USD | `+37.07%` | `1,213.60` |
| `Live` | `Short` | `1.20` | 395,030.00 USD | 253.69 USD | 0.00 USD | `+37.30%` | `211.50` |
| `Live` | `Short` | `1.21` | 395,170.00 USD | 147.43 USD | 0.00 USD | `+37.98%` | `122.30` |
| `Live` | `Short` | `1.22` | 399,620.00 USD | 4,440.00 USD | 0.00 USD | `+39.47%` | `3,646.70` |
| `Live` | `Short` | `1.23` | 400,000.00 USD | 380.84 USD | 0.00 USD | `+41.30%` | `308.50` |
| `Live` | `Short` | `1.25` | 402,850.00 USD | 2,850.00 USD | 0.00 USD | `+43.25%` | `2,278.20` |
| `Live` | `Short` | `1.26` | 405,520.00 USD | 2,670.00 USD | 0.00 USD | `+44.17%` | `2,118.80` |
| `Live` | `Short` | `1.28` | 407,820.00 USD | 2,300.00 USD | 0.00 USD | `+46.23%` | `1,804.00` |
| `Live` | `Short` | `1.28` | 447,710.00 USD | 39,880.00 USD | 0.00 USD | `+46.80%` | `31,097.50` |
| `Live` | `Short` | `1.29` | 447,930.00 USD | 226.80 USD | 0.00 USD | `+48.17%` | `175.20` |
| `Live` | `Short` | `1.30` | 448,050.00 USD | 114.40 USD | 0.00 USD | `+48.63%` | `88.10` |
| `Live` | `Short` | `1.30` | 449,120.00 USD | 1,070.00 USD | 0.00 USD | `+48.86%` | `826.40` |
| `Live` | `Short` | `1.30` | 449,760.00 USD | 635.85 USD | 0.00 USD | `+49.20%` | `487.80` |
| `Live` | `Short` | `1.31` | 459,700.00 USD | 9,950.00 USD | 0.00 USD | `+49.43%` | `7,618.00` |
| `Live` | `Short` | `1.31` | 460,720.00 USD | 1,020.00 USD | 0.00 USD | `+49.89%` | `777.20` |
| `Live` | `Short` | `1.31` | 492,250.00 USD | 31,530.00 USD | 0.00 USD | `+50.12%` | `24,042.40` |
| `Live` | `Short` | `1.33` | 498,590.00 USD | 6,340.00 USD | 0.00 USD | `+51.72%` | `4,781.30` |
| `Live` | `Short` | `1.33` | 520,560.00 USD | 21,970.00 USD | 0.00 USD | `+52.06%` | `16,535.70` |
| `Live` | `Short` | `1.33` | 520,920.00 USD | 358.30 USD | 0.00 USD | `+52.29%` | `269.30` |
| `Live` | `Short` | `1.33` | 522,440.00 USD | 1,520.00 USD | 0.00 USD | `+52.52%` | `1,143.40` |
| `Live` | `Short` | `1.34` | 524,630.00 USD | 2,190.00 USD | 0.00 USD | `+52.86%` | `1,639.00` |
| `Live` | `Short` | `1.34` | 531,490.00 USD | 6,860.00 USD | 0.00 USD | `+53.32%` | `5,119.30` |
| `Live` | `Short` | `1.34` | 552,890.00 USD | 21,400.00 USD | 0.00 USD | `+53.67%` | `15,941.90` |
| `Live` | `Short` | `1.37` | 911,170.00 USD | 358,280.00 USD | 0.00 USD | `+57.10%` | `261,043.60` |
| `Live` | `Short` | `1.41` | 915,620.00 USD | 4,450.00 USD | 0.00 USD | `+61.91%` | `3,142.60` |
| `Live` | `Short` | `1.44` | 916,020.00 USD | 402.08 USD | 0.00 USD | `+64.43%` | `279.90` |
| `Live` | `Short` | `1.44` | 916,310.00 USD | 288.68 USD | 0.00 USD | `+64.88%` | `200.40` |
| `Live` | `Short` | `1.50` | 926,070.00 USD | 9,760.00 USD | 0.00 USD | `+72.09%` | `6,491.20` |
| `Live` | `Short` | `1.51` | 930,090.00 USD | 4,020.00 USD | 0.00 USD | `+73.35%` | `2,654.10` |
| `Live` | `Short` | `1.54` | 930,230.00 USD | 144.34 USD | 0.00 USD | `+75.76%` | `94.00` |
| `Live` | `Short` | `1.58` | 930,360.00 USD | 133.21 USD | 0.00 USD | `+80.45%` | `84.50` |
| `Live` | `Short` | `1.58` | 948,290.00 USD | 17,930.00 USD | 0.00 USD | `+80.56%` | `11,363.40` |
| `Live` | `Short` | `1.60` | 957,870.00 USD | 9,580.00 USD | 0.00 USD | `+82.74%` | `6,000.00` |
| `Live` | `Short` | `1.65` | 979,200.00 USD | 21,330.00 USD | 0.00 USD | `+88.46%` | `12,957.30` |
| `Live` | `Short` | `1.66` | 1,020,000.00 USD | 36,530.00 USD | 0.00 USD | `+90.18%` | `21,988.10` |
| `Live` | `Short` | `1.66` | 1,050,000.00 USD | 39,140.00 USD | 0.00 USD | `+90.41%` | `23,529.40` |
| `Live` | `Short` | `1.68` | 1,060,000.00 USD | 2,280.00 USD | 0.00 USD | `+92.24%` | `1,360.10` |
| `Live` | `Short` | `1.69` | 1,060,000.00 USD | 440.71 USD | 0.00 USD | `+93.50%` | `260.70` |
| `Live` | `Short` | `1.69` | 1,350,000.00 USD | 292,630.00 USD | 0.00 USD | `+93.61%` | `173,000.00` |
| `Live` | `Short` | `1.70` | 1,350,000.00 USD | 167.09 USD | 0.00 USD | `+94.76%` | `98.20` |
| `Live` | `Short` | `1.71` | 1,350,000.00 USD | 205.67 USD | 0.00 USD | `+96.02%` | `120.10` |
| `Live` | `Short` | `1.72` | 1,360,000.00 USD | 9,700.00 USD | 0.00 USD | `+96.70%` | `5,645.40` |
| `Live` | `Short` | `1.73` | 1,360,000.00 USD | 226.05 USD | 0.00 USD | `+98.42%` | `130.40` |
| `Live` | `Short` | `1.74` | 1,360,000.00 USD | 560.67 USD | 0.00 USD | `+98.99%` | `322.50` |
| `Live` | `Short` | `1.74` | 1,360,000.00 USD | 2,080.00 USD | 0.00 USD | `+99.22%` | `1,197.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.2625` | 1,030,000.00 USD | 0.00 USD | 497.31 USD | `-69.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2745` | 1,030,000.00 USD | 0.00 USD | 455.97 USD | `-68.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3425` | 1,030,000.00 USD | 0.00 USD | 102.75 USD | `-60.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3505` | 1,030,000.00 USD | 0.00 USD | 256.78 USD | `-59.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3885` | 1,030,000.00 USD | 0.00 USD | 428.87 USD | `-55.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4115` | 1,030,000.00 USD | 0.00 USD | 123.45 USD | `-52.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4195` | 1,030,000.00 USD | 0.00 USD | 818.15 USD | `-51.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4285` | 1,030,000.00 USD | 0.00 USD | 454.04 USD | `-50.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4345` | 1,030,000.00 USD | 0.00 USD | 436.41 USD | `-50.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4355` | 1,030,000.00 USD | 0.00 USD | 876.79 USD | `-50.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4505` | 1,030,000.00 USD | 0.00 USD | 466.72 USD | `-48.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4765` | 1,030,000.00 USD | 0.00 USD | 142.95 USD | `-45.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 1,030,000.00 USD | 0.00 USD | 781.98 USD | `-42.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5135` | 1,030,000.00 USD | 0.00 USD | 151.74 USD | `-41.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5165` | 1,030,000.00 USD | 0.00 USD | 123.91 USD | `-40.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5495` | 1,030,000.00 USD | 0.00 USD | 219.80 USD | `-37.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5505` | 1,030,000.00 USD | 0.00 USD | 237,400.00 USD | `-36.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5535` | 790,990.00 USD | 0.00 USD | 276.75 USD | `-36.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5605` | 790,710.00 USD | 0.00 USD | 2,010.00 USD | `-35.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5805` | 788,700.00 USD | 0.00 USD | 119.76 USD | `-33.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5955` | 788,580.00 USD | 0.00 USD | 470.62 USD | `-31.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6005` | 788,110.00 USD | 0.00 USD | 108.39 USD | `-31.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6055` | 788,000.00 USD | 0.00 USD | 123.28 USD | `-30.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6205` | 787,880.00 USD | 0.00 USD | 488.52 USD | `-28.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6255` | 787,390.00 USD | 0.00 USD | 4,230.00 USD | `-28.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6305` | 783,160.00 USD | 0.00 USD | 242.24 USD | `-27.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6465` | 782,920.00 USD | 0.00 USD | 193.95 USD | `-26.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6475` | 782,720.00 USD | 0.00 USD | 647.50 USD | `-25.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6505` | 782,080.00 USD | 0.00 USD | 834.79 USD | `-25.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6535` | 781,240.00 USD | 0.00 USD | 158.54 USD | `-25.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6555` | 781,080.00 USD | 0.00 USD | 195.47 USD | `-24.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6615` | 780,890.00 USD | 0.00 USD | 190.25 USD | `-24.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6635` | 780,700.00 USD | 0.00 USD | 153.53 USD | `-24.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6705` | 780,540.00 USD | 0.00 USD | 52,450.00 USD | `-23.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6735` | 728,100.00 USD | 0.00 USD | 536.11 USD | `-22.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6805` | 727,560.00 USD | 0.00 USD | 3,600.00 USD | `-22.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6815` | 723,970.00 USD | 0.00 USD | 340.75 USD | `-21.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6905` | 723,620.00 USD | 0.00 USD | 9,270.00 USD | `-20.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6915` | 714,360.00 USD | 0.00 USD | 120.53 USD | `-20.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6945` | 714,240.00 USD | 0.00 USD | 160.71 USD | `-20.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6965` | 714,080.00 USD | 0.00 USD | 738.08 USD | `-20.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6995` | 713,340.00 USD | 0.00 USD | 187.61 USD | `-19.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7005` | 713,150.00 USD | 0.00 USD | 2,920.00 USD | `-19.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7015` | 710,230.00 USD | 0.00 USD | 89,150.00 USD | `-19.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7065` | 621,080.00 USD | 0.00 USD | 189.06 USD | `-19.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7075` | 620,890.00 USD | 0.00 USD | 5,650.00 USD | `-19.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7085` | 615,240.00 USD | 0.00 USD | 100.47 USD | `-18.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7105` | 615,140.00 USD | 0.00 USD | 152.05 USD | `-18.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7175` | 614,990.00 USD | 0.00 USD | 123.41 USD | `-17.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7275` | 614,870.00 USD | 0.00 USD | 745.54 USD | `-16.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7305` | 614,120.00 USD | 0.00 USD | 1,130.00 USD | `-16.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7315` | 612,990.00 USD | 0.00 USD | 18,770.00 USD | `-16.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7365` | 594,220.00 USD | 0.00 USD | 257.26 USD | `-15.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7435` | 593,960.00 USD | 0.00 USD | 1,590.00 USD | `-14.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7455` | 592,370.00 USD | 0.00 USD | 10,160.00 USD | `-14.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7505` | 582,210.00 USD | 0.00 USD | 93,810.00 USD | `-14.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7545` | 488,400.00 USD | 0.00 USD | 1,230.00 USD | `-13.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7585` | 487,170.00 USD | 0.00 USD | 1,840.00 USD | `-13.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7595` | 485,340.00 USD | 0.00 USD | 804.61 USD | `-13.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7645` | 484,530.00 USD | 0.00 USD | 191.12 USD | `-12.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7675` | 484,340.00 USD | 0.00 USD | 1,370.00 USD | `-12.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7725` | 482,970.00 USD | 0.00 USD | 125.92 USD | `-11.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7735` | 482,840.00 USD | 0.00 USD | 1,980.00 USD | `-11.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7745` | 480,870.00 USD | 0.00 USD | 1,150.00 USD | `-11.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7755` | 479,720.00 USD | 0.00 USD | 174.80 USD | `-11.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7795` | 479,550.00 USD | 0.00 USD | 6,800.00 USD | `-10.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7805` | 472,750.00 USD | 0.00 USD | 128.47 USD | `-10.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7835` | 472,620.00 USD | 0.00 USD | 10,090.00 USD | `-10.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7855` | 462,530.00 USD | 0.00 USD | 135.11 USD | `-10.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7865` | 462,390.00 USD | 0.00 USD | 8,870.00 USD | `-9.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7905` | 453,530.00 USD | 0.00 USD | 1,500.00 USD | `-9.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7945` | 452,030.00 USD | 0.00 USD | 25,170.00 USD | `-9.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7955` | 426,860.00 USD | 0.00 USD | 103.42 USD | `-8.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7965` | 426,750.00 USD | 0.00 USD | 1,260.00 USD | `-8.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8005` | 425,490.00 USD | 0.00 USD | 4,470.00 USD | `-8.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8015` | 421,020.00 USD | 0.00 USD | 144.67 USD | `-8.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8055` | 420,870.00 USD | 0.00 USD | 50,540.00 USD | `-7.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8075` | 370,340.00 USD | 0.00 USD | 263.25 USD | `-7.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8085` | 370,080.00 USD | 0.00 USD | 16,870.00 USD | `-7.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8105` | 353,210.00 USD | 0.00 USD | 91,080.00 USD | `-7.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8115` | 262,130.00 USD | 0.00 USD | 174.63 USD | `-7.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8165` | 261,960.00 USD | 0.00 USD | 13,470.00 USD | `-6.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8185` | 248,490.00 USD | 0.00 USD | 125.72 USD | `-6.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8195` | 248,360.00 USD | 0.00 USD | 4,860.00 USD | `-6.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8205` | 243,500.00 USD | 0.00 USD | 19,320.00 USD | `-6.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8225` | 224,180.00 USD | 0.00 USD | 7,160.00 USD | `-5.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8235` | 217,030.00 USD | 0.00 USD | 226.71 USD | `-5.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8245` | 216,800.00 USD | 0.00 USD | 922.29 USD | `-5.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8255` | 215,880.00 USD | 0.00 USD | 1,120.00 USD | `-5.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8265` | 214,760.00 USD | 0.00 USD | 325.56 USD | `-5.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8295` | 214,430.00 USD | 0.00 USD | 577.25 USD | `-5.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8305` | 213,860.00 USD | 0.00 USD | 5,760.00 USD | `-4.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8315` | 208,100.00 USD | 0.00 USD | 171.46 USD | `-4.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8335` | 207,930.00 USD | 0.00 USD | 1,270.00 USD | `-4.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8345` | 206,650.00 USD | 0.00 USD | 4,170.00 USD | `-4.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8365` | 202,480.00 USD | 0.00 USD | 610.23 USD | `-4.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8375` | 201,870.00 USD | 0.00 USD | 699.65 USD | `-4.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8385` | 201,170.00 USD | 0.00 USD | 320.31 USD | `-4.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8405` | 200,850.00 USD | 0.00 USD | 61,340.00 USD | `-3.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8435` | 139,510.00 USD | 0.00 USD | 221.25 USD | `-3.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8445` | 139,280.00 USD | 0.00 USD | 212.81 USD | `-3.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8455` | 139,070.00 USD | 0.00 USD | 462.49 USD | `-3.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8475` | 138,610.00 USD | 0.00 USD | 481.80 USD | `-2.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8505` | 138,130.00 USD | 0.00 USD | 17,180.00 USD | `-2.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8515` | 120,950.00 USD | 0.00 USD | 901.40 USD | `-2.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8545` | 120,040.00 USD | 0.00 USD | 345.13 USD | `-2.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8555` | 119,700.00 USD | 0.00 USD | 20,920.00 USD | `-2.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8565` | 98,780.00 USD | 0.00 USD | 3,640.00 USD | `-1.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8575` | 95,130.00 USD | 0.00 USD | 108.13 USD | `-1.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8595` | 95,030.00 USD | 0.00 USD | 7,800.00 USD | `-1.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8605` | 87,230.00 USD | 0.00 USD | 8,740.00 USD | `-1.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8615` | 78,490.00 USD | 0.00 USD | 202.45 USD | `-1.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8635` | 78,290.00 USD | 0.00 USD | 921.70 USD | `-1.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8655` | 77,360.00 USD | 0.00 USD | 1,270.00 USD | `-0.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8675` | 76,090.00 USD | 0.00 USD | 741.45 USD | `-0.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8685` | 75,350.00 USD | 0.00 USD | 168.75 USD | `-0.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8695` | 75,180.00 USD | 0.00 USD | 2,990.00 USD | `-0.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8705` | 72,190.00 USD | 0.00 USD | 12,700.00 USD | `-0.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8715` | 59,490.00 USD | 0.00 USD | 712.45 USD | `-0.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8725` | 58,770.00 USD | 0.00 USD | 58,490.00 USD | `-0.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8735` | 281.70 USD | 0.00 USD | 281.70 USD | `-0.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8745` | 133.10 USD | 133.10 USD | 0.00 USD | `+0.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8755` | 380.08 USD | 246.98 USD | 0.00 USD | `+0.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8775` | 9,450.00 USD | 9,070.00 USD | 0.00 USD | `+0.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8785` | 9,600.00 USD | 151.10 USD | 0.00 USD | `+0.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8795` | 10,100.00 USD | 507.74 USD | 0.00 USD | `+0.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8805` | 18,470.00 USD | 8,370.00 USD | 0.00 USD | `+0.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8815` | 22,540.00 USD | 4,070.00 USD | 0.00 USD | `+0.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8825` | 27,560.00 USD | 5,020.00 USD | 0.00 USD | `+1.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8835` | 37,330.00 USD | 9,770.00 USD | 0.00 USD | `+1.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8855` | 40,990.00 USD | 3,660.00 USD | 0.00 USD | `+1.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8865` | 54,440.00 USD | 13,450.00 USD | 0.00 USD | `+1.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8875` | 58,050.00 USD | 3,620.00 USD | 0.00 USD | `+1.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8885` | 69,410.00 USD | 11,360.00 USD | 0.00 USD | `+1.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8895` | 78,190.00 USD | 8,780.00 USD | 0.00 USD | `+1.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8905` | 88,540.00 USD | 10,340.00 USD | 0.00 USD | `+1.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8915` | 89,010.00 USD | 469.91 USD | 0.00 USD | `+2.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8925` | 99,620.00 USD | 10,610.00 USD | 0.00 USD | `+2.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8935` | 106,710.00 USD | 7,100.00 USD | 0.00 USD | `+2.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8945` | 109,640.00 USD | 2,920.00 USD | 0.00 USD | `+2.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8955` | 113,530.00 USD | 3,900.00 USD | 0.00 USD | `+2.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8965` | 113,820.00 USD | 289.12 USD | 0.00 USD | `+2.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8975` | 132,030.00 USD | 18,210.00 USD | 0.00 USD | `+2.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8985` | 134,750.00 USD | 2,710.00 USD | 0.00 USD | `+2.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8995` | 163,710.00 USD | 28,960.00 USD | 0.00 USD | `+2.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9005` | 167,570.00 USD | 3,860.00 USD | 0.00 USD | `+3.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9015` | 169,630.00 USD | 2,050.00 USD | 0.00 USD | `+3.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9025` | 170,550.00 USD | 926.06 USD | 0.00 USD | `+3.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9035` | 171,360.00 USD | 805.29 USD | 0.00 USD | `+3.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9045` | 172,500.00 USD | 1,140.00 USD | 0.00 USD | `+3.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9055` | 174,490.00 USD | 1,990.00 USD | 0.00 USD | `+3.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9065` | 196,940.00 USD | 22,450.00 USD | 0.00 USD | `+3.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9075` | 197,190.00 USD | 250.83 USD | 0.00 USD | `+3.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9085` | 198,290.00 USD | 1,090.00 USD | 0.00 USD | `+3.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9095` | 199,810.00 USD | 1,520.00 USD | 0.00 USD | `+4.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9105` | 200,740.00 USD | 933.08 USD | 0.00 USD | `+4.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9115` | 202,950.00 USD | 2,210.00 USD | 0.00 USD | `+4.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9125` | 217,720.00 USD | 14,760.00 USD | 0.00 USD | `+4.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9135` | 220,740.00 USD | 3,020.00 USD | 0.00 USD | `+4.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9145` | 221,060.00 USD | 318.79 USD | 0.00 USD | `+4.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9155` | 226,130.00 USD | 5,070.00 USD | 0.00 USD | `+4.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9165` | 231,170.00 USD | 5,040.00 USD | 0.00 USD | `+4.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9175` | 235,070.00 USD | 3,900.00 USD | 0.00 USD | `+5.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9185` | 237,040.00 USD | 1,970.00 USD | 0.00 USD | `+5.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9195` | 237,160.00 USD | 116.59 USD | 0.00 USD | `+5.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9205` | 496,270.00 USD | 259,120.00 USD | 0.00 USD | `+5.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9215` | 648,240.00 USD | 151,960.00 USD | 0.00 USD | `+5.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9225` | 653,310.00 USD | 5,070.00 USD | 0.00 USD | `+5.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9235` | 779,660.00 USD | 126,350.00 USD | 0.00 USD | `+5.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9245` | 781,060.00 USD | 1,400.00 USD | 0.00 USD | `+5.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9255` | 785,640.00 USD | 4,580.00 USD | 0.00 USD | `+5.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9265` | 788,420.00 USD | 2,780.00 USD | 0.00 USD | `+6.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9275` | 788,700.00 USD | 287.62 USD | 0.00 USD | `+6.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9285` | 788,900.00 USD | 195.17 USD | 0.00 USD | `+6.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9295` | 789,000.00 USD | 103.17 USD | 0.00 USD | `+6.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9305` | 792,200.00 USD | 3,190.00 USD | 0.00 USD | `+6.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9315` | 792,350.00 USD | 148.85 USD | 0.00 USD | `+6.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9325` | 792,450.00 USD | 100.90 USD | 0.00 USD | `+6.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9335` | 793,430.00 USD | 979.71 USD | 0.00 USD | `+6.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9345` | 796,130.00 USD | 2,700.00 USD | 0.00 USD | `+6.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9355` | 800,010.00 USD | 3,880.00 USD | 0.00 USD | `+7.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9365` | 800,710.00 USD | 701.16 USD | 0.00 USD | `+7.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9375` | 802,580.00 USD | 1,880.00 USD | 0.00 USD | `+7.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9385` | 855,640.00 USD | 53,060.00 USD | 0.00 USD | `+7.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9395` | 859,550.00 USD | 3,910.00 USD | 0.00 USD | `+7.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9405` | 868,510.00 USD | 8,960.00 USD | 0.00 USD | `+7.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9415` | 868,670.00 USD | 158.55 USD | 0.00 USD | `+7.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9425` | 870,560.00 USD | 1,890.00 USD | 0.00 USD | `+7.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9435` | 872,260.00 USD | 1,700.00 USD | 0.00 USD | `+8.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9445` | 873,050.00 USD | 789.04 USD | 0.00 USD | `+8.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9455` | 873,170.00 USD | 117.81 USD | 0.00 USD | `+8.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9465` | 874,220.00 USD | 1,050.00 USD | 0.00 USD | `+8.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9475` | 880,220.00 USD | 6,000.00 USD | 0.00 USD | `+8.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9495` | 880,490.00 USD | 261.97 USD | 0.00 USD | `+8.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9505` | 880,750.00 USD | 265.66 USD | 0.00 USD | `+8.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9535` | 890,660.00 USD | 9,910.00 USD | 0.00 USD | `+9.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9545` | 893,810.00 USD | 3,150.00 USD | 0.00 USD | `+9.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9555` | 895,240.00 USD | 1,440.00 USD | 0.00 USD | `+9.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9565` | 898,130.00 USD | 2,890.00 USD | 0.00 USD | `+9.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9575` | 905,730.00 USD | 7,600.00 USD | 0.00 USD | `+9.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9585` | 905,850.00 USD | 121.54 USD | 0.00 USD | `+9.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9595` | 905,950.00 USD | 100.17 USD | 0.00 USD | `+9.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9605` | 906,200.00 USD | 245.02 USD | 0.00 USD | `+9.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9615` | 906,360.00 USD | 161.82 USD | 0.00 USD | `+10.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9625` | 906,830.00 USD | 469.51 USD | 0.00 USD | `+10.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9635` | 906,970.00 USD | 139.23 USD | 0.00 USD | `+10.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9645` | 908,310.00 USD | 1,340.00 USD | 0.00 USD | `+10.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9655` | 908,510.00 USD | 204.20 USD | 0.00 USD | `+10.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9665` | 909,040.00 USD | 531.57 USD | 0.00 USD | `+10.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9675` | 912,200.00 USD | 3,160.00 USD | 0.00 USD | `+10.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9685` | 913,200.00 USD | 993.78 USD | 0.00 USD | `+10.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9695` | 913,410.00 USD | 212.90 USD | 0.00 USD | `+10.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9705` | 925,090.00 USD | 11,680.00 USD | 0.00 USD | `+11.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9715` | 925,210.00 USD | 125.61 USD | 0.00 USD | `+11.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9725` | 925,650.00 USD | 441.51 USD | 0.00 USD | `+11.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9735` | 936,130.00 USD | 10,480.00 USD | 0.00 USD | `+11.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9755` | 936,380.00 USD | 253.14 USD | 0.00 USD | `+11.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9765` | 936,630.00 USD | 244.81 USD | 0.00 USD | `+11.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9775` | 936,800.00 USD | 176.73 USD | 0.00 USD | `+11.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9785` | 937,010.00 USD | 201.77 USD | 0.00 USD | `+12.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9795` | 937,300.00 USD | 295.22 USD | 0.00 USD | `+12.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9805` | 970,540.00 USD | 33,240.00 USD | 0.00 USD | `+12.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9815` | 976,010.00 USD | 5,470.00 USD | 0.00 USD | `+12.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9825` | 976,570.00 USD | 558.35 USD | 0.00 USD | `+12.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9845` | 977,630.00 USD | 1,060.00 USD | 0.00 USD | `+12.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9855` | 978,870.00 USD | 1,240.00 USD | 0.00 USD | `+12.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9875` | 979,360.00 USD | 490.99 USD | 0.00 USD | `+13.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9905` | 980,130.00 USD | 769.72 USD | 0.00 USD | `+13.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9915` | 981,120.00 USD | 991.50 USD | 0.00 USD | `+13.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9925` | 991,450.00 USD | 10,340.00 USD | 0.00 USD | `+13.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9945` | 991,740.00 USD | 284.92 USD | 0.00 USD | `+13.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9955` | 992,020.00 USD | 277.64 USD | 0.00 USD | `+13.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9965` | 992,370.00 USD | 350.37 USD | 0.00 USD | `+14.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9975` | 992,510.00 USD | 144.04 USD | 0.00 USD | `+14.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9985` | 992,620.00 USD | 105.44 USD | 0.00 USD | `+14.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9995` | 1,000,000.00 USD | 8,760.00 USD | 0.00 USD | `+14.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 1,000,000.00 USD | 1,570.00 USD | 0.00 USD | `+14.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 1,010,000.00 USD | 2,180.00 USD | 0.00 USD | `+14.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 1,010,000.00 USD | 363.87 USD | 0.00 USD | `+14.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 1,010,000.00 USD | 589.52 USD | 0.00 USD | `+15.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 1,010,000.00 USD | 110.62 USD | 0.00 USD | `+15.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 1,020,000.00 USD | 10,090.00 USD | 0.00 USD | `+15.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 1,020,000.00 USD | 5,420.00 USD | 0.00 USD | `+15.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 1,020,000.00 USD | 1,960.00 USD | 0.00 USD | `+15.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 1,020,000.00 USD | 248.49 USD | 0.00 USD | `+16.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 1,060,000.00 USD | 33,450.00 USD | 0.00 USD | `+16.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 1,060,000.00 USD | 722.63 USD | 0.00 USD | `+16.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 1,060,000.00 USD | 312.07 USD | 0.00 USD | `+16.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 1,060,000.00 USD | 171.24 USD | 0.00 USD | `+16.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 1,060,000.00 USD | 561.11 USD | 0.00 USD | `+16.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 1,060,000.00 USD | 249.30 USD | 0.00 USD | `+17.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 1,060,000.00 USD | 2,210.00 USD | 0.00 USD | `+17.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 1,060,000.00 USD | 432.18 USD | 0.00 USD | `+17.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 1,060,000.00 USD | 137.88 USD | 0.00 USD | `+17.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 1,060,000.00 USD | 2,470.00 USD | 0.00 USD | `+18.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 1,060,000.00 USD | 160.60 USD | 0.00 USD | `+18.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 1,070,000.00 USD | 6,560.00 USD | 0.00 USD | `+19.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 1,070,000.00 USD | 2,920.00 USD | 0.00 USD | `+19.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 1,080,000.00 USD | 7,680.00 USD | 0.00 USD | `+19.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 1,080,000.00 USD | 224.56 USD | 0.00 USD | `+19.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 1,090,000.00 USD | 3,570.00 USD | 0.00 USD | `+19.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 1,090,000.00 USD | 5,610.00 USD | 0.00 USD | `+20.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,810,000.00 USD | 1,720,000.00 USD | 0.00 USD | `+20.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,820,000.00 USD | 1,810.00 USD | 0.00 USD | `+20.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,820,000.00 USD | 248.20 USD | 0.00 USD | `+21.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,820,000.00 USD | 5,390.00 USD | 0.00 USD | `+21.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,820,000.00 USD | 285.32 USD | 0.00 USD | `+21.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,820,000.00 USD | 1,130.00 USD | 0.00 USD | `+21.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,820,000.00 USD | 1,240.00 USD | 0.00 USD | `+21.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,820,000.00 USD | 278.06 USD | 0.00 USD | `+21.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,830,000.00 USD | 309.00 USD | 0.00 USD | `+21.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,830,000.00 USD | 272.12 USD | 0.00 USD | `+22.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,830,000.00 USD | 117.12 USD | 0.00 USD | `+22.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,970,000.00 USD | 140,120.00 USD | 0.00 USD | `+22.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,970,000.00 USD | 530.01 USD | 0.00 USD | `+23.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,970,000.00 USD | 128.23 USD | 0.00 USD | `+23.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 3,070,000.00 USD | 108,190.00 USD | 0.00 USD | `+23.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 3,080,000.00 USD | 550.49 USD | 0.00 USD | `+24.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 3,080,000.00 USD | 5,810.00 USD | 0.00 USD | `+24.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 3,090,000.00 USD | 5,570.00 USD | 0.00 USD | `+24.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 3,090,000.00 USD | 1,290.00 USD | 0.00 USD | `+24.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 3,090,000.00 USD | 294.81 USD | 0.00 USD | `+25.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 3,090,000.00 USD | 123.13 USD | 0.00 USD | `+25.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 3,090,000.00 USD | 494.98 USD | 0.00 USD | `+25.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 3,090,000.00 USD | 613.52 USD | 0.00 USD | `+25.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 3,200,000.00 USD | 115,100.00 USD | 0.00 USD | `+25.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 3,200,000.00 USD | 409.76 USD | 0.00 USD | `+26.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 3,200,000.00 USD | 162.77 USD | 0.00 USD | `+26.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 3,210,000.00 USD | 959.70 USD | 0.00 USD | `+26.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 3,210,000.00 USD | 160.18 USD | 0.00 USD | `+26.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 3,210,000.00 USD | 433.10 USD | 0.00 USD | `+27.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 3,210,000.00 USD | 293.61 USD | 0.00 USD | `+28.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 3,320,000.00 USD | 112,050.00 USD | 0.00 USD | `+28.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 3,320,000.00 USD | 462.47 USD | 0.00 USD | `+28.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 3,320,000.00 USD | 2,180.00 USD | 0.00 USD | `+29.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 3,320,000.00 USD | 273.34 USD | 0.00 USD | `+29.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 3,320,000.00 USD | 119.49 USD | 0.00 USD | `+29.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 3,340,000.00 USD | 20,740.00 USD | 0.00 USD | `+29.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 3,340,000.00 USD | 1,430.00 USD | 0.00 USD | `+30.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 3,340,000.00 USD | 338.50 USD | 0.00 USD | `+31.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 3,350,000.00 USD | 769.57 USD | 0.00 USD | `+31.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 3,350,000.00 USD | 1,230.00 USD | 0.00 USD | `+31.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 3,350,000.00 USD | 2,450.00 USD | 0.00 USD | `+32.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 3,350,000.00 USD | 1,250.00 USD | 0.00 USD | `+32.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 3,350,000.00 USD | 143.67 USD | 0.00 USD | `+32.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 3,350,000.00 USD | 1,700.00 USD | 0.00 USD | `+33.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 3,410,000.00 USD | 62,870.00 USD | 0.00 USD | `+33.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 3,420,000.00 USD | 304.33 USD | 0.00 USD | `+33.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 3,420,000.00 USD | 241.65 USD | 0.00 USD | `+34.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 3,420,000.00 USD | 239.97 USD | 0.00 USD | `+34.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 3,420,000.00 USD | 2,470.00 USD | 0.00 USD | `+35.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 3,420,000.00 USD | 3,060.00 USD | 0.00 USD | `+35.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 3,420,000.00 USD | 351.02 USD | 0.00 USD | `+35.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,730,000.00 USD | 310,250.00 USD | 0.00 USD | `+36.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,730,000.00 USD | 309.53 USD | 0.00 USD | `+36.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,730,000.00 USD | 159.09 USD | 0.00 USD | `+36.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,730,000.00 USD | 146.21 USD | 0.00 USD | `+37.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,810,000.00 USD | 74,910.00 USD | 0.00 USD | `+37.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,810,000.00 USD | 933.81 USD | 0.00 USD | `+37.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,810,000.00 USD | 658.86 USD | 0.00 USD | `+37.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.21` | 4,020,000.00 USD | 213,390.00 USD | 0.00 USD | `+38.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.21` | 4,020,000.00 USD | 211.10 USD | 0.00 USD | `+38.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.22` | 4,020,000.00 USD | 1,050.00 USD | 0.00 USD | `+39.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.22` | 4,020,000.00 USD | 812.24 USD | 0.00 USD | `+39.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.22` | 4,020,000.00 USD | 509.71 USD | 0.00 USD | `+40.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 4,020,000.00 USD | 162.15 USD | 0.00 USD | `+40.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 4,030,000.00 USD | 187.04 USD | 0.00 USD | `+40.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 4,030,000.00 USD | 542.12 USD | 0.00 USD | `+41.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 4,050,000.00 USD | 23,740.00 USD | 0.00 USD | `+41.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.24` | 4,050,000.00 USD | 2,010.00 USD | 0.00 USD | `+41.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.24` | 4,050,000.00 USD | 345.91 USD | 0.00 USD | `+41.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 4,050,000.00 USD | 104.79 USD | 0.00 USD | `+42.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 4,050,000.00 USD | 2,470.00 USD | 0.00 USD | `+43.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 4,050,000.00 USD | 265.62 USD | 0.00 USD | `+43.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 4,060,000.00 USD | 1,480.00 USD | 0.00 USD | `+44.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 4,060,000.00 USD | 1,010.00 USD | 0.00 USD | `+44.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 4,060,000.00 USD | 340.38 USD | 0.00 USD | `+45.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 4,060,000.00 USD | 903.22 USD | 0.00 USD | `+45.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 4,060,000.00 USD | 475.01 USD | 0.00 USD | `+45.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 4,100,000.00 USD | 41,160.00 USD | 0.00 USD | `+46.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 4,110,000.00 USD | 12,840.00 USD | 0.00 USD | `+46.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 4,130,000.00 USD | 12,890.00 USD | 0.00 USD | `+47.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 4,130,000.00 USD | 8,820.00 USD | 0.00 USD | `+47.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 4,140,000.00 USD | 466.95 USD | 0.00 USD | `+48.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 4,140,000.00 USD | 613.59 USD | 0.00 USD | `+48.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 4,140,000.00 USD | 1,420.00 USD | 0.00 USD | `+48.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 4,150,000.00 USD | 13,000.00 USD | 0.00 USD | `+48.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 4,150,000.00 USD | 284.42 USD | 0.00 USD | `+48.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.32` | 4,170,000.00 USD | 22,810.00 USD | 0.00 USD | `+51.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 4,170,000.00 USD | 640.82 USD | 0.00 USD | `+52.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 4,190,000.00 USD | 13,400.00 USD | 0.00 USD | `+53.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 4,200,000.00 USD | 13,490.00 USD | 0.00 USD | `+54.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 4,210,000.00 USD | 11,580.00 USD | 0.00 USD | `+54.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 4,220,000.00 USD | 3,610.00 USD | 0.00 USD | `+55.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 4,220,000.00 USD | 1,540.00 USD | 0.00 USD | `+56.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 4,220,000.00 USD | 1,500.00 USD | 0.00 USD | `+56.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 4,230,000.00 USD | 15,000.00 USD | 0.00 USD | `+56.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 4,240,000.00 USD | 9,030.00 USD | 0.00 USD | `+56.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 4,240,000.00 USD | 569.84 USD | 0.00 USD | `+58.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 4,260,000.00 USD | 13,890.00 USD | 0.00 USD | `+59.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 4,260,000.00 USD | 2,710.00 USD | 0.00 USD | `+59.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 4,270,000.00 USD | 14,000.00 USD | 0.00 USD | `+60.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 4,290,000.00 USD | 13,100.00 USD | 0.00 USD | `+60.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 4,320,000.00 USD | 32,860.00 USD | 0.00 USD | `+61.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 4,330,000.00 USD | 7,090.00 USD | 0.00 USD | `+61.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 4,330,000.00 USD | 106.64 USD | 0.00 USD | `+61.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 4,330,000.00 USD | 1,430.00 USD | 0.00 USD | `+61.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 4,330,000.00 USD | 2,810.00 USD | 0.00 USD | `+62.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 4,340,000.00 USD | 8,420.00 USD | 0.00 USD | `+62.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 4,340,000.00 USD | 1,410.00 USD | 0.00 USD | `+63.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 4,340,000.00 USD | 431.38 USD | 0.00 USD | `+64.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 4,340,000.00 USD | 1,390.00 USD | 0.00 USD | `+64.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 4,360,000.00 USD | 14,390.00 USD | 0.00 USD | `+64.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 4,360,000.00 USD | 7,000.00 USD | 0.00 USD | `+65.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 4,360,000.00 USD | 434.98 USD | 0.00 USD | `+65.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 4,380,000.00 USD | 14,490.00 USD | 0.00 USD | `+65.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 4,380,000.00 USD | 1,370.00 USD | 0.00 USD | `+66.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.46` | 4,380,000.00 USD | 1,350.00 USD | 0.00 USD | `+67.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 4,380,000.00 USD | 1,340.00 USD | 0.00 USD | `+67.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 4,380,000.00 USD | 1,300.00 USD | 0.00 USD | `+68.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 4,390,000.00 USD | 342.08 USD | 0.00 USD | `+68.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.48` | 4,390,000.00 USD | 1,330.00 USD | 0.00 USD | `+69.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 4,390,000.00 USD | 1,320.00 USD | 0.00 USD | `+70.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 4,390,000.00 USD | 1,310.00 USD | 0.00 USD | `+70.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 4,400,000.00 USD | 14,890.00 USD | 0.00 USD | `+70.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 4,410,000.00 USD | 9,580.00 USD | 0.00 USD | `+70.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 4,430,000.00 USD | 14,980.00 USD | 0.00 USD | `+71.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 4,550,000.00 USD | 121,130.00 USD | 0.00 USD | `+71.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 4,550,000.00 USD | 1,270.00 USD | 0.00 USD | `+73.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 4,550,000.00 USD | 1,260.00 USD | 0.00 USD | `+74.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.54` | 4,550,000.00 USD | 1,980.00 USD | 0.00 USD | `+76.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.59` | 4,550,000.00 USD | 574.53 USD | 0.00 USD | `+82.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.60` | 4,560,000.00 USD | 391.32 USD | 0.00 USD | `+83.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.62` | 4,560,000.00 USD | 1,160.00 USD | 0.00 USD | `+85.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 4,560,000.00 USD | 1,140.00 USD | 0.00 USD | `+87.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 4,560,000.00 USD | 1,970.00 USD | 0.00 USD | `+87.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 4,560,000.00 USD | 281.45 USD | 0.00 USD | `+89.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.69` | 4,560,000.00 USD | 958.84 USD | 0.00 USD | `+93.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.70` | 4,560,000.00 USD | 3,550.00 USD | 0.00 USD | `+94.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 4,570,000.00 USD | 1,070.00 USD | 0.00 USD | `+99.91%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.7630` | 17,170,000.00 USD | 0.00 USD | 17,170,000.00 USD | 37,590.00 USD | 14,770.00 USD | 1,200.00 USD |
| `7D` | `0.7650` | 17,120,000.00 USD | 0.00 USD | 17,120,000.00 USD | 556.58 USD | 23,090.00 USD | 10,340.00 USD |
| `1D` | `0.7660` | 4,110,000.00 USD | 0.00 USD | 4,110,000.00 USD | 0.00 USD | 101.33 USD | 4,420.00 USD |
| `7D` | `0.7670` | 17,080,000.00 USD | 0.00 USD | 17,080,000.00 USD | 1,280.00 USD | 177.87 USD | 18,920.00 USD |
| `7D` | `0.7690` | 17,060,000.00 USD | 0.00 USD | 17,060,000.00 USD | 182.28 USD | 161.63 USD | 0.00 USD |
| `7D` | `0.7710` | 17,060,000.00 USD | 0.00 USD | 17,060,000.00 USD | 7,690.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.7790` | 17,050,000.00 USD | 0.00 USD | 17,050,000.00 USD | 0.00 USD | 5,390.00 USD | 0.00 USD |
| `1D` | `0.7800` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 0.00 USD | 7,100.00 USD | 22,420.00 USD |
| `7D` | `0.7810` | 17,050,000.00 USD | 0.00 USD | 17,050,000.00 USD | 0.00 USD | 185.50 USD | 5,230.00 USD |
| `7D` | `0.7830` | 17,040,000.00 USD | 0.00 USD | 17,040,000.00 USD | 0.00 USD | 0.00 USD | 5,450.00 USD |
| `7D` | `0.7850` | 17,040,000.00 USD | 0.00 USD | 17,040,000.00 USD | 0.00 USD | 0.00 USD | 13,160.00 USD |
| `7D` | `0.7870` | 17,030,000.00 USD | 0.00 USD | 17,030,000.00 USD | 0.00 USD | 14,110.00 USD | 0.00 USD |
| `1D` | `0.7880` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 26,800.00 USD | 572.15 USD | 0.00 USD |
| `1D` | `0.7900` | 4,050,000.00 USD | 0.00 USD | 4,050,000.00 USD | 0.00 USD | 5,310.00 USD | 0.00 USD |
| `7D` | `0.7910` | 17,010,000.00 USD | 0.00 USD | 17,010,000.00 USD | 0.00 USD | 18,920.00 USD | 0.00 USD |
| `1D` | `0.7920` | 4,040,000.00 USD | 0.00 USD | 4,040,000.00 USD | 0.00 USD | 731.00 USD | 0.00 USD |
| `7D` | `0.7930` | 16,990,000.00 USD | 0.00 USD | 16,990,000.00 USD | 0.00 USD | 0.00 USD | 41,110.00 USD |
| `1D` | `0.7940` | 4,040,000.00 USD | 0.00 USD | 4,040,000.00 USD | 0.00 USD | 4,090.00 USD | 0.00 USD |
| `7D` | `0.7950` | 16,950,000.00 USD | 0.00 USD | 16,950,000.00 USD | 9,530.00 USD | 5,600.00 USD | 9,870.00 USD |
| `1D` | `0.7960` | 4,040,000.00 USD | 0.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 11,240.00 USD |
| `7D` | `0.7970` | 16,930,000.00 USD | 0.00 USD | 16,930,000.00 USD | 9,860.00 USD | 0.00 USD | 9,820.00 USD |
| `1D` | `0.7980` | 4,020,000.00 USD | 0.00 USD | 4,020,000.00 USD | 2,830.00 USD | 8,900.00 USD | 0.00 USD |
| `7D` | `0.7990` | 16,910,000.00 USD | 0.00 USD | 16,910,000.00 USD | 488.55 USD | 0.00 USD | 8,460.00 USD |
| `1D` | `0.8000` | 4,010,000.00 USD | 0.00 USD | 4,010,000.00 USD | 0.00 USD | 11,260.00 USD | 16,320.00 USD |
| `7D` | `0.8010` | 16,900,000.00 USD | 0.00 USD | 16,900,000.00 USD | 1,890.00 USD | 14,760.00 USD | 35,910.00 USD |
| `7D` | `0.8050` | 16,840,000.00 USD | 0.00 USD | 16,840,000.00 USD | 0.00 USD | 15,090.00 USD | 0.00 USD |
| `1D` | `0.8060` | 3,980,000.00 USD | 0.00 USD | 3,980,000.00 USD | 12,740.00 USD | 12,320.00 USD | 14,150.00 USD |
| `1D` | `0.8100` | 3,950,000.00 USD | 0.00 USD | 3,950,000.00 USD | 12,970.00 USD | 5,430.00 USD | 19,940.00 USD |
| `7D` | `0.8110` | 16,830,000.00 USD | 0.00 USD | 16,830,000.00 USD | 57,370.00 USD | 6,420.00 USD | 38,210.00 USD |
| `1D` | `0.8120` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 27,480.00 USD | 1,350.00 USD | 5,320.00 USD |
| `7D` | `0.8130` | 16,730,000.00 USD | 0.00 USD | 16,730,000.00 USD | 45,800.00 USD | 16,750.00 USD | 12,050.00 USD |
| `1D` | `0.8140` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 44,940.00 USD | 23,740.00 USD | 22,730.00 USD |
| `7D` | `0.8150` | 16,650,000.00 USD | 0.00 USD | 16,650,000.00 USD | 135,770.00 USD | 50,280.00 USD | 125,560.00 USD |
| `1D` | `0.8160` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 111,700.00 USD | 22,860.00 USD | 149,520.00 USD |
| `7D` | `0.8170` | 16,340,000.00 USD | 0.00 USD | 16,340,000.00 USD | 91,050.00 USD | 23,590.00 USD | 77,680.00 USD |
| `1D` | `0.8180` | 3,500,000.00 USD | 0.00 USD | 3,500,000.00 USD | 11,610.00 USD | 20,880.00 USD | 20,350.00 USD |
| `7D` | `0.8190` | 16,150,000.00 USD | 0.00 USD | 16,150,000.00 USD | 195,400.00 USD | 52,010.00 USD | 46,820.00 USD |
| `1D` | `0.8200` | 3,440,000.00 USD | 0.00 USD | 3,440,000.00 USD | 13,230.00 USD | 16,660.00 USD | 36,060.00 USD |
| `7D` | `0.8210` | 15,850,000.00 USD | 0.00 USD | 15,850,000.00 USD | 138,580.00 USD | 56,860.00 USD | 152,680.00 USD |
| `1D` | `0.8220` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 12,100.00 USD | 19,830.00 USD | 30,110.00 USD |
| `7D` | `0.8230` | 15,510,000.00 USD | 0.00 USD | 15,510,000.00 USD | 37,880.00 USD | 34,380.00 USD | 63,940.00 USD |
| `1D` | `0.8240` | 3,320,000.00 USD | 0.00 USD | 3,320,000.00 USD | 21,120.00 USD | 16,100.00 USD | 20,080.00 USD |
| `7D` | `0.8250` | 15,370,000.00 USD | 0.00 USD | 15,370,000.00 USD | 187,510.00 USD | 27,530.00 USD | 128,420.00 USD |
| `1D` | `0.8260` | 3,260,000.00 USD | 0.00 USD | 3,260,000.00 USD | 16,150.00 USD | 3,800.00 USD | 14,020.00 USD |
| `7D` | `0.8270` | 15,030,000.00 USD | 0.00 USD | 15,030,000.00 USD | 144,410.00 USD | 51,050.00 USD | 61,810.00 USD |
| `1D` | `0.8280` | 3,230,000.00 USD | 0.00 USD | 3,230,000.00 USD | 22,620.00 USD | 12,830.00 USD | 33,850.00 USD |
| `7D` | `0.8290` | 14,770,000.00 USD | 0.00 USD | 14,770,000.00 USD | 89,470.00 USD | 40,370.00 USD | 82,560.00 USD |
| `1D` | `0.8300` | 3,160,000.00 USD | 0.00 USD | 3,160,000.00 USD | 13,880.00 USD | 9,690.00 USD | 25,690.00 USD |
| `7D` | `0.8310` | 14,560,000.00 USD | 0.00 USD | 14,560,000.00 USD | 36,870.00 USD | 30,800.00 USD | 23,260.00 USD |
| `1D` | `0.8320` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 19,130.00 USD | 29,090.00 USD | 67,320.00 USD |
| `7D` | `0.8330` | 14,470,000.00 USD | 0.00 USD | 14,470,000.00 USD | 150,740.00 USD | 85,780.00 USD | 198,250.00 USD |
| `1D` | `0.8340` | 2,990,000.00 USD | 0.00 USD | 2,990,000.00 USD | 49,780.00 USD | 16,200.00 USD | 43,970.00 USD |
| `7D` | `0.8350` | 14,030,000.00 USD | 0.00 USD | 14,030,000.00 USD | 74,030.00 USD | 14,320.00 USD | 83,810.00 USD |
| `1D` | `0.8360` | 2,880,000.00 USD | 0.00 USD | 2,880,000.00 USD | 72,180.00 USD | 21,090.00 USD | 20,660.00 USD |
| `7D` | `0.8370` | 13,860,000.00 USD | 0.00 USD | 13,860,000.00 USD | 146,890.00 USD | 59,030.00 USD | 103,270.00 USD |
| `1D` | `0.8380` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 29,780.00 USD | 12,720.00 USD | 28,260.00 USD |
| `7D` | `0.8390` | 13,550,000.00 USD | 0.00 USD | 13,550,000.00 USD | 24,790.00 USD | 86,060.00 USD | 76,830.00 USD |
| `1D` | `0.8400` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 80,010.00 USD | 25,720.00 USD | 33,570.00 USD |
| `7D` | `0.8410` | 13,360,000.00 USD | 0.00 USD | 13,360,000.00 USD | 55,190.00 USD | 40,110.00 USD | 27,930.00 USD |
| `1D` | `0.8420` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 43,150.00 USD | 35,080.00 USD | 22,140.00 USD |
| `7D` | `0.8430` | 13,240,000.00 USD | 0.00 USD | 13,240,000.00 USD | 81,850.00 USD | 84,470.00 USD | 30,730.00 USD |
| `1D` | `0.8440` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 21,450.00 USD | 12,010.00 USD | 291.54 USD |
| `7D` | `0.8450` | 13,040,000.00 USD | 0.00 USD | 13,040,000.00 USD | 43,800.00 USD | 55,690.00 USD | 114,990.00 USD |
| `1D` | `0.8460` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 3,860.00 USD | 23,780.00 USD | 40,760.00 USD |
| `7D` | `0.8470` | 12,830,000.00 USD | 0.00 USD | 12,830,000.00 USD | 27,720.00 USD | 4,350.00 USD | 31,920.00 USD |
| `1D` | `0.8480` | 2,350,000.00 USD | 0.00 USD | 2,350,000.00 USD | 46,950.00 USD | 35,940.00 USD | 44,480.00 USD |
| `7D` | `0.8490` | 12,760,000.00 USD | 0.00 USD | 12,760,000.00 USD | 45,210.00 USD | 30,580.00 USD | 46,290.00 USD |
| `1D` | `0.8500` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 52,130.00 USD | 51,210.00 USD | 155,200.00 USD |
| `7D` | `0.8510` | 12,640,000.00 USD | 0.00 USD | 12,640,000.00 USD | 95,990.00 USD | 42,650.00 USD | 42,130.00 USD |
| `1D` | `0.8520` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 72,560.00 USD | 50,510.00 USD | 39,920.00 USD |
| `7D` | `0.8530` | 12,460,000.00 USD | 0.00 USD | 12,460,000.00 USD | 30,570.00 USD | 50,890.00 USD | 24,670.00 USD |
| `1D` | `0.8540` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 56,450.00 USD | 44,760.00 USD | 65,400.00 USD |
| `7D` | `0.8550` | 12,350,000.00 USD | 0.00 USD | 12,350,000.00 USD | 78,320.00 USD | 63,400.00 USD | 98,960.00 USD |
| `1D` | `0.8560` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 28,740.00 USD | 27,040.00 USD | 10,970.00 USD |
| `7D` | `0.8570` | 12,110,000.00 USD | 0.00 USD | 12,110,000.00 USD | 99,680.00 USD | 166,050.00 USD | 6,270.00 USD |
| `1D` | `0.8580` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 185,330.00 USD | 34,130.00 USD | 114.50 USD |
| `7D` | `0.8590` | 11,840,000.00 USD | 0.00 USD | 11,840,000.00 USD | 51,400.00 USD | 12,270.00 USD | 17,420.00 USD |
| `1D` | `0.8600` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 32,470.00 USD | 33,380.00 USD | 636.30 USD |
| `7D` | `0.8610` | 11,760,000.00 USD | 0.00 USD | 11,760,000.00 USD | 36,870.00 USD | 94,130.00 USD | 32,650.00 USD |
| `1D` | `0.8620` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 6,610.00 USD | 4,970.00 USD | 666.95 USD |
| `7D` | `0.8630` | 11,600,000.00 USD | 0.00 USD | 11,600,000.00 USD | 30,710.00 USD | 13,800.00 USD | 176,670.00 USD |
| `1D` | `0.8640` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 40,460.00 USD | 34,720.00 USD | 53,730.00 USD |
| `7D` | `0.8650` | 11,380,000.00 USD | 0.00 USD | 11,380,000.00 USD | 235,900.00 USD | 16,780.00 USD | 98,750.00 USD |
| `1D` | `0.8660` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 184,320.00 USD | 33,670.00 USD | 271.63 USD |
| `7D` | `0.8670` | 11,020,000.00 USD | 0.00 USD | 11,020,000.00 USD | 159,120.00 USD | 41,080.00 USD | 58,280.00 USD |
| `1D` | `0.8680` | 926,930.00 USD | 0.00 USD | 926,930.00 USD | 49,450.00 USD | 48,790.00 USD | 58,380.00 USD |
| `7D` | `0.8690` | 10,770,000.00 USD | 0.00 USD | 10,770,000.00 USD | 182,190.00 USD | 9,930.00 USD | 195,800.00 USD |
| `1D` | `0.8700` | 770,310.00 USD | 0.00 USD | 770,310.00 USD | 59,260.00 USD | 6,380.00 USD | 898.09 USD |
| `7D` | `0.8710` | 10,380,000.00 USD | 0.00 USD | 10,380,000.00 USD | 604,760.00 USD | 13,020.00 USD | 402,050.00 USD |
| `1D` | `0.8720` | 703,770.00 USD | 0.00 USD | 703,770.00 USD | 1,300.00 USD | 54,700.00 USD | 308,910.00 USD |
| `7D` | `0.8730` | 9,360,000.00 USD | 0.00 USD | 9,360,000.00 USD | 333,320.00 USD | 78,000.00 USD | 392,180.00 USD |
| `1D` | `0.8740` | 338,870.00 USD | 0.00 USD | 338,870.00 USD | 0.00 USD | 19,580.00 USD | 45,570.00 USD |
| `7D` | `0.8750` | 8,560,000.00 USD | 0.00 USD | 8,560,000.00 USD | 643,280.00 USD | 118,620.00 USD | 323,590.00 USD |
| `1D` | `0.8760` | 273,710.00 USD | 0.00 USD | 273,710.00 USD | 3,590.00 USD | 34,150.00 USD | 178,920.00 USD |
| `7D` | `0.8770` | 7,470,000.00 USD | 0.00 USD | 7,470,000.00 USD | 398,780.00 USD | 14,470.00 USD | 3,440.00 USD |
| `1D` | `0.8780` | 57,060.00 USD | 0.00 USD | 57,060.00 USD | 5,990.00 USD | 0.00 USD | 305.84 USD |
| `7D` | `0.8790` | 7,050,000.00 USD | 0.00 USD | 7,050,000.00 USD | 296,940.00 USD | 15,310.00 USD | 3,300.00 USD |
| `1D` | `0.8800` | 50,760.00 USD | 0.00 USD | 50,760.00 USD | 7,330.00 USD | 0.00 USD | 722.37 USD |
| `7D` | `0.8810` | 6,740,000.00 USD | 0.00 USD | 6,740,000.00 USD | 629,340.00 USD | 11,380.00 USD | 576.82 USD |
| `1D` | `0.8820` | 42,710.00 USD | 0.00 USD | 42,710.00 USD | 37,490.00 USD | 0.00 USD | 305.55 USD |
| `7D` | `0.8830` | 6,100,000.00 USD | 0.00 USD | 6,100,000.00 USD | 782,180.00 USD | 10,580.00 USD | 10,070.00 USD |
| `1D` | `0.8840` | 4,920.00 USD | 0.00 USD | 4,920.00 USD | 0.00 USD | 0.00 USD | 1,820.00 USD |
| `7D` | `0.8850` | 5,290,000.00 USD | 0.00 USD | 5,290,000.00 USD | 502,690.00 USD | 14,390.00 USD | 7,040.00 USD |
| `1D` | `0.8860` | 3,090.00 USD | 0.00 USD | 3,090.00 USD | 0.00 USD | 0.00 USD | 745.79 USD |
| `7D` | `0.8870` | 4,770,000.00 USD | 0.00 USD | 4,770,000.00 USD | 619,260.00 USD | 2,410.00 USD | 3,050.00 USD |
| `7D` | `0.8890` | 4,140,000.00 USD | 0.00 USD | 4,140,000.00 USD | 1,530,000.00 USD | 3,210.00 USD | 5,380.00 USD |
| `1D` | `0.8900` | 2,350.00 USD | 0.00 USD | 2,350.00 USD | 2,250.00 USD | 0.00 USD | 95.14 USD |
| `7D` | `0.8910` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 806,690.00 USD | 8,230.00 USD | 4,740.00 USD |
| `1D` | `0.8920` | 186,590.00 USD | 186,590.00 USD | 0.00 USD | 186,330.00 USD | 0.00 USD | 255.50 USD |
| `1D` | `0.8920` | 373,180.00 USD | 373,180.00 USD | 0.00 USD | 186,330.00 USD | 0.00 USD | 255.50 USD |
| `7D` | `0.8930` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 1,770,000.00 USD | 7,680.00 USD | 728.40 USD |
| `1D` | `0.8940` | 466,140.00 USD | 466,140.00 USD | 0.00 USD | 92,970.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8950` | 744,960.00 USD | 744,960.00 USD | 0.00 USD | 738,790.00 USD | 2,700.00 USD | 3,460.00 USD |
| `7D` | `0.8950` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 738,790.00 USD | 2,700.00 USD | 3,460.00 USD |
| `1D` | `0.8960` | 466,950.00 USD | 466,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 808.94 USD |
| `7D` | `0.8970` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 659,500.00 USD | 10,620.00 USD | 890.55 USD |
| `1D` | `0.8980` | 468,010.00 USD | 468,010.00 USD | 0.00 USD | 851.50 USD | 0.00 USD | 207.32 USD |
| `7D` | `0.8990` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 308,910.00 USD | 3,220.00 USD | 129,890.00 USD |
| `1D` | `0.9000` | 694,340.00 USD | 694,340.00 USD | 0.00 USD | 73,470.00 USD | 68,700.00 USD | 84,160.00 USD |
| `7D` | `0.9010` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 130,380.00 USD | 15,640.00 USD | 816.88 USD |
| `1D` | `0.9020` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 112,580.00 USD | 96,290.00 USD | 183,010.00 USD |
| `7D` | `0.9030` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 5,880.00 USD | 78,550.00 USD | 5,760.00 USD |
| `1D` | `0.9040` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 46,130.00 USD | 124,850.00 USD | 58,160.00 USD |
| `7D` | `0.9050` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 122,230.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9060` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 76,970.00 USD | 17,480.00 USD | 0.00 USD |
| `7D` | `0.9070` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 341,080.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9080` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 92,600.00 USD | 55,120.00 USD | 81,910.00 USD |
| `7D` | `0.9090` | 3,650,000.00 USD | 3,650,000.00 USD | 0.00 USD | 53,970.00 USD | 108,380.00 USD | 179,540.00 USD |
| `1D` | `0.9100` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 96,000.00 USD | 25,960.00 USD | 0.00 USD |
| `7D` | `0.9110` | 3,960,000.00 USD | 3,960,000.00 USD | 0.00 USD | 212,760.00 USD | 103,750.00 USD | 0.00 USD |
| `1D` | `0.9120` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 25,050.00 USD | 53,680.00 USD | 0.00 USD |
| `7D` | `0.9130` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 80,230.00 USD | 34,480.00 USD | 0.00 USD |
| `1D` | `0.9140` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 79,560.00 USD | 25,930.00 USD | 142,470.00 USD |
| `7D` | `0.9150` | 4,250,000.00 USD | 4,250,000.00 USD | 0.00 USD | 111,690.00 USD | 0.00 USD | 64,730.00 USD |
| `1D` | `0.9160` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 74,950.00 USD | 35,490.00 USD | 71,620.00 USD |
| `7D` | `0.9170` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 123,530.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9180` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 38,060.00 USD | 24,510.00 USD | 0.00 USD |
| `7D` | `0.9190` | 4,650,000.00 USD | 4,650,000.00 USD | 0.00 USD | 257,890.00 USD | 13,920.00 USD | 0.00 USD |
| `1D` | `0.9200` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 8,860.00 USD | 32,760.00 USD |
| `7D` | `0.9210` | 4,860,000.00 USD | 4,860,000.00 USD | 0.00 USD | 128,930.00 USD | 16,660.00 USD | 63,810.00 USD |
| `1D` | `0.9220` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 124,570.00 USD | 61,670.00 USD | 219,080.00 USD |
| `7D` | `0.9230` | 5,310,000.00 USD | 5,310,000.00 USD | 0.00 USD | 51,510.00 USD | 64,540.00 USD | 341,030.00 USD |
| `1D` | `0.9240` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 217,830.00 USD | 59,780.00 USD | 184,790.00 USD |
| `7D` | `0.9250` | 5,480,000.00 USD | 5,480,000.00 USD | 0.00 USD | 52,570.00 USD | 41,710.00 USD | 67,310.00 USD |
| `1D` | `0.9260` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 63,790.00 USD | 80,680.00 USD | 92,700.00 USD |
| `7D` | `0.9270` | 5,810,000.00 USD | 5,810,000.00 USD | 0.00 USD | 209,950.00 USD | 36,910.00 USD | 89,770.00 USD |
| `1D` | `0.9280` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 0.00 USD | 63,360.00 USD | 59,850.00 USD |
| `7D` | `0.9290` | 5,860,000.00 USD | 5,860,000.00 USD | 0.00 USD | 0.00 USD | 51,870.00 USD | 0.00 USD |
| `1D` | `0.9300` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 39,620.00 USD | 57,070.00 USD | 79,160.00 USD |
| `7D` | `0.9310` | 6,260,000.00 USD | 6,260,000.00 USD | 0.00 USD | 177,720.00 USD | 46,670.00 USD | 166,200.00 USD |
| `1D` | `0.9320` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 128,960.00 USD | 29,480.00 USD | 35,380.00 USD |
| `7D` | `0.9330` | 6,370,000.00 USD | 6,370,000.00 USD | 0.00 USD | 0.00 USD | 50,420.00 USD | 63,160.00 USD |
| `1D` | `0.9340` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 2,150.00 USD | 857.80 USD | 0.00 USD |
| `7D` | `0.9350` | 6,480,000.00 USD | 6,480,000.00 USD | 0.00 USD | 53,950.00 USD | 52,710.00 USD | 0.00 USD |
| `1D` | `0.9360` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 25,730.00 USD | 33,250.00 USD | 107,120.00 USD |
| `7D` | `0.9370` | 6,770,000.00 USD | 6,770,000.00 USD | 0.00 USD | 251,760.00 USD | 0.00 USD | 41,940.00 USD |
| `1D` | `0.9380` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 262,840.00 USD | 118,850.00 USD | 293,510.00 USD |
| `7D` | `0.9390` | 7,150,000.00 USD | 7,150,000.00 USD | 0.00 USD | 82,760.00 USD | 33,320.00 USD | 263,360.00 USD |
| `1D` | `0.9400` | 5,000,000.00 USD | 5,000,000.00 USD | 0.00 USD | 119,220.00 USD | 1,710.00 USD | 67,280.00 USD |
| `7D` | `0.9410` | 7,270,000.00 USD | 7,270,000.00 USD | 0.00 USD | 123,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9420` | 5,030,000.00 USD | 5,030,000.00 USD | 0.00 USD | 9,740.00 USD | 0.00 USD | 17,370.00 USD |
| `7D` | `0.9430` | 7,370,000.00 USD | 7,370,000.00 USD | 0.00 USD | 0.00 USD | 62,100.00 USD | 33,660.00 USD |
| `1D` | `0.9440` | 5,180,000.00 USD | 5,180,000.00 USD | 0.00 USD | 2,290.00 USD | 75,230.00 USD | 73,420.00 USD |
| `7D` | `0.9450` | 7,700,000.00 USD | 7,700,000.00 USD | 0.00 USD | 0.00 USD | 244,270.00 USD | 90,360.00 USD |
| `1D` | `0.9460` | 5,460,000.00 USD | 5,460,000.00 USD | 0.00 USD | 59,870.00 USD | 33,530.00 USD | 184,380.00 USD |
| `7D` | `0.9470` | 7,910,000.00 USD | 7,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 210,630.00 USD |
| `1D` | `0.9480` | 5,670,000.00 USD | 5,670,000.00 USD | 0.00 USD | 89,360.00 USD | 67,670.00 USD | 56,220.00 USD |
| `7D` | `0.9490` | 8,140,000.00 USD | 8,140,000.00 USD | 0.00 USD | 0.00 USD | 107,340.00 USD | 118,920.00 USD |
| `1D` | `0.9500` | 5,800,000.00 USD | 5,800,000.00 USD | 0.00 USD | 17,970.00 USD | 36,000.00 USD | 69,750.00 USD |
| `7D` | `0.9510` | 8,960,000.00 USD | 8,960,000.00 USD | 0.00 USD | 2,840.00 USD | 87,720.00 USD | 732,960.00 USD |
| `1D` | `0.9520` | 6,070,000.00 USD | 6,070,000.00 USD | 0.00 USD | 52,120.00 USD | 28,040.00 USD | 196,190.00 USD |
| `7D` | `0.9530` | 8,960,000.00 USD | 8,960,000.00 USD | 0.00 USD | 0.00 USD | 1,270.00 USD | 0.00 USD |
| `1D` | `0.9540` | 6,290,000.00 USD | 6,290,000.00 USD | 0.00 USD | 62,990.00 USD | 74,340.00 USD | 78,100.00 USD |
| `7D` | `0.9550` | 9,100,000.00 USD | 9,100,000.00 USD | 0.00 USD | 71,910.00 USD | 1,290.00 USD | 60,300.00 USD |
| `1D` | `0.9560` | 6,360,000.00 USD | 6,360,000.00 USD | 0.00 USD | 24,450.00 USD | 33,820.00 USD | 15,050.00 USD |
| `7D` | `0.9570` | 9,570,000.00 USD | 9,570,000.00 USD | 0.00 USD | 463,830.00 USD | 2,240.00 USD | 2,940.00 USD |
| `1D` | `0.9580` | 6,390,000.00 USD | 6,390,000.00 USD | 0.00 USD | 689.00 USD | 26,200.00 USD | 159.08 USD |
| `7D` | `0.9590` | 10,130,000.00 USD | 10,130,000.00 USD | 0.00 USD | 562,050.00 USD | 1,040.00 USD | 3,520.00 USD |
| `1D` | `0.9600` | 6,650,000.00 USD | 6,650,000.00 USD | 0.00 USD | 111,160.00 USD | 66,100.00 USD | 82,850.00 USD |
| `7D` | `0.9610` | 11,500,000.00 USD | 11,500,000.00 USD | 0.00 USD | 698,570.00 USD | 190,470.00 USD | 479,310.00 USD |
| `1D` | `0.9620` | 7,340,000.00 USD | 7,340,000.00 USD | 0.00 USD | 315,960.00 USD | 137,300.00 USD | 239,040.00 USD |
| `7D` | `0.9630` | 13,010,000.00 USD | 13,010,000.00 USD | 0.00 USD | 579,300.00 USD | 301,610.00 USD | 624,890.00 USD |
| `1D` | `0.9640` | 7,990,000.00 USD | 7,990,000.00 USD | 0.00 USD | 334,070.00 USD | 117,160.00 USD | 197,090.00 USD |
| `7D` | `0.9650` | 14,570,000.00 USD | 14,570,000.00 USD | 0.00 USD | 857,470.00 USD | 301,210.00 USD | 408,950.00 USD |
| `1D` | `0.9660` | 8,490,000.00 USD | 8,490,000.00 USD | 0.00 USD | 243,570.00 USD | 139,760.00 USD | 120,140.00 USD |
| `7D` | `0.9670` | 16,710,000.00 USD | 16,710,000.00 USD | 0.00 USD | 889,580.00 USD | 544,430.00 USD | 706,070.00 USD |
| `1D` | `0.9680` | 9,040,000.00 USD | 9,040,000.00 USD | 0.00 USD | 199,180.00 USD | 70,260.00 USD | 280,280.00 USD |
| `7D` | `0.9690` | 18,100,000.00 USD | 18,100,000.00 USD | 0.00 USD | 596,350.00 USD | 343,680.00 USD | 447,080.00 USD |
| `1D` | `0.9700` | 9,580,000.00 USD | 9,580,000.00 USD | 0.00 USD | 257,240.00 USD | 106,690.00 USD | 174,530.00 USD |
| `7D` | `0.9710` | 19,200,000.00 USD | 19,200,000.00 USD | 0.00 USD | 645,500.00 USD | 305,860.00 USD | 143,550.00 USD |
| `1D` | `0.9720` | 9,930,000.00 USD | 9,930,000.00 USD | 0.00 USD | 122,820.00 USD | 90,440.00 USD | 138,160.00 USD |
| `7D` | `0.9730` | 19,990,000.00 USD | 19,990,000.00 USD | 0.00 USD | 456,990.00 USD | 160,420.00 USD | 172,850.00 USD |
| `1D` | `0.9740` | 10,090,000.00 USD | 10,090,000.00 USD | 0.00 USD | 81,230.00 USD | 31,010.00 USD | 39,830.00 USD |
| `7D` | `0.9750` | 20,680,000.00 USD | 20,680,000.00 USD | 0.00 USD | 201,510.00 USD | 293,590.00 USD | 194,890.00 USD |
| `1D` | `0.9760` | 10,230,000.00 USD | 10,230,000.00 USD | 0.00 USD | 31,860.00 USD | 33,470.00 USD | 76,650.00 USD |
| `7D` | `0.9770` | 21,720,000.00 USD | 21,720,000.00 USD | 0.00 USD | 329,170.00 USD | 211,000.00 USD | 503,400.00 USD |
| `1D` | `0.9780` | 10,350,000.00 USD | 10,350,000.00 USD | 0.00 USD | 4,640.00 USD | 25,130.00 USD | 91,180.00 USD |
| `7D` | `0.9790` | 22,460,000.00 USD | 22,460,000.00 USD | 0.00 USD | 411,780.00 USD | 99,560.00 USD | 223,900.00 USD |
| `1D` | `0.9800` | 10,590,000.00 USD | 10,590,000.00 USD | 0.00 USD | 65,550.00 USD | 48,270.00 USD | 127,720.00 USD |
| `7D` | `0.9810` | 22,970,000.00 USD | 22,970,000.00 USD | 0.00 USD | 264,890.00 USD | 83,040.00 USD | 166,860.00 USD |
| `1D` | `0.9820` | 10,800,000.00 USD | 10,800,000.00 USD | 0.00 USD | 132,760.00 USD | 29,280.00 USD | 44,360.00 USD |
| `7D` | `0.9830` | 23,550,000.00 USD | 23,550,000.00 USD | 0.00 USD | 260,850.00 USD | 115,290.00 USD | 200,330.00 USD |
| `1D` | `0.9840` | 10,940,000.00 USD | 10,940,000.00 USD | 0.00 USD | 58,950.00 USD | 68,840.00 USD | 18,200.00 USD |
| `7D` | `0.9850` | 23,960,000.00 USD | 23,960,000.00 USD | 0.00 USD | 234,160.00 USD | 58,210.00 USD | 117,390.00 USD |
| `1D` | `0.9860` | 11,170,000.00 USD | 11,170,000.00 USD | 0.00 USD | 83,160.00 USD | 43,210.00 USD | 100,330.00 USD |
| `7D` | `0.9870` | 24,450,000.00 USD | 24,450,000.00 USD | 0.00 USD | 248,980.00 USD | 191,820.00 USD | 57,080.00 USD |
| `1D` | `0.9880` | 11,320,000.00 USD | 11,320,000.00 USD | 0.00 USD | 82,930.00 USD | 16,000.00 USD | 49,360.00 USD |
| `7D` | `0.9890` | 24,750,000.00 USD | 24,750,000.00 USD | 0.00 USD | 194,850.00 USD | 78,280.00 USD | 18,200.00 USD |
| `1D` | `0.9900` | 11,490,000.00 USD | 11,490,000.00 USD | 0.00 USD | 87,940.00 USD | 35,060.00 USD | 51,990.00 USD |
| `7D` | `0.9910` | 25,120,000.00 USD | 25,120,000.00 USD | 0.00 USD | 198,890.00 USD | 89,640.00 USD | 84,050.00 USD |
| `1D` | `0.9920` | 11,600,000.00 USD | 11,600,000.00 USD | 0.00 USD | 62,110.00 USD | 27,720.00 USD | 21,600.00 USD |
| `7D` | `0.9930` | 25,480,000.00 USD | 25,480,000.00 USD | 0.00 USD | 228,340.00 USD | 63,950.00 USD | 72,830.00 USD |
| `1D` | `0.9940` | 11,770,000.00 USD | 11,770,000.00 USD | 0.00 USD | 60,860.00 USD | 36,590.00 USD | 70,300.00 USD |
| `7D` | `0.9950` | 25,800,000.00 USD | 25,800,000.00 USD | 0.00 USD | 48,120.00 USD | 138,500.00 USD | 125,920.00 USD |
| `1D` | `0.9960` | 11,800,000.00 USD | 11,800,000.00 USD | 0.00 USD | 6,270.00 USD | 5,900.00 USD | 20,320.00 USD |
| `7D` | `0.9970` | 26,450,000.00 USD | 26,450,000.00 USD | 0.00 USD | 215,040.00 USD | 81,210.00 USD | 360,870.00 USD |
| `1D` | `0.9980` | 12,080,000.00 USD | 12,080,000.00 USD | 0.00 USD | 110,050.00 USD | 20,740.00 USD | 149,210.00 USD |
| `7D` | `0.9990` | 26,740,000.00 USD | 26,740,000.00 USD | 0.00 USD | 145,170.00 USD | 35,870.00 USD | 101,850.00 USD |
| `1D` | `1.00` | 12,140,000.00 USD | 12,140,000.00 USD | 0.00 USD | 17,400.00 USD | 21,440.00 USD | 16,850.00 USD |
| `7D` | `1.00` | 27,180,000.00 USD | 27,180,000.00 USD | 0.00 USD | 202,970.00 USD | 57,170.00 USD | 183,960.00 USD |
| `1D` | `1.00` | 12,210,000.00 USD | 12,210,000.00 USD | 0.00 USD | 15,000.00 USD | 17,420.00 USD | 36,190.00 USD |
| `7D` | `1.00` | 27,680,000.00 USD | 27,680,000.00 USD | 0.00 USD | 226,340.00 USD | 61,540.00 USD | 206,730.00 USD |
| `1D` | `1.00` | 12,280,000.00 USD | 12,280,000.00 USD | 0.00 USD | 15,370.00 USD | 21,270.00 USD | 30,450.00 USD |
| `7D` | `1.00` | 27,830,000.00 USD | 27,830,000.00 USD | 0.00 USD | 51,930.00 USD | 39,560.00 USD | 66,390.00 USD |
| `1D` | `1.01` | 12,310,000.00 USD | 12,310,000.00 USD | 0.00 USD | 9,400.00 USD | 14,230.00 USD | 8,760.00 USD |
| `7D` | `1.01` | 28,320,000.00 USD | 28,320,000.00 USD | 0.00 USD | 256,020.00 USD | 15,900.00 USD | 212,420.00 USD |
| `1D` | `1.01` | 12,350,000.00 USD | 12,350,000.00 USD | 0.00 USD | 18,940.00 USD | 9,170.00 USD | 12,090.00 USD |
| `7D` | `1.01` | 28,920,000.00 USD | 28,920,000.00 USD | 0.00 USD | 247,480.00 USD | 105,290.00 USD | 248,850.00 USD |
| `1D` | `1.01` | 12,390,000.00 USD | 12,390,000.00 USD | 0.00 USD | 17,560.00 USD | 5,290.00 USD | 14,820.00 USD |
| `7D` | `1.01` | 29,870,000.00 USD | 29,870,000.00 USD | 0.00 USD | 457,740.00 USD | 174,650.00 USD | 316,860.00 USD |
| `1D` | `1.01` | 12,450,000.00 USD | 12,450,000.00 USD | 0.00 USD | 21,660.00 USD | 13,540.00 USD | 33,850.00 USD |
| `7D` | `1.01` | 30,580,000.00 USD | 30,580,000.00 USD | 0.00 USD | 188,370.00 USD | 177,300.00 USD | 345,030.00 USD |
| `1D` | `1.01` | 12,500,000.00 USD | 12,500,000.00 USD | 0.00 USD | 13,360.00 USD | 10,400.00 USD | 25,990.00 USD |
| `7D` | `1.01` | 31,030,000.00 USD | 31,030,000.00 USD | 0.00 USD | 263,990.00 USD | 59,720.00 USD | 126,540.00 USD |
| `1D` | `1.02` | 12,540,000.00 USD | 12,540,000.00 USD | 0.00 USD | 22,200.00 USD | 10,550.00 USD | 6,610.00 USD |
| `7D` | `1.02` | 31,830,000.00 USD | 31,830,000.00 USD | 0.00 USD | 339,650.00 USD | 97,830.00 USD | 359,940.00 USD |
| `1D` | `1.02` | 12,570,000.00 USD | 12,570,000.00 USD | 0.00 USD | 18,050.00 USD | 4,150.00 USD | 133.18 USD |
| `7D` | `1.02` | 32,660,000.00 USD | 32,660,000.00 USD | 0.00 USD | 291,360.00 USD | 74,810.00 USD | 467,860.00 USD |
| `1D` | `1.02` | 12,660,000.00 USD | 12,660,000.00 USD | 0.00 USD | 31,730.00 USD | 13,020.00 USD | 44,180.00 USD |
| `7D` | `1.02` | 33,090,000.00 USD | 33,090,000.00 USD | 0.00 USD | 153,580.00 USD | 41,370.00 USD | 235,080.00 USD |
| `1D` | `1.02` | 12,740,000.00 USD | 12,740,000.00 USD | 0.00 USD | 49,170.00 USD | 12,160.00 USD | 20,660.00 USD |
| `7D` | `1.02` | 33,410,000.00 USD | 33,410,000.00 USD | 0.00 USD | 151,650.00 USD | 60,000.00 USD | 103,400.00 USD |
| `1D` | `1.02` | 12,810,000.00 USD | 12,810,000.00 USD | 0.00 USD | 29,780.00 USD | 12,720.00 USD | 28,260.00 USD |
| `7D` | `1.02` | 33,630,000.00 USD | 33,630,000.00 USD | 0.00 USD | 75,770.00 USD | 54,210.00 USD | 94,000.00 USD |
| `1D` | `1.03` | 12,880,000.00 USD | 12,880,000.00 USD | 0.00 USD | 17,840.00 USD | 16,400.00 USD | 33,500.00 USD |
| `7D` | `1.03` | 33,880,000.00 USD | 33,880,000.00 USD | 0.00 USD | 104,260.00 USD | 35,230.00 USD | 111,040.00 USD |
| `1D` | `1.03` | 12,890,000.00 USD | 12,890,000.00 USD | 0.00 USD | 550.85 USD | 116.87 USD | 11,880.00 USD |
| `7D` | `1.03` | 34,090,000.00 USD | 34,090,000.00 USD | 0.00 USD | 85,920.00 USD | 56,310.00 USD | 67,150.00 USD |
| `1D` | `1.03` | 12,920,000.00 USD | 12,920,000.00 USD | 0.00 USD | 8,830.00 USD | 12,110.00 USD | 10,170.00 USD |
| `7D` | `1.03` | 34,520,000.00 USD | 34,520,000.00 USD | 0.00 USD | 197,430.00 USD | 78,810.00 USD | 156,890.00 USD |
| `1D` | `1.03` | 12,950,000.00 USD | 12,950,000.00 USD | 0.00 USD | 19,720.00 USD | 7,410.00 USD | 0.35 USD |
| `7D` | `1.03` | 34,850,000.00 USD | 34,850,000.00 USD | 0.00 USD | 57,570.00 USD | 103,690.00 USD | 163,320.00 USD |
| `1D` | `1.03` | 12,960,000.00 USD | 12,960,000.00 USD | 0.00 USD | 439.80 USD | 4,130.00 USD | 13,930.00 USD |
| `7D` | `1.03` | 35,040,000.00 USD | 35,040,000.00 USD | 0.00 USD | 112,550.00 USD | 13,040.00 USD | 63,350.00 USD |
| `1D` | `1.04` | 13,030,000.00 USD | 13,030,000.00 USD | 0.00 USD | 18,450.00 USD | 7,120.00 USD | 43,600.00 USD |
| `7D` | `1.04` | 35,430,000.00 USD | 35,430,000.00 USD | 0.00 USD | 176,150.00 USD | 41,220.00 USD | 181,100.00 USD |
| `7D` | `1.04` | 35,740,000.00 USD | 35,740,000.00 USD | 0.00 USD | 112,210.00 USD | 19,230.00 USD | 175,940.00 USD |
| `7D` | `1.04` | 35,970,000.00 USD | 35,970,000.00 USD | 0.00 USD | 104,270.00 USD | 53,470.00 USD | 72,030.00 USD |
| `7D` | `1.04` | 36,060,000.00 USD | 36,060,000.00 USD | 0.00 USD | 18,340.00 USD | 49,420.00 USD | 23,210.00 USD |
| `7D` | `1.04` | 36,150,000.00 USD | 36,150,000.00 USD | 0.00 USD | 68,630.00 USD | 17,210.00 USD | 4,310.00 USD |
| `7D` | `1.05` | 36,260,000.00 USD | 36,260,000.00 USD | 0.00 USD | 78,420.00 USD | 30,790.00 USD | 829.98 USD |
| `7D` | `1.05` | 36,340,000.00 USD | 36,340,000.00 USD | 0.00 USD | 35,930.00 USD | 20,630.00 USD | 16,040.00 USD |
| `7D` | `1.05` | 36,360,000.00 USD | 36,360,000.00 USD | 0.00 USD | 22,610.00 USD | 0.00 USD | 135.33 USD |
| `7D` | `1.05` | 36,440,000.00 USD | 36,440,000.00 USD | 0.00 USD | 8,370.00 USD | 47,690.00 USD | 28,560.00 USD |
| `7D` | `1.05` | 36,500,000.00 USD | 36,500,000.00 USD | 0.00 USD | 2,990.00 USD | 11,060.00 USD | 45,980.00 USD |
| `7D` | `1.06` | 36,510,000.00 USD | 36,510,000.00 USD | 0.00 USD | 6,580.00 USD | 2,720.00 USD | 0.00 USD |
| `7D` | `1.06` | 36,510,000.00 USD | 36,510,000.00 USD | 0.00 USD | 0.00 USD | 194.87 USD | 173.28 USD |
| `7D` | `1.06` | 36,550,000.00 USD | 36,550,000.00 USD | 0.00 USD | 17,530.00 USD | 3,870.00 USD | 11,890.00 USD |
| `7D` | `1.06` | 36,560,000.00 USD | 36,560,000.00 USD | 0.00 USD | 10,210.00 USD | 0.00 USD | 647.09 USD |
| `7D` | `1.06` | 36,560,000.00 USD | 36,560,000.00 USD | 0.00 USD | 6,770.00 USD | 1,110.00 USD | 0.00 USD |
| `7D` | `1.07` | 36,570,000.00 USD | 36,570,000.00 USD | 0.00 USD | 0.00 USD | 1,120.00 USD | 74.53 USD |
| `7D` | `1.07` | 36,600,000.00 USD | 36,600,000.00 USD | 0.00 USD | 2,410.00 USD | 12,740.00 USD | 17,950.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `584.13M` | Total OI Tokens: `656,729,303.8 SUI`
  * 1h OI Change: `-3.02%` | 4h OI Change: `-7.18%` | 24h OI Change: `-9.04%`
  * Exchange Breakdown: Binance=`109.75M` | Bybit=`77.56M` | OKX=`33.13M` | Hyperliquid=`29.16M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `2.31K` | Last 24h: `23.24K` | Last 3d: `72.27K` | Last 7d: `159.10K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0015%` | **USDT OKX** | `0.0068%` |
| **USDT Bybit** | `-0.0026%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0022%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0048%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `SUI` | `50.28%` | `49.72%` | `1.01` | 15,560,000.00 USD |
| `15M` | `Binance` | `52.21%` | `47.79%` | `1.09` | 6,480,000.00 USD |
| `15M` | `OKX` | `49.75%` | `50.25%` | `0.99` | 1,000,000.00 USD |
| `15M` | `Bybit` | `50.73%` | `49.27%` | `1.03` | 1,300,000.00 USD |
| `15M` | `KuCoin` | `49%` | `51%` | `0.96` | 77,630.00 USD |
| `15M` | `Gate` | `47.23%` | `52.77%` | `0.90` | 396,480.00 USD |
| `15M` | `Bitget` | `66.6%` | `33.4%` | `1.99` | 616,910.00 USD |
| `15M` | `BingX` | `58.32%` | `41.68%` | `1.40` | 595,940.00 USD |
| `15M` | `MEXC` | `58.36%` | `41.64%` | `1.40` | 1,160,000.00 USD |
| `15M` | `Bitunix` | `44.64%` | `55.36%` | `0.81` | 381,030.00 USD |
| `15M` | `Hyperliquid` | `21.35%` | `78.65%` | `0.27` | 275,460.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `85.76%` | `14.24%` | `6.02` | 2,860,000.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 71.37 USD |
| `15M` | `WhiteBIT` | `6.61%` | `93.39%` | `0.07` | 284,510.00 USD |
| `15M` | `HTX` | `51.17%` | `48.83%` | `1.05` | 3,140.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `50.66%` | `49.34%` | `1.03` | 71,730.00 USD |
| `15M` | `Aster` | `68.14%` | `31.86%` | `2.14` | 36,660.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `25.78%` | `74.22%` | `0.35` | 15,000.00 USD |
| `15M` | `Whale Positions` | `52.21%` | `47.79%` | `1.09` | 6,480,000.00 USD |
| `15M` | `Global Accounts` | `50.28%` | `49.72%` | `1.01` | 15,560,000.00 USD |
| `1H` | `SUI` | `46.17%` | `53.83%` | `0.86` | 192,050,000.00 USD |
| `1H` | `Binance` | `42.92%` | `57.08%` | `0.75` | 81,990,000.00 USD |
| `1H` | `OKX` | `50.57%` | `49.43%` | `1.02` | 26,890,000.00 USD |
| `1H` | `Bybit` | `47.92%` | `52.08%` | `0.92` | 27,260,000.00 USD |
| `1H` | `KuCoin` | `46.9%` | `53.1%` | `0.88` | 1,950,000.00 USD |
| `1H` | `Gate` | `50.09%` | `49.91%` | `1.00` | 3,090,000.00 USD |
| `1H` | `Bitget` | `43.39%` | `56.61%` | `0.77` | 11,730,000.00 USD |
| `1H` | `BingX` | `58.86%` | `41.14%` | `1.43` | 4,480,000.00 USD |
| `1H` | `MEXC` | `50.15%` | `49.85%` | `1.01` | 15,060,000.00 USD |
| `1H` | `Bitunix` | `42.57%` | `57.43%` | `0.74` | 7,630,000.00 USD |
| `1H` | `Hyperliquid` | `44.83%` | `55.17%` | `0.81` | 7,300,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.26%` | `49.74%` | `1.01` | 616,010.00 USD |
| `1H` | `Crypto.com` | `43.39%` | `56.61%` | `0.77` | 0.00 USD |
| `1H` | `WhiteBIT` | `24.46%` | `75.54%` | `0.32` | 1,330,000.00 USD |
| `1H` | `HTX` | `49.8%` | `50.2%` | `0.99` | 493,420.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `36.22%` | `63.78%` | `0.57` | 976,990.00 USD |
| `1H` | `Aster` | `31.85%` | `68.15%` | `0.47` | 1,030,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `59.82%` | `40.18%` | `1.49` | 241,770.00 USD |
| `1H` | `Whale Positions` | `42.92%` | `57.08%` | `0.75` | 81,990,000.00 USD |
| `1H` | `Global Accounts` | `46.17%` | `53.83%` | `0.86` | 192,050,000.00 USD |
| `4H` | `SUI` | `46.53%` | `53.47%` | `0.87` | 161,240,000.00 USD |
| `4H` | `Binance` | `46.62%` | `53.38%` | `0.87` | 63,280,000.00 USD |
| `4H` | `OKX` | `48.82%` | `51.18%` | `0.95` | 12,140,000.00 USD |
| `4H` | `Bybit` | `45.49%` | `54.51%` | `0.83` | 12,620,000.00 USD |
| `4H` | `KuCoin` | `45.39%` | `54.61%` | `0.83` | 1,360,000.00 USD |
| `4H` | `Gate` | `49.79%` | `50.21%` | `0.99` | 3,300,000.00 USD |
| `4H` | `Bitget` | `46.6%` | `53.4%` | `0.87` | 4,600,000.00 USD |
| `4H` | `BingX` | `46.44%` | `53.56%` | `0.87` | 15,620,000.00 USD |
| `4H` | `MEXC` | `45.04%` | `54.96%` | `0.82` | 10,590,000.00 USD |
| `4H` | `Bitunix` | `47.71%` | `52.29%` | `0.91` | 4,630,000.00 USD |
| `4H` | `Hyperliquid` | `41.35%` | `58.65%` | `0.71` | 2,990,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `42.15%` | `57.85%` | `0.73` | 23,720,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 42,160.00 USD |
| `4H` | `WhiteBIT` | `50.92%` | `49.08%` | `1.04` | 4,990,000.00 USD |
| `4H` | `HTX` | `51.91%` | `48.09%` | `1.08` | 72,500.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `47.06%` | `52.94%` | `0.89` | 604,890.00 USD |
| `4H` | `Aster` | `36.07%` | `63.93%` | `0.56` | 384,250.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `49.55%` | `50.45%` | `0.98` | 268,920.00 USD |
| `4H` | `Whale Positions` | `46.62%` | `53.38%` | `0.87` | 63,280,000.00 USD |
| `4H` | `Global Accounts` | `46.53%` | `53.47%` | `0.87` | 161,240,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.9315` | `0.9301` | `0.9315` | `0.9321` | `0.9274` | 1,221,799.97 USD | 672,184.00 USD | 549,615.97 USD | 122,568.03 USD | `+10.03%` | `9B / 6S` |
| `0:00 UTC` | `0.9318` | `0.9320` | `0.9318` | `0.9338` | `0.9294` | 1,810,474.94 USD | 929,976.91 USD | 880,498.03 USD | 49,478.88 USD | `+2.73%` | `7B / 6S` |
| `5:00 UTC` | `0.9302` | `0.9304` | `0.9302` | `0.9331` | `0.9288` | 1,273,512.84 USD | 565,164.16 USD | 708,348.68 USD | -143,184.52 USD | `-11.24%` | `4B / 11S` |
| `0:00 UTC` | `0.9115` | `0.9168` | `0.9115` | `0.9303` | `0.9099` | 9,410,634.53 USD | 4,625,948.50 USD | 4,784,686.02 USD | -158,737.52 USD | `-1.69%` | `3B / 20S` |
| `5:00 UTC` | `0.9172` | `0.9175` | `0.9172` | `0.9204` | `0.9146` | 2,946,350.12 USD | 1,501,911.34 USD | 1,444,438.78 USD | 57,472.55 USD | `+1.95%` | `10B / 6S` |
| `0:00 UTC` | `0.8942` | `0.8944` | `0.8942` | `0.9194` | `0.8750` | 25,714,743.86 USD | 10,323,786.97 USD | 15,390,956.89 USD | -5,067,169.92 USD | `-19.71%` | `3B / 22S` |
| `5:00 UTC` | `0.8801` | `0.8742` | `0.8801` | `0.8897` | `0.8575` | 25,765,113.89 USD | 12,461,836.10 USD | 13,303,277.79 USD | -841,441.70 USD | `-3.27%` | `7B / 12S` |
| `0:00 UTC` | `0.8841` | `0.8789` | `0.8841` | `0.8854` | `0.8692` | 12,554,511.67 USD | 6,312,205.57 USD | 6,242,306.10 USD | 69,899.48 USD | `+0.56%` | `13B / 6S` |
| `5:00 UTC` | `0.8962` | `0.8922` | `0.8962` | `0.8998` | `0.8850` | 10,029,099.72 USD | 5,129,823.74 USD | 4,899,275.97 USD | 230,547.77 USD | `+2.30%` | `13B / 7S` |
| `0:00 UTC` | `0.8949` | `0.8944` | `0.8949` | `0.8958` | `0.8930` | 539,826.12 USD | 322,826.92 USD | 216,999.20 USD | 105,827.72 USD | `+19.60%` | `8B / 0S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 20:49` | `Volume 5.0M SUI` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.9287` | 0.00 USD | 0.00 USD |
| `10-28 19:47` | `Range 0.0025` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.9190` | 0.00 USD | 0.00 USD |
| `10-28 19:31` | `Volume 5.0M SUI` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.9164` | 1,200,000.00 USD | 0.00 USD |
| `10-28 19:23` | `Range 0.0025` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.9184` | 316,000.00 USD | 0.00 USD |
| `10-28 19:23` | `Range 0.0025` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.9184` | 0.00 USD | 0.00 USD |
| `10-28 19:23` | `Range 0.0025` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.9184` | 316,000.00 USD | 0.00 USD |
| `10-28 18:48` | `Range 0.0025` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.9216` | 447,000.00 USD | 0.00 USD |
| `10-28 18:48` | `Range 0.0025` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.9216` | 447,000.00 USD | 0.00 USD |
| `10-28 17:45` | `Range 0.0025` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.9270` | 0.00 USD | 0.00 USD |
| `10-28 17:36` | `Range 0.0025` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.9363` | 244,000.00 USD | 0.00 USD |
| `10-28 16:37` | `Volume 5.0M SUI` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.9388` | 1,300,000.00 USD | 0.00 USD |
| `10-28 15:31` | `Range 0.0025` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.9459` | 418,000.00 USD | 0.00 USD |
| `10-28 15:15` | `Range 0.0025` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.9429` | 0.00 USD | 0.00 USD |
| `10-28 14:06` | `Range 0.0025` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.9479` | 312,000.00 USD | 0.00 USD |
| `10-28 14:06` | `Range 0.0025` | `Trapped longs` | **`BEARISH`** | Failed breakout | `0.9479` | 312,000.00 USD | 0.00 USD |
| `10-28 13:59` | `Volume 5.0M SUI` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `0.9479` | 2,000,000.00 USD | 0.00 USD |
| `10-28 13:57` | `Range 0.0025` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `0.9455` | 0.00 USD | 0.00 USD |
| `10-28 12:46` | `Range 0.0025` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.9318` | 0.00 USD | 0.00 USD |
| `10-28 11:50` | `Range 0.0025` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `0.9399` | 1,200,000.00 USD | 0.00 USD |
| `10-28 11:10` | `Range 0.0025` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.9359` | 0.00 USD | 0.00 USD |
| `10-28 11:10` | `Range 0.0025` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.9332` | 0.00 USD | 0.00 USD |
| `10-28 10:36` | `Range 0.0025` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.9342` | 0.00 USD | 0.00 USD |
| `10-28 07:42` | `Range 0.0025` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.9370` | 450,000.00 USD | 0.00 USD |
| `10-28 06:51` | `Range 0.0025` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `0.9348` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | -348,060.00 USD | 264,030.00 USD | **`DISTRIBUTION`** |
| `15m` | -526,300.00 USD | 1,490,000.00 USD | **`ACCUMULATION`** |
| `30m` | 392,660.00 USD | 3,530,000.00 USD | **`ACCUMULATION`** |
| `1h` | -6,080,000.00 USD | -11,210,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -7,450,000.00 USD | -11,360,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -7,880,000.00 USD | -12,370,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -5,320,000.00 USD | -18,190,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -4,180,000.00 USD | -15,340,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -4,180,000.00 USD | -16,120,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -9,220,000.00 USD | -29,420,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -22,310,000.00 USD | -77,440,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -150,890,000.00 USD | -475,830,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-348.06K` | 15m=`-526.30K` | 1h=`-6.08M` | 24h=`-9.22M`
* Futures Capital Netflows: 5m=`+264.03K` | 15m=`+1.49M` | 1h=`-11.21M` | 24h=`-29.42M`
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
  * `2026-10-30 02:53:46 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:14:46 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:00:46 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:59:46 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:59:46 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:59:46 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:46 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:46 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:46 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:46 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:46 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:46 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:46 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:01:46 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 22:01:46 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.9074` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `-0.2929` (Risk Distance: `1.20` pts)
  * +2.5R Take Profit: `3.91`
  * Mathematical Lot Sizing: **`8.33 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.9128` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `2.11` (Risk Distance: `1.20` pts)
  * +2.5R Take Profit: `-2.09`
  * Mathematical Lot Sizing: **`8.33 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.9174`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
