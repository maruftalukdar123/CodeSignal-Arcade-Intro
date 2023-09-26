import numpy as np

def solution(a):

    sum_for_all_elements = []

    for i in a:
        sum_for_element_i = np.sum([abs(i-j) for j in a])
        sum_for_all_elements.append(sum_for_element_i)

    return a[sum_for_all_elements.index(min(sum_for_all_elements))]

