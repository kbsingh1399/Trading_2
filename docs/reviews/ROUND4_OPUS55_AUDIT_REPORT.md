Part 2 of 3 (§2–§4) is below, exactly as written in Round 3. Part 3 (§5–§8) comes next.

markdown
## 2. Pre-trade checklists: final form (supersedes Round 2 §2–3)

### 2.1 Model 1: extreme mean reversion (crypto CFDs only until price-only is promoted)
1. **Regime** = MEAN_REVERT, using the bounce-robust VR (§1.2), held for 2 consecutive 1H closes.
2. **Stretch at the sweep bar:** 2.0 ≤ −s·Z_sweep ≤ 3.5. **Never fade |Z| > 3.5.** Pure noise reaches |Z| ≥ 2 only 11–15% of the time, and a straight-line trend saturates near √3 ≈ 1.73. A reading beyond 3.5 means the path is **convex**: accelerating, with the forced flow not yet finished. You would be selling insurance at the moment the insured event is occurring.
3. **Session maturity:** session_bars ≥ 16 and σ_session ≥ 0.8·ATR_15m.
4. **Deceleration:** −s·(Z_t − Z_{t−4}) ≤ 0.75 and σ_YZ(4)/σ_YZ(96) ≤ 2.0.
5. **Flat value:** |ΔVWAP_8| / (8·σ_session) ≤ 0.05.
6. **Order flow:**
   - |CVD_push2| ≤ 0.70·|CVD_push1| with a lower low in price.
   - Sweep taker $ ≥ 2× median 1m.
   - λ_sweep / median λ_60m ≤ 0.50.
   - ≥ 3 consecutive 1m buckets with s·CVD ≥ 0.
7. **Flush done:**
   - Peak 1m liquidation ≥ 3× the 24h median.
   - Last 1m ≤ 20% of peak.
   - ΔOI_5m ≥ −0.10%.
   - A **15m close back inside the sweep extreme**.
8. **Geometry:**
   - Entry = sweep + 0.3·|reclaim − sweep| (+ typical spread for buys).
   - SL = sweep − s·(0.2·ATR + spread).
   - R ≥ 1 ATR.
   - TP = VWAP − 2 ticks.
   - RR ≥ 1.5; friction ≤ 0.15R; p_lower ≥ p* + 0.03.
9. **Expect a low firing rate.** With Z = 2, σ_session = 0.8 ATR and R ≥ 1 ATR, the VWAP target is ≤ 1.6R away, so lines 3 and 8 together admit few trades. Log the rejection reasons and check that they are not all line 8.

### 2.2 Model 2: trend pullback
1. **Regime** = TREND_UP/DOWN:
   - 1H passes ≥ 2 of {ER_48 > 0.35 in direction, VR z* > 1, return-based t > 2}, **and**
   - 4H ER_30 > 0.25 with the same-sign return t > 1.5.
   - Hysteresis as above.
2. **Geometry** from deterministic ZigZag pivots (§1.3):
   - Retrace 0.236–0.618.
   - Depth speed ln(E/P)/(σ_YZ·√n_p) ≤ 2.0.
   - Velocity ratio ≤ 0.60.
   - 15m higher low intact (P > HL − 0.2 ATR).
   - Exhaustion score ≤ 1.
3. **Entry shelf:**
   - ≥ 2 of {EMA20_15m, EMA50_15m, VAL/VAH, prior 15m/1H pivot, session VWAP} within 0.25 ATR of each other.
   - L_long = shelf + 0.25·σ_YZ·P + typical spread; L_short = shelf − 0.25·σ_YZ·P.
4. **Order flow (crypto):** pullback CVD ≤ 50% of impulse CVD; `taker_delta_exhaustion().ok`; no liquidation burst toward the shelf.
5. **Stop:** max(1.5·ATR, swing − 0.2·ATR). Shorts add the spread, because the stop triggers on Ask.
6. **TP:**
   - min(first obstacle − 2 ticks, 2.75R).
   - First obstacle = nearest of {15m/1H swing extreme, prior session high/low, ask wall ≥ 2M USD (crypto), upper 2σ band}.
   - **Gross RR ≥ 2.0** after shrinking to the obstacle; otherwise reject. Do not stretch the TP through the obstacle.
   - "Liquidation cascade pools" and "stop sweep clusters" are only observed for crypto. Elsewhere they are swing extremes. Name them as such.
