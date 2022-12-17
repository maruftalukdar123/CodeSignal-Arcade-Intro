def solution(inputArray, elemToReplace, substitutionElem):
    answer = []
    for i in inputArray:
        if i==elemToReplace:
            answer.append(substitutionElem)
        else:
            answer.append(i)
    
    return answer