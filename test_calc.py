from calc import Calc

def test_get_sum():
    calc = Calc()
    assert calc.getSum(1, 3) == 4

def test_get_minus():
    calc = Calc()
    assert 3 == calc.getMinus(5, 2)

def test_get_zegop():
    sut = Calc()
    ret = sut.get_zegop(5)
    assert ret == 25
