def solution(a,b):

    if a==b:
        return True

    sorted_a, sorted_b = sorted(a), sorted(b)
    
    if sorted_a != sorted_b:
        return False


    ab_combined = [ [a[i],b[i]] for i in range(len(a))]

    number_of_swaps = []
    
    for i in range(1,len(ab_combined)):
        if ab_combined[i-1] != ab_combined[i]:
            if ab_combined[i-1][1] == ab_combined[i][0]:
                number_of_swaps.append(True)

    if sum(number_of_swaps) == 1:
        return True
    elif ab_combined[-1][1] == ab_combined[0][0]:
        number_of_swaps.append(True)
        if sum(number_of_swaps) == 1:
            return True


    return False





a = [1, 1, 4]
b = [1, 2, 3]

solution(a,b)