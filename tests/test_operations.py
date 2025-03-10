from src.math_operations import add, substraction

def test_add():
    assert add(2, 3)==5
    assert add(-1, 1)==0

def test_substraction():
    assert substraction(3, 2) == 1
    assert substraction(6, 4) == 2
    assert substraction(3, 3) == 0