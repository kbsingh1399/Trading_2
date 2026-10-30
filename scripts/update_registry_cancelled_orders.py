import sys
import datetime

sys.stdout.reconfigure(encoding='utf-8')

with open('Data/Manditory/LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Update account section
text = text.replace(
    "- **Active Resting Pending Orders**: **5 LIVE PENDING MAKER LIMIT ORDERS**\n- **Total Contingent Downside Risk**: **33.27 USD**",
    "- **Active Resting Pending Orders**: **3 LIVE PENDING MAKER LIMIT ORDERS** (BTC #19489155 & BNB #19489157 CANCELLED via Tri-Council consensus due to 2.5R violation)\n- **Total Contingent Downside Risk**: **26.90 USD**"
)

# Update order table
old_table = """| **Resting #1** | `#19489155` | `BTCUSD.pi` | SELL_LIMIT | 0.01 lot | 81,084.00 | **81,680.00** | 80,180.00 | 5.96 USD | **LIVE_RESTING_PENDING** (SL placed +185 pts above 24H Short Max Pain 81,494.86 & +127 pts above 81,553 48H peak. Leans against PD_VAH 81,003.11) |
| **Resting #2** | `#19489157` | `BNBUSD.p` | SELL_LIMIT | 0.05 lot | 753.30 | **761.50** | 743.50 | 0.41 USD | **LIVE_RESTING_PENDING** (SL placed +3.01 pts above 24H Short Max Pain 758.49. Aligned with Weekly VAH 751.13 and PD_VAH 754.57) |
| **Resting #3** | `#19489158` | `XAUUSD.pi` | SELL_LIMIT | 0.01 lot | 4,040.50 | **4,049.50** | 4,018.00 | 9.00 USD | **LIVE_RESTING_PENDING** (SL leans against 4,050.00 institutional ask wall. Fades PD_VAH 4,039.67 sweep exhaustion. Purged to raw +2.5R target) |
| **Resting #4** | `#19489159` | `NAS100.p` | SELL_LIMIT | 0.01 lot | 29,535.00 | **29,620.00** | 29,320.00 | 8.50 USD | **LIVE_RESTING_PENDING** (SL padded by 85 index points. Leans against Low Volume Node above PD_VAH 29,520.00. Risk strictly <= 10.00 USD) |
| **Resting #5** | `#19489160` | `DJ30.p` | SELL_LIMIT | 0.01 lot | 52,638.00 | **52,732.00** | 52,402.00 | 9.40 USD | **LIVE_RESTING_PENDING** (SL padded by 94 index points. Leans against exhaustion node above PD_VAH 52,579.18. Risk strictly <= 10.00 USD) |"""

new_table = """| **Resting #1** | `#19489158` | `XAUUSD.pi` | SELL_LIMIT | 0.01 lot | 4,040.50 | **4,049.50** | 4,018.00 | 9.00 USD | **LIVE_RESTING_PENDING** (SL leans against 4,050.00 institutional ask wall. Fades PD_VAH 4,039.67 sweep exhaustion. Purged to raw +2.5R target) |
| **Resting #2** | `#19489159` | `NAS100.p` | SELL_LIMIT | 0.01 lot | 29,535.00 | **29,620.00** | 29,320.00 | 8.50 USD | **LIVE_RESTING_PENDING** (SL padded by 85 index points. Leans against Low Volume Node above PD_VAH 29,520.00. Risk strictly <= 10.00 USD) |
| **Resting #3** | `#19489160` | `DJ30.p` | SELL_LIMIT | 0.01 lot | 52,638.00 | **52,732.00** | 52,402.00 | 9.40 USD | **LIVE_RESTING_PENDING** (SL padded by 94 index points. Leans against exhaustion node above PD_VAH 52,579.18. Risk strictly <= 10.00 USD) |

---

### 🚫 CANCELLED / REMOVED ORDERS IN CYCLE_029 (Tri-Council Solvency Enforcement):
| Ticket | Symbol | Original Order | Limit Entry | Original SL | Original TP | R:R Ratio | Cancellation Rationale |
|---|---|---|---|---|---|---|---|
| `#19489155` | `BTCUSD.pi` | SELL_LIMIT | 81,084.00 | 81,680.00 | 80,180.00 | **1.517R** | **CANCELLED ON MT5 (retcode 10009)**. Violated statutory 2.5R minimum mandate. Reduced contingent risk by 5.96 USD. |
| `#19489157` | `BNBUSD.p` | SELL_LIMIT | 753.30 | 761.50 | 743.50 | **1.195R** | **CANCELLED ON MT5 (retcode 10009)**. Violated statutory 2.5R minimum mandate. Reduced contingent risk by 0.41 USD. |"""

text = text.replace(old_table, new_table)

with open('Data/Manditory/LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("SUCCESS: Updated LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md with cancelled orders.")
