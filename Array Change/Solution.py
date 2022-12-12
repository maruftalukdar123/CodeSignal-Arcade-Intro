def solution(a):

    moves = 0

    for i in range(1,len(a)):
        if a[i] < a[i-1]:
            moves += (-a[i] + a[i-1] + 1)
            a[i] = a[i-1]+1
        if a[i] == a[i-1]:
            moves += 1
            a[i] = a[i-1]+1
        

    return moves
    
    # for i in range(len(a)):
    #     maximum = max(a[:i+1])
    #     difference = maximum - a[i]
    #     if difference == 0 and a[i]!=a[i-1]:
    #         continue
    #     moves += difference+1
    #     # a[i] = a[i-1]+1

    # return moves