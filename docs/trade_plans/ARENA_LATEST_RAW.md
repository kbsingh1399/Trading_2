\n# Institutional co-design review\n\n\n**Decision cutoff:** `2026-10-23 22:00:00 UTC`\n\n## 1. Executive ruling\n\n\n### Trading ruling at the cutoff\n\n\n**No new position and no new pending order were admissible.**\n\nFor BTCUSD.pi ticket `#19267445`:\n\n- **Hold the existing protected short unchanged.**\n- Preserve broker SL `81640` and TP `80600`.\n- Do not add, hedge, widen, extend TP below the target, or prematurely ratchet.\n- The next canonical action was only:
\n- executable broker mark `≤81040` → move SL to `81300`;\n- `≤80820` → move SL to `81060`;\n- `≤80600` → TP/reconcile;\n- `≥81640` → protected stop/reconcile.\n\n- At the cutoff mark `81254`, excursion was `81700−81254=446` points or **`1.115R₀`**, so neither remaining ratchet had triggered.\n\nThis is a **historical cutoff ruling**, not a live instruction for October 24. Any present broker action requires newly authenticated telemetry.\n\n### Architecture ruling\n\n\nThe system was capable of protecting the existing BTC ticket, but it was **not institutionally safe to authorize autonomous new risk** because:\n\n1. Four incompatible solvency/risk envelopes coexist.\n2. Ratchet definitions conflict with the authoritative ticket ledger.\n3. Pending orders are not consistently stressed as independently fillable liabilities.\n4. Candidate arithmetic and column semantics failed in D12.\n5. Prompt/artifact identity and completion validation failed structurally in D11.\n6. Asset clocks and asset-native evidence are applied inconsistently.\n7. The controller can call a cycle complete using status and response length without proving cycle-bound identity, schema validity, or mathematical validity.\n8. “Consensus” was asserted despite materially different floors, ratchets, arithmetic, and evidence provenance.\n\nThe `$5,500` objective does not override these failures.\n\n---\n\n# 2. Provenance and cutoff causality\n\n\nI completed the requested line-by-line review of the six governance documents, `ACTIVE_CONTEXT.md`, and the restored Cycle 280–309 history.\n\n### Graphify disclosure\n\n\nThe required query was attempted first and failed:\n\n```\n/usr/bin/python: No module named graphify\n```\n\nI used a bounded fallback: authenticated GitHub commit/tree/blob retrieval, hash verification, normalized line-by-line reading, targeted commit lineage, and inspection of the risk/lifecycle implementation.\n\n### Commit authority\n\n\n| Object | Time | Role |\n| --- | --- | --- |\n| `6aa303d52ef5972b6e04ef7c61079c5e5fec187e` | `21:56:35Z` | Latest causal commit before the `22:00:00Z` cutoff |\n| `c2c4404ca1b322fabf866b4702559e0672aef861` | `22:01:40Z` | User-designated restored-history commit, but 100 seconds after cutoff |\n\n\nBoth commits are Git-object authenticated but unsigned.\n\nImportant distinction:\n\n- The six requested governance files and `ACTIVE_CONTEXT.md` are byte-identical between the cutoff and `c2c4404...`.\n- `Data/Manditory/session_chat_history.md` is not:
\n- cutoff blob: `257bb1f...`, only 4,357 bytes;\n- restored `c2c4404...` blob: `1814f91...`, 80,771 bytes.\n\n- Therefore, the restored history is usable as a **retrospective audit record**, but it was not all causally present in that path before 22:00.\n- Cutoff-state decisions use `6aa303d...`, its account snapshot blob `331550c...`, cycle state, R0 ledger, and cutoff-present council artifacts.\n\nNo broker request, file mutation, commit, push, or pull request was performed.\n\n---\n\n# 3. Cutoff-state reconciliation\n\n\nAt `21:56:29–21:56:32Z`:\n\n| Field | Authenticated value |\n| --- | --- |\n| Balance | `$4,799.88` |\n| Equity | `$4,825.83` |\n| Margin used | `$2,451.00` |\n| Free margin | `$2,374.83` |\n| Pending orders | `0` |\n| Position | BTCUSD.pi short `#19267445`, `0.06` lot |\n| Entry / current mark | `81700 / 81254` |\n| SL / TP | `81640 / 80600` |\n| Position profit | `+$26.76` |\n| Accrued swap | `−$0.81` |\n| Net floating contribution | `+$25.95` |\n| Snapshot authorization | `DENIED_UNVERIFIED_ORDERFLOW` |\n\n\nThe controlling strict kernel is:\nBbase=min⁡(Balance,Equity)=4799.88B_{\text{base}}=\min(\text{Balance},\text{Equity})=4799.88Bbase​=min(Balance,Equity)=4799.88Ejoint-stop=4799.88−2.00=4797.88E_{\text{joint-stop}}=4799.88-2.00=4797.88Ejoint-stop​=4799.88−2.00=4797.88H=4797.88−4795.00=2.88H=4797.88-4795.00=\boxed{2.88}H=4797.88−4795.00=2.88​\nFloating profit does not create admission headroom because `min(balance,equity)` selects realized balance while equity is higher.\n\nEven ignoring spread, the largest nominal new risk allowed by the current formula would be:\n1.25r+2≤2.881.25r+2\le 2.881.25r+2≤2.88r≤0.704r\le \boxed{0.704}r≤0.704​\nThat is below every active minimum-risk policy. New risk was therefore mathematically impossible.\n\n---\n\n# 4. What actually caused equity stagnation\n\n\nBetween the pre-loss balance of `$4,818.51` and the cutoff:\n\n- Realized balance fell to `$4,799.88`.\n- The net realized change was **`−$18.63`**.\n- No subsequent gain had been realized.\n- BTC carried substantial floating profit, but it had not yet become balance.\n- Realized distance to `$5,500` remained **`$700.12`**.\n\nThe dominant issue was not simply “too many gates.” It was a broken funnel:\nDiscovery→Qualification→Instantiation→Fill→Realization\text{Discovery}\rightarrow\text{Qualification}\rightarrow\text{Instantiation}
\rightarrow\text{Fill}\rightarrow\text{Realization}Discovery→Qualification→Instantiation→Fill→Realization\nDiscovery produced dozens of candidates, but the system lacked:\n\n- calibrated fill and win probabilities;\n- reliable market-clock filtering before row emission;\n- cycle-bound ticket artifacts;\n- consistent solvency math;\n- authoritative broker-native sizing receipts;\n- reliable conversion of valid analyses into safe, timely orders.\n\n## Cycle-history findings\n\n\n### Cycles 280–285: abundant candidates, no calibrated ranking\n\n\n- Brent, BTC, GER40, NZDUSD, indices, and metals repeatedly appeared.\n- The architecture treated multiple statistical indicators as simultaneous binary requirements.\n- Candidate counts such as `47 qualified opportunities` were not probabilities or rankings.\n- Limit distances were frequently selected from static shelves without an event-time fill model.\n\n### NZDUSD #19244087: the decisive realized failure\n\n\nThe restored record first described the NZD setup in Cycle 285:\n\n- BUY `0.81` at `0.56904`\n- SL `0.56888`\n- TP `0.56965`\n\nBy Cycle 286/287, price had already swept `0.56868`, and the transcript said staying flat avoided the setup.\n\nLater broker history records:\n\n- Fill: `07:15:12Z`\n- Stop: `07:38:40Z`\n- Realized P/L: `−$18.63`\n\nThe order failed structurally:\n\n1. Entry-to-stop was only `0.00016`, or **1.6 pips**.\n2. The stop `0.56888` was above daily VAL `0.56868`.\n3. It was far above the Asian low `0.56768`.\n4. Lot size was enlarged to fit the compressed stop.\n5. The fill coincided with the Eurozone PMI window for which the Arena artifact instructed flat-cash defense.\n\nThe later autopsy contains its own inconsistency:\n\n```\nSL <= min(VAL - 0.20×ATR, Session Low, Swing Low)\n```\n\nbut then offers `0.56860` as an example “structural” stop. `0.56860` still does not clear the stated Asian low `0.56768`.\n\nThe cost attribution is also unsupported:\n18.63−12.96=5.6718.63-12.96=5.6718.63−12.96=5.67\n`$5.67` is exactly `$7 × 0.81 lot`, which has the signature of round-turn commission, but the document calls it “spread.” Without broker deal-component receipts, it must be recorded as **unallocated transaction cost**, not asserted as spread or commission.\n\n### Contradictory Cycle-296 artifact\n\n\nThe model-labeled GLM file’s main body rejected the radar and proposed a conditional BTC order, while its attached output said:\n\n```\nORDER 1 (NOW): BUY_LIMIT NZDUSD.pi 0.81 @ 0.56904 ...
Comment: C286-R1\n```\n\nThat attachment was stale-cycle content and contradicted the main response. The repository does not contain a cycle-bound broker transmission receipt proving that this attachment caused the order, so that causality cannot be claimed. It does prove that the architecture allowed an unbound stale ticket to coexist with a different current verdict.\n\n### Unanchored/resting-limit pattern\n\n\n- Cycle 291 staged BTC `#19236218` at `81960`, then canceled it 13 minutes later after the supporting wall changed.\n- The Cycle-295 GER40 command expired or was never instantiated.\n- NZD geometry survived well beyond the cycle in which its false breakout had already been observed.\n- UKBRENT `#19270994` was staged using the loose `$4,650` floor and later canceled when the strict `$4,795` kernel was reapplied.\n- Cycle 309 emitted GER40 geometry even though GER40 was closed, its quote was roughly 116 minutes old, and the dispatch occurred inside every stated rollover window.\n\n### Rollover finding\n\n\nGovernance contradicts itself:\n\n- some sections specify `21:30–22:30 UTC`;\n- others specify `21:15–22:30 UTC`.\n\nCycle 309’s `21:40` GER proposal failed under either interval. I did **not** find an authenticated realized loss caused specifically by rollover widening; the proven defect is that the candidate generator could emit an unstageable row during the embargo and a closed session.\n\n---\n\n# 5. D11 and D12 findings\n\n\n## D11 — template and artifact binding\n\n\nCycle 308 identified missing ticket/candidate/worst-case fields. Cycle 309 populated more text and declared D11 closed, but structural closure was not achieved.\n\nRemaining failures:\n\n- no cycle nonce in harvested artifacts;\n- no prompt digest match;\n- no evidence-manifest digest match;\n- no schema validation;\n- no proof the attachment belongs to the main answer;\n- no semantic validation of ticket rows;\n- no rule preventing a stale-cycle ticket from being harvested;\n- controller completion can be satisfied by output length/status;\n- `cycle_state.json` marked Arena complete while its details still said “Generating.”\n\nD11 must remain open until machine validation—not prose—proves closure.\n\n## D12 — arithmetic and semantic column corruption\n\n\nThe Cycle-309 candidate table omitted a proper header and reused values incorrectly:\n\n- “reward” contained stressed-loss values;\n- “surplus” was derived from a stale base and the mislabeled reward;\n- rows could pass formatting while being economically meaningless.\n\nFor GER40:\n\n- Geometry: `25381.39 / 25420.23 / 25286.79`, `0.03` lot.\n- Pure contract-size proxy:\nN=(25420.23−25381.39)×10×0.03=$11.652N=(25420.23-25381.39)\times10\times0.03=\$11.652N=(25420.23−25381.39)×10×0.03=$11.652G=(25381.39−25286.79)×10×0.03=$28.38G=(25381.39-25286.79)\times10\times0.03=\$28.38G=(25381.39−25286.79)×10×0.03=$28.38\n- The inherited `$11.21/point/lot` estimate produces approximately `$13.06 / $31.81`, potentially reflecting account-currency conversion.\n- Neither value is execution-authoritative without a fresh native `order_calc_profit()` receipt.\n- The reported “reward” of about `$18.74` is neither valid reward result.\n\nFor the BTC long proposal `80500 / 79942.2 / 82000`, `0.02` lot:\nN=(80500−79942.2)×0.02=$11.156N=(80500-79942.2)\times0.02=\$11.156N=(80500−79942.2)×0.02=$11.156G=(82000−80500)×0.02=$30.00G=(82000-80500)\times0.02=\$30.00G=(82000−80500)×0.02=$30.00S=(11.156+0.30)×1.25+2=$16.320S=(11.156+0.30)\times1.25+2=\boxed{\$16.320}S=(11.156+0.30)×1.25+2=$16.320​\nThe prompt’s `$15.95` omitted spread.\n\nRegardless of the GER conversion convention, both candidates failed strict solvency by a wide margin.\n\n---\n\n# 6. Canonical contradiction registry\n\n\n| Domain | Conflicting definitions | Required resolution |\n| --- | --- | --- |\n| Admission floor | `$4,600`, `$4,650`, `$4,775`, `$4,795` | `$4,795` remains the new-risk admission floor. `$4,600/$4,650` are non-authorizing disaster telemetry only. |\n| Risk envelope | `$7.50–20`, `$10–25`, `$15–35` | One versioned policy digest. Until migration, use the safe intersection and reject disagreement. |\n| Stress | `1.25×nominal+2`, spread-inclusive version, 15-bps slippage version | Adopt one all-in definition and use the maximum during migration. |\n| Ratchets | Generic prose, `risk_kernel.py`, ticket ledger | Ticket-specific, versioned R0 ledger controls. |\n| Pending orders | “Uncapped,” ten slots, four filled slots | Every independently fillable pending order consumes joint stress and margin. |\n| Sheets | 30 versus 33 | Use a manifest count and digest; do not hardcode a count without schema version. |\n| Freshness | 7, 15, 20, 25 minutes | Field-specific event-time SLA; workbook mtime never substitutes for row timestamps. |\n| Rollover | Start at `21:15` or `21:30` | Use conservative `21:15–22:30` until broker spread evidence ratifies a narrower interval. |\n| Completion | status/length versus validated artifact | Require cycle identity, digests, schema, verdict, and arithmetic validation. |\n| Consensus | Provider labels and aggregate status | Never count a vote without independently harvested cycle-bound output. |\n\n\n---\n\n# 7. Six-domain target architecture\n\n\n## Domain 1 — hard authorization plus calibrated ranking\n\n\nBinary gates remain binary:\nGj=GlegalGdataGeventGclockGbrokerGsolvencyGstopG_j=G_{\text{legal}}G_{\text{data}}G_{\text{event}}
G_{\text{clock}}G_{\text{broker}}G_{\text{solvency}}G_{\text{stop}}Gj​=Glegal​Gdata​Gevent​Gclock​Gbroker​Gsolvency​Gstop​\nIf `G_j=0`, the candidate is rejected and never ranked.\n\nFor candidates with `G_j=1`, rank soft statistical evidence rather than requiring every indicator to pass:\nEVj=Pf[pwGj$−(1−pw)Lj$−ASj−Cj]−(1−Pf)Cwait,jEV_j=P_f\left[p_wG_j^\$-(1-p_w)L_j^\$-AS_j-C_j\right]
-(1-P_f)C_{\text{wait},j}EVj​=Pf​[pw​Gj$​−(1−pw​)Lj$​−ASj​−Cj​]−(1−Pf​)Cwait,j​\nUse a conservative posterior:\nUj=LCB⁡5%(EVj)E[capital-minutesj]U_j=\frac{\operatorname{LCB}_{5\%}(EV_j)}
{\mathbb{E}[\text{capital-minutes}_j]}Uj​=E[capital-minutesj​]LCB5%​(EVj​)​\nRequirements:\n\n- `P(fill)` and `P(win|fill)` must be separate.\n- Models must be conditioned on symbol class, setup class, session, side, and order type.\n- Missing soft evidence widens uncertainty; it does not automatically become a false binary value.\n- A feature required by a particular model may make that model unavailable, but must not globally block unrelated models.\n- Probabilities require time-blocked walk-forward calibration, reliability plots, Brier/log loss, and an explicit effective sample size.\n- No probability from `0/2` staged orders or `11/17` unrelated trades may authorize execution.\n\n## Domain 2 — strict solvency and House Money compounding\n\n\nFor every scenario ω\omegaω in which pending orders can fill:\nBbase=min⁡(Balance,Equity)B_{\text{base}}=\min(Balance,Equity)Bbase​=min(Balance,Equity)Bpost(ω)=Bbase−∑iStressedLossi(ω)B_{\text{post}}(\omega)=B_{\text{base}}
-\sum_i StressedLoss_i(\omega)Bpost​(ω)=Bbase​−i∑​StressedLossi​(ω)min⁡ωBpost(ω)≥4795\min_{\omega}B_{\text{post}}(\omega)\ge4795ωmin​Bpost​(ω)≥4795\nPending orders are assumed jointly fillable unless an authenticated broker-side OCO relationship makes them mutually exclusive.\n\nHouse Money must use realized balance only:\nPbank=max⁡(0,Brealized−Banchor)P_{\text{bank}}=\max(0,B_{\text{realized}}-B_{\text{anchor}})Pbank​=max(0,Brealized​−Banchor​)\nProposed nominal House Money cap:\nRHM=0.5PbankR_{\text{HM}}=0.5P_{\text{bank}}RHM​=0.5Pbank​Rcap=min⁡(Rpolicy,RHM,Rfloor,RKelly,Rcluster)R_{\text{cap}}=\min(R_{\text{policy}},R_{\text{HM}},
R_{\text{floor}},R_{\text{Kelly}},R_{\text{cluster}})Rcap​=min(Rpolicy​,RHM​,Rfloor​,RKelly​,Rcluster​)\nOne minimum legal retry must remain reserved:\nStressedLosscandidate≤H−StressedLossminimum-retryStressedLoss_{\text{candidate}}
\le H-StressedLoss_{\text{minimum-retry}}StressedLosscandidate​≤H−StressedLossminimum-retry​\nAfter a realized loss, the ladder automatically de-escalates. No floating P/L or expected TP unlocks a rung.\n\n## Domain 3 — wall refill, LIR, sweep/reclaim, and stop geometry\n\n\n- Wall recurrence is not refill.\n- Repeated price levels without trade prints or stable order IDs cannot establish replenishment.\n- A blind resting limit is prohibited where sweep/reclaim is the actual setup.\n- Structural invalidation determines the stop first; lot follows.\n\nFor a long:\nSLlong=floorTick⁡(min⁡(bVAL,bsession,bswing,bwall)−U)SL_{\text{long}}=
\operatorname{floorTick}\left(
\min(b_{\text{VAL}},b_{\text{session}},b_{\text{swing}},b_{\text{wall}})
-U
\right)SLlong​=floorTick(min(bVAL​,bsession​,bswing​,bwall​)−U)\nFor a short:\nSLshort=ceilTick⁡(max⁡(bVAH,bsession,bswing,bwall)+U)SL_{\text{short}}=
\operatorname{ceilTick}\left(
\max(b_{\text{VAH}},b_{\text{session}},b_{\text{swing}},b_{\text{wall}})
+U
\right)SLshort​=ceilTick(max(bVAH​,bsession​,bswing​,bwall​)+U)\nwhere:\nU=max⁡(broker stop level,q99(spread),q99(basis error),q99(boundary overshoot))U=\max(
\text{broker stop level},
q_{99}(\text{spread}),
q_{99}(\text{basis error}),
q_{99}(\text{boundary overshoot})
)U=max(broker stop level,q99​(spread),q99​(basis error),q99​(boundary overshoot))\nUniversal “25 FX points” or “400 BTC points” are diagnostics, not cross-asset laws.\n\n## Domain 4 — market clocks and asset-native evidence\n\n\nA candidate may be emitted only when:\nTradable(s,t)=BrokerOpen∧NativeVenueOpen∧QuoteFresh∧CalendarVerified∧¬Blackout∧¬RolloverTradable(s,t)=BrokerOpen\land NativeVenueOpen
\land QuoteFresh\land CalendarVerified
\land \neg Blackout\land \neg RolloverTradable(s,t)=BrokerOpen∧NativeVenueOpen∧QuoteFresh∧CalendarVerified∧¬Blackout∧¬Rollover\n| Asset | Native evidence | Prohibited substitution |\n| --- | --- | --- |\n| Crypto | CEX/perpetual trades, L2, OI, funding, basis, liquidation maps | Applying stale wallet/whale data without venue/basis identity |\n| FX | Broker ticks/spread, session liquidity, macro/fixing/rollover, CME futures where available | Crypto LIR, exchange whale walls, or crypto CVD |\n| Equity indices | Underlying cash/futures session, holidays, futures depth, basis, breadth | Treating a stale CFD quote as an open native market |\n| Metals | COMEX/native futures flow, DXY/real-yield context, CFD basis | Crypto liquidation maps |\n| Energy | NYMEX/ICE flow, curve, inventory/event clock, CFD basis | Static shelf geometry across closed sessions |\n\n\nClosed-session candidates may be watchlist rows only, never ticket rows.\n\n## Domain 5 — non-overlapping subagents and dialectic verification\n\n\nUse four blind first-pass roles:\n\n1. Regime/calibration.\n2. Fill/microstructure/geometry.\n3. Solvency/portfolio/broker math.\n4. Market clock/provenance/auction.\n\nEach receives the same immutable evidence manifest but may not see other verdicts during round one.\n\nRound two exchanges only claim IDs and evidence references. Each role must challenge assigned interfaces. Majority vote does not resolve a Severity-1 arithmetic, provenance, or solvency dispute.\n\n## Domain 6 — validated completion, quiet interval, and watchdog recovery\n\n\nState machine:\n\n```\nCREATED
→ DISPATCHED
→ HARVESTED
→ SCHEMA_VALIDATED
→ DIALECTIC_RESOLVED
→ FINALIZED
→ QUIET
→ READY\n```\n\nFailure paths:\n\n```\nDISPATCHED → STALLED → RETRY_PENDING → DISPATCHED
STALLED → DEGRADED
SCHEMA_VALIDATED → DISPUTED → DIALECTIC_RESOLVED\n```\n\nA component is complete only when the response matches:\n\n- cycle ID and dispatch nonce;\n- prompt digest;\n- evidence-manifest digest;\n- role;\n- request ID;\n- response schema;\n- response digest;\n- valid timestamps;\n- valid verdict enum;\n- arithmetic validator.\n\nThe full-cycle quiet interval is:\nTnext=max⁡(Tvalidated-final+1200s, Tdata-ready)T_{\text{next}}=
\max(T_{\text{validated-final}}+1200s,\ T_{\text{data-ready}})Tnext​=max(Tvalidated-final​+1200s, Tdata-ready​)\nRisk-management interrupts may execute immediately, but they do not start a new discovery/execution cycle or shorten the quiet interval.\n\n---\n\n# 8. Formal definitions\n\n\n## 8.1 lot*\n\n\nLet legal broker volume be:\nV={vmin⁡+kvstep:k∈N, v≤vmax⁡}\mathcal V=\{v_{\min}+kv_{\text{step}}:k\in\mathbb N,\ v\le v_{\max}\}V={vmin​+kvstep​:k∈N, v≤vmax​}\nBroker-valued stop loss:\nLstop(v)=max⁡(0,−order_calc_profit(side,symbol,v,E,SL))L_{\text{stop}}(v)=
\max\left(0,-order\_calc\_profit(side,symbol,v,E,SL)\right)Lstop​(v)=max(0,−order_calc_profit(side,symbol,v,E,SL))\nThen:\nlot∗=max⁡{v∈V:Rmin⁡≤Lstop(v)≤RcapBbase−Sjoint(v)≥4795Mjoint(v)≤FreeMargin−Mreserveorder_check(v)=OK}lot^*=\max\left\{
v\in\mathcal V:
\begin{array}{l}
R_{\min}\le L_{\text{stop}}(v)\le R_{\text{cap}}\\
B_{\text{base}}-S_{\text{joint}}(v)\ge4795\\
M_{\text{joint}}(v)\le FreeMargin-M_{\text{reserve}}\\
order\_check(v)=OK
\end{array}
\right\}lot∗=max⎩⎨⎧​v∈V:Rmin​≤Lstop​(v)≤Rcap​Bbase​−Sjoint​(v)≥4795Mjoint​(v)≤FreeMargin−Mreserve​order_check(v)=OK​⎭⎬⎫​\nIf the set is empty, reject. Never increase risk or compress the stop to meet minimum lot.\n\n## 8.2 Stressed_Loss\n\n\nCutoff implementation:\nScutoff=1.25Lnominal+2S_{\text{cutoff}}=1.25L_{\text{nominal}}+2Scutoff​=1.25Lnominal​+2\nCandidate prompt convention:\nSprompt=1.25(Lstop+Cspread)+2S_{\text{prompt}}=1.25(L_{\text{stop}}+C_{\text{spread}})+2Sprompt​=1.25(Lstop​+Cspread​)+2\nTarget all-in definition:\nCexec=Cspread-not-embedded+Ccommission+Cswap-to-TTLC_{\text{exec}}=
C_{\text{spread-not-embedded}}+
C_{\text{commission}}+
C_{\text{swap-to-TTL}}Cexec​=Cspread-not-embedded​+Ccommission​+Cswap-to-TTL​Sv1(v)=max⁡[1.25(Lstop(v)+Cexec(v))+2, CVaR99.9%(Lgap,all-in(v))]S_{v1}(v)=
\max\left[
1.25(L_{\text{stop}}(v)+C_{\text{exec}}(v))+2,\ 
CVaR_{99.9\%}(L_{\text{gap,all-in}}(v))
\right]Sv1​(v)=max[1.25(Lstop​(v)+Cexec​(v))+2, CVaR99.9%​(Lgap,all-in​(v))]\nDuring migration:\nScontrol=max⁡(Slive-admission,Srisk-kernel,Sfloor-defense,Sv1)S_{\text{control}}=\max(
S_{\text{live-admission}},
S_{\text{risk-kernel}},
S_{\text{floor-defense}},
S_{v1})Scontrol​=max(Slive-admission​,Srisk-kernel​,Sfloor-defense​,Sv1​)\n## 8.3 
𝑃
(
𝑓
𝑖
𝑙
𝑙
∣
𝑑
)
P(fill∣d)\n\n\nFor passive distance ddd, queue ahead qqq, and TTL TTT, use competing hazards:\nS(t)=exp⁡[−∫0t(hf(u)+hc(u)+hi(u))du]S(t)=\exp\left[-\int_0^t
(h_f(u)+h_c(u)+h_i(u))du\right]S(t)=exp[−∫0t​(hf​(u)+hc​(u)+hi​(u))du]\nwhere hfh_fhf​ is fill hazard, hch_chc​ cancellation/expiry hazard, and hih_ihi​ setup-invalidation hazard.\nP(fill≤T∣d,q,x)=∫0TS(t)hf(t∣d,q,xt)dtP(fill\le T\mid d,q,x)=
\int_0^T S(t)h_f(t\mid d,q,x_t)dtP(fill≤T∣d,q,x)=∫0T​S(t)hf​(t∣d,q,xt​)dt\nEstimate separately by symbol class, session, side, order type, queue state, spread, volatility, OFI, and clock regime.\n\n## 8.4 Adverse selection\n\n\nLet s=+1s=+1s=+1 for a buy and s=−1s=-1s=−1 for a sell, with fill price pfp_fpf​, later midpoint mt+Δm_{t+\Delta}mt+Δ​, cash multiplier KKK, and volume vvv:\nMarkoutΔ=sKv(mt+Δ−pf)Markout_{\Delta}
=sK v(m_{t+\Delta}-p_f)MarkoutΔ​=sKv(mt+Δ​−pf​)ASΔ=max⁡(0,−E[MarkoutΔ∣fill])AS_{\Delta}
=\max\left(0,-\mathbb E[Markout_{\Delta}\mid fill]\right)ASΔ​=max(0,−E[MarkoutΔ​∣fill])\nFor stress testing, use the upper quantile of `−Markout`, not only the mean.\n\n## 8.5 LIR\n\n\nAt current mark mmm and band BBB:\nQshort-up=∑p∈(m,m(1+B)]ShortLiquidationNotional(p)Q_{\text{short-up}}=
\sum_{p\in(m,m(1+B)]}ShortLiquidationNotional(p)Qshort-up​=p∈(m,m(1+B)]∑​ShortLiquidationNotional(p)Qlong-down=∑p∈[m(1−B),m)LongLiquidationNotional(p)Q_{\text{long-down}}=
\sum_{p\in[m(1-B),m)}LongLiquidationNotional(p)Qlong-down​=p∈[m(1−B),m)∑​LongLiquidationNotional(p)LIRB=Qshort-up+ϵQlong-down+ϵLIR_B=
\frac{Q_{\text{short-up}}+\epsilon}
{Q_{\text{long-down}}+\epsilon}LIRB​=Qlong-down​+ϵQshort-up​+ϵ​\nAlso report:\nℓB=log⁡(LIRB)\ell_B=\log(LIR_B)ℓB​=log(LIRB​)\nThe band, venue set, reconstruction method, timestamp, and coverage ratio are mandatory. If coverage is incomplete, return `UNAVAILABLE`, not infinity or zero.\n\n## 8.6 Wall persistence and refill\n\n\nFor displayed size Q(p,tk)Q(p,t_k)Q(p,tk​) and wall threshold Q∗Q^*Q∗:\nIk=1[Q(p,tk)≥Q∗]I_k=\mathbf 1[Q(p,t_k)\ge Q^*]Ik​=1[Q(p,tk​)≥Q∗]πpresence=∑kwkIk∑kwk\pi_{\text{presence}}=
\frac{\sum_kw_kI_k}{\sum_kw_k}πpresence​=∑k​wk​∑k​wk​Ik​​\nContinuous duration may be claimed only when no sampling gap exceeds the declared maximum.\n\nWith authenticated trade prints:\nρrefill=∑displayed additions within Δ after executed depletion∑executed depletion at wall\rho_{\text{refill}}=
\frac{\sum \text{displayed additions within }\Delta
\text{ after executed depletion}}
{\sum \text{executed depletion at wall}}ρrefill​=∑executed depletion at wall∑displayed additions within Δ after executed depletion​\nReport both raw ρ\rhoρ and capped `min(1,ρ)`. If executed depletion cannot be separated from cancellation, refill is `UNAVAILABLE`.\n\n## 8.7 OU half-life\n\n\nFor sampled deviation yty_tyt​:\nyt+Δ=a+ϕyt+ϵty_{t+\Delta}=a+\phi y_t+\epsilon_tyt+Δ​=a+ϕyt​+ϵt​\nFor 0<ϕ<10<\phi<10<ϕ<1:\nκ=−ln⁡ϕΔ\kappa=-\frac{\ln\phi}{\Delta}κ=−Δlnϕ​t1/2=ln⁡2κ=−Δln⁡2ln⁡ϕt_{1/2}=\frac{\ln2}{\kappa}
=-\frac{\Delta\ln2}{\ln\phi}t1/2​=κln2​=−lnϕΔln2​\nIf ϕ≤0\phi\le0ϕ≤0, ϕ≥1\phi\ge1ϕ≥1, or its confidence interval includes one, report no reliable finite OU half-life. Sampling interval and confidence interval are mandatory.\n\n## 8.8 House Money ladder\n\n\nLet RsR_sRs​ be the versioned seed-risk cap:\n\n| State | Condition | Nominal cap |\n| --- | --- | --- |\n| Locked | Strict headroom cannot fund candidate plus retry | `$0` |\n| Seed | No realized profit bank | `min(Rs, Rfloor, Rpolicy)` |\n| HM-1 | Pbank≥2RsP_{\text{bank}}\ge2R_sPbank​≥2Rs​ | RsR_sRs​ |\n| HM-2 | Pbank≥4RsP_{\text{bank}}\ge4R_sPbank​≥4Rs​ | 2Rs2R_s2Rs​ |\n| HM-k | Pbank≥2k+1RsP_{\text{bank}}\ge2^{k+1}R_sPbank​≥2k+1Rs​ | 2kRs2^kR_s2kRs​ |\n\n\nEvery rung is additionally capped by:\nR≤0.5PbankR\le0.5P_{\text{bank}}R≤0.5Pbank​\nand by strict stress, margin, concentration, and calibrated Kelly limits.\n\n---\n\n# 9. BTC #19267445 and exact capital unlock\n\n\n## Cutoff guidance\n\n\nThe bearish case remained supportive of holding:\n\n- broker mark below EMA20, EMA50, EMA200, and session VWAP;\n- negative 15-minute delta;\n- top-20 book imbalance `−0.3384`;\n- downside stops and long-liquidation fuel through `80900–80300`.\n\nBut this did not authorize adding:\n\n- strict residual headroom only `$2.88`;\n- orderflow authorization denied;\n- calendar unavailable/fail-closed;\n- venue prices materially differed;\n- some CoinGlass layers were stale.\n\n### Target absorption\n\n\nThe `80600–80700` region contained substantial downside stop/liquidation fuel, while buy liquidity was recorded near `80500` and wallet-attributed bids around `80484/80427`.\n\nTherefore:\n\n- keep TP at `80600`;\n- do not extend below the shelf;\n- do not manually front-run the TP based only on a wall snapshot;\n- if executable ask reaches `80600` but the position remains after repeated broker reconciliation, classify it as an execution anomaly and freeze new activity;\n- use broker price for execution and P/L, not Binance or Hyperliquid mid without explicit basis translation.\n\n## Post-TP protocol\n\n\nThe theoretical gross TP is:\n(81700−80600)×0.06=$66.00(81700-80600)\times0.06=\$66.00(81700−80600)×0.06=$66.00\nTheoretical pre-cost balance:\n4799.88+66.00=$4865.884799.88+66.00=\$4865.884799.88+66.00=$4865.88\nThis is not the unlock balance. Actual balance must include the broker-confirmed fill, accrued swap, commission, and any slippage.\n\nRequired sequence:\n\n1. Obtain closing deal ID and exact fill.\n2. Confirm no residual BTC position or partial fill.\n3. Confirm no pending BTC/cluster order.\n4. Refresh `account_info`, positions, orders, symbol metadata, quote, and calendar.\n5. Persist the ticket as `CLOSED` in the R0 ledger with deal IDs.\n6. Set:
Pbank=Bnew−4799.88P_{\text{bank}}=B_{\text{new}}-4799.88Pbank​=Bnew​−4799.88\n7. Recalculate joint stress from zero inventory.\n8. Require one minimum legal retry reserve.\n9. Run native `order_calc_profit`, `order_calc_margin`, and `order_check`.\n10. Require a single reconciled risk-policy digest.\n11. Require fresh asset-native setup evidence; old BTC-L2 geometry is not an executable authorization.\n\nFor the historical BTC-L2 proposal `80400 / 79942.2 / 81500`, `0.07` lot, using the old 15-point spread:\nR=(80400−79942.2)×0.07=$32.046R=(80400-79942.2)\times0.07=\$32.046R=(80400−79942.2)×0.07=$32.046G=(81500−80400)×0.07=$77.00G=(81500-80400)\times0.07=\$77.00G=(81500−80400)×0.07=$77.00S=(32.046+1.05)×1.25+2=$43.37S=(32.046+1.05)\times1.25+2=\$43.37S=(32.046+1.05)×1.25+2=$43.37\nWith a minimum retry of:\n1.25(7.50)+2=$11.3751.25(7.50)+2=\$11.3751.25(7.50)+2=$11.375\nthe strict financial threshold is:\nBnew≥4795+43.37+11.375=$4849.745B_{\text{new}}\ge4795+43.37+11.375
=\boxed{\$4849.745}Bnew​≥4795+43.37+11.375=$4849.745​\nHouse Money at a 50% nominal cap additionally requires:\nPbank≥2(32.046)=$64.092P_{\text{bank}}\ge2(32.046)=\boxed{\$64.092}Pbank​≥2(32.046)=$64.092​\nThus the old proposal would unlock only if:\n\n- actual net realized TP profit is at least `$64.092`;\n- actual post-close balance is at least `$4,849.745`;\n- the reconciled policy permits `$32.046` nominal risk;\n- fresh evidence independently revalidates the setup;\n- broker-native receipts pass.\n\nThe GLM artifact’s stated `$172.51` surplus used the obsolete `$4,650` floor. Under the strict floor, theoretical pre-cost surplus was only:\n4865.88−43.37−4795=$27.514865.88-43.37-4795=\boxed{\$27.51}4865.88−43.37−4795=$27.51​\n---\n\n# 10. Arena verification versus the GLM artifact\n\n\nThe cutoff contains:\n\n- Arena-labeled blob `9c834bd4ca8f...`\n- GLM-labeled blob `3b00862a039b...`\n\nGit authenticates their exact repository contents. It does **not** cryptographically attest that the named model produced them.\n\n| Matter | Independent verification | GLM-labeled artifact |\n| --- | --- | --- |\n| New entries | Reject | Reject |\n| Existing BTC | Hold | Hold |\n| GER market clock | Closed/rollover/stale | Correctly identified |\n| D12 | Real semantic corruption | Correctly identified |\n| Admission floor | `$4,795` | Used `$4,650` for surplus |\n| Ratchets | `81040→81300`, `80820→81060` | Used incompatible `80950/80710` ladder |\n| GER sizing | Requires native broker receipt | Reused `$11.21` point value without fresh receipt |\n| BTC-L2 surplus | `$27.51` theoretical pre-cost | `$172.51` |\n| Breach probability | Not established; cannot be zero | Reported `0.0000` |\n| Consensus | Not provenance-complete | Presented as unanimous |\n\n\nThe overlap on “hold/no new entry” is useful corroboration, but it is not co-equal authenticated concurrence.\n\n---\n\n# 11. Ready-to-integrate amendments\n\n\nLine numbers below refer to normalized LF text; use heading text as the definitive anchor.\n\n## A. STANDARDIZED_TRADING_DECISION_CHAIN.md\n\n\n### Replace from\n\n\n`## 🟩 STEP 2 — APPLY THE FOUR HARD GATES`\n
through immediately before `## 🟩 STEP 3`\n\n```\n## 🟩 STEP 2 — HARD AUTHORIZATION, THEN CALIBRATED RANKING

### 2.1 Hard authorization

For candidate j:

G_j = G_legal × G_data × G_event × G_clock × G_broker ×
      G_solvency × G_structural_stop

If any term is zero, status = REJECT_HARD_GATE and the candidate MUST NOT
enter the ranking table.

Hard gates are binary only for:
1. Legal/account authorization.
2. Evidence integrity, causality, and field-level freshness.
3. Event/blackout authorization.
4. Broker session, symbol, stop/freeze level, margin, and order_check validity.
5. Joint solvency under every independently fillable pending-order scenario.
6. Structural stop outside the invalidation envelope.

Missing soft evidence does not silently become FALSE. It either widens model
uncertainty or makes only the affected setup model unavailable.

### 2.2 Soft statistical ranking

Estimate separately:

P_f = P(fill before TTL | distance, queue, symbol, session, side, features)
P_w = P(TP first | fill, setup class, asset-native features)

EV_net = P_f × [P_w × G_net − (1−P_w) × L_net − AS − Costs]
         − (1−P_f) × C_wait

Rank only hard-gate survivors by:

Utility = LCB_5%(EV_net) / E[capital-minutes]

No point probability may authorize execution unless the model has:
- time-blocked out-of-sample calibration;
- setup- and asset-class lineage;
- Brier/log-loss and reliability diagnostics;
- effective sample size and confidence interval;
- no look-ahead or cross-asset feature transfer.

A vote count, indicator count, or “3 of 4 pillars” is not a calibrated
probability.

### 2.3 Market-clock pre-emission rule

Tradable(symbol, now) =
  broker_session_open
  AND native_venue_open
  AND quote_fresh
  AND calendar_verified
  AND NOT blackout
  AND NOT rollover

A closed-session or stale symbol may appear only in WATCHLIST output.
It MUST NOT produce a ticket row.\n```\n\n### Replace the lot-sizing portion of Step 8/9 with\n\n\n```\n### Broker-native structural sizing

