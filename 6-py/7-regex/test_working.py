from working import convert
import pytest

def main():
    test_nominute()
    test_withcolonanddot()
    test_withspace()
    test_afternoontomorning()
    test_wronginput()

def test_nominute():
    assert convert('9am to 5pm') == '0900 to 1700'
    assert convert('12am to 12 pm') == '0000 to 1200'

def test_withcolonanddot():
    assert convert("9:00 A.M. to 5:00 P.M.") == '0900 to 1700'

def test_withspace():
    assert convert("9 AM to 5 PM") == '0900 to 1700'

def test_afternoontomorning():
    assert convert("5:00 PM to 9:00 AM") == '1700 to 0900'

def test_wronginput():
    with pytest.raises(ValueError):
        convert("5:60 PM to 9:00 AM")
        convert("5:00 PM to 13:00 AM")


main()