from sklearn.utils import check_random_state
from nilearn.mass_univariate import permuted_ols

random_state = 0
rng = check_random_state(random_state)

# design parameters
n_samples = 50
n_descriptors = 10
n_regressors = 2
n_covars = 2
n_perm = 10

# create design
target_vars = rng.randn(n_samples, n_descriptors)
tested_vars = rng.randn(n_samples, n_regressors)
confounding_vars = rng.randn(n_samples, n_covars)

neg_log10_pvals, own_scores, h0_fmax = permuted_ols(
    tested_vars,
    target_vars,
    confounding_vars,
    model_intercept=False,
    n_perm=n_perm,
    random_state=random_state,
)
assert own_scores.shape == (n_regressors, n_descriptors)
assert neg_log10_pvals.shape == (n_regressors, n_descriptors)
assert h0_fmax.shape == (n_regressors, n_perm)
# AssertionError, assert (10,) == (2, 10)