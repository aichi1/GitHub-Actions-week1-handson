"""calculator.py のテスト"""

import pytest

from src.calculator import add, average, divide, multiply, subtract


def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0.1, 0.2) == pytest.approx(0.3)


def test_subtract():
    assert subtract(10, 3) == 7
    assert subtract(1, 1) == 0


def test_multiply():
    assert multiply(4, 5) == 20
    assert multiply(0, 100) == 0


def test_divide():
    assert divide(15, 3) == 5.0
    assert divide(1, 2) == 0.5


def test_divide_by_zero():
    with pytest.raises(ValueError, match="0で割ることはできません"):
        divide(10, 0)


def test_average():
    assert average([1, 2, 3, 4, 5]) == 3.0
    assert average([10]) == 10.0


def test_average_empty():
    with pytest.raises(ValueError, match="空のリストの平均は計算できません"):
        average([])
