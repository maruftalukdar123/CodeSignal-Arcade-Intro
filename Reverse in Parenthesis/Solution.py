def solution(inputString):
    inputString = [*inputString]

    start,end = [],[]

    for i in range(len(inputString)):
        if inputString[i]=='(':
            start.append(i)
        if inputString[i]==')':
            end.append(i)
    
    if len(start)==1:
        return print(inputString[end[0]:start[0]])
        


inputString = "foo(bar)baz"
inputString = "foo(bar(baz))blim"
solution(inputString)