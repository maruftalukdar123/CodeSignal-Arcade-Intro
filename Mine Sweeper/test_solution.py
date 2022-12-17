from Solution import solution

def test_1x2_matrix():
    matrix = [[True,False]]

    sol = solution(matrix)
    assert sol == [[0,1]]


def test_another_1x2_matrix():
    matrix = [[True,True]]

    sol = solution(matrix)
    assert sol == [[1,1]]

def test_2x2_matrix():
    matrix = [[True,True],
              [False,True]]

    sol = solution(matrix)
    assert sol == [[2,2],
                    [3,2]]


def test_3x3_matrix():

    matrix= [[True,False,False], 
             [False,True,False], 
             [False,False,False]]

    sol = solution(matrix)
    assert sol == [[1,2,1], 
                   [2,1,1], 
                   [1,1,1]]

