
import os
from pathlib import Path

import numpy as np
import pandas as pd
from nilearn._utils.data_gen import (
    write_fake_fmri_data_and_design,
)
from nibabel import load
from nibabel.tmpdirs import InTemporaryDirectory
BASEDIR = os.path.dirname(os.path.abspath(__file__))
FUNCFILE = os.path.join(BASEDIR, "functional.nii.gz")
from nilearn.image import get_data, new_img_like, smooth_img
from nilearn.glm.second_level import non_parametric_inference
try:
    from nilearn.reporting import get_clusters_table
except ImportError:
    have_mpl = False
else:
    have_mpl = True

def input_df():
    """Input DataFrame for testing."""
    return pd.DataFrame(
        {
            "effects_map_path": ["foo.nii", "bar.nii", "baz.nii"],
            "subject_label": ["foo", "bar", "baz"],
        }
    )

def test_non_parametric_inference_cluster_level_with_covariates(
        random_state=0
):
    """Test non-parametric inference with cluster-level inference in \
    the context of covariates."""
    rng = np.random.RandomState(random_state)

    with InTemporaryDirectory():
        shapes = ((7, 8, 9, 1),)
        mask, FUNCFILE, _ = write_fake_fmri_data_and_design(shapes)
        FUNCFILE = FUNCFILE[0]
        func_img = load(FUNCFILE)

        unc_pval = 0.01
        n_subjects = 2

        # Set up one sample t-test design with two random covariates
        cov1 = rng.random(n_subjects)
        cov2 = rng.random(n_subjects)
        X = pd.DataFrame({"cov1": cov1, "cov2": cov2, "intercept": 1})

        # make sure there is variability in the images
        kernels = rng.uniform(low=0, high=5, size=n_subjects)
        Y = [smooth_img(func_img, kernel) for kernel in kernels]

        # Set up non-parametric test
        out = non_parametric_inference(
            Y,
            design_matrix=X,
            mask=mask,
            model_intercept=False,
            second_level_contrast="intercept",
            n_perm=1 / unc_pval,
            threshold=unc_pval,
        )

        # Calculate uncorrected cluster sizes
        df = len(Y) - X.shape[1]
        neg_log_pval = -np.log10(stats.t.sf(get_data(out["t"]), df=df))
        logp_unc = new_img_like(out["t"], neg_log_pval)
        logp_unc_cluster_sizes = \
            list(get_clusters_table(logp_unc,
                                    -np.log10(unc_pval))["Cluster Size (mm3)"])

        # Calculate corrected cluster sizes
        logp_max_cluster_sizes = \
            list(get_clusters_table(out["logp_max_size"],
                                    unc_pval)["Cluster Size (mm3)"])

        # Compare cluster sizes
        logp_unc_cluster_sizes.sort()
        logp_max_cluster_sizes.sort()
        assert logp_unc_cluster_sizes == logp_max_cluster_sizes

        # Test single covariate
        X = pd.DataFrame({"intercept": [1] * len(Y)})
        non_parametric_inference(
            Y,
            design_matrix=X,
            mask=mask,
            model_intercept=False,
            second_level_contrast="intercept",
            n_perm=N_PERM,
            threshold=unc_pval,
        )

        del func_img, FUNCFILE, out, X, Y, logp_unc

test_non_parametric_inference_cluster_level_with_covariates(0)