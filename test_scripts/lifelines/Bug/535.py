from numpy.random import exponential
from lifelines import utils as survival_utils
from lifelines import KaplanMeierFitter

T_control = exponential(10, size=250)
T_experiment = exponential(20, size=200)

kmf_control = KaplanMeierFitter()
kmf_control.fit(T_control, label='control')

survival_utils.qth_survival_time(.5,kmf_control.survival_function_)