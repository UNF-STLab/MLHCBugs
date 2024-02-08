import numpy as np
import operator
import numpy.testing as npt
from itertools import permutations
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

    npt.assert_array_equal(new_sl_1, np.array([[1, 1, 1], [3, 3, 3]]))
    npt.assert_array_equal(new_sl_2, np.array([[1, 1, 1], [2, 2, 2]]))
    npt.assert_array_equal(new_sl_3, new_sl_1)
    npt.assert_array_equal(new_sl_4, np.array([[1, 1, 2], [1, 2, 3], [3, 3, 3],[1, 1, 1]]))       


# test_compress_streamlines_identical_points()
def test_compress_streamlines_permutations_mr(inputList):
     slPermutations = list(permutations(inputList))
     compressedsl = compress_streamlines(np.array(slPermutations))
     for i in range(len(compressedsl)):
        if i>0:
            npt.assert_array_compare(operator.__ne__, list(compressedsl[i-1]),list(compressedsl[i]))
     return compressedsl

def test_compress_streamlines_adddatapoints_mr(inputList, inputsl):
    # inputsl = list(inputsl)
    # newmodifiedlist= np.array(inputsl)``
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
            npt.assert_array_compare(operator.__ne__, list(compressedmodsl[i-1]),list(compressedmodsl[i]))  


inputList =[1,2,1]
outputsl = test_compress_streamlines_permutations_mr(inputList)
test_compress_streamlines_adddatapoints_mr(inputList, outputsl)
test_compress_streamlines_identical_points()

def test_compress_streamlines_removedatapoints_mr():
    for i in range(len(inputsl)):
         if i%5!=0:
            inputsl.remove(input[i])
    inputarray = np.array(inputsl)
    compressedmodsl = compress_streamlines(inputsl)
    for i in range(len(compressedmodsl)):
         if i>0:
            npt.assert_array_compare(operator.__ne__, list(compressedmodsl[i-1]),list(compressedmodsl[i])) 
    return