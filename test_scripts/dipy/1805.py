import warnings
import types

import numpy as np
from numpy.linalg import norm
import numpy.testing as npt
from dipy.testing.memory import get_type_refcount
from dipy.testing import assert_arrays_equal
from itertools import permutations
from dipy.testing import assert_true
from numpy.testing import (assert_array_equal, assert_array_almost_equal,
                           assert_raises, assert_allclose,
                           assert_almost_equal, assert_equal)

from dipy.tracking.streamlinespeed import compress_streamlines


def test_compress_streamlines_identical_points():

    sl_1 = np.array([[1, 1, 1], [1, 1, 1], [2, 2, 2], [3, 3, 3], [3, 3, 3]])
    sl_2 = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1], [2, 2, 2]])
    sl_3 = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [3, 3, 3], [3, 3, 3]])
    sl_4 = np.array([[1, 1, 2], [1, 1, 2], [1, 1, 2], [1, 1, 2], [1, 2, 3], [3, 3, 3], [1, 1, 1]])
    new_sl_1 = compress_streamlines(sl_1)
    new_sl_2 = compress_streamlines(sl_2)
    new_sl_3 = compress_streamlines(sl_3)
    new_sl_4 = compress_streamlines(sl_4)
    # print(new_sl_4)
    # TC1 = npt.assert_array_equal(new_sl_1, np.array([[1, 1, 1], [3, 3, 3]]))
    # TC2 = npt.assert_array_equal(new_sl_2, np.array([[1, 1, 1], [2, 2, 2]]))
    # TC3 = npt.assert_array_equal(new_sl_3, new_sl_1)
    TC4 = npt.assert_array_equal(new_sl_4, np.array([[1, 1, 2], [1, 2, 3], [3, 3, 3],[1, 1, 1]]))       
    # if (TC1 == None and TC2 == None and TC3 == None and TC4 == None):
    if (TC4 == None):
         print("Test cases executed to retest Bug#1805 has passed")
    else:
         print("Test cases executed to retest Bug#1805 has failed")

# test_compress_streamlines_identical_points()
def test_compress_streamlines_permutations_mr(inputList):
     slPermutations = list(permutations(inputList))
     compressedsl = compress_streamlines(np.array(slPermutations))
     for i in range(len(compressedsl)):
         if i>0:
            if list(compressedsl[i-1]) != list(compressedsl[i]):
                 status = True
            else:
                 status = False
                 break
     print(status)
     return status, compressedsl

def test_compress_streamlines_modify_mr(inputList, inputsl):
    # inputsl = list(inputsl)
    # newmodifiedlist= np.array(inputsl)``
    print(inputsl[2])
    for i in range(len(inputsl)):
         if i == 0:
            newmodifiedlist = np.append([inputsl[i]], [inputsl[i]], axis=0)
            newmodifiedlist= np.append(newmodifiedlist, [inputsl[i]],axis=0)
            newmodifiedlist= np.append(newmodifiedlist, [inputsl[i]],axis=0)
            newmodifiedlist= np.append(newmodifiedlist, [inputsl[i]],axis=0)
         else:     
            newmodifiedlist = np.append(newmodifiedlist, [inputsl[i]], axis=0)
         if i%2!=0:
              newmodifiedlist= np.append(newmodifiedlist, [inputsl[i]],axis=0)
              newmodifiedlist= np.append(newmodifiedlist, [inputsl[i]],axis=0)
    inputarray = np.array(newmodifiedlist)
    compressedmodsl = compress_streamlines(inputarray)        
    for i in range(len(compressedmodsl)):
         if i>0:
            if list(compressedmodsl[i-1]) != list(compressedmodsl[i]):
                 status = True
            else:
                 status = False
                 break
    print(status)   


inputList =[1,2,1]
status, outputsl = test_compress_streamlines_permutations_mr(inputList)
test_compress_streamlines_modify_mr(inputList, outputsl)
test_compress_streamlines_identical_points()


# def test_compress_streamlines_duplicatestreamline_mr(compressedsl):
#      sl = compressedsl
#      duplicatesl = np.concatenate((sl,sl),axis=0)
#      duplicatesl = duplicatesl.tolist()
#      compressedduplicatesl = compress_streamlines(np.array(duplicatesl))
#      print(sl)
#      print(compressedduplicatesl)
#      return sl, compressedduplicatesl

# test_compress_streamlines_permutations_mr([1,2,1])
# print(compressedsl)
# sl, compressedduplicatesl = test_compress_streamlines_duplicatestreamline_mr(compressedsl)
# if (len(sl) == len(compressedduplicatesl)):
#    print("Test cases executed to retest Bug#1805 has passed")
# else:
#     print("Test cases executed to retest Bug#1805 has failed")