1. Determine structural invalidation and stop price before volume.
2. Obtain fresh symbol metadata.
3. Enumerate the broker's legal lot grid.
4. For each volume v, calculate loss with order_calc_profit.
5. Calculate margin with order_calc_margin.
6. Submit the exact request to order_check.
7. Stress all open positions and independently fillable pending orders jointly.
8. Select the largest volume that preserves the $4,795 admission floor.
9. If no legal volume exists, reject. Never tighten SL or over-risk minimum lot.

lot* = max {v in broker lot grid:
  R_min <= broker_stop_loss(v) <= R_cap
  AND min(balance,equity) - stressed_joint_loss(v) >= 4795
  AND joint_margin(v) <= free_margin - reserve
  AND order_check(v) = OK
}

Floating profit, expected TP, model probability, and deadline pressure provide
zero admission credit.\n```\n\n---\n\n## B. AUTONOMOUS_WAKEUP_CHECKLIST.md\n\n\n### Replace STEP 0 through immediately before STEP 1\n\n\n```\n## 🔴 STEP 0 — OPEN IMMUTABLE CYCLE ENVELOPE

Do not dispatch analysis until every box passes:

- [ ] cycle_id and UUID are new and unique.
- [ ] cutoff_utc is explicit.
- [ ] evidence commit and tree are cutoff-causal.
- [ ] evidence manifest has a SHA-256 digest.
- [ ] physical workbook/blob digest is recorded.
- [ ] all critical rows carry source timestamps; workbook mtime is not freshness.
- [ ] account, positions, orders, deals, symbol metadata, and broker clock reconcile.
- [ ] balance/equity residuals are explained or fail closed.
- [ ] calendar is authenticated and available.
- [ ] broker and native market clocks are open.
- [ ] outside the conservative 21:15–22:30 UTC FX rollover embargo.
- [ ] strict admission uses min(balance,equity) and $4,795.
- [ ] all pending orders are included in joint stress and margin.
- [ ] prompt renderer reports zero unresolved placeholders.
- [ ] prompt digest and dispatch nonce are persisted before transmission.

