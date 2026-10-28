# 🏛️ TRI-COUNCIL QUANT COMMISSION: INDEPENDENT CANDIDATE DISCOVERY & SOVEREIGN SYNTHESIS (CYCLE 375)

> **TARGET PLATFORMS**: Arena.ai (GPT_Astra / Fable 5) & Z.ai (GLM-5.3-Flash / Claude 3.7 Sonnet)  
> **DISPATCH TIMESTAMP**: 2026-10-28 19:10:00 UTC (2026-10-29 00:40:00 IST)  
> **CANONICAL DATA REPOSITORY**: `https://github.com/kbsingh1399/Trading_2` (branch `main`)  
> **CANONICAL ENVELOPE**: `Data/cycle_envelope.json` | `docs/telemetry/live_snapshot_latest.json`  

---

## 🎯 OPERATOR DIRECTIVE: INDEPENDENT DISCOVERY & MANDATORY GOVERNANCE COMPLIANCE
The desk operator has issued an authoritative directive:
1. **Mandatory Governance Document Read & Compliance Gate**:
   Both Arena.ai and Z.ai MUST physically read, study, and strictly comply with all 5 canonical governance documents on GitHub:
   - 📑 **`STANDARDIZED_TRADING_DECISION_CHAIN.md`**: https://github.com/kbsingh1399/Trading_2/blob/main/Data/Manditory/STANDARDIZED_TRADING_DECISION_CHAIN.md  
     *(Section 1.5 Dynamic Capacity Policy N_open + N_pending <= 1, Section 2.1 In-Memory Pre-Load, Section 3 Five Confluence Pillars)*
   - 🛡️ **`TOP_10_TRADE_EXECUTION_PITFALLS_AND_AUTOPSY.md`**: https://github.com/kbsingh1399/Trading_2/blob/main/Data/Manditory/TOP_10_TRADE_EXECUTION_PITFALLS_AND_AUTOPSY.md  
     *(Audit all 10 lethal traps: ghost whale walls > 180s, zero staging above stop cascades, zero unabsorbed CVD waterfalls, zero sub-ATR stops, zero random-walk fades, spread <= 5 bps TradFi / <= 25 bps Crypto, rollover blackout 21:15-22:30 UTC, zero cluster double-bets, solvency floor defense)*
   - 📊 **`32_SHEET_REAL_WORLD_PITFALL_AVOIDANCE_QUESTIONS.md`**: https://github.com/kbsingh1399/Trading_2/blob/main/Data/Manditory/32_SHEET_REAL_WORLD_PITFALL_AVOIDANCE_QUESTIONS.md  
     *(35-feed row-by-row interrogation across Macro, Tactical, Orderflow, and Solvency quadrants)*
   - 📋 **`AUTONOMOUS_WAKEUP_CHECKLIST.md`**: https://github.com/kbsingh1399/Trading_2/blob/main/Data/Manditory/AUTONOMOUS_WAKEUP_CHECKLIST.md  
     *(Canonical pre-trade verification checklist and native table formatting mandate)*
   - 🔄 **`CONTINUOUS_KAIZEN_SELF_IMPROVEMENT_PROTOCOL.md`**: https://github.com/kbsingh1399/Trading_2/blob/main/Data/Manditory/CONTINUOUS_KAIZEN_SELF_IMPROVEMENT_PROTOCOL.md  
     *(Kaizen session learning: evaluate past setbacks, eliminate regression, never repeat mistakes)*

2. **Independent Research Mandate Across 156 Assets**:
   - Both Arena.ai and Z.ai MUST individually and independently conduct their own quantitative research across the full **156-asset universe** (Crypto Perpetuals, Forex Majors & Crosses, Precious Metals, Global Equity Indices & Energy).
   - Do NOT simply duplicate Antigravity's candidates. You MUST independently discover and nominate **your own top 1-2 high-confluence candidate limit orders**.

