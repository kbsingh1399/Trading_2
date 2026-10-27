"""Offline numerical kernels for the October 27, 2026 model inquest.

No MT5, network, feed, or strategy-state mutations. These routines do not train
models or authorize trades. All inputs must have an independently verified cutoff.
OU time units are bars: kappa is per bar and sigma is R per square-root bar.
Bootstrap inference assumes local stationarity and requires external size testing.
"""
from __future__ import annotations

import math
from statistics import NormalDist
import warnings

import numpy as np
from scipy.integrate import IntegrationWarning, quad
from scipy.sparse import diags, eye
from scipy.sparse.linalg import splu
from scipy.special import logsumexp


def _vector(values, minimum=1):
    x = np.asarray(values, dtype=float)
    if x.ndim != 1 or x.size < minimum or not np.isfinite(x).all():
        raise ValueError("finite one-dimensional observations required")
    return x


def _integer(value, minimum, name):
    if not isinstance(value, (int, np.integer)) or isinstance(value, bool) or value < minimum:
        raise ValueError(f"{name} must be an integer >= {minimum}")
    return int(value)


def competing_step(fill_logit, invalidation_logit, interval_seconds):
    """Multinomial step probabilities and piecewise-constant hazard equivalents.

    Logits must come from a calibrated, horizon-matched, time-split fitted model.
    An intentional cancellation is censoring, not automatically invalidation.
    """
    logits = _vector([0.0, fill_logit, invalidation_logit])
    if not math.isfinite(interval_seconds) or interval_seconds <= 0:
        raise ValueError("positive interval required")
    normalizer = float(logsumexp(logits))
    probabilities = np.exp(logits - normalizer)
    event_mass = float(probabilities[1:].sum())
    total_hazard = normalizer / interval_seconds
    if normalizer == 0.0:  # Preserve extremely rare events despite rounded p_none.
        total_hazard = event_mass / interval_seconds
    hazards = probabilities[1:] * total_hazard / event_mass if event_mass > 0 else np.zeros(2)
    return {"p_none": float(probabilities[0]), "p_fill": float(probabilities[1]),
            "p_invalidation": float(probabilities[2]),
            "lambda_fill": float(hazards[0]), "lambda_invalidation": float(hazards[1])}


def cumulative_incidence(step_probabilities):
    """Columns: none, fill, invalidation; rows: successive at-risk intervals."""
    p = np.asarray(step_probabilities, dtype=float)
    if (p.ndim != 2 or p.shape[1] != 3 or not np.isfinite(p).all()
            or (p < 0).any() or not np.allclose(p.sum(axis=1), 1, atol=1e-12, rtol=0)):
        raise ValueError("each probability row must sum to one")
    survival, fill, invalidation = 1.0, 0.0, 0.0
    for p_none, p_fill, p_invalid in p:
        fill += survival * p_fill
        invalidation += survival * p_invalid
        survival *= p_none
    return {"fill": float(fill), "invalidation": float(invalidation), "survival": float(survival)}


def _vr_batch(r, q):
    """Rows are return paths. Return VR, heteroskedastic z_star, standard error."""
    n = r.shape[1]
    e = r - r.mean(axis=1, keepdims=True)
    d2 = e * e
    sum_d2 = d2.sum(axis=1)
    if (sum_d2 <= 0).any():
        raise ValueError("zero-variance return path")
    path = np.concatenate([np.zeros((len(r), 1)), np.cumsum(r, axis=1)], axis=1)
    rq = path[:, q:] - path[:, :-q] - q * r.mean(axis=1, keepdims=True)
    m = q * (n - q + 1) * (1 - q / n)
    vr = (rq * rq).sum(axis=1) / m / (sum_d2 / (n - 1))
    phi = np.zeros(len(r))
    for j in range(1, q):
        delta = n * (d2[:, j:] * d2[:, :-j]).sum(axis=1) / (sum_d2 * sum_d2)
        phi += (2 * (q - j) / q) ** 2 * delta
    se = np.sqrt(phi / n)
    if (se <= 0).any() or not np.isfinite(se).all():
        raise ValueError("degenerate VR standard error")
    return vr, (vr - 1) / se, se


