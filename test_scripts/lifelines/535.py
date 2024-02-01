from numpy.random import exponential
from lifelines import utils as survival_utils
from lifelines import KaplanMeierFitter
import numpy as np
import pandas as pd
import pytest
import numpy.testing as npt

# T_control = exponential(10, size=250)
# T_experiment = exponential(20, size=200)

# kmf_control = KaplanMeierFitter()
# kmf_control.fit(T_control, label='control')

# survival_utils.qth_survival_time(.5,kmf_control.survival_function_)

def test_qth_survival_time_with_dataframe():
    sf_df_no_index = pd.DataFrame([1.0, 0.75, 0.5, 0.25, 0.0])
    sf_df_index = pd.DataFrame([1.0, 0.75, 0.5, 0.25, 0.0], index=[10, 20, 30, 40, 50])
    sf_df_too_many_columns = pd.DataFrame([[1,2], [3,4]])

    if survival_utils.qth_survival_time(0.5, sf_df_no_index) == 2:
        print("sf_df_no_index Pass")
    else:
        print("sf_df_no_index Fail")
    if survival_utils.qth_survival_time(0.5, sf_df_index) == 30:
        print("sf_df_index Pass")
    else:
        print("sf_df_index Fail")
    with pytest.raises(ValueError):
        survival_utils.qth_survival_time(0.5, sf_df_too_many_columns)

test_qth_survival_time_with_dataframe()