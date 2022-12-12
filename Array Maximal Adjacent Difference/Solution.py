from itertools import pairwise
def solution(a):

    differences = []
    for i in pairwise(a):
        differences.append(abs(i[1]-i[0]))

    return max(differences)