If any identity, inventory, calendar, or solvency field fails:
AUTHORIZATION = DENIED_FAIL_CLOSED.
Existing-position risk management remains active.\n```\n\n### Replace STEP 12 — Dynamic Joint-Completion with\n\n\n```\n## STEP 12 — VALIDATED JOINT COMPLETION AND QUIET INTERVAL

A provider or subagent is COMPLETE only if all conditions pass:

- [ ] cycle_id matches.
- [ ] dispatch nonce and request_id match.
- [ ] prompt SHA-256 matches.
- [ ] evidence-manifest SHA-256 matches.
- [ ] role matches the dispatched role.
- [ ] response timestamp is after dispatch.
- [ ] response SHA-256 is persisted.
- [ ] schema validation passes.
- [ ] no unresolved template markers exist.
- [ ] verdict is a permitted enum.
- [ ] money columns pass independent recomputation.
- [ ] every material claim references evidence IDs.
- [ ] provider/model identity is labelled with its actual attestation level.
- [ ] all Severity-1/2 dialectic disputes are resolved or fail closed.

State progression:
CREATED → DISPATCHED → HARVESTED → SCHEMA_VALIDATED →
DIALECTIC_RESOLVED → FINALIZED → QUIET → READY

The next full cycle is:
max(validated_final_at + 1200 seconds, data_ready_at)

