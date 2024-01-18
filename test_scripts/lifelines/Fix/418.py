import numpy as np
import pandas as pd
import pytest
import warnings
import numpy.testing as npt
from lifelines import  KaplanMeierFitter


def test_float_weights():
        T = np.array([1,2,3,4,5])
        W = np.array([2.1,0.9,0.9,0.9,0.9])
        correct_values = np.array([1.0,0.632,0.474,0.316,0.158,0.0]).reshape((6,1))
        print(correct_values)
        kmf = KaplanMeierFitter().fit(T,weights=W)
        if(npt.assert_almost_equal(correct_values,kmf.survival_function_,decimal=3) == None):
            print("Pass")
        else:
            print("Fail")

        T = np.array([1,2])
        W = np.array([6.1,7.91])
        #correct_values = np.array([1.0,0.632,0.474,0.316,0.158,0.0]).reshape((6,1))
        kmf = KaplanMeierFitter().fit(T,weights=W)
        print(kmf.survival_function_)
        # if(npt.assert_almost_equal(correct_values,kmf.survival_function_,decimal=3) == None):
        #     print("Pass")
        # else:
        #     print("Fail")

test_float_weights()