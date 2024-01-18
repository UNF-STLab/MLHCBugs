from lifelines.datasets import load_rossi
from lifelines import CoxPHFitter


def test_conditional_after_with_strata_in_prediction2(rossi, cph):
    # cph.fit(df = rossi, duration_col=rossi["week"], event_col=rossi["arrest"], strata=["race"])
    # censored_subjects = rossi.loc[~rossi["arrest"].astype(bool)]
    # censored_subjects_last_obs = censored_subjects["week"]
    # pred = cph.predict_survival_function(censored_subjects, conditional_after=censored_subjects_last_obs)
    cph.fit(rossi, duration_col="week", event_col="arrest", strata=["race"])
    censored_subjects = rossi.loc[~rossi["arrest"].astype(bool)]
    censored_subjects_last_obs = censored_subjects["week"]
    pred = cph.predict_survival_function(censored_subjects, conditional_after=censored_subjects_last_obs)
    print(pred)


rossi = load_rossi()
cph = CoxPHFitter()
test_conditional_after_with_strata_in_prediction2(rossi, cph)