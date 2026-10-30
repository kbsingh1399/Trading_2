import pathlib

p = pathlib.Path("Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md")
text = p.read_text(encoding="utf-8")

old_target = """- [ ] **Step 5: Activate AutoWake daemon and await completion of both systems** (IN PROGRESS: task-167244)
- [ ] **Step 6: Tri-Council Triangulation & Broker Desk Execution**
- [ ] **Step 7: Update records and restart 20-minute AutoWake cycle**"""

new_target = """- [x] **Step 5: Activate AutoWake daemon and await completion of both systems**
  - Watchdog task completed: Arena.ai harvested to `docs/trade_plans/ARENA_LATEST_RAW.md` (5,039 chars). Z.ai output harvested to `docs/trade_plans/ZAI_LATEST_RAW.md` (11,237 chars).
  - Both models probed via Chrome CDP on port 9222.
- [x] **Step 6: Tri-Council Triangulation & Broker Desk Execution**
  - **Seat #1 (Antigravity)**: Reconciled broker fills and exits. Ticket #19532057 (`XMRUSD.p`) filled Deal #17702967 @ 585.50 (17:08:37 UTC), hit SL Deal #17704303 @ 577.50 (17:25:05 UTC) during broad altcoin liquidation flush. Loss strictly capped at -$8.00 USD (0.16% of equity). Capital preserved at $4,755.23 USD (99.83% of equity intact).
  - **Seat #2 (Arena.ai)**: Noted XMR ask dropping below 585.50, flagged fill risk, recommended canceling remaining pending orders (#19532055 BTC, #19532058 AVE) to preserve capital under canonical floor rules.
  - **Tri-Council Synthesis & Operator Mandate**: Operator explicitly overrode artificial floors (*"no hard floor... keep punching and trading"*). Resting limit orders on BTC (#19532055, $5.00 risk) and AAVE (#19532058, $9.10 risk) are retained on MT5 broker. Total contingent risk: $14.10 USD (0.29% of account equity). Available capacity: 1 slot (2/3 deployed).
- [x] **Step 7: Update records and restart 20-minute AutoWake cycle**
  - Updated `Data/cycle_envelope.json` and `Data/Manditory/LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md` to reflect exact balance $4,755.23 USD, 0 open positions, and 2 resting maker orders.
  - Pushed commits to GitHub main (`kbsingh1399/Trading_2`).
  - Gravitas Standard: `[x] 🏛️ Gravitas Rigor Standard: FULLY ENFORCED`."""

norm_text = text.replace("\r\n", "\n")
norm_old = old_target.replace("\r\n", "\n")
norm_new = new_target.replace("\r\n", "\n")

if norm_old in norm_text:
    norm_text = norm_text.replace(norm_old, norm_new, 1)
    p.write_text(norm_text, encoding="utf-8")
    print("SUCCESS: Updated ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md!")
else:
    print("FAILED: old_target not found!")
