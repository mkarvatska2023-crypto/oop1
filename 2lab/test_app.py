import pytest
from app import Figure

# 1. Простий тест з assert
def test_triangle_type():
    triangle = Figure("трикутник", 4)
    assert triangle.type == "трикутник"

# 2. Тест для винятку через pytest.raises
def test_invalid_length_zero():
    with pytest.raises(AssertionError):
        Figure("квадрат", 0)

def test_invalid_length_negative():
    with pytest.raises(AssertionError):
        Figure("квадрат", -1)

def test_invalid_type():
    with pytest.raises(AssertionError):
        Figure("коло", 5)

# 3. Параметризований тест для всіх дозволених фігур
@pytest.mark.parametrize("figure", Figure.FIGURES)
def test_allowed_figure(figure):
    obj = Figure(figure, 1)
    assert obj.type == figure

# 4. Fixture, яка повертає фігуру з довжиною 10
@pytest.fixture
def square():
    return Figure("квадрат", 10)

def test_square_length(square):
    assert square.get_figure_length == 10

# 5. Тести з маркером @pytest.mark.unit
@pytest.mark.unit
def test_square_angles():
    square = Figure("квадрат", 5)
    assert square.get_angles() == 4

@pytest.mark.unit
def test_triangle_angles():
    triangle = Figure("трикутник", 3)
    assert triangle.get_angles() == 3

# 6. Fixture зі scope="module"
@pytest.fixture(scope="module")
def allowed_figures():
    return Figure.FIGURES

def test_module_fixture_contains_square(allowed_figures):
    assert "квадрат" in allowed_figures

def test_module_fixture_contains_triangle(allowed_figures):
    assert "трикутник" in allowed_figures

# 7. Навмисно зламаний тест
def test_broken():
    square = Figure("квадрат", 5)
    # Тут помилка: очікуємо неправильне значення
    assert square.get_angles() == 5
