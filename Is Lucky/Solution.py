def solution(n):

    # Change integers to string so each digit can be iterated through
    # Change string to integers so each digits can be added togheter
    # Check if the sum for the first half of the digits equals the sum of the secod half

    n = str(n)
    n = [int(n[i]) for i in range(len(n))]
    half = int(len(n)/2)
    return sum(n[:half]) == sum(n[half:])


n = 1230
solution(n)