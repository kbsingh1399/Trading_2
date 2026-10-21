# 🏛️ INSTITUTIONAL TRADING DESK: AUTONOMOUS CANDIDATE SCAN & SYNTHESIS (CYCLE 202)

> **Repository Sync Notice**: `origin/main` has been updated with the canonical 29-sheet Excel data warehouse (`Data/DataBase_Trading.xlsx`, 13.2 MB) and the authoritative specification [`docs/specs/STANDARDIZED_TRADING_DECISION_CHAIN.md`](https://github.com/kbsingh1399/Trading_2/blob/main/docs/specs/STANDARDIZED_TRADING_DECISION_CHAIN.md). Pull the latest `main` branch to inspect fresh market intelligence.

---

### 1. LIVE MT5 ACCOUNT STATE & ACTIVE POSITION INVENTORY
- **Broker / Environment**: MetaTrader 5 | Blueberry Markets | Account #5064568 (USD)
- **Account Balance & Equity**: **Balance: 4,824.89 USD | Equity: 4,832.77 USD**
- **Capital Defense Gates**: Hard Floor: **4,775.00 USD** | Operating Defense Buffer: **4,795.00 USD**
- **Live Floor Cushion**: **+57.77 USD** (Hard Floor) / **+37.77 USD** (Operating Buffer)
- **Active Open Positions**: **1**
  - **Ticket**: `19146275`
  - **Instrument**: `NAS100.p` (Nasdaq 100 CFD | Blueberry MT5 Spread: 0.36 bps / 1.06 pts)
  - **Direction**: `BUY` (Volume: `0.01 lot` | 1 pt = 0.10 USD)
  - **Entry Fill**: `29,560.00 USD` (Filled at 200 EMA support shelf)
  - **Current Market**: `29,638.75 USD` (Floating Gain: **+78.75 pts / +0.53R0** | Floating Profit: **+7.88 USD**)
  - **Stop Loss**: `29,410.00 USD` (150 pts structural bunker | Cash Risk: $15.00 USD)
  - **Take Profit**: `29,715.00 USD` (Front-running Daily VWAP 29,718.84 USD by 3.8 pts)
  - **Ratchet Trigger**: Early-BE trigger at 29,672.50 USD (+0.75R0) moves SL to 29,575.00 USD (+0.10R0 lock)
  - **Stressed Post-Loss Cushion**: Equity post-loss = 4,812.02 USD (+37.02 USD above hard floor, +17.02 USD above operating buffer)

---

### 2. MANDATORY WAKE-UP INSTRUCTIONS & DATA INGESTION PROTOCOL
As codified in `docs/specs/STANDARDIZED_TRADING_DECISION_CHAIN.md`:
1. **Mandatory 29-Sheet Reading Mandate**: You are strictly required to read `Data/DataBase_Trading.xlsx` across all 29 worksheets terminating at `19_Calendar`:
   - **Cluster A (Macro & Institutional Flows)**: `Crypto_ETF_Flows` & `1_Crypto_ETF_Flows` (+29.9M USD into IBIT), `2_Spot_Netflow_S` (500 assets), `19_News`, and `19_Calendar` (Zero active blackouts; FOMC Oct 28 distal).
   - **Cluster B (Derivatives Positioning & Technicals)**: `3_Exchanges_LS_Ratio_*`, `5_OI`, `5_Funding_Rate`, `6_Funding_Fee_Settlement`, `11_Technical` (Full 43-column matrix), `12_Hyperdash`, `13_Hyperliquid`.
   - **Cluster C (Liquidations & CVD Delta)**: `7_Liq_Heapmap`, `7_Live_Liq`, `8_Exchange_Liquidation_Map_1D/7D`, `9_Liquidation_Max_Pain_*`, `14_Hyperdash_Liq_Map` (5,700+ rows), `15_Hyperdash_Stops_Map` (3,800+ rows), and `18_CVD` (50,001 rows multi-TF delta).
   - **Cluster D (Whale Walls & L2/L3 Depth)**: `4_Hyperliquid_Analysis` (2,001 whale wallets), `10_Whale_Orders` (7.45M USD BTC overhead sell resistance at 83,688-83,700 USD), `16_Hyperdash_telegram_Intel`, `17_Orderbook`, and live MT5 telemetry.

2. **Spread Friction Gate Verification**:
   - Crypto Perpetuals: MT5 Spread must be <= 25.0 bps (Qualified: BTC 1.80 bps, BNB 8.05 bps, ETH 11.40 bps, BCH 20.21 bps, TRX 21.16 bps, SOL 22.52 bps).
   - TradFi CFDs: MT5 Spread must be <= 5.0 bps (Qualified: EURUSD 0.09 bps, GOLD 0.19 bps, DJ30 0.22 bps, NAS100 0.36 bps, SP500 0.39 bps).

---

### 3. YOUR MANDATE THIS TURN
1. **Audit & Ratify Filled Position `19146275` (`NAS100.p`)**: Evaluate the current +0.53R0 gain and verify the Early-BE ratchet trigger (+0.75R0 at 29,672.50 USD).
2. **Scan for Secondary Candidate**:
   - Evaluate `SP500.p` (Model 1 Extreme Mean Reversion: VWAP Z = -2.31 SD, RSI = 39.74, Spread = 0.39 bps).
   - Evaluate `BTCUSD.pi` (Model 2 Trend Pullback to Daily VWAP 82,919.63 USD support shelf).
3. **Format Your Decision**:
   - Provide your quantitative thesis, explicit asset metrics, and clear directive: RATIFY ACTIVE POSITION / STAGE SECONDARY CANDIDATE / STAND ASIDE.
