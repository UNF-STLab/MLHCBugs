import numpy as np

def test_calculate_tr():
    """ test the TR calculation
    """
    true_tr = 0.75
    n_vols = 4

    # create times for four volumes, shifted forward by half a TR
    # (as with fMRIPrep slice timing corrected data)
    frame_times = np.linspace(
        true_tr / 2, (n_vols * true_tr) + (true_tr / 2), n_vols + 1)

    #estimated_tr = _calculate_tr(frame_times)
    estimated_tr = float(frame_times.max()) / (np.size(frame_times) - 1) 
    if estimated_tr == true_tr:
        print("Pass")
    else:
        print("Fail")

test_calculate_tr()