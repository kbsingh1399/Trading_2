Active Skills Header: /brainstorm, /graphify, /remember, /data-analyst, /data-engineer, /dataform-bigquery, /data-driven-feature, /verify — all 8 activated per SOP Section 4. Additional enforcement via /risk-engine for floor math and /onchain-forensics for Patch1.

Account Health & Capital Floor Audit:

- Balance 4859.55 USD, Equity 4859.55 USD, Free Margin 4859.55 USD, Margin Used 0.0 USD
- Hard Floor 4775.00 USD, Operating Buffer 4795.00 USD
- Current Cushion +84.55 above hard floor, +64.55 above operating buffer
- Risk: total_contingent_stress_usd 15.75, post_joint_stop_equity_usd 4843.80, required_post_stop_equity_usd 4795.00, floor_buffer_preserved True, pending_margin_on_fill 770.75, free_margin_after_pending 4088.80, multiplier 1.25
- Stressed Equity = Current Equity - Sum(Risk_i *1.25) = 4859.55 -15.75 =4843.80 >=4775 PASS, >=4795 PASS
- Capacity: filled 0, pending 1, used_joint_fill 1, available 3, max_concurrent 4 per risk.capacity (SOP Section 8 says 2 but risk file says 4, unified to 4 per Patch6)

Pending Orders Audit Table:

Ticket | Symbol | Type | Volume | Limit Price | SL | TP | Current Distance ATR | Whale Status | Verdict & Justification

18952021 | SP500.p | SELL_LIMIT SHORT | 0.10 | 7707.50 | 7718.50 | 7674.50 | Mid 7694.61 file / 7697.82 prompt, ATR 6.9398 file /6.58 prompt, Distance 12.89 pts =1.86 ATR file / 9.68 pts =1.47 ATR prompt <=2.0 PASS Lesson5 | L2 Provenance Cycle87 ASK 7699.1 200k 0.0s GENUINE FAIL persist_s 0.0 <180, ASK 7699.2 580k 0.0s FAIL, ASK 7700.1 173k 0.0s FAIL, File L3 SELL 7758 6.29M 8843.9s presence 0.9595 gate_g7_eligible True but price 7758 above SL 7718.5 not between entry and SL, no ASK wall between 7707.5-7718.5 FAIL Lesson1 Patch2 | CANCEL — Bunker FAIL per canonical formula SL >= max_price +0.50 ATR +half_spread: Buy Above [7700-7710] max 7710 notional 31370 (<1M noise) and [7710-7720] max 7720 notional 81786 (<1M) small, file shows [7720-7730] 830k (<1M) and [7730-7740] 3,374,751 significant >=1M distance 32.5 pts =4.9 ATR >2 ATR, but SL 7718.5 inside [7710,7720] max 7720 violates SL >= max +0.50 ATR +half_spread =7720+3.4699+0.15=7723.62 (ATR 6.9398). Provenance L2 persist 0.0s violates Patch2 persist_s >=180s presence_frac >=0.85 gate_g7_eligible True. CVD Session -71 SELLER_AGGRESSION supports short but 1m/5m/15m N/A cannot verify deceleration. Spread 0.39 bps <=5 PASS cost 0.30 USD reward 33 USD friction 0.9% <15% PASS Patch5. Trend BEARISH price<EMA20 7696.92<EMA50 7702.67<EMA200 7750.68 short aligns PASS Lesson3. Capital PASS but microstructure invalidated. Dense ladder 7690→7810 every 10 pts makes MODIFY require SL >=7743.62 risk 36.12 pts =36.12 USD for 0.10 lot exceeds Tier2 16-22, lot must drop to 0.04 risk 14.44 USD but TP 7674.5 below sell cluster [7680-7690] 1.8M significant FAIL target magnet front-run (should be above cluster by 5-10 bps). Best action CANCEL to free slot.

Active Positions Management Table:

Ticket | Symbol | Type | Lots | Open Price | Current Price | Unrealized R0 | Ratchet Action Required

None | - | - | - | - | - | - | Hold — 0 open positions, no Phase0 +1.25R0 risk cut to Entry -0.25R0, no Phase1 +1.65R0 profit lock to Entry +0.80R0, no Phase2 >=2.0R0 trailing 0.50 ATR.

