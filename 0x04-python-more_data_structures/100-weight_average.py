#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    totalsum = 0
    totalweight = 0
    for inkscore, inkweight in my_list:
        totalsum += inkscore * inkweight
        totalweight += inkweight
    if totalweight == 0:
        return 0
    return totalsum / totalweight
