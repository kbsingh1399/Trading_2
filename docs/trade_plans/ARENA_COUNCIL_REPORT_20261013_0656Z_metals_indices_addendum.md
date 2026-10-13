# ARENA COUNCIL — CYCLE 51B SPECIAL ADDENDUM · METALS & INDICES ENTRY SCREEN
**Operator question: "Isn't there any other entry potential from metal or indices?"**
**Basis:** gen `699a2ae7e99440619f2f9b845ae0c7ad` @ 2026-10-13 06:56:52 UTC · Zero decision-gate tokens · Kaizen 8-trap law active
**Finding: YES — one qualified Model-2 pullback short (SP500), one geometry-live but lot-grid-dead (GOLD), four arithmetic kills.**

---

## 1. THE REAL FIND — SP500.p MODEL-2 TREND PULLBACK SHORT (the aligned model, not a fade)

The prior screens adjudicated indices mainly as Model-1 fades and killed them on trend-first. The aligned model in a BEARISH regime is the **Model-2 pullback short**, and SP500 is sitting in the exact textbook geometry (same pattern family as the cycle-41B NAS100 card):

| Parameter | Value | Proof |
|---|---|---|
| Regime | **BEARISH** | EMA20 7,796.87 < EMA50 7,799.83 < EMA200 7,802.89; EMA200 slope **−0.0101%/3h** ✓ (Inv 5 aligned — Model-2 short priority) |
| Pullback | **price 7,802.8 kissed the EMA200 shelf (7,802.89) from below** | Z **+2.32** premium over VWAP 7,795.38 (σ ≈ 3.2 pts); pullback_geometry: retrace 0.4029, **velocity_ratio 0.0183** (rally velocity 1.8% of impulse = exhaustion), 22 bars pullback vs impulse |
| Friction | **1.06 bps ≤ 5** ✓ | bid 7,802.41 / ask 7,803.24; target 65 pts = 78× spread ✓ |
| Wall shelf (Inv 4) | **5,563,357 credited ≥500k/≥180s** in [7,802, 7,830] | 2,000,000 @ 7,824.1 / 1,035 s · 1,151,662 @ 7,809.2 / 495 s · 1,000,003 @ 7,808.8 / 372 s · 808,421 @ 7,819.9 / 1,035 s · 603,275 @ 7,810.4 / 372 s (104 walls total, 71 verified) |
| Bunker (Inv 1) | **[7,820–7,840] = 5,096,895 contiguous ≥1M bands** ([7,820–7,830] 4,091,022 + [7,830–7,840] 1,005,873) | SL sits 0.46 ATR past its outer edge 7,840 ✓; the straddled [7,840–7,850] 742,956 whisker is **~7.5× credited-defended** (disclosed) |
| Magnet (TP rule) | [7,730–7,740] long-cascade **2,547,543** + [7,700–7,710] 2,075,524 + stops [7,700–7,710] 2,180,230 | TP front-runs the near-edge by 7 bps |

### CARD 2 — SP500.p · SELL LIMIT · 0.04 lots @ 7,810.00 · SL 7,842.00 · TP 7,745.00

