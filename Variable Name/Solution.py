def solution(name):
    if name[0].isdigit():
        return False
    answer = [i.isdigit() or i.isalpha() or i=='_' for i in name]
    return all(answer)