Position-risk interrupts may run during QUIET but may not open new risk or
shorten the 20-minute interval.

Watchdog recovery:
1. Mark STALLED with stage and last heartbeat.
2. Retry idempotently with the same cycle identity and a new attempt ID.
3. Maximum two retries per component.
4. On exhaustion, mark DEGRADED; never fabricate a vote.
5. Continue existing-position protection.
6. New-risk authorization remains denied while a mandatory component is absent.\n```\n\n---\n\n## C. SUBAGENT_PROMPT_TEMPLATES.md\n\n\n### Replace the four overlapping persona templates with\n\n\n```\n## FOUR NON-OVERLAPPING INSTITUTIONAL ROLES

The dispatcher attaches one immutable `cycle_envelope.json`. The prompt body
contains no account-value placeholders. If the envelope is missing, malformed,
hash-mismatched, or not cutoff-causal, return DENIED_BAD_ENVELOPE.

Every role must return:
- schema_version
- cycle_id
- role
- evidence_manifest_sha256
- prompt_sha256
- dispatch_nonce
- claims[]
- challenges[]
- unknowns[]
- severity_1_or_2_disputes[]
- role_verdict
- response_sha256

Every claim must contain:
claim_id, statement, evidence_ids, formula_or_test, result, uncertainty,
status in {VERIFIED, FALSIFIED, UNAVAILABLE}.

