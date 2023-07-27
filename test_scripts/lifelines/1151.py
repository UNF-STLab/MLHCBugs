import numpy as np
import pandas as pd
from lifelines import KaplanMeierFitter

# Data
np.random.seed(1)
left0 = np.random.normal(loc=60, scale=2, size=20)
add_time = np.random.normal(loc=100, scale=2, size=10)
right1 = left0[0:10] + add_time
right0 = right1.tolist() + [np.inf] * 10

pd.DataFrame({"left0": left0, "right0": right0})

# KaplanMeier
model = KaplanMeierFitter()
model.fit_interval_censoring(lower_bound=left0, upper_bound=right0)
model.cumulative_density_
model.survival_function_