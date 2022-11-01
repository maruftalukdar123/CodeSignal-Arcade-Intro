from more_itertools import locate

def solution(inputArray):

    # Find the lengths of each element in array
    # Find the indeces where the element with the maximum number characters is 
    # Output inputarray[indeces]

    lengths = [len(el) for el in inputArray]
    indeces = list(locate(lengths,lambda x: x==max(lengths)))
    solution = [inputArray[i] for i in indeces]
    
    return print(solution)



inputArray = ["aba", "aa", "ad", "vcd", "aba"]
inputArray= ["abc", "eeee", "abcd", "dcd"]
solution(inputArray)