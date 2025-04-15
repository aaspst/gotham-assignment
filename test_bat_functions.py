import pytest
from bat_functions import calculate_bat_power, signal_strength, get_bat_vehicle, fetch_joker_info

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

# Exercise 2 - Using Fixtures

@pytest.fixture
def bat_vehicles():
    return {
        'Batmobile': {'speed': 200, 'armor': 80},
        'Batwing': {'speed': 300, 'armor': 60},
        'Batcycle': {'speed': 150, 'armor': 50}
    }

def test_get_bat_vehicle_known(bat_vehicles):
    for name, specs in bat_vehicles.items():
        assert get_bat_vehicle(name) == specs

def test_get_bat_vehicle_unknown():
    with pytest.raises(ValueError, match="Unknown vehicle: Batboat"):
        get_bat_vehicle("Batboat")

# Exercise 3 - Mocking External Dependencies

def test_fetch_joker_info_mock_sleep(mocker):
    mock_sleep = mocker.patch("time.sleep")  # Mock only sleep

    result = fetch_joker_info()

    # Check the result is the real one 
    assert result == {'mischief_level': 100, 'location': 'unknown'}

    # Make sure sleep is called
    mock_sleep.assert_called_once_with(1)