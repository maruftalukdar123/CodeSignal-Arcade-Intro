from Solution import solution

def test_3x3_matrix():

    image = [[1, 1, 1], 
             [1, 7, 1], 
             [1, 1, 1]]

    sol = solution(image)
    assert sol == [[1]]



def test_less_than_3x3_matrix():

    image = [[1, 1, 1], 
             [1, 7, 1]]

    sol = solution(image)
    assert sol == [[]]     



def test_3x4_matrix():

    image = [[1, 1, 1, 1], 
             [1, 7, 1, 1], 
             [1, 1, 1, 1]]

    sol = solution(image)
    assert sol == [[1, 1]]



def test_another_3x3_matrix():

    image = [[0,18,9], 
             [27,9,0], 
             [81,63,45]]


    sol = solution(image)
    assert sol == [[28]]



def test_4x4_matrix():

    image = [[7,4,0,1], 
             [5,6,2,2], 
             [6,10,7,8], 
             [1,4,2,0]]

    sol = solution(image)
    assert sol == [[5,4], 
                   [4,4]]