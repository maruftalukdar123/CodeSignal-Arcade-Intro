from Solution import solution

def test_increasing_array():
    sol = solution([1,2,3])
    assert sol == 0

def test_one_wrong():
    sol = solution([1,2,1])
    assert sol == 2

def test_two_wrong():
    sol = solution([1,1,1])
    assert sol == 3

def test_decresing_array():
    sol = solution([5,1,2])
    assert sol == 10

def test_random_array():
    sol = solution([5,4,2,1,5])
    assert sol == 18
    
