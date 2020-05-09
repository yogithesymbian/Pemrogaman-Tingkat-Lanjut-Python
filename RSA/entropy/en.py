import math
import collections


def entropy(data):
        entropy = 0
        counterData = collections.Counter(data)         # python collection
        lengthData = len(data)      # length of $data
        lengthCounterData = len(counterData)        # length of $counterData collection
        for count in counterData.values():      # probabilitas data $count
            # count is always > 0
            p_x = count / lengthData        # avoid zero /
            entropy += - p_x * math.log2(p_x)

        print("debug")

        return entropy
# P = 73
# Q = 131
# N = 9563
# Fai[N] = 9360
# PUBLIK_KEY = 131
# PRIVATE_KEY = 7931
# data = [73,131,9563,9360,131,7931]
# data = ["s","a","y","a"]
# data = [12,17,1,4,19,12,18,14,21,14,21,16,14]
# data = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# data1 = [131,7931, 191, 6851, 151, 18535,#             151, 2263, 99, 347,101, 12477,#             103, 7763, 103, 5955]# datay = [459609268873, 4019492633373]

# data = [2,":",5,":",31,"GMT +8"]
# data = [10,":",5,":",32,"GMT +12"]
# data = [13,":",57,":",8,"GMT +8"]
# data = [14,":",57,":",9,"GMT + 9"]

data = [5,":",00,":",6,"GMT + 2"]


print(entropy(data))
