from Solution import solution

def test_palindrome():
    sol = solution("abba")
    assert sol == True

def test_not_palindrome():
    sol = solution("abbb")
    assert sol == False

def test_one_wrong_position():
    sol = solution("aabb")
    assert sol == True

def test_zero_input():
    sol = solution("")
    assert sol == True

def test_one_letter_odd_number_of_times():
    sol = solution("aacbb")
    assert sol == True

def test_one_letter_odd_number_of_times_but_different_positions():
    sol = solution("aacbbcc")
    assert sol == True   