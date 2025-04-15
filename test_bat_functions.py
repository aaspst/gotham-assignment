import pytest
from bat_functions import calculate_bat_power, signal_strength

# Exercise 1 - Basic Tests and Parametrization

def test_calculate_bat_power():
    assert calculate_bat_power(1) == 42
    assert calculate_bat_power(0) == 0
    assert calculate_bat_power(5) == 210
    assert calculate_bat_power(-1) == -42

@pytest.mark.parametrize("distance, expected", [
    (0, 100),
    (5, 50),
    (10, 0),
    (12, 0),
])
def test_signal_strength(distance, expected):
    assert signal_strength(distance) == expected