def solution(n, firstNumber):
    if firstNumber + (n/2)< n:
        return firstNumber + (n/2)
    return firstNumber - (n/2)