### ROLE A — REGIME AND CALIBRATION

Mandate:
- Identify eligible setup classes from asset-native completed bars.
- Estimate calibrated P(TP first | fill), not P(fill).
- Report walk-forward calibration, uncertainty, and effective sample size.
- Compute VR, ER, HAC drift, and OU only with declared windows and sampling.
- Challenge unsupported alpha and cross-asset feature transfer.

Prohibited:
- No lot sizing.
- No solvency authorization.
- No broker-order recommendation.
- No wall authenticity claim.
- No majority-vote reasoning.

### ROLE B — FILL, MICROSTRUCTURE, AND GEOMETRY

Mandate:
- Estimate P(fill before TTL) with queue/distance/session conditioning.
- Calculate adverse-selection markouts.
- Verify wall polarity, persistence, executed depletion, refill, and cancellation.
- Verify LIR band, venue, timestamp, and coverage.
- Verify sweep/reclaim and structural entry/SL/TP geometry.
- Challenge Role A assumptions that ignore fill or toxicity.

Prohibited:
- No portfolio floor decision.
- No generic crypto features for FX, indices, metals, or energy.
- No refill claim from repeated snapshots alone.
- No blind limit where sweep/reclaim is required.

### ROLE C — SOLVENCY, PORTFOLIO, AND BROKER MATH

