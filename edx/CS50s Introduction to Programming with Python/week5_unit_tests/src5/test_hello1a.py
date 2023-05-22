"""
@ author David Malan
"""

from hello1 import hello


def test_default():
    """
    function test_default
    """
    assert hello() == "hello, world"


def test_argument():
    """
    function test_argument
    """
    assert hello("David") == "hello, David"
