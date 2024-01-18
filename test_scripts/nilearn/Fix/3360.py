from nilearn.glm.first_level.hemodynamic_models import  _calculate_tr
import numpy as np

def test_calculate_tr():
    """ test the TR calculation
    """
    true_tr = 2
    n_vols = 5

    # create times for four volumes, shifted forward by half a TR
    # (as with fMRIPrep slice timing corrected data)
    frame_times = np.linspace(
        true_tr / 2, (n_vols * true_tr) + (true_tr / 2), n_vols + 1)
    print(frame_times)
    estimated_tr = _calculate_tr(frame_times)
    print("{:.2f}".format(round(estimated_tr,2)))
    estimated_tr = round(estimated_tr,2)
    if estimated_tr == true_tr:
        print("Pass")
    else:
        print("Fail")

test_calculate_tr()