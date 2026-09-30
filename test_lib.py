from lib import average

def test_average():
    assert average([10, 20]) == 15
    assert average([11, -11, 10, 20]) == 7.5
    assert average([5]) == 5