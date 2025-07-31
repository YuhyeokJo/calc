import pytest

from calc import Calc


def test_get_minus():
    calc = Calc()
    assert 3 == calc.getMinus(5, 2)

    
def test_get_zegop():
    sut = Calc()
    ret = sut.get_zegop(5)
    assert ret ==


def test_divide():
    calc = Calc()
    result = calc.getDivide(6, 3)
    assert result == 2
