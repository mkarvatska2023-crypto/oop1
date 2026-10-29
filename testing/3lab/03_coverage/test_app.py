import pytest
from app import Figure

def test_triangle_angles():
    f = Figure("трикутник", 10)
    assert f.get_angles() == 3

def test_square_angles():
    f = Figure("квадрат", 5)
    assert f.get_angles() == 4

def test_rectangle_angles():
    f = Figure("прямокутник", 7)
    assert f.get_angles() == 4

def test_unknown_figure():
    f = Figure("коло", 3)
    assert f.get_angles() is None
