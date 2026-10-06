# OMNI Pioneer Decision Engine — Continuous Real-Time Cross-Validated Conviction
**Prompt:** OX_ALPHA_59 follow-up ("keep improving till we have pioneer engine to make trading decisions")
**Date:** 2026-10-06 · **Branch:** `arena/4adf3661-trading-2`
**Baseline:** 225 tests passed / 4 pre-existing environment failures (was 200; +25 new, zero regressions)

This consultation upgrades the zero-cost data factory from a *library you can call* into a
*continuously-running, self-checking conviction system*, and fuses its new data points into
the existing decision architecture — without touching a single risk invariant.

---

## 1. What was delivered

| Component | File | Purpose |
|---|---|---|
| **CrossSourceValidator** | `Terminal/Data_Factory/crosscheck.py` | The pillars become each other's oracles: cross-venue mid agreement, Binance↔Hyperliquid OI agreement, synthetic-model-vs-empirical-prints calibration, optional legacy-vendor parity, per-pillar freshness — all distilled into one **sealed, deterministic quality score** |
| **RealtimeRunner** | `Terminal/Data_Factory/live.py` | The always-on heartbeat: OI polling from every source (300 s), whale-cohort sampling (60 s), completed bars (900 s), Fear & Greed (1 h), Farside ETF flows (6 h), watchdog quality report (30 s) — jittered, failure-isolated, with pillar health/stall streaks exposed via `status()` |
| **PioneerDecisionEngine** | `Terminal/Pioneer_Decision_Engine.py` | The conviction layer: five deterministic signals (orderflow / cascade / stops / whales / macro) fused into one bounded conviction with a 41-bps friction floor, fail-closed gates and a SHA-256 chained digest |
| Factory whale + orderflow block | `Terminal/Data_Factory/factory.py` | `ingest_whale_positions` (HL public `/info` cohort — the exact `Api_Client.fetch_wallet_risk` positions schema, $0), `ingest_whale_flow` (on-chain transfers), payload now carries `whale_positions`, `whale_net_flow_usd_24h` and the live bus `orderflow` snapshot (CVD 1m/5m/15m, taker imbalance, spread) |
| Omni hook | `Terminal/Omni_Trader.py` | `attach_pioneer()` + a **veto-only** consult after the confluence gate: quality floor, stale book, blackout or opposed conviction suppress a NEW entry; nothing else changes |

## 2. Continuous real-time operation (the "always updating" mandate)

```python
from Terminal.Data_Factory import (ZeroCostDataFactory, CrossSourceValidator,
                                   RealtimeRunner, LivePolicy)

factory   = ZeroCostDataFactory(["BTC", "ETH", "SOL", "GOLD"])
validator = CrossSourceValidator(factory)          # records every OI source
runner    = RealtimeRunner(factory, validator,
                           transports={("BINANCE", "SOL"): binance_connect, ...},
                           oi_pollers={"BINANCE": binance_oi, "HYPERLIQUID": hl_oi},
                           whale_sampler=hl_cohort_sampler,     # tracked addresses
                           bar_provider=bridge.get_recent_bars)
asyncio.run(runner.run(assets))                    # Ctrl-C / stop() to end
```

Every loop is failure-isolated (one dead poller never stops the others), every cadence is
jittered ±10 % (no thundering herd into rate-limited endpoints), and the watchdog seals a
quality report every 30 s. `runner.status()` answers "is everything alive?" per pillar with
`last_success`, age and stall streaks — and `runner.quality_history` keeps the last 64
sealed reports so degradation is auditable, never silent.

**Honest degradation is a feature:** in the offline tests, with no live feeds, the quality
score falls from 1.0 to exactly 0.0 as the book goes stale — the system would rather say
"my data is old" than fabricate freshness (tested).

## 3. Cross-source comparison ("compare with other data sources")

| Check | Oracle pair | Scoring |
|---|---|---|
| Mid agreement | Binance vs Coinbase vs Hyperliquid last trades (60 s window) | ≤10 bps pass · ≤50 bps half · >50 bps fail (weight .25) |
| OI agreement | Binance `fapi` OI vs Hyperliquid `metaAndAssetCtxs` (30 min window) | ≤35 % relative disagreement passes |
| **Liquidation calibration** | **synthetic ΔOI-cohort bands vs REAL `@forceOrder` prints** | hit-rate: share of realized forced-liquidation USD landing within ±50 bps of the bands the model ranked hot; requires ≥5 prints / ≥250 k USD to opine, else honestly `available: False` |
| Stop-model parity | synthetic structural stops vs the legacy Hyperdash feed (`Api_Client.fetch_stops`) | optional, best-effort, **recorded not scored** — vendor availability is intermittent; ratio within [⅓, 3] passes |
| Freshness | every pillar vs its max age | book 30 s · trades 180 s · OI 1800 s |

The calibration check is the one that closes the loop on Q1B: the synthetic model is now
**scored against reality every 30 seconds**. If realized liquidation fuel keeps landing
where the model said the density was, `hit_rate` stays high; if it drifts, the quality
score — and therefore the pioneer conviction — decays automatically. Model risk is a
measured quantity, not an assumption.

## 4. The Pioneer conviction layer

Five signals, each a bounded deterministic transform of live factory data, each carrying
its full numeric basis in the advisory (nothing is fabricated):

