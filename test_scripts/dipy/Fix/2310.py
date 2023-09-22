import warnings
import numpy as np
from dipy.testing import assert_true
from numpy.testing import (assert_array_almost_equal,
                           assert_equal, assert_almost_equal,
                           assert_array_equal)
from dipy.tracking import distances as pf
from dipy.tracking.streamline import set_number_of_points
#from dipy.data import get_fnames
from dipy.io.streamline import load_tractogram

def test_bundles_distances_mdf(verbose=False):
    xyz1A = np.array([[0, 0, 0], [1, 0, 0], [2, 0, 0]], dtype='float32')
    xyz2A = np.array([[0, 1, 1], [1, 0, 1], [2, 3, -2]], dtype='float32')
    xyz3A = np.array([[0, 0, 0], [1, 0, 0], [3, 0, 0]], dtype='float32')
    xyz1B = np.array([[-1, 0, 0], [2, 0, 0], [2, 3, 0]], dtype='float32')
    xyz1C = np.array([[-1, 0, 0], [2, 0, 0], [2, 3, 0], [3, 0, 0]], dtype='float32')

    tracksA = [xyz1A, xyz2A]
    tracksB = [xyz1B, xyz1A, xyz2A]
    dist = pf.bundles_distances_mdf(tracksA, tracksA)
    print(dist)
    assert_equal(dist[0, 0], 0)
    assert_equal(dist[1, 1], 0)
    assert_equal(dist[1, 0], dist[0, 1])

    # pf.bundles_distances_mdf(tracksA, tracksB)

    # tracksA = [xyz1A, xyz1A]
    # tracksB = [xyz1A, xyz1A]

    # DM2 = pf.bundles_distances_mdf(tracksA, tracksB)
    # assert_array_almost_equal(DM2, np.zeros((2, 2)))

    # tracksA = [xyz1A, xyz3A]
    # tracksB = [xyz2A]

    # DM2 = pf.bundles_distances_mdf(tracksA, tracksB)
    # if verbose:
    #     print(DM2)

    # # assert_array_almost_equal(DM2,np.zeros((2,2)))
    # DM = np.zeros(DM2.shape)
    # for (a, ta) in enumerate(tracksA):
    #     for (b, tb) in enumerate(tracksB):
    #         md = np.sum(np.sqrt(np.sum((ta-tb)**2, axis=1)))/3.
    #         md2 = np.sum(np.sqrt(np.sum((ta-tb[::-1])**2, axis=1)))/3.
    #         DM[a, b] = np.min((md, md2))

    # if verbose:
    #     print(DM)

    #     print('--------------')
    #     for t in tracksA:
    #         print(t)
    #     print('--------------')
    #     for t in tracksB:
    #         print(t)

    # assert_array_almost_equal(DM, DM2, 4)

    # with warnings.catch_warnings(record=True) as w:
    #     warnings.simplefilter("always", category=UserWarning)
    #     tracksC = [xyz1C, xyz1A]
    #     _ = pf.bundles_distances_mdf(tracksA, tracksC)
    #     print(w)
    #     assert_true(len(w) == 1)
    #     assert_true(issubclass(w[0].category, UserWarning))
    #     assert_true("not have the same number of points" in str(w[0].message))
test_bundles_distances_mdf()