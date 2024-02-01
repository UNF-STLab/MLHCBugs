import numpy as np
import os
import tempfile

import pytest

from nilearn._utils.numpy_conversions import as_ndarray

a = np.asarray([0, 1, 2], dtype=np.int8,order='C')
print(a)
#b = as_ndarray(a, dtype=bool)  # array([False, True, True], dtype=bool)
c = as_ndarray(a, dtype=np.int8)  # array([0, 1, 2], dtype=numpy.int8)

filename = os.path.join(os.path.dirname(__file__), "data", "mmap.dat")

    # same dtype, no copy requested
data = np.arange(12, dtype='float32')
data.resize((3,4))
arr1 = np.memmap(filename, dtype=None, mode='w+', shape=(3,4))
arr1[:] = data[:]
arr2 = as_ndarray(arr1,dtype=np.int8, order='C')
print(isinstance(arr1, np.memmap))
print(arr1)
print(arr2)