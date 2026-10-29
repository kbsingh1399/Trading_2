# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ALGUSD
**Canonical Key**: `ALGUSD` | **Broker Instrument**: `ALGUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 01:11:45 IST` (`2026-10-29 19:41:45 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.0985` | **Live Ask Quote**: `0.1008` | **Mid Price**: `0.0997`
- **Spread Points**: `23.00` | **Spread BPS**: `230.81 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.0993` | VWAP Z-Score: `-0.90` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.000698` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `36.60` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.1034` | Lower -3.00σ Band: `0.0952`
  * Upper +2.51σ Band: `0.1027` | Lower -2.51σ Band: `0.0959`
  * Upper +2.01σ Band: `0.1020` | Lower -2.01σ Band: `0.0966`
  * Upper +2.00σ Band: `0.1020` | Lower -2.00σ Band: `0.0966`
  * Upper +1.28σ Band: `0.1011` | Lower -1.28σ Band: `0.0976`
  * Upper +1.00σ Band: `0.1007` | Lower -1.00σ Band: `0.0980`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.0988` | EMA-20=`0.0993` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.0995` (Slope: `+0.0000`) | EMA-100=`0.0998`
  * Institutional Anchors: EMA-144=`0.1002` | EMA-200=`0.1007` (Slope: `-0.1797`) | EMA-233=`0.1009`
- **Range Boundaries**: 24H High=`0.1048` | 24H Low=`0.0972` | Weekly High=`0.1051` | Weekly Low=`0.0972`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.1004` (Distance: `-0.68%`)
  * Point of Control (POC) = `0.0981` (Distance: `+1.69%`)
  * Value Area Low (VAL) = `0.0974` (Distance: `+2.42%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.1038` | POC=`0.1023` | VAL=`0.1011`
  * Prior Day Extremes: PDH=`0.1048` | PDL=`0.0994` | PDC=`0.1031`
  * Monday Range Blueprint: High=`0.1046` | Mid=`0.1031` | Low=`0.1015`
  * Developing Weekly Value Area: Weekly VAH=`0.1042` | Weekly POC=`0.1023` | Weekly VAL=`0.1009`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.1037` | Low=`0.0972`
  * London Session (08:00-16:00 UTC): High=`0.0999` | Low=`0.0972`
  * New York Session (13:00-21:00 UTC): High=`0.1024` | Low=`0.0978`
  * Initial Balance (First Hour): IB High=`0.0999` | IB Low=`0.0987`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.0993` - `0.1000`
  * Optimal Trade Entry (OTE 0.705): `0.0998`
  * Structural Invalidation Anchor (0.786): `0.1004`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `15m` | - | - | - | - | - | 0.00 USD | 0.00 USD | `+0.00%` | 0.00 USD | `0.00` | **`BALANCED`** | Interbank Volume |

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
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Hyperdash | Resting Book | - | - | - | Normal Interbank Book | - | - |

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
  * 24H Horizon: Short MP=`0.1068` (Vol: 34,981.57 USD, Dist: `+3.28%`) | Long MP=`0.1015` (Vol: 29,089.31 USD, Dist: `--1.77%`)
  * 48H Horizon: Short MP=`0.1067` (Vol: 34,068.88 USD, Dist: `+3.26%`) | Long MP=`0.1016` (Vol: 32,527.85 USD, Dist: `--1.74%`)
  * 3D Horizon: Short MP=`0.1065` (Vol: 32,466.82 USD, Dist: `+3.02%`) | Long MP=`0.1009` (Vol: 37,584.26 USD, Dist: `--2.44%`)
  * 7D Horizon: Short MP=`0.1067` (Vol: 62,663.70 USD, Dist: `+3.72%`) | Long MP=`0.1008` (Vol: 53,528.78 USD, Dist: `--2.01%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0209` | 3,710.00 USD | 264,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0237` | 331.81 USD | 260,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0268` | 1,120.00 USD | 260,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0273` | 224.22 USD | 259,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0278` | 330.91 USD | 259,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0336` | 11,920.00 USD | 258,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0376` | 21,590.00 USD | 246,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0413` | 10,090.00 USD | 225,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0421` | 3,680.00 USD | 215,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 2,100.00 USD | 211,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0432` | 421.58 USD | 209,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0454` | 5,610.00 USD | 209,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0493` | 142.77 USD | 203,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0496` | 267.76 USD | 203,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0508` | 506.59 USD | 203,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0548` | 320.40 USD | 202,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0553` | 5,840.00 USD | 202,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0588` | 111.76 USD | 196,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0599` | 441.33 USD | 196,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0607` | 106.14 USD | 195,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0609` | 223.62 USD | 195,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0621` | 260.91 USD | 195,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0625` | 180.46 USD | 195,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0630` | 6,300.00 USD | 195,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0634` | 167.24 USD | 188,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0636` | 525.94 USD | 188,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0638` | 1,360.00 USD | 188,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0654` | 13,390.00 USD | 186,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0659` | 3,960.00 USD | 173,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0674` | 208.83 USD | 169,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0680` | 12,840.00 USD | 169,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0683` | 5,040.00 USD | 156,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0693` | 6,380.00 USD | 151,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0694` | 155.50 USD | 144,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0717` | 224.98 USD | 144,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0720` | 7,110.00 USD | 144,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0721` | 347.79 USD | 137,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0723` | 563.10 USD | 137,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0727` | 918.15 USD | 136,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0728` | 388.00 USD | 135,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0732` | 1,020.00 USD | 135,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 1,460.00 USD | 134,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0741` | 741.50 USD | 132,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0742` | 838.58 USD | 131,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0751` | 475.62 USD | 131,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0752` | 299.65 USD | 130,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0754` | 557.29 USD | 130,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0755` | 5,460.00 USD | 129,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0756` | 4,630.00 USD | 124,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0759` | 3,050.00 USD | 119,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0761` | 189.82 USD | 116,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0762` | 954.42 USD | 116,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0764` | 1,620.00 USD | 115,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0766` | 133.35 USD | 113,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0766` | 180.43 USD | 113,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0770` | 5,050.00 USD | 113,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0775` | 930.06 USD | 108,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0780` | 438.48 USD | 107,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0793` | 309.08 USD | 107,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0801` | 6,210.00 USD | 106,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0808` | 394.06 USD | 100,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0809` | 487.61 USD | 100,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0814` | 2,040.00 USD | 99,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0819` | 181.85 USD | 97,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0828` | 1,660.00 USD | 97,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0830` | 1,110.00 USD | 95,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0833` | 335.73 USD | 94,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0835` | 7,980.00 USD | 94,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0843` | 24,900.00 USD | 86,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0859` | 2,150.00 USD | 61,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0862` | 1,450.00 USD | 59,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0871` | 994.37 USD | 57,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0872` | 223.88 USD | 56,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0878` | 1,200.00 USD | 56,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0880` | 4,640.00 USD | 55,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0886` | 142.57 USD | 50,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0887` | 442.72 USD | 50,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0890` | 595.97 USD | 50,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0893` | 1,540.00 USD | 49,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0901` | 132.28 USD | 48,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0906` | 338.48 USD | 48,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0912` | 909.76 USD | 47,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0917` | 5,420.00 USD | 46,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0920` | 566.78 USD | 41,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0922` | 659.13 USD | 40,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0924` | 444.94 USD | 40,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 1,780.00 USD | 39,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 110.60 USD | 37,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0927` | 3,230.00 USD | 37,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0930` | 692.39 USD | 34,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0931` | 3,340.00 USD | 33,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0936` | 399.79 USD | 30,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0940` | 134.82 USD | 30,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0943` | 928.17 USD | 30,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0960` | 312.74 USD | 29,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0964` | 22,930.00 USD | 28,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0972` | 291.45 USD | 5,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0974` | 5,150.00 USD | 5,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0979` | 411.07 USD | 411.07 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1048` | 431.56 USD | 431.56 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1105` | 667.17 USD | 1,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1109` | 217.13 USD | 1,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1129` | 289.01 USD | 1,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1268` | 2,190.00 USD | 3,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1416` | 2,540.00 USD | 6,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1474` | 126.43 USD | 6,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1477` | 162.97 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1908` | 102.62 USD | 6,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0209` | 264,580.00 USD | 0.00 USD | 3,710.00 USD | `-79.04%` | `177,866.00` |
| `Live` | `Long` | `0.0237` | 260,870.00 USD | 0.00 USD | 331.81 USD | `-76.23%` | `14,030.00` |
| `Live` | `Long` | `0.0268` | 260,540.00 USD | 0.00 USD | 1,120.00 USD | `-73.01%` | `41,853.00` |
| `Live` | `Long` | `0.0273` | 259,420.00 USD | 0.00 USD | 224.22 USD | `-72.51%` | `8,198.00` |
| `Live` | `Long` | `0.0278` | 259,190.00 USD | 0.00 USD | 330.91 USD | `-72.00%` | `11,882.00` |
| `Live` | `Long` | `0.0336` | 258,860.00 USD | 0.00 USD | 11,920.00 USD | `-66.27%` | `355,228.00` |
| `Live` | `Long` | `0.0376` | 246,950.00 USD | 0.00 USD | 21,590.00 USD | `-62.25%` | `574,860.00` |
| `Live` | `Long` | `0.0413` | 225,360.00 USD | 0.00 USD | 10,090.00 USD | `-58.53%` | `244,544.00` |
| `Live` | `Long` | `0.0421` | 215,270.00 USD | 0.00 USD | 3,680.00 USD | `-57.63%` | `87,382.00` |
| `Live` | `Long` | `0.0425` | 211,590.00 USD | 0.00 USD | 2,100.00 USD | `-57.23%` | `49,368.00` |
| `Live` | `Long` | `0.0432` | 209,490.00 USD | 0.00 USD | 421.58 USD | `-56.62%` | `9,770.00` |
| `Live` | `Long` | `0.0454` | 209,070.00 USD | 0.00 USD | 5,610.00 USD | `-54.41%` | `123,747.00` |
| `Live` | `Long` | `0.0493` | 203,450.00 USD | 0.00 USD | 142.77 USD | `-50.39%` | `2,893.00` |
| `Live` | `Long` | `0.0496` | 203,310.00 USD | 0.00 USD | 267.76 USD | `-50.09%` | `5,393.00` |
| `Live` | `Long` | `0.0508` | 203,040.00 USD | 0.00 USD | 506.59 USD | `-48.98%` | `9,982.00` |
| `Live` | `Long` | `0.0548` | 202,540.00 USD | 0.00 USD | 320.40 USD | `-44.96%` | `5,852.00` |
| `Live` | `Long` | `0.0553` | 202,220.00 USD | 0.00 USD | 5,840.00 USD | `-44.46%` | `105,702.00` |
| `Live` | `Long` | `0.0588` | 196,380.00 USD | 0.00 USD | 111.76 USD | `-40.84%` | `1,899.00` |
| `Live` | `Long` | `0.0599` | 196,270.00 USD | 0.00 USD | 441.33 USD | `-39.84%` | `7,374.00` |
| `Live` | `Long` | `0.0607` | 195,820.00 USD | 0.00 USD | 106.14 USD | `-39.03%` | `1,750.00` |
| `Live` | `Long` | `0.0609` | 195,720.00 USD | 0.00 USD | 223.62 USD | `-38.83%` | `3,675.00` |
| `Live` | `Long` | `0.0621` | 195,490.00 USD | 0.00 USD | 260.91 USD | `-37.53%` | `4,198.00` |
| `Live` | `Long` | `0.0625` | 195,230.00 USD | 0.00 USD | 180.46 USD | `-37.12%` | `2,885.00` |
| `Live` | `Long` | `0.0630` | 195,050.00 USD | 0.00 USD | 6,300.00 USD | `-36.72%` | `100,000.00` |
| `Live` | `Long` | `0.0634` | 188,760.00 USD | 0.00 USD | 167.24 USD | `-36.32%` | `2,640.00` |
| `Live` | `Long` | `0.0636` | 188,590.00 USD | 0.00 USD | 525.94 USD | `-36.02%` | `8,263.00` |
| `Live` | `Long` | `0.0638` | 188,060.00 USD | 0.00 USD | 1,360.00 USD | `-35.92%` | `21,322.00` |
| `Live` | `Long` | `0.0654` | 186,710.00 USD | 0.00 USD | 13,390.00 USD | `-34.31%` | `204,927.00` |
| `Live` | `Long` | `0.0659` | 173,310.00 USD | 0.00 USD | 3,960.00 USD | `-33.71%` | `60,000.00` |
| `Live` | `Long` | `0.0674` | 169,360.00 USD | 0.00 USD | 208.83 USD | `-32.20%` | `3,096.00` |
| `Live` | `Long` | `0.0680` | 169,150.00 USD | 0.00 USD | 12,840.00 USD | `-31.59%` | `188,661.00` |
| `Live` | `Long` | `0.0683` | 156,310.00 USD | 0.00 USD | 5,040.00 USD | `-31.39%` | `73,856.00` |
| `Live` | `Long` | `0.0693` | 151,270.00 USD | 0.00 USD | 6,380.00 USD | `-30.29%` | `92,025.00` |
| `Live` | `Long` | `0.0694` | 144,890.00 USD | 0.00 USD | 155.50 USD | `-30.19%` | `2,239.00` |
| `Live` | `Long` | `0.0717` | 144,730.00 USD | 0.00 USD | 224.98 USD | `-27.98%` | `3,140.00` |
| `Live` | `Long` | `0.0720` | 144,510.00 USD | 0.00 USD | 7,110.00 USD | `-27.67%` | `98,791.00` |
| `Live` | `Long` | `0.0721` | 137,400.00 USD | 0.00 USD | 347.79 USD | `-27.57%` | `4,827.00` |
| `Live` | `Long` | `0.0723` | 137,050.00 USD | 0.00 USD | 563.10 USD | `-27.27%` | `7,783.00` |
| `Live` | `Long` | `0.0727` | 136,490.00 USD | 0.00 USD | 918.15 USD | `-26.97%` | `12,638.00` |
| `Live` | `Long` | `0.0728` | 135,570.00 USD | 0.00 USD | 388.00 USD | `-26.77%` | `5,326.00` |
| `Live` | `Long` | `0.0732` | 135,180.00 USD | 0.00 USD | 1,020.00 USD | `-26.37%` | `13,863.00` |
| `Live` | `Long` | `0.0735` | 134,170.00 USD | 0.00 USD | 1,460.00 USD | `-26.17%` | `19,868.00` |
| `Live` | `Long` | `0.0741` | 132,710.00 USD | 0.00 USD | 741.50 USD | `-25.46%` | `10,000.00` |
| `Live` | `Long` | `0.0742` | 131,960.00 USD | 0.00 USD | 838.58 USD | `-25.36%` | `11,294.00` |
| `Live` | `Long` | `0.0751` | 131,130.00 USD | 0.00 USD | 475.62 USD | `-24.46%` | `6,329.00` |
| `Live` | `Long` | `0.0752` | 130,650.00 USD | 0.00 USD | 299.65 USD | `-24.36%` | `3,982.00` |
| `Live` | `Long` | `0.0754` | 130,350.00 USD | 0.00 USD | 557.29 USD | `-24.26%` | `7,396.00` |
| `Live` | `Long` | `0.0755` | 129,790.00 USD | 0.00 USD | 5,460.00 USD | `-24.16%` | `72,376.00` |
| `Live` | `Long` | `0.0756` | 124,330.00 USD | 0.00 USD | 4,630.00 USD | `-23.95%` | `61,227.00` |
| `Live` | `Long` | `0.0759` | 119,700.00 USD | 0.00 USD | 3,050.00 USD | `-23.75%` | `40,199.00` |
| `Live` | `Long` | `0.0761` | 116,650.00 USD | 0.00 USD | 189.82 USD | `-23.55%` | `2,496.00` |
| `Live` | `Long` | `0.0762` | 116,460.00 USD | 0.00 USD | 954.42 USD | `-23.35%` | `12,517.00` |
| `Live` | `Long` | `0.0764` | 115,510.00 USD | 0.00 USD | 1,620.00 USD | `-23.25%` | `21,173.00` |
| `Live` | `Long` | `0.0766` | 113,890.00 USD | 0.00 USD | 133.35 USD | `-23.05%` | `1,742.00` |
| `Live` | `Long` | `0.0766` | 113,760.00 USD | 0.00 USD | 180.43 USD | `-22.95%` | `2,354.00` |
| `Live` | `Long` | `0.0770` | 113,580.00 USD | 0.00 USD | 5,050.00 USD | `-22.65%` | `65,640.00` |
| `Live` | `Long` | `0.0775` | 108,530.00 USD | 0.00 USD | 930.06 USD | `-22.04%` | `11,993.00` |
| `Live` | `Long` | `0.0780` | 107,600.00 USD | 0.00 USD | 438.48 USD | `-21.54%` | `5,618.00` |
| `Live` | `Long` | `0.0793` | 107,160.00 USD | 0.00 USD | 309.08 USD | `-20.34%` | `3,900.00` |
| `Live` | `Long` | `0.0801` | 106,850.00 USD | 0.00 USD | 6,210.00 USD | `-19.43%` | `77,489.00` |
| `Live` | `Long` | `0.0808` | 100,640.00 USD | 0.00 USD | 394.06 USD | `-18.83%` | `4,880.00` |
| `Live` | `Long` | `0.0809` | 100,240.00 USD | 0.00 USD | 487.61 USD | `-18.73%` | `6,031.00` |
| `Live` | `Long` | `0.0814` | 99,760.00 USD | 0.00 USD | 2,040.00 USD | `-18.12%` | `25,041.00` |
| `Live` | `Long` | `0.0819` | 97,720.00 USD | 0.00 USD | 181.85 USD | `-17.62%` | `2,219.00` |
| `Live` | `Long` | `0.0828` | 97,530.00 USD | 0.00 USD | 1,660.00 USD | `-16.82%` | `20,000.00` |
| `Live` | `Long` | `0.0830` | 95,880.00 USD | 0.00 USD | 1,110.00 USD | `-16.52%` | `13,414.00` |
| `Live` | `Long` | `0.0833` | 94,770.00 USD | 0.00 USD | 335.73 USD | `-16.21%` | `4,028.00` |
| `Live` | `Long` | `0.0835` | 94,430.00 USD | 0.00 USD | 7,980.00 USD | `-16.01%` | `95,507.00` |
| `Live` | `Long` | `0.0843` | 86,450.00 USD | 0.00 USD | 24,900.00 USD | `-15.21%` | `295,245.00` |
| `Live` | `Long` | `0.0859` | 61,550.00 USD | 0.00 USD | 2,150.00 USD | `-13.60%` | `25,000.00` |
| `Live` | `Long` | `0.0862` | 59,400.00 USD | 0.00 USD | 1,450.00 USD | `-13.40%` | `16,779.00` |
| `Live` | `Long` | `0.0871` | 57,950.00 USD | 0.00 USD | 994.37 USD | `-12.49%` | `11,423.00` |
| `Live` | `Long` | `0.0872` | 56,960.00 USD | 0.00 USD | 223.88 USD | `-12.29%` | `2,566.00` |
| `Live` | `Long` | `0.0878` | 56,730.00 USD | 0.00 USD | 1,200.00 USD | `-11.69%` | `13,623.00` |
| `Live` | `Long` | `0.0880` | 55,540.00 USD | 0.00 USD | 4,640.00 USD | `-11.59%` | `52,790.00` |
| `Live` | `Long` | `0.0886` | 50,890.00 USD | 0.00 USD | 142.57 USD | `-10.99%` | `1,610.00` |
| `Live` | `Long` | `0.0887` | 50,750.00 USD | 0.00 USD | 442.72 USD | `-10.89%` | `4,994.00` |
| `Live` | `Long` | `0.0890` | 50,310.00 USD | 0.00 USD | 595.97 USD | `-10.59%` | `6,700.00` |
| `Live` | `Long` | `0.0893` | 49,710.00 USD | 0.00 USD | 1,540.00 USD | `-10.18%` | `17,219.00` |
| `Live` | `Long` | `0.0901` | 48,170.00 USD | 0.00 USD | 132.28 USD | `-9.48%` | `1,469.00` |
| `Live` | `Long` | `0.0906` | 48,040.00 USD | 0.00 USD | 338.48 USD | `-8.98%` | `3,738.00` |
| `Live` | `Long` | `0.0912` | 47,700.00 USD | 0.00 USD | 909.76 USD | `-8.27%` | `9,970.00` |
| `Live` | `Long` | `0.0917` | 46,790.00 USD | 0.00 USD | 5,420.00 USD | `-7.77%` | `59,049.00` |
| `Live` | `Long` | `0.0920` | 41,380.00 USD | 0.00 USD | 566.78 USD | `-7.57%` | `6,164.00` |
| `Live` | `Long` | `0.0922` | 40,810.00 USD | 0.00 USD | 659.13 USD | `-7.27%` | `7,145.00` |
| `Live` | `Long` | `0.0924` | 40,150.00 USD | 0.00 USD | 444.94 USD | `-7.17%` | `4,818.00` |
| `Live` | `Long` | `0.0925` | 39,710.00 USD | 0.00 USD | 1,780.00 USD | `-7.07%` | `19,238.00` |
| `Live` | `Long` | `0.0925` | 37,930.00 USD | 0.00 USD | 110.60 USD | `-6.97%` | `1,195.00` |
| `Live` | `Long` | `0.0927` | 37,820.00 USD | 0.00 USD | 3,230.00 USD | `-6.77%` | `34,813.00` |
| `Live` | `Long` | `0.0930` | 34,590.00 USD | 0.00 USD | 692.39 USD | `-6.46%` | `7,441.00` |
| `Live` | `Long` | `0.0931` | 33,890.00 USD | 0.00 USD | 3,340.00 USD | `-6.36%` | `35,827.00` |
| `Live` | `Long` | `0.0936` | 30,560.00 USD | 0.00 USD | 399.79 USD | `-5.86%` | `4,269.00` |
| `Live` | `Long` | `0.0940` | 30,160.00 USD | 0.00 USD | 134.82 USD | `-5.56%` | `1,435.00` |
| `Live` | `Long` | `0.0943` | 30,020.00 USD | 0.00 USD | 928.17 USD | `-5.26%` | `9,848.00` |
| `Live` | `Long` | `0.0960` | 29,090.00 USD | 0.00 USD | 312.74 USD | `-3.45%` | `3,256.00` |
| `Live` | `Long` | `0.0964` | 28,780.00 USD | 0.00 USD | 22,930.00 USD | `-3.05%` | `237,757.00` |
| `Live` | `Long` | `0.0972` | 5,850.00 USD | 0.00 USD | 291.45 USD | `-2.34%` | `3,000.00` |
| `Live` | `Long` | `0.0974` | 5,560.00 USD | 0.00 USD | 5,150.00 USD | `-2.04%` | `52,827.00` |
| `Live` | `Long` | `0.0979` | 411.07 USD | 0.00 USD | 411.07 USD | `-1.64%` | `4,201.00` |
| `Live` | `Short` | `0.1048` | 431.56 USD | 431.56 USD | 0.00 USD | `+5.40%` | `4,116.00` |
| `Live` | `Short` | `0.1105` | 1,100.00 USD | 667.17 USD | 0.00 USD | `+11.13%` | `6,035.00` |
| `Live` | `Short` | `0.1109` | 1,320.00 USD | 217.13 USD | 0.00 USD | `+11.53%` | `1,957.00` |
| `Live` | `Short` | `0.1129` | 1,600.00 USD | 289.01 USD | 0.00 USD | `+13.44%` | `2,561.00` |
| `Live` | `Short` | `0.1268` | 3,790.00 USD | 2,190.00 USD | 0.00 USD | `+27.41%` | `17,254.00` |
| `Live` | `Short` | `0.1416` | 6,330.00 USD | 2,540.00 USD | 0.00 USD | `+42.39%` | `17,912.00` |
| `Live` | `Short` | `0.1474` | 6,460.00 USD | 126.43 USD | 0.00 USD | `+48.12%` | `858.00` |
| `Live` | `Short` | `0.1477` | 6,620.00 USD | 162.97 USD | 0.00 USD | `+48.52%` | `1,103.00` |
| `Live` | `Short` | `0.1908` | 6,720.00 USD | 102.62 USD | 0.00 USD | `+91.75%` | `538.00` |

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
  * Current Rate: `337.06` | Last 24h: `-4.06K` | Last 3d: `-3.32K` | Last 7d: `-6.03K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0036%` | **USDT OKX** | `-0.0068%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0012%` |
| **USDT MEXC** | `-0.0031%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0100%` |
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
| Live | 15m | Tape Flow | NEUTRAL | Orderflow balanced at current level | - | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 10,920.00 USD | 12,910.00 USD | **`ACCUMULATION`** |
| `15m` | 11,450.00 USD | 12,740.00 USD | **`ACCUMULATION`** |
| `30m` | 11,440.00 USD | 38,100.00 USD | **`ACCUMULATION`** |
| `1h` | -19,940.00 USD | 59,650.00 USD | **`ACCUMULATION`** |
| `2h` | -67,570.00 USD | -100,430.00 USD | **`DISTRIBUTION`** |
| `4h` | -97,330.00 USD | -469,480.00 USD | **`DISTRIBUTION`** |
| `6h` | -118,200.00 USD | -557,800.00 USD | **`DISTRIBUTION`** |
| `8h` | -114,070.00 USD | -532,890.00 USD | **`DISTRIBUTION`** |
| `12h` | -44,060.00 USD | -381,840.00 USD | **`DISTRIBUTION`** |
| `24h` | -200,410.00 USD | -812,680.00 USD | **`DISTRIBUTION`** |
| `1w` | -1,450,000.00 USD | -2,410,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -12,770,000.00 USD | -20,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+10.92K` | 15m=`+11.45K` | 1h=`-19.94K` | 24h=`-200.41K`
* Futures Capital Netflows: 5m=`+12.91K` | 15m=`+12.74K` | 1h=`+59.65K` | 24h=`-812.68K`
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
  * `2026-10-30 00:58:08 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:48:08 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:17:08 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:09:08 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:09:08 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:08:08 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:08:08 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:08:08 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 01:08:08 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:10:08 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:10:08 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:08 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:08 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:08 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:08 IST`: [think.ing.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.0974` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.0931` (Risk Distance: `0.0046` pts)
  * +2.5R Take Profit: `0.1089`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.1004` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.1047` (Risk Distance: `0.0046` pts)
  * +2.5R Take Profit: `0.0889`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.1004`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
