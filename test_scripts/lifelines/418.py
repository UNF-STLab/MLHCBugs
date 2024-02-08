import numpy as np
import pandas as pd
import numpy.testing as npt
from lifelines import  KaplanMeierFitter
import random
from itertools import permutations 
import operator

def test_float_weights():
        T = np.array([1,2,3,4,5])
        W = np.array([2.1,0.9,0.9,0.9,0.9])
        correct_values = np.array([1.0,0.632,0.474,0.316,0.158,0.0]).reshape((6,1))
        print(correct_values)
        kmf = KaplanMeierFitter().fit(T,weights=W)
        if(npt.assert_almost_equal(correct_values,kmf.survival_function_,decimal=3) == None):
            print("Pass")
        else:
            print("Fail")

# test_float_weights()

def inputGenerator(length: int):
    timeline = []
    weights = []
    for i in range(length):
        timeline.append(random.random()*length+random.random())
        weights.append(random.random()*length+random.random())
    timeline = np.array(timeline, dtype=np.int32)
    weights = np.array(weights, dtype=np.float32)
  
    return timeline, weights

def test_floatVsint_weights_mr(timeline, weights):
        floatweight2 = []
        floatweight3 = []
        for i in range(len(weights)):
             floatweight2.append(round(weights[i],2))
        print(floatweight2)
        kmf_floatweights = KaplanMeierFitter().fit(timeline,weights=np.array(floatweight2))
        # for i in range(len(weights)):
        #      floatweight3.append(round(weights[i],3))
        # print(floatweight3)
        for i in range(len(weights)):
             weights[i] = int(weights[i])
        print(weights)
        kmf_intweights = KaplanMeierFitter().fit(timeline,weights=np.array(floatweight2))
        print(kmf_intweights.survival_function_)
        print(kmf_floatweights.survival_function_)
        npt.assert_array_compare(operator.__ne__, kmf_intweights.survival_function_, kmf_floatweights.survival_function_)

length = 5
timeline, weights= inputGenerator(length)
test_floatVsint_weights_mr(timeline, weights)