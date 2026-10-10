# 🏛️ GPT ASTRA: INSTITUTIONAL CODE AUDIT & DIRECT EDIT MANDATE

> **Target Agent**: GPT Astra (Locally Installed Senior Code Auditor & Systems Architect)  
> **Workspace**: `c:\Users\SIGMA\Documents\Trading_2`  
> **Direct Execution Mandate**: Forensic review of recent upgrades, bug diagnosis, and **direct in-place editing/patching** of the codebase.

---

## 🔗 CANONICAL GITHUB REPOSITORY & RAW FILE REFERENCES

All code, data, and live telemetry are versioned and synchronized on GitHub:

- **Primary Repository**: [https://github.com/kbsingh1399/Trading_2](https://github.com/kbsingh1399/Trading_2)
- **Production `main` Branch**: [https://github.com/kbsingh1399/Trading_2/tree/main](https://github.com/kbsingh1399/Trading_2/tree/main)
- **Bidirectional Arena Branch**: [https://github.com/kbsingh1399/Trading_2/tree/arena%2F537c1eb8-trading-2](https://github.com/kbsingh1399/Trading_2/tree/arena%2F537c1eb8-trading-2)

### Direct Raw Endpoints for Immediate Ingestion:
1. **Live Telemetry Snapshot (Auto-updated every 60s)**:  
   `https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/telemetry/live_snapshot_latest.json`
2. **Decision Gates Engine (V3)**:  
   `https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Terminal/decision_gates_v3.py`
3. **Hyperdash On-Chain Flow Feed**:  
   `https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Terminal/Data_Factory/hyperdash_flow_feed.py`
4. **Autonomous Telemetry Git Daemon**:  
   `https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Terminal/Data_Factory/autonomous_telemetry_git_daemon.py`
5. **Arena Strategy Bridge**:  
   `https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Terminal/arena_bridge.py`
6. **Master Active Context & Invariants**:  
   `https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/rules/ACTIVE_CONTEXT.md`
7. **Complete Historical Session Narrative**:  
   `https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/memory/session_chat_history.md`

---

## 🎯 AUDIT TARGETS & SPECIFIC UPGRADES TO REVIEW

Review the following recent upgrades in detail. If any bug, race condition, or degradation is discovered, **directly edit and fix the code in place**:

### 1. `Terminal/Data_Factory/hyperdash_flow_feed.py`
- **Recent Upgrades**:
  * Real Hyperliquid L1 on-chain DEX flow integration via GraphQL.
  * Verified Ethereum whale wallet orders (`0x...` addresses, notionals $\ge 150\text{k USD}$).
  * Structural stop clusters and reconstructed liquidation cascade bands.
  * L3 whale wall extraction with standing duration (`persist_s`) and Gate G-7 classification.
- **Audit Focus & Required Fix**:
  * In `sync_live_api_flows()`, evaluate trade deduplication:
    ```python
    tid = f"{t_ms}_{int(round(px*1e2))}_{int(round(sz*1e2))}_{side_char}_{trade_seq}"
    ```
    Arena.ai flagged that `trade_seq` resets to 0 each 60-second poll cycle. For fills that lack a native exchange ID, if they reappear in the next polling window, they receive a different key and could duplicate.
    👉 *Task*: Verify or patch deduplication so that records are deduplicated persistently on `(t_ms, px, sz, side)` without risk of double-counting whale notionals.
  * Atomic writes: Ensure persistence to `Data/Hyperdash_Flows/hyperdash_flows_history.parquet` and `.json` is crash-safe and atomic.

### 2. `Terminal/Data_Factory/autonomous_telemetry_git_daemon.py`
- **Recent Upgrades**:
  * Continuous 60-second telemetry snapshot generation and git push.
  * Dual-ref atomic push: pushes simultaneously to both `origin/main` and `origin/arena/537c1eb8-trading-2`.
- **Audit Focus**:
  * Concurrency safety: Verify that `sync_git_cycle()` does not conflict with manual operator commits or code development.
  * Singleton enforcement on Windows: Verify that file locking (`msvcrt.locking`) recovers cleanly across process restarts.
  * Memory hygiene: Confirm `gc.collect()` and file handle closing prevent memory leaks over multi-day uptime.

### 3. `Terminal/decision_gates_v3.py` & `Terminal/dg_context.py`
- **Recent Upgrades**:
  * 7-stage deterministic gating pipeline (G-1 Floor Defense, G-2 Macro Blackout, G-3 Staleness & Weekend CFDs, G-4 HTF Trend Agreement, G-5 Spread Friction, G-6 Volatility/ATR, G-7 Orderbook L2/L3 Whale Walls).
  * Dual-Model Architecture: Model 1 Extreme Mean Reversion ($|Z| \ge 2.0\text{ SD}$) with CVD absorption vs Model 2 Trend Pullbacks ($|Z| < 2.0\text{ SD}$, 1H votes $\ge 2$, 4H ER $> 0.25$, 4H $t$-stat $< -1.5$ for short).
- **Audit Focus**:
  * Check for division by zero risks (zero ATR, zero volume, zero sigma).
  * Check null/None handling across all gate dictionaries.
  * Verify strict causal anti-lookahead: order execution is evaluated only at next bar open (`opens[j+1]`), never at current bar close.

### 4. `Terminal/arena_bridge.py`
- **Recent Upgrades**:
  * Lean link-driven prompt architecture: reduced from 55k characters down to 15k characters (>73% token reduction).
  * Replaced redundant 48,000-character raw OHLCV dump with direct pointer to `live_snapshot_latest.json`.
- **Audit Focus**:
  * Ensure all prompt generation functions remain robust and properly format guidance for external reasoning models.

---

## 🛡️ STRICT INVARIANTS TO MAINTAIN DURING EDITS

1. **Zero Dollar Signs**: Strict prohibition on literal `$` symbols for currencies in documentation, prompts, and code comments where math formatting applies; always write `USD` or KaTeX math notation.
2. **Capital Floor Defense**: Stressed post-loss equity across all staged tickets must preserve $\ge 20.00\text{ USD}$ operating buffer above the 4,775.00 USD hard floor at all times (Stressed Equity $\ge 4,795.00\text{ USD}$).
3. **Passive Limit Orders Only**: Execution engine must ONLY stage passive limit orders resting at structural liquidity bands; NEVER cross the spread with market orders.
4. **Preserve Comments & Clean Architecture**: Keep changes scoped, high-signal, and preserve existing architecture.

---

## 🧪 POST-EDIT VERIFICATION PROTOCOL

After applying any edits, run the following commands locally:
1. **Run Test Suite**:
   ```powershell
   python -m pytest Tests/ -v
   ```
   (Must achieve 100% pass rate, zero failed tests).
2. **Update Code Graph**:
   ```powershell
   python -m graphify update .
   ```
3. **Verify Git Working Tree**:
   ```powershell
   git status
   ```

---

## 📋 OUTPUT FORMAT FOR YOUR REPORT

After inspecting and patching the files, provide your summary:
1. **Issues Diagnosed**: Exact file paths, line numbers, and root causes identified.
2. **Code Edits Applied**: Clear diff summary of the modifications you made.
3. **Test Results**: Output of `pytest` confirming all tests pass.
