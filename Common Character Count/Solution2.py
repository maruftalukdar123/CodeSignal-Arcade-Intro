# Model Solution

def solution(s1, s2):
    com = [min(s1.count(i),s2.count(i)) for i in set(s1)]
    return print(sum(com))


s1 = "aabcc"
s2 = "adcaa"
solution(s1,s2)