Cycle_037 — inline audit and ruling

Source cut: GitHub main at cd95960ba566e59c4e3fd88b2e727f433a10c447 (committed 14:56:30 UTC), using the 92 individual master dossiers. This is repository evidence—not live MT5 verification. No broker action or Z.ai/Tri-Council vote occurred; no sidecar was created.

Ruling first

If BTC #19532055 and AVE #19532058 are still pending at the broker, cancel both; do not replace them or stage the ETH idea now. If either has filled, reconcile the broker history first rather than treating it as a pending order.

The later repository registry, synced at 14:38:30 UTC, reports equity $4,755.23, 0 positions, 2 pending orders, and $14.10 contingent risk. That equity is $19.77 below the canonical SOP’s $4,775 hard floor; the SOP requires zero open/pending risk at or below it. It is also $39.77 below the $4,795 operating threshold. The envelope’s hard_floor_usd: 0 / new_risk_admissible: true override conflicts with the canonical SOP and is not policy authorization.

I cannot verify or perform the cancellations: the Cycle_037 certificate path returned 404, there are no execution receipts for these two ticket IDs, and the repository registry is not a live broker connection.

15-pillar evidence review

The figures below are from the pinned dossiers and repository records. Flow, funding and OI rows are generally timestamped around 14:28–14:32 UTC; the task timestamp is 14:57 UTC. A reported 4.2 ms pipeline latency is not proof that every upstream feed—or the account inventory—is current.

Solvency and risk lock. The registry’s $4,755.23 equity is below the SOP floor; its two pending tickets carry $14.10 reported risk. No new risk is admissible under the canonical rule.

Cycle integrity, freshness and receipts. The envelope and checklist remain Cycle_036 (envelope cutoff 14:12:17 UTC); the registry is later but still 19 minutes old at the task time. The account snapshot is older still and lists different tickets. The Cycle_037 certificate is absent, and receipts for #19532055/#19532058 are missing. Reconcile broker history before any new order.

Broker specifications and nominal risk.

BTC: dossier contract size 1.0; 0.01 lot × 500 points = $5 nominal risk for the registered stop.
AVE: dossier contract size is 1.0, while the registry’s $9.10 risk implies 100. At the dossier size, 0.07 × $1.30 × 1.0 = $0.091; at 100, it is $9.10. This is unresolved without broker-spec/OrderCalcProfit verification.
ETH: dossier contract size 1.0; the proposed 0.10 lot × $40 stop = $4 nominal risk, on that dossier assumption.

Spread and permitted execution. The dossiers permit passive limits. BTC is 5.46 bps / 25 bps threshold; ETH 15.27 / 25; AVE 24.72 / 25. AVE passes by only 0.28 bps. These are dossier gates, not a live quote check.

Macro, calendar and news. The calendar rows are dated Oct 25–27, not an up-to-date Oct 30 event schedule. The news feed includes generic items and some timestamp inconsistencies. I cannot use it to certify a current catalyst embargo—or a clean catalyst window—for these trades.

ETF flows. BTC’s ten-row ETF table has only one numeric daily net-flow entry, −$15.3M; the others are blank. It does not substantiate a broader positive-flow claim. ETH and AVE dossiers carry the same Bitcoin ETF table, so it is not valid ETH/AAVE flow evidence.

Spot netflows. BTC reports −$862.78M/24h and −$1.58B/30d; ETH −$142.68M/24h and −$3.24B/30d. AVE’s spot-netflow field is empty. I’m reporting the signs as published; the dossier does not establish the sign convention well enough to infer direction from them.

Futures netflows. BTC reports −$3.07B/24h and −$10.25B/30d; ETH −$2.06B and −$9.88B; AVE −$9.61M and −$89.51M. These are not clean confirmations for adding risk.

Funding and settlement. BTC funding is at or near +0.010% on most listed venues; its settlement row reports +$1.71M current and +$3.60M/24h. ETH funding is mixed around zero; settlement is −$202.59K current but +$195.10K/24h. AVE funding is mostly negative on linear venues, while the CoinM Binance row is +0.0302%; settlement is −$14.57K current and +$2.40K/24h.

Open interest and long/short positioning. BTC OI is $53.52B, −1.36%/24h and +1.11%/4h; ETH $28.38B, −6.47%/24h and −0.38%/4h. AVE has no OI row. BTC and ETH long/short rows show 1% long / 50% short / 0.02 ratio / zero volume across horizons—internally unusable, not a positioning signal. AVE’s ratio ladder is absent.

Liquidation and forced-liquidation feeds. BTC heatmap reports $24.98M/1h, $32.46M/4h and $559.41M/24h; the forced-liquidation ladder records $23,860 of shorts purged over 14:30–14:45 UTC. ETH reports $7.73M/1h, $11.50M/4h and $369.51M/24h, with no forced-liquidation rows. AVE has $4.85M/24h only; shorter heatmap horizons and forced-liquidation rows are absent.

Max-pain levels. Current dossier values are BTC long/short $76,045.48 / $79,868.95, ETH $2,174.37 / $2,275.30, and AVE $116.52 / $128.80. The BTC long value differs from the prompt’s $76,195.42 by $149.94; I use the pinned dossier value.

