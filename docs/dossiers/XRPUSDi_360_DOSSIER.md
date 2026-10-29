# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XRP
**Canonical Key**: `XRP` | **Broker Instrument**: `XRPUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-29 22:45:58 IST` (`2026-10-29 17:15:58 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1.29` | **Live Ask Quote**: `1.30` | **Mid Price**: `1.30`
- **Spread Points**: `3.00` | **Spread BPS**: `23.14 bps` (Charter Threshold: `25.00 bps`)
- **Gate 1 Clearance**: **`PASS`** | **Execution Posture**: `PASSIVE LIMIT ONLY` | **Order Type Allowed**: `BUY_LIMIT / SELL_LIMIT`
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
  * Session VWAP: `1.29` | VWAP Z-Score: `+0.38` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0067` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.63` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.32` | Lower -3.00σ Band: `1.27`
  * Upper +2.51σ Band: `1.32` | Lower -2.51σ Band: `1.27`
  * Upper +2.01σ Band: `1.31` | Lower -2.01σ Band: `1.28`
  * Upper +2.00σ Band: `1.31` | Lower -2.00σ Band: `1.28`
  * Upper +1.28σ Band: `1.30` | Lower -1.28σ Band: `1.28`
  * Upper +1.00σ Band: `1.30` | Lower -1.00σ Band: `1.29`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1.30` | EMA-20=`1.30` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1.30` (Slope: `+0.0000`) | EMA-100=`1.30`
  * Institutional Anchors: EMA-144=`1.30` | EMA-200=`1.30` (Slope: `-0.0296`) | EMA-233=`1.30`
- **Range Boundaries**: 24H High=`1.34` | 24H Low=`1.28` | Weekly High=`1.34` | Weekly Low=`1.28`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.30` (Distance: `-0.17%`)
  * Point of Control (POC) = `1.29` (Distance: `+0.63%`)
  * Value Area Low (VAL) = `1.28` (Distance: `+1.03%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1.33` | POC=`1.33` | VAL=`1.32`
  * Prior Day Extremes: PDH=`1.34` | PDL=`1.30` | PDC=`1.33`
  * Monday Range Blueprint: High=`1.30` | Mid=`1.29` | Low=`1.27`
  * Developing Weekly Value Area: Weekly VAH=`1.31` | Weekly POC=`1.29` | Weekly VAL=`1.28`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1.33` | Low=`1.28`
  * London Session (08:00-16:00 UTC): High=`1.30` | Low=`1.28`
  * New York Session (13:00-21:00 UTC): High=`1.31` | Low=`1.28`
  * Initial Balance (First Hour): IB High=`1.30` | IB Low=`1.29`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1.29` - `1.30`
  * Optimal Trade Entry (OTE 0.705): `1.30`
  * Structural Invalidation Anchor (0.786): `1.31`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `1.30` | `1.30` | `1.30` | `1.30` | `1,414,620` | 1,837,086.29 USD | -147,547.29 USD | `-8.03%` | -21,606,684.87 USD | `+0.09` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `1.30` | `1.30` | `1.30` | `1.30` | `3,197,004` | 4,145,508.01 USD | -1,140,072.44 USD | `-27.50%` | -22,746,757.31 USD | `-1.08` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `1.30` | `1.30` | `1.30` | `1.30` | `1,743,660` | 2,261,911.87 USD | 998,804.26 USD | `+44.16%` | -21,747,953.05 USD | `+1.40` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `1.30` | `1.30` | `1.30` | `1.30` | `7,848,039` | 10,205,311.65 USD | -1,193,506.66 USD | `-11.69%` | -21,679,226.41 USD | `-0.95` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `1.30` | `1.30` | `1.30` | `1.30` | `3,676,406` | 4,776,328.08 USD | 220,088.84 USD | `+4.61%` | -21,459,137.57 USD | `+0.27` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `1.30` | `1.30` | `1.30` | `1.30` | `6,365,906` | 8,258,294.20 USD | -302,603.50 USD | `-3.66%` | -21,761,741.08 USD | `-0.18` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `1.30` | `1.31` | `1.30` | `1.31` | `30,464,520` | 39,839,799.06 USD | 106,608.94 USD | `+0.27%` | -19,101,925.36 USD | `+0.38` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `1.31` | `1.32` | `1.30` | `1.30` | `30,534,069` | 39,864,527.69 USD | -3,664,960.48 USD | `-9.19%` | -22,766,885.83 USD | `-0.63` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `1.30` | `1.30` | `1.30` | `1.30` | `6,355,284` | 8,244,506.18 USD | -288,815.48 USD | `-3.50%` | -23,055,701.31 USD | `+0.34` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `1.29` | `1.30` | `1.29` | `1.29` | `51,543,790` | 66,567,053.49 USD | -1,316,863.99 USD | `-1.98%` | -26,364,168.80 USD | `+0.55` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.29` | `1.31` | `1.29` | `1.31` | `105,451,962` | 136,952,441.12 USD | 1,861,993.66 USD | `+1.36%` | -24,502,175.14 USD | `+0.73` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.31` | `1.32` | `1.30` | `1.30` | `36,899,974` | 48,122,821.89 USD | -3,967,563.98 USD | `-8.24%` | -28,469,739.12 USD | `+0.09` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.33` | `1.33` | `1.29` | `1.29` | `112,558,954` | 146,533,666.97 USD | -23,231,128.88 USD | `-15.85%` | -23,206,069.15 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.29` | `1.30` | `1.29` | `1.29` | `60,938,672` | 78,900,359.45 USD | -1,841,235.66 USD | `-2.33%` | -25,047,304.81 USD | `+0.62` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `1.29` | `1.30` | `1.29` | `1.29` | `51,543,790` | 66,567,053.49 USD | -1,316,863.99 USD | `-1.98%` | -26,364,168.80 USD | `+0.55` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.29` | `1.31` | `1.29` | `1.31` | `105,451,962` | 136,952,441.12 USD | 1,861,993.66 USD | `+1.36%` | -24,502,175.14 USD | `+0.73` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.31` | `1.32` | `1.30` | `1.30` | `36,899,974` | 48,122,821.89 USD | -3,967,563.98 USD | `-8.24%` | -28,469,739.12 USD | `+0.09` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`1.30`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `ASK` | `1.30` | `94573.0000` | 122,935.44 USD | 2,516,283.63 USD | `10 orders` | `+0.15%` | `-` |
| `ASK` | `1.30` | `427152.0000` | 555,212.17 USD | 2,393,348.19 USD | `10 orders` | `+0.14%` | `-` |
| `ASK` | `1.30` | `278734.0000` | 362,270.58 USD | 1,838,136.02 USD | `9 orders` | `+0.13%` | `-` |
| `ASK` | `1.30` | `61424.0000` | 79,826.63 USD | 1,475,865.44 USD | `11 orders` | `+0.13%` | `-` |
| `ASK` | `1.30` | `85075.0000` | 110,554.96 USD | 1,396,038.81 USD | `12 orders` | `+0.12%` | `-` |
| `ASK` | `1.30` | `39702.0000` | 51,588.78 USD | 1,285,483.85 USD | `5 orders` | `+0.11%` | `-` |
| `ASK` | `1.30` | `71974.0000` | 93,515.82 USD | 1,233,895.07 USD | `10 orders` | `+0.10%` | `-` |
| `ASK` | `1.30` | `141071.0000` | 183,279.44 USD | 1,140,379.25 USD | `8 orders` | `+0.10%` | `-` |
| `ASK` | `1.30` | `55158.0000` | 71,655.76 USD | 957,099.81 USD | `12 orders` | `+0.09%` | `-` |
| `ASK` | `1.30` | `39376.0000` | 51,149.42 USD | 885,444.05 USD | `10 orders` | `+0.08%` | `-` |
| `ASK` | `1.30` | `25652.0000` | 33,319.38 USD | 834,294.63 USD | `6 orders` | `+0.07%` | `-` |
| `ASK` | `1.30` | `327313.0000` | 425,114.12 USD | 800,975.24 USD | `12 orders` | `+0.07%` | `-` |
| `ASK` | `1.30` | `85936.0000` | 111,605.08 USD | 375,861.12 USD | `15 orders` | `+0.06%` | `-` |
| `ASK` | `1.30` | `35854.0000` | 46,560.00 USD | 264,256.04 USD | `8 orders` | `+0.05%` | `-` |
| `ASK` | `1.30` | `51034.0000` | 66,267.65 USD | 217,696.03 USD | `12 orders` | `+0.04%` | `-` |
| `ASK` | `1.30` | `47186.0000` | 61,266.30 USD | 151,428.38 USD | `10 orders` | `+0.03%` | `-` |
| `ASK` | `1.30` | `44325.0000` | 57,547.15 USD | 90,162.08 USD | `7 orders` | `+0.03%` | `-` |
| `ASK` | `1.30` | `17353.0000` | 22,527.66 USD | 32,614.93 USD | `6 orders` | `+0.02%` | `-` |
| `ASK` | `1.30` | `5100.0000` | 6,620.31 USD | 10,087.27 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `1.30` | `2671.0000` | 3,466.96 USD | 3,466.96 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `1.30` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 1.30` | `0.00%` | `-` |
| `BID` | `1.30` | `15924.0000` | 20,667.76 USD | 20,667.76 USD | `4 orders` | `-0.00%` | `-` |
| `BID` | `1.30` | `23077.0000` | 29,949.33 USD | 50,617.09 USD | `11 orders` | `-0.01%` | `-` |
| `BID` | `1.30` | `46616.0000` | 60,493.58 USD | 111,110.67 USD | `10 orders` | `-0.02%` | `-` |
| `BID` | `1.30` | `50590.0000` | 65,645.58 USD | 176,756.26 USD | `17 orders` | `-0.03%` | `-` |
| `BID` | `1.30` | `43111.0000` | 55,936.52 USD | 232,692.78 USD | `14 orders` | `-0.03%` | `-` |
| `BID` | `1.30` | `115055.0000` | 149,272.36 USD | 381,965.14 USD | `14 orders` | `-0.04%` | `-` |
| `BID` | `1.30` | `74644.0000` | 96,835.66 USD | 478,800.80 USD | `13 orders` | `-0.05%` | `-` |
| `BID` | `1.30` | `350886.0000` | 455,169.32 USD | 933,970.12 USD | `14 orders` | `-0.06%` | `-` |
| `BID` | `1.30` | `147808.0000` | 191,721.76 USD | 1,125,691.87 USD | `17 orders` | `-0.07%` | `-` |
| `BID` | `1.30` | `95097.0000` | 123,340.81 USD | 1,249,032.68 USD | `10 orders` | `-0.07%` | `-` |
| `BID` | `1.30` | `252484.0000` | 327,446.50 USD | 1,576,479.18 USD | `14 orders` | `-0.08%` | `-` |
| `BID` | `1.30` | `95929.0000` | 124,400.73 USD | 1,700,879.91 USD | `9 orders` | `-0.09%` | `-` |
| `BID` | `1.30` | `22004.0000` | 28,532.59 USD | 1,729,412.50 USD | `9 orders` | `-0.10%` | `-` |
| `BID` | `1.30` | `344313.0000` | 446,436.24 USD | 2,175,848.73 USD | `11 orders` | `-0.10%` | `-` |
| `BID` | `1.30` | `328356.0000` | 425,713.55 USD | 2,601,562.29 USD | `10 orders` | `-0.11%` | `-` |
| `BID` | `1.30` | `80164.0000` | 103,924.61 USD | 2,705,486.90 USD | `6 orders` | `-0.12%` | `-` |
| `BID` | `1.30` | `78901.0000` | 102,279.37 USD | 2,807,766.26 USD | `14 orders` | `-0.13%` | `-` |
| `BID` | `1.30` | `46107.0000` | 59,763.89 USD | 2,867,530.16 USD | `5 orders` | `-0.13%` | `-` |
| `BID` | `1.30` | `73005.0000` | 94,621.78 USD | 2,962,151.94 USD | `6 orders` | `-0.14%` | `-` |
| `BID` | `1.30` | `616390.0000` | 798,841.44 USD | 3,760,993.38 USD | `11 orders` | `-0.15%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 22:44:58 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `26` | `0x31b1...1434` | `LONG` | 45,456,783.57 USD | `35,031,430.00` | `1.13` | `1.30` | `0.9611` | 5,877,900.30 USD | `+12.93%` | `10X Cross` |
| `93` | `0x5b5d...c060` | `SHORT` | 20,295,430.85 USD | `15,652,808.00` | `1.44` | `1.30` | `10.94` | 2,219,582.40 USD | `+10.94%` | `5X Cross` |
| `150` | `0x58f0...0d20` | `LONG` | 14,188,161.28 USD | `10,931,629.00` | `1.36` | `1.30` | `1.25` | -676,991.68 USD | `-4.77%` | `20X Cross` |
| `159` | `0xb83d...6e36` | `SHORT` | 13,687,252.02 USD | `10,555,450.00` | `1.50` | `1.30` | `13.25` | 2,135,317.63 USD | `+15.60%` | `5X Cross` |
| `450` | `0xca49...53c8` | `SHORT` | 5,372,274.03 USD | `4,138,886.00` | `1.44` | `1.30` | `4.30` | 581,048.70 USD | `+10.82%` | `20X Cross` |
| `470` | `0xfc27...9d9d` | `SHORT` | 5,134,027.73 USD | `3,959,608.00` | `1.31` | `1.30` | `4.81` | 71,179.15 USD | `+1.39%` | `20X Cross` |
| `521` | `0x610b...b613` | `LONG` | 4,599,687.51 USD | `3,543,946.00` | `1.44` | `1.30` | `0.6869` | -500,305.10 USD | `-10.88%` | `5X Cross` |
| `552` | `0xc30c...a4c9` | `SHORT` | 4,287,633.94 USD | `3,302,753.00` | `1.42` | `1.30` | `1.60` | 412,252.90 USD | `+9.61%` | `8X Cross` |
| `564` | `0xdd53...2b13` | `SHORT` | 4,185,493.15 USD | `3,227,306.00` | `1.44` | `1.30` | `18.12` | 459,893.29 USD | `+10.99%` | `3X Cross` |
| `601` | `0xecb6...2b00` | `SHORT` | 3,978,272.20 USD | `3,068,234.00` | `1.31` | `1.30` | `12.01` | 32,419.29 USD | `+0.81%` | `10X Cross` |
| `611` | `0x9946...0852` | `SHORT` | 3,923,266.46 USD | `3,025,111.00` | `1.43` | `1.30` | `1.62` | 389,918.10 USD | `+9.94%` | `20X Cross` |
| `699` | `0x9aa5...58af` | `SHORT` | 3,379,844.53 USD | `2,604,083.00` | `1.46` | `1.30` | `4.05` | 417,876.12 USD | `+12.36%` | `20X Cross` |
| `716` | `0xf48f...10fe` | `LONG` | 3,327,045.63 USD | `2,565,779.00` | `1.53` | `1.30` | `0.8951` | -597,595.10 USD | `-17.96%` | `4X Cross` |
| `735` | `0x023a...2355` | `SHORT` | 3,239,093.51 USD | `2,498,144.00` | `1.33` | `1.30` | `4.75` | 77,812.17 USD | `+2.40%` | `20X Cross` |
| `748` | `0x45d2...4029` | `SHORT` | 3,182,767.50 USD | `2,453,000.00` | `1.48` | `1.30` | `15.45` | 455,512.92 USD | `+14.31%` | `20X Cross` |
| `1020` | `0xc179...e0c8` | `SHORT` | 2,276,086.65 USD | `1,755,427.00` | `1.30` | `1.30` | `4.85` | 8,376.72 USD | `+0.37%` | `10X Cross` |
| `1085` | `0xeadc...9d55` | `LONG` | 2,102,830.85 USD | `1,619,805.00` | `1.21` | `1.30` | `0.000000` | 143,987.83 USD | `+6.85%` | `20X Cross` |
| `1090` | `0xfc66...ca06` | `SHORT` | 2,099,359.89 USD | `1,619,002.00` | `1.31` | `1.30` | `22.48` | 22,042.79 USD | `+1.05%` | `20X Cross` |
| `1150` | `0x94b2...599e` | `SHORT` | 1,999,207.13 USD | `1,540,696.00` | `1.36` | `1.30` | `1.81` | 101,259.32 USD | `+5.06%` | `20X Cross` |
| `1171` | `0xbcd4...0dd2` | `SHORT` | 1,982,946.19 USD | `1,529,461.00` | `1.31` | `1.30` | `2.25` | 21,598.41 USD | `+1.09%` | `20X Cross` |
| `1183` | `0x3fc5...c0c1` | `SHORT` | 1,960,021.47 USD | `1,511,779.00` | `1.52` | `1.30` | `2.56` | 331,593.13 USD | `+16.92%` | `20X Cross` |
| `1220` | `0x31ef...f715` | `LONG` | 1,914,506.33 USD | `1,475,080.00` | `1.49` | `1.30` | `1.04` | -284,759.07 USD | `-14.87%` | `3X Isolated` |
| `1270` | `0x7737...bf66` | `SHORT` | 1,834,113.48 USD | `1,413,466.00` | `1.41` | `1.30` | `14.46` | 164,755.17 USD | `+8.98%` | `10X Cross` |
| `1292` | `0xef96...9383` | `SHORT` | 1,805,794.90 USD | `1,390,999.00` | `1.34` | `1.30` | `3.90` | 57,990.32 USD | `+3.21%` | `20X Cross` |
| `1362` | `0xee2b...d67e` | `LONG` | 1,693,727.83 USD | `1,306,284.00` | `1.55` | `1.30` | `0.2207` | -336,927.07 USD | `-19.89%` | `4X Cross` |
| `1415` | `0x215d...f80a` | `LONG` | 1,625,056.90 USD | `1,251,777.00` | `1.32` | `1.30` | `1.19` | -29,397.33 USD | `-1.81%` | `14X Cross` |
| `1471` | `0x123d...3bff` | `LONG` | 1,577,010.91 USD | `1,215,329.00` | `1.35` | `1.30` | `0.000000` | -60,058.31 USD | `-3.81%` | `10X Cross` |
| `1509` | `0x95da...2328` | `LONG` | 1,520,549.74 USD | `1,171,817.00` | `1.37` | `1.30` | `0.000000` | -81,226.25 USD | `-5.34%` | `5X Cross` |
| `1514` | `0xdf95...7d72` | `SHORT` | 1,504,184.36 USD | `1,160,099.00` | `1.37` | `1.30` | `32.29` | 89,154.37 USD | `+5.93%` | `20X Cross` |
| `1592` | `0x5fa3...35b7` | `SHORT` | 1,428,228.87 USD | `1,101,009.00` | `1.31` | `1.30` | `2.98` | 13,619.67 USD | `+0.95%` | `20X Cross` |
| `1679` | `0xb1ce...681b` | `LONG` | 1,325,636.61 USD | `1,021,764.00` | `1.49` | `1.30` | `1.16` | -198,419.88 USD | `-14.97%` | `4X Isolated` |
| `1686` | `0x4537...8732` | `SHORT` | 1,321,378.99 USD | `1,018,875.00` | `1.32` | `1.30` | `2.24` | 19,437.91 USD | `+1.47%` | `10X Cross` |
| `1778` | `0x3c36...461a` | `LONG` | 1,220,186.20 USD | `940,051.00` | `1.30` | `1.30` | `1.06` | 1,105.58 USD | `+0.09%` | `10X Cross` |
| `2004` | `0xbfc7...80b4` | `SHORT` | 1,037,760.00 USD | `800,000.00` | `1.48` | `1.30` | `6.53` | 145,694.65 USD | `+14.04%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1.32` | 17,109.01 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 17.11K USD at 1.3231 USD [API] | `2026-10-27 19:18:58` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 7,024.34 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.02K USD at 1.3231 USD [API] | `2026-10-27 19:18:58` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 6,853.66 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.85K USD at 1.3231 USD [API] | `2026-10-27 19:18:58` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 9,366.93 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 9.37K USD at 1.3232 USD [API] | `2026-10-27 19:18:58` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 10,313.02 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 10.31K USD at 1.3232 USD [API] | `2026-10-27 19:18:58` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,006.61 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3224 USD [API] | `2026-10-27 19:25:01` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 6,941.03 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.94K USD at 1.3221 USD [API] | `2026-10-27 19:32:19` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 8,142.63 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 8.14K USD at 1.3225 USD [API] | `2026-10-27 19:34:38` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 12,586.65 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 12.59K USD at 1.3231 USD [API] | `2026-10-27 19:40:33` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 6,236.71 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 6.24K USD at 1.3233 USD [API] | `2026-10-27 19:50:17` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 7,372.17 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 7.37K USD at 1.3245 USD [API] | `2026-10-27 19:58:34` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 7,956.27 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 7.96K USD at 1.3245 USD [API] | `2026-10-27 19:58:33` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 6,333.76 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 6.33K USD at 1.3245 USD [API] | `2026-10-27 19:58:33` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,005.29 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.3245 USD [API] | `2026-10-27 19:58:33` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 7,354.95 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 7.35K USD at 1.3245 USD [API] | `2026-10-27 19:58:33` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 6,429.39 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 6.43K USD at 1.3251 USD [API] | `2026-10-27 20:05:47` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 8,828.47 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 8.83K USD at 1.3248 USD [API] | `2026-10-27 20:05:41` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,006.42 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3248 USD [API] | `2026-10-27 20:05:41` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,006.42 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3248 USD [API] | `2026-10-27 20:05:41` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 32,202.33 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 32.20K USD at 1.3240 USD [API] | `2026-10-27 20:18:04` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 15,001.31 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 15.00K USD at 1.3231 USD [API] | `2026-10-27 20:20:17` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 13,924.60 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 13.92K USD at 1.3225 USD [API] | `2026-10-27 20:28:31` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 8,592.28 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 8.59K USD at 1.3225 USD [API] | `2026-10-27 20:28:31` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,006.60 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.3217 USD [API] | `2026-10-27 20:30:46` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,006.60 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.3217 USD [API] | `2026-10-27 20:30:46` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 11,874.15 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 11.87K USD at 1.3217 USD [API] | `2026-10-27 20:30:46` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,007.16 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.3215 USD [API] | `2026-10-27 20:30:42` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 37,802.81 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 37.80K USD at 1.3197 USD [API] | `2026-10-27 20:41:48` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 6,861.64 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.86K USD at 1.3198 USD [API] | `2026-10-27 20:41:48` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 8,373.65 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 8.37K USD at 1.3191 USD [API] | `2026-10-27 20:43:35` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 15,275.18 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 15.28K USD at 1.3191 USD [API] | `2026-10-27 20:43:35` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 10,579.33 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 10.58K USD at 1.3206 USD [API] | `2026-10-27 20:49:53` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 10,824.96 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 10.82K USD at 1.3206 USD [API] | `2026-10-27 20:49:49` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 11,449.19 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 11.45K USD at 1.3204 USD [API] | `2026-10-27 21:16:32` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 73,780.32 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 73.78K USD at 1.3180 USD [API] | `2026-10-27 21:24:04` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,005.76 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3180 USD [API] | `2026-10-27 21:24:04` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 8,099.11 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 8.10K USD at 1.3180 USD [API] | `2026-10-27 21:24:04` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 30,750.26 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 30.75K USD at 1.3180 USD [API] | `2026-10-27 21:24:04` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,005.79 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.3187 USD [API] | `2026-10-27 21:26:10` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 10,640.59 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 10.64K USD at 1.3187 USD [API] | `2026-10-27 21:26:10` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 10,188.28 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 10.19K USD at 1.3187 USD [API] | `2026-10-27 21:26:10` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 6,112.17 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 6.11K USD at 1.3187 USD [API] | `2026-10-27 21:26:10` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 6,572.40 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 6.57K USD at 1.3187 USD [API] | `2026-10-27 21:26:10` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 6,590.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.59K USD at 1.3180 USD [API] | `2026-10-27 21:29:26` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 583.89 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.58K USD at 1.2611 USD [API] | `2026-10-18 19:39:16` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 10,779.88 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 10.78K USD at 1.2611 USD [API] | `2026-10-18 19:39:16` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 389.68 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.39K USD at 1.2611 USD [API] | `2026-10-18 19:35:52` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 355.63 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.36K USD at 1.2611 USD [API] | `2026-10-18 19:35:52` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 35,023.27 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 35.02K USD at 1.2611 USD [API] | `2026-10-18 19:35:52` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 721.35 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.72K USD at 1.2611 USD [API] | `2026-10-18 19:35:49` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 94,303.80 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 94.30K USD at 1.2611 USD [API] | `2026-10-18 19:35:49` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 11.40 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.2670 USD [API] | `2026-10-18 19:30:42` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 89.96 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.09K USD at 1.2670 USD [API] | `2026-10-18 19:30:42` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 39,789.10 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 39.79K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 97.79 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.10K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 139.70 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.14K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 30.48 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.03K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 27.94 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.03K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 16,159.48 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 16.16K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 11.43 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 12.70 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 635.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.64K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 82.55 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.08K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 40.64 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.04K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 11.43 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 11.43 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 523.24 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.52K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 424.18 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.42K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 139.70 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.14K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 1,369.06 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.37K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 528.32 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.53K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 34.29 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.03K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 199.39 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.20K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 3,439.16 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 3.44K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 953.77 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.95K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 10.16 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 23,519.13 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 23.52K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 204.47 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.20K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 198.12 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.20K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 57.15 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.06K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 24.13 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.02K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 1,327.15 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.33K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 116.84 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.12K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 11.43 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 739.14 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.74K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 4,381.50 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 4.38K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 107.81 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.11K USD at 1.3310 USD [API] | `2026-10-14 14:37:05` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 25.29 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.03K USD at 1.3310 USD [API] | `2026-10-14 14:37:02` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 2,500.95 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 2.50K USD at 1.3310 USD [API] | `2026-10-14 14:37:02` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 89.18 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.09K USD at 1.3310 USD [API] | `2026-10-14 14:37:02` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 246.23 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.25K USD at 1.3310 USD [API] | `2026-10-14 14:37:02` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 25.35 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.03K USD at 1.3340 USD [API] | `2026-10-14 14:31:12` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 33,375.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 33.38K USD at 1.3350 USD [API] | `2026-10-14 14:28:24` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,345.76 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.35K USD at 1.3288 USD [API] | `2026-10-27 21:37:26` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 6,266.62 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.27K USD at 1.3288 USD [API] | `2026-10-27 21:37:26` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,371.41 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.37K USD at 1.3289 USD [API] | `2026-10-27 21:37:26` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,939.30 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.94K USD at 1.3290 USD [API] | `2026-10-27 21:37:26` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 8,355.42 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 8.36K USD at 1.3290 USD [API] | `2026-10-27 21:37:26` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,633.80 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.63K USD at 1.3281 USD [API] | `2026-10-27 21:39:46` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 12,869.99 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 12.87K USD at 1.3253 USD [API] | `2026-10-27 21:41:02` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 10,391.68 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 10.39K USD at 1.3253 USD [API] | `2026-10-27 21:41:02` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,362.05 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.36K USD at 1.3256 USD [API] | `2026-10-27 21:42:55` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 184.91 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.18K USD at 1.3303 USD [API] | `2026-10-27 21:36:32` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,006.03 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.3261 USD [API] | `2026-10-27 21:46:58` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,006.03 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.3261 USD [API] | `2026-10-27 21:46:58` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 6,482.61 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.48K USD at 1.3265 USD [API] | `2026-10-27 21:51:19` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 8,630.21 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 8.63K USD at 1.3265 USD [API] | `2026-10-27 21:51:19` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,006.03 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3261 USD [API] | `2026-10-27 21:55:58` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1.32` (Vol: 1,700,000.00 USD, Dist: `+2.33%`) | Long MP=`1.28` (Vol: 2,200,000.00 USD, Dist: `--1.10%`)
  * 48H Horizon: Short MP=`1.35` (Vol: 2,700,000.00 USD, Dist: `+4.48%`) | Long MP=`1.28` (Vol: 2,300,000.00 USD, Dist: `--1.19%`)
  * 3D Horizon: Short MP=`1.35` (Vol: 2,600,000.00 USD, Dist: `+4.48%`) | Long MP=`1.28` (Vol: 3,500,000.00 USD, Dist: `--0.63%`)
  * 7D Horizon: Short MP=`1.35` (Vol: 3,300,000.00 USD, Dist: `+4.55%`) | Long MP=`1.28` (Vol: 4,000,000.00 USD, Dist: `--1.15%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.2650` | 4,330.00 USD | 74,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2750` | 379.50 USD | 74,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2850` | 1,500.00 USD | 74,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2950` | 1,060.00 USD | 74,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3150` | 5,060.00 USD | 74,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3450` | 1,010.00 USD | 74,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3550` | 1,140.00 USD | 74,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3650` | 1,900.00 USD | 74,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3750` | 9,820.00 USD | 74,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3850` | 1,250.00 USD | 74,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3950` | 1,320.00 USD | 74,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4050` | 2,620.00 USD | 74,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4150` | 151,310.00 USD | 74,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4250` | 15,910.00 USD | 74,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4350` | 376.27 USD | 74,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4550` | 2,680.00 USD | 74,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4650` | 989.06 USD | 74,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4750` | 3,100.00 USD | 74,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4850` | 30,430.00 USD | 74,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4950` | 3,140.00 USD | 74,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5050` | 6,750.00 USD | 74,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5150` | 2,030.00 USD | 74,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5250` | 50,280.00 USD | 74,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5350` | 10,910.00 USD | 74,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5550` | 2,730.00 USD | 74,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5650` | 374.03 USD | 74,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5750` | 6,200.00 USD | 74,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5850` | 889.20 USD | 74,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5950` | 5,760.00 USD | 74,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6050` | 32,400.00 USD | 74,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6150` | 50,190.00 USD | 74,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6250` | 7,150.00 USD | 74,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6450` | 8,030.00 USD | 74,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6550` | 140,570.00 USD | 74,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6650` | 31,770.00 USD | 74,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6750` | 28,620.00 USD | 74,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6850` | 2,450,000.00 USD | 74,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6950` | 11,360.00 USD | 71,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7050` | 25,010.00 USD | 71,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7150` | 67,440.00 USD | 71,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7250` | 217,680.00 USD | 71,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7350` | 23,650.00 USD | 71,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7450` | 52,420.00 USD | 71,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7550` | 563,960.00 USD | 71,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7650` | 2,190.00 USD | 70,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7750` | 29,790.00 USD | 70,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7850` | 40,330.00 USD | 70,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7950` | 11,580.00 USD | 70,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8050` | 22,350.00 USD | 70,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8150` | 22,650.00 USD | 70,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8250` | 11,200.00 USD | 70,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8350` | 44,490.00 USD | 70,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8450` | 70,540.00 USD | 70,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8550` | 165,960.00 USD | 70,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8650` | 28,530.00 USD | 70,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8750` | 128,340.00 USD | 70,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8850` | 357,260.00 USD | 70,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8950` | 2,390,000.00 USD | 69,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9050` | 151,820.00 USD | 67,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9150` | 26,030.00 USD | 67,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9250` | 647,340.00 USD | 67,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9350` | 86,480.00 USD | 66,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9450` | 79,680.00 USD | 66,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9550` | 238,350.00 USD | 66,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9650` | 34,010,000.00 USD | 66,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9750` | 601,530.00 USD | 32,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9850` | 451,370.00 USD | 31,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9950` | 109,310.00 USD | 30,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.00` | 472,770.00 USD | 30,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.01` | 155,310.00 USD | 30,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.02` | 136,000.00 USD | 30,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.03` | 2,110,000.00 USD | 30,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.04` | 88,220.00 USD | 28,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.05` | 1,120,000.00 USD | 27,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.06` | 390,040.00 USD | 26,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.07` | 455,900.00 USD | 26,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.08` | 744,660.00 USD | 25,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.09` | 124,020.00 USD | 25,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.10` | 107,230.00 USD | 25,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.11` | 874,470.00 USD | 24,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.12` | 260,740.00 USD | 24,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.14` | 86,630.00 USD | 23,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.15` | 366,370.00 USD | 23,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.16` | 221,570,000.00 USD | 221,570,000.00 USD | 100,770.00 USD | 64,860.00 USD | 127,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.16` | 108,390.00 USD | 23,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.16` | 221,270,000.00 USD | 221,270,000.00 USD | 173,190.00 USD | 99,350.00 USD | 396,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 220,600,000.00 USD | 220,600,000.00 USD | 171,750.00 USD | 52,740.00 USD | 204,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 220,180,000.00 USD | 220,180,000.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 219,150,000.00 USD | 219,150,000.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 80,480,000.00 USD | 80,480,000.00 USD | 172,040.00 USD | 61,210.00 USD | 202,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 217,780,000.00 USD | 217,780,000.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.17` | 1,680,000.00 USD | 23,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.17` | 80,040,000.00 USD | 80,040,000.00 USD | 152,440.00 USD | 38,870.00 USD | 60,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 217,150,000.00 USD | 217,150,000.00 USD | 406,410.00 USD | 132,100.00 USD | 785,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 79,790,000.00 USD | 79,790,000.00 USD | 86,630.00 USD | 31,280.00 USD | 43,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 215,830,000.00 USD | 215,830,000.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 79,630,000.00 USD | 79,630,000.00 USD | 27,580.00 USD | 49,790.00 USD | 94,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 214,320,000.00 USD | 214,320,000.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 79,460,000.00 USD | 79,460,000.00 USD | 32,280.00 USD | 26,620.00 USD | 195,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 212,930,000.00 USD | 212,930,000.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 79,200,000.00 USD | 79,200,000.00 USD | 141,540.00 USD | 16,760.00 USD | 182,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 212,130,000.00 USD | 212,130,000.00 USD | 290,470.00 USD | 107,150.00 USD | 505,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.18` | 806,220.00 USD | 21,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.18` | 78,860,000.00 USD | 78,860,000.00 USD | 80,830.00 USD | 13,900.00 USD | 30,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 211,230,000.00 USD | 211,230,000.00 USD | 154,760.00 USD | 93,720.00 USD | 245,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 78,730,000.00 USD | 78,730,000.00 USD | 77,850.00 USD | 41,360.00 USD | 49,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 210,740,000.00 USD | 210,740,000.00 USD | 299,590.00 USD | 131,210.00 USD | 459,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 78,570,000.00 USD | 78,570,000.00 USD | 19,950.00 USD | 11,210.00 USD | 2,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 209,840,000.00 USD | 209,840,000.00 USD | 69,670.00 USD | 152,290.00 USD | 286,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 78,530,000.00 USD | 78,530,000.00 USD | 37,820.00 USD | 22,830.00 USD | 66,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 209,340,000.00 USD | 209,340,000.00 USD | 67,200.00 USD | 53,830.00 USD | 12,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 78,410,000.00 USD | 78,410,000.00 USD | 56,380.00 USD | 20,760.00 USD | 28,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 209,200,000.00 USD | 209,200,000.00 USD | 81,610.00 USD | 98,170.00 USD | 428,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.19` | 1,650,000.00 USD | 20,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.19` | 78,300,000.00 USD | 78,300,000.00 USD | 50,010.00 USD | 37,580.00 USD | 102,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 208,600,000.00 USD | 208,600,000.00 USD | 190,550.00 USD | 38,510.00 USD | 383,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 78,110,000.00 USD | 78,110,000.00 USD | 60,820.00 USD | 4,280.00 USD | 13,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 207,980,000.00 USD | 207,980,000.00 USD | 186,430.00 USD | 128,180.00 USD | 350,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 78,030,000.00 USD | 78,030,000.00 USD | 36,460.00 USD | 10,480.00 USD | 75,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 207,320,000.00 USD | 207,320,000.00 USD | 130,690.00 USD | 67,850.00 USD | 262,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 77,910,000.00 USD | 77,910,000.00 USD | 67,440.00 USD | 29,830.00 USD | 130,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 206,860,000.00 USD | 206,860,000.00 USD | 218,910.00 USD | 107,850.00 USD | 335,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 77,680,000.00 USD | 77,680,000.00 USD | 106,940.00 USD | 33,950.00 USD | 32,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 206,190,000.00 USD | 206,190,000.00 USD | 338,060.00 USD | 79,070.00 USD | 291,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.20` | 477,200.00 USD | 19,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.20` | 77,510,000.00 USD | 77,510,000.00 USD | 134,160.00 USD | 6,620.00 USD | 61,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 205,490,000.00 USD | 205,490,000.00 USD | 5,350.00 USD | 93,870.00 USD | 187,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 77,310,000.00 USD | 77,310,000.00 USD | 41,430.00 USD | 21,290.00 USD | 1,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 205,200,000.00 USD | 205,200,000.00 USD | 67,200.00 USD | 57,670.00 USD | 21,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 77,240,000.00 USD | 77,240,000.00 USD | 23,000.00 USD | 6,640.00 USD | 1,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 205,050,000.00 USD | 205,050,000.00 USD | 34,730.00 USD | 26,000.00 USD | 15,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 77,210,000.00 USD | 77,210,000.00 USD | 43,340.00 USD | 13,890.00 USD | 61,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 204,980,000.00 USD | 204,980,000.00 USD | 202,570.00 USD | 53,170.00 USD | 48,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 204,670,000.00 USD | 204,670,000.00 USD | 0.00 USD | 14,550.00 USD | 79,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.21` | 656,350.00 USD | 18,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.21` | 77,090,000.00 USD | 77,090,000.00 USD | 2,880.00 USD | 5,600.00 USD | 814.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 204,580,000.00 USD | 204,580,000.00 USD | 80,450.00 USD | 5,390.00 USD | 9,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 77,080,000.00 USD | 77,080,000.00 USD | 0.00 USD | 0.00 USD | 32,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 204,480,000.00 USD | 204,480,000.00 USD | 361,660.00 USD | 45,260.00 USD | 357,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 203,720,000.00 USD | 203,720,000.00 USD | 70,670.00 USD | 152,900.00 USD | 457,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 203,040,000.00 USD | 203,040,000.00 USD | 278,240.00 USD | 50,420.00 USD | 33,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 202,670,000.00 USD | 202,670,000.00 USD | 5,680.00 USD | 39,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.22` | 355,520.00 USD | 18,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.22` | 202,630,000.00 USD | 202,630,000.00 USD | 97,920.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 202,530,000.00 USD | 202,530,000.00 USD | 0.00 USD | 765.15 USD | 40,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 202,490,000.00 USD | 202,490,000.00 USD | 54,470.00 USD | 2,490.00 USD | 14,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 202,420,000.00 USD | 202,420,000.00 USD | 10,460.00 USD | 191,360.00 USD | 207,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 202,010,000.00 USD | 202,010,000.00 USD | 649,620.00 USD | 191,250.00 USD | 200,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.23` | 1,680,000.00 USD | 17,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.23` | 200,970,000.00 USD | 200,970,000.00 USD | 341,300.00 USD | 128,580.00 USD | 60,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 200,440,000.00 USD | 200,440,000.00 USD | 44,790.00 USD | 125,700.00 USD | 371,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 199,900,000.00 USD | 199,900,000.00 USD | 257,070.00 USD | 187,490.00 USD | 353,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 77,050,000.00 USD | 77,050,000.00 USD | 0.00 USD | 396.00 USD | 903.28 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 199,100,000.00 USD | 199,100,000.00 USD | 702,400.00 USD | 142,840.00 USD | 467,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 77,050,000.00 USD | 77,050,000.00 USD | 73,550.00 USD | 22,720.00 USD | 4,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 197,780,000.00 USD | 197,780,000.00 USD | 1,150,000.00 USD | 525,690.00 USD | 2,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.24` | 401,010.00 USD | 15,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.24` | 76,950,000.00 USD | 76,950,000.00 USD | 747,060.00 USD | 300,230.00 USD | 424,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 193,980,000.00 USD | 193,980,000.00 USD | 1,620,000.00 USD | 912,620.00 USD | 1,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 75,480,000.00 USD | 75,480,000.00 USD | 1,290,000.00 USD | 617,140.00 USD | 896,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 189,590,000.00 USD | 189,590,000.00 USD | 1,890,000.00 USD | 930,140.00 USD | 2,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 72,670,000.00 USD | 72,670,000.00 USD | 503,480.00 USD | 255,200.00 USD | 574,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 184,510,000.00 USD | 184,510,000.00 USD | 1,980,000.00 USD | 633,060.00 USD | 2,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 71,340,000.00 USD | 71,340,000.00 USD | 179,040.00 USD | 232,710.00 USD | 299,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 179,330,000.00 USD | 179,330,000.00 USD | 982,310.00 USD | 740,000.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 70,630,000.00 USD | 70,630,000.00 USD | 390,870.00 USD | 84,110.00 USD | 195,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 176,530,000.00 USD | 176,530,000.00 USD | 2,040,000.00 USD | 376,950.00 USD | 1,810,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.25` | 13,870,000.00 USD | 15,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.25` | 69,960,000.00 USD | 69,960,000.00 USD | 357,170.00 USD | 90,850.00 USD | 261,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 172,300,000.00 USD | 172,300,000.00 USD | 2,120,000.00 USD | 1,190,000.00 USD | 5,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 69,250,000.00 USD | 69,250,000.00 USD | 207,040.00 USD | 196,500.00 USD | 303,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 163,690,000.00 USD | 163,690,000.00 USD | 2,280,000.00 USD | 1,370,000.00 USD | 3,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 68,540,000.00 USD | 68,540,000.00 USD | 117,990.00 USD | 79,810.00 USD | 571,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 156,560,000.00 USD | 156,560,000.00 USD | 2,810,000.00 USD | 918,840.00 USD | 2,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 67,770,000.00 USD | 67,770,000.00 USD | 374,100.00 USD | 17,220.00 USD | 531,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 150,830,000.00 USD | 150,830,000.00 USD | 1,240,000.00 USD | 673,830.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 66,850,000.00 USD | 66,850,000.00 USD | 213,710.00 USD | 42,480.00 USD | 82,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 147,430,000.00 USD | 147,430,000.00 USD | 625,270.00 USD | 563,370.00 USD | 776,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.25` | 641,680.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.26` | 66,510,000.00 USD | 66,510,000.00 USD | 259,250.00 USD | 149,990.00 USD | 197,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 145,470,000.00 USD | 145,470,000.00 USD | 370,280.00 USD | 446,010.00 USD | 344,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 65,910,000.00 USD | 65,910,000.00 USD | 196,210.00 USD | 1,980.00 USD | 171,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 144,310,000.00 USD | 144,310,000.00 USD | 1,190,000.00 USD | 449,360.00 USD | 890,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 65,540,000.00 USD | 65,540,000.00 USD | 501,390.00 USD | 220,330.00 USD | 390,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 141,780,000.00 USD | 141,780,000.00 USD | 1,470,000.00 USD | 1,130,000.00 USD | 852,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 64,420,000.00 USD | 64,420,000.00 USD | 1,380,000.00 USD | 528,250.00 USD | 768,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 138,330,000.00 USD | 138,330,000.00 USD | 2,860,000.00 USD | 1,720,000.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 61,750,000.00 USD | 61,750,000.00 USD | 2,680,000.00 USD | 1,360,000.00 USD | 2,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 131,710,000.00 USD | 131,710,000.00 USD | 3,640,000.00 USD | 1,750,000.00 USD | 4,470,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.26` | 464,620.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.27` | 55,670,000.00 USD | 55,670,000.00 USD | 1,190,000.00 USD | 559,560.00 USD | 1,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 121,870,000.00 USD | 121,870,000.00 USD | 3,940,000.00 USD | 1,540,000.00 USD | 6,430,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.27` | 52,570,000.00 USD | 52,570,000.00 USD | 479,480.00 USD | 466,310.00 USD | 667,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 109,960,000.00 USD | 109,960,000.00 USD | 1,990,000.00 USD | 1,500,000.00 USD | 2,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.27` | 50,960,000.00 USD | 50,960,000.00 USD | 919,330.00 USD | 234,050.00 USD | 623,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 104,090,000.00 USD | 104,090,000.00 USD | 3,830,000.00 USD | 1,680,000.00 USD | 4,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.27` | 49,180,000.00 USD | 49,180,000.00 USD | 1,250,000.00 USD | 345,070.00 USD | 893,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 94,500,000.00 USD | 94,500,000.00 USD | 4,300,000.00 USD | 3,000,000.00 USD | 9,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.27` | 46,690,000.00 USD | 46,690,000.00 USD | 2,160,000.00 USD | 857,380.00 USD | 1,680,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 77,940,000.00 USD | 77,940,000.00 USD | 3,980,000.00 USD | 1,300,000.00 USD | 7,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.27` | 479,930.00 USD | 598,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.28` | 42,000,000.00 USD | 42,000,000.00 USD | 4,520,000.00 USD | 2,770,000.00 USD | 4,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.28` | 65,420,000.00 USD | 65,420,000.00 USD | 6,760,000.00 USD | 2,990,000.00 USD | 8,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.28` | 30,620,000.00 USD | 30,620,000.00 USD | 4,350,000.00 USD | 1,700,000.00 USD | 3,860,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.28` | 47,320,000.00 USD | 47,320,000.00 USD | 4,830,000.00 USD | 1,750,000.00 USD | 6,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.28` | 20,720,000.00 USD | 20,720,000.00 USD | 1,640,000.00 USD | 789,830.00 USD | 1,510,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.28` | 34,520,000.00 USD | 34,520,000.00 USD | 4,610,000.00 USD | 1,440,000.00 USD | 3,850,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.28` | 16,780,000.00 USD | 16,780,000.00 USD | 1,610,000.00 USD | 799,310.00 USD | 1,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.28` | 24,630,000.00 USD | 24,630,000.00 USD | 2,970,000.00 USD | 2,130,000.00 USD | 2,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.28` | 12,470,000.00 USD | 12,470,000.00 USD | 2,070,000.00 USD | 488,880.00 USD | 749,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.28` | 17,040,000.00 USD | 17,040,000.00 USD | 3,830,000.00 USD | 1,550,000.00 USD | 4,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.28` | 118,740.00 USD | 118,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.29` | 9,150,000.00 USD | 9,150,000.00 USD | 365,870.00 USD | 103,610.00 USD | 898,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.29` | 7,540,000.00 USD | 7,540,000.00 USD | 724,970.00 USD | 0.00 USD | 3,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.29` | 7,790,000.00 USD | 7,790,000.00 USD | 460,040.00 USD | 83,240.00 USD | 745,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.29` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 665,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.29` | 6,500,000.00 USD | 6,500,000.00 USD | 1,180,000.00 USD | 196,280.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.29` | 3,120,000.00 USD | 3,120,000.00 USD | 1,040,000.00 USD | 0.00 USD | 819,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.29` | 3,430,000.00 USD | 3,430,000.00 USD | 503,180.00 USD | 167,570.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.29` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 213,200.00 USD | 301,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.29` | 1,530,000.00 USD | 1,530,000.00 USD | 975,270.00 USD | 184,260.00 USD | 371,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.29` | 747,810.00 USD | 747,810.00 USD | 440,550.00 USD | 0.00 USD | 307,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 581,550.00 USD | 581,550.00 USD | 167,950.00 USD | 413,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 389,370.00 USD | 389,370.00 USD | 0.00 USD | 389,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 778,740.00 USD | 778,740.00 USD | 0.00 USD | 389,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 668,470.00 USD | 668,470.00 USD | 0.00 USD | 86,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 749,800.00 USD | 749,800.00 USD | 0.00 USD | 81,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 286,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 1,920,000.00 USD | 1,920,000.00 USD | 327,930.00 USD | 841,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 2,340,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 1,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 5,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 5,180,000.00 USD | 5,180,000.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 194,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 5,240,000.00 USD | 5,240,000.00 USD | 62,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 3,370,000.00 USD | 3,370,000.00 USD | 323,900.00 USD | 743,970.00 USD | 181,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 7,610,000.00 USD | 7,610,000.00 USD | 703,820.00 USD | 318,670.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 5,840,000.00 USD | 5,840,000.00 USD | 1,280,000.00 USD | 511,150.00 USD | 682,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 9,970,000.00 USD | 9,970,000.00 USD | 557,940.00 USD | 430,030.00 USD | 1,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 8,940,000.00 USD | 8,940,000.00 USD | 267,480.00 USD | 537,730.00 USD | 2,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 12,390,000.00 USD | 12,390,000.00 USD | 57,160.00 USD | 1,070,000.00 USD | 1,280,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.31` | 4,840.00 USD | 4,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.32` | 15,270,000.00 USD | 15,270,000.00 USD | 1,160,000.00 USD | 1,690,000.00 USD | 3,480,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 16,930,000.00 USD | 16,930,000.00 USD | 1,120,000.00 USD | 1,120,000.00 USD | 2,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 20,660,000.00 USD | 20,660,000.00 USD | 2,060,000.00 USD | 820,760.00 USD | 2,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 19,860,000.00 USD | 19,860,000.00 USD | 755,330.00 USD | 406,240.00 USD | 1,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 23,790,000.00 USD | 23,790,000.00 USD | 1,450,000.00 USD | 704,780.00 USD | 970,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 21,400,000.00 USD | 21,400,000.00 USD | 966,720.00 USD | 235,180.00 USD | 336,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 27,750,000.00 USD | 27,750,000.00 USD | 1,660,000.00 USD | 720,740.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 25,190,000.00 USD | 25,190,000.00 USD | 1,740,000.00 USD | 761,100.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 29,690,000.00 USD | 29,690,000.00 USD | 1,030,000.00 USD | 287,550.00 USD | 625,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 27,560,000.00 USD | 27,560,000.00 USD | 1,620,000.00 USD | 198,920.00 USD | 553,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.32` | 22,430.00 USD | 27,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.33` | 32,180,000.00 USD | 32,180,000.00 USD | 624,130.00 USD | 621,340.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 28,100,000.00 USD | 28,100,000.00 USD | 462,320.00 USD | 5,470.00 USD | 69,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 34,420,000.00 USD | 34,420,000.00 USD | 683,490.00 USD | 159,620.00 USD | 1,400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 29,250,000.00 USD | 29,250,000.00 USD | 53,290.00 USD | 10,370.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 37,010,000.00 USD | 37,010,000.00 USD | 748,200.00 USD | 298,240.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 30,970,000.00 USD | 30,970,000.00 USD | 581,420.00 USD | 268,860.00 USD | 869,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 38,250,000.00 USD | 38,250,000.00 USD | 713,230.00 USD | 84,950.00 USD | 440,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 32,920,000.00 USD | 32,920,000.00 USD | 830,370.00 USD | 108,920.00 USD | 1,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 39,930,000.00 USD | 39,930,000.00 USD | 717,360.00 USD | 300,370.00 USD | 665,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 33,410,000.00 USD | 33,410,000.00 USD | 109,550.00 USD | 194,680.00 USD | 189,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.33` | 57,610.00 USD | 84,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.34` | 41,960,000.00 USD | 41,960,000.00 USD | 834,660.00 USD | 219,020.00 USD | 976,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 35,050,000.00 USD | 35,050,000.00 USD | 679,750.00 USD | 645,230.00 USD | 312,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 45,730,000.00 USD | 45,730,000.00 USD | 1,540,000.00 USD | 373,490.00 USD | 1,860,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 37,150,000.00 USD | 37,150,000.00 USD | 1,240,000.00 USD | 362,920.00 USD | 494,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 49,190,000.00 USD | 49,190,000.00 USD | 1,720,000.00 USD | 804,730.00 USD | 929,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 41,880,000.00 USD | 41,880,000.00 USD | 2,650,000.00 USD | 1,630,000.00 USD | 440,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 53,860,000.00 USD | 53,860,000.00 USD | 2,500,000.00 USD | 765,730.00 USD | 1,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 47,580,000.00 USD | 47,580,000.00 USD | 1,730,000.00 USD | 2,830,000.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 57,290,000.00 USD | 57,290,000.00 USD | 1,350,000.00 USD | 692,900.00 USD | 1,380,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 58,760,000.00 USD | 58,760,000.00 USD | 3,700,000.00 USD | 1,880,000.00 USD | 5,610,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.34` | 163,410.00 USD | 248,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.35` | 58,850,000.00 USD | 58,850,000.00 USD | 753,910.00 USD | 309,200.00 USD | 502,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 66,500,000.00 USD | 66,500,000.00 USD | 2,550,000.00 USD | 2,230,000.00 USD | 2,960,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 61,740,000.00 USD | 61,740,000.00 USD | 1,170,000.00 USD | 384,860.00 USD | 1,330,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 76,870,000.00 USD | 76,870,000.00 USD | 4,290,000.00 USD | 1,760,000.00 USD | 4,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 62,810,000.00 USD | 62,810,000.00 USD | 489,370.00 USD | 130,090.00 USD | 452,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 84,650,000.00 USD | 84,650,000.00 USD | 2,580,000.00 USD | 1,440,000.00 USD | 3,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 65,140,000.00 USD | 65,140,000.00 USD | 879,540.00 USD | 405,430.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 92,970,000.00 USD | 92,970,000.00 USD | 2,620,000.00 USD | 1,230,000.00 USD | 4,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 67,520,000.00 USD | 67,520,000.00 USD | 857,510.00 USD | 297,760.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 101,200,000.00 USD | 101,200,000.00 USD | 3,780,000.00 USD | 873,380.00 USD | 3,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.35` | 3,990.00 USD | 252,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.36` | 69,640,000.00 USD | 69,640,000.00 USD | 1,120,000.00 USD | 102,980.00 USD | 901,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 105,280,000.00 USD | 105,280,000.00 USD | 1,320,000.00 USD | 881,730.00 USD | 1,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 70,460,000.00 USD | 70,460,000.00 USD | 504,090.00 USD | 150,540.00 USD | 163,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 109,180,000.00 USD | 109,180,000.00 USD | 1,490,000.00 USD | 729,940.00 USD | 1,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 71,250,000.00 USD | 71,250,000.00 USD | 374,230.00 USD | 183,190.00 USD | 237,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 111,690,000.00 USD | 111,690,000.00 USD | 671,910.00 USD | 581,640.00 USD | 1,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 72,360,000.00 USD | 72,360,000.00 USD | 454,700.00 USD | 103,540.00 USD | 547,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 116,080,000.00 USD | 116,080,000.00 USD | 2,100,000.00 USD | 918,100.00 USD | 1,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 72,450,000.00 USD | 72,450,000.00 USD | 16,020.00 USD | 28,030.00 USD | 46,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 117,990,000.00 USD | 117,990,000.00 USD | 664,020.00 USD | 328,930.00 USD | 923,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.36` | 201,820.00 USD | 454,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.37` | 72,830,000.00 USD | 72,830,000.00 USD | 126,080.00 USD | 85,100.00 USD | 170,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 118,490,000.00 USD | 118,490,000.00 USD | 239,150.00 USD | 216,290.00 USD | 40,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 73,270,000.00 USD | 73,270,000.00 USD | 172,840.00 USD | 18,750.00 USD | 251,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 120,280,000.00 USD | 120,280,000.00 USD | 547,200.00 USD | 138,950.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 73,750,000.00 USD | 73,750,000.00 USD | 100,350.00 USD | 120,860.00 USD | 258,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 121,680,000.00 USD | 121,680,000.00 USD | 465,040.00 USD | 398,870.00 USD | 543,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 74,180,000.00 USD | 74,180,000.00 USD | 186,780.00 USD | 49,160.00 USD | 193,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 124,540,000.00 USD | 124,540,000.00 USD | 931,390.00 USD | 404,120.00 USD | 1,520,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 74,370,000.00 USD | 74,370,000.00 USD | 121,400.00 USD | 884.30 USD | 69,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 126,230,000.00 USD | 126,230,000.00 USD | 594,550.00 USD | 326,340.00 USD | 769,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 74,810,000.00 USD | 74,810,000.00 USD | 137,580.00 USD | 65,830.00 USD | 232,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 127,850,000.00 USD | 127,850,000.00 USD | 676,760.00 USD | 389,310.00 USD | 552,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 75,590,000.00 USD | 75,590,000.00 USD | 336,250.00 USD | 76,440.00 USD | 369,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 129,790,000.00 USD | 129,790,000.00 USD | 579,450.00 USD | 290,350.00 USD | 1,070,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 76,200,000.00 USD | 76,200,000.00 USD | 331,700.00 USD | 108,980.00 USD | 163,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 132,330,000.00 USD | 132,330,000.00 USD | 1,210,000.00 USD | 330,740.00 USD | 1,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 76,800,000.00 USD | 76,800,000.00 USD | 371,970.00 USD | 42,880.00 USD | 185,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 133,420,000.00 USD | 133,420,000.00 USD | 297,210.00 USD | 312,330.00 USD | 477,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 77,040,000.00 USD | 77,040,000.00 USD | 145,190.00 USD | 54,030.00 USD | 40,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 134,520,000.00 USD | 134,520,000.00 USD | 505,510.00 USD | 190,450.00 USD | 401,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.39` | 31,530.00 USD | 485,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.39` | 77,130,000.00 USD | 77,130,000.00 USD | 57,490.00 USD | 16,600.00 USD | 19,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 135,010,000.00 USD | 135,010,000.00 USD | 86,820.00 USD | 203,870.00 USD | 200,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 77,510,000.00 USD | 77,510,000.00 USD | 140,810.00 USD | 51,770.00 USD | 189,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 136,100,000.00 USD | 136,100,000.00 USD | 690,420.00 USD | 162,590.00 USD | 238,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 136,260,000.00 USD | 136,260,000.00 USD | 118,760.00 USD | 39,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 136,580,000.00 USD | 136,580,000.00 USD | 82,350.00 USD | 36,390.00 USD | 208,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.40` | 77,530,000.00 USD | 77,530,000.00 USD | 7,190.00 USD | 14,010.00 USD | 2,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 136,730,000.00 USD | 136,730,000.00 USD | 121,260.00 USD | 22,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.40` | 11,740.00 USD | 497,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.40` | 77,630,000.00 USD | 77,630,000.00 USD | 19,030.00 USD | 0.00 USD | 80,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 136,740,000.00 USD | 136,740,000.00 USD | 0.00 USD | 0.00 USD | 16,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 136,750,000.00 USD | 136,750,000.00 USD | 0.00 USD | 996.88 USD | 5,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 136,890,000.00 USD | 136,890,000.00 USD | 0.00 USD | 75,720.00 USD | 60,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 137,010,000.00 USD | 137,010,000.00 USD | 94,530.00 USD | 21,520.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 137,250,000.00 USD | 137,250,000.00 USD | 178,210.00 USD | 25,430.00 USD | 38,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.41` | 952.59 USD | 498,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.41` | 137,410,000.00 USD | 137,410,000.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 137,580,000.00 USD | 137,580,000.00 USD | 12,250.00 USD | 37,300.00 USD | 120,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 137,740,000.00 USD | 137,740,000.00 USD | 88,530.00 USD | 57,460.00 USD | 7,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.41` | 77,630,000.00 USD | 77,630,000.00 USD | 0.00 USD | 158.40 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 137,910,000.00 USD | 137,910,000.00 USD | 11,290.00 USD | 26,480.00 USD | 132,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 77,670,000.00 USD | 77,670,000.00 USD | 29,120.00 USD | 9,090.00 USD | 1,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 138,410,000.00 USD | 138,410,000.00 USD | 161,890.00 USD | 72,870.00 USD | 264,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.42` | 3,860.00 USD | 502,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.42` | 77,890,000.00 USD | 77,890,000.00 USD | 115,890.00 USD | 26,520.00 USD | 70,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 138,830,000.00 USD | 138,830,000.00 USD | 171,750.00 USD | 52,740.00 USD | 204,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 78,480,000.00 USD | 78,480,000.00 USD | 269,920.00 USD | 170,450.00 USD | 151,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 139,860,000.00 USD | 139,860,000.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 79,070,000.00 USD | 79,070,000.00 USD | 292,830.00 USD | 105,740.00 USD | 193,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 141,230,000.00 USD | 141,230,000.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 79,290,000.00 USD | 79,290,000.00 USD | 63,800.00 USD | 59,830.00 USD | 91,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 141,860,000.00 USD | 141,860,000.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.43` | 79,380,000.00 USD | 79,380,000.00 USD | 31,260.00 USD | 27,740.00 USD | 34,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 142,210,000.00 USD | 142,210,000.00 USD | 87,470.00 USD | 69,800.00 USD | 196,840.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.43` | 95,360.00 USD | 597,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.43` | 79,540,000.00 USD | 79,540,000.00 USD | 121,180.00 USD | 11,130.00 USD | 25,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 143,180,000.00 USD | 143,180,000.00 USD | 318,950.00 USD | 62,300.00 USD | 588,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.43` | 79,700,000.00 USD | 79,700,000.00 USD | 86,630.00 USD | 31,280.00 USD | 43,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 144,690,000.00 USD | 144,690,000.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.43` | 79,870,000.00 USD | 79,870,000.00 USD | 27,580.00 USD | 49,790.00 USD | 94,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 146,080,000.00 USD | 146,080,000.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.43` | 80,130,000.00 USD | 80,130,000.00 USD | 32,280.00 USD | 26,620.00 USD | 195,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 146,880,000.00 USD | 146,880,000.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.44` | 80,300,000.00 USD | 80,300,000.00 USD | 102,020.00 USD | 0.00 USD | 76,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 147,410,000.00 USD | 147,410,000.00 USD | 215,800.00 USD | 23,880.00 USD | 290,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.44` | 181,920.00 USD | 779,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.44` | 80,470,000.00 USD | 80,470,000.00 USD | 39,530.00 USD | 16,760.00 USD | 106,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 147,780,000.00 USD | 147,780,000.00 USD | 74,670.00 USD | 83,260.00 USD | 215,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.44` | 80,590,000.00 USD | 80,590,000.00 USD | 80,830.00 USD | 13,900.00 USD | 30,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 148,280,000.00 USD | 148,280,000.00 USD | 154,760.00 USD | 93,720.00 USD | 245,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.44` | 80,760,000.00 USD | 80,760,000.00 USD | 77,850.00 USD | 41,360.00 USD | 49,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 149,170,000.00 USD | 149,170,000.00 USD | 299,590.00 USD | 131,210.00 USD | 459,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.44` | 80,790,000.00 USD | 80,790,000.00 USD | 19,950.00 USD | 11,210.00 USD | 2,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 149,670,000.00 USD | 149,670,000.00 USD | 69,670.00 USD | 152,290.00 USD | 286,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.45` | 80,920,000.00 USD | 80,920,000.00 USD | 37,820.00 USD | 22,830.00 USD | 66,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 149,810,000.00 USD | 149,810,000.00 USD | 67,200.00 USD | 53,830.00 USD | 12,180.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.45` | 11,390.00 USD | 790,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.45` | 80,960,000.00 USD | 80,960,000.00 USD | 35,430.00 USD | 247.55 USD | 1,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 149,940,000.00 USD | 149,940,000.00 USD | 11,070.00 USD | 2,120.00 USD | 116,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.45` | 81,030,000.00 USD | 81,030,000.00 USD | 20,940.00 USD | 20,510.00 USD | 26,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 150,420,000.00 USD | 150,420,000.00 USD | 70,540.00 USD | 96,050.00 USD | 311,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.45` | 81,210,000.00 USD | 81,210,000.00 USD | 42,480.00 USD | 37,580.00 USD | 102,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 151,010,000.00 USD | 151,010,000.00 USD | 190,550.00 USD | 38,510.00 USD | 370,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.45` | 81,250,000.00 USD | 81,250,000.00 USD | 28,580.00 USD | 4,170.00 USD | 12,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 151,640,000.00 USD | 151,640,000.00 USD | 161,500.00 USD | 127,370.00 USD | 338,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.46` | 5,760.00 USD | 796,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.47` | 28,340.00 USD | 824,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.48` | 11,820.00 USD | 836,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.49` | 227.20 USD | 837,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.50` | 12,680.00 USD | 849,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.50` | 47,570.00 USD | 897,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.51` | 1,940.00 USD | 899,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.53` | 1,130.00 USD | 900,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 6,320.00 USD | 906,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.55` | 1,360.00 USD | 908,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 555.57 USD | 908,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.57` | 2,840.00 USD | 911,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.58` | 7,570.00 USD | 918,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.59` | 321,070.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.60` | 5,220,000.00 USD | 6,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.61` | 4,890,000.00 USD | 11,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.62` | 6,420.00 USD | 11,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.64` | 11,270.00 USD | 11,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 133,590.00 USD | 11,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 911.91 USD | 11,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 586.08 USD | 11,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.68` | 760.45 USD | 11,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.69` | 47,320.00 USD | 11,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.70` | 1,040.00 USD | 11,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.71` | 1,980.00 USD | 11,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.72` | 10,410.00 USD | 11,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.73` | 1,920.00 USD | 11,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 2,970.00 USD | 11,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 3,260.00 USD | 11,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 4,000.00 USD | 11,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.76` | 2,540.00 USD | 11,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.77` | 2,040.00 USD | 11,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.78` | 129,540.00 USD | 11,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.79` | 3,210.00 USD | 11,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.80` | 889.87 USD | 11,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.81` | 2,800,000.00 USD | 14,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.82` | 297.48 USD | 14,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.83` | 889.98 USD | 14,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.84` | 5,540.00 USD | 14,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.85` | 632.55 USD | 14,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.86` | 2,040.00 USD | 14,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.88` | 246,040.00 USD | 14,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.89` | 339.30 USD | 14,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.90` | 4,190.00 USD | 14,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.91` | 69,460.00 USD | 14,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.93` | 103.95 USD | 14,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.94` | 8,870.00 USD | 14,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.95` | 287.86 USD | 14,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.96` | 293.25 USD | 14,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.97` | 333,390.00 USD | 15,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.98` | 651.75 USD | 15,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.00` | 1,120.00 USD | 15,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.00` | 393,140.00 USD | 15,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.02` | 513.83 USD | 15,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.04` | 279,600.00 USD | 15,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.06` | 5,330.00 USD | 15,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.10` | 2,540.00 USD | 15,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.10` | 1,960.00 USD | 15,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.12` | 3,100.00 USD | 15,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.15` | 196.11 USD | 15,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.17` | 2,830.00 USD | 15,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.19` | 100.51 USD | 15,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.19` | 72,080.00 USD | 15,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.23` | 3,890.00 USD | 15,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.25` | 2,350,000.00 USD | 18,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.27` | 3,460,000.00 USD | 21,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.27` | 14,930.00 USD | 21,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.29` | 1,060,000.00 USD | 22,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.31` | 92,880.00 USD | 22,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.33` | 3,280.00 USD | 22,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.33` | 175,880.00 USD | 23,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.35` | 108.33 USD | 23,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.37` | 146.63 USD | 23,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.38` | 91,880.00 USD | 23,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.38` | 74,260.00 USD | 23,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.40` | 167.65 USD | 23,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.40` | 1,210.00 USD | 23,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.42` | 2,420.00 USD | 23,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.46` | 24,840.00 USD | 23,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.48` | 256,540.00 USD | 23,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.50` | 114.77 USD | 23,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.52` | 5,640.00 USD | 23,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.52` | 42,710.00 USD | 23,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.54` | 613.47 USD | 23,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.56` | 3,870,000.00 USD | 27,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.56` | 346.27 USD | 27,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.58` | 2,250.00 USD | 27,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.58` | 23,350.00 USD | 27,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.2650` | 74,630,000.00 USD | 0.00 USD | 4,330.00 USD | `-79.60%` | `16,327.00` |
| `Live` | `Long` | `0.2750` | 74,630,000.00 USD | 0.00 USD | 379.50 USD | `-78.83%` | `1,380.00` |
| `Live` | `Long` | `0.2850` | 74,620,000.00 USD | 0.00 USD | 1,500.00 USD | `-78.06%` | `5,267.00` |
| `Live` | `Long` | `0.2950` | 74,620,000.00 USD | 0.00 USD | 1,060.00 USD | `-77.29%` | `3,596.00` |
| `Live` | `Long` | `0.3150` | 74,620,000.00 USD | 0.00 USD | 5,060.00 USD | `-75.75%` | `16,065.00` |
| `Live` | `Long` | `0.3450` | 74,620,000.00 USD | 0.00 USD | 1,010.00 USD | `-73.45%` | `2,922.00` |
| `Live` | `Long` | `0.3550` | 74,620,000.00 USD | 0.00 USD | 1,140.00 USD | `-72.68%` | `3,215.00` |
| `Live` | `Long` | `0.3650` | 74,620,000.00 USD | 0.00 USD | 1,900.00 USD | `-71.91%` | `5,205.00` |
| `Live` | `Long` | `0.3750` | 74,610,000.00 USD | 0.00 USD | 9,820.00 USD | `-71.14%` | `26,194.00` |
| `Live` | `Long` | `0.3850` | 74,600,000.00 USD | 0.00 USD | 1,250.00 USD | `-70.37%` | `3,252.00` |
| `Live` | `Long` | `0.3950` | 74,600,000.00 USD | 0.00 USD | 1,320.00 USD | `-69.60%` | `3,342.00` |
| `Live` | `Long` | `0.4050` | 74,600,000.00 USD | 0.00 USD | 2,620.00 USD | `-68.83%` | `6,463.00` |
| `Live` | `Long` | `0.4150` | 74,600,000.00 USD | 0.00 USD | 151,310.00 USD | `-68.06%` | `364,614.00` |
| `Live` | `Long` | `0.4250` | 74,450,000.00 USD | 0.00 USD | 15,910.00 USD | `-67.29%` | `37,429.00` |
| `Live` | `Long` | `0.4350` | 74,430,000.00 USD | 0.00 USD | 376.27 USD | `-66.52%` | `865.00` |
| `Live` | `Long` | `0.4550` | 74,430,000.00 USD | 0.00 USD | 2,680.00 USD | `-64.98%` | `5,884.00` |
| `Live` | `Long` | `0.4650` | 74,430,000.00 USD | 0.00 USD | 989.06 USD | `-64.21%` | `2,127.00` |
| `Live` | `Long` | `0.4750` | 74,430,000.00 USD | 0.00 USD | 3,100.00 USD | `-63.44%` | `6,526.00` |
| `Live` | `Long` | `0.4850` | 74,420,000.00 USD | 0.00 USD | 30,430.00 USD | `-62.67%` | `62,742.00` |
| `Live` | `Long` | `0.4950` | 74,390,000.00 USD | 0.00 USD | 3,140.00 USD | `-61.90%` | `6,342.00` |
| `Live` | `Long` | `0.5050` | 74,390,000.00 USD | 0.00 USD | 6,750.00 USD | `-61.13%` | `13,373.00` |
| `Live` | `Long` | `0.5150` | 74,380,000.00 USD | 0.00 USD | 2,030.00 USD | `-60.36%` | `3,945.00` |
| `Live` | `Long` | `0.5250` | 74,380,000.00 USD | 0.00 USD | 50,280.00 USD | `-59.59%` | `95,774.00` |
| `Live` | `Long` | `0.5350` | 74,330,000.00 USD | 0.00 USD | 10,910.00 USD | `-58.82%` | `20,395.00` |
| `Live` | `Long` | `0.5550` | 74,320,000.00 USD | 0.00 USD | 2,730.00 USD | `-57.28%` | `4,927.00` |
| `Live` | `Long` | `0.5650` | 74,320,000.00 USD | 0.00 USD | 374.03 USD | `-56.51%` | `662.00` |
| `Live` | `Long` | `0.5750` | 74,320,000.00 USD | 0.00 USD | 6,200.00 USD | `-55.74%` | `10,784.00` |
| `Live` | `Long` | `0.5850` | 74,310,000.00 USD | 0.00 USD | 889.20 USD | `-54.97%` | `1,520.00` |
| `Live` | `Long` | `0.5950` | 74,310,000.00 USD | 0.00 USD | 5,760.00 USD | `-54.20%` | `9,684.00` |
| `Live` | `Long` | `0.6050` | 74,300,000.00 USD | 0.00 USD | 32,400.00 USD | `-53.43%` | `53,561.00` |
| `Live` | `Long` | `0.6150` | 74,270,000.00 USD | 0.00 USD | 50,190.00 USD | `-52.66%` | `81,617.00` |
| `Live` | `Long` | `0.6250` | 74,220,000.00 USD | 0.00 USD | 7,150.00 USD | `-51.89%` | `11,446.00` |
| `Live` | `Long` | `0.6450` | 74,210,000.00 USD | 0.00 USD | 8,030.00 USD | `-50.35%` | `12,457.00` |
| `Live` | `Long` | `0.6550` | 74,210,000.00 USD | 0.00 USD | 140,570.00 USD | `-49.58%` | `214,605.00` |
| `Live` | `Long` | `0.6650` | 74,070,000.00 USD | 0.00 USD | 31,770.00 USD | `-48.81%` | `47,779.00` |
| `Live` | `Long` | `0.6750` | 74,030,000.00 USD | 0.00 USD | 28,620.00 USD | `-48.04%` | `42,397.00` |
| `Live` | `Long` | `0.6850` | 74,010,000.00 USD | 0.00 USD | 2,450,000.00 USD | `-47.28%` | `3,574,974.00` |
| `Live` | `Long` | `0.6950` | 71,560,000.00 USD | 0.00 USD | 11,360.00 USD | `-46.51%` | `16,348.00` |
| `Live` | `Long` | `0.7050` | 71,550,000.00 USD | 0.00 USD | 25,010.00 USD | `-45.74%` | `35,475.00` |
| `Live` | `Long` | `0.7150` | 71,520,000.00 USD | 0.00 USD | 67,440.00 USD | `-44.97%` | `94,326.00` |
| `Live` | `Long` | `0.7250` | 71,450,000.00 USD | 0.00 USD | 217,680.00 USD | `-44.20%` | `300,251.00` |
| `Live` | `Long` | `0.7350` | 71,240,000.00 USD | 0.00 USD | 23,650.00 USD | `-43.43%` | `32,174.00` |
| `Live` | `Long` | `0.7450` | 71,210,000.00 USD | 0.00 USD | 52,420.00 USD | `-42.66%` | `70,363.00` |
| `Live` | `Long` | `0.7550` | 71,160,000.00 USD | 0.00 USD | 563,960.00 USD | `-41.89%` | `746,966.00` |
| `Live` | `Long` | `0.7650` | 70,600,000.00 USD | 0.00 USD | 2,190.00 USD | `-41.12%` | `2,860.00` |
| `Live` | `Long` | `0.7750` | 70,590,000.00 USD | 0.00 USD | 29,790.00 USD | `-40.35%` | `38,433.00` |
| `Live` | `Long` | `0.7850` | 70,560,000.00 USD | 0.00 USD | 40,330.00 USD | `-39.58%` | `51,375.00` |
| `Live` | `Long` | `0.7950` | 70,520,000.00 USD | 0.00 USD | 11,580.00 USD | `-38.81%` | `14,569.00` |
| `Live` | `Long` | `0.8050` | 70,510,000.00 USD | 0.00 USD | 22,350.00 USD | `-38.04%` | `27,761.00` |
| `Live` | `Long` | `0.8150` | 70,490,000.00 USD | 0.00 USD | 22,650.00 USD | `-37.27%` | `27,793.00` |
| `Live` | `Long` | `0.8250` | 70,470,000.00 USD | 0.00 USD | 11,200.00 USD | `-36.50%` | `13,578.00` |
| `Live` | `Long` | `0.8350` | 70,460,000.00 USD | 0.00 USD | 44,490.00 USD | `-35.73%` | `53,278.00` |
| `Live` | `Long` | `0.8450` | 70,410,000.00 USD | 0.00 USD | 70,540.00 USD | `-34.96%` | `83,477.00` |
| `Live` | `Long` | `0.8550` | 70,340,000.00 USD | 0.00 USD | 165,960.00 USD | `-34.19%` | `194,107.00` |
| `Live` | `Long` | `0.8650` | 70,170,000.00 USD | 0.00 USD | 28,530.00 USD | `-33.42%` | `32,977.00` |
| `Live` | `Long` | `0.8750` | 70,150,000.00 USD | 0.00 USD | 128,340.00 USD | `-32.65%` | `146,671.00` |
| `Live` | `Long` | `0.8850` | 70,020,000.00 USD | 0.00 USD | 357,260.00 USD | `-31.88%` | `403,678.00` |
| `Live` | `Long` | `0.8950` | 69,660,000.00 USD | 0.00 USD | 2,390,000.00 USD | `-31.11%` | `2,667,409.00` |
| `Live` | `Long` | `0.9050` | 67,270,000.00 USD | 0.00 USD | 151,820.00 USD | `-30.34%` | `167,753.00` |
| `Live` | `Long` | `0.9150` | 67,120,000.00 USD | 0.00 USD | 26,030.00 USD | `-29.57%` | `28,446.00` |
| `Live` | `Long` | `0.9250` | 67,090,000.00 USD | 0.00 USD | 647,340.00 USD | `-28.80%` | `699,828.00` |
| `Live` | `Long` | `0.9350` | 66,450,000.00 USD | 0.00 USD | 86,480.00 USD | `-28.03%` | `92,488.00` |
| `Live` | `Long` | `0.9450` | 66,360,000.00 USD | 0.00 USD | 79,680.00 USD | `-27.26%` | `84,321.00` |
| `Live` | `Long` | `0.9550` | 66,280,000.00 USD | 0.00 USD | 238,350.00 USD | `-26.49%` | `249,585.00` |
| `Live` | `Long` | `0.9650` | 66,040,000.00 USD | 0.00 USD | 34,010,000.00 USD | `-25.72%` | `35,243,710.00` |
| `Live` | `Long` | `0.9750` | 32,030,000.00 USD | 0.00 USD | 601,530.00 USD | `-24.95%` | `616,951.00` |
| `Live` | `Long` | `0.9850` | 31,430,000.00 USD | 0.00 USD | 451,370.00 USD | `-24.18%` | `458,242.00` |
| `Live` | `Long` | `0.9950` | 30,980,000.00 USD | 0.00 USD | 109,310.00 USD | `-23.41%` | `109,856.00` |
| `Live` | `Long` | `1.00` | 30,870,000.00 USD | 0.00 USD | 472,770.00 USD | `-22.64%` | `470,421.00` |
| `Live` | `Long` | `1.01` | 30,400,000.00 USD | 0.00 USD | 155,310.00 USD | `-21.87%` | `153,014.00` |
| `Live` | `Long` | `1.02` | 30,240,000.00 USD | 0.00 USD | 136,000.00 USD | `-21.11%` | `132,685.00` |
| `Live` | `Long` | `1.03` | 30,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | `-20.34%` | `2,038,781.00` |
| `Live` | `Long` | `1.04` | 28,000,000.00 USD | 0.00 USD | 88,220.00 USD | `-19.57%` | `84,423.00` |
| `Live` | `Long` | `1.05` | 27,910,000.00 USD | 0.00 USD | 1,120,000.00 USD | `-18.80%` | `1,059,173.00` |
| `Live` | `Long` | `1.06` | 26,790,000.00 USD | 0.00 USD | 390,040.00 USD | `-18.03%` | `366,231.00` |
| `Live` | `Long` | `1.07` | 26,400,000.00 USD | 0.00 USD | 455,900.00 USD | `-17.26%` | `424,092.00` |
| `Live` | `Long` | `1.08` | 25,940,000.00 USD | 0.00 USD | 744,660.00 USD | `-16.49%` | `686,318.00` |
| `Live` | `Long` | `1.09` | 25,200,000.00 USD | 0.00 USD | 124,020.00 USD | `-15.72%` | `113,256.00` |
| `Live` | `Long` | `1.10` | 25,080,000.00 USD | 0.00 USD | 107,230.00 USD | `-14.95%` | `97,040.00` |
| `Live` | `Long` | `1.11` | 24,970,000.00 USD | 0.00 USD | 874,470.00 USD | `-14.18%` | `784,280.00` |
| `Live` | `Long` | `1.12` | 24,090,000.00 USD | 0.00 USD | 260,740.00 USD | `-13.41%` | `231,773.00` |
| `Live` | `Long` | `1.14` | 23,830,000.00 USD | 0.00 USD | 86,630.00 USD | `-12.64%` | `76,330.00` |
| `Live` | `Long` | `1.15` | 23,750,000.00 USD | 0.00 USD | 366,370.00 USD | `-11.87%` | `319,977.00` |
| `Live` | `Long` | `1.16` | 23,380,000.00 USD | 0.00 USD | 108,390.00 USD | `-11.10%` | `93,846.00` |
| `Live` | `Long` | `1.17` | 23,270,000.00 USD | 0.00 USD | 1,680,000.00 USD | `-10.33%` | `1,438,783.00` |
| `Live` | `Long` | `1.18` | 21,600,000.00 USD | 0.00 USD | 806,220.00 USD | `-9.56%` | `686,142.00` |
| `Live` | `Long` | `1.19` | 20,790,000.00 USD | 0.00 USD | 1,650,000.00 USD | `-8.79%` | `1,388,418.00` |
| `Live` | `Long` | `1.20` | 19,140,000.00 USD | 0.00 USD | 477,200.00 USD | `-8.02%` | `399,331.00` |
| `Live` | `Long` | `1.21` | 18,670,000.00 USD | 0.00 USD | 656,350.00 USD | `-7.25%` | `544,691.00` |
| `Live` | `Long` | `1.22` | 18,010,000.00 USD | 0.00 USD | 355,520.00 USD | `-6.48%` | `292,612.00` |
| `Live` | `Long` | `1.23` | 17,660,000.00 USD | 0.00 USD | 1,680,000.00 USD | `-5.71%` | `1,367,921.00` |
| `Live` | `Long` | `1.24` | 15,980,000.00 USD | 0.00 USD | 401,010.00 USD | `-4.94%` | `324,705.00` |
| `Live` | `Long` | `1.25` | 15,580,000.00 USD | 0.00 USD | 13,870,000.00 USD | `-4.17%` | `11,143,653.00` |
| `Live` | `Long` | `1.25` | 1,700,000.00 USD | 0.00 USD | 641,680.00 USD | `-3.40%` | `511,296.00` |
| `Live` | `Long` | `1.26` | 1,060,000.00 USD | 0.00 USD | 464,620.00 USD | `-2.63%` | `367,291.00` |
| `Live` | `Long` | `1.27` | 598,670.00 USD | 0.00 USD | 479,930.00 USD | `-1.86%` | `376,418.00` |
| `Live` | `Long` | `1.28` | 118,740.00 USD | 0.00 USD | 118,740.00 USD | `-1.09%` | `92,404.00` |
| `Live` | `Short` | `1.31` | 4,840.00 USD | 4,840.00 USD | 0.00 USD | `+1.22%` | `3,680.00` |
| `Live` | `Short` | `1.32` | 27,260.00 USD | 22,430.00 USD | 0.00 USD | `+1.99%` | `16,925.00` |
| `Live` | `Short` | `1.33` | 84,880.00 USD | 57,610.00 USD | 0.00 USD | `+2.76%` | `43,154.00` |
| `Live` | `Short` | `1.34` | 248,280.00 USD | 163,410.00 USD | 0.00 USD | `+3.53%` | `121,492.00` |
| `Live` | `Short` | `1.35` | 252,280.00 USD | 3,990.00 USD | 0.00 USD | `+4.29%` | `2,947.00` |
| `Live` | `Short` | `1.36` | 454,100.00 USD | 201,820.00 USD | 0.00 USD | `+5.06%` | `147,857.00` |
| `Live` | `Short` | `1.39` | 485,630.00 USD | 31,530.00 USD | 0.00 USD | `+6.60%` | `22,763.00` |
| `Live` | `Short` | `1.40` | 497,370.00 USD | 11,740.00 USD | 0.00 USD | `+7.37%` | `8,418.00` |
| `Live` | `Short` | `1.41` | 498,320.00 USD | 952.59 USD | 0.00 USD | `+8.14%` | `678.00` |
| `Live` | `Short` | `1.42` | 502,180.00 USD | 3,860.00 USD | 0.00 USD | `+8.91%` | `2,727.00` |
| `Live` | `Short` | `1.43` | 597,540.00 USD | 95,360.00 USD | 0.00 USD | `+9.68%` | `66,921.00` |
| `Live` | `Short` | `1.44` | 779,460.00 USD | 181,920.00 USD | 0.00 USD | `+10.45%` | `126,772.00` |
| `Live` | `Short` | `1.45` | 790,850.00 USD | 11,390.00 USD | 0.00 USD | `+11.22%` | `7,884.00` |
| `Live` | `Short` | `1.46` | 796,610.00 USD | 5,760.00 USD | 0.00 USD | `+11.99%` | `3,957.00` |
| `Live` | `Short` | `1.47` | 824,950.00 USD | 28,340.00 USD | 0.00 USD | `+12.76%` | `19,347.00` |
| `Live` | `Short` | `1.48` | 836,780.00 USD | 11,820.00 USD | 0.00 USD | `+13.53%` | `8,016.00` |
| `Live` | `Short` | `1.49` | 837,010.00 USD | 227.20 USD | 0.00 USD | `+14.30%` | `153.00` |
| `Live` | `Short` | `1.50` | 849,690.00 USD | 12,680.00 USD | 0.00 USD | `+15.07%` | `8,482.00` |
| `Live` | `Short` | `1.50` | 897,260.00 USD | 47,570.00 USD | 0.00 USD | `+15.84%` | `31,611.00` |
| `Live` | `Short` | `1.51` | 899,200.00 USD | 1,940.00 USD | 0.00 USD | `+16.61%` | `1,280.00` |
| `Live` | `Short` | `1.53` | 900,330.00 USD | 1,130.00 USD | 0.00 USD | `+18.15%` | `734.00` |
| `Live` | `Short` | `1.54` | 906,640.00 USD | 6,320.00 USD | 0.00 USD | `+18.92%` | `4,088.00` |
| `Live` | `Short` | `1.55` | 908,000.00 USD | 1,360.00 USD | 0.00 USD | `+19.69%` | `873.00` |
| `Live` | `Short` | `1.56` | 908,560.00 USD | 555.57 USD | 0.00 USD | `+20.46%` | `355.00` |
| `Live` | `Short` | `1.57` | 911,390.00 USD | 2,840.00 USD | 0.00 USD | `+21.23%` | `1,800.00` |
| `Live` | `Short` | `1.58` | 918,960.00 USD | 7,570.00 USD | 0.00 USD | `+22.00%` | `4,773.00` |
| `Live` | `Short` | `1.59` | 1,240,000.00 USD | 321,070.00 USD | 0.00 USD | `+22.77%` | `201,298.00` |
| `Live` | `Short` | `1.60` | 6,460,000.00 USD | 5,220,000.00 USD | 0.00 USD | `+23.54%` | `3,253,745.00` |
| `Live` | `Short` | `1.61` | 11,350,000.00 USD | 4,890,000.00 USD | 0.00 USD | `+24.31%` | `3,025,482.00` |
| `Live` | `Short` | `1.62` | 11,350,000.00 USD | 6,420.00 USD | 0.00 USD | `+25.08%` | `3,950.00` |
| `Live` | `Short` | `1.64` | 11,370,000.00 USD | 11,270.00 USD | 0.00 USD | `+25.85%` | `6,892.00` |
| `Live` | `Short` | `1.65` | 11,500,000.00 USD | 133,590.00 USD | 0.00 USD | `+26.62%` | `81,210.00` |
| `Live` | `Short` | `1.66` | 11,500,000.00 USD | 911.91 USD | 0.00 USD | `+27.39%` | `551.00` |
| `Live` | `Short` | `1.67` | 11,500,000.00 USD | 586.08 USD | 0.00 USD | `+28.16%` | `352.00` |
| `Live` | `Short` | `1.68` | 11,500,000.00 USD | 760.45 USD | 0.00 USD | `+28.93%` | `454.00` |
| `Live` | `Short` | `1.69` | 11,550,000.00 USD | 47,320.00 USD | 0.00 USD | `+29.70%` | `28,084.00` |
| `Live` | `Short` | `1.70` | 11,550,000.00 USD | 1,040.00 USD | 0.00 USD | `+30.46%` | `615.00` |
| `Live` | `Short` | `1.71` | 11,550,000.00 USD | 1,980.00 USD | 0.00 USD | `+31.23%` | `1,163.00` |
| `Live` | `Short` | `1.72` | 11,560,000.00 USD | 10,410.00 USD | 0.00 USD | `+32.00%` | `6,068.00` |
| `Live` | `Short` | `1.73` | 11,560,000.00 USD | 1,920.00 USD | 0.00 USD | `+32.77%` | `1,115.00` |
| `Live` | `Short` | `1.74` | 11,570,000.00 USD | 2,970.00 USD | 0.00 USD | `+33.54%` | `1,713.00` |
| `Live` | `Short` | `1.75` | 11,570,000.00 USD | 3,260.00 USD | 0.00 USD | `+34.31%` | `1,869.00` |
| `Live` | `Short` | `1.75` | 11,570,000.00 USD | 4,000.00 USD | 0.00 USD | `+35.08%` | `2,277.00` |
| `Live` | `Short` | `1.76` | 11,580,000.00 USD | 2,540.00 USD | 0.00 USD | `+35.85%` | `1,440.00` |
| `Live` | `Short` | `1.77` | 11,580,000.00 USD | 2,040.00 USD | 0.00 USD | `+36.62%` | `1,148.00` |
| `Live` | `Short` | `1.78` | 11,710,000.00 USD | 129,540.00 USD | 0.00 USD | `+37.39%` | `72,574.00` |
| `Live` | `Short` | `1.79` | 11,710,000.00 USD | 3,210.00 USD | 0.00 USD | `+38.16%` | `1,790.00` |
| `Live` | `Short` | `1.80` | 11,710,000.00 USD | 889.87 USD | 0.00 USD | `+38.93%` | `493.00` |
| `Live` | `Short` | `1.81` | 14,510,000.00 USD | 2,800,000.00 USD | 0.00 USD | `+39.70%` | `1,541,357.00` |
| `Live` | `Short` | `1.82` | 14,510,000.00 USD | 297.48 USD | 0.00 USD | `+40.47%` | `163.00` |
| `Live` | `Short` | `1.83` | 14,510,000.00 USD | 889.98 USD | 0.00 USD | `+41.24%` | `485.00` |
| `Live` | `Short` | `1.84` | 14,520,000.00 USD | 5,540.00 USD | 0.00 USD | `+42.01%` | `3,000.00` |
| `Live` | `Short` | `1.85` | 14,520,000.00 USD | 632.55 USD | 0.00 USD | `+42.78%` | `341.00` |
| `Live` | `Short` | `1.86` | 14,520,000.00 USD | 2,040.00 USD | 0.00 USD | `+43.55%` | `1,095.00` |
| `Live` | `Short` | `1.88` | 14,770,000.00 USD | 246,040.00 USD | 0.00 USD | `+44.32%` | `131,222.00` |
| `Live` | `Short` | `1.89` | 14,770,000.00 USD | 339.30 USD | 0.00 USD | `+45.09%` | `180.00` |
| `Live` | `Short` | `1.90` | 14,770,000.00 USD | 4,190.00 USD | 0.00 USD | `+45.86%` | `2,211.00` |
| `Live` | `Short` | `1.91` | 14,840,000.00 USD | 69,460.00 USD | 0.00 USD | `+46.63%` | `36,460.00` |
| `Live` | `Short` | `1.93` | 14,840,000.00 USD | 103.95 USD | 0.00 USD | `+48.17%` | `54.00` |
| `Live` | `Short` | `1.94` | 14,850,000.00 USD | 8,870.00 USD | 0.00 USD | `+48.94%` | `4,584.00` |
| `Live` | `Short` | `1.95` | 14,850,000.00 USD | 287.86 USD | 0.00 USD | `+49.71%` | `148.00` |
| `Live` | `Short` | `1.96` | 14,850,000.00 USD | 293.25 USD | 0.00 USD | `+50.48%` | `150.00` |
| `Live` | `Short` | `1.97` | 15,180,000.00 USD | 333,390.00 USD | 0.00 USD | `+51.25%` | `169,663.00` |
| `Live` | `Short` | `1.98` | 15,180,000.00 USD | 651.75 USD | 0.00 USD | `+52.02%` | `330.00` |
| `Live` | `Short` | `2.00` | 15,180,000.00 USD | 1,120.00 USD | 0.00 USD | `+53.56%` | `561.00` |
| `Live` | `Short` | `2.00` | 15,580,000.00 USD | 393,140.00 USD | 0.00 USD | `+54.33%` | `196,081.00` |
| `Live` | `Short` | `2.02` | 15,580,000.00 USD | 513.83 USD | 0.00 USD | `+55.10%` | `255.00` |
| `Live` | `Short` | `2.04` | 15,860,000.00 USD | 279,600.00 USD | 0.00 USD | `+57.40%` | `136,722.00` |
| `Live` | `Short` | `2.06` | 15,860,000.00 USD | 5,330.00 USD | 0.00 USD | `+58.94%` | `2,583.00` |
| `Live` | `Short` | `2.10` | 15,870,000.00 USD | 2,540.00 USD | 0.00 USD | `+61.25%` | `1,214.00` |
| `Live` | `Short` | `2.10` | 15,870,000.00 USD | 1,960.00 USD | 0.00 USD | `+62.02%` | `929.00` |
| `Live` | `Short` | `2.12` | 15,870,000.00 USD | 3,100.00 USD | 0.00 USD | `+62.79%` | `1,468.00` |
| `Live` | `Short` | `2.15` | 15,870,000.00 USD | 196.11 USD | 0.00 USD | `+65.87%` | `91.00` |
| `Live` | `Short` | `2.17` | 15,870,000.00 USD | 2,830.00 USD | 0.00 USD | `+67.41%` | `1,299.00` |
| `Live` | `Short` | `2.19` | 15,870,000.00 USD | 100.51 USD | 0.00 USD | `+68.18%` | `46.00` |
| `Live` | `Short` | `2.19` | 15,950,000.00 USD | 72,080.00 USD | 0.00 USD | `+68.95%` | `32,837.00` |
| `Live` | `Short` | `2.23` | 15,950,000.00 USD | 3,890.00 USD | 0.00 USD | `+71.26%` | `1,748.00` |
| `Live` | `Short` | `2.25` | 18,300,000.00 USD | 2,350,000.00 USD | 0.00 USD | `+72.80%` | `1,048,956.00` |
| `Live` | `Short` | `2.27` | 21,770,000.00 USD | 3,460,000.00 USD | 0.00 USD | `+74.34%` | `1,529,461.00` |
| `Live` | `Short` | `2.27` | 21,780,000.00 USD | 14,930.00 USD | 0.00 USD | `+75.11%` | `6,561.00` |
| `Live` | `Short` | `2.29` | 22,850,000.00 USD | 1,060,000.00 USD | 0.00 USD | `+75.88%` | `465,112.00` |
| `Live` | `Short` | `2.31` | 22,940,000.00 USD | 92,880.00 USD | 0.00 USD | `+77.42%` | `40,296.00` |
| `Live` | `Short` | `2.33` | 22,940,000.00 USD | 3,280.00 USD | 0.00 USD | `+78.96%` | `1,409.00` |
| `Live` | `Short` | `2.33` | 23,120,000.00 USD | 175,880.00 USD | 0.00 USD | `+79.73%` | `75,323.00` |
| `Live` | `Short` | `2.35` | 23,120,000.00 USD | 108.33 USD | 0.00 USD | `+81.27%` | `46.00` |
| `Live` | `Short` | `2.37` | 23,120,000.00 USD | 146.63 USD | 0.00 USD | `+82.04%` | `62.00` |
| `Live` | `Short` | `2.38` | 23,210,000.00 USD | 91,880.00 USD | 0.00 USD | `+82.80%` | `38,688.00` |
| `Live` | `Short` | `2.38` | 23,290,000.00 USD | 74,260.00 USD | 0.00 USD | `+83.57%` | `31,136.00` |
| `Live` | `Short` | `2.40` | 23,290,000.00 USD | 167.65 USD | 0.00 USD | `+84.34%` | `70.00` |
| `Live` | `Short` | `2.40` | 23,290,000.00 USD | 1,210.00 USD | 0.00 USD | `+85.11%` | `504.00` |
| `Live` | `Short` | `2.42` | 23,290,000.00 USD | 2,420.00 USD | 0.00 USD | `+85.88%` | `1,000.00` |
| `Live` | `Short` | `2.46` | 23,310,000.00 USD | 24,840.00 USD | 0.00 USD | `+89.73%` | `10,078.00` |
| `Live` | `Short` | `2.48` | 23,570,000.00 USD | 256,540.00 USD | 0.00 USD | `+90.50%` | `103,651.00` |
| `Live` | `Short` | `2.50` | 23,570,000.00 USD | 114.77 USD | 0.00 USD | `+92.04%` | `46.00` |
| `Live` | `Short` | `2.52` | 23,580,000.00 USD | 5,640.00 USD | 0.00 USD | `+93.58%` | `2,244.00` |
| `Live` | `Short` | `2.52` | 23,620,000.00 USD | 42,710.00 USD | 0.00 USD | `+94.35%` | `16,914.00` |
| `Live` | `Short` | `2.54` | 23,620,000.00 USD | 613.47 USD | 0.00 USD | `+95.12%` | `242.00` |
| `Live` | `Short` | `2.56` | 27,490,000.00 USD | 3,870,000.00 USD | 0.00 USD | `+96.66%` | `1,516,193.00` |
| `Live` | `Short` | `2.56` | 27,490,000.00 USD | 346.27 USD | 0.00 USD | `+97.43%` | `135.00` |
| `Live` | `Short` | `2.58` | 27,500,000.00 USD | 2,250.00 USD | 0.00 USD | `+98.20%` | `875.00` |
| `Live` | `Short` | `2.58` | 27,520,000.00 USD | 23,350.00 USD | 0.00 USD | `+98.97%` | `9,031.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.3050` | 197,030,000.00 USD | 0.00 USD | 147.62 USD | `-76.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3250` | 197,030,000.00 USD | 0.00 USD | 145.28 USD | `-74.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3750` | 197,030,000.00 USD | 0.00 USD | 139.12 USD | `-71.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4150` | 197,030,000.00 USD | 0.00 USD | 200.86 USD | `-68.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4250` | 197,030,000.00 USD | 0.00 USD | 173.82 USD | `-67.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4450` | 197,030,000.00 USD | 0.00 USD | 408.51 USD | `-65.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4550` | 197,030,000.00 USD | 0.00 USD | 520.52 USD | `-64.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4650` | 197,030,000.00 USD | 0.00 USD | 151.12 USD | `-64.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4750` | 197,030,000.00 USD | 0.00 USD | 190.00 USD | `-63.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4850` | 197,030,000.00 USD | 0.00 USD | 145.50 USD | `-62.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5050` | 197,020,000.00 USD | 0.00 USD | 1,030.00 USD | `-61.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5250` | 197,020,000.00 USD | 0.00 USD | 306.60 USD | `-59.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5550` | 197,020,000.00 USD | 0.00 USD | 6,750.00 USD | `-57.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5650` | 197,020,000.00 USD | 0.00 USD | 374.60 USD | `-56.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5850` | 197,020,000.00 USD | 0.00 USD | 100.62 USD | `-54.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6350` | 197,020,000.00 USD | 0.00 USD | 791.85 USD | `-51.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6450` | 197,020,000.00 USD | 0.00 USD | 573.40 USD | `-50.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6550` | 197,010,000.00 USD | 0.00 USD | 3,450.00 USD | `-49.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6650` | 197,010,000.00 USD | 0.00 USD | 3,010.00 USD | `-48.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6950` | 197,010,000.00 USD | 0.00 USD | 1,060.00 USD | `-46.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7050` | 197,010,000.00 USD | 0.00 USD | 1,590.00 USD | `-45.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7550` | 197,010,000.00 USD | 0.00 USD | 1,300.00 USD | `-41.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7650` | 197,000,000.00 USD | 0.00 USD | 2,880.00 USD | `-41.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7950` | 197,000,000.00 USD | 0.00 USD | 1,110.00 USD | `-38.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8550` | 197,000,000.00 USD | 0.00 USD | 798.57 USD | `-34.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8750` | 197,000,000.00 USD | 0.00 USD | 690.38 USD | `-32.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8850` | 197,000,000.00 USD | 0.00 USD | 1,420.00 USD | `-31.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8950` | 197,000,000.00 USD | 0.00 USD | 1,910.00 USD | `-31.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9050` | 197,000,000.00 USD | 0.00 USD | 838.94 USD | `-30.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9150` | 196,990,000.00 USD | 0.00 USD | 188.49 USD | `-29.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9250` | 196,990,000.00 USD | 0.00 USD | 2,730.00 USD | `-28.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9350` | 196,990,000.00 USD | 0.00 USD | 1,150.00 USD | `-28.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9450` | 196,990,000.00 USD | 0.00 USD | 112.46 USD | `-27.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9550` | 196,990,000.00 USD | 0.00 USD | 2,360.00 USD | `-26.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9650` | 196,990,000.00 USD | 0.00 USD | 3,910.00 USD | `-25.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9750` | 196,980,000.00 USD | 0.00 USD | 546,370.00 USD | `-24.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9850` | 196,440,000.00 USD | 0.00 USD | 5,250.00 USD | `-24.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9950` | 196,430,000.00 USD | 0.00 USD | 897.49 USD | `-23.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.00` | 196,430,000.00 USD | 0.00 USD | 15,070.00 USD | `-22.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.01` | 196,420,000.00 USD | 0.00 USD | 4,330.00 USD | `-21.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.02` | 196,410,000.00 USD | 0.00 USD | 2,020.00 USD | `-21.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.03` | 196,410,000.00 USD | 0.00 USD | 38,000.00 USD | `-20.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.04` | 196,370,000.00 USD | 0.00 USD | 3,970.00 USD | `-19.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.05` | 196,370,000.00 USD | 0.00 USD | 7,090.00 USD | `-18.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.06` | 196,360,000.00 USD | 0.00 USD | 3,230.00 USD | `-18.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.07` | 196,360,000.00 USD | 0.00 USD | 34,770.00 USD | `-17.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.08` | 196,320,000.00 USD | 0.00 USD | 973.25 USD | `-16.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.09` | 196,320,000.00 USD | 0.00 USD | 8,250.00 USD | `-15.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.10` | 196,310,000.00 USD | 0.00 USD | 2,970.00 USD | `-14.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.11` | 196,310,000.00 USD | 0.00 USD | 9,300.00 USD | `-14.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.12` | 196,300,000.00 USD | 0.00 USD | 77,120.00 USD | `-13.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.14` | 196,220,000.00 USD | 0.00 USD | 12,910.00 USD | `-12.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.15` | 196,210,000.00 USD | 0.00 USD | 35,220.00 USD | `-11.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.16` | 196,180,000.00 USD | 0.00 USD | 5,360.00 USD | `-11.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.17` | 196,170,000.00 USD | 0.00 USD | 14,080.00 USD | `-10.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.18` | 196,160,000.00 USD | 0.00 USD | 4,790.00 USD | `-9.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.19` | 196,150,000.00 USD | 0.00 USD | 90,010.00 USD | `-8.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.20` | 196,060,000.00 USD | 0.00 USD | 12,570.00 USD | `-8.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.21` | 196,050,000.00 USD | 0.00 USD | 57,020.00 USD | `-7.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.22` | 195,990,000.00 USD | 0.00 USD | 57,160.00 USD | `-6.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.23` | 195,940,000.00 USD | 0.00 USD | 144,860.00 USD | `-5.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.24` | 195,790,000.00 USD | 0.00 USD | 398,990.00 USD | `-4.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.25` | 195,390,000.00 USD | 0.00 USD | 258,780.00 USD | `-4.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.25` | 195,130,000.00 USD | 0.00 USD | 480,130.00 USD | `-3.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.26` | 194,650,000.00 USD | 0.00 USD | 134,550.00 USD | `-2.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.27` | 194,520,000.00 USD | 0.00 USD | 360,930.00 USD | `-1.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.28` | 194,160,000.00 USD | 0.00 USD | 64,520,000.00 USD | `-1.09%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1.29` | 129,630,000.00 USD | 0.00 USD | 129,630,000.00 USD | `-0.32%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `1.30` | 2,670.00 USD | 2,670.00 USD | 0.00 USD | `+0.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 69,370.00 USD | 66,700.00 USD | 0.00 USD | `+1.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.32` | 352,430.00 USD | 283,070.00 USD | 0.00 USD | `+1.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 462,870.00 USD | 110,440.00 USD | 0.00 USD | `+2.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 635,700.00 USD | 172,830.00 USD | 0.00 USD | `+3.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 664,110.00 USD | 28,410.00 USD | 0.00 USD | `+4.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 964,200.00 USD | 300,090.00 USD | 0.00 USD | `+5.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.38` | 1,040,000.00 USD | 73,650.00 USD | 0.00 USD | `+5.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 1,110,000.00 USD | 71,640.00 USD | 0.00 USD | `+6.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 1,190,000.00 USD | 81,740.00 USD | 0.00 USD | `+7.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 5,560,000.00 USD | 4,370,000.00 USD | 0.00 USD | `+8.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 5,600,000.00 USD | 31,160.00 USD | 0.00 USD | `+8.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 5,620,000.00 USD | 19,800.00 USD | 0.00 USD | `+9.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 5,700,000.00 USD | 82,400.00 USD | 0.00 USD | `+10.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 5,960,000.00 USD | 260,610.00 USD | 0.00 USD | `+11.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.46` | 6,000,000.00 USD | 44,870.00 USD | 0.00 USD | `+11.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 6,030,000.00 USD | 27,080.00 USD | 0.00 USD | `+12.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.48` | 6,140,000.00 USD | 108,480.00 USD | 0.00 USD | `+13.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 6,220,000.00 USD | 84,290.00 USD | 0.00 USD | `+14.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 6,240,000.00 USD | 15,160.00 USD | 0.00 USD | `+15.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 6,320,000.00 USD | 84,680.00 USD | 0.00 USD | `+15.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.51` | 6,340,000.00 USD | 18,210.00 USD | 0.00 USD | `+16.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 6,370,000.00 USD | 32,440.00 USD | 0.00 USD | `+17.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.53` | 6,430,000.00 USD | 57,450.00 USD | 0.00 USD | `+18.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.54` | 6,470,000.00 USD | 36,160.00 USD | 0.00 USD | `+18.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 6,470,000.00 USD | 6,110.00 USD | 0.00 USD | `+19.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.56` | 6,480,000.00 USD | 6,300.00 USD | 0.00 USD | `+20.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.57` | 6,490,000.00 USD | 6,410.00 USD | 0.00 USD | `+21.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.58` | 6,500,000.00 USD | 9,700.00 USD | 0.00 USD | `+22.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.59` | 6,620,000.00 USD | 126,740.00 USD | 0.00 USD | `+22.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.60` | 6,620,000.00 USD | 1,130.00 USD | 0.00 USD | `+23.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.61` | 6,710,000.00 USD | 83,090.00 USD | 0.00 USD | `+24.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.62` | 6,710,000.00 USD | 464.75 USD | 0.00 USD | `+25.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 6,910,000.00 USD | 199,230.00 USD | 0.00 USD | `+25.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.65` | 6,910,000.00 USD | 3,970.00 USD | 0.00 USD | `+26.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 6,940,000.00 USD | 33,550.00 USD | 0.00 USD | `+27.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 6,950,000.00 USD | 8,220.00 USD | 0.00 USD | `+28.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.68` | 6,960,000.00 USD | 5,760.00 USD | 0.00 USD | `+28.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.69` | 7,030,000.00 USD | 70,850.00 USD | 0.00 USD | `+29.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.70` | 7,040,000.00 USD | 8,570.00 USD | 0.00 USD | `+30.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.71` | 7,300,000.00 USD | 259,410.00 USD | 0.00 USD | `+31.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.72` | 7,310,000.00 USD | 14,030.00 USD | 0.00 USD | `+32.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.73` | 7,330,000.00 USD | 14,560.00 USD | 0.00 USD | `+32.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.74` | 7,370,000.00 USD | 44,100.00 USD | 0.00 USD | `+33.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 7,370,000.00 USD | 4,710.00 USD | 0.00 USD | `+34.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 7,380,000.00 USD | 6,330.00 USD | 0.00 USD | `+35.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.76` | 7,400,000.00 USD | 21,720.00 USD | 0.00 USD | `+35.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 7,520,000.00 USD | 122,200.00 USD | 0.00 USD | `+36.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.78` | 7,620,000.00 USD | 96,900.00 USD | 0.00 USD | `+37.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.79` | 7,660,000.00 USD | 33,690.00 USD | 0.00 USD | `+38.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 7,660,000.00 USD | 254.51 USD | 0.00 USD | `+38.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.81` | 7,660,000.00 USD | 2,530.00 USD | 0.00 USD | `+39.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.82` | 7,660,000.00 USD | 1,830.00 USD | 0.00 USD | `+40.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.83` | 7,670,000.00 USD | 7,630.00 USD | 0.00 USD | `+41.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.84` | 7,670,000.00 USD | 5,700.00 USD | 0.00 USD | `+42.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.85` | 7,680,000.00 USD | 8,390.00 USD | 0.00 USD | `+42.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.88` | 7,690,000.00 USD | 4,550.00 USD | 0.00 USD | `+44.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.89` | 7,690,000.00 USD | 591.89 USD | 0.00 USD | `+45.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.90` | 7,730,000.00 USD | 44,350.00 USD | 0.00 USD | `+45.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.91` | 7,740,000.00 USD | 10,020.00 USD | 0.00 USD | `+46.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.92` | 7,750,000.00 USD | 7,410.00 USD | 0.00 USD | `+47.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.94` | 7,750,000.00 USD | 265.10 USD | 0.00 USD | `+48.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.95` | 7,750,000.00 USD | 2,040.00 USD | 0.00 USD | `+49.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.96` | 7,750,000.00 USD | 1,510.00 USD | 0.00 USD | `+50.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.97` | 7,770,000.00 USD | 14,120.00 USD | 0.00 USD | `+51.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.98` | 7,770,000.00 USD | 4,010.00 USD | 0.00 USD | `+52.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.99` | 7,770,000.00 USD | 325.54 USD | 0.00 USD | `+52.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 7,780,000.00 USD | 7,020.00 USD | 0.00 USD | `+53.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 7,920,000.00 USD | 138,900.00 USD | 0.00 USD | `+54.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.02` | 7,920,000.00 USD | 781.82 USD | 0.00 USD | `+55.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.02` | 7,920,000.00 USD | 222.75 USD | 0.00 USD | `+55.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 7,920,000.00 USD | 862.84 USD | 0.00 USD | `+56.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 7,920,000.00 USD | 3,490.00 USD | 0.00 USD | `+57.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.06` | 7,930,000.00 USD | 3,940.00 USD | 0.00 USD | `+58.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.08` | 7,930,000.00 USD | 661.93 USD | 0.00 USD | `+59.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 8,050,000.00 USD | 124,400.00 USD | 0.00 USD | `+61.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 8,050,000.00 USD | 1,580.00 USD | 0.00 USD | `+62.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.12` | 8,070,000.00 USD | 13,900.00 USD | 0.00 USD | `+63.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 8,090,000.00 USD | 24,840.00 USD | 0.00 USD | `+65.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 8,140,000.00 USD | 50,580.00 USD | 0.00 USD | `+65.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.17` | 8,140,000.00 USD | 1,710.00 USD | 0.00 USD | `+66.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.19` | 8,150,000.00 USD | 1,970.00 USD | 0.00 USD | `+68.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.21` | 8,300,000.00 USD | 151,380.00 USD | 0.00 USD | `+70.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.23` | 8,300,000.00 USD | 7,340.00 USD | 0.00 USD | `+72.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.27` | 8,310,000.00 USD | 3,120.00 USD | 0.00 USD | `+75.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 8,310,000.00 USD | 1,140.00 USD | 0.00 USD | `+75.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 8,320,000.00 USD | 12,150.00 USD | 0.00 USD | `+76.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.31` | 8,320,000.00 USD | 370.40 USD | 0.00 USD | `+78.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.33` | 8,370,000.00 USD | 47,430.00 USD | 0.00 USD | `+79.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.37` | 8,370,000.00 USD | 2,410.00 USD | 0.00 USD | `+82.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.38` | 8,370,000.00 USD | 475.00 USD | 0.00 USD | `+82.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 8,370,000.00 USD | 2,540.00 USD | 0.00 USD | `+84.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 8,630,000.00 USD | 251,200.00 USD | 0.00 USD | `+85.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.42` | 8,630,000.00 USD | 1,370.00 USD | 0.00 USD | `+85.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.44` | 8,630,000.00 USD | 564.92 USD | 0.00 USD | `+87.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.46` | 8,640,000.00 USD | 8,110.00 USD | 0.00 USD | `+88.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.48` | 8,640,000.00 USD | 3,420.00 USD | 0.00 USD | `+91.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.50` | 8,640,000.00 USD | 124.75 USD | 0.00 USD | `+92.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.50` | 8,680,000.00 USD | 42,600.00 USD | 0.00 USD | `+92.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.52` | 8,680,000.00 USD | 378.75 USD | 0.00 USD | `+94.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.56` | 8,680,000.00 USD | 389.88 USD | 0.00 USD | `+97.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.58` | 8,680,000.00 USD | 775.50 USD | 0.00 USD | `+98.97%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `1.16` | 221,570,000.00 USD | 0.00 USD | 221,570,000.00 USD | 100,770.00 USD | 64,860.00 USD | 127,210.00 USD |
| `7D` | `1.16` | 221,270,000.00 USD | 0.00 USD | 221,270,000.00 USD | 173,190.00 USD | 99,350.00 USD | 396,520.00 USD |
| `7D` | `1.16` | 220,600,000.00 USD | 0.00 USD | 220,600,000.00 USD | 171,750.00 USD | 52,740.00 USD | 204,770.00 USD |
| `7D` | `1.16` | 220,180,000.00 USD | 0.00 USD | 220,180,000.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD |
| `7D` | `1.16` | 219,150,000.00 USD | 0.00 USD | 219,150,000.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD |
| `1D` | `1.17` | 80,480,000.00 USD | 0.00 USD | 80,480,000.00 USD | 172,040.00 USD | 61,210.00 USD | 202,250.00 USD |
| `7D` | `1.17` | 217,780,000.00 USD | 0.00 USD | 217,780,000.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD |
| `1D` | `1.17` | 80,040,000.00 USD | 0.00 USD | 80,040,000.00 USD | 152,440.00 USD | 38,870.00 USD | 60,250.00 USD |
| `7D` | `1.17` | 217,150,000.00 USD | 0.00 USD | 217,150,000.00 USD | 406,410.00 USD | 132,100.00 USD | 785,270.00 USD |
| `1D` | `1.17` | 79,790,000.00 USD | 0.00 USD | 79,790,000.00 USD | 86,630.00 USD | 31,280.00 USD | 43,000.00 USD |
| `7D` | `1.17` | 215,830,000.00 USD | 0.00 USD | 215,830,000.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD |
| `1D` | `1.17` | 79,630,000.00 USD | 0.00 USD | 79,630,000.00 USD | 27,580.00 USD | 49,790.00 USD | 94,780.00 USD |
| `7D` | `1.17` | 214,320,000.00 USD | 0.00 USD | 214,320,000.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD |
| `1D` | `1.17` | 79,460,000.00 USD | 0.00 USD | 79,460,000.00 USD | 32,280.00 USD | 26,620.00 USD | 195,860.00 USD |
| `7D` | `1.17` | 212,930,000.00 USD | 0.00 USD | 212,930,000.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD |
| `1D` | `1.18` | 79,200,000.00 USD | 0.00 USD | 79,200,000.00 USD | 141,540.00 USD | 16,760.00 USD | 182,860.00 USD |
| `7D` | `1.18` | 212,130,000.00 USD | 0.00 USD | 212,130,000.00 USD | 290,470.00 USD | 107,150.00 USD | 505,430.00 USD |
| `1D` | `1.18` | 78,860,000.00 USD | 0.00 USD | 78,860,000.00 USD | 80,830.00 USD | 13,900.00 USD | 30,960.00 USD |
| `7D` | `1.18` | 211,230,000.00 USD | 0.00 USD | 211,230,000.00 USD | 154,760.00 USD | 93,720.00 USD | 245,840.00 USD |
| `1D` | `1.18` | 78,730,000.00 USD | 0.00 USD | 78,730,000.00 USD | 77,850.00 USD | 41,360.00 USD | 49,320.00 USD |
| `7D` | `1.18` | 210,740,000.00 USD | 0.00 USD | 210,740,000.00 USD | 299,590.00 USD | 131,210.00 USD | 459,970.00 USD |
| `1D` | `1.18` | 78,570,000.00 USD | 0.00 USD | 78,570,000.00 USD | 19,950.00 USD | 11,210.00 USD | 2,560.00 USD |
| `7D` | `1.18` | 209,840,000.00 USD | 0.00 USD | 209,840,000.00 USD | 69,670.00 USD | 152,290.00 USD | 286,090.00 USD |
| `1D` | `1.18` | 78,530,000.00 USD | 0.00 USD | 78,530,000.00 USD | 37,820.00 USD | 22,830.00 USD | 66,040.00 USD |
| `7D` | `1.18` | 209,340,000.00 USD | 0.00 USD | 209,340,000.00 USD | 67,200.00 USD | 53,830.00 USD | 12,180.00 USD |
| `1D` | `1.19` | 78,410,000.00 USD | 0.00 USD | 78,410,000.00 USD | 56,380.00 USD | 20,760.00 USD | 28,230.00 USD |
| `7D` | `1.19` | 209,200,000.00 USD | 0.00 USD | 209,200,000.00 USD | 81,610.00 USD | 98,170.00 USD | 428,040.00 USD |
| `1D` | `1.19` | 78,300,000.00 USD | 0.00 USD | 78,300,000.00 USD | 50,010.00 USD | 37,580.00 USD | 102,510.00 USD |
| `7D` | `1.19` | 208,600,000.00 USD | 0.00 USD | 208,600,000.00 USD | 190,550.00 USD | 38,510.00 USD | 383,280.00 USD |
| `1D` | `1.19` | 78,110,000.00 USD | 0.00 USD | 78,110,000.00 USD | 60,820.00 USD | 4,280.00 USD | 13,230.00 USD |
| `7D` | `1.19` | 207,980,000.00 USD | 0.00 USD | 207,980,000.00 USD | 186,430.00 USD | 128,180.00 USD | 350,400.00 USD |
| `1D` | `1.19` | 78,030,000.00 USD | 0.00 USD | 78,030,000.00 USD | 36,460.00 USD | 10,480.00 USD | 75,640.00 USD |
| `7D` | `1.19` | 207,320,000.00 USD | 0.00 USD | 207,320,000.00 USD | 130,690.00 USD | 67,850.00 USD | 262,740.00 USD |
| `1D` | `1.19` | 77,910,000.00 USD | 0.00 USD | 77,910,000.00 USD | 67,440.00 USD | 29,830.00 USD | 130,440.00 USD |
| `7D` | `1.19` | 206,860,000.00 USD | 0.00 USD | 206,860,000.00 USD | 218,910.00 USD | 107,850.00 USD | 335,240.00 USD |
| `1D` | `1.20` | 77,680,000.00 USD | 0.00 USD | 77,680,000.00 USD | 106,940.00 USD | 33,950.00 USD | 32,860.00 USD |
| `7D` | `1.20` | 206,190,000.00 USD | 0.00 USD | 206,190,000.00 USD | 338,060.00 USD | 79,070.00 USD | 291,070.00 USD |
| `1D` | `1.20` | 77,510,000.00 USD | 0.00 USD | 77,510,000.00 USD | 134,160.00 USD | 6,620.00 USD | 61,430.00 USD |
| `7D` | `1.20` | 205,490,000.00 USD | 0.00 USD | 205,490,000.00 USD | 5,350.00 USD | 93,870.00 USD | 187,830.00 USD |
| `1D` | `1.20` | 77,310,000.00 USD | 0.00 USD | 77,310,000.00 USD | 41,430.00 USD | 21,290.00 USD | 1,700.00 USD |
| `7D` | `1.20` | 205,200,000.00 USD | 0.00 USD | 205,200,000.00 USD | 67,200.00 USD | 57,670.00 USD | 21,970.00 USD |
| `1D` | `1.20` | 77,240,000.00 USD | 0.00 USD | 77,240,000.00 USD | 23,000.00 USD | 6,640.00 USD | 1,060.00 USD |
| `7D` | `1.20` | 205,050,000.00 USD | 0.00 USD | 205,050,000.00 USD | 34,730.00 USD | 26,000.00 USD | 15,030.00 USD |
| `1D` | `1.20` | 77,210,000.00 USD | 0.00 USD | 77,210,000.00 USD | 43,340.00 USD | 13,890.00 USD | 61,870.00 USD |
| `7D` | `1.20` | 204,980,000.00 USD | 0.00 USD | 204,980,000.00 USD | 202,570.00 USD | 53,170.00 USD | 48,290.00 USD |
| `7D` | `1.21` | 204,670,000.00 USD | 0.00 USD | 204,670,000.00 USD | 0.00 USD | 14,550.00 USD | 79,720.00 USD |
| `1D` | `1.21` | 77,090,000.00 USD | 0.00 USD | 77,090,000.00 USD | 2,880.00 USD | 5,600.00 USD | 814.23 USD |
| `7D` | `1.21` | 204,580,000.00 USD | 0.00 USD | 204,580,000.00 USD | 80,450.00 USD | 5,390.00 USD | 9,940.00 USD |
| `1D` | `1.21` | 77,080,000.00 USD | 0.00 USD | 77,080,000.00 USD | 0.00 USD | 0.00 USD | 32,130.00 USD |
| `7D` | `1.21` | 204,480,000.00 USD | 0.00 USD | 204,480,000.00 USD | 361,660.00 USD | 45,260.00 USD | 357,420.00 USD |
| `7D` | `1.21` | 203,720,000.00 USD | 0.00 USD | 203,720,000.00 USD | 70,670.00 USD | 152,900.00 USD | 457,650.00 USD |
| `7D` | `1.21` | 203,040,000.00 USD | 0.00 USD | 203,040,000.00 USD | 278,240.00 USD | 50,420.00 USD | 33,960.00 USD |
| `7D` | `1.22` | 202,670,000.00 USD | 0.00 USD | 202,670,000.00 USD | 5,680.00 USD | 39,860.00 USD | 0.00 USD |
| `7D` | `1.22` | 202,630,000.00 USD | 0.00 USD | 202,630,000.00 USD | 97,920.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.22` | 202,530,000.00 USD | 0.00 USD | 202,530,000.00 USD | 0.00 USD | 765.15 USD | 40,620.00 USD |
| `7D` | `1.22` | 202,490,000.00 USD | 0.00 USD | 202,490,000.00 USD | 54,470.00 USD | 2,490.00 USD | 14,710.00 USD |
| `7D` | `1.22` | 202,420,000.00 USD | 0.00 USD | 202,420,000.00 USD | 10,460.00 USD | 191,360.00 USD | 207,400.00 USD |
| `7D` | `1.23` | 202,010,000.00 USD | 0.00 USD | 202,010,000.00 USD | 649,620.00 USD | 191,250.00 USD | 200,510.00 USD |
| `7D` | `1.23` | 200,970,000.00 USD | 0.00 USD | 200,970,000.00 USD | 341,300.00 USD | 128,580.00 USD | 60,930.00 USD |
| `7D` | `1.23` | 200,440,000.00 USD | 0.00 USD | 200,440,000.00 USD | 44,790.00 USD | 125,700.00 USD | 371,190.00 USD |
| `7D` | `1.23` | 199,900,000.00 USD | 0.00 USD | 199,900,000.00 USD | 257,070.00 USD | 187,490.00 USD | 353,810.00 USD |
| `1D` | `1.23` | 77,050,000.00 USD | 0.00 USD | 77,050,000.00 USD | 0.00 USD | 396.00 USD | 903.28 USD |
| `7D` | `1.23` | 199,100,000.00 USD | 0.00 USD | 199,100,000.00 USD | 702,400.00 USD | 142,840.00 USD | 467,410.00 USD |
| `1D` | `1.24` | 77,050,000.00 USD | 0.00 USD | 77,050,000.00 USD | 73,550.00 USD | 22,720.00 USD | 4,460.00 USD |
| `7D` | `1.24` | 197,780,000.00 USD | 0.00 USD | 197,780,000.00 USD | 1,150,000.00 USD | 525,690.00 USD | 2,130,000.00 USD |
| `1D` | `1.24` | 76,950,000.00 USD | 0.00 USD | 76,950,000.00 USD | 747,060.00 USD | 300,230.00 USD | 424,170.00 USD |
| `7D` | `1.24` | 193,980,000.00 USD | 0.00 USD | 193,980,000.00 USD | 1,620,000.00 USD | 912,620.00 USD | 1,860,000.00 USD |
| `1D` | `1.24` | 75,480,000.00 USD | 0.00 USD | 75,480,000.00 USD | 1,290,000.00 USD | 617,140.00 USD | 896,480.00 USD |
| `7D` | `1.24` | 189,590,000.00 USD | 0.00 USD | 189,590,000.00 USD | 1,890,000.00 USD | 930,140.00 USD | 2,250,000.00 USD |
| `1D` | `1.24` | 72,670,000.00 USD | 0.00 USD | 72,670,000.00 USD | 503,480.00 USD | 255,200.00 USD | 574,860.00 USD |
| `7D` | `1.24` | 184,510,000.00 USD | 0.00 USD | 184,510,000.00 USD | 1,980,000.00 USD | 633,060.00 USD | 2,560,000.00 USD |
| `1D` | `1.24` | 71,340,000.00 USD | 0.00 USD | 71,340,000.00 USD | 179,040.00 USD | 232,710.00 USD | 299,200.00 USD |
| `7D` | `1.24` | 179,330,000.00 USD | 0.00 USD | 179,330,000.00 USD | 982,310.00 USD | 740,000.00 USD | 1,080,000.00 USD |
| `1D` | `1.25` | 70,630,000.00 USD | 0.00 USD | 70,630,000.00 USD | 390,870.00 USD | 84,110.00 USD | 195,310.00 USD |
| `7D` | `1.25` | 176,530,000.00 USD | 0.00 USD | 176,530,000.00 USD | 2,040,000.00 USD | 376,950.00 USD | 1,810,000.00 USD |
| `1D` | `1.25` | 69,960,000.00 USD | 0.00 USD | 69,960,000.00 USD | 357,170.00 USD | 90,850.00 USD | 261,580.00 USD |
| `7D` | `1.25` | 172,300,000.00 USD | 0.00 USD | 172,300,000.00 USD | 2,120,000.00 USD | 1,190,000.00 USD | 5,300,000.00 USD |
| `1D` | `1.25` | 69,250,000.00 USD | 0.00 USD | 69,250,000.00 USD | 207,040.00 USD | 196,500.00 USD | 303,690.00 USD |
| `7D` | `1.25` | 163,690,000.00 USD | 0.00 USD | 163,690,000.00 USD | 2,280,000.00 USD | 1,370,000.00 USD | 3,470,000.00 USD |
| `1D` | `1.25` | 68,540,000.00 USD | 0.00 USD | 68,540,000.00 USD | 117,990.00 USD | 79,810.00 USD | 571,660.00 USD |
| `7D` | `1.25` | 156,560,000.00 USD | 0.00 USD | 156,560,000.00 USD | 2,810,000.00 USD | 918,840.00 USD | 2,000,000.00 USD |
| `1D` | `1.25` | 67,770,000.00 USD | 0.00 USD | 67,770,000.00 USD | 374,100.00 USD | 17,220.00 USD | 531,190.00 USD |
| `7D` | `1.25` | 150,830,000.00 USD | 0.00 USD | 150,830,000.00 USD | 1,240,000.00 USD | 673,830.00 USD | 1,480,000.00 USD |
| `1D` | `1.25` | 66,850,000.00 USD | 0.00 USD | 66,850,000.00 USD | 213,710.00 USD | 42,480.00 USD | 82,390.00 USD |
| `7D` | `1.25` | 147,430,000.00 USD | 0.00 USD | 147,430,000.00 USD | 625,270.00 USD | 563,370.00 USD | 776,740.00 USD |
| `1D` | `1.26` | 66,510,000.00 USD | 0.00 USD | 66,510,000.00 USD | 259,250.00 USD | 149,990.00 USD | 197,320.00 USD |
| `7D` | `1.26` | 145,470,000.00 USD | 0.00 USD | 145,470,000.00 USD | 370,280.00 USD | 446,010.00 USD | 344,360.00 USD |
| `1D` | `1.26` | 65,910,000.00 USD | 0.00 USD | 65,910,000.00 USD | 196,210.00 USD | 1,980.00 USD | 171,150.00 USD |
| `7D` | `1.26` | 144,310,000.00 USD | 0.00 USD | 144,310,000.00 USD | 1,190,000.00 USD | 449,360.00 USD | 890,430.00 USD |
| `1D` | `1.26` | 65,540,000.00 USD | 0.00 USD | 65,540,000.00 USD | 501,390.00 USD | 220,330.00 USD | 390,450.00 USD |
| `7D` | `1.26` | 141,780,000.00 USD | 0.00 USD | 141,780,000.00 USD | 1,470,000.00 USD | 1,130,000.00 USD | 852,870.00 USD |
| `1D` | `1.26` | 64,420,000.00 USD | 0.00 USD | 64,420,000.00 USD | 1,380,000.00 USD | 528,250.00 USD | 768,600.00 USD |
| `7D` | `1.26` | 138,330,000.00 USD | 0.00 USD | 138,330,000.00 USD | 2,860,000.00 USD | 1,720,000.00 USD | 2,030,000.00 USD |
| `1D` | `1.26` | 61,750,000.00 USD | 0.00 USD | 61,750,000.00 USD | 2,680,000.00 USD | 1,360,000.00 USD | 2,050,000.00 USD |
| `7D` | `1.26` | 131,710,000.00 USD | 0.00 USD | 131,710,000.00 USD | 3,640,000.00 USD | 1,750,000.00 USD | 4,470,000.00 USD |
| `1D` | `1.27` | 55,670,000.00 USD | 0.00 USD | 55,670,000.00 USD | 1,190,000.00 USD | 559,560.00 USD | 1,340,000.00 USD |
| `7D` | `1.27` | 121,870,000.00 USD | 0.00 USD | 121,870,000.00 USD | 3,940,000.00 USD | 1,540,000.00 USD | 6,430,000.00 USD |
| `1D` | `1.27` | 52,570,000.00 USD | 0.00 USD | 52,570,000.00 USD | 479,480.00 USD | 466,310.00 USD | 667,740.00 USD |
| `7D` | `1.27` | 109,960,000.00 USD | 0.00 USD | 109,960,000.00 USD | 1,990,000.00 USD | 1,500,000.00 USD | 2,380,000.00 USD |
| `1D` | `1.27` | 50,960,000.00 USD | 0.00 USD | 50,960,000.00 USD | 919,330.00 USD | 234,050.00 USD | 623,360.00 USD |
| `7D` | `1.27` | 104,090,000.00 USD | 0.00 USD | 104,090,000.00 USD | 3,830,000.00 USD | 1,680,000.00 USD | 4,080,000.00 USD |
| `1D` | `1.27` | 49,180,000.00 USD | 0.00 USD | 49,180,000.00 USD | 1,250,000.00 USD | 345,070.00 USD | 893,120.00 USD |
| `7D` | `1.27` | 94,500,000.00 USD | 0.00 USD | 94,500,000.00 USD | 4,300,000.00 USD | 3,000,000.00 USD | 9,250,000.00 USD |
| `1D` | `1.27` | 46,690,000.00 USD | 0.00 USD | 46,690,000.00 USD | 2,160,000.00 USD | 857,380.00 USD | 1,680,000.00 USD |
| `7D` | `1.27` | 77,940,000.00 USD | 0.00 USD | 77,940,000.00 USD | 3,980,000.00 USD | 1,300,000.00 USD | 7,240,000.00 USD |
| `1D` | `1.28` | 42,000,000.00 USD | 0.00 USD | 42,000,000.00 USD | 4,520,000.00 USD | 2,770,000.00 USD | 4,080,000.00 USD |
| `7D` | `1.28` | 65,420,000.00 USD | 0.00 USD | 65,420,000.00 USD | 6,760,000.00 USD | 2,990,000.00 USD | 8,350,000.00 USD |
| `1D` | `1.28` | 30,620,000.00 USD | 0.00 USD | 30,620,000.00 USD | 4,350,000.00 USD | 1,700,000.00 USD | 3,860,000.00 USD |
| `7D` | `1.28` | 47,320,000.00 USD | 0.00 USD | 47,320,000.00 USD | 4,830,000.00 USD | 1,750,000.00 USD | 6,220,000.00 USD |
| `1D` | `1.28` | 20,720,000.00 USD | 0.00 USD | 20,720,000.00 USD | 1,640,000.00 USD | 789,830.00 USD | 1,510,000.00 USD |
| `7D` | `1.28` | 34,520,000.00 USD | 0.00 USD | 34,520,000.00 USD | 4,610,000.00 USD | 1,440,000.00 USD | 3,850,000.00 USD |
| `1D` | `1.28` | 16,780,000.00 USD | 0.00 USD | 16,780,000.00 USD | 1,610,000.00 USD | 799,310.00 USD | 1,910,000.00 USD |
| `7D` | `1.28` | 24,630,000.00 USD | 0.00 USD | 24,630,000.00 USD | 2,970,000.00 USD | 2,130,000.00 USD | 2,480,000.00 USD |
| `1D` | `1.28` | 12,470,000.00 USD | 0.00 USD | 12,470,000.00 USD | 2,070,000.00 USD | 488,880.00 USD | 749,800.00 USD |
| `7D` | `1.28` | 17,040,000.00 USD | 0.00 USD | 17,040,000.00 USD | 3,830,000.00 USD | 1,550,000.00 USD | 4,130,000.00 USD |
| `1D` | `1.29` | 9,150,000.00 USD | 0.00 USD | 9,150,000.00 USD | 365,870.00 USD | 103,610.00 USD | 898,450.00 USD |
| `7D` | `1.29` | 7,540,000.00 USD | 0.00 USD | 7,540,000.00 USD | 724,970.00 USD | 0.00 USD | 3,030,000.00 USD |
| `1D` | `1.29` | 7,790,000.00 USD | 0.00 USD | 7,790,000.00 USD | 460,040.00 USD | 83,240.00 USD | 745,340.00 USD |
| `7D` | `1.29` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 665,270.00 USD |
| `1D` | `1.29` | 6,500,000.00 USD | 0.00 USD | 6,500,000.00 USD | 1,180,000.00 USD | 196,280.00 USD | 1,690,000.00 USD |
| `7D` | `1.29` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 1,040,000.00 USD | 0.00 USD | 819,130.00 USD |
| `1D` | `1.29` | 3,430,000.00 USD | 0.00 USD | 3,430,000.00 USD | 503,180.00 USD | 167,570.00 USD | 1,220,000.00 USD |
| `7D` | `1.29` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 0.00 USD | 213,200.00 USD | 301,640.00 USD |
| `1D` | `1.29` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 975,270.00 USD | 184,260.00 USD | 371,890.00 USD |
| `7D` | `1.29` | 747,810.00 USD | 0.00 USD | 747,810.00 USD | 440,550.00 USD | 0.00 USD | 307,250.00 USD |
| `1D` | `1.30` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.30` | 581,550.00 USD | 581,550.00 USD | 0.00 USD | 167,950.00 USD | 413,600.00 USD | 0.00 USD |
| `7D` | `1.30` | 389,370.00 USD | 389,370.00 USD | 0.00 USD | 0.00 USD | 389,370.00 USD | 0.00 USD |
| `7D` | `1.30` | 778,740.00 USD | 778,740.00 USD | 0.00 USD | 0.00 USD | 389,370.00 USD | 0.00 USD |
| `1D` | `1.30` | 668,470.00 USD | 668,470.00 USD | 0.00 USD | 0.00 USD | 86,920.00 USD | 0.00 USD |
| `1D` | `1.30` | 749,800.00 USD | 749,800.00 USD | 0.00 USD | 0.00 USD | 81,320.00 USD | 0.00 USD |
| `7D` | `1.30` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 286,660.00 USD | 0.00 USD |
| `1D` | `1.30` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 327,930.00 USD | 841,930.00 USD | 0.00 USD |
| `7D` | `1.30` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 0.00 USD | 2,340,000.00 USD | 0.00 USD |
| `1D` | `1.30` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 1,630.00 USD | 0.00 USD |
| `1D` | `1.31` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 5,650.00 USD | 0.00 USD |
| `7D` | `1.31` | 5,180,000.00 USD | 5,180,000.00 USD | 0.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.31` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 194,310.00 USD |
| `7D` | `1.31` | 5,240,000.00 USD | 5,240,000.00 USD | 0.00 USD | 62,300.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.31` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 323,900.00 USD | 743,970.00 USD | 181,760.00 USD |
| `7D` | `1.31` | 7,610,000.00 USD | 7,610,000.00 USD | 0.00 USD | 703,820.00 USD | 318,670.00 USD | 1,350,000.00 USD |
| `1D` | `1.31` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 1,280,000.00 USD | 511,150.00 USD | 682,510.00 USD |
| `7D` | `1.31` | 9,970,000.00 USD | 9,970,000.00 USD | 0.00 USD | 557,940.00 USD | 430,030.00 USD | 1,370,000.00 USD |
| `1D` | `1.31` | 8,940,000.00 USD | 8,940,000.00 USD | 0.00 USD | 267,480.00 USD | 537,730.00 USD | 2,290,000.00 USD |
| `7D` | `1.31` | 12,390,000.00 USD | 12,390,000.00 USD | 0.00 USD | 57,160.00 USD | 1,070,000.00 USD | 1,280,000.00 USD |
| `1D` | `1.32` | 15,270,000.00 USD | 15,270,000.00 USD | 0.00 USD | 1,160,000.00 USD | 1,690,000.00 USD | 3,480,000.00 USD |
| `7D` | `1.32` | 16,930,000.00 USD | 16,930,000.00 USD | 0.00 USD | 1,120,000.00 USD | 1,120,000.00 USD | 2,300,000.00 USD |
| `1D` | `1.32` | 20,660,000.00 USD | 20,660,000.00 USD | 0.00 USD | 2,060,000.00 USD | 820,760.00 USD | 2,520,000.00 USD |
| `7D` | `1.32` | 19,860,000.00 USD | 19,860,000.00 USD | 0.00 USD | 755,330.00 USD | 406,240.00 USD | 1,770,000.00 USD |
| `1D` | `1.32` | 23,790,000.00 USD | 23,790,000.00 USD | 0.00 USD | 1,450,000.00 USD | 704,780.00 USD | 970,290.00 USD |
| `7D` | `1.32` | 21,400,000.00 USD | 21,400,000.00 USD | 0.00 USD | 966,720.00 USD | 235,180.00 USD | 336,820.00 USD |
| `1D` | `1.32` | 27,750,000.00 USD | 27,750,000.00 USD | 0.00 USD | 1,660,000.00 USD | 720,740.00 USD | 1,580,000.00 USD |
| `7D` | `1.32` | 25,190,000.00 USD | 25,190,000.00 USD | 0.00 USD | 1,740,000.00 USD | 761,100.00 USD | 1,290,000.00 USD |
| `1D` | `1.32` | 29,690,000.00 USD | 29,690,000.00 USD | 0.00 USD | 1,030,000.00 USD | 287,550.00 USD | 625,660.00 USD |
| `7D` | `1.32` | 27,560,000.00 USD | 27,560,000.00 USD | 0.00 USD | 1,620,000.00 USD | 198,920.00 USD | 553,750.00 USD |
| `1D` | `1.33` | 32,180,000.00 USD | 32,180,000.00 USD | 0.00 USD | 624,130.00 USD | 621,340.00 USD | 1,240,000.00 USD |
| `7D` | `1.33` | 28,100,000.00 USD | 28,100,000.00 USD | 0.00 USD | 462,320.00 USD | 5,470.00 USD | 69,380.00 USD |
| `1D` | `1.33` | 34,420,000.00 USD | 34,420,000.00 USD | 0.00 USD | 683,490.00 USD | 159,620.00 USD | 1,400,000.00 USD |
| `7D` | `1.33` | 29,250,000.00 USD | 29,250,000.00 USD | 0.00 USD | 53,290.00 USD | 10,370.00 USD | 1,090,000.00 USD |
| `1D` | `1.33` | 37,010,000.00 USD | 37,010,000.00 USD | 0.00 USD | 748,200.00 USD | 298,240.00 USD | 1,540,000.00 USD |
| `7D` | `1.33` | 30,970,000.00 USD | 30,970,000.00 USD | 0.00 USD | 581,420.00 USD | 268,860.00 USD | 869,220.00 USD |
| `1D` | `1.33` | 38,250,000.00 USD | 38,250,000.00 USD | 0.00 USD | 713,230.00 USD | 84,950.00 USD | 440,300.00 USD |
| `7D` | `1.33` | 32,920,000.00 USD | 32,920,000.00 USD | 0.00 USD | 830,370.00 USD | 108,920.00 USD | 1,000,000.00 USD |
| `1D` | `1.33` | 39,930,000.00 USD | 39,930,000.00 USD | 0.00 USD | 717,360.00 USD | 300,370.00 USD | 665,230.00 USD |
| `7D` | `1.33` | 33,410,000.00 USD | 33,410,000.00 USD | 0.00 USD | 109,550.00 USD | 194,680.00 USD | 189,650.00 USD |
| `1D` | `1.34` | 41,960,000.00 USD | 41,960,000.00 USD | 0.00 USD | 834,660.00 USD | 219,020.00 USD | 976,490.00 USD |
| `7D` | `1.34` | 35,050,000.00 USD | 35,050,000.00 USD | 0.00 USD | 679,750.00 USD | 645,230.00 USD | 312,290.00 USD |
| `1D` | `1.34` | 45,730,000.00 USD | 45,730,000.00 USD | 0.00 USD | 1,540,000.00 USD | 373,490.00 USD | 1,860,000.00 USD |
| `7D` | `1.34` | 37,150,000.00 USD | 37,150,000.00 USD | 0.00 USD | 1,240,000.00 USD | 362,920.00 USD | 494,950.00 USD |
| `1D` | `1.34` | 49,190,000.00 USD | 49,190,000.00 USD | 0.00 USD | 1,720,000.00 USD | 804,730.00 USD | 929,730.00 USD |
| `7D` | `1.34` | 41,880,000.00 USD | 41,880,000.00 USD | 0.00 USD | 2,650,000.00 USD | 1,630,000.00 USD | 440,440.00 USD |
| `1D` | `1.34` | 53,860,000.00 USD | 53,860,000.00 USD | 0.00 USD | 2,500,000.00 USD | 765,730.00 USD | 1,410,000.00 USD |
| `7D` | `1.34` | 47,580,000.00 USD | 47,580,000.00 USD | 0.00 USD | 1,730,000.00 USD | 2,830,000.00 USD | 1,140,000.00 USD |
| `1D` | `1.34` | 57,290,000.00 USD | 57,290,000.00 USD | 0.00 USD | 1,350,000.00 USD | 692,900.00 USD | 1,380,000.00 USD |
| `7D` | `1.34` | 58,760,000.00 USD | 58,760,000.00 USD | 0.00 USD | 3,700,000.00 USD | 1,880,000.00 USD | 5,610,000.00 USD |
| `1D` | `1.35` | 58,850,000.00 USD | 58,850,000.00 USD | 0.00 USD | 753,910.00 USD | 309,200.00 USD | 502,210.00 USD |
| `7D` | `1.35` | 66,500,000.00 USD | 66,500,000.00 USD | 0.00 USD | 2,550,000.00 USD | 2,230,000.00 USD | 2,960,000.00 USD |
| `1D` | `1.35` | 61,740,000.00 USD | 61,740,000.00 USD | 0.00 USD | 1,170,000.00 USD | 384,860.00 USD | 1,330,000.00 USD |
| `7D` | `1.35` | 76,870,000.00 USD | 76,870,000.00 USD | 0.00 USD | 4,290,000.00 USD | 1,760,000.00 USD | 4,320,000.00 USD |
| `1D` | `1.35` | 62,810,000.00 USD | 62,810,000.00 USD | 0.00 USD | 489,370.00 USD | 130,090.00 USD | 452,540.00 USD |
| `7D` | `1.35` | 84,650,000.00 USD | 84,650,000.00 USD | 0.00 USD | 2,580,000.00 USD | 1,440,000.00 USD | 3,750,000.00 USD |
| `1D` | `1.35` | 65,140,000.00 USD | 65,140,000.00 USD | 0.00 USD | 879,540.00 USD | 405,430.00 USD | 1,040,000.00 USD |
| `7D` | `1.35` | 92,970,000.00 USD | 92,970,000.00 USD | 0.00 USD | 2,620,000.00 USD | 1,230,000.00 USD | 4,480,000.00 USD |
| `1D` | `1.35` | 67,520,000.00 USD | 67,520,000.00 USD | 0.00 USD | 857,510.00 USD | 297,760.00 USD | 1,220,000.00 USD |
| `7D` | `1.35` | 101,200,000.00 USD | 101,200,000.00 USD | 0.00 USD | 3,780,000.00 USD | 873,380.00 USD | 3,580,000.00 USD |
| `1D` | `1.36` | 69,640,000.00 USD | 69,640,000.00 USD | 0.00 USD | 1,120,000.00 USD | 102,980.00 USD | 901,760.00 USD |
| `7D` | `1.36` | 105,280,000.00 USD | 105,280,000.00 USD | 0.00 USD | 1,320,000.00 USD | 881,730.00 USD | 1,870,000.00 USD |
| `1D` | `1.36` | 70,460,000.00 USD | 70,460,000.00 USD | 0.00 USD | 504,090.00 USD | 150,540.00 USD | 163,660.00 USD |
| `7D` | `1.36` | 109,180,000.00 USD | 109,180,000.00 USD | 0.00 USD | 1,490,000.00 USD | 729,940.00 USD | 1,680,000.00 USD |
| `1D` | `1.36` | 71,250,000.00 USD | 71,250,000.00 USD | 0.00 USD | 374,230.00 USD | 183,190.00 USD | 237,270.00 USD |
| `7D` | `1.36` | 111,690,000.00 USD | 111,690,000.00 USD | 0.00 USD | 671,910.00 USD | 581,640.00 USD | 1,250,000.00 USD |
| `1D` | `1.36` | 72,360,000.00 USD | 72,360,000.00 USD | 0.00 USD | 454,700.00 USD | 103,540.00 USD | 547,500.00 USD |
| `7D` | `1.36` | 116,080,000.00 USD | 116,080,000.00 USD | 0.00 USD | 2,100,000.00 USD | 918,100.00 USD | 1,380,000.00 USD |
| `1D` | `1.36` | 72,450,000.00 USD | 72,450,000.00 USD | 0.00 USD | 16,020.00 USD | 28,030.00 USD | 46,170.00 USD |
| `7D` | `1.36` | 117,990,000.00 USD | 117,990,000.00 USD | 0.00 USD | 664,020.00 USD | 328,930.00 USD | 923,440.00 USD |
| `1D` | `1.37` | 72,830,000.00 USD | 72,830,000.00 USD | 0.00 USD | 126,080.00 USD | 85,100.00 USD | 170,030.00 USD |
| `7D` | `1.37` | 118,490,000.00 USD | 118,490,000.00 USD | 0.00 USD | 239,150.00 USD | 216,290.00 USD | 40,350.00 USD |
| `1D` | `1.37` | 73,270,000.00 USD | 73,270,000.00 USD | 0.00 USD | 172,840.00 USD | 18,750.00 USD | 251,320.00 USD |
| `7D` | `1.37` | 120,280,000.00 USD | 120,280,000.00 USD | 0.00 USD | 547,200.00 USD | 138,950.00 USD | 1,100,000.00 USD |
| `1D` | `1.37` | 73,750,000.00 USD | 73,750,000.00 USD | 0.00 USD | 100,350.00 USD | 120,860.00 USD | 258,200.00 USD |
| `7D` | `1.37` | 121,680,000.00 USD | 121,680,000.00 USD | 0.00 USD | 465,040.00 USD | 398,870.00 USD | 543,240.00 USD |
| `1D` | `1.37` | 74,180,000.00 USD | 74,180,000.00 USD | 0.00 USD | 186,780.00 USD | 49,160.00 USD | 193,840.00 USD |
| `7D` | `1.37` | 124,540,000.00 USD | 124,540,000.00 USD | 0.00 USD | 931,390.00 USD | 404,120.00 USD | 1,520,000.00 USD |
| `1D` | `1.38` | 74,370,000.00 USD | 74,370,000.00 USD | 0.00 USD | 121,400.00 USD | 884.30 USD | 69,340.00 USD |
| `7D` | `1.38` | 126,230,000.00 USD | 126,230,000.00 USD | 0.00 USD | 594,550.00 USD | 326,340.00 USD | 769,660.00 USD |
| `1D` | `1.38` | 74,810,000.00 USD | 74,810,000.00 USD | 0.00 USD | 137,580.00 USD | 65,830.00 USD | 232,740.00 USD |
| `7D` | `1.38` | 127,850,000.00 USD | 127,850,000.00 USD | 0.00 USD | 676,760.00 USD | 389,310.00 USD | 552,000.00 USD |
| `1D` | `1.38` | 75,590,000.00 USD | 75,590,000.00 USD | 0.00 USD | 336,250.00 USD | 76,440.00 USD | 369,950.00 USD |
| `7D` | `1.38` | 129,790,000.00 USD | 129,790,000.00 USD | 0.00 USD | 579,450.00 USD | 290,350.00 USD | 1,070,000.00 USD |
| `1D` | `1.38` | 76,200,000.00 USD | 76,200,000.00 USD | 0.00 USD | 331,700.00 USD | 108,980.00 USD | 163,240.00 USD |
| `7D` | `1.38` | 132,330,000.00 USD | 132,330,000.00 USD | 0.00 USD | 1,210,000.00 USD | 330,740.00 USD | 1,000,000.00 USD |
| `1D` | `1.38` | 76,800,000.00 USD | 76,800,000.00 USD | 0.00 USD | 371,970.00 USD | 42,880.00 USD | 185,280.00 USD |
| `7D` | `1.38` | 133,420,000.00 USD | 133,420,000.00 USD | 0.00 USD | 297,210.00 USD | 312,330.00 USD | 477,040.00 USD |
| `1D` | `1.39` | 77,040,000.00 USD | 77,040,000.00 USD | 0.00 USD | 145,190.00 USD | 54,030.00 USD | 40,640.00 USD |
| `7D` | `1.39` | 134,520,000.00 USD | 134,520,000.00 USD | 0.00 USD | 505,510.00 USD | 190,450.00 USD | 401,920.00 USD |
| `1D` | `1.39` | 77,130,000.00 USD | 77,130,000.00 USD | 0.00 USD | 57,490.00 USD | 16,600.00 USD | 19,970.00 USD |
| `7D` | `1.39` | 135,010,000.00 USD | 135,010,000.00 USD | 0.00 USD | 86,820.00 USD | 203,870.00 USD | 200,360.00 USD |
| `1D` | `1.39` | 77,510,000.00 USD | 77,510,000.00 USD | 0.00 USD | 140,810.00 USD | 51,770.00 USD | 189,590.00 USD |
| `7D` | `1.39` | 136,100,000.00 USD | 136,100,000.00 USD | 0.00 USD | 690,420.00 USD | 162,590.00 USD | 238,810.00 USD |
| `7D` | `1.39` | 136,260,000.00 USD | 136,260,000.00 USD | 0.00 USD | 118,760.00 USD | 39,430.00 USD | 0.00 USD |
| `7D` | `1.39` | 136,580,000.00 USD | 136,580,000.00 USD | 0.00 USD | 82,350.00 USD | 36,390.00 USD | 208,520.00 USD |
| `1D` | `1.40` | 77,530,000.00 USD | 77,530,000.00 USD | 0.00 USD | 7,190.00 USD | 14,010.00 USD | 2,040.00 USD |
| `7D` | `1.40` | 136,730,000.00 USD | 136,730,000.00 USD | 0.00 USD | 121,260.00 USD | 22,660.00 USD | 0.00 USD |
| `1D` | `1.40` | 77,630,000.00 USD | 77,630,000.00 USD | 0.00 USD | 19,030.00 USD | 0.00 USD | 80,320.00 USD |
| `7D` | `1.40` | 136,740,000.00 USD | 136,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16,250.00 USD |
| `7D` | `1.40` | 136,750,000.00 USD | 136,750,000.00 USD | 0.00 USD | 0.00 USD | 996.88 USD | 5,880.00 USD |
| `7D` | `1.40` | 136,890,000.00 USD | 136,890,000.00 USD | 0.00 USD | 0.00 USD | 75,720.00 USD | 60,830.00 USD |
| `7D` | `1.40` | 137,010,000.00 USD | 137,010,000.00 USD | 0.00 USD | 94,530.00 USD | 21,520.00 USD | 1,960.00 USD |
| `7D` | `1.41` | 137,250,000.00 USD | 137,250,000.00 USD | 0.00 USD | 178,210.00 USD | 25,430.00 USD | 38,070.00 USD |
| `7D` | `1.41` | 137,410,000.00 USD | 137,410,000.00 USD | 0.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD |
| `7D` | `1.41` | 137,580,000.00 USD | 137,580,000.00 USD | 0.00 USD | 12,250.00 USD | 37,300.00 USD | 120,130.00 USD |
| `7D` | `1.41` | 137,740,000.00 USD | 137,740,000.00 USD | 0.00 USD | 88,530.00 USD | 57,460.00 USD | 7,070.00 USD |
| `1D` | `1.41` | 77,630,000.00 USD | 77,630,000.00 USD | 0.00 USD | 0.00 USD | 158.40 USD | 0.00 USD |
| `7D` | `1.41` | 137,910,000.00 USD | 137,910,000.00 USD | 0.00 USD | 11,290.00 USD | 26,480.00 USD | 132,120.00 USD |
| `1D` | `1.42` | 77,670,000.00 USD | 77,670,000.00 USD | 0.00 USD | 29,120.00 USD | 9,090.00 USD | 1,040.00 USD |
| `7D` | `1.42` | 138,410,000.00 USD | 138,410,000.00 USD | 0.00 USD | 161,890.00 USD | 72,870.00 USD | 264,400.00 USD |
| `1D` | `1.42` | 77,890,000.00 USD | 77,890,000.00 USD | 0.00 USD | 115,890.00 USD | 26,520.00 USD | 70,810.00 USD |
| `7D` | `1.42` | 138,830,000.00 USD | 138,830,000.00 USD | 0.00 USD | 171,750.00 USD | 52,740.00 USD | 204,770.00 USD |
| `1D` | `1.42` | 78,480,000.00 USD | 78,480,000.00 USD | 0.00 USD | 269,920.00 USD | 170,450.00 USD | 151,900.00 USD |
| `7D` | `1.42` | 139,860,000.00 USD | 139,860,000.00 USD | 0.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD |
| `1D` | `1.42` | 79,070,000.00 USD | 79,070,000.00 USD | 0.00 USD | 292,830.00 USD | 105,740.00 USD | 193,830.00 USD |
| `7D` | `1.42` | 141,230,000.00 USD | 141,230,000.00 USD | 0.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD |
| `1D` | `1.42` | 79,290,000.00 USD | 79,290,000.00 USD | 0.00 USD | 63,800.00 USD | 59,830.00 USD | 91,270.00 USD |
| `7D` | `1.42` | 141,860,000.00 USD | 141,860,000.00 USD | 0.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD |
| `1D` | `1.43` | 79,380,000.00 USD | 79,380,000.00 USD | 0.00 USD | 31,260.00 USD | 27,740.00 USD | 34,760.00 USD |
| `7D` | `1.43` | 142,210,000.00 USD | 142,210,000.00 USD | 0.00 USD | 87,470.00 USD | 69,800.00 USD | 196,840.00 USD |
| `1D` | `1.43` | 79,540,000.00 USD | 79,540,000.00 USD | 0.00 USD | 121,180.00 USD | 11,130.00 USD | 25,490.00 USD |
| `7D` | `1.43` | 143,180,000.00 USD | 143,180,000.00 USD | 0.00 USD | 318,950.00 USD | 62,300.00 USD | 588,430.00 USD |
| `1D` | `1.43` | 79,700,000.00 USD | 79,700,000.00 USD | 0.00 USD | 86,630.00 USD | 31,280.00 USD | 43,000.00 USD |
| `7D` | `1.43` | 144,690,000.00 USD | 144,690,000.00 USD | 0.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD |
| `1D` | `1.43` | 79,870,000.00 USD | 79,870,000.00 USD | 0.00 USD | 27,580.00 USD | 49,790.00 USD | 94,780.00 USD |
| `7D` | `1.43` | 146,080,000.00 USD | 146,080,000.00 USD | 0.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD |
| `1D` | `1.43` | 80,130,000.00 USD | 80,130,000.00 USD | 0.00 USD | 32,280.00 USD | 26,620.00 USD | 195,860.00 USD |
| `7D` | `1.43` | 146,880,000.00 USD | 146,880,000.00 USD | 0.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD |
| `1D` | `1.44` | 80,300,000.00 USD | 80,300,000.00 USD | 0.00 USD | 102,020.00 USD | 0.00 USD | 76,770.00 USD |
| `7D` | `1.44` | 147,410,000.00 USD | 147,410,000.00 USD | 0.00 USD | 215,800.00 USD | 23,880.00 USD | 290,120.00 USD |
| `1D` | `1.44` | 80,470,000.00 USD | 80,470,000.00 USD | 0.00 USD | 39,530.00 USD | 16,760.00 USD | 106,100.00 USD |
| `7D` | `1.44` | 147,780,000.00 USD | 147,780,000.00 USD | 0.00 USD | 74,670.00 USD | 83,260.00 USD | 215,310.00 USD |
| `1D` | `1.44` | 80,590,000.00 USD | 80,590,000.00 USD | 0.00 USD | 80,830.00 USD | 13,900.00 USD | 30,960.00 USD |
| `7D` | `1.44` | 148,280,000.00 USD | 148,280,000.00 USD | 0.00 USD | 154,760.00 USD | 93,720.00 USD | 245,840.00 USD |
| `1D` | `1.44` | 80,760,000.00 USD | 80,760,000.00 USD | 0.00 USD | 77,850.00 USD | 41,360.00 USD | 49,320.00 USD |
| `7D` | `1.44` | 149,170,000.00 USD | 149,170,000.00 USD | 0.00 USD | 299,590.00 USD | 131,210.00 USD | 459,970.00 USD |
| `1D` | `1.44` | 80,790,000.00 USD | 80,790,000.00 USD | 0.00 USD | 19,950.00 USD | 11,210.00 USD | 2,560.00 USD |
| `7D` | `1.44` | 149,670,000.00 USD | 149,670,000.00 USD | 0.00 USD | 69,670.00 USD | 152,290.00 USD | 286,090.00 USD |
| `1D` | `1.45` | 80,920,000.00 USD | 80,920,000.00 USD | 0.00 USD | 37,820.00 USD | 22,830.00 USD | 66,040.00 USD |
| `7D` | `1.45` | 149,810,000.00 USD | 149,810,000.00 USD | 0.00 USD | 67,200.00 USD | 53,830.00 USD | 12,180.00 USD |
| `1D` | `1.45` | 80,960,000.00 USD | 80,960,000.00 USD | 0.00 USD | 35,430.00 USD | 247.55 USD | 1,470.00 USD |
| `7D` | `1.45` | 149,940,000.00 USD | 149,940,000.00 USD | 0.00 USD | 11,070.00 USD | 2,120.00 USD | 116,410.00 USD |
| `1D` | `1.45` | 81,030,000.00 USD | 81,030,000.00 USD | 0.00 USD | 20,940.00 USD | 20,510.00 USD | 26,770.00 USD |
| `7D` | `1.45` | 150,420,000.00 USD | 150,420,000.00 USD | 0.00 USD | 70,540.00 USD | 96,050.00 USD | 311,630.00 USD |
| `1D` | `1.45` | 81,210,000.00 USD | 81,210,000.00 USD | 0.00 USD | 42,480.00 USD | 37,580.00 USD | 102,510.00 USD |
| `7D` | `1.45` | 151,010,000.00 USD | 151,010,000.00 USD | 0.00 USD | 190,550.00 USD | 38,510.00 USD | 370,320.00 USD |
| `1D` | `1.45` | 81,250,000.00 USD | 81,250,000.00 USD | 0.00 USD | 28,580.00 USD | 4,170.00 USD | 12,650.00 USD |
| `7D` | `1.45` | 151,640,000.00 USD | 151,640,000.00 USD | 0.00 USD | 161,500.00 USD | 127,370.00 USD | 338,310.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `3.01B` | Total OI Tokens: `2,324,000,761.8 XRP`
  * 1h OI Change: `-0.95%` | 4h OI Change: `-0.26%` | 24h OI Change: `+2.39%`
  * Exchange Breakdown: Binance=`498.91M` | Bybit=`329.98M` | OKX=`103.09M` | Hyperliquid=`227.13M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `82.51K` | Last 24h: `142.09K` | Last 3d: `599.05K` | Last 7d: `1.15M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0041%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `XRP` | `42.89%` | `57.11%` | `0.75` | 641,890,000.00 USD |
| `15M` | `Binance` | `37.98%` | `62.02%` | `0.61` | 252,730,000.00 USD |
| `15M` | `OKX` | `48.76%` | `51.24%` | `0.95` | 76,540,000.00 USD |
| `15M` | `Bybit` | `36.97%` | `63.03%` | `0.59` | 59,290,000.00 USD |
| `15M` | `KuCoin` | `45.08%` | `54.92%` | `0.82` | 1,740,000.00 USD |
| `15M` | `Gate` | `45.27%` | `54.73%` | `0.83` | 67,240,000.00 USD |
| `15M` | `Bitget` | `45.78%` | `54.22%` | `0.84` | 28,760,000.00 USD |
| `15M` | `BingX` | `51.74%` | `48.26%` | `1.07` | 8,500,000.00 USD |
| `15M` | `MEXC` | `45.24%` | `54.76%` | `0.83` | 30,850,000.00 USD |
| `15M` | `Bitunix` | `51.28%` | `48.72%` | `1.05` | 25,930,000.00 USD |
| `15M` | `Hyperliquid` | `48.25%` | `51.75%` | `0.93` | 22,030,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `81.28%` | `18.72%` | `4.34` | 6,300,000.00 USD |
| `15M` | `Crypto.com` | `45.67%` | `54.33%` | `0.84` | 6,650,000.00 USD |
| `15M` | `WhiteBIT` | `51.23%` | `48.77%` | `1.05` | 17,600,000.00 USD |
| `15M` | `HTX` | `40.04%` | `59.96%` | `0.67` | 2,350,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `48.3%` | `51.7%` | `0.93` | 10,990,000.00 USD |
| `15M` | `Bitfinex` | `35.76%` | `64.24%` | `0.56` | 345,040.00 USD |
| `15M` | `Kraken` | `70.1%` | `29.9%` | `2.34` | 2,720,000.00 USD |
| `15M` | `Aster` | `26.67%` | `73.33%` | `0.36` | 9,870,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `46.33%` | `53.67%` | `0.86` | 11,460,000.00 USD |
| `15M` | `Whale Positions` | `37.98%` | `62.02%` | `0.61` | 252,730,000.00 USD |
| `15M` | `Global Accounts` | `42.89%` | `57.11%` | `0.75` | 641,890,000.00 USD |
| `1H` | `XRP` | `43.09%` | `56.91%` | `0.76` | 2,560,000,000.00 USD |
| `1H` | `Binance` | `42.43%` | `57.57%` | `0.74` | 752,800,000.00 USD |
| `1H` | `OKX` | `46.01%` | `53.99%` | `0.85` | 443,930,000.00 USD |
| `1H` | `Bybit` | `40.32%` | `59.68%` | `0.68` | 195,570,000.00 USD |
| `1H` | `KuCoin` | `48.41%` | `51.59%` | `0.94` | 6,630,000.00 USD |
| `1H` | `Gate` | `49.48%` | `50.52%` | `0.98` | 387,750,000.00 USD |
| `1H` | `Bitget` | `51.56%` | `48.44%` | `1.06` | 138,000,000.00 USD |
| `1H` | `BingX` | `40.6%` | `59.4%` | `0.68` | 39,430,000.00 USD |
| `1H` | `MEXC` | `51.37%` | `48.63%` | `1.06` | 93,360,000.00 USD |
| `1H` | `Bitunix` | `44.1%` | `55.9%` | `0.79` | 90,990,000.00 USD |
| `1H` | `Hyperliquid` | `28.18%` | `71.82%` | `0.39` | 52,190,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `40.75%` | `59.25%` | `0.69` | 6,130,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `21.81%` | `78.19%` | `0.28` | 234,840,000.00 USD |
| `1H` | `HTX` | `54.85%` | `45.15%` | `1.21` | 30,570,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `51.17%` | `48.83%` | `1.05` | 5,300,000.00 USD |
| `1H` | `Bitfinex` | `39.93%` | `60.07%` | `0.66` | 962,000.00 USD |
| `1H` | `Kraken` | `67.71%` | `32.29%` | `2.10` | 17,520,000.00 USD |
| `1H` | `Aster` | `42.7%` | `57.3%` | `0.75` | 26,720,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `50.56%` | `49.44%` | `1.02` | 34,850,000.00 USD |
| `1H` | `Whale Positions` | `42.43%` | `57.57%` | `0.74` | 752,800,000.00 USD |
| `1H` | `Global Accounts` | `43.09%` | `56.91%` | `0.76` | 2,560,000,000.00 USD |
| `4H` | `XRP` | `49.17%` | `50.83%` | `0.97` | 11,730,000,000.00 USD |
| `4H` | `Binance` | `50.47%` | `49.53%` | `1.02` | 3,560,000,000.00 USD |
| `4H` | `OKX` | `51.16%` | `48.84%` | `1.05` | 2,260,000,000.00 USD |
| `4H` | `Bybit` | `52.03%` | `47.97%` | `1.08` | 874,990,000.00 USD |
| `4H` | `KuCoin` | `64.37%` | `35.63%` | `1.81` | 40,710,000.00 USD |
| `4H` | `Gate` | `50.54%` | `49.46%` | `1.02` | 1,890,000,000.00 USD |
| `4H` | `Bitget` | `49.72%` | `50.28%` | `0.99` | 592,640,000.00 USD |
| `4H` | `BingX` | `46%` | `54%` | `0.85` | 181,010,000.00 USD |
| `4H` | `MEXC` | `50.38%` | `49.62%` | `1.02` | 468,220,000.00 USD |
| `4H` | `Bitunix` | `48.52%` | `51.48%` | `0.94` | 435,790,000.00 USD |
| `4H` | `Hyperliquid` | `42.84%` | `57.16%` | `0.75` | 320,140,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.72%` | `51.28%` | `0.95` | 47,800,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `18.53%` | `81.47%` | `0.23` | 537,260,000.00 USD |
| `4H` | `HTX` | `68.65%` | `31.35%` | `2.19` | 182,910,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `47.25%` | `52.75%` | `0.90` | 42,690,000.00 USD |
| `4H` | `Bitfinex` | `43.53%` | `56.47%` | `0.77` | 2,800,000.00 USD |
| `4H` | `Kraken` | `65.97%` | `34.03%` | `1.94` | 55,480,000.00 USD |
| `4H` | `Aster` | `43.8%` | `56.2%` | `0.78` | 99,770,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `47.09%` | `52.91%` | `0.89` | 129,280,000.00 USD |
| `4H` | `Whale Positions` | `50.47%` | `49.53%` | `1.02` | 3,560,000,000.00 USD |
| `4H` | `Global Accounts` | `49.17%` | `50.83%` | `0.97` | 11,730,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `1.31` | `1.30` | `1.31` | `1.31` | `1.30` | 10,431,153.03 USD | 4,511,706.21 USD | 5,919,446.82 USD | -1,407,740.61 USD | `-13.50%` | `9B / 12S` |
| `0:00 UTC` | `1.31` | `1.31` | `1.31` | `1.31` | `1.30` | 11,542,627.64 USD | 6,670,849.58 USD | 4,871,778.06 USD | 1,799,071.52 USD | `+15.59%` | `29B / 7S` |
| `5:00 UTC` | `1.31` | `1.31` | `1.31` | `1.31` | `1.30` | 9,428,108.38 USD | 3,943,451.38 USD | 5,484,657.00 USD | -1,541,205.63 USD | `-16.35%` | `8B / 24S` |
| `0:00 UTC` | `1.30` | `1.31` | `1.30` | `1.31` | `1.30` | 9,077,727.01 USD | 4,773,597.25 USD | 4,304,129.76 USD | 469,467.49 USD | `+5.17%` | `10B / 12S` |
| `5:00 UTC` | `1.31` | `1.31` | `1.31` | `1.31` | `1.31` | 9,791,336.03 USD | 4,585,305.80 USD | 5,206,030.23 USD | -620,724.44 USD | `-6.34%` | `2B / 6S` |
| `0:00 UTC` | `1.31` | `1.31` | `1.31` | `1.32` | `1.31` | 13,794,897.02 USD | 7,005,423.08 USD | 6,789,473.94 USD | 215,949.13 USD | `+1.57%` | `17B / 16S` |
| `5:00 UTC` | `1.30` | `1.31` | `1.30` | `1.31` | `1.30` | 11,087,990.94 USD | 4,090,249.58 USD | 6,997,741.36 USD | -2,907,491.79 USD | `-26.22%` | `5B / 28S` |
| `0:00 UTC` | `1.30` | `1.30` | `1.30` | `1.30` | `1.30` | 10,205,311.65 USD | 4,505,902.50 USD | 5,699,409.15 USD | -1,193,506.66 USD | `-11.69%` | `6B / 11S` |
| `5:00 UTC` | `1.30` | `1.30` | `1.30` | `1.30` | `1.30` | 4,776,328.08 USD | 2,498,208.46 USD | 2,278,119.62 USD | 220,088.84 USD | `+4.61%` | `7B / 8S` |
| `0:00 UTC` | `1.30` | `1.30` | `1.30` | `1.30` | `1.30` | 6,337,189.07 USD | 2,493,909.60 USD | 3,843,279.47 USD | -1,349,369.87 USD | `-21.29%` | `2B / 17S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 19:52` | `Range 0.005` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `1.31` | 0.00 USD | 0.00 USD |
| `10-28 19:07` | `Volume 10M XRP` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `1.32` | 2,000,000.00 USD | 0.00 USD |
| `10-28 19:07` | `Volume 10M XRP` | `Trapped longs` | **`BEARISH`** | Failed breakout | `1.32` | 2,000,000.00 USD | 0.00 USD |
| `10-28 18:52` | `Volume 10M XRP` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `1.31` | 1,200,000.00 USD | 0.00 USD |
| `10-28 17:43` | `Volume 10M XRP` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `1.31` | 3,000,000.00 USD | 0.00 USD |
| `10-28 12:56` | `Range 0.005` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `1.32` | 0.00 USD | 0.00 USD |
| `10-28 10:21` | `Volume 10M XRP` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `1.33` | 3,600,000.00 USD | 0.00 USD |
| `10-28 08:33` | `Volume 10M XRP` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `1.33` | 2,100,000.00 USD | 0.00 USD |
| `10-28 08:12` | `Range 0.005` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `1.33` | 3,700,000.00 USD | 0.00 USD |
| `10-28 07:47` | `Volume 10M XRP` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `1.34` | 0.00 USD | 0.00 USD |
| `10-28 07:47` | `Range 0.005` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `1.34` | 0.00 USD | 0.00 USD |
| `10-28 07:20` | `Volume 10M XRP` | `Divergence` | **`BULLISH`** | Drop without taker selling | `1.33` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 167,160.00 USD | 640,250.00 USD | **`ACCUMULATION`** |
| `15m` | -731,400.00 USD | -2,390,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -1,480,000.00 USD | -3,690,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -3,300,000.00 USD | -9,020,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -1,840,000.00 USD | -13,310,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 1,290,000.00 USD | -5,500,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -465,510.00 USD | -6,080,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -646,500.00 USD | -941,860.00 USD | **`DISTRIBUTION`** |
| `12h` | -757,600.00 USD | -13,770,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -13,900,000.00 USD | -46,170,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -72,860,000.00 USD | -83,580,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -551,100,000.00 USD | -1,170,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+167.16K` | 15m=`-731.40K` | 1h=`-3.30M` | 24h=`-13.90M`
* Futures Capital Netflows: 5m=`+640.25K` | 15m=`-2.39M` | 1h=`-9.02M` | 24h=`-46.17M`
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
  * `2026-10-29 22:05:54 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:38:54 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:38:54 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 22:38:54 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 18:40:54 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 18:40:54 IST`: [dol.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 18:40:54 IST`: [bea.gov] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1.28` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1.27` (Risk Distance: `0.0125` pts)
  * +2.5R Take Profit: `1.32`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1.30` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.31` (Risk Distance: `0.0125` pts)
  * +2.5R Take Profit: `1.27`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.31`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
