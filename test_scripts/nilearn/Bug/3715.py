from nilearn.decoding.decoder import Decoder
from sklearn.datasets import load_iris, make_classification, make_regression
# from nilearn.decoding.tests.test_same_api import to_niimgs
N_SAMPLES = 100
import nibabel
import numpy as np
from nilearn.masking import _unmask_from_to_3d_array

def to_niimgs(X, dim):
    p = np.prod(dim)
    assert len(dim) == 3
    assert X.shape[-1] <= p
    mask = np.zeros(p).astype(bool)
    mask[:X.shape[-1]] = 1
    assert mask.sum() == X.shape[1]
    mask = mask.reshape(dim)
    X = np.rollaxis(
        np.array([_unmask_from_to_3d_array(x, mask) for x in X]), 0, start=4)
    affine = np.eye(4)
    return nibabel.Nifti1Image(X, affine), nibabel.Nifti1Image(
        mask.astype(np.float64), affine)

def _make_binary_classification_test_data(n_samples=N_SAMPLES):
    X, y = make_classification(
        n_samples=n_samples,
        n_features=125,
        scale=3.0,
        n_informative=5,
        n_classes=2,
        random_state=42,
    )
    X, mask = to_niimgs(X, [5, 5, 5])
    return X, y, mask
def binary_classification_data():
    """Use for test where classification is actually performed."""
    return _make_binary_classification_test_data(n_samples=N_SAMPLES)

def test_decoder_param_grid_sequence(binary_classification_data):
    X, y, _ = binary_classification_data
    n_cv_folds = 10
    param_grid = [
        {
            "penalty": ["l2"],
            "C": [100, 1000],
            "random_state": [42],  # fix the seed for consistent behaviour
        },
        {
            "penalty": ["l1"],
            "dual": [False],  # "dual" is not in the first dict
            "C": [100, 10],
            "random_state": [42],  # fix the seed for consistent behaviour
        },
    ]

    model = Decoder(param_grid=param_grid, cv=n_cv_folds)
    model.fit(X, y)

    for best_params in model.cv_params_.values():
        for param_list in best_params.values():
            # assert len(param_list) == n_cv_folds
            print(len(param_list))


binary_classification_dat = binary_classification_data()
test_decoder_param_grid_sequence(binary_classification_dat)
