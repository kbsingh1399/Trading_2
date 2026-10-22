# CoinGlass Large Orderbook Whale Orders Per-Asset Reconciliation Artifact

- **Harvest Timestamp UTC**: `2026-10-17T08:15:03.014017+00:00`
- **Harvest Epoch**: `1792224903.0140493`
- **Schema Version**: `1.0.0`
- **Arithmetic Exact Match**: `True`

---

## 1. Top-Level Metrics & Verification

| Metric | Recorded Value | Sum of Per-Asset Breakdown | Difference | Verified |
|---|---|---|---|---|
| **Total Queried Assets** | 18 | 18 | 0 | True |
| **DOM Extracted Assets** | 18 | 18 | 0 | True |
| **Price Rejected Assets** | 4 | 4 | 0 | True |
| **Ingested Assets** | 14 | 14 | 0 | True |
| **Total Whale Orders** | 508 | 508 | 0 | True |
| **Grand Total Notional USD** | 216,728,410.00 USD | 216,728,410.00 USD | 0.00 USD | True |

---

## 2. Exhaustive Per-Asset Reconciliation Breakdown (All 18 Institutional Assets)

| # | Asset | Status | Notional (USD) | Orders | Buys | Sells | Detail / Rejection Reason |
|---|---|---|---|---|---|---|---|
| 1 | **BTC** | `INGESTED` | 87,130,000.00 USD | 39 | 20 | 19 |  |
| 2 | **ETH** | `INGESTED` | 54,284,690.00 USD | 39 | 22 | 17 |  |
| 3 | **SOL** | `INGESTED` | 27,464,110.00 USD | 39 | 20 | 19 |  |
| 4 | **BNB** | `INGESTED` | 5,702,720.00 USD | 39 | 20 | 19 |  |
| 5 | **DOGE** | `INGESTED` | 4,800,390.00 USD | 39 | 21 | 18 |  |
| 6 | **XRP** | `INGESTED` | 3,933,690.00 USD | 39 | 17 | 22 |  |
| 7 | **ADA** | `INGESTED` | 4,039,710.00 USD | 39 | 20 | 19 |  |
| 8 | **LINK** | `INGESTED` | 4,812,120.00 USD | 39 | 20 | 19 |  |
| 9 | **AVAX** | `INGESTED` | 3,617,330.00 USD | 39 | 16 | 23 |  |
| 10 | **SUI** | `INGESTED` | 6,777,630.00 USD | 39 | 20 | 19 |  |
| 11 | **NEAR** | `INGESTED` | 3,850,490.00 USD | 39 | 20 | 19 |  |
| 12 | **DOT** | `PRICE_SANITY_REJECTED` | 0.00 USD | 0 | 0 | 0 | DYNAMIC_PRICE_SANITY: Median price 1.6000 deviates by 38.0% ... |
| 13 | **LTC** | `INGESTED` | 5,483,240.00 USD | 39 | 14 | 25 |  |
| 14 | **BCH** | `INGESTED` | 3,118,990.00 USD | 28 | 14 | 14 |  |
| 15 | **APT** | `PRICE_SANITY_REJECTED` | 0.00 USD | 0 | 0 | 0 | STATIC_PRICE_SANITY: Median price 0.77 is outside [1.0, 150.... |
| 16 | **OP** | `INGESTED` | 1,713,300.00 USD | 12 | 4 | 8 |  |
| 17 | **ARB** | `PRICE_SANITY_REJECTED` | 0.00 USD | 0 | 0 | 0 | DYNAMIC_PRICE_SANITY: Median price 0.2500 deviates by 32.8% ... |
| 18 | **TRX** | `PRICE_SANITY_REJECTED` | 0.00 USD | 0 | 0 | 0 | DYNAMIC_PRICE_SANITY: Median price 0.4000 deviates by 19.2% ... |

---

## 3. Reconciliation Equations & Mathematical Invariants

1. Total Queried Identity:
   18 = 14 (ingested) + 4 (price-rejected) + 0 (unilateral)
2. Grand Total Notional Identity:
   216,728,410.00 USD == 216,728,410.00 USD (0.00 USD Difference)
3. Total Order Count Identity:
   508 == 508 (0 Orders Difference)