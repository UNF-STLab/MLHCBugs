import numpy as np
from nilearn.signal import clean

def main():
    x = np.array([
            np.sin(np.linspace(0, 100, 100) * 1.5),
            np.sin(np.linspace(0, 100, 100) * 3.),
            np.sin(np.linspace(0, 100, 100) / 8.),
        ]).T
    x_orig = x.copy()

    # This should do nothing
    out = clean(x, standardize=False, detrend=False, t_r=1.0, high_pass=0.2)
    # clean should not modify inputs
    assert np.array_equal(x_orig, x)

if __name__ == '__main__':
    main()