# Quantitative model hardening research, October 27, 2026

This package is isolated numerical research. It contains no broker client,
network calls, feed publication, fitted trading coefficients or trade authority.
The adjacent `quant_model_hardening.py` implements reviewable numerical kernels;
`Tests/Test_Quant_Model_Hardening.py` checks their mathematical invariants.
It is not an integrated or certified production strategy.

## 1. Competing fill and invalidation events

Fit one multinomial outcome per at-risk interval: NONE, FILL, INVALIDATION.
For fitted logits f and i, probabilities are softmax([0, f, i]). Two independent
binary logits do not ensure mutually exclusive probabilities that sum to one.
Map a step to piecewise-constant hazards using

```text
total_hazard = -log(p_none) / interval_seconds
lambda_j = total_hazard * p_j / (1 - p_none)
survival_(k+1) = survival_k * p_none_k
F_fill_(k+1) = F_fill_k + survival_k * p_fill_k
```

Inputs must be known at interval start. Features include executable-price
distance in ATR/ticks, spread, same-price depth changes, signed order-flow
imbalance, trade intensity, volatility, venue basis, session and resting age.
Fit post-fill markout or trade outcome separately. Do not subtract an extra
adverse-selection charge from a prediction already trained on full net outcomes.

Snapshot identity: depth change = additions - cancellations - executions.
Depth snapshots plus executions identify cancellations minus additions, not
gross cancellations or true queue rank. A rank-shifted book must first be matched
by absolute price. Quote-level queue dynamics require events with timestamps.
Volume-clock VPIN needs consistently bucketed signed trade volume; minute CVD
alone does not reconstruct it. External exchange depth is not an MT5 CFD queue.

An intentional desk cancellation censors the fill process. Counterfactual fill
labels after cancellation require shadow replay or a justified censoring model;
they must not be fabricated. Cancellation criteria must be defined before labels
are generated. Reconcile cancellation/fill races with broker history.

## 2. Variance-ratio inference and HAC

`vr_bootstrap` separates two purposes:

- Moving-block resampling produces a studentized interval for the VR estimate.
- Independent wild signs applied to demeaned returns impose a martingale-
  difference null while preserving the observed magnitude sequence.

Unrestricted block resampling preserves the empirical serial dependence, so
its uncentered distribution is not the random-walk null distribution. Wild
bootstrap validity remains assumption-dependent; it is not an exact finite-
sample theorem for arbitrary skew, dependence, jumps or missing data.

For VR estimate v, standard error s and block draws v_b, s_b:

```text
t_b = (v_b - v) / s_b
CI = [v - quantile(t_b, 1-alpha/2)*s,
      v - quantile(t_b, alpha/2)*s]
left_p = (1 + count(z_null <= z_observed)) / (B + 1)
```

Use corrected Politis-White block selection on relevant moment/score series,
including squared returns and lagged-return products. Block size is statistic-
specific, not a universal fraction of the raw-return autocorrelation length.
Check neighboring block sizes and block-seam sensitivity. A block of eight bars
with 48 observations leaves only six effective blocks; the function warns.
It does not emit a trading qualification. Longer locally comparable samples,
multiple-testing controls and chronological validation remain necessary.

For scalar mean-score AR(1) coefficient rho, Andrews Bartlett bandwidth is:

```text
alpha1 = 4*rho^2 / (1-rho^2)^2
B = 1.1447*(alpha1*N)^(1/3)
weight_j = max(1-j/B, 0)
```

The kernel bandwidth B is not the integer lag count in weights 1-j/(L+1).
The kernel implementation retains a floating B. Long bandwidth requirements
raise instead of silently clipping rho. The maximum-bandwidth fraction is an
explicit engineering sufficiency guard, not Andrews' theorem. This routine is
for a scalar mean; general regression needs the appropriate score-vector
sandwich and possibly prewhitening. Volatility amplitude alone does not imply
a longer bandwidth: the scalar plug-in is scale invariant.

## 3. Volatility forecasts and structural buffers

For stationary GARCH parameters phi=alpha+beta<1 and h_bar=omega/(1-phi):

```text
V_H = H*h_bar + (h_next-h_bar)*(1-phi^H)/(1-phi)
```

This is a forecast of cumulative variance, not a guarantee that future variance
is deterministic. For a zero-drift Brownian log-price with deterministic V_H,
the reflection principle gives the running-maximum quantile:

