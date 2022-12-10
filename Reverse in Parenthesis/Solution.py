def solution(inputString):

    # Edge case
    if (len(inputString) == 0) or (len(inputString) == 2 and inputString[0]=='('):
        return ''

    def start_end_index(inputString: str) -> list[list[int]]:

        # Split input into array so it's mutable
        # Index where the parenthesis are
        inputString = [*inputString]
        brackets = [ i for i in inputString if i=='(' or i==')']
        brackets_indeces = [ i for i in range(len(inputString)) if inputString[i]=='(' or inputString[i]==')' ]

        # This array will hold the paris of ( and ) indeces 
        start_end = []

        i = 0
        pairs = len(brackets)/2
        
        while len(start_end)<=pairs:
            # Everytime ) appears after (,
            # Append the indeces of the () as a list to the start_end array
            # Remembering to delete both the indecis and the brackets from their respective lists
            # This is to avoid being stuck on one () for the entire loop
            # If a set of () is found then set i to 0 and restart the loop
            # Otherwise move along the loop by adding 1 to i

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

        # Reverese the string from the indecis obtained from the start_end_index function
        # Remove the brackets and join back characters to form string
        for i in start_end:
            temporary_string = inputString[i[0]+1:i[1]][::-1]
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