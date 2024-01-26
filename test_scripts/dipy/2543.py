import json
import os
from copy import deepcopy

import numpy as np
import numpy.testing as npt


from dipy.data import fetch_gold_standard_io
from dipy.io.stateful_tractogram import Origin, Space, StatefulTractogram
from dipy.io.streamline import load_tractogram, save_tractogram


filepath_dix = {}
files, folder = fetch_gold_standard_io()
for filename in files:
    filepath_dix[filename] = os.path.join(folder, filename)

# with open(filepath_dix['points_data.json']) as json_file:
#     points_data = dict(json.load(json_file))

# with open(filepath_dix['streamlines_data.json']) as json_file:
#     streamlines_data = dict(json.load(json_file))

sft_2_points_data = {
    "color_x": [
        [[60], [60], [60], [60], [60], [60], [60], [60]],
        [[0], [0], [0], [0], [0], [0], [0], [0]],
        [[128], [128], [128], [128], [128], [128], [128], [128]],
        [[208], [208], [208], [208], [208], [208], [208], [208]],
        [[255], [255], [255], [255], [255], [255], [255], [255]],
        [[205], [205], [205], [205], [205], [205], [205], [205]],
        [[255], [255], [255], [255], [255], [255], [255], [255]],
        [[45], [45], [45], [45], [45], [45], [45], [45]],
        [[180], [180], [180], [180], [180], [180], [180], [180]],
        [[222], [222], [222], [222], [222], [222], [222], [222]],
        [[0], [0], [0], [0], [0], [0], [0], [0]],
        [[0], [0], [0], [0], [0], [0], [0], [0]],
        [[0], [0], [0], [0], [0], [0], [0], [0]],
    ],
    "color_z": [
        [[20], [20], [20], [20], [20], [20], [20], [20]],
        [[165], [165], [165], [165], [165], [165], [165], [165]],
        [[128], [128], [128], [128], [128], [128], [128], [128]],
        [[224], [224], [224], [224], [224], [224], [224], [224]],
        [[144], [144], [144], [144], [144], [144], [144], [144]],
        [[0], [0], [0], [0], [0], [0], [0], [0]],
        [[0], [0], [0], [0], [0], [0], [0], [0]],
        [[82], [82], [82], [82], [82], [82], [82], [82]],
        [[105], [105], [105], [105], [105], [105], [105], [105]],
        [[196], [196], [196], [196], [196], [196], [196], [196]],
        [[255], [255], [255], [255], [255], [255], [255], [255]],
        [[0], [0], [0], [0], [0], [0], [0], [0]],
        [[255], [255], [255], [255], [255], [255], [255], [255]],
    ],
    "color_y": [
        [[220], [220], [220], [220], [220], [220], [220], [220]],
        [[255], [255], [255], [255], [255], [255], [255], [255]],
        [[128], [128], [128], [128], [128], [128], [128], [128]],
        [[64], [64], [64], [64], [64], [64], [64], [64]],
        [[30], [30], [30], [30], [30], [30], [30], [30]],
        [[0], [0], [0], [0], [0], [0], [0], [0]],
        [[255], [255], [255], [255], [255], [255], [255], [255]],
        [[160], [160], [160], [160], [160], [160], [160], [160]],
        [[255], [255], [255], [255], [255], [255], [255], [255]],
        [[176], [176], [176], [176], [176], [176], [176], [176]],
        [[0], [0], [0], [0], [0], [0], [0], [0]],
        [[255], [255], [255], [255], [255], [255], [255], [255]],
        [[0], [0], [0], [0], [0], [0], [0], [0]],
    ],
}
def test_StatefulTractogram_are_compatible():
    sft_1 = load_tractogram(filepath_dix['gs.trk'], filepath_dix['gs.nii'])
    sft_2 = load_tractogram(filepath_dix['gs.trk'], filepath_dix['gs.nii'])
    sft_2.data_per_point = sft_2_points_data
    print(sft_1.get_data_per_point_keys(), sft_2.get_data_per_point_keys())
    if StatefulTractogram.are_compatible(sft_1, sft_2) == True:
        print("Test cases executed to retest Bug#2543 has passed")
    else:
        print("Test cases executed to retest Bug#2543 has Failed")

test_StatefulTractogram_are_compatible()

# def test_create_from_sft():
#     sft_1 = load_tractogram(filepath_dix['gs.tck'], filepath_dix['gs.nii'])
#     sft_2 = StatefulTractogram.from_sft(
#         sft_1.streamlines, sft_1,
#         data_per_point=sft_1.data_per_point,
#         data_per_streamline=sft_1.data_per_streamline)