7. **EV:** friction ≤ 0.15R and p_lower ≥ p* + 0.03.

### 2.3 Unconditional stand-aside (any one)
1. Regime UNDEFINED.
2. Spread + commission > min(20 bps, 1.5× median for the hour of week), or > 10% of R.
3. Fast approach v > 2.0 while within 1 ATR (resting orders: cancel).
4. Tier-1 macro ±15 min.
5. Rollover 21:30–22:30 UTC.
6. Friday after 20:00 UTC.
7. First 60 min after the weekly open.
8. Unverified tape on non-crypto **unless** running the promoted price-only Model 2.
9. Tick age outside [−0.5 s, 2 s] after offset correction; L2 > 10 s; bars > 30 min.
10. ≥ 2R realised loss in the session, or 3 consecutive losses.
11. **Ledger not reconciled** (§0 #4): stop until the 187.50 USD is explained.

**The in-range mandate must be repealed.** `ACTIVE_CONTEXT.md` §3 and `AGENTS.md` Part 5 say agents are "FORBIDDEN … from defaulting to Stand Aside simply because price is not at an extreme" and that "Stand Aside is only permitted if NEITHER model produces valid structural setups". Read literally, this forces a Model 2 search on every in-range asset. It directly contradicts stand-aside #1. Replace it with: *"Stand-aside is the default; an engine must prove admission."*

---

## 3. MT5 CFD microstructure, invalidation, and lifecycle

### 3.1 Queue priority: confirmed, with one nuance
- MT5 retail pending orders are held server-side and trigger when the broker's own quote reaches the price. There is no shared CLOB, so there is no queue position to lose.
- `stage_limit_order` already enforces `passive_only` against the **Bid** for buys, which is stricter than necessary.
- The nuance: a cancel is not entirely free. Re-staging costs one request plus the risk of a `stops_level` reject near the market.
- Protocol rebuttal #4 ("deleting forfeits queue priority … SP500 fill @ 7,791.50") is an anecdote, not evidence. Delete it from `ANTIGRAVITY_ARENA_THINKING_CHAIN_COUNCIL_PROTOCOL.md` §2.

**Why impulsive approaches are adversely selected.** A touch-triggered limit fills *exactly when* price arrives. Conditional on arrival, the post-fill return is E[r | fill] = μ_local + (information in the arrival speed). A fast approach (v > 2σ) means a flow imbalance that has not yet been absorbed. The fills it produces are therefore weighted towards paths that continue through the level, which is the same mechanism as Glosten–Milgrom adverse selection.

The **testable claim** is that 900 s markout in the v > 2σ bucket is significantly below markout in the v < 1σ bucket. Until `markout_report()` shows this on ≥ 30 fills per bucket, the threshold 2.0 is a prior.

**Timezone fix (P0 #1).** Replace the fixed constant with the dynamic estimator the bridge already has:
```python
def _normalize_tick_msc(self, raw_msc, symbol=None):
    if not raw_msc:
        return 0
    return int(raw_msc - 1000 * self._utc_offset_seconds(symbol))   # 30-min grid, cached 300 s
```
Also use `_utc_offset_seconds` for `broker_now` in `stage_limit_order` (expiration) and in `chain_verification_360.py`. Add a test that runs the GMT+2 and GMT+3 cases. Verified: with the current code, GMT+3 gives age 0 s, while GMT+2 gives **age 3,600 s, ratchet_ok = False, market_ok = False**.

### 3.2 Hold / cut / breakeven
The Round 2 result stands. Under zero drift, hold, cut and BE all have equal gross EV (0.800R from +0.8R with a 2.5R target). Only a **negative post-trigger drift** justifies BE or cut. Required before Phase 0 stays enabled: journal `P(TP | touched +0.8R)` for every trade and shadow order, and compare it with the martingale value 0.514 (Wilson interval). The ACTIVE_CONTEXT BE offset of +0.35R, the code's +0.15R and the protocol's "+0.50 USD net" are three different rules (§5.2).

---

## 4. Asset-class divergence: price-only variant
The policy is sound, but **it cannot execute as configured**:
1. **Admission rejects it.** `assert_joint_fill_safe(min_risk_usd=10.0)` raises `proposed_risk_out_of_bounds:7.25`.
   - **Fix:** add `min_risk_usd=5.0` for intents tagged `variant=price_only`.
   - Also check that `volume_min` lets 7.25 USD be reached at the structural stop. If not, skip the trade; don't round up.
2. **Friction doubles in R.** At 7.25 USD risk, c ≤ 0.15R allows **≤ 1.087 USD** round-trip cost. Many index/metal CFDs at minimum lot will fail. This is correct behaviour, but expect a low firing rate.
3. Stricter geometry for price-only Model 2:
   - 15m reclaim close back above the shelf.
   - Higher low confirmed by a ZigZag pivot.
   - Thrust ratio ≥ 0.7.
   - Exhaustion score = 0, not ≤ 1.
   - RR ≥ 2.25.
4. Attribution: separate `variant` tag in `executions.jsonl`; promote only after ≥ 30 shadow + live fills with a 900 s markout lower bound > friction.

---


Round 4 correction to §3.1: the timezone code above measures the offset separately for each symbol. As my Round 4 review showed, that lets a stale quote change the offset, which then makes the stale quote look fresh. Calibrate a single offset for the whole account instead:

Take the newest time_msc across at least 3 symbols that trade around the clock.
Fail closed if the result is more than 120 s from a 30-minute step.
Always subtract that offset, for every symbol.

End of Part 2 of 3. Reply "continue" for Part 3 (§5–§8: codebase health, wiring, risk of ruin and verification).

---

Part 3 of 3 (§5–§8) is below, exactly as written in Round 3. With it, Parts 1–3 make up the complete file.

markdown
## 5. Codebase health

### 5.1 `copilot_studio_bridge.py`
- **Fabricated state on failure.** If MT5 import or initialisation fails, the prompt reports the hard-coded `balance = equity = 4896.55` as live. **Fail closed:** abort the cycle or label it `STATE_UNAVAILABLE`.
- `"(100% Cash Reserves | 0.00 Margin Used)"` is a literal string, printed even with open positions.
- `r_multiple` has no direction sign, so it is wrong for shorts.
- Section 3 of the prompt still teaches the **Z-routed** dual engine with RSI 30/70, not the regime router. The LLM is being asked to apply rules the code is moving away from.
- It asks the LLM for "Top 2 Candidate Orders … Lots, Risk USD". Make the output **advisory JSON only** (`{asset, direction, thesis, invalidation}`), never prices or lots. Any candidate must be re-derived by `decision_gates_v3` from raw data.
- Response scraping keys on hashed CSS classes (`___1frxvlh`, …), which break on any UI deploy. It also does a single check after a fixed `sleep(180)`.
- Appending raw LLM text into `LIVE_COLLABORATIVE_ORDER_DESK.md`, which agents read and act on, is a prompt-injection path into order authority.

### 5.2 Parameter drift (single source of truth needed)
| Parameter | Values found |
|---|---|
| Max risk/trade (USD) | 14.50 (protocol G6, ACTIVE_CONTEXT §3) · 15 (`live_admission.py`, **binding**) · 15 "house money" (AGENTS P2) · 20 (`floor_defense.py`, `Omni_Trader._risk_cap`, ACTIVE_CONTEXT §2 launch flag) · 45 (`OF_Strategy.py` default `--max-risk`) |
| Max concurrent | 2 (AGENTS P2, §9.1) · 4 (everywhere else) |
| Phase 0 stop | +0.15R (AGENTS, `ratchet_manager.py`) · +0.35R (ACTIVE_CONTEXT §3) · net +0.50 USD (protocol G7) |
| Phase 1 / target | 1.5R / 2.5R (most) · 1.8R / ≥ 3.0R (AGENTS §9.1) · TP floor 1.5R + friction (`structural_exit`) |
| Friction | 41 bps on notional (AGENTS P7, Pioneer) vs broker-valued per symbol (Round 2) |
| Universe | 11 Binance perps (ACTIVE_CONTEXT §2) · 18 (AGENTS P2) · 24 CFDs (verifier, bridge) |
| Floor-check equity base | `min(balance, equity)` (`live_admission`) · `balance` (`floor_defense.can_admit`, verifier) |
| Unknown cluster | reject (`live_admission`) · **allow** (`floor_defense._cluster_check`) |

Create `Terminal/policy.py` with one frozen dataclass. Import it everywhere, and have a test fail if any module defines its own constant.

### 5.3 `live_admission.py` (Round 1 fixes reviewed)
- **Correct:** the USD-leg mapping for USD pairs; the floor uses `min(balance, equity)` plus 1.25× stress plus 2 USD.
- **Gap 1, non-USD crosses.** Crosses (EURGBP, EURJPY …) are mapped to "short USD" for longs, which is wrong. Map each pair to a two-currency vector, e.g. long EURJPY = +EUR, −JPY. Block when any single currency's summed signed exposure exceeds one position's worth.
- **Gap 2, "natural hedge" is not a hedge.** Long EURUSD + long USDJPY is USD-flat but **long EURJPY**. Both legs lose together on a JPY shock, such as the intervention risk flagged in Round 1. The floor math still reserves both stops, so solvency is fine, but the correlation guard should treat this as a JPY concentration.
- **Gap 3, cross-cluster risk-on.** Long SP500 + long USDJPY + long BTC passes. Add a beta-to-risk-on check: the sum of signed betas from the Ledoit–Wolf covariance already loaded in `OF_Strategy.py`.

### 5.4 `chain_verification_360.py`
- `anti_lookahead_causal_verified`, `vwap_reset_verified` (L2) and `positions_in_sync` (telemetry) are initialised `True` and never tested.
- **ATR and RSI** use simple means of the last 14 values, not Wilder. They will not match `Candle_Indicator_Engine`, and the module never compares them anyway, so "Z-score parity" is unverified.
- **Timestamps:** the session-VWAP day mask and parquet recency use the `time` column, which is **broker time**. Use `utc_time`, which `Candle_Indicator_Engine` writes. Broker time ahead of UTC makes `hours_old` negative, which weakens the staleness test by 2–3 h.
- **Tick staleness:** MT5 tick staleness compares `tick.time` (broker time) to UTC, which is negative, so it never fires.
- **Telemetry key:** it reads `data.get("assets")`, but the exporter writes `assets_matrix_24`. Unless both keys exist, `assets_serialized` is always 0.
- **Floor math:**
  - Uses `balance`, not `min(balance, equity)`.
  - Credits locked profit (`net -= locked_cash`) against other tickets' risk.
  - Has no 1.25× stress.
  - It is a third floor calculator that disagrees with `live_admission`. Make the verifier call `assert_joint_fill_safe`'s math instead of reimplementing it.
- Treat the certificate as a smoke test until these are fixed. Rename the top verdict to `SMOKE_PASS`.

### 5.5 Operational governance
- **Unproven backtest claims.** `ACTIVE_CONTEXT.md` §2 states "20/20 profitable OOS regimes, 19,480 trades, +330,766.70 USD, 10/10 certification". That works out to **+16.98 USD per trade** at a 10–20 USD risk budget, i.e. about +1R average expectancy with 59.3% wins. Live trading shows nothing like that. Until it is reproduced from raw parquet with live-parity frictions, it should not be quoted as a fact in agent context, where it biases every agent towards confidence.
- **Remove the AGENTS.md proof-of-compliance banner** and the mandates for multi-persona headers and skill-loading headers. They spend tokens and attention on ritual rather than on the checks above.

---

## 6. Wiring `decision_gates_v3` into the live loop

**Step 0, shadow mode (1–2 weeks, no veto power).** In `Omni_Trader.evaluate_market` (≈ L773, where `classify_sleeve` runs):
```python
from Terminal import decision_gates_v3 as dg
h1 = self.bridge.get_recent_bars(symbol, count=60, timeframe=mt5.TIMEFRAME_H1)   # UTC-normalised
h4 = self.bridge.get_recent_bars(symbol, count=40, timeframe=mt5.TIMEFRAME_H4)
m15 = self.bridge.get_recent_bars(symbol, count=120)
regime, rstats = dg.classify_regime([b["close"] for b in m15], [b["close"] for b in h1], [b["close"] for b in h4])
ctx = build_ctx(features, payload, pivots, quote, regime)          # one pure function, unit-tested
verdict = (dg.model2_checklist if regime.startswith("TREND") else
           dg.model1_checklist if regime == "MEAN_REVERT" else None)
features["dg_v3"] = {"regime": regime, "stats": rstats,
                     "passed": bool(verdict and verdict(ctx).passed),
                     "failures": verdict(ctx).failures if verdict else ["REGIME_UNDEFINED"]}
```
Journal `features["dg_v3"]` into `decisions.jsonl` next to the current decision.

**Step 1, enforce.** After the shadow comparison, raise `ValueError("dg_v3:" + "|".join(failures))` when the check fails. Change the L784–790 branch so `UNVERIFIED_NO_TAPE` raises for Model 1 and tags `variant=price_only` for Model 2 (risk × 0.5, `min_risk_usd = 5`).

**Step 2, governor.** In `Order_Persistence_Governor.heartbeat`, before the drift guard, call `dg.resting_order_invalidation(order, metrics)`. Store `ttl_minutes` **at registration**. Replace `except Exception: pass` with cancel-and-journal.

**Step 3, pre-send.** In `Omni_Trader._dispatch` (≈ L1135), call `dg.pre_send_gate(mt5, req, plan)` with an offset-corrected `utc_now_ms` immediately before `stage_limit_order`. Fail → `HOLD_VALIDATION`.

**Step 4, Copilot bridge.** Make it advisory-only: a structured JSON ruling, schema-validated, and stored in `docs/trade_plans/` as data. Allow no code path from the ruling to `stage_limit_order` except through `evaluate_market`.

**Step 5, tests.**
- Golden-file tests for every checklist failure code.
- DST test (GMT+2/+3).
- Raw-spread (median 0) test.
- `price_only` admission test (7.25 USD admitted).
- Regime classifier null-rate test on stored random-walk fixtures (UNDEFINED ≥ 85%).
- Ledger reconciliation test: `history_deals_get` from account inception, where Σ(profit + commission + swap + fee) must equal `balance − initial deposit`.

---

## 7. Risk of ruin at current cushion
Operating-buffer room is 4,896.55 − 4,795.00 = **101.55 USD**. Bootstrapping the 17 listed trades:
- **If the observed edge is real**, P(touch buffer) = 0.002 / 0.004 / 0.004 within 25 / 50 / 100 trades.
- **If the edge is zero** (same dispersion, mean removed), P = **0.151 / 0.312 / 0.479**.

Seventeen trades can't distinguish these cases (Wilson 95% on win rate: [0.413, 0.827]). Size for the zero-edge case until about 170 trades have accumulated. One way: cap risk at 10 USD while the buffer is < 150 USD, which roughly halves the zero-edge ruin probability by doubling the number of losses needed.

---

## 8. Verification performed this round
- Read at `a2a9fd70`: `decision_gates_v3.py`, `live_admission.py`, `floor_defense.py`, `chain_verification_360.py`, `copilot_studio_bridge.py`, `MT5_Execution_Bridge.py`, `OF_Strategy.py`, `Omni_Trader.py` (grep plus the L330–338, L780–805 and L1095–1150 sections), `ACTIVE_CONTEXT.md`, `AGENTS.md`, the protocol spec, the Round 2 report, and the newest session-history entry.
- Simulations: component null rates (iid and GARCH-t, n = 48/30), the classifier under six data-generating processes, BM touch probabilities, the raw-spread cancel, the DST normalisation, the ledger sum, and the bootstrap ruin.
- **Not verified:**
  - Blueberry's actual server-time convention and DST date. Confirm with `symbol_info_tick().time_msc − utc_now` today and after Nov 1.
  - How agents physically submit "punched" orders.
  - The 405-test pytest claim.
  - Classifier behaviour on real parquet data (§1.2 last bullet).


End of Part 3 of 3: the report is now complete. To rebuild the file, join Parts 1, 2 and 3 in order. It should come to about 27.5 KB. Replace docs/reviews/ROUND3_OPUS55_AUDIT_REPORT.md with it; that file currently holds my chat summary, not the report.

Where the Round 4 review supersedes this report:

§3.1 (timezone): use one offset for the whole account, calibrated from at least 3 symbols that trade around the clock. Fail closed if the offset is more than 120 s from a 30-minute step, and always subtract it.
§6 Step 0: the code snippet runs verdict(ctx) twice. Assign the result once.
§6 wiring: also require a dg_verdict token inside bridge.stage_limit_order. Otherwise orders placed by agents or the LLM bypass the gates.
§0 status:
#1 is partly fixed in ee3ade9a.
#2–#5 are still open, and the Round 2 report in the repo is also still truncated.