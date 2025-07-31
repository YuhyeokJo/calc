from calc import Calc


def test_get_zegop():
    sut = Calc()
    ret = sut.get_zegop(5)
    assert ret == 25