3. **Antigravity Final Boss Execution Gate**:
   - Antigravity is the Sovereign Final Boss and sole execution authority on MetaTrader 5 Account #5064568.
   - Antigravity will combine its own 156-asset findings, Arena.ai's individual candidate nominations, and Z.ai's individual candidate nominations into a final consensus clearance matrix, and make the definitive order punch on MT5.

---

## 📊 1. LIVE BROKER & ACCOUNT STATE (GROUND TRUTH)
From `00_MT5_Account_Telemetry.parquet` and `Data/account_equity/latest/account_equity_snapshot.json`:
- **Realized Balance**: **4,782.61 USD** | **Equity**: **4,782.61 USD** (100% Cash)
- **Active Open Positions**: **0**
- **Active Pending Limit Orders**: **0**
- **G-1 Hard Statutory Floor**: **4,775.00 USD** (Inviolable Floor)
- **Operating Defense Buffer**: **4,795.00 USD**
- **Current Floor Cushion**: **+7.61 USD** (4,782.61 USD - 4,775.00 USD)
- **Active Solvency Mode**: **CAPITAL PRESERVATION MODE** (Equity <= 4,795.00 USD)
- **Capacity Constraint**: Strictly **1 Trade Slot** (`N_open + N_pending <= 1`)
- **Mandatory Risk Sizing**: Nominal Risk strictly capped at **5.00 USD** per order (Stressed loss <= 8.25 USD)
- **Mandatory Friday Target**: **5,500.00+ USD** by Friday close (2026-10-30 21:00 UTC / 2026-10-31 02:30 IST) (~46.1 hours remaining).

---

## 🔍 2. ANTIGRAVITY'S INDEPENDENT SCANNER FINDINGS (FOR REFERENCE)
Antigravity's vectorized in-memory parquet data lake scan (43 feeds, 76,206 rows across 156 assets) surfaced the following top setups on our radar (all sized at strictly $5.00 USD risk):

1. **`GBPUSD.pi`** (Forex Raw):
   - Setup: `MODEL_1A_EXTREME_OVERBOUGHT` (Asian Session High Sweep / Mean Reversion)
   - Side: **SELL_LIMIT** @ `1.33236` | SL: `1.33391` (15.5 pips / 1.5 * ATR) | TP: `1.32895` (34.1 pips / 2.2R)
   - Sizing: `0.03 lots` -> Nominal Risk: **$4.65 USD** | Spread: **3.1 bps** | VR(4): **0.782**

2. **`EURUSD.pi`** (Forex Raw):
   - Setup: `MODEL_1A_EXTREME_OVERBOUGHT` (Prior Day High Sweep Fade)
   - Side: **SELL_LIMIT** @ `1.11561` | SL: `1.11696` (13.5 pips / 1.5 * ATR) | TP: `1.11263` (29.8 pips / 2.2R)
   - Sizing: `0.04 lots` -> Nominal Risk: **$4.80 USD** | Spread: **2.8 bps** | VR(4): **0.814**

3. **`USDCAD.pi`** (Forex Raw):
   - Setup: `MODEL_1A_EXTREME_OVERSOLD` (Demand Zone Liquidity Tap)
   - Side: **BUY_LIMIT** @ `1.40145` | SL: `1.39994` (15.1 pips / 1.45 * ATR) | TP: `1.40476` (33.1 pips / 2.2R)
   - Sizing: `0.05 lots` -> Nominal Risk: **$5.03 USD** | Spread: **3.5 bps** | VR(4): **0.825**

4. **`NAS100.p`** (Indices):
   - Setup: `MODEL_1B_SWEEP_RECLAIM_SELL` (Session Value Area High Rejection)
   - Side: **SELL_LIMIT** @ `20485.50` | SL: `20535.50` (50 pts / 1.35 * ATR) | TP: `20385.50` (100 pts / 2.0R)
   - Sizing: `0.10 lots` -> Nominal Risk: **$5.00 USD** | Spread: **0.46 bps** | VR(4): **0.795**

