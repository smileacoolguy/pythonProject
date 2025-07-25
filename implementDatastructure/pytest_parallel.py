import time

class Math:
    # my_math.py
    def add(self, a, b):
        return a + b


m=Math()

def test_add_positive_numbers():
    result = m.add(2, 3)
    time.sleep(5)
    assert result == 5

def test_add_negative_numbers():
    result = m.add(-2, -3)
    time.sleep(5)
    assert result == -5

def test_add_mixed_numbers_1():
    result = m.add(2, -3)
    time.sleep(5)
    assert result == -1

def test_add_mixed_numbers_2():
    result = m.add(-2, 3)
    time.sleep(5)
    assert result == 1

def test_add_zero():
    result = m.add(0, 0)
    time.sleep(5)
    assert result == 0


