from Solution import solution

def test_no_obstacles():
    sol = solution([])
    assert sol == 1

def test_obstacles_every_other_point():
    sol = solution([1,3,5,7])
    assert sol == 2

def test_obstacles_random():
    sol = solution([5,3,6,7,9])
    assert sol == 4

def test_only_two_numbers():
    sol = solution([2,3])
    assert sol == 4

