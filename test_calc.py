import pytest

from calc import Calc


def test_divide():
    calc = Calc()
    result = calc.divide(6, 3)
    assert result == 2