| Signal | Weight | Inputs | Direction convention |
|---|---|---|---|
| `orderflow` | 0.30 | bus CVD 1m/5m/15m sign-agreement (weights .2/.3/.5) + 15 m taker imbalance | buying pressure → + |
| `cascade` | 0.25 | synthetic liquidation fuel asymmetry within 5 % of mid, proximity-discounted | heavy SHORT fuel above (squeeze) → + |
| `stops` | 0.15 | structural stop-cluster asymmetry (sell stops below vs buy stops above) | heavier pool is the magnet |
| `whale` | 0.15 | sampled HL cohort net positioning (60 %) + 24 h net exchange flow (40 %) | whales net long / outflow → + |
| `macro` | 0.15 | ETF net flow (40 %) + Coinbase premium (40 %) + F&G contrarian-at-extremes (20 %) | inflows + premium → + |

$$\text{conviction} = \underbrace{\frac{\sum_k w_k s_k}{\sum_k w_k}}_{\text{unavailable signals drop out}} \times \underbrace{q}_{\text{live quality}} \in [-1, 1]$$

- **Advice:** `SUPPORT_LONG` (≥ +0.25) · `NEUTRAL` · `SUPPORT_SHORT` (≤ −0.25).
- **Friction floor:** every advisory carries `min_favorable_move_bps = 41 + 5 (slip) + live spread` — a conviction that cannot pay its own round trip is noise by construction.
- **Fail-closed gates (ABSTAIN):** no mid · book older than 30 s · macro blackout · quality < 0.60.
- **Tamper-evidence:** each advisory is SHA-256 chained per asset (`prev_digest | canonical json`), same discipline as the feature seals — the cognitive layer can only ever attest against a verifiable vector.

### 4.1 Integration semantics — veto-only, by construction

Inside `evaluate_market`, immediately after the confluence gate:

```python
if self.pioneer is not None:
    advisory = self.pioneer.evaluate(asset, payload, features, macro, now)
    if not advisory.get("tradeable"):
        raise ValueError(f"pioneer_veto:{advisory.get('reason')}")
    features["pioneer"] = {conviction, advice, min_favorable_move_bps, quality_score, digest}
```

A `raise` here is the same path every existing veto takes (coverage, FFR, confluence,
basis dislocation): it suppresses **new entries only**. The pioneer can never:
- size a trade (RiskPolicy 10–45 USD untouched),
- force or extend a position (2-filled / 5-resting caps untouched),
- delay an exit (manage_active_positions never consults it),
- touch the 4,775 floor or the drawdown latch.

When the pioneer is absent (`pioneer=None`, the default), the trader is bit-for-bit
unchanged — asserted by test against the proven T1-breakout fixture.

## 5. Test suite — `Tests/Test_Pioneer_Decision_Engine.py` (25 tests, 100 % offline)

- **Crosscheck (6):** divergence detection & scoring; two-source OI agreement
  (8 % passes, 60 % fails); calibration hit-rate (prints inside the modeled corridor
  hit, prints in cold bands miss, thin samples honestly unavailable); stale-book
  fail-closed; deterministic sealed digests; legacy-vendor parity within ratio.
- **Runner (5):** every OI source polled at cadence (primary feeds the cohort model,
  both feed the agreement check); whale cohort lands in the payload; macro refresh +
  watchdog quality history; jitter-free determinism (two identical runs → identical
  stats and digest); honest quality degradation to 0.0 with no live feeds.
- **Pioneer (12):** each gate and signal in isolation; weight renormalization;
  quality discount scaling; advice thresholds; friction floor ≥ 41 bps + spread;
  digest chaining + determinism; end-to-end over `features_from_factory`.
- **Omni integration (2):** the proven PAPER_FILLED fixture — baseline fills,
  low-quality pioneer vetoes (`pioneer_veto:quality_below_floor`), opposed conviction
  vetoes, passing pioneer leaves sizing identical; and no-pioneer bit-for-bit equality.

The runner tests run the **full concurrent schedule on a discrete-event virtual clock**
(concurrent sleeps overlap like wall time) in ~1 second of real time — no network, no
waiting, deterministic to the digest.

## 6. File map

| File | Status |
|---|---|
| `Terminal/Data_Factory/crosscheck.py` | new (~250 lines) |
| `Terminal/Data_Factory/live.py` | new (~230 lines) |
| `Terminal/Pioneer_Decision_Engine.py` | new (~250 lines) |
| `Terminal/Data_Factory/factory.py` | + whale ingestion, orderflow/whale payload blocks |
| `Terminal/Data_Factory/__init__.py` | + exports |
| `Terminal/Omni_Trader.py` | + `attach_pioneer`, veto-only consult |
| `Tests/Test_Pioneer_Decision_Engine.py` | new, 25 tests |

## 7. Standing invariants (all preserved, all re-tested)

5,000 USD capital · **4,775 hard floor** · 10–45 USD risk · **≥41 bps friction** in every
payoff/advisory floor · 2 filled / 5 resting under first-fill OCO · sealed deterministic
vectors only (pioneer advisories are SHA-256 chained) · cognitive layer advisory · legacy
candle-only backtest still not treated as validation.

## 8. Bottom line

- Every data point now **refreshes continuously** on a jittered, failure-isolated
  schedule with a 30-second sealed quality heartbeat.
- The data sources now **check each other**: venues against venues, OI against OI, and —
  the decisive one — the synthetic liquidation model against real forced-liquidation
  prints, with optional parity against the legacy vendor it replaced.
- The decision architecture gains a **pioneer conviction layer**: five live signals,
  quality-discounted, friction-floored, fail-closed, tamper-evident — and wired so it
  can only ever *refuse* a new entry, never create or resize risk.