5. **`ETHUSD.pi`** (Crypto Raw):
   - Setup: `MODEL_1A_WHALE_WALL_FADE_SELL` (Exhaustion into Institutional Ask Armor)
   - Side: **SELL_LIMIT** @ `2365.50` | SL: `2375.50` (10.0 pts / 1.20 * ATR) | TP: `2340.50` (25.0 pts / 2.5R)
   - Sizing: `0.50 lots` -> Nominal Risk: **$5.00 USD** | Spread: **12.86 bps** | VR(4): **0.897** | Whale Ask Armor: **$12.3M USD** at 2350–2368.

---

## 🏛️ 3. YOUR REQUIRED OUTPUT FORMAT (EXACT TABLES AS MANDATED)
In your response, you MUST output the following markdown tables and structured JSON:

### TABLE 1: 🛡️ 10-Pitfall Forensic Autopsy Matrix (For Your Proposed Candidate)
Audit your proposed candidate against all 10 pitfalls:
- Pitfall 1 (Whale wall persistence >= 180s, >= 100K USD)
- Pitfall 2 (Zero staging above un-swept stop cascades)
- Pitfall 3 (Zero unabsorbed CVD waterfalls)
- Pitfall 4 (Stop loss distance >= 1.20 * ATR_14)
- Pitfall 5 (Variance ratio regime bounds: VR(4) < 0.85 for M1, > 1.15 for M2)
- Pitfall 6 (Spread <= 5.0 bps TradFi / <= 25.0 bps Crypto)
- Pitfall 7 (Rollover spread blackout 21:15–22:30 UTC)
- Pitfall 8 (Zero cluster double-bets; capacity = 1)
- Pitfall 9 (Solvency floor defense: Equity - Stressed_Loss >= 4,775.00 USD)
- Pitfall 10 (Context amnesia & phantom fills)

### TABLE 2: 📑 Canonical Governance Documents Read & Proof-of-Compliance Audit
Confirm you have studied all 5 governance documents on GitHub.

### TABLE 3: 🎯 Nominated Individual Candidate Limit Order
Provide your exact nominated candidate limit order:
- Symbol
- Side (`BUY_LIMIT` / `SELL_LIMIT`)
- Entry Price
- Stop Loss Price
- Take Profit Price
- Volume Lots (strictly **$5.00 USD nominal risk**)
- Spread (in bps)
- Variance Ratio VR(4)
- Stop / ATR Ratio
- Primary Catalyst / Supporting Whale Armor

### STRUCTURED JSON BLOCK:
Conclude with this standardized JSON:
```json
{
  "council": "[ARENA_AI / Z_AI]",
  "canonical_docs_verified": true,
  "own_candidate_nomination": {
    "symbol": "[SYMBOL]",
    "side": "[BUY_LIMIT / SELL_LIMIT]",
    "entry_price": 0.0,
    "sl_price": 0.0,
    "tp_price": 0.0,
    "volume_lots": 0.0,
    "nominal_risk_usd": 5.00,
    "stressed_risk_usd": 8.25,
    "spread_bps": 0.0,
    "model_type": "[MODEL_1A / MODEL_1B / MODEL_2]",
    "primary_catalyst": "[Orderbook wall / Liquidation sweep / CVD divergence / Fib shelf]"
  },
  "evaluation_of_antigravity_candidates": {
    "preferred_antigravity_pick": "[GBPUSD / EURUSD / USDCAD / NAS100 / ETHUSD]",
    "rationale": "[Why this is the best among Antigravity's list or why your own candidate is superior]"
  },
  "solvency_clearance": {
    "equity_usd": 4782.61,
    "post_loss_equity_usd": 4777.61,
    "hard_floor_usd": 4775.00,
    "floor_cushion_remaining_usd": 2.61,
    "verdict": "RATIFIED_CAPITAL_PRESERVATION"
  }
}
```
