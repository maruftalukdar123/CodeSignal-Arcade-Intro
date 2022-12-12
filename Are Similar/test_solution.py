from solution import solution


def test_same_arrays():
    sol = solution([1,2,3],[1,2,3])
    assert sol == True

def test_swapped_one_digit():
    sol = solution([1,2,3],[2,1,3])
    assert sol == True

def test_swapped_two_digit():
    sol = solution([1,2,3],[3,1,2])
    assert sol == False

def test_4_numbers():
    sol = solution([1,2,3,1],[1,3,2,1])
    assert sol == True

def test_same_number_two_times():
    sol = solution([1,1,4],[1,2,3])
    assert sol == False

def test_swapped_at_the_edges():
    sol = solution([2,3,1],[1,3,2])
    assert sol == True