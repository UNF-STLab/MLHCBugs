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


test_one_sided_versus_two_test(0)
print("pass")

from nilearn.glm.second_level import non_parametric_inference
import pandas as pd
from nilearn.datasets import fetch_localizer_contrasts

n_subjects = 16
data = fetch_localizer_contrasts(
    ["left vs right button press"],
    n_subjects,
    get_tmaps=True,
    legacy_format=False,
)
second_level_input = data["cmaps"]
design_matrix = pd.DataFrame(
    [1] * len(second_level_input),
    columns=["intercept"],
)
#random_state = random_state
rng = check_random_state(0)
N_SAMPLES = 50
N_PERM = 10
n_descriptors = 100
n_regressors = 1
target_var = rng.randn(N_SAMPLES, n_descriptors)
tested_var = rng.randn(N_SAMPLES, n_regressors)
MD_dict = non_parametric_inference(
    second_level_input,
    design_matrix=design_matrix,
    mask=None,
    model_intercept=True,
    second_level_contrast="intercept",
    two_sided_test=True,
    smoothing_fwhm=6,
    n_jobs=8,
    threshold=0.001
)
print("pass2")