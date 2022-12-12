from Solution import solution

def test_equally_strong():
    sol = solution(10,10,10,10)
    assert sol == True

def test_equally_strong_unequal_arms():
    sol = solution(10,15,10,15)
    assert sol == True

def test_equally_strong_opposite_arms():
    sol = solution(10,15,15,10)
    assert sol == True

def test_not_equally_strong():
    sol = solution(10,15,15,15)
    assert sol == False