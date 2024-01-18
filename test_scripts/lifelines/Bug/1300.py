import numpy as np
from lifelines import statistics as stats
def test_logrank_test_with_t_0():
    control_T = [1, 1, 2, 2, 3, 4, 4, 5, 5, 8, 8, 8, 8, 11, 11, 12, 12, 15, 17, 22, 23]
    control_E = np.ones_like(control_T)
    treatment_T = [6, 6, 6, 7, 10, 13, 16, 22, 23, 6, 9, 10, 11, 17, 19, 20, 25, 32, 32, 34, 25]
    treatment_E = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    result = stats.logrank_test(control_T, treatment_T, event_observed_A=control_E, event_observed_B=treatment_E, t_0=10)
    print(result)
test_logrank_test_with_t_0()