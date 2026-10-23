# 🏛️ DIRECT LOCAL CODEBASE EXECUTION DIRECTIVE: GPT SOL 6.1
## Authority: Chief Quantitative Architect & Systems Engineer
### Target Workspace: `C:\Users\SIGMA\Documents\Trading_2`
### Operating System: Windows 11 (PowerShell) | Python 3.10+
### MT5 Account: Blueberry Markets SVG-Live (#5064568)

---

## ⚡ OPERATIONAL DIRECTIVE FOR GPT SOL 6.1 (LOCAL EXECUTION AGENT)

You are operating as a **locally installed autonomous quantitative engineering agent** with direct access to file tools (`read_file`, `write_file`, `edit_file`) and terminal shell (`run_command`).
You are NOT merely producing conversational text or suggestions. You are commanded to **directly open, inspect, modify, and save the required production governance files on disk** in `C:\Users\SIGMA\Documents\Trading_2\Data\Manditory\`.

---

## 🎯 1. GROUND-TRUTH ACCOUNT STATE (REAL-TIME MT5 TELEMETRY)

Ticket #19267445 (`BTCUSD.pi` Short) has hit its Take Profit target at **80,600.00 USD**, banking **+$66.00 USD gross** / **+$65.19 USD net**!
- **Realized Balance**: **`4,865.07 USD`** (Real-time verified via MT5 API).
- **Floating Equity**: **`4,865.07 USD`** (100% Flat Cash baseline).
- **Open Positions**: **0** | **Pending Orders**: **0**.
- **Hard Floor (4,600.00 USD) Cushion**: **`+265.07 USD`** (Inviolate evaluation floor).
- **Operating Buffer (4,650.00 USD) Cushion**: **`+215.07 USD`** (Capital preservation barrier).
- **Solvency Kernel (4,795.00 USD) Cushion**: **`+70.07 USD`**.
- **Net Realized Headroom**: **`+68.07 USD`** (`4,865.07 - 2.00 contingency reserve - 4,795.00`).
- **New Risk Admission Status**: **`TRUE`** (Exceeds the 11.38 USD minimum risk threshold).
- **Capital Regime**: **`TIER 2 HOUSE MONEY`** (Realized Equity > 4,850.00 USD):
  * Base Risk Budget per Trade: **`15.00 USD to 25.00 USD`** (0.30% to 0.50%).
  * Max Concurrent Positions: **`2`** across independent, non-correlated assets.
  * Solvency Check: Even under double simultaneous maximum stopouts (-50.00 USD), realized balance remains `4,815.07 USD >= 4,795.00 USD` (+20.07 USD safe cushion above kernel).

---

## 📂 2. TARGET FILES FOR DIRECT LOCAL MODIFICATION

All files are located in: `C:\Users\SIGMA\Documents\Trading_2\`

| File Name | Absolute Windows Path | Required Direct Modifications |
|---|---|---|
| **1. Decision Chain** | `C:\Users\SIGMA\Documents\Trading_2\Data\Manditory\STANDARDIZED_TRADING_DECISION_CHAIN.md` | - Refine Section 2.2: Hard Binary Gates vs Soft Calibrated EV Ranking.<br/>- Codify Section 2.3: Asset-specific microstructure (Crypto L2/L3, FX/Metals Auction Value Area, Indices Cash Session).<br/>- Update Step 8: Broker-native lot snapping `lot*` with `order_calc_profit` and Tier 2 House Money budget (15.00–25.00 USD). |
| **2. Wakeup Checklist** | `C:\Users\SIGMA\Documents\Trading_2\Data\Manditory\AUTONOMOUS_WAKEUP_CHECKLIST.md` | - Update Step 0: Reflect 4,865.07 USD baseline balance.<br/>- Update Step 8: Size candidate orders at Tier 2 House Money risk (15.00–25.00 USD) with `order_check`. |
| **3. Account Switch** | `C:\Users\SIGMA\Documents\Trading_2\Data\Manditory\ACCOUNT_SWITCH_BOOTSTRAP_PROTOCOL.md` | - Update Section 1: Set ground-truth balance to 4,865.07 USD, 0 open positions, +70.07 USD kernel cushion, Tier 2 House Money status.<br/>- Guarantee all 5 persistent background daemons remain undisturbed during boots. |
| **4. Subagent Prompts** | `C:\Users\SIGMA\Documents\Trading_2\Data\Manditory\SUBAGENT_PROMPT_TEMPLATES.md` | - Verify Part 2 prompt blocks (Role A, B, C, D) maintain exact mathematical estimators, sheet coordinates, and the step-level meta-cognitive check. |
| **5. Kaizen Protocol** | `C:\Users\SIGMA\Documents\Trading_2\Data\Manditory\CONTINUOUS_KAIZEN_SELF_IMPROVEMENT_PROTOCOL.md` | - Verify Part 6 meta-cognitive self-inquest check ("Can I do this better with installed skills/agents?"). |
| **6. Dual-Council Prompt** | `C:\Users\SIGMA\Documents\Trading_2\Data\Manditory\Arena_GLM_Standard_Prompt.md` | - Update ground-truth account figures: 4,865.07 USD balance, +68.07 USD realized headroom, Tier 2 House Money risk authorization. |

---

## 🔬 3. DETAILED IMPLEMENTATION INSTRUCTIONS FOR EACH FILE

### TASK 1: Edit `C:\Users\SIGMA\Documents\Trading_2\Data\Manditory\STANDARDIZED_TRADING_DECISION_CHAIN.md`
Directly modify the file to codify:
1. **The Calibrated Two-Tier Ranking Funnel (Section 2.1 - 2.2)**:
   - **Tier 1 (Hard Gates)**: Strictly binary fail-closed checks:
     * `SolvencyMet`: `min(balance, equity) - StressedLoss >= 4795.00 USD`
     * `SessionTradable`: Broker session open, native venue open, no event blackout, no rollover.
     * `DataFresh`: Row-level sheet cell timestamp <= cutoff_utc.
   - **Tier 2 (Soft Expected Value Ranking)**: For hard-gate survivors, calculate:
     `EV_net = P_fill * [P_TP * Gain_net - (1 - P_TP) * Loss_net - AdverseSelection - BrokerFrictions] - (1 - P_fill) * WaitCost`
     Rank by `Utility = LCB_5%(EV_net) / Expected_Capital_Minutes`.
2. **Asset-Class Specific Microstructure Architecture (Section 2.3)**:
   - *Crypto Perpetuals*: L2 20-level depth imbalance, taker CVD z-score divergence (`zc_div > 0.8`), resting whale orders (`persist >= 180s`), stop cascades.
   - *Forex Majors & Metals*: Auction Market Structure (Sheet 33 Value Area High/Low, POC balance vs imbalance), London/NY session open sweeps, interbank rollover lockout (`21:15–22:30 UTC`).
   - *Equity Indices*: Cash session hours (`14:30–21:00 UTC` for US, `08:00–16:30 UTC` for EU), Fair Value Gaps, Volume Profile POCs. Mark off-hours CFD quotes as `WATCHLIST_ONLY`.
3. **Broker-Native Structural Lot Sizing (Step 8)**:
   - Mandate MT5 API primitives: `order_calc_profit()`, `order_calc_margin()`, `order_check()`.
   - Algorithm `lot*`: Search broker volume grid `[volume_min, volume_max, volume_step]`. Pick the largest volume where `abs(profit_at_sl) <= Risk_Budget` (15.00–25.00 USD) AND `min(balance, equity) - StressedLoss >= 4,795.00 USD`.

### TASK 2: Edit `C:\Users\SIGMA\Documents\Trading_2\Data\Manditory\ACCOUNT_SWITCH_BOOTSTRAP_PROTOCOL.md`
Directly update the telemetry baseline:
- Balance: **4,865.07 USD** | Equity: **4,865.07 USD** | Margin Used: **0.00 USD** | Free Margin: **4,865.07 USD**.
- Active Positions: **0** (Ticket #19267445 closed at TP 80,600.00 USD, banking +65.19 USD net).
- Hard Floor Cushion: **+265.07 USD** | Operating Buffer Cushion: **+215.07 USD** | Solvency Cushion: **+70.07 USD**.
- Realized Headroom: **+68.07 USD** | New Risk Admissible: **TRUE** | Capital Mode: **Tier 2 House Money**.

### TASK 3: Edit `C:\Users\SIGMA\Documents\Trading_2\Data\Manditory\Arena_GLM_Standard_Prompt.md`
Update the prompt template dispatched to Arena.ai and Z.ai:
- Update the embedded account inventory to reflect the new 4,865.07 USD balance and Tier 2 House Money risk budget.
- Command Arena and Z.ai to evaluate candidates across the 156-asset universe using the Two-Tier Hard Gate + Soft EV Funnel.

---

## ⚙️ 4. POST-MODIFICATION VERIFICATION & PARITY SYNC

Immediately after editing the files on disk, execute these verification commands in the workspace:

1. **Re-generate Fresh Cycle Envelope**:
   ```powershell
   python Terminal/generate_cycle_envelope.py
   ```
   Confirm output prints: `Balance: 4865.07 | Solvency Headroom: $70.07 USD | New Risk Admissible: True`.

2. **Run Universe Scanner**:
   ```powershell
   python Terminal/run_comprehensive_universe_scanner.py
   ```
   Confirm candidate generation evaluates setups with dynamic risk sizing (15.00–25.00 USD).

3. **Synchronize Dual-Repo Parity**:
   ```powershell
   python .agents/scripts/verify_and_sync_agents.py
   ```
   Confirm 0 byte mismatches across `Trading_2` and `Engine_2`.

4. **Git Commit & Push**:
   ```powershell
   git add Data/Manditory/ docs/ ; git commit -m "feat(quant): integrate GPT SOL 6.1 production governance upgrades and 4,865 USD baseline" ; git push origin main
   ```
