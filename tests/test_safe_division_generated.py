import math
from decimal import Decimal
import pytest

from src.safe_math import safe_division


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (6, 3, 2.0),
        (5, 2, 2.5),
        (0, 5, 0.0),
        (-4, 2, -2.0),
        (1, 3, pytest.approx(1/3)),
    ],
)
def test_various_numeric_divisions(a, b, expected):
    result = safe_division(a, b)
    if isinstance(expected, float):
        assert result == expected
    else:
        assert result == expected


def test_zero_denominator_returns_none():
    assert safe_division(1, 0) is None
    assert safe_division(0, 0) is None


def test_decimal_inputs_return_decimal():
    a = Decimal("10")
    b = Decimal("4")
    result = safe_division(a, b)
    assert isinstance(result, Decimal)
    assert result == Decimal("2.5")


def test_nan_denominator_produces_nan():
    nan = float("nan")
    res = safe_division(1.0, nan)
    assert math.isnan(res)


def test_infinite_denominator_and_numerator():
    inf = float("inf")
    # a / inf -> 0.0
    assert safe_division(1.0, inf) == 0.0
    # inf / 1 -> inf
    assert safe_division(inf, 1.0) == inf


def test_non_numeric_raises_typeerror():
    with pytest.raises(TypeError):
        safe_division("not-a-number", 2)
    with pytest.raises(TypeError):
        safe_division(1, "x")
