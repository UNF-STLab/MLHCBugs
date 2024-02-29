import numpy as np
import pandas as pd
import numpy.testing as npt
from lifelines import  KaplanMeierFitter
import random
from itertools import permutations 
import operator
from lifelines import KaplanMeierFitter
from lifelines.datasets import load_waltons

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

def randomInputGenerator(length: int):
    timeline = []
    weights = []
    for i in range(length):
        timeline.append(random.random()*length+random.random())
        weights.append(random.random()*length+random.random())
    timeline = np.array(timeline, dtype=np.int32)
    weights = np.array(weights, dtype=np.float32)
    return timeline, weights

def inputGenerator(length: int, weight: float):
    timeline = []
    weights = []
    for i in range(length):
        timeline.append(random.random()*length+random.random())
        weights.append(weight)
    timeline = np.array(timeline, dtype=np.int32)
    weights = np.array(weights, dtype=np.float32)
    return timeline, weights

def test_floatVsint_weights_mr(timeline, weights):
        floatweight2 = []
        floatweight3 = []
        for i in range(len(weights)):
             floatweight2.append(round(weights[i],2))
        # print(floatweight2)
        # kmf_floatweights = KaplanMeierFitter().fit(timeline,weights=np.array(floatweight2))
        # # for i in range(len(weights)):
        # #      floatweight3.append(round(weights[i],3))
        # # print(floatweight3)
        # for i in range(len(weights)):
        #      weights[i] = int(weights[i])
        # print(weights)
        kmf_intweights = KaplanMeierFitter().fit(timeline,weights=np.array(floatweight2))
        print(kmf_intweights.survival_function_)
        # print(kmf_floatweights.survival_function_)
        # npt.assert_array_compare(operator.__ne__, kmf_intweights.survival_function_, kmf_floatweights.survival_function_)

# length = len([0.6776002789377035, 0.5199387521520817, 0.24095011567819735, 0.8794319039525854, 0.37299931753189697, 0.46583141168014686, 0.14088934480270487, 0.1833101226357976, 0.41216910538498863, 0.7524773619668541, 0.45760439808464404, 0.3869531362912859, 0.8997403715680454, 0.32747882230722714, 0.09498929438871773, 0.5456874293524919, 0.5683084289604395, 0.253107451031219, 0.19341324756661726, 0.07542076680679066, 0.6494104504808937, 0.847650809240911, 0.36221834584533086, 0.6747644224785192, 0.11279180359498875, 0.6689243158335345, 0.3469996770936383, 0.08611162379227943, 0.7715508726617278, 0.7525793053626179, 0.6499668382348841, 0.5464576666013523, 0.05421749997490044, 0.4646344494358974, 0.899106052346948, 0.5479372651429388, 0.5746620428682672, 0.9931061076024703, 0.7925218670217851, 0.6172013642517404, 0.7414049529862161, 0.49909734772124226, 0.807739273124514, 0.3965101305736801, 0.9219301868326834, 0.09069304392208122, 0.8763539046201648, 0.2427424991484658, 0.6993801999760014, 0.8308674611850091, 0.04752125274850727, 0.08470858734157738, 0.4968272766649723, 0.8084609675792598, 0.5327209468901692, 0.33395398453805325, 0.5698012938853619, 0.38488636756619665, 0.4483966607404105, 0.39505279345552824, 0.5987349877784137, 0.7765741982057108, 0.8551508111508, 0.7515001636110623, 0.1126030460921188, 0.23935542709428193, 0.4204220112092255, 0.20264982248056762, 0.5640759900643381, 0.6177745872422731, 0.665964809118219, 0.2740404425570757, 0.2289466158073712, 0.5551516152715863, 0.6346746385368902, 0.9870808930769092, 0.34448749003773194, 0.7389481371900016, 0.3468054580316907, 0.2686298252638132, 0.8389228729139497, 0.15708941264939036, 0.510134587130605, 0.9268282159894883, 0.23722075269460086, 0.7699845123158258, 0.5409132367953007, 0.19154913495962367, 0.8370016417864403, 0.10491398463692603, 0.3005144870429237, 0.23986149123189837, 0.022323818491863934, 0.43078864998285327, 0.933118515077726, 0.01861106909669097, 0.28557820123472566, 0.5833179823524852, 0.06550670253929514, 0.2969599388593619, 0.27241669455550077, 0.19323256125985333, 0.49391114395392244, 0.30563366328166786, 0.3417834434130559, 0.1761064792940671, 0.33384187062798487, 0.19915915030406783, 0.6590369549441412, 0.8831885957990038, 0.8138625417587979, 0.4073391030611261, 0.4470572159535432, 0.07542280864299744, 0.4545526642518998, 0.7141498151626748, 0.7909898282941321, 0.34419035543163523, 0.7068707582580213, 0.8853202424547947, 0.10220409978288636, 0.5313030107775855, 0.7402408191223678, 0.9944414454760815, 0.828449052799195, 0.3465328018085546, 0.982898049408132, 0.5702873932016227, 0.04317515709580999, 0.3824683773640847, 0.10587813697443571, 0.7304052368394862, 0.9175666499402558, 0.9509702270919524, 0.9771910586143274, 0.7028025621871907, 0.7777619069571513, 0.3465417536564205, 0.32976491152475096, 0.385770105999953, 0.48933517458715203, 0.7590103269249584, 0.6960895989074458, 0.7728309874995477, 0.9345448650668761, 0.13892386947383284, 0.827020020205887, 0.8678733388518657, 0.6963003651466548, 0.40376139157375013, 0.22118472390260635, 0.11255649293746184, 0.6577001903620703, 0.05749568798988813, 0.9870732660297938, 0.6334702097048008, 0.8247763682825346, 0.08963980670300442, 0.09144649173641717, 0.9930655360420539, 0.49415413706136835, 0.6076990193093083, 0.6771638006552869])
# timeline, weights= inputGenerator(length,0.25)
# test_floatVsint_weights_mr(timeline, weights)

def test_constantInterval_weights_mr(waltons, weights):
        predict = {}
        weightsList = []
        w = []
        for i in range(1,4):
            for j in range(len(waltons['T'])):
                w.append(weights)
            weightsList.append(weights)
            kmf_intweights = KaplanMeierFitter().fit(waltons['T'],weights=np.array(w))
            # print(kmf_intweights.survival_function_)
            predict[weights] = (kmf_intweights.survival_function_).to_dict()
            print(predict[weights])
            weights = weights + 0.25
            w = []
        npt.assert_array_compare(operator.__ne__,predict[weightsList[0]],predict[weightsList[1]])


waltons = load_waltons()
weights = 0.25
test_constantInterval_weights_mr(waltons, weights)

