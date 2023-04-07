from twttr import shorten
import pytest

def main():

    test_shorten()
    test_str()

def test_shorten():
    assert shorten("twitter") == 'twttr'

def test_str():
    with pytest.raises(TypeError):
        shorten(0)


if __name__ == '__main__':
    main()

# Usage: pytest test_twttr.py
# Installation: pip install pytest

