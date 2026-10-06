# OMNI Zero-Cost Data Factory — Architectural Consultation
**Prompt:** OX_ALPHA_59_DATA_FACTORY · **Date:** 2026-10-06
**Branch:** `arena/4adf3661-trading-2` · **Baseline:** 200 tests passed / 4 pre-existing environment failures (was 155 before this delivery; +45 new, zero regressions)
**Cost replicated:** CoinGlass ($29–500/mo) + Hyperdash GraphQL dependency + Arkham ($1,000s/mo) → **$0.00/mo**

---

## 0. Repository audit performed (as instructed)

| Module | What was verified | Consequence for the design |
|---|---|---|
| `Terminal/Api_Client.py` L350–450, L544–591 | Hyperdash GraphQL `GetStopOrderLevelsV2`/`GetLiquidationLevelsV2`; `fetch_wallet_risk` samples ≤2 whale addresses via HL `/info` `clearinghouseState` + `frontendOpenOrders`, emitting `PROJECTED_EXPOSURE` / `OBSERVED_STOP_ORDERS` bands | The factory must emit the **exact band schema** (`min_px`, `max_px`, `mid_px`, `amount_usd`, `position_side_at_risk`) and `sources.*.observed_at` receipt stamps — it does |
| `Terminal/Chrome_Terminal.py` L85–278, L340–405 | `/api/live/{coin}` payload assembly: l2_book, recent_trades (`side` = aggressor), l3_orders walls, cumulative stop/liq curves | `factory.payload()` reproduces this payload contract 1:1 |
| `Terminal/Asset_Universe.py` | 14-asset canonical universe, broker aliases | Factory is universe-agnostic; maps `binance_symbol/coinbase_product/hyperliquid_coin` per asset |
| `Terminal/Market_Intelligence.py` | Fail-closed macro calendar (`CALENDAR_UNAVAILABLE` → blackout), keyword sentiment, ±15-min gates | Factory enrichment is **additive** (`attach_data_factory`); the blackout path is untouched |
| `Terminal/Risk_Sizing_Engine.py` L109–300 | `OrderflowModel.features` staleness gates (book ≤ `max_book_age`, component as-of ≤ 60 s), band corridor matching, FAFR denominator | Factory payloads flow through the same gates; synthetic blocks carry explicit `coverage` markers and can never masquerade as observed data |
| `Terminal/Candle_Indicator_Engine.py` | **Not present on this branch** (exists only in your local paste) | Q4-style causal candle ingestion was delivered in the prior consultation as `Terminal/Causal_Candle_Stream.py`; the factory consumes completed bars the same way |

---

## 1. Question 1A — can the raw public venues replace Hyperdash for free?

**Short answer: liquidations — yes, exactly; stops — no, and no one else can see them either.** The honest decomposition:

### 1A.1 What Hyperliquid gives you for free, keyless, today

