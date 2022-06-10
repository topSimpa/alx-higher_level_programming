#!/usr/bin/python3
def weight_average(my_list=[]):
    if weight_average:
        prod_sum = list(map(lambda x: x[0] * x[1], my_list))
        weight_avg = sum(prod_sum) / sum([i[1] for i in my_list])
        return weight_avg
    return 0
