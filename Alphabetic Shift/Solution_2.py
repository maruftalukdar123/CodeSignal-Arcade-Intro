# Optimal solution copied from keeping_it_leal

def solution(s):
    return "".join(chr((ord(i)-96)%26+97) for i in s)