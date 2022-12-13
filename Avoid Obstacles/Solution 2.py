# Best solution copied from andrew_pudge

def solution(inputArray):
    c = 2
    while True:
        if sorted([i%c for i in inputArray])[0]>0:
            return c
        c += 1

solution([3,7,5,6])