| Field | Value | Check |
|---|---|---|
| Lots | **0.04** (contract 10 → $0.40/pt) | Kaizen #7 dynamic sizing: 32.0-pt structural stop × 0.40 = **risk 12.80 ∈ [7.50, 14.50]** ✓ |
| Entry | **7,810.00** (round + wall-belt core 7,808.8–7,810.9) | fill distance 7.2 pts = 1.67 ATR ≤ 2.0 ✓ |
| SL | **7,842.00** | 0.46 ATR past [7,820–7,840] outer edge (Inv 1 ✓, hard ≥1M band rule ✓); whisker straddle 743k at ~7.5× credited defense — disclosed |
| TP | **7,745.00** | 7-bps front-run of [7,730–7,740] 2.55M cascade top edge (playbook magnet rule) + round number |
| Reward / RR / EV | 26.00 / **2.03** / **+3.48 @ p_win LB** | RR ≥ 2.00 house bar ✓ |
| 8-trap defenses | (1) bunker-clearing 0.46-ATR stop — #18825384/#18806752/#18749312 defended (2) N/A-long; with-trend short — #18813343/#18798018 N/A (3) entry BELOW the [7,820–7,830] buy-stop pool with walls between entry and SL (the #18786372 shape is entry ABOVE the pool — inverted here) (4) ≥500k/≥180s credited shelf walls; relocation kill-switch armed (5) BEARISH HTF alignment — #18744533 inverse (with-trend, not against momentum) (6) n/a (7) lot sized to the structural stop ✓ |
| Kill-switches | [7,820–7,830] 4.09M bunker thins >50% pre-fill → cancel/re-audit (bunker moves); 15m closes holding above 7,812 (EMA200 reclaimed as support) → cancel; **any pre-07:10 staging auto-purges** | |
| **Macro gate (7-Point Checklist)** | **FAILS pre-event — Fed Waller 07:45 UTC is the highest-impact possible event for this instrument.** Staging window: **≥ 08:15 UTC (post-blackout)**, re-validate levels on the first post-blackout generation before placing. Operator may override into the pre-event window explicitly (binding), but the Council recommendation is unambiguous: post-blackout. | |
| Portfolio | Orthogonal to the ETH crypto cluster ✓. With ETH: joint 12.775 + 12.80 = 25.58 → post-stop 4,842.23 / stressed 4,831.84 ≥ 4,795 ✓ (capacity 2/4) | |

## 2. GOLD XAUUSD.pi — Model-2 pullback LONG: geometry live, **LOT-GRID DEAD** (arithmetic, not doctrine)

The bullish pullback-long geometry is genuinely present (EMA20 4,185.3 > EMA50 4,178.9 > EMA200 4,173.7, slope +0.055%/3h; Z +1.14 not extended; 40%-retrace pullback with velocity 0.82; bid shelf 1.41M credited at 4,173–4,180; friction 0.19 bps). **But the sizing cannot be reconciled with Invariant 1:**

- Governing bunker below the shelf = **[4,150–4,160] 707,578** (+ [4,120–4,130] 987,101 beneath). Compliant SL = below 4,150 by 0.35–0.50 ATR (ATR 5.73) → **SL ≤ 4,148.0**.
- Entry at the documented shelf 4,180 → stop distance ≥ 32.0 pts. Contract 100: min lot 0.01 = $1/pt → **min-lot risk = 32.00–33.00 USD > 14.50 ceiling** (Kaizen #7 cannot downsize below min lot).
- The only envelope-feasible variant (SL 4,165.5 at max risk 14.50) places the stop inside the pre-bunker corridor — the exact **#18749312** error (stop between VAL and the sweep band). Rejected on zero-regression grounds.
- **Verdict: NO GOLD CARD TONIGHT.** (The Inv-2 CVD-proxy question is moot — the kill is pure lot-grid arithmetic. If the bunker stack thins after the Fed event, the card re-opens for evaluation.)

## 3. THE OTHERS — ARITHMETIC KILLS

| Name | Kill |
|---|---|
| SILVER XAGUSD.pi | Friction **9.59 > 5 bps** (standing TradFi ruling) — geometry otherwise plausible, friction disqualifies |
| NAS100.p | Z −0.39 at VAL (30,445 vs 30,429) — **no pullback premium to short**; Model-1 long banned (Bearish HTF, Inv 5); ATR 38.4 wide-stop sizing hostile |
| DJ30.p | Z +2.77 chase at RSI 73 with pullback retrace **−0.02 (none)**; **0 walls, no L2** (Inv 4 unverifiable) |
| GER40.p | Z **+5.54** parabolic (3.35→3.67→5.0→5.54); 0 walls, no L2, no CVD; **DO-NOT-TOUCH** (momentum-against = #18744533 inverted) |
| USWTI.p | Credited ≥500k walls = **0** (the standing 13-cycle kill); price below VAL in a BULLISH label = mixed regime |

## 4. SYNC
Appended to `LIVE_COLLABORATIVE_ORDER_DESK.md` + sidecar; pushed to `arena/5c05910e-trading-2`. Book context: ETH #18826511 holds (−0.44R at 06:56 gen); Watch-Card 1 (SOL) remains suspended on the flow gate; **Card 2 (SP500) joins the post-blackout staging queue.**

— Signed, Arena.ai Multi-Persona Quantitative Council · Cycle 51B · 2026-10-13
