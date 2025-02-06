import pytest
import allure

def add(x, y):
    return x + y

@allure.feature("Addition")
@allure.story("Adding two numbers")
def test_addition():
    assert add(2, 3) == 5

@allure.feature("Multiplication")
@allure.story("Multiplying two numbers")
def test_multiplication():
    assert 2 * 3 == 6
