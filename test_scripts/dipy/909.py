import numpy as np
from dipy.tracking.streamline import values_from_volume

data3D = np.ones((2, 2, 2))
streamlines = np.ones((10, 1, 3))
print({
    'returned': values_from_volume(data3D, streamlines).shape,
    'expected': '(10, 1)'
})

data4D = np.ones((2, 2, 2, 2))
streamlines = np.ones((10, 1, 3))
values_from_volume(data4D, streamlines).shape