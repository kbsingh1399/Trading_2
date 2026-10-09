# Round 2 audit: decision-making thinking chain and pre-trade gates
**Repo:** `kbsingh1399/Trading_2` @ `8ea1a01` · **Date:** 2026-10-09 · **Companion code:** `decision_gates_v3.py` (tested, see §9)

> **How to read the numbers.** Every threshold in this document is a **prior**, not a calibrated value. The book has 17 closed trades (11W/6L). The 95% Wilson interval on the win rate is **[0.413, 0.827]**. Detecting a +0.2R edge with a 1.3R per-trade standard deviation at t = 2 takes about **169 trades**. Treat these thresholds as starting points for walk-forward and shadow-fill calibration (§8), not as proven parameters.

---

## 0. Executive verdict

This round found three architectural defects. Each is bigger than any single parameter:

1. **Gate 3 picks the engine using the Z-score. It should pick the engine by regime first.**
   - Your session-VWAP Z cannot tell continuation from exhaustion, because Z saturates in a steady trend:
     - On a linear price ramp, the Z of the last bar converges to √3 ≈ 1.73. Measured: n = 8 → 1.53, n = 32 → 1.68, n = 96 → 1.71.
     - With strong drift (drift/σ = 3 per bar), P(|Z| ≥ 2) = **0.000**.
     - With no drift at all, P(|Z| ≥ 2) = **0.11–0.15**.
     - A convex (accelerating) path reaches Z = 2.18 (x²) and 2.55 (x³).
   - Consequences:
     - |Z| ≥ 2 selects noise excursions **and accelerating cascades**. That is Model 1's knife-catch failure mode (EURUSD, BTC, and WTI at Z = −2.80 on 10-07).
     - A steady trend almost always sits at |Z| ≈ 1.6–1.7. It gets routed to Model 2 even when price is at the extreme, with no pullback.
   - `scan_vwap_opportunities()` defaults to `z_threshold=1.75`. That is just above the linear-trend asymptote, so steady trends get flagged as "EXTREME" on about 35–40% of bars (drift/σ = 1: P(|Z| ≥ 1.75) = 0.35–0.37).
2. **Pillars 2–4 cannot be observed for most of the universe.**
   - `generate_telemetry_snapshot.py` emits `cvd_1m_buckets`, HTF 4H/D1 bars and funding **only for `CRYPTO_ASSETS`**. VWAP weights are `MT5_TICK_VOLUME_PROXY_NOT_EXCHANGE_CONTRACTS`.
   - The Pioneer `_signal_cascade` always returns `unavailable`, and `Terminal/stop_clusters.py`, cited as data source #8, does not exist at this commit.
   - So for FX, indices, gold and oil, the "all 5 pillars" rule can only be met by narrative. That is exactly the heuristic optimism you want to remove.
   - `taker_delta_exhaustion()` returns `UNVERIFIED_NO_TAPE`, and its docstring says "the trader passes with a marker". That **fails open**.
3. **The "queue priority" model does not apply to MT5 CFDs.**
   - A Blueberry buy limit fills when the broker Ask touches it; there is no FIFO queue to lose. Protocol rebuttal #4 ("deleting forfeits queue priority") is therefore invalid on MT5.
   - Cancel cost is about zero, so the invalidation logic should lean towards cancelling.
   - Binance walls sit on a different venue. They are **information about where price may hold**, not slippage protection for a CFD fill.

### Code-level defects found this round (all verified in source)

