from lifelines import CoxPHFitter
from lifelines.datasets import load_diabetes

df = load_diabetes()
df['gender'] = df['gender'] == 'male'

print(df.head())

cph = CoxPHFitter()
cph.fit_interval_censoring(df, lower_bound_col='left', upper_bound_col='right')
cph.print_summary()