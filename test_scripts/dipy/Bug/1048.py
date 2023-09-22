import itertools
import numpy as np
from scipy import ndimage
from dipy.align import floating
from dipy.align.metrics import SSDMetric, CCMetric, EMMetric
from numpy.testing import (assert_array_equal,
                           assert_array_almost_equal,
                           assert_raises)

def init_metric(shape, radius):
    dim = len(shape)
    metric = CCMetric(dim, radius=radius)
    metric.set_static_image(np.arange(np.prod(shape),
                                        dtype=np.float).reshape(shape),
                            np.eye(4), np.ones(dim), np.eye(3))
    metric.set_moving_image(np.arange(np.prod(shape),
                            dtype=np.float).reshape(shape),
                            np.eye(4), np.ones(dim), np.eye(3))
    return metric

# Generate many shape combinations
shapes_2d = itertools.product((5, 8), (8, 5))
shapes_3d = itertools.product((5, 8), (8, 5), (30, 50))
all_shapes = itertools.chain(shapes_2d, shapes_3d)
# expected to fail for any dimension < 2*radius + 1.
for shape in all_shapes:
    metric = init_metric(shape, 4)
    assert_raises(ValueError, metric.initialize_iteration())

# expected to pass for any dimension == 2*radius + 1.
metric = init_metric((9, 9), 4)
metric.initialize_iteration()