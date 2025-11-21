import math
from src.safe_math import safe_division


def test_normal_division():
    assert safe_division(6, 3) == 2


def test_zero_denominator():
    assert safe_division(1, 0) is None


def test_negative_and_float():
    assert math.isclose(safe_division(5.0, -2.0), -2.5)


def test_non_numeric_raises():
    try:
        safe_division("a", 2)
    except TypeError:
        assert True
    else:
        assert False, "Expected TypeError for non-numeric input"
