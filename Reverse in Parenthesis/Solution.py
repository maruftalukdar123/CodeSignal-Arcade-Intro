def solution(inputString):

    if (len(inputString) == 0) or (len(inputString) == 2 and inputString[0]=='('):
        return ''

    def start_end_index(inputString: str) -> list[list[int]]:
        inputString = [*inputString]
        brackets = [ i for i in inputString if i=='(' or i==')']
        brackets_indeces = [ i for i in range(len(inputString)) if inputString[i]=='(' or inputString[i]==')' ]

        start_end = []

        i = 0
        pairs = len(brackets)/2
        
        while len(start_end)<=pairs:

            if brackets[i]=='(' and brackets[i+1]==')':
                start_end.append([brackets_indeces[i],brackets_indeces[i+1]])

                brackets = brackets[:i] + brackets[i+2:]
                brackets_indeces = brackets_indeces[:i] + brackets_indeces[i+2:]
                i = 0

                if len(start_end)==pairs:
                    break

            else:
                i += 1

        return start_end

    def reverse_string(start_end:  list[list[int]], inputString: str) -> str:
        inputString = [ i for i in inputString]

        for i in start_end:
            temporary_string = inputString[i[0]+1:i[1]]
            temporary_string = temporary_string[::-1]
            inputString[i[0]+1:i[1]] = temporary_string

        inputString = [ i for i in inputString if i!='(' and i!=')']

        return ('').join(inputString)

    start_end = start_end_index(inputString)
    reversed_string = reverse_string(start_end, inputString)

    return reversed_string



inputString = "foo(bar(b(az)))b(li)mo(t(at)i)on"
print(solution(inputString))


# nested 1 start_end = [
# (9,12)
# (7,13)
# (3,14)
# ]

# nested 2 start_end = [
#     (24,27)
#     (22,29)
# ]

# normal start_end = [
#     (16,19)
# ]