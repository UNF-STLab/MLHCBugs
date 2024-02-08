import numpy as np
from dipy.testing import assert_true
from numpy.testing import (assert_array_almost_equal,
                           assert_equal, assert_almost_equal,
                           assert_array_equal)
from dipy.tracking import distances as pf
from itertools import permutations
import dipy.tracking.streamline as dts
from warnings import warn
import random

A = np.load('/Users/n01545735/Downloads/max_asymmetric_mdf.npy')
dist = dts.bundles_distances_mdf(A, A)
assert_equal(np.sum(abs(dist-dist.T)),0.0)

def test_bundles_distances_mdf_sametracks(trackA):
    # xyz1A = np.array([[0, 1.0232343234, 0], [2.98374589734, 0, 0], [3.93458745, 1.0823498374, 0]], dtype='float32')
    # xyz2A = np.array([[0, 4.98623476, 5.97834857], [67.034898454595, 0, 1.23423523], [2.23457645, 3.2436575, -2.47657354]], dtype='float32')
    # tracksA = [xyz1A, xyz2A]

    dist = pf.bundles_distances_mdf(trackA, trackA)
    assert_equal(dist[0, 0], 0)
    assert_equal(dist[1, 1], 0)
    assert_equal(dist[1, 0], dist[0, 1])


def test_bundles_distances_mdf_differenttracks(trackA, trackB):
    # xyz1A = np.array([[0, 1, 0], [2, 0, 0]], dtype='float32')
    # xyz2A = np.array([[0.234234, 4, 5], [4, 0.45452234, 1]], dtype='float32')
    # tracksA = [xyz1A, xyz2A]
    # tracksB = [xyz2A, xyz1A]
    dist1 = pf.bundles_distances_mdf(trackA, trackB)
    dist2 = pf.bundles_distances_mdf(trackB, trackA)
    assert_equal(dist1[0, 0], dist2[1, 1])
    assert_equal(dist1[0, 1], dist2[1, 0])
    assert_equal(np.sum(abs(dist1-dist2.T)),0.0)


def source_code_replication(trackA, trackB):
    # xyz1A = np.array([[0, 1, 0], [2, 0, 0]], dtype='float32')
    # xyz2A = np.array([[0.234234, 4, 5], [4, 0.45452234, 1]], dtype='float32')
    # tracksA = [xyz1A, xyz2A]
    # tracksB = [xyz2A, xyz1A]
    lentA = len(trackA)
    lentB = len(trackB)
    if lentA != lentB:
        w_s = "Streamlines do not have the same number of points. "
        w_s += "All streamlines need to have the same number of points. "
        w_s += "Use dipy.tracking.streamline.set_number_of_points to adjust "
        w_s += "your streamlines"
        warn(w_s)
    tracksA32 = np.zeros((lentA,), dtype=object)
    tracksB32 = np.zeros((lentB,), dtype=object)
    distMat = np.zeros((lentA,lentB), dtype=np.double)

    for i in range(lentA):
        tracksA32[i] = np.ascontiguousarray(trackA[i], dtype=np.dtype(np.float32))
        # print(f'tracksA32 {i}: {tracksA32[i]}')
    for i in range(lentB):
        tracksB32[i] = np.ascontiguousarray(trackB[i], dtype=np.dtype(np.float32))
        # print(f'tracksB32 {i}: {tracksB32[i]}')
    
    for i in range(lentA):
        t1 = tracksA32[i]
        t1_ptr = t1.data
        # print(f't1 = {t1}, t1_ptr = {t1_ptr}')
        for j in range(lentB):
            t2 = tracksB32[j]
            t2_ptr = t2.data
            # print(f't1 = {t1}, t2 = {t2}')
            distance = []
            distancef = []
            average = []
            averagef = []
            for k in range(len(t1)):
                temp = t1[k] - t2[k]
                tempf = t1[k] - t2[-k]
                distance.append(np.sqrt(np.sum(np.square(temp))))
                distancef.append(np.sqrt(np.sum(np.square(tempf))))
                # print(distance)
                average = sum(distance)/len(t1)
                averagef = sum(distancef)/len(t1)
                # print(average)
                if average<averagef:
                    distMat[i,j]=average
                else:
                    distMat[i,j]=averagef
    assert_equal(np.sum(abs(distMat-distMat.T)),0.0)

def permutation(length):
    sl1 = []
    sl2 = []
    sl3 = []
    sl4 = []
    for i in range(length):
        sl1.append(random.random())
        sl2.append(random.random())
        sl3.append(random.random())
        sl4.append(random.random())
    sl1 = np.array(list(permutations(sl1)), dtype=np.float32)
    sl2 = np.array(list(permutations(sl2)), dtype=np.float32)
    sl3 = np.array(list(permutations(sl3)), dtype=np.float32)
    sl4 = np.array(list(permutations(sl4)), dtype=np.float32)
    # trackA = [sl1, sl2, sl3, sl4]
    # trackB = [sl2, sl3, sl2, sl1]
    # trackA = [sl1, sl2, sl3, sl4]
    # trackB = [sl2, sl1, sl3, sl4]
    trackA = [sl1, sl2]
    trackB = [sl2, sl1]
    return trackA, trackB
length = 3    
trackA, trackB = permutation(length)
test_bundles_distances_mdf_differenttracks(trackA, trackB)
test_bundles_distances_mdf_sametracks(trackA)
source_code_replication(trackA, trackB)