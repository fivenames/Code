from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.size == 12


def test_str():
    jar = Jar()
    jar.withdraw(1)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(11)
    assert str(jar) == ""


def test_deposit():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(1)

def test_withdraw():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(13)
