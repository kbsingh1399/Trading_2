# OX_ALPHA_63 Master Specification: GitHub-Anchored Strategy Co-Pilot & Decision Chain Upgrade

## 1. System Topology & Synchronization Protocol
This document establishes the GitHub branch `arena/4adf3661-trading-2` on repository `https://github.com/kbsingh1399/Trading_2` as the **Single Source of Truth (SSOT)** and asynchronous synchronization bus between **Arena.ai (Cloud Quantitative Strategist)** and **Antigravity (Local Execution Workstation & Risk Arbiter)** on MetaTrader 5 Account 5064568 (Blueberry Markets SVG LLC).

### Operational Invariants:
1. **GitHub Synchronization Bus**:
   * Remote URL: `https://github.com/kbsingh1399/Trading_2.git`
   * Target Branch: `arena/4adf3661-trading-2`
   * All code updates, strategy logic refactors, and trade plans (`docs/trade_plans/*.json`) produced by Arena.ai MUST be committed and pushed directly to `origin/arena/4adf3661-trading-2`.
   * Local Antigravity will pull directly from `origin/arena/4adf3661-trading-2`, verify bit-identity, run the offline and live test suites, and stage verified orders.
2. **Bidirectional M2M Tunnel**:
   * Active Cloudflare Tunnel: `https://constantly-combines-collectables-script.trycloudflare.com` -> `http://127.0.0.1:8080`
   * HMAC Secret (`OMNI_API_SECRET`): `0b07f4298deddd67dcb505038002399023601bfed067cf48`
   * Protocol: `omni.arena_remote.v1` signed envelopes with timestamp window and replay nonces.

---

## 2. Live Account Financials & Ground Truth (As of 2026-10-07 07:15 UTC)
* **Broker Terminal**: MetaTrader 5 Account `5064568` (Blueberry Markets SVG LLC)
* **Balance & Equity**: **4,831.73 USD** (100% Cash Defense | 0.00 USD Margin in Use)
* **Floating Profit / Loss**: **0.00 USD**
* **Hard Capital Floor**: **4,775.00 USD** (Strict 4.50% / 225.00 USD drawdown circuit breaker)
* **Headroom Above Floor**: **+56.73 USD** cash reserve (+1.19% buffer above absolute stop)
* **Account Drawdown**: **-168.27 USD** (-3.37% DD on 5,000.00 USD initial capital; Drawdown Defense Mode active)
* **Open Positions Count**: **0** (Flat across all 24 instruments)
* **Pending Orders Count**: **0** (No dangling limits)
* **Capacity Utilization**: **0 / 2 slots** occupied (2 full slots available under institutional `MAX_CONCURRENT = 2` mandate)
* **Prior Execution Outcomes**:
  * GOLD Short ticket `#18576872` was closed for **+20.80 USD profit**.
  * SOL Long ticket `#18596013` (0.10 lots @ 120.05 USD) was stopped out at **118.85 USD** during the overnight crypto liquidation cascade for **-12.00 USD (-1.00R)** with zero excess slippage.

---

## 3. Forensic Autopsy of OX_ALPHA_62 SOL Plan Refusal
When Arena's `OXALPHA62-SOL-LONG-20261007A` plan (`SOLUSD.p` Long 0.15 lots @ Limit 119.95, SL 119.25, TP 121.70, Risk 10.50 USD) was evaluated by the local fail-closed stager (`stage_trade_plan.py`) over the live tunnel:
* **Transport Gate**: PASSED (`ok`).
* **Freshness Gate**: PASSED (`ok`).
* **Macro Blackout Gate**: PASSED (`clear`).
* **Account Solvency Gate**: PASSED (`equity_usd: 4831.73`, `cushion_above_floor_usd: 46.23`).
* **Capacity Gate**: PASSED (`filled: 0, pending: 0`).
* **Live Marketable Limit Gate**: **FAILED (`REFUSED live (marketable_limit)`)**.
  * *Root Cause*: Live broker ask for `SOLUSD.p` was **118.91 USD**.
  * The plan commanded a limit buy at **119.95 USD**, which is **above current market ask**. Placing a buy limit above market crosses the spread and executes as an aggressive market taker order.
  * Furthermore, the stop loss at **119.25 USD** was **above the live market price (118.73 USD)**, which MT5 rejects with `TRADE_RETCODE_INVALID_STOPS (10016)`.
  * The local fail-closed gatekeeper operated with 100% mathematical fidelity and saved the account from execution error.

---

## 4. Institutional Upgrade Mandate: Zero-Cost Factory Suite Integration
Arena.ai is tasked with upgrading the quantitative decision-making chain (`omni.decision_chain.v2`) and trade plan specification (`omni.trade_plan.v2`) by directly integrating our local 6-Pillar `ZeroCostDataFactory` (`Terminal/Data_Factory/`):

### The 6 Pillars to Integrate:
1. **Pillar 1: Reconstructed Trade Flow & Forced Liquidations** (`Terminal/Data_Factory/liquidation_engine.py`):
   * Reconstructs liquidation clusters and margin calls from tick-level volume surges.
   * *Requirement*: Require `long_liq_zs > 1.8` or confirmed discount absorption before approving Long entries.
2. **Pillar 2: Stop Cluster Engine & Whale Wall Persistence** (`Terminal/Data_Factory/factory.py` - `_WallTracker`):
   * Enforces that resting whale walls (>= 50k USD on L3 orderbook) must have a verified persistence of `>= 180 seconds` to eliminate spoofing.
3. **Pillar 3: On-Chain Whale Flows & Entity Clusters** (`Terminal/Data_Factory/onchain.py`):
   * Ingests exchange net transfers from major wallets to prevent buying into active institutional distribution.
4. **Pillar 4: Farside Institutional ETF Flows** (`Terminal/Data_Factory/macro.py` - `FarsideETFFlows`):
   * Evaluates US spot Bitcoin & Ethereum net ETF flows (IBIT, FBTC, etc.) to set directional macro beta bias.
5. **Pillar 5: Fear & Greed Index + Coinbase Premium Index** (`Terminal/Data_Factory/macro.py`):
   * Evaluates market sentiment regime (Extreme Fear < 25, Extreme Greed > 75).
   * Evaluates Coinbase spot vs Binance futures price differential to confirm genuine US institutional spot demand vs offshore leverage.
6. **Pillar 6: Cross-Source Consistency & Anomaly Engine** (`Terminal/Data_Factory/crosscheck.py`):
   * Vetoes orders if book spreads or feeds diverge abnormally across venues.

---

## 5. Deliverables for Arena.ai
1. **Decision Chain Upgrade (`omni.decision_chain.v2`)**: Implement an upgraded decision evaluator that takes inputs from the 6 Factory pillars and produces verifiable trade plans.
2. **Deterministic Tests**: Add comprehensive test coverage verifying that every Factory gate correctly gates trade candidate generation.
3. **Calibrated Trade Plans**: Formulate fresh trade plans calibrated to current live market prices:
   * **GOLD (`XAUUSD.pi`)**: Re-evaluating accumulation at 4,132–4,136 USD base toward 4,149 USD Session VWAP (0.24 bps spread).
   * **BTC (`BTCUSD.pi`)**: Front-running the 25.05M USD Mega Whale bid at 83,500 USD (1.78 bps spread).
   * **SOL (`SOLUSD.p`)**: Passive limit resting strictly below ask, front-running the 14.62M USD Mega Whale bid at 117.00 USD.
4. **Direct Push**: Commit all changes and push directly to `origin/arena/4adf3661-trading-2`.
