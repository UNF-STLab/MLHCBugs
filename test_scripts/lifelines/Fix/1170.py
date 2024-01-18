from lifelines import WeibullFitter, KaplanMeierFitter

def test_label_is_not_overwritten():
        fitter = WeibullFitter(label="Weibull")
        fitter.fit([1, 2, 3, 4], event_observed=[1, 1, 1, 1])
        print(fitter.fit([1, 2, 3, 4], event_observed=[1, 1, 1, 1]))
        assert fitter._label == "Weibull"

        fitter = KaplanMeierFitter(label="KM")
        fitter.fit([1, 2, 3, 4], event_observed=[1, 1, 1, 1])
        assert fitter._label == "KM"
test_label_is_not_overwritten()