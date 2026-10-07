# Observed-only telemetry and Hyperdash probe

**Status:** the Git snapshot is a delayed, read-only receipt, not an MT5 order-authorisation feed. The `as_of_utc`/`as_of_epoch` are the original broker snapshot time; Git commit time is merely publication time. Check age before any decision. These changes do not place broker orders.

## What is and is not observed

| Field | Scope / unit | Live policy |
|---|---|---|
| Account, positions, pending orders, bid/ask and execution specifications | MT5 broker, account/symbol specific | Only from the connected bridge. Unknown values are null; no bar-close quote or assumed 4-bp spread. Tick age, if supplied, is exposed. An old JSON is not a current account readback. |
| Candles, EMA/RSI/ATR, VWAP/profile | Derived from actual completed MT5 bars; broker-reported bar volume may be tick count, **not base-asset traded volume** | Insufficient, stale, or volume-less bars make affected fields null. Derived indicators are not exchange stop orders. |
| Top-20 bids/asks and large price levels | Binance USD-M Futures anonymous aggregated **L2** | Observed price/quantity samples, sampled receipt time and venue. `l2_wall_levels` are not wallet orders or uninterrupted wall persistence. Legacy `whale_walls_l3` is empty. Binance is a different venue from MT5/Hyperliquid. |
| Open interest | Binance Futures public REST, contract quantity | Kept separately with venue/time when available. OI cannot reveal leverage, liquidation locations or stop orders. |
| Forced liquidations | Binance `@forceOrder` websocket (Data Factory only) | Already-executed, sampled events in `realized_liquidation_events`; **not** current resting liquidation exposure. The standalone minute JSON has no recorded force-order stream and reports resting exposure unavailable. |
| Wallet positions/stop triggers | Hyperliquid public `clearinghouseState`/`frontendOpenOrders` in the local Chrome Terminal | Only sampled addresses (currently at most two), exchange-reported position liq price and explicitly reduce-only stop trigger orders; fresh receipt and named provider required by scoring. Not all wallets or all stops. A reported liquidation *price* is projected risk, not an observed future forced fill. |
| Hyperdash order rows | Existing `orderbookSnapshotFiltered` GraphQL query in `Api_Client.py` | Address-attributed filtered **snapshot**, no order ID/event stream; neither proof of full matching-engine L3 nor uninterrupted persistence. Anonymous Binance L2 must never be merged into it. |
| Hyperdash `stopOrderLevelsV2` / `liquidationLevelsV2` | Existing GraphQL queries return `historicalData.totalAmount` bands and totals (`size` in reported base-asset units) | Marked `UNVERIFIED_*_LANDSCAPE`. The GraphQL response can be real while the platform's aggregation/coverage/methodology is unverified; do not call bars native hidden stops or realized forced liquidations and **never** use them as observed execution corridors. Missing query data is unavailable, not zero. The Chrome Terminal leaves chart `bands` empty and exposes provider-returned levels separately as `unverified_raw_bands`; it does not multiply an unverified unit into purported USD or reconstruct trader PnL/leverage from chart levels. `/api/heatmap` returns `UNAVAILABLE_UNVERIFIED_ANALYTICS` instead of displaying the research engine's carried-forward historical amounts as live USD. This deliberately hides the old stop/liquidation heatmap until a verifiable unit and coverage contract is established. |
| Stop/liquidation research reconstruction | `StopClusterEngine`, `LiquidationReconstructionEngine` | Retained only for separate research as `MODEL_*`, never in live snapshots or execution evidence. No artificial prior OI sample, assumed taker ratio or leverage tier is published as live exposure. |
| Coinbase premium | Coinbase BTC-USD spot vs Binance BTCUSDT spot | Null if either observation fails; Binance-only mark/index spread is **not** a Coinbase premium. |

The minute snapshot protocol is `omni.telemetry.v3.observed_only`; absent stop/liquidation bands are empty with `source: UNAVAILABLE`, monetary totals null, and `trade_authorization: DENIED_UNVERIFIED_ORDERFLOW`. The Data Factory also emits empty/unavailable stop, projected-liquidation and unattributed sampler whale-position blocks; only the separately attested Chrome Terminal Hyperliquid wallet sample may count as observed wallet risk. `Risk_Sizing_Engine` verifies named Hyperliquid provider, wallet coverage, freshness and **point-trigger prices** before including sampled stops; it never spreads one observed trigger across an invented price corridor. A relevant trigger outside the sampled L2 book or absent coverage yields `ffr: null`, `coverage_missing: true` and an entry veto, not neutral fuel. `Pioneer_Decision_Engine` does not score reconstructed liquidations; its unverified walls/whales cannot support an entry. Existing positions/exits remain independently managed.

## Hyperdash API exploration and local validation

The repository contains three GraphQL calls: `orderbookSnapshotFiltered`, `stopOrderLevelsV2`, `liquidationLevelsV2` (`Terminal/Api_Client.py`). The first returns address + side/price/quantity **without an order ID**; the latter two return platform aggregates with historical samples and top addresses. The API host/schema and screenshot-equivalent results could **not** be live-verified in this Arena sandbox (outbound access is restricted); offline mock tests only validate parsing, error handling and provenance. Do not claim the screenshot's 59.75 BTC / 176.62 BTC stops, 212.34 BTC / 481.44 BTC liquidations or 223 address-labelled orders are reproduced here. Screenshots do not by themselves attest how Hyperdash derives aggregates.

On a locally network-enabled machine, run `python scripts/probe_hyperdash.py BTC`. It performs read-only L2 and GraphQL calls, prints query errors, receipt time, band historical sample time, sample rows, provider and coverage. If an endpoint fails or is rate-limited, it reports `UNAVAILABLE` instead of making up values. Verify BTC coin/contract mapping, HTTP access, returned band units and sample timestamps against Hyperdash before any optional use; the script never executes or changes an order. Do **not** put API credentials in Git or this chat.

## Deploy / pull

On the local machine that runs the MT5 telemetry daemon, pull **the session branch**:

```bash
git fetch origin arena/83d03e3f-trading-2
git switch arena/83d03e3f-trading-2
git pull --ff-only origin arena/83d03e3f-trading-2
python -m pytest -q Tests/
python scripts/probe_hyperdash.py BTC  # optional; only if Hyperdash is reachable
```

Restart the local minute daemon after pulling so it reloads the observed-only producer. Its Git publisher rejects v2/model-backed or stale telemetry and only pushes to this Arena branch. Verify new `docs/telemetry/live_snapshot_latest.json` has protocol v3 and a recent `as_of_utc`; if MT5 is disconnected, no new account snapshot should be published. The tracked snapshot may have been sanitized from an older observation pending the local restart; `snapshot_status` flags that historical state. Do not mistake a Git push for a new MT5 readback.
