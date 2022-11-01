def solution(inputArray):
    lengths = [len(el) for el in inputArray]
    max_len = max(lengths)

    solution = [inputArray[i] for i in range(len(lengths)) if len(inputArray[i])==max_len]

    return solution


inputArray= ["abc", "eeee", "abcd", "dcd"]
solution(inputArray)