| Endpoint | Channel/body | What it yields |
|---|---|---|
| `wss://api.hyperliquid.xyz/ws` | `l2Book` | Full resting book per coin — every limit level with px/sz/**n** (order count). This *is* the whale-wall data (`l3_orders` in your pipeline is derived from exactly this) |
| `wss://…` | `trades`, `allMids` | Trade tape + mids for all 288 perpetuals |
| `POST /info` `{"type":"clearinghouseState","user":<addr>}` | REST | **Per-account positions with `liquidationPx`, entry, leverage, size for ANY address** — on-chain, public, permanent |
| `POST /info` `{"type":"frontendOpenOrders","user":<addr>}` | REST | Open orders incl. **trigger (`isTrigger`) reduce-only stop orders with `triggerPx`** for any address |
| `POST /info` `metaAndAssetCtxs` | REST | OI, mark, funding, day volume per coin |

**The critical asymmetry:** your current `fetch_wallet_risk` already uses `clearinghouseState`/`frontendOpenOrders` — but only for ≤2 addresses sampled from L3 whale walls. That is the *only* free, exact source of stop-loss orders anywhere: **stops are exchange-held conditional orders, invisible in the book and not on-chain** (Hyperliquid stops live in the exchange's trigger engine, not the smart contract). CoinGlass/Hyperdash do not see "all stops" either — they aggregate the same public per-account queries over whale-watchlists plus synthetic models. The correct free replication is therefore:

1. **Exact, for whales you track:** query `clearinghouseState` + `frontendOpenOrders` for your tracked whale cohort (the factory's `LabelRegistry` + `WhaleTransferListener` grow that cohort automatically from on-chain flows). This is a *lower bound*, exactly as your current code labels it (`coverage: SAMPLED_WALLETS`).
2. **Exact, for realized liquidations:** Binance `@forceOrder` WebSocket (real-time forced prints, keyless) + Binance Data Vision `liquidationSnapshot` archives (history).
3. **Synthetic, for the market-wide landscape:** the Q1B model below. This is what the heatmap vendors actually sell; it is reproducible locally.

**Vendor-decoupling fix included:** `Terminal/Data_Factory/factory.py` emits the identical payload schema, so `Omni_Trader(fetcher=...)` can switch from the Chrome_Terminal HTTP hop to the factory with **one constructor argument** (§5.3) — no Hyperdash GraphQL in the hot path, no IP-blacklist single point of failure.

### 1A.2 What no venue gives (and never will)

- Resting stops of *untracked* accounts (nowhere public — by design, they'd be front-run).
- Cross-exchange liquidation aggregates in one call (must be composed; the factory composes Binance + Hyperliquid + synthetic tiers).

---

## 2. Question 1B — the mathematical reconstruction (Pillar 3 core)

### 2.1 Liquidation levels from leverage arithmetic

For a position entered at $P_0$ with leverage $L$ and maintenance-margin rate $m(L)$:

$$P_{\text{liq,long}} = P_0\left(1 - \tfrac{1}{L} + m\right), \qquad P_{\text{liq,short}} = P_0\left(1 + \tfrac{1}{L} - m\right)$$

Validity condition (enforced in `liq_price`): $\tfrac{1}{L} > m$ — otherwise the tier is unreachable and the model refuses to emit an inverted level. Defaults: weights `{10x:.35, 25x:.40, 50x:.20, 100x:.05}`, `mmr = {10x:.004, 25x:.005, 50x:.010, 100x:.008}` (all configurable; calibrate per-venue from their published tier tables).

Worked check (unit-tested): 100× long from 100, m=0.004 → **99.40**; 10× short from 100, m=0.004 → **109.60**.

### 2.2 Cohort construction from ΔOI conditioned on price intervals

Open interest is the only public aggregate that tracks *aggregate position notional*. The engine treats each OI sample as a cohort ledger:

- **ΔOI > 0** during bar $t$ (price $P_t$): open a cohort of notional ΔOI at entry $P_t$, split long/short by the bar's **aggressive tape ratio** (from the live taker flow on the bus; 50/50 when unknown): `buy_share = taker_buy_usd/(taker_buy_usd+taker_sell_usd)`.
- **ΔOI < 0**: unwind the oldest cohorts FIFO (positions closed), removing long and short notional pro-rata.
- Each cohort then fans out over the leverage tiers → a liquidation ladder per cohort → aggregated into **25 bps geometric price bands** (band $k$ spans $[1.0025^k, 1.0025^{k+1}]$), each tagged `position_side_at_risk` LONG (below current price) or SHORT (above).

This is the same construction CoinGlass sells as its heatmap: an OI-vs-price-entry distribution convolved with a leverage kernel. Your `XAUUSD`/CFD assets have no OI feed — for those, the band comes out empty (honest) and the structural stop model (§2.4) still applies.

### 2.3 Hazard decay: density is consumed, not static

A corridor that the tape has already traded through has spent its fuel. Remaining density per band:

$$D_{\text{remaining}} = D_0 \cdot \underbrace{e^{-\Delta t/\tau}}_{\text{time}} \cdot \underbrace{e^{-V_{\text{corridor}}/(\kappa \cdot D_0)}}_{\text{volume}}, \quad \tau = 72\,\text{h},\ \kappa = 3$$

where $V_{\text{corridor}}$ is cumulative traded notional in the band **and its two adjacent bands** (25 bps each side). Empirical `@forceOrder` prints additionally *deplete* cohort notional directly (a realized liquidation cannot liquidate twice) and build an independent empirical histogram (`empirical_bands`). Both are unit-tested: time decay halves density at τ; 50 M USD traded through a ~1 M corridor drains it to dust.

### 2.4 Stop-loss clusters from structure (swings × ATR × profile × round numbers)

`StopClusterEngine` reconstructs resting stop clusters — the Hyperdash "Stops" tab — from four structural priors, each weighted by recency ($0.5^{\text{age}/48\text{bars}}$) and local volume:

1. **Fractal swing pivots** (k=2 confirmed): longs' stops rest just *under* swing lows (`L − 0.05·ATR`), shorts' just *over* swing highs.
2. **ATR multiples** (1.0/1.5/2.0 × ATR(14)) offset from each swing — measured stop placement.
3. **Volume-profile anchors**: stops beyond POC/VAH/VAL (from the factory's tick histogram or bars).
4. **Round numbers** within 10% of mid (psychological levels).

Hard side rule (enforced): sell stops only **below** current mid, buy stops only **above** — a candidate on the wrong side is already-triggered history. Output is the `OBSERVED_STOP_ORDERS` schema with `coverage: SYNTHETIC_STRUCTURAL_MODEL` so downstream never mistakes it for observed orders.

### 2.5 Liquidation Max Pain

For current price $P$ and target $p$: forced notional $F(p) = \sum_{\text{long bands } p \le m < P} D_m + \sum_{\text{short bands } P < m \le p} D_m$. Max pain is the argmax over band mids — the price a cascade would find "easiest" (unit-tested: long-heavy OI → DOWN max pain below the long wall).

### 2.6 FAFR — Friction-Adjusted Fuel Ratio (local, not vendor)

$$\text{FAFR}(p) = \frac{F(p)}{\text{notional} \times 41\,\text{bps}/10^4}$$

Fuel toward the target divided by our own ≥41 bps round-trip friction (your invariant). ≥1 means the forced-flow the move triggers pays for our execution. This complements the corridor-depth FAFR already inside `OrderflowModel.features` (which uses *visible depth* rather than synthetic fuel — both remain, explicitly labeled).

---

## 3. The six pillars — what was delivered

**Package `Terminal/Data_Factory/`** (new, ~1,900 lines) + additive hooks in `Risk_Sizing_Engine` / `Market_Intelligence`:

| Pillar | Module | Contents |
|---|---|---|
| 1. CEX streams | `streams.py` | Pure parsers: Binance `@trade`/`@depth20@100ms`/`@forceOrder`; Coinbase `matches` (maker-side flip) + `level2_batch` assembler (snapshot/update/delete); Hyperliquid `l2Book`/`trades`/`allMids`. `ReconnectingWebsocket`: exponential backoff 1→60 s with jitter, heartbeat keep-alive, stall detection (90 s silent → reconnect), graceful stop; `websockets` imported lazily so offline hosts run everything else |
| 2. Bulk archives | `bulk.py` | `data.binance.vision` daily/monthly URL builders (aggTrades/klines/funding/liquidationSnapshot, spot+UM), SHA-256 `CHECKSUM` verification, in-memory zip→CSV parse (buyer-maker semantics), strict monotonic-ms + zero-null validation, idempotent atomic parquet append (unique on `ts_ms`), gap audit; free OI pollers (Binance `/fapi/v1/openInterest`, HL `metaAndAssetCtxs`) |
| 3. Liqs & stops | `liquidation_engine.py` | Everything in §2: `liq_price` (with tier-validity guard), OI cohort ledger with taker-ratio splits + FIFO unwind, 25 bps band aggregation, time×volume hazard decay, empirical `@forceOrder` depletion + histogram, `max_pain`, `fafr`, `StopClusterEngine` (swings/ATR/POC/round numbers, side-enforced) |
| 4. On-chain whales | `onchain.py` | `WhaleTransferListener`: ERC-20 `Transfer` (`eth_getLogs`, canonical topic) + native-ETH block scans, ≥500 k USD threshold, entity-aware direction bucketing (`EXCHANGE_INFLOW`/`OUTFLOW`/`INTERNAL`/`WHALE_TO_WHALE`); `LabelRegistry`: bundled institutional seed + Dune Spellbook CSV/URL loaders; `BigQueryWhaleForensics`: SQL builders over `bigquery-public-data.crypto_ethereum` (whale transfers, counterparty frequency, exchange sweeps) + row parser, lazy `google-cloud-bigquery` |
| 5. Macro & ETF | `macro.py` | Farside BTC/ETH ETF flow table parser (chronological, per-fund + totals, sign-correct), `net_flow`/`streak`; `alternative.me` Fear & Greed with cache; **Coinbase Premium** `(P_cb − P_bin)/P_bin × 10⁴` bps computed live from the two venue mids on the bus; standalone fail-closed blackout helper mirroring `Market_Intelligence` semantics |
| 6. Bus & bridge | `bus.py`, `factory.py` | `IntelligenceBus`: per-asset 1,024-event ring buffers, per-venue monotonicity enforcement (violations counted & refused, never reordered), rolling CVD/taker windows (1 m/5 m/15 m), footprint tick ladder, depth imbalance, SHA-256 **chained** snapshot seals (deterministic + tamper-evident). `ZeroCostDataFactory`: ingest API, `_WallTracker` (depth→persistent 150 k+ wall clusters with first/last-seen spans feeding `OrderflowModel.observe_walls`), full trader-contract `payload()`, `payload_fetcher()` for `Omni_Trader`, `max_pain`/`fafr`/`macro_snapshot`, async `run()` over **injectable transports** |

**Resilience guarantees (all tested):** backoff reconnect after socket death and after 90 s stalls; heartbeat keep-alive sends; torn/corrupt frames skipped; per-venue timestamp regressions refused; stale books fail closed inside `features`; future-stamped ticks never enter a payload (zero lookahead).

**Sub-millisecond reads (tested):** with 1,024 live ticks, mean CVD + taker-flow + footprint query latency < 1 ms — the 15-minute loop pays nothing for the factory.

---

## 4. Test suite — `Tests/Test_Zero_Cost_Data_Factory.py` (45 tests, 100% offline)

Every network surface is injected: recorded WS frames, fake sockets that die and reconnect, fabricated RPC logs, Farside HTML fixtures, in-memory zips with real SHA-256 checksums, fake BigQuery rows.

- **Bus (7):** capacity eviction; 4-thread parallel-writer safety; per-venue monotonicity refusal; CVD/taker windows; footprint + depth imbalance; seal determinism + chain linkage + tamper evidence; **mean read latency < 1 ms**.
- **Streams (6):** Binance trade aggressor semantics (`m` flag), depth zero-level drops, forceOrder side mapping (forced SELL = long liquidated); Coinbase maker-side flip + level2 update/delete; Hyperliquid book/trades/mids + subscription shape; reconnect-with-backoff on stall, clean stop.
- **Liquidation engine (8):** exact liq-price arithmetic incl. invalid-tier guard; cohort split by taker ratio; FIFO unwind; `PROJECTED_EXPOSURE` schema with LONG-below/SHORT-above sides; time+volume hazard drain; forced-print depletion + empirical histogram; max-pain direction + cascade; FAFR at 41 bps.
- **Stops (3):** fractal pivots; side-correct structural bands; ATR-multiple offsets from the swing.
- **Bulk (4):** canonical URLs; zip/parse/validate/checksum roundtrip with failure modes; idempotent parquet sync + gap audit; OI parsers.
- **On-chain (5):** topic/uint decoding; whale threshold + entity direction bucketing; native block scan; Spellbook CSV loader; BigQuery SQL builders + row filtering.
- **Macro (4):** Farside parse + net flow + streak; FNG parse/cache; premium math + live index; fail-closed blackout.
- **Factory & integration (8):** full payload contract (`coin/price/l2_book/recent_trades/l3_orders/projected_liquidations/observed_stops/sources`); future-tick exclusion (zero lookahead); `payload_fetcher` gate; **`OrderflowModel.features_from_factory` end-to-end** (deterministic features from factory payloads, friction ≥ 41 bps preserved); stale-book fail-closed; `Market_Intelligence` report enrichment; async `run()` over fake transports ingesting live frames into the bus; sealed snapshots.

**Suite state:** 155 → **200 passed**; the same 4 pre-existing environment failures (msvcrt lock, MetaTrader5 import, 2 UI fixtures) — unchanged since the first consultation.

---

## 5. Integration guide (branch `arena/4adf3661-trading-2`)

### 5.1 What is already wired (this delivery, additive only)

**`Risk_Sizing_Engine.OrderflowModel.features_from_factory(factory, asset, bars, macro, as_of)`** — builds the payload from the factory and runs the *identical* deterministic feature pipeline: same staleness gates, same corridor matching, same ≥41 bps friction, same robust z-scores. Synthetic coverage markers flow through, so nothing synthetic is ever mistaken for observed.

**`Market_IntelligenceEngine.attach_data_factory(factory)`** — `get_market_intelligence_report()` gains a `data_factory` block (Coinbase premium bps, Fear & Greed, ETF net flows). The blackout gate and sentiment scoring are untouched; enrichment failures degrade to `{"error": ...}` and never block the report.

### 5.2 Swapping the trader's feed source (one argument)

```python
from Terminal.Data_Factory import ZeroCostDataFactory
factory = ZeroCostDataFactory(assets)          # start streams in a background task
trader = AI15mMT5Trader(bridge=..., intel=..., ...,
                        fetcher=factory.payload_fetcher())   # was Chrome_Terminal HTTP
intel.attach_data_factory(factory)
```

`payload_fetcher()` raises `ValueError("no_book_yet:…")` before the first book snapshot — the existing `feed_errors.jsonl` path handles it exactly like a dead Chrome_Terminal. **Risk invariants are untouched**: sizing, covariance, the 4,775 floor, 2-filled/5-resting gates and the governor all sit downstream of the payload contract and are indifferent to its origin.

### 5.3 Production runbook

1. `pip install websockets polars` (streaming + parquet; everything else is stdlib/numpy). Optional: `google-cloud-bigquery` for Pillar-4 batch forensics.
2. Launch the factory once per machine (it is single-writer per bus asset; multiple consumers read freely):
   ```python
   asyncio.run(factory.run(assets=["BTC","ETH","SOL","GOLD"], oi_poller=binance_oi_poller))
   ```
   Backfill history separately: `DataVisionDownloader(root="Data/Ticks").sync_agg_trades("SOLUSDT", daily=False, date="2026-09")`.
3. Seed `LabelRegistry` from the Spellbook (`load_spellbook_csv`) and verify the seed addresses before trusting entity attribution; unlabeled whale flows remain anonymous-but-real.
4. Optional: build the 90-day footprint from Data Vision aggTrades, then let the live stream extend it (`bus.footprint`).

### 5.4 Deployment cautions

- Binance depth frames are top-20 snapshots; wall *persistence* spans come from the factory's own `_WallTracker` (first/last-seen), matching `observe_walls` semantics — do not mix the two persistence notions.
- Hyperliquid `clearinghouseState` is rate-limited per IP: poll your tracked cohort (≤ dozens of addresses) on a ≥30 s cadence, not per-tick.
- The synthetic liquidation model is a **density estimate, not an order book**: it feeds the same pressure/corridor math as before, but its `coverage` marker must never be stripped — `Risk_Sizing_Engine` relies on it for honest labelling.
- Coinbase `level2_batch` needs a `snapshot` before updates; the assembler returns `None` until then (fail-closed).

---

## 6. File map

| File | Status | Lines |
|---|---|---|
| `Terminal/Data_Factory/__init__.py` | new | public API surface |
| `Terminal/Data_Factory/bus.py` | new | ~270 |
| `Terminal/Data_Factory/streams.py` | new | ~300 |
| `Terminal/Data_Factory/liquidation_engine.py` | new | ~330 |
| `Terminal/Data_Factory/bulk.py` | new | ~240 |
| `Terminal/Data_Factory/onchain.py` | new | ~230 |
| `Terminal/Data_Factory/macro.py` | new | ~190 |
| `Terminal/Data_Factory/factory.py` | new | ~330 |
| `Terminal/Risk_Sizing_Engine.py` | +`features_from_factory` | additive |
| `Terminal/Market_Intelligence.py` | +`attach_data_factory` | additive |
| `Tests/Test_Zero_Cost_Data_Factory.py` | new | 45 tests |

**Standing invariants preserved:** 5,000 USD capital · 4,775 hard floor · 10–45 USD risk · ≥41 bps friction in all payoff math · 2 filled / 5 resting under first-fill OCO · sealed deterministic features only · cognitive layer advisory.

## 7. Bottom line

- **Q1A:** Hyperliquid's public `/info` + WS gives *exact* per-address liquidation prices and trigger-stop orders for any whale you track, and Binance `@forceOrder` gives *exact* realized liquidations — both free and keyless. Market-wide *resting* stops are unobservable everywhere (including to CoinGlass); vendors sell reconstructions, and the reconstruction is now yours.
- **Q1B:** Implemented end-to-end (§2): ΔOI cohorts × leverage tiers × maintenance margin → 25 bps liquidation density with time×volume hazard decay, depleted by empirical prints; structural stops from swings×ATR×POC×round numbers; Max Pain and 41-bps FAFR as first-class analytics.
- **Cost:** $0.00/month, no API keys, no third-party GraphQL in the hot path, every feed surface injectable and offline-tested, 45 new tests, 200 total green.
