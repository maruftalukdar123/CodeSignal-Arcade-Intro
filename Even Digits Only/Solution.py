def solution(n):
    answer = [int(i)%2 == 0  for i in str(n)]
    return all(answer)