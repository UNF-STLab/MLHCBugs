import numpy as np
from pandas.testing import assert_frame_equal, assert_series_equal, assert_index_equal
import numpy.testing as npt

from lifelines import (
    WeibullFitter,
    NelsonAalenFitter,
    KaplanMeierFitter,
)

def univariate_fitters():
        return [
            KaplanMeierFitter,
            NelsonAalenFitter,
            WeibullFitter,
        ]
def positive_sample_lifetimes():
    N = 100
    return (np.random.randint(1, 20, size=N), np.random.randint(2, size=N))
def test_lists_and_tuples_as_input(positive_sample_lifetimes, univariate_fitters):
        T, C = positive_sample_lifetimes
        for f in univariate_fitters:
            fitter = f()

            if isinstance(fitter, NelsonAalenFitter):
                with_array = fitter.fit(T, C).cumulative_hazard_
                with_list = fitter.fit(list(T), list(C)).cumulative_hazard_
                with_tuple = fitter.fit(tuple(T), tuple(C)).cumulative_hazard_
                if assert_frame_equal(with_list, with_array) == None:
                    status = True
                else:
                    return False
                if assert_frame_equal(with_tuple, with_array) == None:
                    status = True
                else:
                    return False


            else:
                with_array = fitter.fit(T, C).survival_function_
                with_list = fitter.fit(list(T), list(C)).survival_function_
                with_tuple = fitter.fit(tuple(T), tuple(C)).survival_function_
                if assert_frame_equal(with_list, with_array) == None:
                    status = True
                else:
                    return False
                if assert_frame_equal(with_tuple, with_array) == None:
                    status = True
                else:
                    return False
        return status

if test_lists_and_tuples_as_input(positive_sample_lifetimes(), univariate_fitters()) == True:
    print("Pass")
else:
    print("Fail")