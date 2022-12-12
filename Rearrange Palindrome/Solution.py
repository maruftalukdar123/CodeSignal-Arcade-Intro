def solution(s):
    count = [s.count(s[i]) for i in range(len(s)) if s[i] not in s[:i]]
    even = []
    for i in count:
        even.append(i%2==0)
    
    if even.count(False)<=1:
        return True
    
    return False