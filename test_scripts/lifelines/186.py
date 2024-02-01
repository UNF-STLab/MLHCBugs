import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import lifelines
import random

n = 1000

testData = pd.DataFrame(index=range(n))
testData['duration'] = np.random.exponential(1,(n,))

b = 1
naf = lifelines.NelsonAalenFitter()
naf.fit(testData['duration'])
ax = naf.plot_hazard(bandwidth=b)

plt.show()