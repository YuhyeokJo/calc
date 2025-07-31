import pytest
from calc import Calc

def test_get_sum():
    calc = Calc()
    assert calc.getSum(1, 3) == 4

def test_getGop():
    calc = Calc()
    ret = calc.getGop(2,3)
    assert ret == 6

def test_getGop():
    calc = Calc()
    ret = calc.getGop(8,9)
    assert ret == 72

def test_getGop():
    calc = Calc()
    ret = calc.getGop(-1,-2)
    assert ret == 2

def test_get_minus():
    calc = Calc()
    assert 3 == calc.getMinus(5, 2)

def test_get_zegop():
    sut = Calc()
    ret = sut.get_zegop(5)
    assert ret == 25

def test_divide():
    calc = Calc()
    result = calc.getDivide(6, 3)
    assert result == 2