def vr_stats(log_returns, q=4):
    q = _integer(q, 2, "q")
    r = _vector(log_returns, 4 * q)
    vr, z, se = _vr_batch(r[None, :], q)
    return {"vr": float(vr[0]), "z_star": float(z[0]), "se": float(se[0])}


def vr_bootstrap(log_returns, *, q=4, block=8, replications=1999, alpha=0.05, seed=20261027):
    """Studentized MBB interval for VR; separate null-imposing wild p-values.

    Ordinary block resampling preserves alternatives: it is NOT the null test.
    Block seams, few blocks, breaks, and multiple testing need external controls.
    This function returns inference diagnostics, never a trading qualification.
    """
    q = _integer(q, 2, "q")
    block = _integer(block, q + 1, "block")
    replications = _integer(replications, 199, "replications")
    r = _vector(log_returns, max(4 * q, 4 * block))
    if not 0 < alpha < 1:
        raise ValueError("alpha outside (0, 1)")
    rng = np.random.default_rng(seed)
    n = len(r)
    vr, z, se = (float(a[0]) for a in _vr_batch(r[None, :], q))
    starts = rng.integers(0, n - block + 1, size=(replications, math.ceil(n / block)))
    indices = (starts[:, :, None] + np.arange(block)).reshape(replications, -1)[:, :n]
    vr_mbb, _, se_mbb = _vr_batch(r[indices], q)
    t_mbb = (vr_mbb - vr) / se_mbb
    low, high = np.quantile(t_mbb, [alpha / 2, 1 - alpha / 2])
    signs = rng.choice([-1.0, 1.0], size=(replications, n))
    _, z_null, _ = _vr_batch((r - r.mean())[None, :] * signs, q)
    warnings_out = ["few_effective_blocks"] if n / block < 8 else []
    return {"vr": vr, "z_star": z, "vr_ci": [float(vr - high * se), float(vr - low * se)],
            "wild_p_left": float((1 + np.sum(z_null <= z)) / (replications + 1)),
            "wild_p_two_sided": float((1 + np.sum(np.abs(z_null) >= abs(z))) / (replications + 1)),
            "effective_blocks": n / block, "block": block, "seed": seed,
            "replications": replications, "warnings": warnings_out}


def andrews_hac_mean(observations, *, maximum_bandwidth_fraction=0.25):
    """Scalar mean-score AR(1) plug-in, Bartlett kernel with FLOAT bandwidth.

    Not a general regression sandwich or prewhitened estimator. Insufficient
    history raises instead of silently clipping a persistent AR coefficient.
    """
    x = _vector(observations, 20)
    n = len(x)
    if not 0 < maximum_bandwidth_fraction <= 0.5:
        raise ValueError("invalid maximum bandwidth fraction")
    e = x - x.mean()
    denominator = float(e[:-1] @ e[:-1])
    if denominator <= 0:
        raise ValueError("zero-variance score")
    rho = float((e[1:] @ e[:-1]) / denominator)
    if abs(rho) >= 1:
        raise ValueError("nonstationary AR(1) score approximation")
    alpha1 = 4 * rho * rho / (1 - rho * rho) ** 2
    bandwidth = max(1.0, 1.1447 * (alpha1 * n) ** (1 / 3))
    if bandwidth > maximum_bandwidth_fraction * n:
        raise ValueError("bandwidth requires a longer locally stationary record")
    lrv = float(e @ e) / n
    for lag in range(1, math.ceil(bandwidth)):
        lrv += 2 * (1 - lag / bandwidth) * float(e[lag:] @ e[:-lag]) / n
    if lrv <= 0 or not math.isfinite(lrv):
        raise ValueError("nonpositive long-run variance")
    standard_error = math.sqrt(lrv / n)
    return {"mean": float(x.mean()), "rho": rho, "bandwidth": bandwidth,
            "long_run_variance": lrv, "standard_error": standard_error,
            "t_mean": float(x.mean() / standard_error)}


