
        #DO NOT LEAVE THIS OUT
from src.tip_calculator import calculate_tip

#Test 1: Check if the function returns the correct value when given a bill, percentage and number of people
def test_calculate_tip():
    assert calculate_tip(100, 0.2, 4) == 30.0

#Test 2: Check if the function returns the correct value when given a bill, percentage and number of people
def test_calculate_tip_2():
    assert calculate_tip(50, 0.15, 2) == 32.5

#Test 3: Check if the function returns the correct value when given a bill, percentage and number of people
def test_calculate_tip_3():
    assert calculate_tip(20, 0.1, 1) == 22.0

#Test 4: Check if the function returns the correct value when given a bill, percentage and number of people
def test_calculate_tip_4():
    assert calculate_tip(200, 0.25, 5) == 55.0

#Test 5: Check if the function returns the correct value when given a bill, percentage and number of people
def test_calculate_tip_5():
    assert calculate_tip(150, 0.2, 3) == 45.0