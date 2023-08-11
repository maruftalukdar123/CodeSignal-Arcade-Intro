from Solution import solution

def test_3x3_matrix():

    image = [[1, 1, 1], 
             [1, 7, 1], 
             [1, 1, 1]]

    sol = solution(image)
    assert sol == [[1]]