Mandate:
- Reconcile balance, equity, P/L, swap, commission, positions, and orders.
- Recompute risk/reward/stress directly from entry, SL, TP, volume, and native
  broker receipts.
- Enumerate every independently fillable pending-order scenario.
- Calculate lot*, joint margin, cluster exposure, and House Money status.
- Enforce min(balance,equity) − joint stress >= 4795.
- Challenge every monetary column produced by any other role.

Prohibited:
- No alpha claim.
- No probability invention.
- No credit for floating profit or expected TP.
- No fallback contract arithmetic when broker-native calculation is required.

### ROLE D — MARKET CLOCK, AUCTION, EVENTS, AND PROVENANCE

Mandate:
- Verify cutoff causality, source timestamps, manifest and workbook digests.
- Verify broker session, native venue, holiday, rollover, and event windows.
- Verify auction levels and CFD/native basis.
- Classify each symbol as EXECUTABLE, WATCHLIST_ONLY, or CLOSED.
- Challenge stale-cycle artifacts, unsupported provider identity, and stale data.

Prohibited:
- No risk sizing.
- No directional alpha verdict.
- No crypto microstructure transfer to non-crypto instruments.
- No use of workbook mtime as row-level freshness.

## DIALECTIC ROUND

Round 1 is blind and independent.