def garch_integrated_variance(next_variance, omega, alpha, beta, horizon_bars):
    """Sum of forward conditional log-return variances; parameters fitted offline."""
    horizon_bars = _integer(horizon_bars, 1, "horizon_bars")
    values = _vector([next_variance, omega, alpha, beta])
    if next_variance <= 0 or omega <= 0 or (values[2:] < 0).any() or alpha + beta >= 1:
        raise ValueError("stationary positive GARCH parameters required")
    persistence = alpha + beta
    stationary_variance = omega / (1 - persistence)
    decay_sum = (-math.expm1(horizon_bars * math.log(persistence)) / (1 - persistence)
                 if persistence else 1.0)
    result = horizon_bars * stationary_variance + (next_variance - stationary_variance) * decay_sum
    if not math.isfinite(result) or result <= 0:
        raise ValueError("invalid forecast variance")
    return float(result)


def diffusion_structural_stop(current, structure, side, integrated_log_variance, breach_probability=0.02):
    """Zero-drift Brownian running-maximum bound, NOT a real-market guarantee.

    side=+1 long, -1 short. Distance to an unbreached structure counts toward
    total adverse distance. Gaps, jumps, broker basis and costs are not included.
    """
    _vector([current, structure, integrated_log_variance, breach_probability])
    if (current <= 0 or structure <= 0 or integrated_log_variance <= 0
            or side not in (-1, 1) or not 0 < breach_probability < 0.5):
        raise ValueError("invalid stop inputs")
    adverse_sign = -side
    distance = adverse_sign * math.log(structure / current)
    if distance < 0:
        raise ValueError("structure already breached")
    path_quantile = NormalDist().inv_cdf(1 - breach_probability / 2)
    required_distance = path_quantile * math.sqrt(integrated_log_variance)
    beyond_structure = max(0.0, required_distance - distance)
    stop = structure * math.exp(adverse_sign * beyond_structure)
    if stop <= 0 or not math.isfinite(stop):
        raise ValueError("nonfinite stop")
    return {"stop": stop, "log_buffer_beyond_structure": beyond_structure,
            "total_adverse_log_distance": distance + beyond_structure,
            "path_quantile": path_quantile}


def _ou_inputs(x, lower, upper, theta, kappa, sigma):
    _vector([x, lower, upper, theta, kappa, sigma])
    if lower >= upper or kappa < 0 or sigma <= 0:
        raise ValueError("invalid OU parameters or boundaries")


def _log_scale_integral(lower, upper, theta, kappa, sigma):
    peak = max(kappa * ((lower - theta) / sigma) ** 2,
               kappa * ((upper - theta) / sigma) ** 2)
    if not math.isfinite(peak):
        raise ValueError("OU scale exponent outside numerical range")
    with warnings.catch_warnings():
        warnings.simplefilter("error", IntegrationWarning)
        integral, _ = quad(lambda y: math.exp(kappa * ((y - theta) / sigma) ** 2 - peak),
                           lower, upper, epsabs=1e-11, epsrel=1e-10, limit=150)
    if integral <= 0:
        raise ValueError("degenerate OU scale integral")
    return peak + math.log(integral)


def ou_upper_before_lower(x, lower, upper, theta, kappa, sigma):
    """Infinite-horizon fixed-barrier probability via the OU scale function."""
    _ou_inputs(x, lower, upper, theta, kappa, sigma)
    if x <= lower:
        return 0.0
    if x >= upper:
        return 1.0
    if kappa == 0:
        return (x - lower) / (upper - lower)
    log_p = (_log_scale_integral(lower, x, theta, kappa, sigma)
             - _log_scale_integral(lower, upper, theta, kappa, sigma))
    return min(1.0, max(0.0, math.exp(log_p)))


