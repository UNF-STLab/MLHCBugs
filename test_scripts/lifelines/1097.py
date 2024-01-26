import os
# import pytest
import pandas as pd
import numpy as np
import scipy
from matplotlib import pyplot as plt
from lifelines import (
    KaplanMeierFitter,
    CoxPHFitter,
)


from lifelines.plotting import add_at_risk_counts
from lifelines.datasets import (
    load_rossi,
)
from lifelines.calibration import survival_probability_calibration

def kmf():
        return KaplanMeierFitter()

def test_kmf_add_at_risk_counts_with_specific_rows(kmf):
        T = np.random.exponential(10, size=(10))
        E = np.random.binomial(1, 0.8, size=(10))
        T = np.array(T)
        E = np.array(E)
        kmf.fit(T, E)

        fig = plt.figure()
        ax = fig.subplots(1, 1)
        kmf.plot(ax=ax)
        add_at_risk_counts(kmf, ax=ax, rows_to_show=["Censored", "At risk"], labels=False)

        plt.title("test_kmf_add_at_risk_counts_with_specific_rows")
        plt.show()

# def test_survival_probability_calibration():
#         rossi = load_rossi()
#         cph = CoxPHFitter().fit(rossi, "week", "arrest")
#         survival_probability_calibration(cph, rossi, 25)
#         plt.title("test_survival_probability_calibration")
#         plt.show()

# def test_survival_probability_calibration_on_out_of_sample_data():
#         rossi = load_rossi()
#         rossi = rossi.sample(frac=1.0)
#         cph = CoxPHFitter().fit(rossi.loc[:300], "week", "arrest")
#         survival_probability_calibration(cph, rossi.loc[300:], 25)
#         plt.title("test_survival_probability_calibration_on_out_of_sample_data")
#         plt.show()

kmf = kmf()
test_kmf_add_at_risk_counts_with_specific_rows(kmf)
# test_survival_probability_calibration()
# test_survival_probability_calibration_on_out_of_sample_data()