Round 2 distributes claim IDs only:
- A challenges B/D claims affecting statistical conditioning.
- B challenges A/C claims affecting fill and geometry.
- C challenges all money, margin, and solvency claims.
- D challenges all causality, freshness, clock, and provenance claims.

A Severity-1 or Severity-2 dispute cannot be resolved by vote. It requires
evidence-backed correction or AUTHORIZATION = DENIED_DISPUTED.\n```\n\n---\n\n## D. TOP_10_TRADE_EXECUTION_PITFALLS_AND_AUTOPSY.md\n\n\n### Correct the NZD cost statement\n\n\nReplace “Realized −$18.63 with spread” with:\n\n```\nRealized P/L was −$18.63 versus −$12.96 entry-to-SL price loss. The remaining
−$5.67 is an unallocated transaction-cost component until broker deal receipts
separate commission, spread/slippage, and swap. Do not label it by inference.\n```\n\n### Insert after Pitfall 18\n\n\n```\n### PITFALL 19 — CLOSED-MARKET OR ROLLOVER ZOMBIE ORDER
A technically attractive row is emitted while the native venue is closed,
the broker quote is stale, or rollover is active.

Prevention:
- Market-clock gate before candidate emission.
- Conservative FX rollover embargo 21:15–22:30 UTC.
- Closed symbols are WATCHLIST_ONLY.
- Re-pin every level, quote, event state, and TTL after reopening.

### PITFALL 20 — UNBOUND PROMPT OR STALE ATTACHMENT (D11)
A ticket is harvested without proving cycle ID, nonce, prompt digest, evidence
digest, role, and response schema. A stale attachment can contradict the main
answer.

Prevention:
- Reject unresolved placeholders.
- Reject cycle or digest mismatch.
- Parse only one schema-valid ticket object.
- Never execute free-form attachment text.
- Persist broker request/response linkage.

### PITFALL 21 — SEMANTIC MONEY-COLUMN ALIASING (D12)
A valid number is placed under the wrong economic label, such as stress being
reported as reward or stale surplus being reported as current capacity.

Prevention:
- Recompute risk, reward, R:R, stress, and post-loss equity independently.
- Enforce:
  abs(reward − broker_profit(entry→TP)) <= $0.01
  abs(risk − broker_loss(entry→SL)) <= $0.01
  post_loss = min(balance,equity) − joint_stress
- Quarantine the entire row on any mismatch.

### PITFALL 22 — FALSE COMPLETION OR FALSE CONSENSUS
A cycle is marked complete from response length/status, or a provider is counted
despite missing/unauthenticated output.

Prevention:
- Cycle-bound artifact identity and schema validation.
- No vote without a harvested response digest.
- Provider identity carries an attestation level.
- Mathematical disagreement is a dispute, not consensus.
- Watchdog must retry or degrade explicitly.\n```\n\n### Replace the malformed duplicated checklist with\n\n\n```\n## EX-ANTE 22-CONTROL CHECKLIST

