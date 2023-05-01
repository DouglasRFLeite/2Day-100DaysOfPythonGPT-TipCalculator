# Import the function to be tested
from src.tip_calculator import calculate_tip

# Define the tests
def test_calculate_tip():
    assert calculate_tip(100, 0.15, 2) == 57.5
    assert calculate_tip(25.50, 0.18, 3) == 9.03
    assert calculate_tip(60, 0.2, 4) == 15.6
    assert calculate_tip(150, 0.25, 5) == 37.5
    assert calculate_tip(45.80, 0.12, 2) == 21.1
