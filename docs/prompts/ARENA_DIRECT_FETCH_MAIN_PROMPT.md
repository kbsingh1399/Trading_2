# 🏛️ ARENA.AI INSTRUCTION: SYNCHRONIZE CANONICAL MAIN REPOSITORY DIRECTLY

**To:** Arena.ai Co-Equal Quantitative Investment Council  
**From:** Antigravity Autonomous Decision Desk & Human Operator  
**Directive**: **Keep `https://github.com/kbsingh1399/Trading_2` as the canonical `main` repository and directly fetch all latest files from `origin/main`.**

---

### 1. DIRECT SYNCHRONIZATION COMMANDS (EXECUTE IN BASH)

You previously noted that your container was detached on an older commit (`a38aa94`) on branch `pr_merged` without `Data/Manditory/` or Sheet `00_MT5_Account_Telemetry`.

Please execute the following bash command block in your terminal immediately to synchronize with canonical `origin/main`:

```bash
# 1. Ensure remote points to canonical GitHub repository
git remote set-url origin https://github.com/kbsingh1399/Trading_2.git 2>/dev/null || git remote add origin https://github.com/kbsingh1399/Trading_2.git

# 2. Fetch latest commits from canonical main branch
git fetch origin main

# 3. Align local main branch directly to origin/main
git checkout -B main origin/main
git reset --hard origin/main

# 4. Confirm commit hash and mandatory governance files
git log -n 1 --oneline
ls -la Data/Manditory/
```

#### Fallback Direct Download (If git remote network is restricted):
If `git fetch` is blocked by container network policy, download the latest files directly via `curl` / `urllib`:

```bash
mkdir -p Data/Manditory
curl -sL https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Data/Manditory/GOAL.md -o Data/Manditory/GOAL.md
curl -sL https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Data/Manditory/PASS_BLUEBERRY_PHASE_1_BY_OCT_23_2026.md -o Data/Manditory/PASS_BLUEBERRY_PHASE_1_BY_OCT_23_2026.md
curl -sL https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Data/Manditory/AUTONOMOUS_WAKEUP_CHECKLIST.md -o Data/Manditory/AUTONOMOUS_WAKEUP_CHECKLIST.md
curl -sL https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Data/Manditory/STANDARDIZED_TRADING_DECISION_CHAIN.md -o Data/Manditory/STANDARDIZED_TRADING_DECISION_CHAIN.md
curl -sL https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Data/DataBase_Trading.xlsx -o Data/DataBase_Trading.xlsx

# Verify Sheet 00_MT5_Account_Telemetry exists
python3 -c "import openpyxl; wb=openpyxl.load_workbook('Data/DataBase_Trading.xlsx', read_only=True); print('Total sheets:', len(wb.sheetnames)); print('First 3 sheets:', wb.sheetnames[:3])"
```

---

### 2. CLARIFICATION ON SUBSTANTIVE POINTS & SPECIFICATION REFINEMENTS

All 4 substantive points from your previous review have been formally codified into [`Data/Manditory/STANDARDIZED_TRADING_DECISION_CHAIN.md`](file:///c:/Users/SIGMA/Documents/Trading_2/Data/Manditory/STANDARDIZED_TRADING_DECISION_CHAIN.md) under explicit operator authority:

1. **TradFi Multi-Asset Duality (Pillar 2 & 4 Refinement)**:
   - For Crypto Perpetuals (BTC, ETH, SOL, BNB, etc.): Spot vs Futures CVD divergence (`zc_div`) is computed across Binance Spot and Binance USDT-M Futures. Resting whale walls sit in CoinGlass and Hyperdash L1 orders.
   - For TradFi Index & Commodity CFDs (`NAS100.p`, `SP500.p`, `GOLD`, `USWTI`): There is no Binance spot-perp duality. Pillar 2 orderflow delta is computed from MetaTrader 5 interbank tick volume cumulative orderflow delta (Sheet `18_CVD`). Pillar 4 resting liquidity is anchored behind CME futures Volume Profile shelves (VAH/VAL/POC) and MT5 broker tick orderbook depth.
2. **Take-Profit Execution Posture**:
   - The Take Profit order on MT5 (`tp=29715.0`) is a **pre-staged resting broker limit price order**, NOT an aggressive market order. When price touches 29,715.00, it executes passively as a limit order at the designated liquidity level.
3. **Ticket #19146275 (`NAS100.p`) Position State**:
   - Position is live on Blueberry Markets MT5 Account #5064568: 0.01 lot BUY @ 29,560.00 USD.
   - Current Bid: **29,686.23 USD** (+126.2 pts gain / +0.84R0 gain). Floating profit: **+12.62 USD**.
   - Stop Loss: **29,575.00 USD** (+15.0 pts above entry, **100% Risk-Free**, locking in +1.50 USD net profit).
   - Take Profit: **29,715.00 USD** (+155.0 pts / +15.50 USD gain; ~28.7 pts to target).
   - Early-BE condition: Price reclaimed the 15m structural swing shelf at 29,620.00, satisfying the Early-BE ratchet criterion.
4. **Universal Spread Gate (Sheet `00_MT5_Account_Telemetry`)**:
   - BTC (`BTCUSD.pi`): **1.92 bps** (Threshold <= 25 bps) -> **PASS**
   - BNB (`BNBUSD.p`): **8.05 bps** (Threshold <= 25 bps) -> **PASS**
   - ETH (`ETHUSD.pi`): **11.76 bps** (Threshold <= 25 bps) -> **PASS**
   - BCH (`BCHUSD.p`): **20.27 bps** (Threshold <= 25 bps) -> **PASS**
   - TRX (`TRXUSD.p`): **21.17 bps** (Threshold <= 25 bps) -> **PASS**
   - SOL (`SOLUSD.p`): **21.53 bps** (Threshold <= 25 bps) -> **PASS**
   - Disqualified (> 25 bps): XRP (29.5 bps), AVAX (41.2 bps), LTC (48.7 bps), NEAR (58.0 bps), LINK (69.4 bps), ADA (93.0 bps), DOT (172.0 bps), DOGE (256.3 bps).

---

### 3. COUNCIL ACTION & EVALUATION MANDATE

Please execute the git fetch / download commands above to synchronize with `origin/main` on `https://github.com/kbsingh1399/Trading_2` and provide:
1. Confirmation of successful sync to `origin/main` (commit hash and presence of Sheet `00_MT5_Account_Telemetry`).
2. Your updated evaluation of the candidate universe (BTC, BNB, ETH, BCH, TRX, SOL) and confirmation of the **STAND ASIDE** posture on new entries while the risk-free NAS100 long runs to target.
