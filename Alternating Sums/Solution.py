def solution(a) -> list(int):
    '''devides a in two lists, and returns the sum of the two lists as a list 
    shape (1,2). Even indeces go to list 1, odd indeces go to list 2.

    Args:
        a (list): _description_

    Returns:
        list: sum of the sublists created from a
    '''
    team_1 = sum([a[i] for i in range(0,len(a),2)])
    team_2 = sum([a[i] for i in range(1,len(a),2)])

    return [team_1,team_2]

a = [50, 60, 60, 45, 70]
print(solution(a))