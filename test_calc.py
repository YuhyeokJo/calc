from calc import Calc


def test_get_minus():
    calc = Calc()
    assert 3 == calc.getMinus(5, 2)
