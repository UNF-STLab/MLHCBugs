import nibabel as nib
import numpy as np
from nilearn.mass_univariate import permuted_ols
from numpy.testing import assert_equal
from scipy import stats
from sklearn.utils import check_random_state

def test_one_sided_versus_two_test(random_state):
    """Check that a positive effect is always better \
    recovered with one-sided."""
    random_state = random_state
    rng = check_random_state(random_state)
    N_SAMPLES = 50
    N_PERM = 10
    n_descriptors = 100
    n_regressors = 1
    target_var = rng.randn(N_SAMPLES, n_descriptors)
    tested_var = rng.randn(N_SAMPLES, n_regressors)

    # one-sided
    output_1_sided = permuted_ols(
        tested_var,
        target_var,
        model_intercept=False,
        two_sided_test=False,
        n_perm=N_PERM,
        random_state=random_state,
        output_type="dict",
    )
    assert output_1_sided["logp_max_t"].shape == (n_regressors, n_descriptors)

    # two-sided
    output_2_sided = permuted_ols(
        tested_var,
        target_var,
        model_intercept=False,
        two_sided_test=True,
        n_perm=N_PERM,
        random_state=random_state,
        output_type="dict",
    )
    assert output_2_sided["logp_max_t"].shape == (n_regressors, n_descriptors)

    positive_effect_location = output_1_sided["logp_max_t"] > 1
    assert_equal(
        np.sum(
            output_2_sided["logp_max_t"][positive_effect_location]
            - output_1_sided["logp_max_t"][positive_effect_location]
            > 0
        ),
        0,
    )
print("pass")

test_one_sided_versus_two_test(0)