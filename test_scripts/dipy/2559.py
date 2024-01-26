import os
from copy import deepcopy
import numpy as np
import subprocess
from numpy.testing import (assert_array_equal, assert_array_almost_equal,
                           assert_raises, run_module_suite)

from dipy.data import fetch_sherbrooke_3shell
from dipy.io.stateful_tractogram import Origin, Space, StatefulTractogram
from dipy.io.streamline import load_tractogram, save_tractogram

filepath_dix = {}
files, folder = fetch_sherbrooke_3shell()
for filename in files:
    filepath_dix[filename] = os.path.join(folder, filename)

file_path =  os.path.join(folder, "HARDI193.nii.gz")
response = subprocess.run("dipy_denoise_mppca "+ file_path +" --out_dir dwipreproc1.0.0 --patch_radius 3", capture_output=True, shell=True)
if("ValueError" not in str(response)):
    print("Test cases executed to retest Bug#2559 has passed")
else:
    print("Test cases executed to retest Bug#2559 has failed")
# os.system("dipy_denoise_mppca /Users/n01545735/.dipy/sherbrooke_3shell/HARDI193.nii.gz --out_dir dwipreproc1.0.0 --patch_radius 3 3 3")

