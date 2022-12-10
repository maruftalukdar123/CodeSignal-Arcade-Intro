from collections import deque

def solution(picture) -> list:
    '''given a "matrix", borders it with asterisks

    Args:
        picture (list): The list to border

    Returns:
        list : picture but bordered with *
    '''

    # borders the top and bottom
    columns = len(picture[0])
    top_bottom_border = '*'*columns
    picture.insert(0,top_bottom_border)
    picture.append(top_bottom_border) 

    # Borders the sides
    for i in range(len(picture)):
        picture[i] = '*' + picture[i] + '*'
    
    return list(picture)

picture = ["abc",
           "ded"]

print(solution(picture))