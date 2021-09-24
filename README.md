# MLBugs

| Identifier      | Project name               | Number of bugs | Active bug ids      | Deprecated bug ids (\*) |
|-----------------|----------------------------|---------------:|---------------------|-------------------------| 
| BCC             | BCC                        |       1        | 1                   | None                    |
| MZP             | MZP                        |       2        | 2,3                 | None                    |
| RGAN            | RGAN                       |       1        | 4                   | None                    |
| nilearn         | nilearn                    |       11       | 5-15                | None                    |
| lifelines       | lifelines                  |       5        | 16-20               | None                    |



Bug ID description:

1) Input shape.
2) Namespace' object has no attribute 'samples_train'
3) Input shape Dimension error
4) Logic error makes an conditional irrelevant.
5) Transform should never modify object. (issue #71)
6) Open ended if elif allows for dimension error. (issue #162)
7) Variable defined twice evaded coverage. (# 2959)
8) Incorrect/unwanted data modification. (# 325)
9) Colobar code breaks when a map is fully empty (#510)
10) Python int too large to convert to C long (#658)
11) Nilearn resampling doesn't support int16, throws RuntimeError: data type not supported (#817)
12) fetch_atlas_harvard_oxford and symmetric_split (#914)
13) ConnectivityMeasure requires 3D data (#941) 
14) Decoder with ridge_regressor fails on oasis vbm example (#2360)
15) clean function modifies the input time series object if performing pass-filtering without detrending (#2475)
16) Nelson Aalen hazard off by a factor of 1/2 #186
17) Float weights in Kaplan-Meier #418
18) qth_survival_time raising ambiguous truth value error #535
19) Shape mismatch when using conditional_after with strata in CoxPHFitter #880
20) KMF fit fails with tuples #1034
