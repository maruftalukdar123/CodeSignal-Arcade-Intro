from string import ascii_lowercase
def solution(inputString):
    alphabet = list(ascii_lowercase)
    answer = ''
    
    for i in inputString:
        if i != 'z':
            index = alphabet.index(i)
            answer = answer + alphabet[index+1]
        else:
            answer = answer + 'a'
    
    return answer

