import numpy as np
import pandas as pd
from lifelines import NelsonAalenFitter

def sample_lifetimes():
    N = 100
    return (np.random.randint(1, 20, size=N), np.random.randint(2, size=N))

def test_cumulative_hazard_at_times(sample_lifetimes):
        T, _ = sample_lifetimes
        naf = NelsonAalenFitter(nelson_aalen_smoothing=False)
        naf.fit(T)
        print(naf.cumulative_hazard_at_times([0.5, 0.9, 1.0]))

test_cumulative_hazard_at_times(sample_lifetimes())