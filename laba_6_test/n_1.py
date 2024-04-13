import pytest

def factorial(n: int) -> int:
    if type(n) != int:
        raise TypeError("n must be an integer")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def test_factorial_values():
    assert factorial(0) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800

def test_factorial_exception():
    with pytest.raises(TypeError):
        factorial("5")
        factorial(5.0)
        factorial([1, 2, 3])
        factorial({1, 2, 3})
        factorial(False)