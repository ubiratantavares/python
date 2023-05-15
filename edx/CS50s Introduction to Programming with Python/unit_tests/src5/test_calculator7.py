"""
@ author David Malan
"""

from calculator1 import square

import pytest


def test_positive():
    """
    function test_positive
    """
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    """
    function test_negative
    """
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    """
    function test_zero
    """
    assert square(0) == 0


def test_str():
    """
    function test_str
    """
    with pytest.raises(TypeError):
        square("cat")
