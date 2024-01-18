import warnings
import numpy as np
import numpy.linalg as npl

from dipy.testing import assert_true
from numpy.testing import (assert_array_equal, assert_array_almost_equal,
                           assert_equal, assert_raises, run_module_suite)
from scipy.special import sph_harm as sph_harm_sp

from dipy.core.sphere import hemi_icosahedron
from dipy.core.gradients import gradient_table



from dipy.reconst.shm import QballModel

def make_fake_signal():
    hemisphere = hemi_icosahedron.subdivide(2)
    bvecs = np.concatenate(([[0, 0, 0]], hemisphere.vertices))
    bvals = np.zeros(len(bvecs)) + 2000
    bvals[0] = 0
    gtab = gradient_table(bvals, bvecs)

def test_min_signal_default():
      model = QballModel
      signal, gtab, expected = make_fake_signal()
      model_default = model(gtab, 4)
      shm_default = model_default.fit(signal).shm_coeff
      model_correct = model(gtab, 4, min_signal=1e-5)
      shm_correct = model_correct.fit(signal).shm_coeff
      assert_equal(shm_default, shm_correct)
      if (shm_default == shm_correct):
         print("Test case excuted to retesting Bug#1783 have passed")
      else:
         print("Test case excuted to retesting Bug#1783 have failed")

test_min_signal_default()