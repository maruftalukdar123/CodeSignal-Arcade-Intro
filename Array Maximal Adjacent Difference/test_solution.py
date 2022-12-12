from Solution import solution

def test_all_same():
    sol = solution([1,1,1])
    assert sol == 0

def test_random_array():
    sol = solution([2,4,1,0])
    assert sol == 3