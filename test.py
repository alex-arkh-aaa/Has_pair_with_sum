from main import has_pair_with_sum

def test_main_tests():
    assert has_pair_with_sum([1, 2, 3], 5) == True
    assert has_pair_with_sum([100, 20, 160, 9999], 180) == True
    assert has_pair_with_sum([1, 1, 1, 1, 1, 1, 1], 2) == True
    assert has_pair_with_sum([123456789, 987654321, 1, 10], 987654331) == True
    assert has_pair_with_sum([10, 20, 30, 40, 50, 50, 160, 270], 100) == True



def test_negative_nums():
    assert has_pair_with_sum([10, 20, -40], -30) == True
    assert has_pair_with_sum([-50, -60, -10], -60) == True
    assert has_pair_with_sum([-1, -2, -3, -4, -123456780, -876543219], -999999999) == True


def test_no_passings():
    assert has_pair_with_sum([5, 15, 3, 7], 999) != True
    assert has_pair_with_sum([5, 15, 3, 745, 2, 666, 3636], 9999) != True
    assert has_pair_with_sum([5, 15, 3, 7, 2, 25, 62, -654], 99999) != True
    assert has_pair_with_sum([5, 15, 3, 7, -43, 543, -654, 45645], -9999) != True
    assert has_pair_with_sum([5, 15, 3, 7], -34567) != True