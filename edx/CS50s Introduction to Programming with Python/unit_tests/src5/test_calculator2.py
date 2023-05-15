"""
@ author David Malan
"""

from calculator2 import square


def main():
    """
    function main
    """
    test_square()


def test_square():
    """
    function test_square
    """
    assert square(2) == 4
    assert square(3) == 9


if __name__ == "__main__":
    main()
