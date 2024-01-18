import numpy as np
import pytest
from nilearn.decoding.decoder import DecoderRegressor, FREMRegressor
from nilearn.decoding.tests.test_same_api import to_niimgs
from nilearn.input_data import NiftiMasker
from sklearn.datasets import make_regression
from sklearn.linear_model import RidgeCV
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR


# Regression
ridge = RidgeCV()
svr = SVR(kernel='linear')

regressors = {'ridge': (ridge, []),
              'svr': (svr, 'C')}

def test_decoder_regression():
    dim = 30
    X, y = make_regression(n_samples=100, n_features=dim**3, n_informative=dim,
                           noise=1.5, bias=1.0, random_state=42)
    X = StandardScaler().fit_transform(X)
    X, mask = to_niimgs(X, [dim, dim, dim])
    for reg in regressors:
        for screening_percentile in [100, 20, 1, None]:
            model = DecoderRegressor(estimator=reg, mask=mask,
                                     screening_percentile=screening_percentile)
            model.fit(X, y)
            y_pred = model.predict(X)
            assert r2_score(y, y_pred) > 0.95

    dim = 5
    X, y = make_regression(n_samples=100, n_features=dim**3, n_informative=dim,
                           noise=1.5, bias=1.0, random_state=42)
    X = StandardScaler().fit_transform(X)
    X, mask = to_niimgs(X, [dim, dim, dim])

    for clustering_percentile in [100, 99]:
        model = FREMRegressor(estimator=reg, mask=mask,
                              clustering_percentile=clustering_percentile,
                              screening_percentile=90,
                              cv=10)
        model.fit(X, y)
        y_pred = model.predict(X)
        assert r2_score(y, y_pred) > 0.95

if __name__ == '__main__':
    test_decoder_regression()