New Order Recommendations Table:

Result: STAND ASIDE — No new passive limit order satisfies 100% of 6 mandatory patches under strict interpretation.

Screened 24 assets as_of 10:44:32 file / 11:20:51 prompt:

- Spread FAIL (>25 bps crypto or >5 bps TradFi): SOL 22.52 file PASS but 25.46 prompt >25 FAIL, XRP 22.94 file PASS but 30.6 prompt >25 FAIL, ADA 90.21/99.68, DOGE 261.68/275, TRX 27.12/27.13 >25, DOT 191.87/192.22, LINK 72.96/71.56, LTC 51.69/51.8, AVAX 31.5/41.97, NEAR 65.75/65.4, SILVER 6.35 >5
- Wall FAIL (0 walls or persist 0.0s and notional <threshold): BCH 0, DJ30 0, GER40 0, USWTI L2 ASK 93.935 197k 0.0s FAIL persist, GBPUSD nearest 302s INSUFFICIENT
- Trend FAIL: USWTI SHORT fights BULLISH Z 1.81/2.17 RSI 61.1/61.5 Model1 forbidden per Playbook 7.3
- Remaining 8 (BTC, ETH, BNB, SP500, NAS100, GOLD, EURUSD, USDJPY):

BTC: SELL LIMIT pullback to EMA20 81105 / EMA50 81271, Z -1.04/-0.63 BEARISH ATR 289.12/285.62, price 80806.5/80923, entry 81050 distance 243.5 pts =0.84 ATR PASS proximity, spread 1.86/1.98 bps <=25 PASS cost 16.02*0.04=0.64 USD reward 33.6 friction 1.9% PASS, walls file SELL 82365 25.38M 5173s presence 0.954 True PASS >=5M and >=180s and >=0.85 and gate_g7_eligible True, but L2 provenance BID/ASK 81012 0.0s FAIL Patch2, bunker: Buy Above [81000-81100] 61291 <5M noise (<50k filtered), [81100-81200] 3,037,532 <5M noise (needs >=5M), no significant >=5M within 2 ATR (572 pts) PASS relaxed, but entry 81050 inside small cluster FAIL strict clearance, and wall 81438 between entry and SL? Entry 81050 SL 81560 wall 81438 between PASS, but SL inside [81500-81600] 4.78M <5M noise but file significant? Under >=5M PASS, strict FAIL. CVD Session -2,644,475 BULLISH_ABSORPTION while price falling indicates buyers absorbing — potential reversal against short, fails absorption vs blow-through forensics (need CVD deceleration, L2 replenishment positive, Arkham outflow). Arkham on-chain {} empty in file — Patch1 FAIL cannot corroborate exchange inflows/outflows with CVD delta. Therefore BTC fails 100% strict.

ETH: SELL LIMIT 2377 SL 2395 risk 10.98 USD, walls SELL 2392.70 14.69M 611s PASS >=5M and >=180s, SELL 2377.50 7.53M between PASS, spread 11.86/12.28 bps <=25 PASS friction 7.8% <15% PASS but Grade B requires >=2.2R per Playbook 7.4, order 2.06R FAIL, bunker: Buy Above [2360-2370] 1582 <5M, [2370-2380] 358k <5M no significant within 2 ATR PASS relaxed, but SL 2395 inside [2390-2400] small cluster strict FAIL, CVD Session -104,053,019 BEARISH_MOMENTUM synchronous decline d2(CVD)/dt2 <0 indicates blow-through, not absorption, fading pullback risky, Arkham empty FAIL Patch1.

BNB: SELL LIMIT 720.5 SL 722, walls SELL 724.01 1.19M 658s but threshold altcoins >=500k PASS, but wall above SL not between, no wall between entry and SL FAIL.

NAS100: SELL LIMIT 29620 SL 29750, L2 BID 29598 807k 360s PASS >=1M and >=180s, but ASK walls 29607 281k 0.0s FAIL persist, no ASK wall between entry and SL FAIL.

