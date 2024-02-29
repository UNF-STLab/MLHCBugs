from lifelines import WeibullFitter, KaplanMeierFitter
from lifelines.datasets import load_waltons
import numpy.testing as npt
import operator

def test_label_is_not_overwritten():
        fitter = WeibullFitter(label="Weibull")
        fitter.fit([1, 2, 3, 4], event_observed=[1, 1, 1, 1])
        assert fitter._label == "Weibull"
        fitter = KaplanMeierFitter(label="KM")
        fitter.fit([1, 2, 3, 4], event_observed=[1, 1, 1, 1])
        assert fitter._label == "KM"
test_label_is_not_overwritten()

def test_different_label(label1, label2):
        waltons = load_waltons()
        wbfL1 = WeibullFitter(label=label1)
        wbfL1.fit(waltons['T'], waltons['E'])
        wbfL2 = WeibullFitter(label=label2)
        wbfL2.fit(waltons['T'], waltons['E'])
        npt.assert_array_compare(operator.__ne__, wbfL1, wbfL2)

test_different_label("Weibull", "KM")