# 🏛️ SOVEREIGN CANDIDATE DOSSIER: SP500
**Canonical Key**: `SP500` | **Broker Instrument**: `SP500.p` | **Asset Class**: `Equity Index US`
**Timestamp**: `2026-10-29 23:52:58 IST` (`2026-10-29 18:22:58 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `7701.79` | **Live Ask Quote**: `7702.56` | **Mid Price**: `7702.18`
- **Spread Points**: `77.00` | **Spread BPS**: `1.00 bps` (Charter Threshold: `5.00 bps`)
- **Gate 1 Clearance**: **`PASS`** | **Execution Posture**: `PASSIVE LIMIT ONLY` | **Order Type Allowed**: `BUY_LIMIT / SELL_LIMIT`
- **True Broker Contract Specifications**:
  * Contract Size: `10.0` | Digits: `2` | Point: `0.01`
  * Point Value (1.0 Lot): `0.10 USD` | Point Value (0.01 Lot): `0.0010 USD`
  * Allowed Lot Sizing: Min Lot=`0.10` | Step Lot=`0.10` | Max Lot=`100.00`
- **Solvency Defense Ladder**:
  * Hard Floor Stop: `4,775.00 USD` (Zero Open Risk) | Operating Defense Buffer: `4,795.00 USD` (Capital Preservation Mode)
  * Kernel Admission Floor: `4,795.00 USD` (`min(balance, equity) - StressedLoss - 2.00 >= 4,795.00 USD`)
- **Pipeline Health (23_Master_Pipeline_Telemetry.parquet)**: Status=`HEALTHY` | Latency=`4.2 ms` | RAM Usage=`385.0 MB`

---

## 2. Technical Profile, VWAP Dispersion Grid & BTC Ribbon
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Session Anchor & Volatility**:
  * Session VWAP: `7718.78` | VWAP Z-Score: `-2.17` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `11.15` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `39.83` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `7742.55` | Lower -3.00σ Band: `7695.01`
  * Upper +2.51σ Band: `7738.67` | Lower -2.51σ Band: `7698.90`
  * Upper +2.01σ Band: `7734.71` | Lower -2.01σ Band: `7702.86`
  * Upper +2.00σ Band: `7734.63` | Lower -2.00σ Band: `7702.94`
  * Upper +1.28σ Band: `7728.92` | Lower -1.28σ Band: `7708.64`
  * Upper +1.00σ Band: `7726.70` | Lower -1.00σ Band: `7710.86`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`7707.97` | EMA-20=`7713.15` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`7718.07` (Slope: `+0.0000`) | EMA-100=`7720.39`
  * Institutional Anchors: EMA-144=`7718.99` | EMA-200=`7714.72` (Slope: `-0.0026`) | EMA-233=`7712.37`
- **Range Boundaries**: 24H High=`7783.55` | 24H Low=`7690.44` | Weekly High=`7783.55` | Weekly Low=`7637.90`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `7727.50` (Distance: `-0.32%`)
  * Point of Control (POC) = `7717.14` (Distance: `-0.18%`)
  * Value Area Low (VAL) = `7709.70` (Distance: `-0.09%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`7738.67` | POC=`7727.63` | VAL=`7723.02`
  * Prior Day Extremes: PDH=`7783.55` | PDL=`7714.51` | PDC=`7724.35`
  * Monday Range Blueprint: High=`7701.39` | Mid=`7657.69` | Low=`7613.99`
  * Developing Weekly Value Area: Weekly VAH=`7740.03` | Weekly POC=`7726.46` | Weekly VAL=`7680.12`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`7733.22` | Low=`7705.30`
  * London Session (08:00-16:00 UTC): High=`7738.99` | Low=`7709.78`
  * New York Session (13:00-21:00 UTC): High=`7735.97` | Low=`7697.54`
  * Initial Balance (First Hour): IB High=`7738.99` | IB Low=`7722.51`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `7671.37` - `7732.98`
  * Optimal Trade Entry (OTE 0.705): `7717.58`
  * Structural Invalidation Anchor (0.786): `7763.79`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `7717.52` | `7722.77` | `7713.07` | `7721.29` | `12,512` | 96,608,780.48 USD | 52,338,055.82 USD | `+54.18%` | 166,063,488.75 USD | `+0.56` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `7721.30` | `7725.53` | `7719.51` | `7724.79` | `8,516` | 65,784,311.64 USD | 43,874,420.47 USD | `+66.69%` | 209,937,909.22 USD | `+0.35` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `7724.79` | `7724.85` | `7719.05` | `7720.81` | `8,637` | 66,684,635.97 USD | -35,986,708.72 USD | `-53.97%` | 173,951,200.50 USD | `-0.92` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `7721.02` | `7722.06` | `7701.32` | `7711.44` | `39,546` | 304,956,606.24 USD | -74,107,102.00 USD | `-24.30%` | -8,316,693.76 USD | `-0.87` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `7711.32` | `7725.53` | `7710.82` | `7724.79` | `32,993` | 254,863,996.47 USD | 229,377,596.82 USD | `+90.00%` | 221,060,903.06 USD | `+2.32` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `7724.79` | `7726.55` | `7719.05` | `7725.58` | `26,093` | 201,583,558.94 USD | 85,337,039.95 USD | `+42.33%` | 306,397,943.02 USD | `+0.73` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `7723.04` | `7728.26` | `7697.54` | `7711.79` | `145,347` | 1,120,885,541.13 USD | -245,741,019.52 USD | `-21.92%` | 325,189,153.90 USD | `-1.04` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `7711.83` | `7727.02` | `7701.32` | `7711.44` | `167,782` | 1,293,840,826.08 USD | -147,256,202.97 USD | `-11.38%` | 177,932,950.93 USD | `-0.62` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `7711.32` | `7732.02` | `7710.82` | `7726.08` | `112,784` | 871,378,206.72 USD | 494,877,057.02 USD | `+56.79%` | 672,810,007.95 USD | `+1.68` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `7723.28` | `7738.99` | `7710.02` | `7724.51` | `191,595` | 1,479,977,493.45 USD | 31,673,664.00 USD | `+2.14%` | -1,321,480,923.80 USD | `+0.47` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `7724.51` | `7736.52` | `7709.78` | `7723.03` | `209,680` | 1,619,364,930.40 USD | -52,081,295.44 USD | `-3.22%` | -1,373,562,219.24 USD | `+0.32` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `7723.04` | `7732.02` | `7697.54` | `7719.53` | `510,982` | 3,944,540,878.46 USD | 342,630,508.44 USD | `+8.69%` | -1,030,931,710.80 USD | `+0.75` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `7728.41` | `7733.22` | `7707.49` | `7724.70` | `121,469` | 938,311,584.30 USD | 90,804,346.87 USD | `+9.68%` | -1,578,135,608.35 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `7724.71` | `7731.99` | `7705.30` | `7723.29` | `197,582` | 1,525,983,084.78 USD | 224,981,020.55 USD | `+14.74%` | -1,353,154,587.80 USD | `+0.78` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `7723.28` | `7738.99` | `7710.02` | `7724.51` | `191,595` | 1,479,977,493.45 USD | 31,673,664.00 USD | `+2.14%` | -1,321,480,923.80 USD | `+0.47` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `7724.51` | `7736.52` | `7709.78` | `7723.03` | `209,680` | 1,619,364,930.40 USD | -52,081,295.44 USD | `-3.22%` | -1,373,562,219.24 USD | `+0.32` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `7723.04` | `7732.02` | `7697.54` | `7719.53` | `510,982` | 3,944,540,878.46 USD | 342,630,508.44 USD | `+8.69%` | -1,030,931,710.80 USD | `+0.75` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| `BID` | `7698.30` | `0.0260` | 200.16 USD | 2,245,242.09 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `7698.40` | `1.6230` | 12,494.50 USD | 2,245,041.93 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `7698.50` | `10.6700` | 82,142.99 USD | 2,232,547.43 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `7698.60` | `0.0470` | 361.83 USD | 2,150,404.43 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `7698.70` | `34.0430` | 262,086.84 USD | 2,150,042.60 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `7698.80` | `12.2280` | 94,140.93 USD | 1,887,955.76 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `7698.90` | `2.4240` | 18,662.13 USD | 1,793,814.83 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `7699.00` | `70.8910` | 545,789.81 USD | 1,775,152.70 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `7699.10` | `3.1180` | 24,005.79 USD | 1,229,362.89 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `7699.30` | `0.4110` | 3,164.41 USD | 1,205,357.09 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `7699.40` | `11.6860` | 89,975.19 USD | 1,202,192.68 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `7699.50` | `2.5480` | 19,618.33 USD | 1,112,217.49 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `7699.60` | `25.3690` | 195,331.15 USD | 1,092,599.17 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `7699.70` | `25.9850` | 200,076.70 USD | 897,268.01 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `7699.90` | `33.6730` | 259,278.73 USD | 697,191.31 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `7700.00` | `13.7460` | 105,844.20 USD | 437,912.58 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `7700.10` | `0.6920` | 5,328.47 USD | 332,068.38 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `7700.30` | `0.0020` | 15.40 USD | 326,739.91 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `7700.40` | `0.0690` | 531.33 USD | 326,724.51 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `7700.50` | `42.3600` | 326,193.18 USD | 326,193.18 USD | `3 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `7700.55` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 7,700.55` | `0.00%` | `-` |
| `ASK` | `7700.60` | `4.4720` | 34,437.08 USD | 34,437.08 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `7700.80` | `1.6310` | 12,560.00 USD | 46,997.09 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `7701.10` | `14.2830` | 109,994.81 USD | 156,991.90 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `7701.20` | `14.8020` | 113,993.16 USD | 270,985.06 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `7701.30` | `2.5960` | 19,992.57 USD | 290,977.64 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `7701.40` | `9.8830` | 76,112.94 USD | 367,090.57 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `7701.50` | `1.9950` | 15,364.49 USD | 382,455.07 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `7701.60` | `14.4420` | 111,226.51 USD | 493,681.57 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `7701.70` | `32.6650` | 251,576.03 USD | 745,257.60 USD | `5 orders` | `+0.01%` | `-` |
| `ASK` | `7701.80` | `54.4280` | 419,193.57 USD | 1,164,451.17 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `7701.90` | `3.1430` | 24,207.07 USD | 1,188,658.24 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `7702.00` | `1.2400` | 9,550.48 USD | 1,198,208.72 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `7702.10` | `12.2130` | 94,065.75 USD | 1,292,274.47 USD | `5 orders` | `+0.02%` | `-` |
| `ASK` | `7702.20` | `9.0730` | 69,882.06 USD | 1,362,156.53 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `7702.30` | `66.4150` | 511,548.25 USD | 1,873,704.79 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `7702.40` | `26.4370` | 203,628.35 USD | 2,077,333.14 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `7702.50` | `16.8870` | 130,072.12 USD | 2,207,405.25 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `7702.60` | `4.0350` | 31,079.99 USD | 2,238,485.24 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `7702.70` | `0.4050` | 3,119.59 USD | 2,241,604.84 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `7702.80` | `0.0470` | 362.03 USD | 2,241,966.87 USD | `1 orders` | `+0.03%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 23:45:33 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `30` | `0x8af7...fa05` | `LONG` | 43,066,171.15 USD | `5,594.10` | `7171.77` | `7697.00` | `4113.57` | 2,946,556.05 USD | `+6.84%` | `20X Cross` |
| `44` | `0x42bc...3946` | `SHORT` | 28,941,829.40 USD | `3,759.56` | `7713.23` | `7697.00` | `8266.88` | 56,521.42 USD | `+0.20%` | `20X Cross` |
| `95` | `0x50a4...8168` | `SHORT` | 19,728,573.25 USD | `2,563.15` | `7144.92` | `7697.00` | `9285.36` | -1,415,066.17 USD | `-7.17%` | `5X Cross` |
| `109` | `0xb4ea...f6e8` | `SHORT` | 18,683,435.37 USD | `2,426.96` | `7692.89` | `7697.00` | `8013.46` | -13,141.05 USD | `-0.07%` | `50X Cross` |
| `128` | `0x0911...129a` | `SHORT` | 15,827,003.52 USD | `2,056.18` | `7105.30` | `7697.00` | `8247.36` | -1,217,257.74 USD | `-7.69%` | `20X Cross` |
| `136` | `0xe9ff...5903` | `LONG` | 15,059,139.34 USD | `1,955.96` | `7756.25` | `7697.00` | `0.000000` | -111,777.76 USD | `-0.74%` | `10X Cross` |
| `151` | `0x9dea...d617` | `LONG` | 13,983,656.92 USD | `1,816.37` | `7653.45` | `7697.00` | `7081.04` | 82,186.36 USD | `+0.59%` | `50X Cross` |
| `193` | `0x7fda...17d1` | `LONG` | 11,142,964.28 USD | `1,447.53` | `7726.15` | `7697.00` | `1697.33` | -40,886.48 USD | `-0.37%` | `10X Cross` |
| `196` | `0x0742...57c2` | `LONG` | 11,008,426.00 USD | `1,430.00` | `7694.69` | `7697.00` | `7250.14` | 5,016.49 USD | `+0.05%` | `50X Cross` |
| `260` | `0x5d2f...9bb7` | `LONG` | 9,236,923.40 USD | `1,200.07` | `6970.52` | `7697.00` | `6699.98` | 871,830.77 USD | `+9.44%` | `20X Isolated` |
| `265` | `0x2322...895a` | `LONG` | 9,101,489.48 USD | `1,182.29` | `7690.42` | `7697.00` | `7362.47` | 9,201.14 USD | `+0.10%` | `50X Cross` |
| `322` | `0xc671...411d` | `SHORT` | 7,697,300.00 USD | `1,000.00` | `7712.56` | `7697.00` | `7960.67` | 15,264.77 USD | `+0.20%` | `50X Cross` |
| `343` | `0xd8c5...99b0` | `LONG` | 6,928,508.43 USD | `900.16` | `7707.48` | `7697.00` | `0.000000` | -9,435.27 USD | `-0.14%` | `8X Cross` |
| `358` | `0xf141...a01d` | `SHORT` | 6,709,120.84 USD | `871.65` | `7355.40` | `7697.00` | `10520.09` | -297,757.39 USD | `-4.44%` | `20X Cross` |
| `579` | `0xc3b1...9a03` | `SHORT` | 4,002,856.00 USD | `520.00` | `7700.59` | `7697.00` | `8718.82` | 1,449.78 USD | `+0.04%` | `7X Cross` |
| `582` | `0xe025...95a8` | `SHORT` | 3,976,101.89 USD | `516.56` | `7742.85` | `7697.00` | `7966.79` | 23,528.60 USD | `+0.59%` | `50X Cross` |
| `605` | `0xb322...d51f` | `LONG` | 3,849,250.00 USD | `500.00` | `7651.00` | `7697.00` | `5943.87` | 23,750.00 USD | `+0.62%` | `20X Cross` |
| `606` | `0xa314...3a81` | `LONG` | 3,848,900.00 USD | `500.00` | `7638.23` | `7697.00` | `6943.25` | 29,786.08 USD | `+0.77%` | `10X Isolated` |
| `654` | `0x45d2...4029` | `LONG` | 3,540,620.00 USD | `460.00` | `6574.84` | `7697.00` | `3946.34` | 516,195.19 USD | `+14.58%` | `4X Isolated` |
| `759` | `0x6ad0...5af1` | `SHORT` | 3,079,480.00 USD | `400.00` | `7572.77` | `7697.00` | `9001.47` | -50,369.94 USD | `-1.64%` | `20X Cross` |
| `760` | `0xa243...f989` | `SHORT` | 3,079,400.00 USD | `400.00` | `7416.79` | `7697.00` | `8739.83` | -112,682.07 USD | `-3.66%` | `13X Cross` |
| `851` | `0xcfbb...9c6d` | `LONG` | 2,693,504.99 USD | `349.87` | `7407.73` | `7697.00` | `6743.88` | 101,731.50 USD | `+3.78%` | `50X Cross` |
| `859` | `0x9cf6...959f` | `SHORT` | 2,661,987.20 USD | `345.77` | `7614.52` | `7697.00` | `7914.67` | -29,105.28 USD | `-1.09%` | `20X Isolated` |
| `875` | `0xfc27...9d9d` | `LONG` | 2,605,349.83 USD | `338.49` | `7707.24` | `7697.00` | `0.000000` | -3,467.74 USD | `-0.13%` | `30X Cross` |
| `908` | `0xcf53...b70f` | `LONG` | 2,521,943.92 USD | `327.59` | `7737.06` | `7697.00` | `7656.79` | -12,630.95 USD | `-0.50%` | `50X Isolated` |
| `981` | `0xf8b5...e2bb` | `LONG` | 2,336,525.54 USD | `303.50` | `7781.16` | `7697.00` | `7307.08` | -25,087.14 USD | `-1.07%` | `20X Isolated` |
| `990` | `0x5238...54e5` | `SHORT` | 2,309,550.00 USD | `300.00` | `7702.48` | `7697.00` | `8256.33` | 1,194.34 USD | `+0.05%` | `20X Isolated` |
| `991` | `0xff2c...efde` | `LONG` | 2,309,340.00 USD | `300.00` | `7698.29` | `7697.00` | `6891.04` | -147.19 USD | `-0.01%` | `50X Cross` |
| `1081` | `0x5f96...d6ca` | `LONG` | 2,081,220.19 USD | `270.34` | `7728.48` | `7697.00` | `3341.75` | -8,104.88 USD | `-0.39%` | `10X Cross` |
| `1082` | `0x9abb...84d8` | `SHORT` | 2,078,406.00 USD | `270.00` | `7711.80` | `7697.00` | `8664.61` | 3,780.00 USD | `+0.18%` | `50X Cross` |
| `1150` | `0x7f2e...6f84` | `LONG` | 1,979,740.49 USD | `257.20` | `7784.96` | `7697.00` | `7473.19` | -22,520.94 USD | `-1.14%` | `40X Isolated` |
| `1188` | `0x296e...0a04` | `SHORT` | 1,924,325.00 USD | `250.00` | `6567.55` | `7697.00` | `8202.06` | -282,437.54 USD | `-14.68%` | `5X Isolated` |
| `1190` | `0x572c...6a90` | `SHORT` | 1,918,577.63 USD | `249.21` | `7632.81` | `7697.00` | `7791.47` | -16,419.68 USD | `-0.86%` | `50X Cross` |
| `1369` | `0xbb1a...f1c8` | `SHORT` | 1,648,102.58 USD | `214.08` | `7525.58` | `7697.00` | `8217.36` | -37,019.12 USD | `-2.25%` | `10X Isolated` |
| `1371` | `0xfc66...ca06` | `SHORT` | 1,645,395.39 USD | `213.77` | `7713.31` | `7697.00` | `205740.74` | 3,485.68 USD | `+0.21%` | `3X Cross` |
| `1400` | `0x0a26...5255` | `SHORT` | 1,616,685.00 USD | `210.00` | `7642.25` | `7697.00` | `7947.86` | -11,813.24 USD | `-0.73%` | `20X Cross` |
| `1402` | `0x9751...a97e` | `SHORT` | 1,616,622.00 USD | `210.00` | `7650.71` | `7697.00` | `25718.39` | -9,972.56 USD | `-0.62%` | `10X Cross` |
| `1481` | `0x897e...de99` | `SHORT` | 1,530,084.57 USD | `198.75` | `7269.18` | `7697.00` | `8656.37` | -85,328.08 USD | `-5.58%` | `5X Isolated` |
| `1502` | `0x321f...1c84` | `SHORT` | 1,499,899.23 USD | `194.82` | `7650.70` | `7697.00` | `9419.09` | -9,350.53 USD | `-0.62%` | `10X Cross` |
| `1532` | `0x1c2c...09fe` | `LONG` | 1,456,808.65 USD | `189.25` | `7573.39` | `7697.00` | `5753.74` | 23,543.84 USD | `+1.62%` | `50X Cross` |
| `1672` | `0xec5b...9bc6` | `LONG` | 1,308,779.00 USD | `170.00` | `7665.72` | `7697.00` | `5147.75` | 5,605.77 USD | `+0.43%` | `50X Cross` |
| `1742` | `0x4301...f5ed` | `SHORT` | 1,231,760.00 USD | `160.00` | `7230.50` | `7697.00` | `8054.42` | -74,879.21 USD | `-6.08%` | `50X Cross` |
| `1762` | `0x6adc...072d` | `SHORT` | 1,213,207.34 USD | `157.59` | `7721.67` | `7697.00` | `8932.73` | 3,620.47 USD | `+0.30%` | `20X Cross` |
| `1783` | `0xb3e4...806f` | `LONG` | 1,193,221.00 USD | `155.00` | `7717.31` | `7697.00` | `0.000000` | -2,962.12 USD | `-0.25%` | `20X Cross` |
| `1826` | `0xebcd...fcf4` | `LONG` | 1,155,574.87 USD | `150.10` | `7743.09` | `7697.00` | `3987.21` | -6,663.69 USD | `-0.58%` | `50X Cross` |
| `1827` | `0x9e11...e762` | `LONG` | 1,154,595.00 USD | `150.00` | `7500.14` | `7697.00` | `7510.71` | 29,574.42 USD | `+2.56%` | `50X Cross` |
| `1972` | `0xbc26...bde1` | `SHORT` | 1,034,370.46 USD | `134.36` | `7693.30` | `7697.00` | `9169.27` | -698.67 USD | `-0.07%` | `50X Cross` |
| `1978` | `0xfc37...3b84` | `LONG` | 1,030,968.66 USD | `133.94` | `7738.49` | `7697.00` | `4613.68` | -5,517.48 USD | `-0.54%` | `50X Cross` |
| `1996` | `0x7e41...1c3e` | `LONG` | 1,016,202.00 USD | `132.00` | `7706.86` | `7697.00` | `2469.02` | -1,103.10 USD | `-0.11%` | `14X Cross` |
| `2003` | `0xbe50...877b` | `SHORT` | 1,012,898.36 USD | `131.58` | `7800.49` | `7697.00` | `9525.65` | 13,458.70 USD | `+1.33%` | `50X Cross` |
| `2005` | `0x1965...17f9` | `LONG` | 1,011,658.95 USD | `131.41` | `7685.82` | `7697.00` | `7628.35` | 1,627.16 USD | `+0.16%` | `50X Cross` |
| `2011` | `0xecb6...2b00` | `SHORT` | 1,007,692.03 USD | `130.91` | `7714.18` | `7697.00` | `93446.78` | 2,210.11 USD | `+0.22%` | `3X Cross` |
| `2033` | `0x1e25...ffa9` | `SHORT` | 1,000,610.00 USD | `130.00` | `7302.28` | `7697.00` | `9311.54` | -51,313.49 USD | `-5.13%` | `9X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 48H Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 3D Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 7D Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Envelope` | `Long Liquidation` | `7673.71` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |
| `Envelope` | `Short Liquidation` | `7729.47` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |

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
  * Current Rate: `0.00` | Last 24h: `0.00` | Last 3d: `0.00` | Last 7d: `439.85`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `-` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `-0.0066%` | **USDT BingX** | `-` |
| **USDT Gate** | `-0.0200%` | **USDT Bitget** | `-` |
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
  * `2026-10-29 23:31:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:26:26 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:03:26 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:26 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 22:55:26 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:51:26 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:51:26 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:50:26 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 23:50:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 23:50:26 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 20:52:26 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:52:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:52:26 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 19:52:26 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:52:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `7709.70` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `7695.16` (Risk Distance: `14.54` pts)
  * +2.5R Take Profit: `7746.04`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.15 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `7727.50` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `7742.04` (Risk Distance: `14.54` pts)
  * +2.5R Take Profit: `7691.16`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.15 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`7763.79`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
