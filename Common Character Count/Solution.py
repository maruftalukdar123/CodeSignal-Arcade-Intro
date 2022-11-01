def solution(s1, s2):
    s1,s2 = [*s1],[*s2]
    common = []
    
    for ch in s2:
        if ch in s1:
            common.append(ch)
            s1.remove(ch)

    return len(common)

s1 = "aabcc"
s2 = "adcaa"
solution(s1,s2)