```text
adverse_log_distance = NormalQuantile(1-p/2)*sqrt(V_H)
```

At p=0.02 the multiplier is 2.32635, versus 2.05375 for the terminal-only
one-sided quantile. Distance already lying between current price and structure
must count toward total distance. `diffusion_structural_stop` returns only the
additional log buffer required beyond an unbreached structural level.

For GARCH, jumps, random spreads or news, validate conditional running maxima
using simulated or held-out empirical paths, with uncertainty around the tail
quantile. A forecast mean variance plugged into the Brownian formula does not
guarantee a real-market two-percent touch probability. The six-hour conditional
stagnation exit is not a six-hour unconditional maximum holding period.

Do not repair oversized minimum-lot risk by narrowing a validated stop. Broker
minimum-volume loss exceeding the nominal cap means no trade. Reserve native
costs and all pending/filled book liabilities independently.

## 4. OU exit probabilities and ratchet expectancy

Transform to profit coordinates Y=side*(X-entry)/initial_price_risk. Theta and
sigma must be transformed consistently; kappa retains its time units. Use
executable-side quotes, or explicitly model spread in translating mid-price
barriers. Do not subtract the same spread a second time as a separate cost.

For fixed lower l, upper u and current y, define the OU scale density:

```text
w(z) = exp(kappa*(z-theta)^2/sigma^2)
P(upper before lower) = integral(l,y,w) / integral(l,u,w)
```

`ou_upper_before_lower` evaluates log-scaled integrals. This is an infinite-
horizon, fixed-barrier probability. `ou_finite_horizon` solves a fixed-barrier
backward equation and reports stop, target and still-open probabilities; it
does not silently force survivors to exit. The full policy requires stage and
age in its state, including the actual conditional stagnation rule after 24 bars.

`staged_ratchet_ev` recursively combines first-passage probabilities for two
monotone stages. It is exact for its stated continuous OU, infinite-horizon
assumptions, not for latency, gaps, parameter changes or age-dependent exits.
It accepts an initial gain so a broker executable spread can be represented
at fill. Additional fees are subtracted once.

Driftless illustration at y=0.8, tightened stop=0.15, target=2:

```text
P(tight stop before target) = (2-0.8)/(2-0.15) = 0.64864865
P(tight stop, then hypothetical target before original -1 stop)
    = 0.64864865 * (0.15+1)/(2+1) = 0.24864865
```

These are different quantities. Neither estimates this Gold trade's probability.
Without drift or costs, a bounded martingale's expected exit gain equals its
current gain: tightening a stop cannot create alpha. Select ratchet thresholds
only by out-of-sample, cost-aware expectancy under parameter uncertainty.

## Numerical checks observed in this research run

- GARCH martingale-difference null, 400 trials per sample size, 399 wild draws,
  nominal one-sided alpha 0.025: 5/400 rejections for N=48 and 10/400 for N=128.
  Wilson 95 percent intervals were [0.00535, 0.02892] and [0.01363, 0.04540].
  This is one synthetic null experiment, not broad inference certification.
- A synthetic fixed-barrier OU example, theta=1 R, kappa=0.2/bar,
  sigma=0.4 R/sqrt(bar), current=0.8 R, lower=0.15 R, upper=2 R, horizon=24 bars:
  coarse/fine mesh maximum probability difference 0.00015722.
- One local B=1999, N=128 bootstrap benchmark took approximately 40 ms.
  Recompute inference on completed bars in a worker; do not repeat it in the
  five-second protective management loop.

Run isolated tests:

```text
python -m pytest Tests/Test_Quant_Model_Hardening.py -q
```

## Primary references

- Andrews, HAC covariance estimation: https://cowles.yale.edu/sites/default/files/2022-08/d0877.pdf
- Corrected block-length implementation: https://bashtage.github.io/arch/bootstrap/generated/arch.bootstrap.optimal_block_length.html
- Kim, wild bootstrap VR tests: https://research.monash.edu/en/publications/wild-bootstrapping-variance-ratio-tests/
- Cont, Kukanov and Stoikov, order-flow impact: https://arxiv.org/abs/1011.6402
- Cont and Kukanov, order placement: https://arxiv.org/abs/1210.1625
- Lipton and Kaushansky, OU first passage: https://arxiv.org/abs/1810.02390

The competing-risks model and code here are a proposed construction, not a claim
that the cited order-flow papers supply fitted hazards for this broker.
