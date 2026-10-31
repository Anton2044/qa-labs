import pytest
from calculator import Calculator

# Фикстура для создания экземпляра класса
@pytest.fixture
def calc():
    return Calculator()

# Тесты для метода add (параметризованные)
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (10, -5, 5)
])
def test_add(calc, a, b, expected):
    assert calc.add(a, b) == expected

# Тесты для метода subtract
@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (0, 5, -5),
    (-5, -5, 0),
    (10, 2, 8)
])
def test_subtract(calc, a, b, expected):
    assert calc.subtract(a, b) == expected

# Тесты для метода multiply
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-2, 3, -6),
    (0, 100, 0),
    (1.5, 2, 3.0)
])
def test_multiply(calc, a, b, expected):
    assert calc.multiply(a, b) == expected

# Тесты для метода divide
@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (9, 3, 3),
    (5, 2, 2.5)
])
def test_divide(calc, a, b, expected):
    assert calc.divide(a, b) == expected

# Проверка выброса исключения при делении на ноль
def test_divide_by_zero(calc):
    with pytest.raises(ZeroDivisionError):
        calc.divide(10, 0)

# Тесты для метода is_prime_number
@pytest.mark.parametrize("n, expected", [
    (2, True),
    (3, True),
    (4, False),
    (17, True),
    (1, False),
    (-5, False)
])
def test_is_prime_number(calc, n, expected):
    assert calc.is_prime_number(n) == expected