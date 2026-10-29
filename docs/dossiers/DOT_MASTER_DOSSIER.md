# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOT
**Canonical Key**: `DOT` | **Broker Instrument**: `DOTUSD.pi` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-29 21:43:08 IST` (`2026-10-29 16:13:08 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.9890` | **Live Ask Quote**: `1.01` | **Mid Price**: `0.9990`
- **Spread Points**: `20.00` | **Spread BPS**: `200.20 bps` (Charter Threshold: `25.00 bps`)
- **Gate 1 Clearance**: **`SPREAD_DISQUALIFIED`** | **Execution Posture**: `DISQUALIFIED` | **Order Type Allowed**: `NONE`
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
  * Session VWAP: `0.9716` | VWAP Z-Score: `+1.25` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0059` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `63.52` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.01` | Lower -3.00σ Band: `0.9371`
  * Upper +2.51σ Band: `1.00` | Lower -2.51σ Band: `0.9427`
  * Upper +2.01σ Band: `0.9947` | Lower -2.01σ Band: `0.9485`
  * Upper +2.00σ Band: `0.9946` | Lower -2.00σ Band: `0.9486`
  * Upper +1.28σ Band: `0.9863` | Lower -1.28σ Band: `0.9569`
  * Upper +1.00σ Band: `0.9831` | Lower -1.00σ Band: `0.9601`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.9805` | EMA-20=`0.9770` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.9764` (Slope: `+0.0000`) | EMA-100=`0.9804`
  * Institutional Anchors: EMA-144=`0.9830` | EMA-200=`0.9844` (Slope: `-0.0838`) | EMA-233=`0.9849`
- **Range Boundaries**: 24H High=`1.03` | 24H Low=`0.9510` | Weekly High=`1.03` | Weekly Low=`0.9510`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.9852` (Distance: `+1.40%`)
  * Point of Control (POC) = `0.9630` (Distance: `+3.74%`)
  * Value Area Low (VAL) = `0.9539` (Distance: `+4.72%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1.00` | POC=`0.9890` | VAL=`0.9812`
  * Prior Day Extremes: PDH=`1.03` | PDL=`0.9690` | PDC=`1.01`
  * Monday Range Blueprint: High=`1.03` | Mid=`1.01` | Low=`0.9890`
  * Developing Weekly Value Area: Weekly VAH=`1.01` | Weekly POC=`1.01` | Weekly VAL=`0.9779`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1.02` | Low=`0.9510`
  * London Session (08:00-16:00 UTC): High=`0.9850` | Low=`0.9600`
  * New York Session (13:00-21:00 UTC): High=`0.9890` | Low=`0.9680`
  * Initial Balance (First Hour): IB High=`0.9800` | IB Low=`0.9670`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.9950` - `1.00`
  * Optimal Trade Entry (OTE 0.705): `1.00`
  * Structural Invalidation Anchor (0.786): `1.01`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.9969` | `0.9989` | `0.9961` | `0.9979` | `150,796` | 150,416.44 USD | -26,034.05 USD | `-17.31%` | -864,562.09 USD | `-0.50` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.9981` | `0.9993` | `0.9963` | `0.9966` | `139,196` | 138,898.68 USD | -36,121.09 USD | `-26.01%` | -900,683.18 USD | `-0.60` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.9966` | `0.9998` | `0.9946` | `0.9995` | `127,919` | 127,566.53 USD | 39,296.76 USD | `+30.80%` | -861,386.42 USD | `+0.36` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.9963` | `0.9966` | `0.9873` | `0.9930` | `1,009,497` | 999,827.36 USD | 156,509.33 USD | `+15.65%` | -890,452.63 USD | `+1.30` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.9930` | `1.00` | `0.9918` | `0.9969` | `663,960` | 661,501.20 USD | 51,924.59 USD | `+7.85%` | -838,528.04 USD | `+0.34` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.9969` | `0.9998` | `0.9946` | `0.9995` | `417,911` | 416,881.64 USD | -22,858.38 USD | `-5.48%` | -861,386.42 USD | `-0.30` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.9833` | `0.9912` | `0.9787` | `0.9898` | `2,052,215` | 2,020,140.30 USD | -64,907.82 USD | `-3.21%` | -1,209,912.00 USD | `-0.11` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.9898` | `1.00` | `0.9873` | `0.9969` | `2,817,081` | 2,799,350.24 USD | 265,051.20 USD | `+9.47%` | -944,860.80 USD | `+1.05` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.9969` | `0.9998` | `0.9946` | `0.9995` | `417,911` | 416,881.64 USD | -22,858.38 USD | `-5.48%` | -967,719.19 USD | `-0.05` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9699` | `0.9906` | `0.9674` | `0.9732` | `8,505,701` | 8,320,368.15 USD | 13,201.93 USD | `+0.16%` | -1,265,254.30 USD | `+0.50` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9732` | `0.9961` | `0.9713` | `0.9832` | `7,577,906` | 7,454,920.57 USD | 85,064.41 USD | `+1.14%` | -1,180,189.90 USD | `+0.53` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9833` | `1.00` | `0.9787` | `0.9995` | `5,287,208` | 5,236,372.18 USD | 177,285.00 USD | `+3.39%` | -1,002,904.90 USD | `+0.60` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.03` | `1.04` | `1.01` | `1.01` | `8,091,558` | 8,275,924.93 USD | -831,861.35 USD | `-10.05%` | -1,874,272.82 USD | `+1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.01` | `1.01` | `0.9612` | `0.9700` | `15,616,467` | 15,304,422.31 USD | 595,816.59 USD | `+3.89%` | -1,278,456.23 USD | `+1.40` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.9699` | `0.9906` | `0.9674` | `0.9732` | `8,505,701` | 8,320,368.15 USD | 13,201.93 USD | `+0.16%` | -1,265,254.30 USD | `+0.50` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9732` | `0.9961` | `0.9713` | `0.9832` | `7,577,906` | 7,454,920.57 USD | 85,064.41 USD | `+1.14%` | -1,180,189.90 USD | `+0.53` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9833` | `1.00` | `0.9787` | `0.9995` | `5,287,208` | 5,236,372.18 USD | 177,285.00 USD | `+3.39%` | -1,002,904.90 USD | `+0.60` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| --- | **`0.9990`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 19:44:05 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1.01` (Vol: 78,500.00 USD, Dist: `+1.08%`) | Long MP=`0.9649` (Vol: 113,700.00 USD, Dist: `--3.29%`)
  * 48H Horizon: Short MP=`1.01` (Vol: 80,100.00 USD, Dist: `+1.28%`) | Long MP=`0.9510` (Vol: 124,200.00 USD, Dist: `--4.68%`)
  * 3D Horizon: Short MP=`1.05` (Vol: 92,800.00 USD, Dist: `+4.85%`) | Long MP=`0.9510` (Vol: 130,500.00 USD, Dist: `--4.68%`)
  * 7D Horizon: Short MP=`1.07` (Vol: 211,000.00 USD, Dist: `+7.08%`) | Long MP=`0.9606` (Vol: 177,500.00 USD, Dist: `--3.72%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.2485` | 124.25 USD | 542,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3295` | 594.98 USD | 542,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3345` | 738.91 USD | 541,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3645` | 2,080.00 USD | 540,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4185` | 2,790.00 USD | 538,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4695` | 2,580.00 USD | 536,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4905` | 156.62 USD | 533,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4935` | 197.75 USD | 533,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5115` | 809.19 USD | 533,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5125` | 4,130.00 USD | 532,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5165` | 12,600.00 USD | 528,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5465` | 106.84 USD | 515,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5695` | 577.36 USD | 515,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5895` | 137.53 USD | 514,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5955` | 3,390.00 USD | 514,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6025` | 147.37 USD | 511,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6045` | 1,670.00 USD | 511,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6065` | 1,800.00 USD | 509,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6125` | 105.96 USD | 507,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6145` | 147.48 USD | 507,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6225` | 52,910.00 USD | 507,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6245` | 525.77 USD | 454,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6315` | 757.80 USD | 454,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6355` | 106.00 USD | 453,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6415` | 20,270.00 USD | 453,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6465` | 4,230.00 USD | 432,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6475` | 202.47 USD | 428,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6595` | 149.44 USD | 428,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6775` | 423.10 USD | 428,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6825` | 264.67 USD | 427,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6835` | 247.91 USD | 427,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6855` | 2,110.00 USD | 427,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6955` | 1,020.00 USD | 425,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6965` | 155.60 USD | 424,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6975` | 1,430.00 USD | 424,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7055` | 176.38 USD | 422,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7075` | 16,520.00 USD | 422,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7145` | 988.87 USD | 406,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7175` | 322.88 USD | 405,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7205` | 866.26 USD | 404,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7255` | 1,090.00 USD | 403,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7275` | 126.44 USD | 402,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7285` | 291.18 USD | 402,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7305` | 2,300.00 USD | 402,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7335` | 1,140.00 USD | 400,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7395` | 283.30 USD | 398,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7445` | 1,380.00 USD | 398,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7525` | 331.18 USD | 397,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7555` | 2,390.00 USD | 396,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7605` | 834.88 USD | 394,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7725` | 1,580.00 USD | 393,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7865` | 292.03 USD | 392,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7895` | 20,380.00 USD | 391,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7965` | 106.49 USD | 371,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7995` | 120.00 USD | 371,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8025` | 238.90 USD | 371,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8045` | 566.61 USD | 370,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8055` | 699.01 USD | 370,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8135` | 14,110.00 USD | 369,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8215` | 1,950.00 USD | 355,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8285` | 1,890.00 USD | 353,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8325` | 8,990.00 USD | 351,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8365` | 316.70 USD | 342,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8415` | 1,240.00 USD | 342,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8495` | 1,260.00 USD | 341,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8575` | 620.32 USD | 339,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8625` | 309.55 USD | 339,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8635` | 208.02 USD | 339,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8645` | 438.30 USD | 338,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8665` | 118.54 USD | 338,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8710` | 4,990,000.00 USD | 4,990,000.00 USD | 21,960.00 USD | 3,060.00 USD | 6,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8730` | 4,960,000.00 USD | 4,960,000.00 USD | 0.00 USD | 2,120.00 USD | 295.31 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8750` | 4,960,000.00 USD | 4,960,000.00 USD | 0.00 USD | 0.00 USD | 5,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8765` | 171.88 USD | 338,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8770` | 4,950,000.00 USD | 4,950,000.00 USD | 20,650.00 USD | 6,200.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8790` | 4,920,000.00 USD | 4,920,000.00 USD | 873.30 USD | 3,920.00 USD | 2,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8795` | 948.01 USD | 338,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8805` | 41,390.00 USD | 337,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8810` | 2,390,000.00 USD | 2,390,000.00 USD | 9,960.00 USD | 5,740.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8810` | 4,910,000.00 USD | 4,910,000.00 USD | 228.30 USD | 114.50 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8830` | 2,360,000.00 USD | 2,360,000.00 USD | 6,520.00 USD | 3,470.00 USD | 36.19 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8830` | 4,910,000.00 USD | 4,910,000.00 USD | 8,430.00 USD | 5,730.00 USD | 360.61 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8850` | 2,350,000.00 USD | 2,350,000.00 USD | 7,950.00 USD | 1,290.00 USD | 2,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8850` | 4,900,000.00 USD | 4,900,000.00 USD | 8,630.00 USD | 3,210.00 USD | 698.60 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8870` | 2,340,000.00 USD | 2,340,000.00 USD | 6,560.00 USD | 3,430.00 USD | 8,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8870` | 4,880,000.00 USD | 4,880,000.00 USD | 12,220.00 USD | 5,100.00 USD | 6,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8875` | 28,390.00 USD | 295,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8890` | 2,320,000.00 USD | 2,320,000.00 USD | 3,880.00 USD | 3,900.00 USD | 3,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8890` | 4,860,000.00 USD | 4,860,000.00 USD | 17,210.00 USD | 5,370.00 USD | 15,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8910` | 2,310,000.00 USD | 2,310,000.00 USD | 7,750.00 USD | 1,620.00 USD | 4,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8910` | 4,820,000.00 USD | 4,820,000.00 USD | 30,330.00 USD | 7,970.00 USD | 24,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8925` | 526.84 USD | 267,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8930` | 2,300,000.00 USD | 2,300,000.00 USD | 5,380.00 USD | 3,370.00 USD | 4,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8930` | 4,760,000.00 USD | 4,760,000.00 USD | 24,780.00 USD | 7,360.00 USD | 9,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8950` | 2,290,000.00 USD | 2,290,000.00 USD | 2,810.00 USD | 3,490.00 USD | 3,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8950` | 4,720,000.00 USD | 4,720,000.00 USD | 7,380.00 USD | 12,080.00 USD | 27,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8955` | 9,190.00 USD | 266,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8970` | 2,280,000.00 USD | 2,280,000.00 USD | 11,330.00 USD | 5,770.00 USD | 12,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8970` | 4,670,000.00 USD | 4,670,000.00 USD | 43,160.00 USD | 6,690.00 USD | 28,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8990` | 2,250,000.00 USD | 2,250,000.00 USD | 3,820.00 USD | 792.84 USD | 2,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8990` | 4,590,000.00 USD | 4,590,000.00 USD | 51,930.00 USD | 11,550.00 USD | 17,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8995` | 3,820.00 USD | 257,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9010` | 2,240,000.00 USD | 2,240,000.00 USD | 1,310.00 USD | 2,570.00 USD | 806.11 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9010` | 4,510,000.00 USD | 4,510,000.00 USD | 20,170.00 USD | 11,570.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9030` | 2,230,000.00 USD | 2,230,000.00 USD | 5,900.00 USD | 1,300.00 USD | 8,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9030` | 4,470,000.00 USD | 4,470,000.00 USD | 12,700.00 USD | 8,650.00 USD | 21,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9050` | 2,220,000.00 USD | 2,220,000.00 USD | 12,620.00 USD | 2,920.00 USD | 9,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9050` | 4,430,000.00 USD | 4,430,000.00 USD | 35,230.00 USD | 21,830.00 USD | 26,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9070` | 2,190,000.00 USD | 2,190,000.00 USD | 5,360.00 USD | 435.19 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9070` | 4,350,000.00 USD | 4,350,000.00 USD | 29,740.00 USD | 7,690.00 USD | 12,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9090` | 2,190,000.00 USD | 2,190,000.00 USD | 10,750.00 USD | 4,100.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9090` | 4,300,000.00 USD | 4,300,000.00 USD | 13,790.00 USD | 8,050.00 USD | 6,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9095` | 1,150.00 USD | 253,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9110` | 2,170,000.00 USD | 2,170,000.00 USD | 11,100.00 USD | 769.81 USD | 7,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9110` | 4,270,000.00 USD | 4,270,000.00 USD | 8,010.00 USD | 7,760.00 USD | 13,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9130` | 2,150,000.00 USD | 2,150,000.00 USD | 4,590.00 USD | 146.71 USD | 3,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9130` | 4,240,000.00 USD | 4,240,000.00 USD | 26,980.00 USD | 2,110.00 USD | 680.66 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9135` | 143.42 USD | 252,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9150` | 2,140,000.00 USD | 2,140,000.00 USD | 8,880.00 USD | 2,210.00 USD | 8,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9150` | 4,210,000.00 USD | 4,210,000.00 USD | 34,870.00 USD | 10,660.00 USD | 34,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9155` | 1,990.00 USD | 252,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9170` | 2,120,000.00 USD | 2,120,000.00 USD | 3,440.00 USD | 52.38 USD | 398.89 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9170` | 4,130,000.00 USD | 4,130,000.00 USD | 22,610.00 USD | 14,810.00 USD | 18,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9185` | 145.86 USD | 250,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9190` | 2,120,000.00 USD | 2,120,000.00 USD | 2,770.00 USD | 138.43 USD | 186.24 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9190` | 4,080,000.00 USD | 4,080,000.00 USD | 33,980.00 USD | 4,860.00 USD | 19,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9210` | 2,120,000.00 USD | 2,120,000.00 USD | 1,690.00 USD | 48.64 USD | 2,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9210` | 4,020,000.00 USD | 4,020,000.00 USD | 22,070.00 USD | 7,060.00 USD | 15,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9225` | 17,900.00 USD | 250,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9230` | 2,110,000.00 USD | 2,110,000.00 USD | 10,750.00 USD | 2,010.00 USD | 907.53 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9230` | 3,970,000.00 USD | 3,970,000.00 USD | 35,230.00 USD | 11,030.00 USD | 37,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9235` | 282.78 USD | 232,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9250` | 2,100,000.00 USD | 2,100,000.00 USD | 19,910.00 USD | 8,940.00 USD | 14,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9250` | 3,890,000.00 USD | 3,890,000.00 USD | 56,800.00 USD | 9,090.00 USD | 30,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9270` | 2,060,000.00 USD | 2,060,000.00 USD | 15,520.00 USD | 5,450.00 USD | 10,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9270` | 3,790,000.00 USD | 3,790,000.00 USD | 70,300.00 USD | 9,380.00 USD | 21,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9285` | 252.74 USD | 232,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9290` | 2,020,000.00 USD | 2,020,000.00 USD | 25,270.00 USD | 4,390.00 USD | 6,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9290` | 3,690,000.00 USD | 3,690,000.00 USD | 38,760.00 USD | 8,340.00 USD | 31,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9310` | 1,990,000.00 USD | 1,990,000.00 USD | 10,720.00 USD | 12,160.00 USD | 21,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9310` | 3,610,000.00 USD | 3,610,000.00 USD | 26,050.00 USD | 10,070.00 USD | 7,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9330` | 1,940,000.00 USD | 1,940,000.00 USD | 21,790.00 USD | 9,080.00 USD | 9,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9330` | 3,570,000.00 USD | 3,570,000.00 USD | 33,550.00 USD | 9,510.00 USD | 25,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9335` | 361.45 USD | 231,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9350` | 1,900,000.00 USD | 1,900,000.00 USD | 36,480.00 USD | 10,740.00 USD | 13,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9350` | 3,500,000.00 USD | 3,500,000.00 USD | 82,010.00 USD | 29,170.00 USD | 17,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9365` | 7,250.00 USD | 231,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9370` | 1,840,000.00 USD | 1,840,000.00 USD | 38,860.00 USD | 12,720.00 USD | 20,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9370` | 3,370,000.00 USD | 3,370,000.00 USD | 29,580.00 USD | 14,670.00 USD | 7,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9375` | 196.97 USD | 224,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9390` | 1,770,000.00 USD | 1,770,000.00 USD | 18,190.00 USD | 14,310.00 USD | 13,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9390` | 3,320,000.00 USD | 3,320,000.00 USD | 18,750.00 USD | 14,310.00 USD | 12,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9405` | 923.85 USD | 224,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9410` | 1,720,000.00 USD | 1,720,000.00 USD | 35,920.00 USD | 11,320.00 USD | 2,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9410` | 3,280,000.00 USD | 3,280,000.00 USD | 45,790.00 USD | 14,420.00 USD | 4,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9430` | 1,670,000.00 USD | 1,670,000.00 USD | 21,490.00 USD | 8,500.00 USD | 3,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9430` | 3,210,000.00 USD | 3,210,000.00 USD | 53,960.00 USD | 11,100.00 USD | 10,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9445` | 1,060.00 USD | 223,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9450` | 1,640,000.00 USD | 1,640,000.00 USD | 36,530.00 USD | 20,550.00 USD | 40,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9450` | 3,130,000.00 USD | 3,130,000.00 USD | 77,230.00 USD | 33,720.00 USD | 41,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9455` | 106,880.00 USD | 222,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9470` | 1,540,000.00 USD | 1,540,000.00 USD | 45,130.00 USD | 24,810.00 USD | 40,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9470` | 2,980,000.00 USD | 2,980,000.00 USD | 108,210.00 USD | 24,210.00 USD | 50,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9475` | 323.19 USD | 115,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9490` | 1,430,000.00 USD | 1,430,000.00 USD | 88,550.00 USD | 21,030.00 USD | 27,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9490` | 2,800,000.00 USD | 2,800,000.00 USD | 127,990.00 USD | 34,600.00 USD | 113,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9495` | 105,430.00 USD | 115,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9510` | 1,300,000.00 USD | 1,300,000.00 USD | 42,770.00 USD | 30,320.00 USD | 50,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9510` | 2,520,000.00 USD | 2,520,000.00 USD | 198,910.00 USD | 37,040.00 USD | 81,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9515` | 405.62 USD | 9,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9530` | 1,170,000.00 USD | 1,170,000.00 USD | 53,470.00 USD | 24,690.00 USD | 25,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9530` | 2,210,000.00 USD | 2,210,000.00 USD | 79,700.00 USD | 27,690.00 USD | 123,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9550` | 1,070,000.00 USD | 1,070,000.00 USD | 88,250.00 USD | 36,640.00 USD | 46,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9550` | 1,980,000.00 USD | 1,980,000.00 USD | 172,820.00 USD | 90,700.00 USD | 56,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9555` | 2,940.00 USD | 9,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9570` | 898,140.00 USD | 898,140.00 USD | 151,990.00 USD | 48,680.00 USD | 78,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9570` | 1,660,000.00 USD | 1,660,000.00 USD | 129,820.00 USD | 43,030.00 USD | 119,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9575` | 4,690.00 USD | 6,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9585` | 1,530.00 USD | 1,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9590` | 619,330.00 USD | 619,330.00 USD | 45,110.00 USD | 21,430.00 USD | 36,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9590` | 1,360,000.00 USD | 1,360,000.00 USD | 176,280.00 USD | 48,940.00 USD | 66,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9610` | 516,540.00 USD | 516,540.00 USD | 55,850.00 USD | 28,270.00 USD | 8,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9610` | 1,070,000.00 USD | 1,070,000.00 USD | 182,060.00 USD | 77,580.00 USD | 32,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9630` | 424,240.00 USD | 424,240.00 USD | 25,160.00 USD | 12,420.00 USD | 31,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9630` | 778,640.00 USD | 778,640.00 USD | 95,260.00 USD | 281.90 USD | 12,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9650` | 355,010.00 USD | 355,010.00 USD | 25,320.00 USD | 13,150.00 USD | 26,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9650` | 670,690.00 USD | 670,690.00 USD | 64,180.00 USD | 1,120.00 USD | 8,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9670` | 290,380.00 USD | 290,380.00 USD | 21,930.00 USD | 9,620.00 USD | 21,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9670` | 596,630.00 USD | 596,630.00 USD | 11,430.00 USD | 4,400.00 USD | 39,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9690` | 237,240.00 USD | 237,240.00 USD | 37,870.00 USD | 25,560.00 USD | 25,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9690` | 541,240.00 USD | 541,240.00 USD | 3,040.00 USD | 11,390.00 USD | 37,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9710` | 148,720.00 USD | 148,720.00 USD | 24,610.00 USD | 12,350.00 USD | 11,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9710` | 489,600.00 USD | 489,600.00 USD | 64,680.00 USD | 619.85 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9730` | 100,520.00 USD | 100,520.00 USD | 10,120.00 USD | 0.00 USD | 7,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9730` | 424,310.00 USD | 424,310.00 USD | 0.00 USD | 0.00 USD | 7,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9750` | 82,960.00 USD | 82,960.00 USD | 10,430.00 USD | 12,660.00 USD | 3,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9750` | 416,800.00 USD | 416,800.00 USD | 0.00 USD | 16,590.00 USD | 2,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9770` | 56,320.00 USD | 56,320.00 USD | 22,490.00 USD | 2,870.00 USD | 6,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9770` | 397,930.00 USD | 397,930.00 USD | 0.00 USD | 0.00 USD | 13,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9790` | 24,230.00 USD | 24,230.00 USD | 819.00 USD | 3,600.00 USD | 1,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9790` | 384,520.00 USD | 384,520.00 USD | 0.00 USD | 0.00 USD | 77,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9810` | 17,820.00 USD | 17,820.00 USD | 0.00 USD | 0.00 USD | 1,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9810` | 306,800.00 USD | 306,800.00 USD | 7,900.00 USD | 0.00 USD | 132,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9830` | 165,950.00 USD | 165,950.00 USD | 2,190.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9850` | 16,560.00 USD | 16,560.00 USD | 575.70 USD | 0.00 USD | 518.30 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9850` | 163,750.00 USD | 163,750.00 USD | 0.00 USD | 16,440.00 USD | 22,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9930` | 15,460.00 USD | 15,460.00 USD | 0.00 USD | 13,250.00 USD | 601.92 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9930` | 125,230.00 USD | 125,230.00 USD | 0.00 USD | 0.00 USD | 1,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9950` | 124,010.00 USD | 124,010.00 USD | 16,510.00 USD | 0.00 USD | 42,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9970` | 1,610.00 USD | 1,610.00 USD | 0.00 USD | 0.00 USD | 1,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9970` | 64,730.00 USD | 64,730.00 USD | 38,220.00 USD | 0.00 USD | 26,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9990` | 46,130.00 USD | 46,130.00 USD | 37,100.00 USD | 0.00 USD | 9,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9990` | 92,250.00 USD | 92,250.00 USD | 37,100.00 USD | 0.00 USD | 9,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9990` | 7,090.00 USD | 7,090.00 USD | 0.00 USD | 0.00 USD | 7,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 173,660.00 USD | 173,660.00 USD | 49,050.00 USD | 25,560.00 USD | 6,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 88,130.00 USD | 88,130.00 USD | 52,850.00 USD | 27,670.00 USD | 514.14 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 274,600.00 USD | 274,600.00 USD | 50,360.00 USD | 23,660.00 USD | 26,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 168,950.00 USD | 168,950.00 USD | 53,480.00 USD | 3,250.00 USD | 24,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 393,050.00 USD | 393,050.00 USD | 43,090.00 USD | 27,900.00 USD | 47,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 320,570.00 USD | 320,570.00 USD | 109,050.00 USD | 19,310.00 USD | 23,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 487,620.00 USD | 487,620.00 USD | 51,770.00 USD | 17,570.00 USD | 25,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 386,360.00 USD | 386,360.00 USD | 17,210.00 USD | 3,900.00 USD | 44,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 642,790.00 USD | 642,790.00 USD | 75,340.00 USD | 35,830.00 USD | 44,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 493,240.00 USD | 493,240.00 USD | 52,580.00 USD | 16,040.00 USD | 38,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 731,130.00 USD | 731,130.00 USD | 46,500.00 USD | 21,340.00 USD | 20,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 613,130.00 USD | 613,130.00 USD | 72,420.00 USD | 110.10 USD | 47,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 828,370.00 USD | 828,370.00 USD | 58,820.00 USD | 18,230.00 USD | 20,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 718,690.00 USD | 718,690.00 USD | 51,030.00 USD | 34,770.00 USD | 19,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 943,820.00 USD | 943,820.00 USD | 54,330.00 USD | 33,250.00 USD | 27,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 771,170.00 USD | 771,170.00 USD | 18,600.00 USD | 26,360.00 USD | 7,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 1,020,000.00 USD | 1,020,000.00 USD | 40,370.00 USD | 17,040.00 USD | 19,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 800,100.00 USD | 800,100.00 USD | 4,160.00 USD | 16,300.00 USD | 8,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 1,090,000.00 USD | 1,090,000.00 USD | 39,470.00 USD | 20,470.00 USD | 4,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 1,170,000.00 USD | 1,170,000.00 USD | 306,990.00 USD | 60,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 1,140,000.00 USD | 1,140,000.00 USD | 33,060.00 USD | 13,660.00 USD | 6,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 1,340,000.00 USD | 1,340,000.00 USD | 76,830.00 USD | 25,870.00 USD | 67,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 1,220,000.00 USD | 1,220,000.00 USD | 40,700.00 USD | 15,440.00 USD | 23,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 1,600,000.00 USD | 1,600,000.00 USD | 56,570.00 USD | 85,890.00 USD | 124,660.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.02` | 104.70 USD | 104.70 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.02` | 1,330,000.00 USD | 1,330,000.00 USD | 42,950.00 USD | 33,190.00 USD | 38,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 1,690,000.00 USD | 1,690,000.00 USD | 11,270.00 USD | 48,490.00 USD | 28,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 1,360,000.00 USD | 1,360,000.00 USD | 12,950.00 USD | 201.13 USD | 16,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 1,940,000.00 USD | 1,940,000.00 USD | 120,780.00 USD | 109,850.00 USD | 12,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 1,440,000.00 USD | 1,440,000.00 USD | 26,960.00 USD | 22,680.00 USD | 28,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 2,140,000.00 USD | 2,140,000.00 USD | 141,540.00 USD | 38,750.00 USD | 21,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 1,560,000.00 USD | 1,560,000.00 USD | 81,210.00 USD | 14,130.00 USD | 20,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 2,300,000.00 USD | 2,300,000.00 USD | 160,920.00 USD | 118.80 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 1,620,000.00 USD | 1,620,000.00 USD | 48,750.00 USD | 104.84 USD | 11,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 2,420,000.00 USD | 2,420,000.00 USD | 122,520.00 USD | 95.00 USD | 3,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 1,710,000.00 USD | 1,710,000.00 USD | 33,320.00 USD | 21,990.00 USD | 31,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 2,740,000.00 USD | 2,740,000.00 USD | 259,060.00 USD | 8,290.00 USD | 42,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 1,880,000.00 USD | 1,880,000.00 USD | 82,440.00 USD | 16,480.00 USD | 77,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 3,000,000.00 USD | 3,000,000.00 USD | 161,430.00 USD | 430.60 USD | 100,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 1,910,000.00 USD | 1,910,000.00 USD | 6,030.00 USD | 2,410.00 USD | 16,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 3,350,000.00 USD | 3,350,000.00 USD | 239,200.00 USD | 1,390.00 USD | 111,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 1,920,000.00 USD | 1,920,000.00 USD | 7,030.00 USD | 4,350.00 USD | 3,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 3,790,000.00 USD | 3,790,000.00 USD | 276,890.00 USD | 1,930.00 USD | 159,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 1,980,000.00 USD | 1,980,000.00 USD | 10,800.00 USD | 6,840.00 USD | 41,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 3,970,000.00 USD | 3,970,000.00 USD | 49,280.00 USD | 32,550.00 USD | 103,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 2,040,000.00 USD | 2,040,000.00 USD | 20,200.00 USD | 14,780.00 USD | 23,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 4,240,000.00 USD | 4,240,000.00 USD | 184,670.00 USD | 23,650.00 USD | 59,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 2,080,000.00 USD | 2,080,000.00 USD | 26,860.00 USD | 2,490.00 USD | 8,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 4,720,000.00 USD | 4,720,000.00 USD | 157,820.00 USD | 87,820.00 USD | 232,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 2,100,000.00 USD | 2,100,000.00 USD | 2,380.00 USD | 9,760.00 USD | 11,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 4,930,000.00 USD | 4,930,000.00 USD | 116,030.00 USD | 13,780.00 USD | 76,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 2,150,000.00 USD | 2,150,000.00 USD | 33,040.00 USD | 4,170.00 USD | 12,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 5,220,000.00 USD | 5,220,000.00 USD | 175,210.00 USD | 43,570.00 USD | 77,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 2,200,000.00 USD | 2,200,000.00 USD | 16,160.00 USD | 5,850.00 USD | 23,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 5,420,000.00 USD | 5,420,000.00 USD | 63,760.00 USD | 55,700.00 USD | 74,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 2,230,000.00 USD | 2,230,000.00 USD | 11,080.00 USD | 111.54 USD | 24,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 5,650,000.00 USD | 5,650,000.00 USD | 130,860.00 USD | 33,660.00 USD | 72,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 2,260,000.00 USD | 2,260,000.00 USD | 6,040.00 USD | 5,180.00 USD | 20,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 6,050,000.00 USD | 6,050,000.00 USD | 220,920.00 USD | 69,780.00 USD | 106,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 2,290,000.00 USD | 2,290,000.00 USD | 14,940.00 USD | 2,920.00 USD | 13,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 6,480,000.00 USD | 6,480,000.00 USD | 216,930.00 USD | 71,180.00 USD | 138,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 2,310,000.00 USD | 2,310,000.00 USD | 1,840.00 USD | 7,520.00 USD | 10,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 6,740,000.00 USD | 6,740,000.00 USD | 130,860.00 USD | 56,310.00 USD | 78,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 2,320,000.00 USD | 2,320,000.00 USD | 4,200.00 USD | 2,700.00 USD | 2,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 7,030,000.00 USD | 7,030,000.00 USD | 140,340.00 USD | 73,690.00 USD | 71,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 2,340,000.00 USD | 2,340,000.00 USD | 7,120.00 USD | 3,880.00 USD | 9,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 7,230,000.00 USD | 7,230,000.00 USD | 89,920.00 USD | 28,390.00 USD | 83,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 2,370,000.00 USD | 2,370,000.00 USD | 13,470.00 USD | 4,690.00 USD | 6,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 7,440,000.00 USD | 7,440,000.00 USD | 85,780.00 USD | 43,390.00 USD | 82,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 2,390,000.00 USD | 2,390,000.00 USD | 6,530.00 USD | 3,920.00 USD | 6,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 7,740,000.00 USD | 7,740,000.00 USD | 219,670.00 USD | 14,280.00 USD | 62,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 2,410,000.00 USD | 2,410,000.00 USD | 16,590.00 USD | 3,050.00 USD | 4,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 7,970,000.00 USD | 7,970,000.00 USD | 141,570.00 USD | 36,430.00 USD | 52,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 2,430,000.00 USD | 2,430,000.00 USD | 6,130.00 USD | 4,250.00 USD | 12,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 8,210,000.00 USD | 8,210,000.00 USD | 101,980.00 USD | 42,960.00 USD | 95,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 2,450,000.00 USD | 2,450,000.00 USD | 4,510.00 USD | 5,370.00 USD | 10,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 8,390,000.00 USD | 8,390,000.00 USD | 97,650.00 USD | 27,480.00 USD | 60,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 2,470,000.00 USD | 2,470,000.00 USD | 8,480.00 USD | 3,420.00 USD | 5,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 8,550,000.00 USD | 8,550,000.00 USD | 75,040.00 USD | 29,850.00 USD | 48,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 2,480,000.00 USD | 2,480,000.00 USD | 7,340.00 USD | 3,590.00 USD | 36.19 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 8,790,000.00 USD | 8,790,000.00 USD | 165,660.00 USD | 21,060.00 USD | 52,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 2,490,000.00 USD | 2,490,000.00 USD | 8,690.00 USD | 1,430.00 USD | 2,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 9,010,000.00 USD | 9,010,000.00 USD | 164,440.00 USD | 23,690.00 USD | 33,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 2,500,000.00 USD | 2,500,000.00 USD | 2,120.00 USD | 3,000.00 USD | 2,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 9,210,000.00 USD | 9,210,000.00 USD | 61,330.00 USD | 41,110.00 USD | 100,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 2,510,000.00 USD | 2,510,000.00 USD | 5,310.00 USD | 3,010.00 USD | 6,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 9,350,000.00 USD | 9,350,000.00 USD | 78,840.00 USD | 18,540.00 USD | 46,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 2,530,000.00 USD | 2,530,000.00 USD | 4,520.00 USD | 4,080.00 USD | 3,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 9,590,000.00 USD | 9,590,000.00 USD | 102,510.00 USD | 58,170.00 USD | 69,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 2,540,000.00 USD | 2,540,000.00 USD | 8,330.00 USD | 1,690.00 USD | 4,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 9,760,000.00 USD | 9,760,000.00 USD | 71,650.00 USD | 20,280.00 USD | 85,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 2,550,000.00 USD | 2,550,000.00 USD | 5,680.00 USD | 3,430.00 USD | 4,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 9,890,000.00 USD | 9,890,000.00 USD | 70,660.00 USD | 25,660.00 USD | 32,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 2,570,000.00 USD | 2,570,000.00 USD | 2,940.00 USD | 3,620.00 USD | 3,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 10,110,000.00 USD | 10,110,000.00 USD | 92,880.00 USD | 39,220.00 USD | 81,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 2,570,000.00 USD | 2,570,000.00 USD | 2,130.00 USD | 3,070.00 USD | 53.55 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 10,310,000.00 USD | 10,310,000.00 USD | 66,930.00 USD | 44,010.00 USD | 92,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.10` | 2,600,000.00 USD | 2,600,000.00 USD | 9,890.00 USD | 2,730.00 USD | 12,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 10,500,000.00 USD | 10,500,000.00 USD | 88,590.00 USD | 58,180.00 USD | 40,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.10` | 2,600,000.00 USD | 2,600,000.00 USD | 574.37 USD | 811.13 USD | 2,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 10,860,000.00 USD | 10,860,000.00 USD | 198,530.00 USD | 64,000.00 USD | 101,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.10` | 2,600,000.00 USD | 2,600,000.00 USD | 1,420.00 USD | 2,510.00 USD | 656.98 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 11,050,000.00 USD | 11,050,000.00 USD | 122,300.00 USD | 43,880.00 USD | 26,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.10` | 2,620,000.00 USD | 2,620,000.00 USD | 3,150.00 USD | 1,240.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 11,260,000.00 USD | 11,260,000.00 USD | 83,370.00 USD | 17,940.00 USD | 100,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.10` | 68,420.00 USD | 68,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.10` | 11,290,000.00 USD | 11,290,000.00 USD | 25,460.00 USD | 9,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.11` | 169.86 USD | 68,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.18` | 228.40 USD | 68,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.18` | 2,780.00 USD | 71,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.19` | 22,180.00 USD | 93,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.32` | 11,730.00 USD | 105,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.34` | 389.93 USD | 106,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.36` | 1,370.00 USD | 107,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.42` | 4,330.00 USD | 111,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.49` | 513,610.00 USD | 625,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.50` | 219.67 USD | 625,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.52` | 232.49 USD | 625,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.53` | 293.13 USD | 626,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 176.31 USD | 626,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 9,590.00 USD | 635,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.64` | 762.12 USD | 636,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 300.15 USD | 636,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.69` | 106,690.00 USD | 743,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.73` | 2,670.00 USD | 746,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.73` | 86,310.00 USD | 832,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.86` | 208.37 USD | 832,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.90` | 181.78 USD | 832,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.97` | 2,950.00 USD | 835,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.99` | 1,610.00 USD | 837,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.2485` | 542,440.00 USD | 0.00 USD | 124.25 USD | `-75.09%` | `500.00` |
| `Live` | `Long` | `0.3295` | 542,320.00 USD | 0.00 USD | 594.98 USD | `-66.97%` | `1,805.70` |
| `Live` | `Long` | `0.3345` | 541,720.00 USD | 0.00 USD | 738.91 USD | `-66.47%` | `2,209.00` |
| `Live` | `Long` | `0.3645` | 540,980.00 USD | 0.00 USD | 2,080.00 USD | `-63.47%` | `5,698.80` |
| `Live` | `Long` | `0.4185` | 538,900.00 USD | 0.00 USD | 2,790.00 USD | `-58.05%` | `6,675.20` |
| `Live` | `Long` | `0.4695` | 536,110.00 USD | 0.00 USD | 2,580.00 USD | `-52.94%` | `5,500.00` |
| `Live` | `Long` | `0.4905` | 533,530.00 USD | 0.00 USD | 156.62 USD | `-50.84%` | `319.30` |
| `Live` | `Long` | `0.4935` | 533,370.00 USD | 0.00 USD | 197.75 USD | `-50.54%` | `400.70` |
| `Live` | `Long` | `0.5115` | 533,170.00 USD | 0.00 USD | 809.19 USD | `-48.73%` | `1,582.00` |
| `Live` | `Long` | `0.5125` | 532,360.00 USD | 0.00 USD | 4,130.00 USD | `-48.63%` | `8,067.10` |
| `Live` | `Long` | `0.5165` | 528,230.00 USD | 0.00 USD | 12,600.00 USD | `-48.23%` | `24,390.20` |
| `Live` | `Long` | `0.5465` | 515,630.00 USD | 0.00 USD | 106.84 USD | `-45.22%` | `195.50` |
| `Live` | `Long` | `0.5695` | 515,530.00 USD | 0.00 USD | 577.36 USD | `-42.92%` | `1,013.80` |
| `Live` | `Long` | `0.5895` | 514,950.00 USD | 0.00 USD | 137.53 USD | `-40.91%` | `233.30` |
| `Live` | `Long` | `0.5955` | 514,810.00 USD | 0.00 USD | 3,390.00 USD | `-40.31%` | `5,695.60` |
| `Live` | `Long` | `0.6025` | 511,420.00 USD | 0.00 USD | 147.37 USD | `-39.61%` | `244.60` |
| `Live` | `Long` | `0.6045` | 511,270.00 USD | 0.00 USD | 1,670.00 USD | `-39.41%` | `2,761.80` |
| `Live` | `Long` | `0.6065` | 509,600.00 USD | 0.00 USD | 1,800.00 USD | `-39.21%` | `2,971.80` |
| `Live` | `Long` | `0.6125` | 507,800.00 USD | 0.00 USD | 105.96 USD | `-38.61%` | `173.00` |
| `Live` | `Long` | `0.6145` | 507,690.00 USD | 0.00 USD | 147.48 USD | `-38.41%` | `240.00` |
| `Live` | `Long` | `0.6225` | 507,550.00 USD | 0.00 USD | 52,910.00 USD | `-37.61%` | `85,000.00` |
| `Live` | `Long` | `0.6245` | 454,630.00 USD | 0.00 USD | 525.77 USD | `-37.41%` | `841.90` |
| `Live` | `Long` | `0.6315` | 454,110.00 USD | 0.00 USD | 757.80 USD | `-36.70%` | `1,200.00` |
| `Live` | `Long` | `0.6355` | 453,350.00 USD | 0.00 USD | 106.00 USD | `-36.30%` | `166.80` |
| `Live` | `Long` | `0.6415` | 453,240.00 USD | 0.00 USD | 20,270.00 USD | `-35.70%` | `31,595.60` |
| `Live` | `Long` | `0.6465` | 432,980.00 USD | 0.00 USD | 4,230.00 USD | `-35.20%` | `6,539.70` |
| `Live` | `Long` | `0.6475` | 428,750.00 USD | 0.00 USD | 202.47 USD | `-35.10%` | `312.70` |
| `Live` | `Long` | `0.6595` | 428,550.00 USD | 0.00 USD | 149.44 USD | `-33.90%` | `226.60` |
| `Live` | `Long` | `0.6775` | 428,400.00 USD | 0.00 USD | 423.10 USD | `-32.09%` | `624.50` |
| `Live` | `Long` | `0.6825` | 427,970.00 USD | 0.00 USD | 264.67 USD | `-31.59%` | `387.80` |
| `Live` | `Long` | `0.6835` | 427,710.00 USD | 0.00 USD | 247.91 USD | `-31.49%` | `362.70` |
| `Live` | `Long` | `0.6855` | 427,460.00 USD | 0.00 USD | 2,110.00 USD | `-31.29%` | `3,075.70` |
| `Live` | `Long` | `0.6955` | 425,350.00 USD | 0.00 USD | 1,020.00 USD | `-30.29%` | `1,463.20` |
| `Live` | `Long` | `0.6965` | 424,330.00 USD | 0.00 USD | 155.60 USD | `-30.19%` | `223.40` |
| `Live` | `Long` | `0.6975` | 424,180.00 USD | 0.00 USD | 1,430.00 USD | `-30.09%` | `2,047.90` |
| `Live` | `Long` | `0.7055` | 422,750.00 USD | 0.00 USD | 176.38 USD | `-29.29%` | `250.00` |
| `Live` | `Long` | `0.7075` | 422,570.00 USD | 0.00 USD | 16,520.00 USD | `-29.09%` | `23,344.30` |
| `Live` | `Long` | `0.7145` | 406,060.00 USD | 0.00 USD | 988.87 USD | `-28.38%` | `1,384.00` |
| `Live` | `Long` | `0.7175` | 405,070.00 USD | 0.00 USD | 322.88 USD | `-28.08%` | `450.00` |
| `Live` | `Long` | `0.7205` | 404,750.00 USD | 0.00 USD | 866.26 USD | `-27.78%` | `1,202.30` |
| `Live` | `Long` | `0.7255` | 403,880.00 USD | 0.00 USD | 1,090.00 USD | `-27.28%` | `1,500.00` |
| `Live` | `Long` | `0.7275` | 402,790.00 USD | 0.00 USD | 126.44 USD | `-27.08%` | `173.80` |
| `Live` | `Long` | `0.7285` | 402,670.00 USD | 0.00 USD | 291.18 USD | `-26.98%` | `399.70` |
| `Live` | `Long` | `0.7305` | 402,370.00 USD | 0.00 USD | 2,300.00 USD | `-26.78%` | `3,143.00` |
| `Live` | `Long` | `0.7335` | 400,080.00 USD | 0.00 USD | 1,140.00 USD | `-26.48%` | `1,557.80` |
| `Live` | `Long` | `0.7395` | 398,940.00 USD | 0.00 USD | 283.30 USD | `-25.88%` | `383.10` |
| `Live` | `Long` | `0.7445` | 398,650.00 USD | 0.00 USD | 1,380.00 USD | `-25.38%` | `1,859.90` |
| `Live` | `Long` | `0.7525` | 397,270.00 USD | 0.00 USD | 331.18 USD | `-24.58%` | `440.10` |
| `Live` | `Long` | `0.7555` | 396,940.00 USD | 0.00 USD | 2,390.00 USD | `-24.28%` | `3,161.00` |
| `Live` | `Long` | `0.7605` | 394,550.00 USD | 0.00 USD | 834.88 USD | `-23.77%` | `1,097.80` |
| `Live` | `Long` | `0.7725` | 393,710.00 USD | 0.00 USD | 1,580.00 USD | `-22.57%` | `2,046.10` |
| `Live` | `Long` | `0.7865` | 392,130.00 USD | 0.00 USD | 292.03 USD | `-21.17%` | `371.30` |
| `Live` | `Long` | `0.7895` | 391,840.00 USD | 0.00 USD | 20,380.00 USD | `-20.87%` | `25,816.60` |
| `Live` | `Long` | `0.7965` | 371,460.00 USD | 0.00 USD | 106.49 USD | `-20.17%` | `133.70` |
| `Live` | `Long` | `0.7995` | 371,350.00 USD | 0.00 USD | 120.00 USD | `-19.86%` | `150.10` |
| `Live` | `Long` | `0.8025` | 371,230.00 USD | 0.00 USD | 238.90 USD | `-19.56%` | `297.70` |
| `Live` | `Long` | `0.8045` | 370,990.00 USD | 0.00 USD | 566.61 USD | `-19.36%` | `704.30` |
| `Live` | `Long` | `0.8055` | 370,430.00 USD | 0.00 USD | 699.01 USD | `-19.26%` | `867.80` |
| `Live` | `Long` | `0.8135` | 369,730.00 USD | 0.00 USD | 14,110.00 USD | `-18.46%` | `17,340.90` |
| `Live` | `Long` | `0.8215` | 355,620.00 USD | 0.00 USD | 1,950.00 USD | `-17.66%` | `2,370.70` |
| `Live` | `Long` | `0.8285` | 353,670.00 USD | 0.00 USD | 1,890.00 USD | `-16.96%` | `2,283.30` |
| `Live` | `Long` | `0.8325` | 351,780.00 USD | 0.00 USD | 8,990.00 USD | `-16.56%` | `10,795.60` |
| `Live` | `Long` | `0.8365` | 342,790.00 USD | 0.00 USD | 316.70 USD | `-16.16%` | `378.60` |
| `Live` | `Long` | `0.8415` | 342,480.00 USD | 0.00 USD | 1,240.00 USD | `-15.66%` | `1,469.60` |
| `Live` | `Long` | `0.8495` | 341,240.00 USD | 0.00 USD | 1,260.00 USD | `-14.85%` | `1,486.90` |
| `Live` | `Long` | `0.8575` | 339,980.00 USD | 0.00 USD | 620.32 USD | `-14.05%` | `723.40` |
| `Live` | `Long` | `0.8625` | 339,360.00 USD | 0.00 USD | 309.55 USD | `-13.55%` | `358.90` |
| `Live` | `Long` | `0.8635` | 339,050.00 USD | 0.00 USD | 208.02 USD | `-13.45%` | `240.90` |
| `Live` | `Long` | `0.8645` | 338,840.00 USD | 0.00 USD | 438.30 USD | `-13.35%` | `507.00` |
| `Live` | `Long` | `0.8665` | 338,400.00 USD | 0.00 USD | 118.54 USD | `-13.15%` | `136.80` |
| `Live` | `Long` | `0.8765` | 338,280.00 USD | 0.00 USD | 171.88 USD | `-12.15%` | `196.10` |
| `Live` | `Long` | `0.8795` | 338,110.00 USD | 0.00 USD | 948.01 USD | `-11.85%` | `1,077.90` |
| `Live` | `Long` | `0.8805` | 337,160.00 USD | 0.00 USD | 41,390.00 USD | `-11.75%` | `47,002.60` |
| `Live` | `Long` | `0.8875` | 295,780.00 USD | 0.00 USD | 28,390.00 USD | `-11.04%` | `31,994.10` |
| `Live` | `Long` | `0.8925` | 267,380.00 USD | 0.00 USD | 526.84 USD | `-10.54%` | `590.30` |
| `Live` | `Long` | `0.8955` | 266,860.00 USD | 0.00 USD | 9,190.00 USD | `-10.24%` | `10,267.00` |
| `Live` | `Long` | `0.8995` | 257,660.00 USD | 0.00 USD | 3,820.00 USD | `-9.84%` | `4,250.30` |
| `Live` | `Long` | `0.9095` | 253,840.00 USD | 0.00 USD | 1,150.00 USD | `-8.84%` | `1,259.00` |
| `Live` | `Long` | `0.9135` | 252,690.00 USD | 0.00 USD | 143.42 USD | `-8.44%` | `157.00` |
| `Live` | `Long` | `0.9155` | 252,550.00 USD | 0.00 USD | 1,990.00 USD | `-8.24%` | `2,169.50` |
| `Live` | `Long` | `0.9185` | 250,560.00 USD | 0.00 USD | 145.86 USD | `-7.94%` | `158.80` |
| `Live` | `Long` | `0.9225` | 250,420.00 USD | 0.00 USD | 17,900.00 USD | `-7.54%` | `19,401.30` |
| `Live` | `Long` | `0.9235` | 232,520.00 USD | 0.00 USD | 282.78 USD | `-7.44%` | `306.20` |
| `Live` | `Long` | `0.9285` | 232,240.00 USD | 0.00 USD | 252.74 USD | `-6.94%` | `272.20` |
| `Live` | `Long` | `0.9335` | 231,980.00 USD | 0.00 USD | 361.45 USD | `-6.43%` | `387.20` |
| `Live` | `Long` | `0.9365` | 231,620.00 USD | 0.00 USD | 7,250.00 USD | `-6.13%` | `7,739.40` |
| `Live` | `Long` | `0.9375` | 224,380.00 USD | 0.00 USD | 196.97 USD | `-6.03%` | `210.10` |
| `Live` | `Long` | `0.9405` | 224,180.00 USD | 0.00 USD | 923.85 USD | `-5.73%` | `982.30` |
| `Live` | `Long` | `0.9445` | 223,250.00 USD | 0.00 USD | 1,060.00 USD | `-5.33%` | `1,117.80` |
| `Live` | `Long` | `0.9455` | 222,200.00 USD | 0.00 USD | 106,880.00 USD | `-5.23%` | `113,040.20` |
| `Live` | `Long` | `0.9475` | 115,320.00 USD | 0.00 USD | 323.19 USD | `-5.03%` | `341.10` |
| `Live` | `Long` | `0.9495` | 115,000.00 USD | 0.00 USD | 105,430.00 USD | `-4.83%` | `111,034.60` |
| `Live` | `Long` | `0.9515` | 9,570.00 USD | 0.00 USD | 405.62 USD | `-4.63%` | `426.30` |
| `Live` | `Long` | `0.9555` | 9,160.00 USD | 0.00 USD | 2,940.00 USD | `-4.23%` | `3,075.40` |
| `Live` | `Long` | `0.9575` | 6,220.00 USD | 0.00 USD | 4,690.00 USD | `-4.03%` | `4,898.90` |
| `Live` | `Long` | `0.9585` | 1,530.00 USD | 0.00 USD | 1,530.00 USD | `-3.93%` | `1,600.00` |
| `Live` | `Short` | `1.02` | 104.70 USD | 104.70 USD | 0.00 USD | `+2.59%` | `102.30` |
| `Live` | `Short` | `1.10` | 68,520.00 USD | 68,420.00 USD | 0.00 USD | `+10.61%` | `62,000.00` |
| `Live` | `Short` | `1.11` | 68,690.00 USD | 169.86 USD | 0.00 USD | `+11.21%` | `153.10` |
| `Live` | `Short` | `1.18` | 68,920.00 USD | 228.40 USD | 0.00 USD | `+17.82%` | `194.30` |
| `Live` | `Short` | `1.18` | 71,700.00 USD | 2,780.00 USD | 0.00 USD | `+18.52%` | `2,347.60` |
| `Live` | `Short` | `1.19` | 93,880.00 USD | 22,180.00 USD | 0.00 USD | `+19.13%` | `18,664.00` |
| `Live` | `Short` | `1.32` | 105,610.00 USD | 11,730.00 USD | 0.00 USD | `+32.66%` | `8,862.90` |
| `Live` | `Short` | `1.34` | 106,000.00 USD | 389.93 USD | 0.00 USD | `+34.26%` | `291.10` |
| `Live` | `Short` | `1.36` | 107,370.00 USD | 1,370.00 USD | 0.00 USD | `+36.77%` | `1,002.70` |
| `Live` | `Short` | `1.42` | 111,690.00 USD | 4,330.00 USD | 0.00 USD | `+42.28%` | `3,049.30` |
| `Live` | `Short` | `1.49` | 625,300.00 USD | 513,610.00 USD | 0.00 USD | `+49.19%` | `345,051.20` |
| `Live` | `Short` | `1.50` | 625,520.00 USD | 219.67 USD | 0.00 USD | `+50.50%` | `146.30` |
| `Live` | `Short` | `1.52` | 625,760.00 USD | 232.49 USD | 0.00 USD | `+52.80%` | `152.50` |
| `Live` | `Short` | `1.53` | 626,050.00 USD | 293.13 USD | 0.00 USD | `+53.10%` | `191.90` |
| `Live` | `Short` | `1.54` | 626,230.00 USD | 176.31 USD | 0.00 USD | `+54.61%` | `114.30` |
| `Live` | `Short` | `1.56` | 635,820.00 USD | 9,590.00 USD | 0.00 USD | `+56.01%` | `6,161.90` |
| `Live` | `Short` | `1.64` | 636,580.00 USD | 762.12 USD | 0.00 USD | `+64.63%` | `464.00` |
| `Live` | `Short` | `1.67` | 636,880.00 USD | 300.15 USD | 0.00 USD | `+67.14%` | `180.00` |
| `Live` | `Short` | `1.69` | 743,570.00 USD | 106,690.00 USD | 0.00 USD | `+69.84%` | `62,962.50` |
| `Live` | `Short` | `1.73` | 746,240.00 USD | 2,670.00 USD | 0.00 USD | `+73.35%` | `1,542.20` |
| `Live` | `Short` | `1.73` | 832,540.00 USD | 86,310.00 USD | 0.00 USD | `+73.85%` | `49,759.80` |
| `Live` | `Short` | `1.86` | 832,750.00 USD | 208.37 USD | 0.00 USD | `+85.98%` | `112.30` |
| `Live` | `Short` | `1.90` | 832,930.00 USD | 181.78 USD | 0.00 USD | `+90.39%` | `95.70` |
| `Live` | `Short` | `1.97` | 835,890.00 USD | 2,950.00 USD | 0.00 USD | `+97.41%` | `1,500.00` |
| `Live` | `Short` | `1.99` | 837,500.00 USD | 1,610.00 USD | 0.00 USD | `+99.31%` | `808.40` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.4015` | 605,670.00 USD | 0.00 USD | 120.45 USD | `-59.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 605,540.00 USD | 0.00 USD | 150.15 USD | `-49.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7005` | 605,390.00 USD | 0.00 USD | 781.90 USD | `-29.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7105` | 604,610.00 USD | 0.00 USD | 477.38 USD | `-28.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7195` | 604,140.00 USD | 0.00 USD | 341.33 USD | `-27.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7205` | 603,790.00 USD | 0.00 USD | 972.82 USD | `-27.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7305` | 602,820.00 USD | 0.00 USD | 160.20 USD | `-26.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7465` | 602,660.00 USD | 0.00 USD | 289.49 USD | `-25.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7805` | 602,370.00 USD | 0.00 USD | 14,570.00 USD | `-21.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7965` | 587,800.00 USD | 0.00 USD | 274,830.00 USD | `-20.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8115` | 312,970.00 USD | 0.00 USD | 405.75 USD | `-18.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8365` | 312,570.00 USD | 0.00 USD | 772.84 USD | `-16.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8505` | 311,790.00 USD | 0.00 USD | 9,180.00 USD | `-14.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8555` | 302,610.00 USD | 0.00 USD | 341.94 USD | `-14.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8565` | 302,270.00 USD | 0.00 USD | 1,150.00 USD | `-14.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8575` | 301,120.00 USD | 0.00 USD | 2,020.00 USD | `-14.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8585` | 299,110.00 USD | 0.00 USD | 429.25 USD | `-13.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8605` | 298,680.00 USD | 0.00 USD | 1,290.00 USD | `-13.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8665` | 297,390.00 USD | 0.00 USD | 518.51 USD | `-13.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8865` | 296,870.00 USD | 0.00 USD | 223.04 USD | `-11.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8875` | 296,640.00 USD | 0.00 USD | 401.86 USD | `-11.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8895` | 296,240.00 USD | 0.00 USD | 158.51 USD | `-10.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8925` | 296,080.00 USD | 0.00 USD | 293.81 USD | `-10.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9085` | 295,790.00 USD | 0.00 USD | 492.41 USD | `-8.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9155` | 295,300.00 USD | 0.00 USD | 869.27 USD | `-8.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9165` | 294,430.00 USD | 0.00 USD | 274.77 USD | `-8.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9205` | 294,150.00 USD | 0.00 USD | 1,480.00 USD | `-7.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9255` | 292,680.00 USD | 0.00 USD | 1,010.00 USD | `-7.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9275` | 291,660.00 USD | 0.00 USD | 2,120.00 USD | `-7.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9285` | 289,550.00 USD | 0.00 USD | 246.05 USD | `-6.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9295` | 289,300.00 USD | 0.00 USD | 776.50 USD | `-6.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9365` | 288,520.00 USD | 0.00 USD | 9,680.00 USD | `-6.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9405` | 278,840.00 USD | 0.00 USD | 555.18 USD | `-5.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9425` | 278,280.00 USD | 0.00 USD | 409.14 USD | `-5.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9445` | 277,880.00 USD | 0.00 USD | 1,730.00 USD | `-5.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9485` | 276,150.00 USD | 0.00 USD | 634.74 USD | `-4.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9525` | 275,510.00 USD | 0.00 USD | 381.00 USD | `-4.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9555` | 275,130.00 USD | 0.00 USD | 3,900.00 USD | `-4.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9565` | 271,240.00 USD | 0.00 USD | 674.91 USD | `-4.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9575` | 270,560.00 USD | 0.00 USD | 166.41 USD | `-4.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9585` | 270,390.00 USD | 0.00 USD | 192.95 USD | `-3.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9595` | 270,200.00 USD | 0.00 USD | 383.90 USD | `-3.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9605` | 269,820.00 USD | 0.00 USD | 376.80 USD | `-3.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9615` | 269,440.00 USD | 0.00 USD | 152.11 USD | `-3.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9625` | 269,290.00 USD | 0.00 USD | 573.55 USD | `-3.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9635` | 268,720.00 USD | 0.00 USD | 124.10 USD | `-3.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9645` | 268,590.00 USD | 0.00 USD | 148.82 USD | `-3.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9665` | 268,440.00 USD | 0.00 USD | 554.58 USD | `-3.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9675` | 267,890.00 USD | 0.00 USD | 1,800.00 USD | `-3.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9685` | 266,090.00 USD | 0.00 USD | 153.22 USD | `-2.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9695` | 265,930.00 USD | 0.00 USD | 22,800.00 USD | `-2.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9705` | 243,130.00 USD | 0.00 USD | 11,230.00 USD | `-2.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9715` | 231,900.00 USD | 0.00 USD | 10,370.00 USD | `-2.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9725` | 221,530.00 USD | 0.00 USD | 6,930.00 USD | `-2.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9735` | 214,600.00 USD | 0.00 USD | 7,630.00 USD | `-2.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9745` | 206,970.00 USD | 0.00 USD | 8,750.00 USD | `-2.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9755` | 198,220.00 USD | 0.00 USD | 21,960.00 USD | `-2.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9765` | 176,260.00 USD | 0.00 USD | 9,500.00 USD | `-2.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9775` | 166,760.00 USD | 0.00 USD | 1,280.00 USD | `-2.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9785` | 165,480.00 USD | 0.00 USD | 11,400.00 USD | `-1.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9795` | 154,080.00 USD | 0.00 USD | 123.61 USD | `-1.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9805` | 153,960.00 USD | 0.00 USD | 5,810.00 USD | `-1.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9835` | 148,150.00 USD | 0.00 USD | 120.48 USD | `-1.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9845` | 148,030.00 USD | 0.00 USD | 22,170.00 USD | `-1.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9855` | 125,860.00 USD | 0.00 USD | 15,070.00 USD | `-1.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9865` | 110,790.00 USD | 0.00 USD | 32,800.00 USD | `-1.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9875` | 77,990.00 USD | 0.00 USD | 217.05 USD | `-1.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9895` | 77,780.00 USD | 0.00 USD | 34,970.00 USD | `-0.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9925` | 42,800.00 USD | 0.00 USD | 31,750.00 USD | `-0.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9935` | 11,050.00 USD | 0.00 USD | 1,320.00 USD | `-0.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9945` | 9,730.00 USD | 0.00 USD | 782.07 USD | `-0.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9955` | 8,950.00 USD | 0.00 USD | 403.28 USD | `-0.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9965` | 8,540.00 USD | 0.00 USD | 3,400.00 USD | `-0.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9975` | 5,140.00 USD | 0.00 USD | 5,140.00 USD | `-0.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 1,000.00 USD | 1,000.00 USD | 0.00 USD | `+0.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 1,150.00 USD | 150.33 USD | 0.00 USD | `+0.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 1,390.00 USD | 235.79 USD | 0.00 USD | `+0.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 2,730.00 USD | 1,340.00 USD | 0.00 USD | `+0.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 3,290.00 USD | 560.17 USD | 0.00 USD | `+0.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 5,330.00 USD | 2,040.00 USD | 0.00 USD | `+1.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 5,530.00 USD | 198.46 USD | 0.00 USD | `+1.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 6,140.00 USD | 615.60 USD | 0.00 USD | `+1.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 9,600.00 USD | 3,460.00 USD | 0.00 USD | `+1.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 11,720.00 USD | 2,110.00 USD | 0.00 USD | `+1.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 12,280.00 USD | 561.17 USD | 0.00 USD | `+1.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 15,280.00 USD | 3,000.00 USD | 0.00 USD | `+2.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 17,730.00 USD | 2,450.00 USD | 0.00 USD | `+2.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 18,130.00 USD | 401.26 USD | 0.00 USD | `+2.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 18,410.00 USD | 286.22 USD | 0.00 USD | `+2.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 19,220.00 USD | 804.09 USD | 0.00 USD | `+2.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 21,870.00 USD | 2,660.00 USD | 0.00 USD | `+2.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 22,070.00 USD | 201.52 USD | 0.00 USD | `+2.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 22,280.00 USD | 201.60 USD | 0.00 USD | `+2.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 25,480.00 USD | 3,210.00 USD | 0.00 USD | `+2.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 25,590.00 USD | 101.51 USD | 0.00 USD | `+3.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 27,290.00 USD | 1,700.00 USD | 0.00 USD | `+3.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 27,490.00 USD | 206.92 USD | 0.00 USD | `+3.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 27,700.00 USD | 202.90 USD | 0.00 USD | `+3.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 27,930.00 USD | 234.48 USD | 0.00 USD | `+3.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 28,450.00 USD | 516.75 USD | 0.00 USD | `+3.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 28,650.00 USD | 204.93 USD | 0.00 USD | `+3.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 29,120.00 USD | 472.50 USD | 0.00 USD | `+3.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 29,330.00 USD | 203.87 USD | 0.00 USD | `+3.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 30,990.00 USD | 1,670.00 USD | 0.00 USD | `+4.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 32,900.00 USD | 1,900.00 USD | 0.00 USD | `+4.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 33,100.00 USD | 205.99 USD | 0.00 USD | `+4.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 44,410.00 USD | 11,310.00 USD | 0.00 USD | `+4.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 45,710.00 USD | 1,290.00 USD | 0.00 USD | `+4.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 45,910.00 USD | 206.97 USD | 0.00 USD | `+5.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 46,020.00 USD | 107.99 USD | 0.00 USD | `+5.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 46,270.00 USD | 247.60 USD | 0.00 USD | `+5.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 46,400.00 USD | 129.79 USD | 0.00 USD | `+6.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 112,210.00 USD | 65,810.00 USD | 0.00 USD | `+6.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 112,760.00 USD | 544.88 USD | 0.00 USD | `+7.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 112,910.00 USD | 157.10 USD | 0.00 USD | `+8.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 115,080.00 USD | 2,170.00 USD | 0.00 USD | `+9.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 116,620.00 USD | 1,540.00 USD | 0.00 USD | `+9.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 126,550.00 USD | 9,930.00 USD | 0.00 USD | `+9.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 127,520.00 USD | 976.36 USD | 0.00 USD | `+10.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 128,740.00 USD | 1,210.00 USD | 0.00 USD | `+11.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 129,620.00 USD | 877.63 USD | 0.00 USD | `+11.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 129,790.00 USD | 171.50 USD | 0.00 USD | `+11.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 129,960.00 USD | 171.09 USD | 0.00 USD | `+12.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 131,980.00 USD | 2,020.00 USD | 0.00 USD | `+12.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 132,230.00 USD | 249.83 USD | 0.00 USD | `+13.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 134,890.00 USD | 2,670.00 USD | 0.00 USD | `+13.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 137,270.00 USD | 2,380.00 USD | 0.00 USD | `+14.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 137,420.00 USD | 151.16 USD | 0.00 USD | `+15.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 137,570.00 USD | 151.29 USD | 0.00 USD | `+15.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 137,720.00 USD | 151.42 USD | 0.00 USD | `+15.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 137,870.00 USD | 151.55 USD | 0.00 USD | `+15.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 138,030.00 USD | 151.69 USD | 0.00 USD | `+15.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 139,010.00 USD | 986.35 USD | 0.00 USD | `+16.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 141,060.00 USD | 2,050.00 USD | 0.00 USD | `+16.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 141,170.00 USD | 110.00 USD | 0.00 USD | `+17.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 141,410.00 USD | 237.90 USD | 0.00 USD | `+19.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 142,620.00 USD | 1,210.00 USD | 0.00 USD | `+20.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 312,200.00 USD | 169,580.00 USD | 0.00 USD | `+20.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 314,200.00 USD | 2,000.00 USD | 0.00 USD | `+23.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 314,450.00 USD | 245.41 USD | 0.00 USD | `+28.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 321,800.00 USD | 7,350.00 USD | 0.00 USD | `+29.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 322,210.00 USD | 415.25 USD | 0.00 USD | `+30.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 328,730.00 USD | 6,520.00 USD | 0.00 USD | `+30.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 785,720.00 USD | 456,990.00 USD | 0.00 USD | `+31.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 786,370.00 USD | 655.75 USD | 0.00 USD | `+31.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 788,190.00 USD | 1,810.00 USD | 0.00 USD | `+34.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 802,070.00 USD | 13,880.00 USD | 0.00 USD | `+34.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 803,320.00 USD | 1,250.00 USD | 0.00 USD | `+35.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 805,390.00 USD | 2,070.00 USD | 0.00 USD | `+39.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 805,530.00 USD | 140.05 USD | 0.00 USD | `+40.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 805,690.00 USD | 160.42 USD | 0.00 USD | `+40.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 806,290.00 USD | 598.33 USD | 0.00 USD | `+41.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 840,460.00 USD | 34,170.00 USD | 0.00 USD | `+43.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 841,340.00 USD | 879.84 USD | 0.00 USD | `+49.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 841,930.00 USD | 590.88 USD | 0.00 USD | `+50.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 844,990.00 USD | 3,050.00 USD | 0.00 USD | `+51.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 845,280.00 USD | 297.27 USD | 0.00 USD | `+55.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.65` | 853,810.00 USD | 8,530.00 USD | 0.00 USD | `+65.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 853,960.00 USD | 143.99 USD | 0.00 USD | `+67.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 854,130.00 USD | 177.05 USD | 0.00 USD | `+77.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 854,570.00 USD | 431.40 USD | 0.00 USD | `+80.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.91` | 859,670.00 USD | 5,100.00 USD | 0.00 USD | `+91.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.91` | 862,150.00 USD | 2,480.00 USD | 0.00 USD | `+91.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.98` | 867,980.00 USD | 5,830.00 USD | 0.00 USD | `+98.51%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.8720` | 4,960,000.00 USD | 0.00 USD | 4,960,000.00 USD | 6,700.00 USD | 3,140.00 USD | 2,250.00 USD |
| `7D` | `0.8740` | 4,950,000.00 USD | 0.00 USD | 4,950,000.00 USD | 0.00 USD | 86.15 USD | 0.00 USD |
| `7D` | `0.8760` | 4,950,000.00 USD | 0.00 USD | 4,950,000.00 USD | 6,030.00 USD | 6,200.00 USD | 5,860.00 USD |
| `7D` | `0.8780` | 4,930,000.00 USD | 0.00 USD | 4,930,000.00 USD | 15,500.00 USD | 50.60 USD | 5,490.00 USD |
| `7D` | `0.8800` | 4,910,000.00 USD | 0.00 USD | 4,910,000.00 USD | 0.00 USD | 3,870.00 USD | 0.00 USD |
| `7D` | `0.8820` | 4,910,000.00 USD | 0.00 USD | 4,910,000.00 USD | 8,660.00 USD | 3,420.00 USD | 0.00 USD |
| `1D` | `0.8830` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 11,510.00 USD | 3,820.00 USD | 5,500.00 USD |
| `7D` | `0.8840` | 4,900,000.00 USD | 0.00 USD | 4,900,000.00 USD | 4,540.00 USD | 2,690.00 USD | 1,060.00 USD |
| `1D` | `0.8850` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 7,950.00 USD | 1,290.00 USD | 2,160.00 USD |
| `7D` | `0.8860` | 4,890,000.00 USD | 0.00 USD | 4,890,000.00 USD | 15,980.00 USD | 8,010.00 USD | 2,410.00 USD |
| `1D` | `0.8870` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 6,560.00 USD | 3,430.00 USD | 8,790.00 USD |
| `7D` | `0.8880` | 4,860,000.00 USD | 0.00 USD | 4,860,000.00 USD | 825.15 USD | 2,020.00 USD | 11,470.00 USD |
| `1D` | `0.8890` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 3,880.00 USD | 3,900.00 USD | 3,800.00 USD |
| `7D` | `0.8900` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 25,940.00 USD | 6,560.00 USD | 21,510.00 USD |
| `1D` | `0.8910` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 7,750.00 USD | 1,620.00 USD | 4,630.00 USD |
| `7D` | `0.8920` | 4,790,000.00 USD | 0.00 USD | 4,790,000.00 USD | 45,890.00 USD | 6,740.00 USD | 15,680.00 USD |
| `1D` | `0.8930` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 5,380.00 USD | 3,370.00 USD | 4,050.00 USD |
| `7D` | `0.8940` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 7,120.00 USD | 9,570.00 USD | 26,540.00 USD |
| `1D` | `0.8950` | 2,300,000.00 USD | 0.00 USD | 2,300,000.00 USD | 2,810.00 USD | 3,460.00 USD | 3,860.00 USD |
| `7D` | `0.8960` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 30,120.00 USD | 13,190.00 USD | 12,020.00 USD |
| `1D` | `0.8970` | 2,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 11,540.00 USD | 5,730.00 USD | 13,550.00 USD |
| `7D` | `0.8980` | 4,630,000.00 USD | 0.00 USD | 4,630,000.00 USD | 31,080.00 USD | 6,910.00 USD | 36,260.00 USD |
| `1D` | `0.8990` | 2,260,000.00 USD | 0.00 USD | 2,260,000.00 USD | 5,530.00 USD | 792.84 USD | 2,380.00 USD |
| `7D` | `0.9000` | 4,550,000.00 USD | 0.00 USD | 4,550,000.00 USD | 39,940.00 USD | 10,960.00 USD | 12,480.00 USD |
| `1D` | `0.9010` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 1,310.00 USD | 2,570.00 USD | 806.11 USD |
| `7D` | `0.9020` | 4,490,000.00 USD | 0.00 USD | 4,490,000.00 USD | 16,980.00 USD | 11,760.00 USD | 11,020.00 USD |
| `1D` | `0.9030` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 5,900.00 USD | 1,300.00 USD | 8,500.00 USD |
| `7D` | `0.9040` | 4,450,000.00 USD | 0.00 USD | 4,450,000.00 USD | 17,160.00 USD | 5,840.00 USD | 11,110.00 USD |
| `1D` | `0.9050` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 12,620.00 USD | 2,920.00 USD | 9,760.00 USD |
| `7D` | `0.9060` | 4,420,000.00 USD | 0.00 USD | 4,420,000.00 USD | 45,450.00 USD | 27,200.00 USD | 38,830.00 USD |
| `1D` | `0.9070` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 5,360.00 USD | 435.19 USD | 0.00 USD |
| `7D` | `0.9080` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 21,830.00 USD | 3,470.00 USD | 6,560.00 USD |
| `1D` | `0.9090` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 10,750.00 USD | 4,100.00 USD | 1,460.00 USD |
| `7D` | `0.9100` | 4,270,000.00 USD | 0.00 USD | 4,270,000.00 USD | 6,390.00 USD | 10,340.00 USD | 13,290.00 USD |
| `1D` | `0.9110` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 11,100.00 USD | 769.81 USD | 7,070.00 USD |
| `7D` | `0.9120` | 4,240,000.00 USD | 0.00 USD | 4,240,000.00 USD | 21,820.00 USD | 3,890.00 USD | 371.71 USD |
| `1D` | `0.9130` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 4,590.00 USD | 146.71 USD | 3,650.00 USD |
| `7D` | `0.9140` | 4,220,000.00 USD | 0.00 USD | 4,220,000.00 USD | 46,140.00 USD | 8,800.00 USD | 26,510.00 USD |
| `1D` | `0.9150` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 8,880.00 USD | 2,210.00 USD | 8,480.00 USD |
| `7D` | `0.9160` | 4,140,000.00 USD | 0.00 USD | 4,140,000.00 USD | 6,440.00 USD | 12,510.00 USD | 17,200.00 USD |
| `1D` | `0.9170` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 3,440.00 USD | 52.38 USD | 398.89 USD |
| `7D` | `0.9180` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 29,970.00 USD | 9,070.00 USD | 13,780.00 USD |
| `1D` | `0.9190` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 2,770.00 USD | 138.43 USD | 186.24 USD |
| `7D` | `0.9200` | 4,050,000.00 USD | 0.00 USD | 4,050,000.00 USD | 40,700.00 USD | 4,910.00 USD | 22,830.00 USD |
| `1D` | `0.9210` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 1,690.00 USD | 48.64 USD | 2,330.00 USD |
| `7D` | `0.9220` | 3,980,000.00 USD | 0.00 USD | 3,980,000.00 USD | 15,960.00 USD | 2,440.00 USD | 15,640.00 USD |
| `1D` | `0.9230` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 10,750.00 USD | 2,010.00 USD | 907.53 USD |
| `7D` | `0.9240` | 3,940,000.00 USD | 0.00 USD | 3,940,000.00 USD | 56,450.00 USD | 17,730.00 USD | 51,900.00 USD |
| `1D` | `0.9250` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 19,910.00 USD | 8,940.00 USD | 14,770.00 USD |
| `7D` | `0.9260` | 3,820,000.00 USD | 0.00 USD | 3,820,000.00 USD | 32,320.00 USD | 3,140.00 USD | 21,360.00 USD |
| `1D` | `0.9270` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 15,520.00 USD | 5,410.00 USD | 10,980.00 USD |
| `7D` | `0.9280` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 85,040.00 USD | 14,050.00 USD | 26,530.00 USD |
| `1D` | `0.9290` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 25,580.00 USD | 4,300.00 USD | 6,800.00 USD |
| `7D` | `0.9300` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 27,510.00 USD | 11,900.00 USD | 18,410.00 USD |
| `1D` | `0.9310` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 10,550.00 USD | 12,160.00 USD | 21,600.00 USD |
| `7D` | `0.9320` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 28,310.00 USD | 7,740.00 USD | 6,120.00 USD |
| `1D` | `0.9330` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 21,790.00 USD | 9,080.00 USD | 9,250.00 USD |
| `7D` | `0.9340` | 3,540,000.00 USD | 0.00 USD | 3,540,000.00 USD | 53,710.00 USD | 31,620.00 USD | 24,000.00 USD |
| `1D` | `0.9350` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 36,480.00 USD | 10,740.00 USD | 13,660.00 USD |
| `7D` | `0.9360` | 3,430,000.00 USD | 0.00 USD | 3,430,000.00 USD | 59,280.00 USD | 6,090.00 USD | 14,950.00 USD |
| `1D` | `0.9370` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 38,860.00 USD | 12,720.00 USD | 20,310.00 USD |
| `7D` | `0.9380` | 3,350,000.00 USD | 0.00 USD | 3,350,000.00 USD | 20,200.00 USD | 20,520.00 USD | 12,010.00 USD |
| `1D` | `0.9390` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 18,190.00 USD | 14,310.00 USD | 13,920.00 USD |
| `7D` | `0.9400` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 26,270.00 USD | 5,930.00 USD | 7,370.00 USD |
| `1D` | `0.9410` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 35,920.00 USD | 11,320.00 USD | 2,030.00 USD |
| `7D` | `0.9420` | 3,250,000.00 USD | 0.00 USD | 3,250,000.00 USD | 51,440.00 USD | 21,070.00 USD | 10,090.00 USD |
| `1D` | `0.9430` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 21,490.00 USD | 8,500.00 USD | 3,110.00 USD |
| `7D` | `0.9440` | 3,170,000.00 USD | 0.00 USD | 3,170,000.00 USD | 56,500.00 USD | 19,940.00 USD | 25,460.00 USD |
| `1D` | `0.9450` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 36,940.00 USD | 20,450.00 USD | 40,150.00 USD |
| `7D` | `0.9460` | 3,070,000.00 USD | 0.00 USD | 3,070,000.00 USD | 69,980.00 USD | 19,530.00 USD | 44,410.00 USD |
| `1D` | `0.9470` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 45,130.00 USD | 24,730.00 USD | 40,860.00 USD |
| `7D` | `0.9480` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 184,270.00 USD | 42,900.00 USD | 84,360.00 USD |
| `1D` | `0.9490` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 88,320.00 USD | 21,030.00 USD | 27,010.00 USD |
| `7D` | `0.9500` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 125,620.00 USD | 39,340.00 USD | 114,560.00 USD |
| `1D` | `0.9510` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 42,770.00 USD | 30,320.00 USD | 50,570.00 USD |
| `7D` | `0.9520` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 134,730.00 USD | 19,590.00 USD | 57,660.00 USD |
| `1D` | `0.9530` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 53,470.00 USD | 24,690.00 USD | 25,930.00 USD |
| `7D` | `0.9540` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 116,590.00 USD | 92,450.00 USD | 108,620.00 USD |
| `1D` | `0.9550` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 88,250.00 USD | 36,640.00 USD | 46,220.00 USD |
| `7D` | `0.9560` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 207,570.00 USD | 30,210.00 USD | 87,460.00 USD |
| `1D` | `0.9570` | 908,660.00 USD | 0.00 USD | 908,660.00 USD | 147,600.00 USD | 47,530.00 USD | 78,300.00 USD |
| `7D` | `0.9580` | 1,490,000.00 USD | 0.00 USD | 1,490,000.00 USD | 107,300.00 USD | 48,050.00 USD | 119,490.00 USD |
| `1D` | `0.9590` | 635,230.00 USD | 0.00 USD | 635,230.00 USD | 49,590.00 USD | 21,430.00 USD | 34,140.00 USD |
| `7D` | `0.9600` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 221,290.00 USD | 74,450.00 USD | 53,600.00 USD |
| `1D` | `0.9610` | 530,070.00 USD | 0.00 USD | 530,070.00 USD | 55,850.00 USD | 28,270.00 USD | 8,180.00 USD |
| `7D` | `0.9620` | 864,650.00 USD | 0.00 USD | 864,650.00 USD | 140,700.00 USD | 32,300.00 USD | 14,350.00 USD |
| `1D` | `0.9630` | 437,780.00 USD | 0.00 USD | 437,780.00 USD | 25,160.00 USD | 12,420.00 USD | 31,660.00 USD |
| `7D` | `0.9640` | 677,300.00 USD | 0.00 USD | 677,300.00 USD | 84,900.00 USD | 778.20 USD | 6,180.00 USD |
| `1D` | `0.9650` | 368,550.00 USD | 0.00 USD | 368,550.00 USD | 25,320.00 USD | 13,150.00 USD | 26,160.00 USD |
| `7D` | `0.9660` | 585,440.00 USD | 0.00 USD | 585,440.00 USD | 4,960.00 USD | 1,120.00 USD | 30,630.00 USD |
| `1D` | `0.9670` | 303,920.00 USD | 0.00 USD | 303,920.00 USD | 21,930.00 USD | 9,620.00 USD | 21,600.00 USD |
| `7D` | `0.9680` | 548,740.00 USD | 0.00 USD | 548,740.00 USD | 6,480.00 USD | 4,670.00 USD | 14,280.00 USD |
| `1D` | `0.9690` | 250,780.00 USD | 0.00 USD | 250,780.00 USD | 37,870.00 USD | 25,560.00 USD | 25,090.00 USD |
| `7D` | `0.9700` | 523,310.00 USD | 0.00 USD | 523,310.00 USD | 33,960.00 USD | 11,250.00 USD | 36,430.00 USD |
| `1D` | `0.9710` | 162,260.00 USD | 0.00 USD | 162,260.00 USD | 24,610.00 USD | 12,350.00 USD | 11,250.00 USD |
| `7D` | `0.9720` | 441,680.00 USD | 0.00 USD | 441,680.00 USD | 33,760.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9730` | 114,050.00 USD | 0.00 USD | 114,050.00 USD | 10,120.00 USD | 0.00 USD | 7,440.00 USD |
| `7D` | `0.9740` | 407,920.00 USD | 0.00 USD | 407,920.00 USD | 0.00 USD | 16,590.00 USD | 7,950.00 USD |
| `1D` | `0.9750` | 96,490.00 USD | 0.00 USD | 96,490.00 USD | 10,430.00 USD | 12,660.00 USD | 3,540.00 USD |
| `7D` | `0.9760` | 383,380.00 USD | 0.00 USD | 383,380.00 USD | 0.00 USD | 0.00 USD | 8,980.00 USD |
| `1D` | `0.9770` | 69,850.00 USD | 0.00 USD | 69,850.00 USD | 22,490.00 USD | 2,870.00 USD | 11,290.00 USD |
| `7D` | `0.9780` | 374,400.00 USD | 0.00 USD | 374,400.00 USD | 0.00 USD | 0.00 USD | 27,680.00 USD |
| `1D` | `0.9790` | 33,200.00 USD | 0.00 USD | 33,200.00 USD | 9,790.00 USD | 3,600.00 USD | 1,990.00 USD |
| `7D` | `0.9800` | 346,720.00 USD | 0.00 USD | 346,720.00 USD | 0.00 USD | 0.00 USD | 152,190.00 USD |
| `1D` | `0.9810` | 17,820.00 USD | 0.00 USD | 17,820.00 USD | 0.00 USD | 0.00 USD | 1,270.00 USD |
| `7D` | `0.9820` | 194,540.00 USD | 0.00 USD | 194,540.00 USD | 10,090.00 USD | 0.00 USD | 55,110.00 USD |
| `7D` | `0.9840` | 129,330.00 USD | 0.00 USD | 129,330.00 USD | 0.00 USD | 0.00 USD | 22,090.00 USD |
| `1D` | `0.9850` | 16,560.00 USD | 0.00 USD | 16,560.00 USD | 575.70 USD | 0.00 USD | 518.30 USD |
| `7D` | `0.9860` | 107,240.00 USD | 0.00 USD | 107,240.00 USD | 0.00 USD | 16,440.00 USD | 0.00 USD |
| `7D` | `0.9920` | 90,810.00 USD | 0.00 USD | 90,810.00 USD | 0.00 USD | 0.00 USD | 1,220.00 USD |
| `1D` | `0.9930` | 15,460.00 USD | 0.00 USD | 15,460.00 USD | 0.00 USD | 13,250.00 USD | 601.92 USD |
| `7D` | `0.9960` | 89,590.00 USD | 0.00 USD | 89,590.00 USD | 32,670.00 USD | 0.00 USD | 56,910.00 USD |
| `1D` | `0.9970` | 1,610.00 USD | 0.00 USD | 1,610.00 USD | 0.00 USD | 0.00 USD | 1,610.00 USD |
| `7D` | `0.9970` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9980` | 25,190.00 USD | 25,190.00 USD | 0.00 USD | 22,050.00 USD | 0.00 USD | 3,140.00 USD |
| `1D` | `0.9990` | 9,020.00 USD | 9,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,020.00 USD |
| `1D` | `0.9990` | 18,040.00 USD | 18,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,020.00 USD |
| `7D` | `1.00` | 89,390.00 USD | 89,390.00 USD | 0.00 USD | 52,850.00 USD | 11,340.00 USD | 0.00 USD |
| `1D` | `1.00` | 99,450.00 USD | 99,450.00 USD | 0.00 USD | 49,050.00 USD | 25,560.00 USD | 6,800.00 USD |
| `7D` | `1.00` | 155,880.00 USD | 155,880.00 USD | 0.00 USD | 28,410.00 USD | 19,580.00 USD | 18,510.00 USD |
| `1D` | `1.00` | 200,390.00 USD | 200,390.00 USD | 0.00 USD | 50,360.00 USD | 23,660.00 USD | 26,910.00 USD |
| `7D` | `1.00` | 274,890.00 USD | 274,890.00 USD | 0.00 USD | 81,950.00 USD | 11,090.00 USD | 25,970.00 USD |
| `1D` | `1.00` | 318,840.00 USD | 318,840.00 USD | 0.00 USD | 43,090.00 USD | 27,900.00 USD | 47,460.00 USD |
| `7D` | `1.01` | 379,220.00 USD | 379,220.00 USD | 0.00 USD | 69,380.00 USD | 8,220.00 USD | 26,720.00 USD |
| `1D` | `1.01` | 413,420.00 USD | 413,420.00 USD | 0.00 USD | 51,770.00 USD | 17,570.00 USD | 25,230.00 USD |
| `7D` | `1.01` | 455,890.00 USD | 455,890.00 USD | 0.00 USD | 44,170.00 USD | 9,650.00 USD | 22,850.00 USD |
| `1D` | `1.01` | 568,580.00 USD | 568,580.00 USD | 0.00 USD | 75,340.00 USD | 35,830.00 USD | 44,000.00 USD |
| `7D` | `1.01` | 583,020.00 USD | 583,020.00 USD | 0.00 USD | 47,080.00 USD | 10,410.00 USD | 69,650.00 USD |
| `1D` | `1.01` | 656,920.00 USD | 656,920.00 USD | 0.00 USD | 46,500.00 USD | 21,340.00 USD | 20,500.00 USD |
| `7D` | `1.01` | 672,330.00 USD | 672,330.00 USD | 0.00 USD | 46,910.00 USD | 26,300.00 USD | 16,100.00 USD |
| `1D` | `1.01` | 754,160.00 USD | 754,160.00 USD | 0.00 USD | 58,820.00 USD | 18,230.00 USD | 20,200.00 USD |
| `7D` | `1.01` | 765,160.00 USD | 765,160.00 USD | 0.00 USD | 46,130.00 USD | 28,140.00 USD | 18,560.00 USD |
| `1D` | `1.01` | 869,610.00 USD | 869,610.00 USD | 0.00 USD | 54,330.00 USD | 33,250.00 USD | 27,870.00 USD |
| `7D` | `1.02` | 814,660.00 USD | 814,660.00 USD | 0.00 USD | 14,510.00 USD | 22,990.00 USD | 12,000.00 USD |
| `1D` | `1.02` | 951,240.00 USD | 951,240.00 USD | 0.00 USD | 40,370.00 USD | 17,040.00 USD | 24,210.00 USD |
| `7D` | `1.02` | 956,220.00 USD | 956,220.00 USD | 0.00 USD | 99,580.00 USD | 20,410.00 USD | 21,580.00 USD |
| `1D` | `1.02` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 48,440.00 USD | 20,470.00 USD | 4,480.00 USD |
| `7D` | `1.02` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 240,080.00 USD | 65,780.00 USD | 32,020.00 USD |
| `1D` | `1.02` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 33,060.00 USD | 13,660.00 USD | 6,770.00 USD |
| `7D` | `1.02` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 56,930.00 USD | 45,320.00 USD | 90,540.00 USD |
| `1D` | `1.02` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 40,700.00 USD | 15,440.00 USD | 23,850.00 USD |
| `7D` | `1.02` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 52,560.00 USD | 56,700.00 USD | 86,350.00 USD |
| `1D` | `1.02` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 42,950.00 USD | 33,190.00 USD | 38,570.00 USD |
| `7D` | `1.03` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 5,590.00 USD | 107,890.00 USD | 23,170.00 USD |
| `1D` | `1.03` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 12,950.00 USD | 201.13 USD | 16,960.00 USD |
| `7D` | `1.03` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 210,020.00 USD | 50,370.00 USD | 3,930.00 USD |
| `1D` | `1.03` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 26,960.00 USD | 22,680.00 USD | 28,810.00 USD |
| `7D` | `1.03` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 133,500.00 USD | 22,700.00 USD | 18,210.00 USD |
| `1D` | `1.03` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 81,210.00 USD | 14,130.00 USD | 20,630.00 USD |
| `7D` | `1.03` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 78,340.00 USD | 213.80 USD | 0.00 USD |
| `1D` | `1.03` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 48,750.00 USD | 104.84 USD | 11,890.00 USD |
| `7D` | `1.03` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 216,820.00 USD | 8,290.00 USD | 3,970.00 USD |
| `1D` | `1.03` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 33,320.00 USD | 21,990.00 USD | 31,510.00 USD |
| `7D` | `1.04` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 262,550.00 USD | 430.60 USD | 42,930.00 USD |
| `1D` | `1.04` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 78,050.00 USD | 15,340.00 USD | 77,390.00 USD |
| `7D` | `1.04` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 147,750.00 USD | 1,290.00 USD | 198,490.00 USD |
| `1D` | `1.04` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 10,510.00 USD | 2,410.00 USD | 14,850.00 USD |
| `7D` | `1.04` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 279,460.00 USD | 1,650.00 USD | 86,970.00 USD |
| `1D` | `1.04` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 7,030.00 USD | 4,350.00 USD | 3,080.00 USD |
| `7D` | `1.04` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 167,900.00 USD | 2,070.00 USD | 143,680.00 USD |
| `1D` | `1.04` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 10,800.00 USD | 6,840.00 USD | 41,320.00 USD |
| `7D` | `1.04` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 145,680.00 USD | 39,010.00 USD | 78,780.00 USD |
| `1D` | `1.04` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 20,610.00 USD | 14,680.00 USD | 23,280.00 USD |
| `7D` | `1.05` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 145,490.00 USD | 82,280.00 USD | 176,210.00 USD |
| `1D` | `1.05` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 26,860.00 USD | 2,410.00 USD | 8,120.00 USD |
| `7D` | `1.05` | 4,930,000.00 USD | 4,930,000.00 USD | 0.00 USD | 179,200.00 USD | 27,950.00 USD | 155,020.00 USD |
| `1D` | `1.05` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 2,150.00 USD | 9,760.00 USD | 11,580.00 USD |
| `7D` | `1.05` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 91,750.00 USD | 29,070.00 USD | 40,280.00 USD |
| `1D` | `1.05` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 33,040.00 USD | 4,170.00 USD | 12,890.00 USD |
| `7D` | `1.05` | 5,410,000.00 USD | 5,410,000.00 USD | 0.00 USD | 143,060.00 USD | 49,560.00 USD | 124,150.00 USD |
| `1D` | `1.05` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 16,160.00 USD | 5,850.00 USD | 23,600.00 USD |
| `7D` | `1.05` | 5,570,000.00 USD | 5,570,000.00 USD | 0.00 USD | 82,020.00 USD | 41,820.00 USD | 36,750.00 USD |
| `1D` | `1.05` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 11,080.00 USD | 111.54 USD | 24,570.00 USD |
| `7D` | `1.06` | 5,930,000.00 USD | 5,930,000.00 USD | 0.00 USD | 195,510.00 USD | 47,880.00 USD | 121,890.00 USD |
| `1D` | `1.06` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 6,040.00 USD | 5,180.00 USD | 20,020.00 USD |
| `7D` | `1.06` | 6,280,000.00 USD | 6,280,000.00 USD | 0.00 USD | 192,680.00 USD | 63,010.00 USD | 94,660.00 USD |
| `1D` | `1.06` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 14,940.00 USD | 2,920.00 USD | 13,590.00 USD |
| `7D` | `1.06` | 6,670,000.00 USD | 6,670,000.00 USD | 0.00 USD | 197,680.00 USD | 69,880.00 USD | 118,850.00 USD |
| `1D` | `1.06` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 1,840.00 USD | 7,480.00 USD | 10,670.00 USD |
| `7D` | `1.06` | 6,950,000.00 USD | 6,950,000.00 USD | 0.00 USD | 130,760.00 USD | 83,000.00 USD | 65,720.00 USD |
| `1D` | `1.06` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 4,510.00 USD | 2,600.00 USD | 2,590.00 USD |
| `7D` | `1.06` | 7,190,000.00 USD | 7,190,000.00 USD | 0.00 USD | 102,750.00 USD | 49,310.00 USD | 92,130.00 USD |
| `1D` | `1.06` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 6,950.00 USD | 3,880.00 USD | 9,680.00 USD |
| `7D` | `1.07` | 7,370,000.00 USD | 7,370,000.00 USD | 0.00 USD | 77,180.00 USD | 32,860.00 USD | 61,900.00 USD |
| `1D` | `1.07` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 13,470.00 USD | 4,690.00 USD | 6,100.00 USD |
| `7D` | `1.07` | 7,710,000.00 USD | 7,710,000.00 USD | 0.00 USD | 220,420.00 USD | 30,090.00 USD | 93,450.00 USD |
| `1D` | `1.07` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 6,530.00 USD | 3,920.00 USD | 6,120.00 USD |
| `7D` | `1.07` | 7,910,000.00 USD | 7,910,000.00 USD | 0.00 USD | 121,300.00 USD | 33,000.00 USD | 42,480.00 USD |
| `1D` | `1.07` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 16,590.00 USD | 3,050.00 USD | 4,120.00 USD |
| `7D` | `1.07` | 8,140,000.00 USD | 8,140,000.00 USD | 0.00 USD | 108,840.00 USD | 37,580.00 USD | 83,520.00 USD |
| `1D` | `1.07` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 6,130.00 USD | 4,250.00 USD | 12,130.00 USD |
| `7D` | `1.07` | 8,340,000.00 USD | 8,340,000.00 USD | 0.00 USD | 102,600.00 USD | 21,420.00 USD | 83,440.00 USD |
| `1D` | `1.07` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 4,510.00 USD | 5,370.00 USD | 10,050.00 USD |
| `7D` | `1.08` | 8,490,000.00 USD | 8,490,000.00 USD | 0.00 USD | 103,110.00 USD | 18,670.00 USD | 27,400.00 USD |
| `1D` | `1.08` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 8,480.00 USD | 3,420.00 USD | 5,470.00 USD |
| `7D` | `1.08` | 8,760,000.00 USD | 8,760,000.00 USD | 0.00 USD | 158,650.00 USD | 40,740.00 USD | 69,670.00 USD |
| `1D` | `1.08` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 7,340.00 USD | 3,590.00 USD | 36.19 USD |
| `7D` | `1.08` | 9,000,000.00 USD | 9,000,000.00 USD | 0.00 USD | 176,070.00 USD | 23,400.00 USD | 33,270.00 USD |
| `1D` | `1.08` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 8,690.00 USD | 1,430.00 USD | 2,570.00 USD |
| `7D` | `1.08` | 9,120,000.00 USD | 9,120,000.00 USD | 0.00 USD | 62,710.00 USD | 20,510.00 USD | 38,480.00 USD |
| `1D` | `1.08` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 2,120.00 USD | 3,000.00 USD | 2,640.00 USD |
| `7D` | `1.08` | 9,300,000.00 USD | 9,300,000.00 USD | 0.00 USD | 45,260.00 USD | 31,940.00 USD | 103,610.00 USD |
| `1D` | `1.08` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 5,310.00 USD | 3,010.00 USD | 6,150.00 USD |
| `7D` | `1.09` | 9,490,000.00 USD | 9,490,000.00 USD | 0.00 USD | 127,350.00 USD | 28,200.00 USD | 34,080.00 USD |
| `1D` | `1.09` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 4,520.00 USD | 4,080.00 USD | 3,800.00 USD |
| `7D` | `1.09` | 9,720,000.00 USD | 9,720,000.00 USD | 0.00 USD | 59,850.00 USD | 54,400.00 USD | 114,470.00 USD |
| `1D` | `1.09` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 8,330.00 USD | 1,690.00 USD | 4,630.00 USD |
| `7D` | `1.09` | 9,870,000.00 USD | 9,870,000.00 USD | 0.00 USD | 109,670.00 USD | 15,490.00 USD | 31,860.00 USD |
| `1D` | `1.09` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 5,680.00 USD | 3,430.00 USD | 4,050.00 USD |
| `7D` | `1.09` | 10,010,000.00 USD | 10,010,000.00 USD | 0.00 USD | 39,750.00 USD | 24,570.00 USD | 69,070.00 USD |
| `1D` | `1.09` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 2,940.00 USD | 3,590.00 USD | 3,860.00 USD |
| `7D` | `1.09` | 10,230,000.00 USD | 10,230,000.00 USD | 0.00 USD | 97,830.00 USD | 52,720.00 USD | 67,980.00 USD |
| `1D` | `1.09` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 2,340.00 USD | 3,050.00 USD | 48.08 USD |
| `7D` | `1.10` | 10,420,000.00 USD | 10,420,000.00 USD | 0.00 USD | 82,000.00 USD | 45,500.00 USD | 65,790.00 USD |
| `1D` | `1.10` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 9,890.00 USD | 2,710.00 USD | 13,500.00 USD |
| `7D` | `1.10` | 10,710,000.00 USD | 10,710,000.00 USD | 0.00 USD | 114,770.00 USD | 71,210.00 USD | 105,080.00 USD |
| `1D` | `1.10` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 2,290.00 USD | 811.13 USD | 2,380.00 USD |
| `7D` | `1.10` | 11,030,000.00 USD | 11,030,000.00 USD | 0.00 USD | 193,040.00 USD | 64,610.00 USD | 57,760.00 USD |
| `1D` | `1.10` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 1,420.00 USD | 2,510.00 USD | 656.98 USD |
| `7D` | `1.10` | 11,240,000.00 USD | 11,240,000.00 USD | 0.00 USD | 112,480.00 USD | 17,680.00 USD | 84,010.00 USD |
| `1D` | `1.10` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 3,150.00 USD | 760.75 USD | 7,710.00 USD |
| `7D` | `1.10` | 11,340,000.00 USD | 11,340,000.00 USD | 0.00 USD | 56,090.00 USD | 20,360.00 USD | 21,090.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `BALANCED` | 9,850.00 USD | 0.00 USD | 9,850.00 USD | -9,850.00 USD | `1` | `2026-10-29 14:10:00 UTC - 2026-10-29 14:15:00 UTC` |
| `15m` | `BALANCED` | 9,850.00 USD | 0.00 USD | 9,850.00 USD | -9,850.00 USD | `1` | `2026-10-29 14:00:00 UTC - 2026-10-29 14:15:00 UTC` |
| `1h` | `BALANCED` | 9,850.00 USD | 0.00 USD | 9,850.00 USD | -9,850.00 USD | `1` | `2026-10-29 14:00:00 UTC - 2026-10-29 15:00:00 UTC` |
| `4h` | `BALANCED` | 9,850.00 USD | 0.00 USD | 9,850.00 USD | -9,850.00 USD | `1` | `2026-10-29 12:00:00 UTC - 2026-10-29 16:00:00 UTC` |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `211.91M` | Total OI Tokens: `212,642,076.2 DOT`
  * 1h OI Change: `+0.49%` | 4h OI Change: `+1.82%` | 24h OI Change: `-2.38%`
  * Exchange Breakdown: Binance=`37.46M` | Bybit=`25.00M` | OKX=`10.61M` | Hyperliquid=`5.89M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `3.62K` | Last 24h: `1.09K` | Last 3d: `-16.99K` | Last 7d: `-28.40K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0083%` | **USDT OKX** | `0.0040%` |
| **USDT Bybit** | `0.0014%` | **USDT KuCoin** | `0.0041%` |
| **USDT MEXC** | `0.0082%` | **USDT BingX** | `0.0086%` |
| **USDT Gate** | `0.0088%` | **USDT Bitget** | `-0.0006%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOT` | `37.54%` | `62.46%` | `0.60` | 8,400,000.00 USD |
| `15M` | `Binance` | `42.31%` | `57.69%` | `0.73` | 2,910,000.00 USD |
| `15M` | `OKX` | `41.09%` | `58.91%` | `0.70` | 725,710.00 USD |
| `15M` | `Bybit` | `43.81%` | `56.19%` | `0.78` | 511,910.00 USD |
| `15M` | `KuCoin` | `45.77%` | `54.23%` | `0.84` | 58,350.00 USD |
| `15M` | `Gate` | `28.56%` | `71.44%` | `0.40` | 2,480,000.00 USD |
| `15M` | `Bitget` | `27.53%` | `72.47%` | `0.38` | 500,640.00 USD |
| `15M` | `BingX` | `13.99%` | `86.01%` | `0.16` | 116,080.00 USD |
| `15M` | `MEXC` | `43.52%` | `56.48%` | `0.77` | 59,330.00 USD |
| `15M` | `Bitunix` | `33.54%` | `66.46%` | `0.50` | 90,090.00 USD |
| `15M` | `Hyperliquid` | `35.04%` | `64.96%` | `0.54` | 120,880.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.87%` | `50.13%` | `0.99` | 428,280.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `49.79%` | `50.21%` | `0.99` | 265,470.00 USD |
| `15M` | `HTX` | `41.12%` | `58.88%` | `0.70` | 18,730.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `51.61%` | `48.39%` | `1.07` | 78,450.00 USD |
| `15M` | `Aster` | `53.69%` | `46.31%` | `1.16` | 28,500.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `39.26%` | `60.74%` | `0.65` | 11,970.00 USD |
| `15M` | `Whale Positions` | `42.31%` | `57.69%` | `0.73` | 2,910,000.00 USD |
| `15M` | `Global Accounts` | `37.54%` | `62.46%` | `0.60` | 8,400,000.00 USD |
| `1H` | `DOT` | `55.12%` | `44.88%` | `1.23` | 55,280,000.00 USD |
| `1H` | `Binance` | `57.03%` | `42.97%` | `1.33` | 36,960,000.00 USD |
| `1H` | `OKX` | `46.07%` | `53.93%` | `0.85` | 3,270,000.00 USD |
| `1H` | `Bybit` | `56.46%` | `43.54%` | `1.30` | 1,510,000.00 USD |
| `1H` | `KuCoin` | `43.58%` | `56.42%` | `0.77` | 257,510.00 USD |
| `1H` | `Gate` | `48.84%` | `51.16%` | `0.95` | 4,870,000.00 USD |
| `1H` | `Bitget` | `59.32%` | `40.68%` | `1.46` | 1,170,000.00 USD |
| `1H` | `BingX` | `50.88%` | `49.12%` | `1.04` | 1,630,000.00 USD |
| `1H` | `MEXC` | `58.67%` | `41.33%` | `1.42` | 680,730.00 USD |
| `1H` | `Bitunix` | `51.88%` | `48.12%` | `1.08` | 1,370,000.00 USD |
| `1H` | `Hyperliquid` | `51.15%` | `48.85%` | `1.05` | 641,210.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `46.07%` | `53.93%` | `0.85` | 1,340,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `95.13%` | `4.87%` | `19.53` | 262,360.00 USD |
| `1H` | `HTX` | `78.45%` | `21.55%` | `3.64` | 194,530.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `42.66%` | `57.34%` | `0.74` | 237,590.00 USD |
| `1H` | `Aster` | `56.79%` | `43.21%` | `1.31` | 618,840.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `39.39%` | `60.61%` | `0.65` | 265,570.00 USD |
| `1H` | `Whale Positions` | `57.03%` | `42.97%` | `1.33` | 36,960,000.00 USD |
| `1H` | `Global Accounts` | `55.12%` | `44.88%` | `1.23` | 55,280,000.00 USD |
| `4H` | `DOT` | `48.32%` | `51.68%` | `0.93` | 20,430,000.00 USD |
| `4H` | `Binance` | `45.79%` | `54.21%` | `0.84` | 6,550,000.00 USD |
| `4H` | `OKX` | `52.66%` | `47.34%` | `1.11` | 1,750,000.00 USD |
| `4H` | `Bybit` | `41.61%` | `58.39%` | `0.71` | 911,800.00 USD |
| `4H` | `KuCoin` | `49.32%` | `50.68%` | `0.97` | 321,340.00 USD |
| `4H` | `Gate` | `29.57%` | `70.43%` | `0.42` | 2,780,000.00 USD |
| `4H` | `Bitget` | `29.71%` | `70.29%` | `0.42` | 629,940.00 USD |
| `4H` | `BingX` | `24.83%` | `75.17%` | `0.33` | 1,130,000.00 USD |
| `4H` | `MEXC` | `87.68%` | `12.32%` | `7.12` | 883,270.00 USD |
| `4H` | `Bitunix` | `46.73%` | `53.27%` | `0.88` | 208,000.00 USD |
| `4H` | `Hyperliquid` | `53.27%` | `46.73%` | `1.14` | 352,920.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.42%` | `49.58%` | `1.02` | 2,810,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `86.4%` | `13.6%` | `6.35` | 1,500,000.00 USD |
| `4H` | `HTX` | `49.38%` | `50.62%` | `0.98` | 227,880.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `61.24%` | `38.76%` | `1.58` | 226,680.00 USD |
| `4H` | `Aster` | `69.14%` | `30.86%` | `2.24` | 55,450.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `64.83%` | `35.17%` | `1.84` | 92,310.00 USD |
| `4H` | `Whale Positions` | `45.79%` | `54.21%` | `0.84` | 6,550,000.00 USD |
| `4H` | `Global Accounts` | `48.32%` | `51.68%` | `0.93` | 20,430,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.9850` | `0.9843` | `0.9850` | `0.9862` | `0.9826` | 337,983.57 USD | 120,302.78 USD | 217,680.79 USD | -97,378.01 USD | `-28.81%` | `2B / 8S` |
| `0:00 UTC` | `0.9801` | `0.9807` | `0.9801` | `0.9839` | `0.9788` | 679,003.70 USD | 307,703.79 USD | 371,299.91 USD | -63,596.13 USD | `-9.37%` | `6B / 6S` |
| `5:00 UTC` | `0.9812` | `0.9819` | `0.9812` | `0.9844` | `0.9804` | 293,595.13 USD | 150,035.25 USD | 143,559.88 USD | 6,475.37 USD | `+2.21%` | `5B / 2S` |
| `0:00 UTC` | `0.9840` | `0.9868` | `0.9840` | `0.9912` | `0.9830` | 702,313.26 USD | 358,591.01 USD | 343,722.25 USD | 14,868.76 USD | `+2.12%` | `10B / 9S` |
| `5:00 UTC` | `0.9900` | `0.9891` | `0.9900` | `0.9909` | `0.9870` | 345,228.21 USD | 161,286.19 USD | 183,942.02 USD | -22,655.82 USD | `-6.56%` | `4B / 5S` |
| `0:00 UTC` | `0.9940` | `0.9939` | `0.9940` | `0.9960` | `0.9899` | 547,224.62 USD | 290,627.23 USD | 256,597.39 USD | 34,029.84 USD | `+6.22%` | `10B / 5S` |
| `5:00 UTC` | `0.9970` | `0.9963` | `0.9970` | `0.9988` | `0.9931` | 590,797.05 USD | 306,692.25 USD | 284,104.80 USD | 22,587.44 USD | `+3.82%` | `8B / 11S` |
| `0:00 UTC` | `0.9880` | `0.9905` | `0.9880` | `0.9967` | `0.9873` | 999,827.36 USD | 578,168.35 USD | 421,659.02 USD | 156,509.33 USD | `+15.65%` | `11B / 17S` |
| `5:00 UTC` | `0.9926` | `0.9964` | `0.9926` | `1.00` | `0.9919` | 661,501.20 USD | 356,712.90 USD | 304,788.31 USD | 51,924.59 USD | `+7.85%` | `10B / 7S` |
| `0:00 UTC` | `0.9971` | `0.9976` | `0.9971` | `0.9993` | `0.9950` | 305,927.97 USD | 116,962.10 USD | 188,965.87 USD | -72,003.77 USD | `-23.54%` | `0B / 13S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 20:39` | `Volume 1.0M DOT` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `1.01` | 0.00 USD | 0.00 USD |
| `10-28 19:19` | `Range 0.005` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.9951` | 122,000.00 USD | 0.00 USD |
| `10-28 19:07` | `Volume 1.0M DOT` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `1.01` | 333,000.00 USD | 0.00 USD |
| `10-28 19:01` | `Range 0.005` | `Divergence` | **`BEARISH`** | Rally without taker buying | `1.01` | 0.00 USD | 0.00 USD |
| `10-28 18:58` | `Volume 1.0M DOT` | `Divergence` | **`BEARISH`** | Rally without taker buying | `1.01` | 0.00 USD | 0.00 USD |
| `10-28 18:40` | `Volume 1.0M DOT` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.9970` | 0.00 USD | 0.00 USD |
| `10-28 18:31` | `Range 0.005` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.9987` | 0.00 USD | 0.00 USD |
| `10-28 18:31` | `Range 0.005` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `1.00` | 219,000.00 USD | 0.00 USD |
| `10-28 18:30` | `Volume 1.0M DOT` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.9987` | 0.00 USD | 0.00 USD |
| `10-28 18:30` | `Volume 1.0M DOT` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `1.00` | 221,000.00 USD | 0.00 USD |
| `10-28 18:19` | `Range 0.005` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.9972` | 0.00 USD | 0.00 USD |
| `10-28 18:16` | `Volume 1.0M DOT` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.9972` | 0.00 USD | 0.00 USD |
| `10-28 17:55` | `Volume 1.0M DOT` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `1.01` | 229,000.00 USD | 0.00 USD |
| `10-28 17:46` | `Range 0.005` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `1.01` | 260,000.00 USD | 0.00 USD |
| `10-28 17:45` | `Volume 1.0M DOT` | `Divergence` | **`BEARISH`** | Rally without taker buying | `1.01` | 0.00 USD | 0.00 USD |
| `10-28 17:45` | `Volume 1.0M DOT` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `1.00` | 0.00 USD | 0.00 USD |
| `10-28 11:08` | `Range 0.005` | `Divergence` | **`BEARISH`** | Rally without taker buying | `1.00` | 0.00 USD | 0.00 USD |
| `10-28 09:02` | `Range 0.005` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `1.01` | 363,000.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | -5,140.00 USD | -112,280.00 USD | **`DISTRIBUTION`** |
| `15m` | 3,210.00 USD | -137,540.00 USD | **`DISTRIBUTION`** |
| `30m` | 37,300.00 USD | 240.23 USD | **`ACCUMULATION`** |
| `1h` | 26,910.00 USD | -41,630.00 USD | **`DISTRIBUTION`** |
| `2h` | 42,940.00 USD | 80,710.00 USD | **`ACCUMULATION`** |
| `4h` | -156,830.00 USD | -485,110.00 USD | **`DISTRIBUTION`** |
| `6h` | -121,530.00 USD | -294,570.00 USD | **`DISTRIBUTION`** |
| `8h` | -82,830.00 USD | 267,120.00 USD | **`ACCUMULATION`** |
| `12h` | 148,820.00 USD | 852,660.00 USD | **`ACCUMULATION`** |
| `24h` | -256,130.00 USD | -2,210,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -5,780,000.00 USD | -16,460,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -28,790,000.00 USD | -72,640,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-5.14K` | 15m=`+3.21K` | 1h=`+26.91K` | 24h=`-256.13K`
* Futures Capital Netflows: 5m=`-112.28K` | 15m=`-137.54K` | 1h=`-41.63K` | 24h=`-2.21M`
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
  * `2026-10-29 19:41:49 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:20:49 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:09:49 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [dol.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [bea.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [bea.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:48:49 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-29 19:48:49 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-29 16:50:49 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [bankofengland.co.uk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.9539` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.9169` (Risk Distance: `0.0400` pts)
  * +2.5R Take Profit: `1.05`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.9852` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.02` (Risk Distance: `0.0400` pts)
  * +2.5R Take Profit: `0.8852`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.01`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
