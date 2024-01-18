import numpy as np
import pandas as pd
from lifelines import WeibullAFTFitter
from lifelines.datasets import load_diabetes
data = pd.read_excel('/Users/n01545735/Downloads/data.xlsx',sheet_name='Sheet1')
data['start'] = data['start'].fillna(0)#left censor
data['end'] = data['end'].fillna(np.inf)#right censor
wAFT = WeibullAFTFitter()
wAFT.fit_interval_censoring(data,
                            lower_bound_col='start',
                            upper_bound_col='end',
                            formula="design * weight")
