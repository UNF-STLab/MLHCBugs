import numpy as np
from numpy.testing import (assert_equal, assert_array_almost_equal,
                           assert_raises)
from dipy.align.streamlinear import (compose_matrix44, decompose_matrix44,
                                     transform_streamlines, whole_brain_slr,
                                     slr_with_qbx)
from dipy.io.streamline import load_tractogram
from dipy.data import get_fnames
from dipy.tracking.streamline import Streamlines

def test_slr_one_streamline():
    fname = get_fnames('fornix')

    fornix = load_tractogram(fname, 'same',
                             bbox_valid_check=False).streamlines

    f = Streamlines(fornix)
    f1_one = Streamlines([f[0]])
    f2 = f.copy()
    f2._data += np.array([50, 0, 0])

    assert_raises(ValueError, slr_with_qbx, f1_one, f2, verbose=False,
                  rm_small_clusters=50, greater_than=20,
                  less_than=np.inf, qbx_thr=[2], progressive=True)

    assert_raises(ValueError, slr_with_qbx, f2, f1_one, verbose=False,
                  rm_small_clusters=50, greater_than=20,
                  less_than=np.inf, qbx_thr=[2], progressive=True)

test_slr_one_streamline()