import pandas as pd
import lifelines
df = pd.DataFrame()
df['t'] = [1,2,3,4,5]
df['d'] = [1,1,1,1,1]
df['w1'] = [2,1,1,1,1]
df['w2'] = [2.1,0.9,0.9,0.9,0.9]

y = lifelines.KaplanMeierFitter().fit(df['t'],weights=df['w2'])

print('''Expected values:
=====================
KM_estimate  timeline             
0.0             1.000
1.0             0.632
2.0             0.474
3.0             0.316
4.0             0.158
5.0             0.000
''')

print('\n\nCalculated values:\n=====================')
print(y.survival_function_)