def ou_finite_horizon(x, lower, upper, theta, kappa, sigma, horizon_bars,
                      *, grid_points=401, time_steps=480):
    """Fixed-barrier finite-horizon hit probabilities using an implicit PDE grid.

    Absorbing upwind generator preserves nonnegative transition rates. Run mesh
    refinement before use. Survivors are OPEN at the horizon, not forced exits.
    This is not the full staged ratchet or its age-dependent time-decay rule.
    """
    _ou_inputs(x, lower, upper, theta, kappa, sigma)
    grid_points = _integer(grid_points, 101, "grid_points")
    time_steps = _integer(time_steps, 20, "time_steps")
    if not math.isfinite(horizon_bars) or horizon_bars <= 0:
        raise ValueError("positive horizon required")
    if x <= lower:
        return {"stop": 1.0, "target": 0.0, "survival": 0.0}
    if x >= upper:
        return {"stop": 0.0, "target": 1.0, "survival": 0.0}
    grid = np.linspace(lower, upper, grid_points)
    spacing = float(grid[1] - grid[0])
    drift = kappa * (theta - grid[1:-1])
    up = 0.5 * sigma ** 2 / spacing ** 2 + np.maximum(drift, 0) / spacing
    down = 0.5 * sigma ** 2 / spacing ** 2 + np.maximum(-drift, 0) / spacing
    main = np.zeros(grid_points)
    main[1:-1] = -(up + down)
    upper_diagonal = np.zeros(grid_points - 1)
    upper_diagonal[1:] = up
    lower_diagonal = np.zeros(grid_points - 1)
    lower_diagonal[:-1] = down
    generator = diags([lower_diagonal, main, upper_diagonal], [-1, 0, 1], format="csc")
    solve = splu(eye(grid_points, format="csc") - horizon_bars / time_steps * generator).solve
    probability = np.zeros((grid_points, 2))
    probability[0, 0], probability[-1, 1] = 1.0, 1.0
    for _ in range(time_steps):
        probability = solve(probability)
    stop = float(np.interp(x, grid, probability[:, 0]))
    target = float(np.interp(x, grid, probability[:, 1]))
    if min(stop, target) < -1e-9 or stop + target > 1 + 1e-9:
        raise ArithmeticError("PDE probability conservation failed")
    return {"stop": max(0.0, stop), "target": max(0.0, target),
            "survival": max(0.0, 1 - stop - target)}


def staged_ratchet_ev(theta, kappa, sigma, *, stage1_trigger=0.8, stage1_lock=0.15,
                      stage2_trigger=1.5, stage2_lock=0.8, initial_stop=-1.0,
                      target=2.0, cost_r=0.0, initial_gain=0.0):
    """Exact infinite-horizon, two-stage OU expectancy at an initial gain.

    Continuous monitoring, fixed parameters, no gaps, no trailing runner, no
    age-dependent exit. Use executable-side prices: initial_gain can be negative
    at fill. Do not subtract spread again if already represented in those prices.
    Additional cost is subtracted once. Not a live policy optimizer.
    """
    _vector([stage1_trigger, stage1_lock, stage2_trigger, stage2_lock, initial_stop, target, cost_r, initial_gain])
    if not (initial_stop < initial_gain < stage1_trigger < stage2_trigger < target
            and stage1_trigger > 0
            and initial_stop < stage1_lock < stage1_trigger
            and stage1_lock <= stage2_lock < stage2_trigger and cost_r >= 0):
        raise ValueError("invalid monotone ratchet geometry")
    p1 = ou_upper_before_lower(initial_gain, initial_stop, stage1_trigger, theta, kappa, sigma)
    p2 = ou_upper_before_lower(stage1_trigger, stage1_lock, stage2_trigger, theta, kappa, sigma)
    p3 = ou_upper_before_lower(stage2_trigger, stage2_lock, target, theta, kappa, sigma)
    value2 = p3 * target + (1 - p3) * stage2_lock
    value1 = p2 * value2 + (1 - p2) * stage1_lock
    return p1 * value1 + (1 - p1) * initial_stop - cost_r