| # | File | Defect | Effect |
|---|---|---|---|
| D1 | `signals/wall_tracker.py::_cluster_price` | Cluster grid size = `mark*bps/1e4`, so the key changes whenever the mark moves. A static wall at 83,000 got keys 83002.9 / 83011.2 / 83019.5 for mark moves of 0 / 1 / 2 bps. | Persistence resets on almost every tick. The 180 s rule is effectively unreachable in a moving market. Anchor the grid to a fixed tick multiple. |
| D2 | `wall_tracker.update` | The `>= 150k` filter is applied **per level before clustering**, and a second level in the same cluster **overwrites** (`refresh`) the first instead of summing. | Contradicts the docstring ("Aggregate walls within 10 bps"). Under-counts walls. |
| D3 | `Adverse_Selection.observe/hazard` | Each snapshot sums trades from the last 60 s. A 12-snapshot window at about 5 s polls counts each trade up to about 11 times. | Cancel-to-trade ratio (CTR) is deflated about 10×. The `ctr_max=2.5` alarm effectively needs removal ≥ 25–30× traded, so it is almost never armed. Sum only trades with `ts > previous snapshot ts`. |
| D4 | `Adverse_Selection` | "Defending depth" = the whole top-20 side, not depth within ±0.5 ATR of the limit. Aggressor share uses only the last snapshot. | Measures the touch, not the level being defended. |
| D5 | `Order_Persistence_Governor.heartbeat` step 4 | `except Exception: pass` around the adverse-selection monitor. | Fails open. A monitor crash leaves the order resting. It should cancel or flag. |
| D6 | Governor vs spec | Spec: 2.0× ATR drift, >50% thinning. Code: 1.5×/3.0× ATR, `pull_ratio=0.40` (cancels only after >60% thinning). | Parameter drift between spec and production. |
| D7 | `risk/ratchet_manager.py` | Phase 0 = fixed entry + 0.15R (spec: invert broker PnL to +0.50 USD net). Phase 2 = static entry + 1.5R (spec: trail the 15m EMA20). Time decay uses wall-clock, so weekends count as bars. | A "breakeven" stop that is not net breakeven. A Friday position can be force-closed into the Monday gap. |
| D8 | `risk/live_admission.py` | `MAX_RISK_USD = 15.0` (spec 14.50). Slots count tickets, so a BE position still uses a slot even though spec says BE "recirculates" capacity. The correlation guard is same-cluster and same-direction only (USDJPY long + SP500 long risk-on passes). | Spec and code disagree on capacity. Cross-cluster correlation is not guarded. |
| D9 | `Orderbook_Structure.structural_exit` | Allows a hurdle down to `1.5R + friction`. Spec Gate 6 says ≥ 2.0R. | Spec drift. |
| D10 | Telemetry `trend_status` | `ema_200_slope >= 0` → BULLISH. A flat slope counts as a trend, and there is no chop state. | Feeds Model 2 in chop. |
| D11 | `Candle_Indicator_Engine` | Session sigma is the volume-weighted dispersion of the **current session's** bars (reset 00:00 UTC, minimum 8 bars). It is small early in the session, so Z inflates. | Z is not comparable across hours of the day. Hence A1 below requires `session_bars ≥ 16` and `σ_session ≥ 0.8·ATR`. |
| D12 | Protocol rubric | Spread scoring covers ≤5 bps (10 pts), 5–15 (5 pts) and >20 (veto); **15–20 bps is undefined.** | Ambiguous scoring. |
| D13 | Pioneer | `friction_bps = 41` for every asset. | Over-penalises FX (~1–3 bps) and under-penalises illiquid alts. Use per-symbol broker-valued cost. |

---

## 1. Revised thinking chain

```
G0  DATA PROVENANCE      fail-closed: tick ≤2 s, L2 ≤10 s (crypto), bars ≤30 min, no nulls
G1  FLOOR CUSHION        (unchanged; live_admission.assert_joint_fill_safe)
G2  CAPACITY + CORRELATION   slots + cross-cluster beta guard (D8)
G3  REGIME ROUTER        TREND_UP | TREND_DOWN | MEAN_REVERT | UNDEFINED  ← NEW ORDER
        TREND_*      → Model 2 only (Z is a location descriptor)
        MEAN_REVERT  → Model 1 only (Z ≥ 2 is a stretch signal)
        UNDEFINED    → STAND ASIDE (both engines)
G4  ENGINE CHECKLIST     Checklist A or B (§2/§3), asset-class evidence map (§1.4)
G5  NET EV               p_lower_CI ≥ p_breakeven + 0.03 (per-symbol friction)
G6  STRUCTURAL TP        first obstacle − buffer; RR floor per engine
G7  STAGING + INVALIDATION MONITOR (§1.1)
G8  PRE-SEND MILLISECOND GATE (§4.3)
G9  LIFECYCLE            hold / cut / BE decided by the drift estimate (§4.2)
```

Two rules for the LLM council:

- **Every checklist line must carry a number and its source field.**
- **A field reported as `UNAVAILABLE` cannot be satisfied by argument.** It either fails closed or switches to the documented price-only variant, which runs at half risk and needs its own backtest.

### 1.1 Invalidation architecture (resting limits)

Because MT5 has no queue (§1.3), cancelling is close to free. The asymmetry is: a wrong cancel costs one missed fill, while a wrong keep costs a full −1R plus stop slippage.