Stop-cluster geometry. BTC has a “HIGH” sell-stop cluster at $76,050; the ticket’s $75,850 stop is itself a tactical sell-stop rung ($2.71M reported). The 1D liquidation ladder shows cumulative long liquidation of $890.42M at $75,824; the 7D ladder shows $854.04M at $75,820—only $26–30 below the ticket stop. ETH has a high sell-stop rung at $2,175 ($8.98M) and a lower rung at $2,135 ($315K); the proposed $2,130 stop is only $5 below the latter, about 0.40 ATR. Its 1D cumulative liquidation ladder is also dense around $2,131.6–$2,129.2, so I cannot certify that stop as clear of the band. AVE has no HD stop or exchange-liquidation ladder.

Whales, order book and cross-venue positioning. BTC has 22 whale rows and 41 book rows, concentrated around $76,974–$77,024—not at its entry or stop; the book’s coins scale also does not reconcile with the whale rows. ETH has 33/41 rows around $2,226.7–$2,230.8, well above the proposed entry. AVE has no local whale or book rows. The dossiers report a $178.1M BTC Hyperliquid short, a $227.9M ETH short (reported profit $10.55M), and a $5.40M AVE long (reported profit $2.05M); these rows are not a substitute for verified, level-local resting depth or persistence.

CVD, footprint, technicals, auction and order construction.

BTC ticket: mid $76,888; RSI 35.32; ATR $308.59; VWAP $77,518.66; daily VAH/POC/VAL $78,376.24/$77,180.56/$76,639.12. The buy limit at $76,350 is below VAL and just $38 above the reported 24h low ($76,312). Its registered $76,350/$75,850/$77,600 levels calculate to 2.50R / $5. CVD is bullish across the last 5m/15m/1h/4h rows (+19.7/+16.7/+7.6/+4.1%), but that conflicts with the negative flow rows; the stop-map evidence is mixed.
AVE ticket: mid $125.385; RSI 48.84; ATR $1.058; VWAP $122.885; daily VAH/POC/VAL $127.07/$124.84/$120.73. Entry $122.50 is $1.77 above VAL; stop $121.20 is still $0.47 above VAL and $4.68 above long max pain. The registered levels calculate to 2.50R, but the dossier model is STAND_ASIDE_MONITOR (82); CVD is empty, the book/whale rows are empty, and the risk/specification conflict remains.
ETH proposal: mid $2,226.70; RSI 42.59; ATR $12.382; VWAP $2,221.55; daily VAH/POC/VAL $2,246.61/$2,224.76/$2,200.48, with a rotational/bearish session label. The proposed BUY_LIMIT $2,170 / SL $2,130 / TP $2,270 / 0.10 lot calculates to $4 nominal risk and 2.50R. Entry is $4.37 below long max pain and $2.30 above the 24h low; TP is $5.30 below short max pain. Short-term CVD is positive (+38.2%/5m, +28.9%/15m, +8.8%/1h), but 4h is slightly negative (−0.55%). Footprint exhaustion/absorption signals are at $2,215/$2,240—not at the proposed $2,170 entry. The model’s own $2,200.48/$2,180.52/$2,250.38 setup is different; its stop is above long max pain, so its “armed” label is not validation of this plan.
92-asset search and ETH assessment

The exact 92-file scan at the pinned commit finds 91 PASS and one SPREAD_DISQUALIFIED: XRP at 32.31 bps versus a 25 bps threshold. The universe count is inconsistent: the envelope says 93, while the aggregate file lists 98 PASS. The model marks 16 assets PASSIVE_MAKER_LIMIT_ARMED and 76 STAND_ASIDE_MONITOR; this is a candidate-generation label, not an execution approval. The mechanical screen also flags 27 placeholder-like technical profiles, 13 ATR/mid anomalies and 34 passive-side/quote mismatches. The generated 2.50R arithmetic does not establish valid stop geometry or broker risk.

I found no independent new setup to elevate beyond the user-proposed ETH idea. I did not use the account-floor veto as a reason to skip the scan; other model “armed” candidates failed the evidence/geometry review. For example, BCH’s model long at $274.50/$271.20/$282.75 (3.03 lots, about $10 risk, 2.50R) has its stop $5.76 above long max pain at $265.44, no whale/L2 book, and invalid zero-volume L/S rows. GBPUSD’s model long at 1.33794/1.336776/1.34085 (0.08 lot, about $9.31, 2.50R) conflicts with the latest 4h aggressive-selling CVD row and lacks corroborating positioning/flow feeds. I would not pad the list to three.

The ETH idea is the best research candidate, not a clean 15-pillar green light. Its location and arithmetic are coherent; the outflow/OI picture, unusable L/S feed, misplaced ETF data, lack of entry-level book confirmation and nearby liquidation/stop band are the counterevidence. Keep it on watch; do not stage it from this snapshot. Revalidate the entry/stop against fresh levels before treating it as an order.

Actionable order verdict
Item	Verdict
BTC #19532055 — BUY_LIMIT 0.01 @ 76,350; SL 75,850; TP 77,600; registry risk $5, 2.50R	Cancel if still pending. Do not replace now. Math is valid, but the order lacks a receipt, the current stop map is not clean, and the account is below the SOP floor.
AVE #19532058 — BUY_LIMIT 0.07 @ 122.50; SL 121.20; TP 125.75; registry risk $9.10, 2.50R	Cancel if still pending. Do not replace now. Contract-size/risk conflict, absent core feeds and weak stop geometry make it unverified even before the floor gate.
ETH slot-3 proposal — BUY_LIMIT 0.10 @ 2,170; SL 2,130; TP 2,270	Hold as research only; do not submit. $4 nominal risk and 2.50R are arithmetic only, based on dossier contract size.

If either registered ticket is already filled, verify the live position and broker history before acting; the SOP’s zero-risk rule at or below the floor still applies. No cancellation, replacement or placement was performed by me.