1. [ ] Wall side/polarity and venue verified.
2. [ ] Stop/liquidation path verified and source-bounded.
3. [ ] Asset-native CVD/OFI confirmed or explicitly unavailable.
4. [ ] Stop lies beyond the structural invalidation envelope.
5. [ ] Entry is at a defined auction/structural location.
6. [ ] All-in friction is <=10% of expected gross reward.
7. [ ] Statistical probability is calibrated for this setup class.
8. [ ] Required sweep/reclaim is event-time verified.
9. [ ] TP front-runs opposing absorption with net R:R >=2.
10. [ ] Joint stressed balance remains >=$4,795.
11. [ ] Order type is passive/legal and tick-snapped.
12. [ ] P(fill|distance,queue,TTL) is calibrated.
13. [ ] Partial-fill and residual-cancel policy is explicit.
14. [ ] Current spread <= configured expansion threshold.
15. [ ] Wall persistence and actual refill are separately verified.
16. [ ] Cluster/correlation scenarios are jointly stressed.
17. [ ] Evidence manifest and physical data digests match.
18. [ ] Stop was chosen before lot; no stop compression.
19. [ ] Broker/native clock, holiday, event, and rollover gates pass.
20. [ ] D11 cycle/prompt/evidence identities pass.
21. [ ] D12 risk/reward/stress/surplus recomputation passes.
22. [ ] Joint completion and provenance validation pass.\n```\n\n---\n\n## E. CONTINUOUS_KAIZEN_SELF_IMPROVEMENT_PROTOCOL.md\n\n\n### Replace Section 2.5 with\n\n\n```\n## 2.5 — FALSIFIABLE FUNNEL IMPROVEMENT

Measure the entire causal funnel by immutable candidate ID:

discovered
→ hard-gate eligible
→ ranked
→ authorized
→ transmitted
→ acknowledged
→ filled
→ TP/SL/cancel/censored
→ realized

Required metrics by symbol class, setup class, side, and session:
- candidate count;
- hard-gate rejection reason;
- P(fill) forecast and outcome;
- P(win|fill) forecast and outcome;
- adverse-selection markouts;
- time to fill and time to resolution;
- net realized P/L after all costs;
- Brier score, log loss, reliability error;
- rejected-candidate shadow outcome without survivorship editing.

Do not optimize order count. Optimize conservative out-of-sample net EV per
capital-minute subject to the hard solvency kernel.

Every claimed fix requires:
1. defect ID;
2. failing fixture;
3. causal root;
4. code/doc/config change;
5. test artifact;
6. shadow period;
7. closure criterion;
8. rollback rule.\n```\n\n### Insert a defect ledger\n\n\n```\n## 2.6 — OPEN DEFECT LEDGER

| ID | Defect | Severity | Closure criterion |
|---|---|---:|---|
| D11 | Unbound or unresolved prompt/ticket artifact | 1 | 100% rejection of cycle, nonce, prompt, evidence, schema, or placeholder mismatch in tests |
| D12 | Risk/reward/stress/surplus semantic aliasing | 1 | Broker-native recomputation fixture passes to $0.01 for every ticket row |
| D13 | Market-clock candidate emitted while closed | 1 | Closed/rollover fixtures can emit WATCHLIST only |
| D14 | Risk-policy digest disagreement | 1 | All admission components load one policy digest or deny execution |
| D15 | Lifecycle STALLED has no recovery | 2 | Idempotent retry, degraded state, restart recovery, and no fabricated completion |
| D16 | Refill inferred from recurrence | 2 | Refill requires executions plus replacements; otherwise UNAVAILABLE |\n```\n\n---\n\n## F. Arena_GLM_Standard_Prompt.md\n\n\n### Replace ## 📋 FULL STANDARD PROMPT to end-of-file with\n\n\n```\n## STATIC COUNCIL REVIEW PROTOCOL

The dispatcher attaches one immutable machine-generated `cycle_envelope.json`.
This prompt contains no account-value, ticket, candidate, or cycle placeholders.

If the attachment is absent, malformed, digest-mismatched, post-cutoff, or
contains unresolved template markers, return only:
DENIED_BAD_CYCLE_ENVELOPE

### Required review

1. Provenance
   - Verify cycle ID, cutoff, evidence commit/tree, manifest digest, prompt
     digest, dispatch nonce, and timestamps.
   - State the actual attestation level of every external/provider artifact.

2. Inventory
   - Reconcile balance, equity, margin, free margin, positions, pending orders,
     deals, swap, and commission.
   - Explain every residual or fail closed.

3. Strict solvency
   - Use min(balance,equity).
   - Stress every independently fillable order scenario.
   - Require post-joint-stress balance >= $4,795.
   - Give zero credit to floating P/L or expected TP.

4. Candidate mathematics
   - Recompute risk from entry to SL.
   - Recompute reward from entry to TP.
   - Recompute R:R.
   - Recompute all-in stress.
   - Recompute joint post-loss balance.
   - Require native order_calc_profit, order_calc_margin, and order_check before
     an executable verdict.

5. Market clock and asset-native evidence
   - Reject closed, rollover, stale, calendar-unverified, or cross-asset
     evidence.
   - Closed symbols are watchlist-only.

6. Existing positions
   - Use the ticket's immutable R0 ledger.
   - Ticket-specific ratchets override generic prose.
   - Never call a protected position risk-free; state the modeled reserve and
     gap limitations.

7. Methodology
   - Separate hard gates from calibrated ranking.
   - Separate P(fill) from P(win|fill).
   - Report adverse selection, calibration limits, and unknowns.
   - Do not convert a small sample into a confident probability.

### Required response schema

Return one JSON object plus a human-readable explanation.

The JSON object must contain:
- schema_version
- cycle_id
- cutoff_utc
- evidence_manifest_sha256
- prompt_sha256
- dispatch_nonce
- provenance_status
- inventory_status
- hard_gate_results
- existing_ticket_actions
- candidate_rows
- arithmetic_validation
- disputes
- unknowns
- authorization
- response_sha256

Each candidate row must contain:
- candidate_id
- symbol
- native_market
- clock_status
- quote_timestamp
- side
- order_type
- entry
- stop
- target
- volume
- broker_risk_usd
- broker_reward_usd
- rr
- spread_cost_usd
- stressed_loss_usd
- post_joint_stop_balance
- p_fill
- p_win_given_fill
- adverse_selection_usd
- evidence_ids
- verdict
- rejection_reasons

Permitted authorization values:
DENIED_FAIL_CLOSED
DENIED_DISPUTED
WATCHLIST_ONLY
MANAGE_EXISTING_ONLY
AUTHORIZED_PENDING_BROKER_RECEIPT
AUTHORIZED

No prose ticket, attachment, majority vote, or provider label may override this
schema.\n```\n\n---\n\n# 12. Required implementation order\n\n\nThese amendments should not be applied as documentation-only changes.\n\n1. Freeze autonomous new-order transmission.\n2. Introduce one versioned risk-policy object and digest.\n3. Update `live_admission.py`, `risk_kernel.py`, and `floor_defense.py` atomically.\n4. Make `trade_r0_ledger.json` authoritative for active ticket ratchets.\n5. Add broker-native calculation receipts to candidate artifacts.\n6. Implement prompt compilation and D11/D12 validators.\n7. Implement market-clock filtering before row emission.\n8. Upgrade `joint_cycle_controller.py` to the validated state machine and recovery path.\n9. Run fixtures for:
\n- NZD stop behind `0.56768`;\n- stale NZD attachment rejection;\n- GER closed/rollover rejection;\n- GER/BTC D12 column corruption;\n- BTC canonical ratchets;\n- joint pending-order stress;\n- prompt nonce/digest mismatch;\n- STALLED recovery;\n- post-TP House Money de-escalation.\n\n10. Shadow-test before permitting new risk.\n\nThe existing BTC protection loop may remain active during migration, but it should not be described as zero-risk and must not authorize additional capital by itself.\n