**Rule:**

- Any **HARD** event cancels immediately.
- **Two or more SOFT** events cancel.
- Every cancel is kept as a **shadow order** (virtual limit) so you can measure its counterfactual outcome (§8).

| Class | Event | Formula / threshold | Data |
|---|---|---|---|
| HARD | Regime flip | `classify_regime()` ≠ regime at staging | All |
| HARD | Counter-structure before fill | Long: a new 15m lower low **and** a lower high formed before touching the shelf | All |
| HARD | **Fast approach** (most important) | `v = −s·ln(P_t/P_{t−3}) / (σ_bar·√3) > 2.0` while `0 ≤ dist ≤ 1 ATR` | All |
| HARD | Drift | `s·(mid − L) > 2.0·ATR` | All |
| HARD | Diffusion TTL | `minutes > 2·(dist/σ_bar,price)²·15` (first-passage scale) | All |
| HARD | Context | Macro window, or spread > 2.5× median for the hour of week | All |
| HARD | Primary wall pulled | Retained < 50% **and** the wall was the main thesis | Crypto |
| HARD | Liquidation cascade toward limit | Forced-liq notional in the trade direction over the last 1m ≥ 3× the 24h median 1m **and** rising | Crypto |
| SOFT | Aggressor pressure | Taker share toward the level over 5m ≥ 0.65 | Crypto |
| SOFT | No absorption | Kyle-λ ratio `λ_5m / median λ_60m ≥ 1.5`, where `λ = |Δln P| / |CVD$|` | Crypto |
| SOFT | Depth thinning **near the limit** | Bid depth within ±0.5 ATR of L falls ≥ 50% over 3 min | Crypto |
| SOFT | Value migration | Developing POC moves ≥ 0.5 ATR through L | All (tick-volume POC) |
| SOFT | Broker/reference divergence | `|mid_MT5 − mid_Binance| > max(15 bps, 3× median basis)` | Crypto CFDs |

**Why fast approach is HARD.** On a touch-fill venue, the fill is conditioned on price reaching your level. Fills that arrive after an impulsive approach are the ones most likely to keep going through you; this is the adverse-selection term. Validate it with the markout split by approach-speed bucket (§1.3).

Implementation: `resting_order_invalidation()`, `diffusion_ttl_minutes()`.

### 1.2 True pullback vs. exhaustion rollover

Normalising by volatility only sets the scale. To tell the two cases apart you need to **compare the pullback leg with the impulse leg, and HTF persistence with LTF**.

Let the impulse run from anchor `A` to extreme `E` over `n_i` bars, and the pullback from `E` to the current price `P` over `n_p` bars. `σ_bar` is the Yang-Zhang per-bar log volatility.

| Test | Healthy pullback | Exhaustion / reversal |
|---|---|---|
| Retrace fraction `|E−P|/|E−A|` | 0.236–0.618 | > 0.618 (structure damaged) |
| Depth speed `ln(E/P)/(σ_bar·√n_p)` | ≤ 2.0 | > 2.0 (impulsive counter-move) |
| Velocity ratio `(ln(E/P)/n_p) / (ln(E/A)/n_i)` | ≤ 0.60 | ≥ 1.0 |
| 15m structure | Higher low intact (P > HL − 0.2 ATR) | HL broken on close |
| 1H/4H persistence | ER_1H > 0.35, VR z* > 1, HAC t > 2.5 (≥2 of 3), 4H agrees | ER_1H falling from > 0.5 to < 0.3 over 16 bars |
| Thrust | Last impulse ≥ 0.7× the previous impulse (σ units) | Last impulse < 0.7× the previous (momentum divergence) |
| EMA20–EMA50 spread / ATR | Stable or widening | Compressing for ≥ 6 bars |
| CVD (crypto) | New price high confirmed by a new CVD high; pullback CVD share ≤ 50% of impulse CVD | Price higher high, CVD lower high |
| OI (crypto) | Price up, OI up (new longs) | Price up, OI down (short-covering rally) |
| Funding (crypto) | Not in the top 5% of 30-day history | Extreme crowding |

**Exhaustion score** = count of the right-hand column flags among {thrust, ER-roll, EMA compression, CVD divergence, OI divergence, funding}. Model 2 requires **≤ 1**.

Do **not** require the 15m to be trending. During a pullback it is counter-trend by construction, which is why the router measures the trend on 1H/4H.