GOLD: BUY LIMIT 4152 SL 4127 risk 25 USD, walls file BUY 4140 807k 419.9s presence 1.0 True but notional 807k <1M FAIL TradFi threshold >=1M, SELL 4188 1,067,102 0.0s FAIL persist, so zero walls pass BOTH >=1M and >=180s and >=0.85 and gate_g7_eligible True. Under Patch4, GOLD has 0 qualifying walls FAIL. L2 BID 60s FAIL. CVD Session +31 BUYER_AGGRESSION supports long PASS, but Arkham empty FAIL Patch1. Proximity 0.79 ATR PASS, spread 0.17 bps PASS friction 0.14% PASS, trend BULLISH Z 1.54 long PASS.

USDJPY: BUY LIMIT 157.65 SL 157.45, walls BID 157.58 160k 669.1s PASS persist but notional 160k <500k FAIL threshold, only wall >=500k is SELL 157.81 565k 0.0s FAIL persist, zero walls pass both.

EURUSD: walls file none >=500k passing both.

Mathematical Rationale for STAND ASIDE: Under Patch4 significant notional filter (<50k noise filtered) and Patch2 persist_s >=180s presence_frac >=0.85 gate_g7_eligible True, zero assets have qualifying wall with notional >= threshold AND persist >=180s AND presence >=0.85 AND gate_g7_eligible True located between entry and SL within 2.0 ATR. Additionally Patch1 Arkham Intelligence onchain_arkham_intelligence and arkham_onchain are empty {} in live_snapshot_latest.json — cannot corroborate exchange net_flow_usd = outflow - inflow with CVD delta, so absorption vs blow-through forensics cannot be completed. Trade authorization remains DENIED_UNVERIFIED_ORDERFLOW per data_policy OBSERVED_OR_DERIVED_FROM_OBSERVED. Therefore no new order ratified.

If relaxed significance (>=500k ignored, use file L3 419s walls), best effort candidate would be GOLD LONG 0.01 @4152 SL 4127 TP 4202 risk 25 USD 2.0R with BUY 4140 wall between, CVD +31 BUYER_AGGRESSION, trend BULLISH, but still fails strict Patch2 L2 60s and Patch4 notional <1M.

Dialectic Debate Summary:

- Orderflow Specialist: L2 orderbook Cycle87 shows 0.0s persistence for 5/7 top candidates — spoofed liquidity, book imbalance BTC -0.8773 heavy ask supports short but no replenishment velocity data, NAS100 BID 29598 807k 360s GENUINE is only L2 wall passing >=180s, but ASK side hollow 0.0s. No wall satisfies Patch2+4 AND between entry/SL for new setup. CVD Session values: BTC -2.6M BULLISH_ABSORPTION indicates buyers absorbing, ETH -104M BEARISH_MOMENTUM blow-through, SP500 -71 SELLER_AGGRESSION, GOLD +31 BUYER_AGGRESSION, USDJPY +54 BUYER_AGGRESSION, NAS100 -81 SELLER_AGGRESSION.
- Macro Risk Officer: HTF regimes BEARISH for BTC/ETH/NAS100/SP500, BULLISH for GOLD/EURUSD/GBPUSD/DJ30. Model2 pullback shorts valid in bearish, longs valid in bullish. VWAP_Z extremes: NAS100 -1.25/-2.23, NEAR -1.60/-1.82, SILVER 1.88/2.04, GOLD 1.54/1.85, USWTI 1.81/1.55 — none reach |Z|>=2.0 for Model1 except SILVER 2.04 and NEAR -1.82 borderline, but SILVER spread 6.35 >5 FAIL. No Model1 extreme exhaustion with tape deceleration.
- Forensic Auditor: Capital floor 4775 preserved, stressed post 4843.80 >4795, 3 slots available, Tier1 risk 10-14.50 Tier2 16-22 enforced. Pending SP500 fails canonical bunker formula SL <= min_price -0.50 ATR -half_spread / SL >= max_price +0.50 ATR +half_spread — SL 7718.5 inside [7710,7720] max 7720. Arkham empty — cannot verify net_flow. Must cancel pending and stand aside new.

Final Actions: CANCEL 18952021, STAND ASIDE new orders pending Arkham pipeline fix and L2 persistence recovery above 180s.