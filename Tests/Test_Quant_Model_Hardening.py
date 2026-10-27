"""Offline mathematical invariants; never initializes MT5 or reads live feeds."""
import math

import numpy as np
import pytest

from Research.quant_model_hardening import (
    andrews_hac_mean, competing_step, cumulative_incidence,
    diffusion_structural_stop, garch_integrated_variance,
    ou_finite_horizon, ou_upper_before_lower, staged_ratchet_ev,
    vr_bootstrap, vr_stats,
)


def test_competing_hazards_conserve_probability_and_reconstruct_survival():
    r = competing_step(0.7, -0.5, 5.0)
    assert r['p_none'] + r['p_fill'] + r['p_invalidation'] == pytest.approx(1)
    assert math.exp(-5 * (r['lambda_fill'] + r['lambda_invalidation'])) == pytest.approx(r['p_none'])
    cumulative = cumulative_incidence([[r['p_none'], r['p_fill'], r['p_invalidation']]] * 12)
    assert sum(cumulative.values()) == pytest.approx(1)
    assert cumulative['survival'] == pytest.approx(r['p_none'] ** 12)


def test_competing_softmax_handles_extreme_but_finite_logits():
    r = competing_step(1000, -1000, 1)
    assert r['p_fill'] == pytest.approx(1)
    assert math.isfinite(r['lambda_fill'])
    assert competing_step(-100, -100, 1)['lambda_fill'] > 0


def test_vr_and_hac_are_scale_invariant():
    r = np.random.default_rng(7).normal(size=256)
    assert vr_stats(r) == pytest.approx(vr_stats(r * 100))
    base = andrews_hac_mean(r)
    scaled = andrews_hac_mean(r * 100)
    assert base['bandwidth'] == pytest.approx(scaled['bandwidth'])
    assert base['t_mean'] == pytest.approx(scaled['t_mean'])


def test_bootstrap_is_reproducible_and_has_nonzero_p_resolution():
    r = np.random.default_rng(8).normal(size=128)
    a = vr_bootstrap(r, replications=199, seed=9)
    b = vr_bootstrap(r, replications=199, seed=9)
    assert a == b
    assert a['vr_ci'][0] < a['vr_ci'][1]
    assert 1 / 200 <= a['wild_p_left'] <= 1


def test_short_bootstrap_record_is_reported_as_few_blocks():
    r = np.random.default_rng(9).normal(size=48)
    assert 'few_effective_blocks' in vr_bootstrap(r, replications=199)['warnings']


def test_andrews_formula_matches_scalar_bartlett_plugin():
    r = np.random.default_rng(10).normal(size=300)
    for i in range(1, len(r)):
        r[i] += 0.5 * r[i - 1]
    result = andrews_hac_mean(r)
    rho = result['rho']
    expected = max(1, 1.1447 * (len(r) * 4 * rho ** 2 / (1 - rho ** 2) ** 2) ** (1 / 3))
    assert result['bandwidth'] == pytest.approx(expected)


def test_garch_forecast_matches_recursive_conditional_expectations():
    h, omega, alpha, beta, horizon = 0.04, 0.002, 0.12, 0.7, 24
    total = 0
    for _ in range(horizon):
        total += h
        h = omega + (alpha + beta) * h
    assert garch_integrated_variance(0.04, omega, alpha, beta, horizon) == pytest.approx(total)


def test_path_extreme_buffer_counts_existing_structural_distance():
    result = diffusion_structural_stop(100, 101, -1, 0.01 ** 2)
    assert result['path_quantile'] == pytest.approx(2.326347874, rel=1e-8)
    assert math.log(result['stop'] / 100) == pytest.approx(2.326347874 * 0.01)
    distant = diffusion_structural_stop(100, 110, -1, 0.01 ** 2)
    assert distant['log_buffer_beyond_structure'] == 0
    assert distant['stop'] == 110


def test_ou_fixed_barriers_match_brownian_limit_and_symmetric_ou():
    assert 1 - ou_upper_before_lower(0.8, 0.15, 2, 0, 0, 0.3) == pytest.approx(1.2 / 1.85)
    assert ou_upper_before_lower(0, -1, 1, 0, 0.2, 0.3) == pytest.approx(0.5)
    probabilities = [ou_upper_before_lower(x, -1, 2, 0.4, 0.2, 0.5) for x in (-0.8, 0, 1.5)]
    assert probabilities == sorted(probabilities)


def test_finite_horizon_preserves_mass_and_converges_to_eventual_probability():
    result = ou_finite_horizon(0, -1, 1, 0, 0.2, 0.7, 60, grid_points=201)
    assert sum(result.values()) == pytest.approx(1)
    assert result['target'] == pytest.approx(0.5, abs=0.002)
    assert result['stop'] == pytest.approx(result['target'], abs=1e-9)


@pytest.mark.parametrize('threshold', [0.5, 0.8, 1.1])
def test_staged_ratchet_cannot_create_brownian_alpha(threshold):
    assert staged_ratchet_ev(0, 0, 0.3, stage1_trigger=threshold, cost_r=0.03) == pytest.approx(-0.03)


def test_initial_executable_spread_is_counted_once():
    assert staged_ratchet_ev(0, 0, 0.3, initial_gain=-0.05, cost_r=0.03) == pytest.approx(-0.08)


@pytest.mark.parametrize('call', [
    lambda: competing_step(float('nan'), 0, 1),
    lambda: cumulative_incidence([[0.5, 0.5, 0.5]]),
    lambda: vr_stats(np.zeros(48)),
    lambda: andrews_hac_mean(np.ones(48)),
    lambda: garch_integrated_variance(1, 0.1, 0.5, 0.5, 10),
    lambda: diffusion_structural_stop(100, 99, -1, 0.01),
    lambda: ou_upper_before_lower(0, -1, 1, 0, 0.2, 0),
    lambda: staged_ratchet_ev(0, 0.2, 0.3, stage1_lock=0.9),
])
def test_invalid_or_unavailable_models_raise(call):
    with pytest.raises(ValueError):
        call()