### 1.3 Adverse selection on MT5 CFDs: proving the edge

On a CLOB, edge comes partly from queue position. On MT5 it can only come from **post-fill drift**. The proof is statistical, measured per fill `i` (side `s_i`, fill price `p_i`, broker mid `m`):

```
Markout_i(Δ) = s_i · (m(t_i+Δ) − p_i) / p_i · 1e4      Δ ∈ {5s, 60s, 300s, 900s}
Edge proven   ⇔ mean(Markout(900s)) − friction_bps > 0  with t ≥ 2
Toxic fills   ⇔ mean(Markout(5s..60s)) significantly < 0 (t ≤ −2)
Stale-quote pick-off (crypto CFDs):
     Lag_i = s_i · (mid_Binance(t_i) − p_i)/p_i · 1e4 ;  pick-off if Lag_i < −5 bps
     Track frac(pick-off); require < 10%.
Conditional tests (decide the invalidation rules):
     Markout(900s) split by approach-speed bucket {<1σ, 1–2σ, >2σ}
     Markout(900s) split by wall present / absent, CVD exhausted / not
Stop-side asymmetry: mean slippage on SL fills vs. on TP/limit fills
```

`markout_report()` implements this. With 200 synthetic fills, it correctly flags both `toxic=True` (5s t = −7.99) and `edge_proven=True` (900s t = +4.10). The two conditions can co-exist: short-horizon adverse selection can still be outweighed by longer-horizon drift.

### 1.4 Evidence availability by asset class

| Evidence | Crypto CFDs | FX / indices / metals / oil CFDs |
|---|---|---|
| Taker CVD, λ, absorption | Binance 1m buckets | **Unavailable.** MT5 tick volume is quote updates, not aggressor flow. |
| L2 walls | Binance (other venue, informational) | **Unavailable** |
| Forced liquidations / OI / funding | Binance | **Unavailable** |
| VWAP / POC | Tick-volume proxy | Tick-volume proxy |
| Regime, YZ vol, structure | MT5 bars (+ Binance HTF) | MT5 bars; fetch H1/H4 natively via `copy_rates_from_pos` |

**Policy for non-crypto:** run the **price-only variant**:
- Checklist with orderflow lines replaced by stricter structure lines (reclaim close, thrust divergence).
- **50% risk**.
- Separate PnL attribution.
- Promote only after its own shadow sample.

---

## 2. Checklist A: Model 1, extreme mean reversion

`model1_checklist()`. ALL lines are mandatory; `s = +1` for long, −1 for short.

### A1. Regime and VWAP geometry
- [ ] `regime == MEAN_REVERT`: ER_1H < 0.20, ER_4H < 0.30, VR(4) z*_15m < −1.5. **No Model 1 in TREND_* or UNDEFINED.**
- [ ] `2.0 ≤ −s·Z ≤ 3.5` (beyond 3.5 is cascade territory: stand aside).
- [ ] `session_bars ≥ 16` and `σ_session ≥ 0.8·ATR_15m` (prevents early-session Z inflation, D11).
- [ ] VWAP slope `|ΔVWAP over 8 bars| / (8·σ_session) ≤ 0.05` per bar (flat value).
- [ ] **Z deceleration:** `−s·(Z_t − Z_{t−4}) ≤ 0.75`. Z rising more than 0.75σ in 4 bars means acceleration.
- [ ] Vol shock: `σ_YZ(4 bars) / σ_YZ(96 bars) ≤ 2.0`.

### A2. Orderflow absorption (crypto; otherwise fail closed or use the price-only variant)
- [ ] **Two-push CVD divergence:** price makes a lower low (longs) while `|CVD_push2| ≤ 0.70·|CVD_push1|`. Each push is measured from swing to swing on 1m buckets.
- [ ] **Aggression present:** taker sell $ in the sweep window ≥ 2× the median 1m taker sell $ over 60 min.
- [ ] **Absorption (passive bid soaking up aggression):** `λ_sweep / median λ_60m ≤ 0.50`, where `λ = |Δln P| / |CVD$|`. This is your requested "aggressor selling into passive bid" ratio, expressed as price impact per dollar.
- [ ] **CVD turned:** ≥ 3 consecutive 1m buckets with `s·CVD ≥ 0`, plus `taker_delta_exhaustion().ok == True`.

### A3. Opposing resting wall (informational; Binance)
- [
