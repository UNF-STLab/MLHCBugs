
import os.path
import warnings
# from nilearn.version import _compare_version
import numpy as np
import pytest
from nilearn import signal as nisignal
from nilearn.signal import clean
from pandas import read_csv
import scipy.signal

def generate_signals(n_features=17, n_confounds=5, length=41,
                     same_variance=True, order="C"):
    """Generate test signals.
    All returned signals have no trends at all (to machine precision).
    Parameters
    ----------
    n_features, n_confounds : int, optional
        respectively number of features to generate, and number of confounds
        to use for generating noise signals.
    length : int, optional
        number of samples for every signal.
    same_variance : bool, optional
        if True, every column of "signals" have a unit variance. Otherwise,
        a random amplitude is applied.
    order : "C" or "F"
        gives the contiguousness of the output arrays.
    Returns
    -------
    signals : numpy.ndarray, shape (length, n_features)
        unperturbed signals.
    noises : numpy.ndarray, shape (length, n_features)
        confound-based noises. Each column is a signal obtained by linear
        combination of all confounds signals (below). The coefficients in
        the linear combination are also random.
    confounds : numpy.ndarray, shape (length, n_confounds)
        random signals used as confounds.
    """
    rng = np.random.RandomState(42)
    # Generate random confounds
    confounds_shape = (length, n_confounds)
    confounds = np.ndarray(confounds_shape, order=order)
    confounds[...] = rng.standard_normal(size=confounds_shape)
    confounds[...] = scipy.signal.detrend(confounds, axis=0)
    # Compute noise based on confounds, with random factors
    factors = rng.standard_normal(size=(n_confounds, n_features))
    noises_shape = (length, n_features)
    noises = np.ndarray(noises_shape, order=order)
    noises[...] = np.dot(confounds, factors)
    noises[...] = scipy.signal.detrend(noises, axis=0)
    # Generate random signals with random amplitudes
    signals_shape = noises_shape
    signals = np.ndarray(signals_shape, order=order)
    if same_variance:
        signals[...] = rng.standard_normal(size=signals_shape)
    else:
        signals[...] = (
            4.0 * abs(rng.standard_normal(size=signals_shape[1])) + 0.5
        ) * rng.standard_normal(size=signals_shape)
    signals[...] = scipy.signal.detrend(signals, axis=0)
    return signals, noises, confounds


# def test_standardize():
#     rng = np.random.RandomState(42)
#     n_features = 10
#     n_samples = 17
#     # Create random signals with offsets
#     a = rng.random_sample((n_samples, n_features))
#     a += np.linspace(0, 2., n_features)

#     # Test raise error when strategy is not valid option
#     with pytest.raises(ValueError, match="no valid standardize strategy"):
#         nisignal._standardize(a, standardize="foo")

#     # test warning for strategy that will be removed
#     with pytest.warns(FutureWarning, match="default strategy for standardize"):
#         nisignal._standardize(a, standardize="zscore")

#     # transpose array to fit _standardize input.
#     # Without trend removal
#     b = nisignal._standardize(a, standardize='zscore')
#     stds = np.std(b)
#     np.testing.assert_almost_equal(stds, np.ones(n_features))
#     np.testing.assert_almost_equal(b.sum(axis=0), np.zeros(n_features))

#     # Repeating test above but for new correct strategy
#     b = nisignal._standardize(a, standardize='zscore_sample')
#     stds = np.std(b)
#     np.testing.assert_almost_equal(stds, np.ones(n_features), decimal=1)
#     np.testing.assert_almost_equal(b.sum(axis=0), np.zeros(n_features))

#     # With trend removal
#     a = np.atleast_2d(np.linspace(0, 2., n_features)).T
#     b = nisignal._standardize(a, detrend=True, standardize=False)
#     np.testing.assert_almost_equal(b, np.zeros(b.shape))

#     b = nisignal._standardize(a, detrend=True, standardize="zscore_sample")
#     np.testing.assert_almost_equal(b, np.zeros(b.shape))

#     length_1_signal = np.atleast_2d(np.linspace(0, 2., n_features))
#     np.testing.assert_array_equal(length_1_signal,
#                                   nisignal._standardize(length_1_signal,
#                                                         standardize='zscore'))

#     # Repeating test above but for new correct strategy
#     length_1_signal = np.atleast_2d(np.linspace(0, 2., n_features))
#     np.testing.assert_array_equal(
#         length_1_signal,
#         nisignal._standardize(length_1_signal, standardize="zscore_sample")
#     )



def test_clean_zscore():
    rng = np.random.RandomState(42)
    n_samples = 500
    n_features = 5
    signals, _, _ = generate_signals(n_features=n_features,
                                     length=n_samples)
    signals += rng.standard_normal(size=(1, n_features))
    cleaned_signals_ = clean(signals, standardize='zscore')
    np.testing.assert_almost_equal(cleaned_signals_.mean(0), 0)
    np.testing.assert_almost_equal(cleaned_signals_.std(0), 1)

    # Repeating test above but for new correct strategy
    cleaned_signals = clean(signals, standardize='zscore_sample')
    np.testing.assert_almost_equal(cleaned_signals.mean(0), 0)
    np.testing.assert_almost_equal(cleaned_signals.std(0), 1)
    np.testing.assert_almost_equal(cleaned_signals.std(0), 1, decimal=3)

    # Show outcome from two zscore strategies is not equal
    with pytest.raises(AssertionError):
        np.testing.assert_array_equal(cleaned_signals_, cleaned_signals)

# test_standardize()
test_clean_zscore()