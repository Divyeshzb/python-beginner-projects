# ********RoostGPT********
"""
Test generated by RoostGPT for test python-unit-test using AI Type  and AI Model 

ROOST_METHOD_HASH=toss_c71f9d1496
ROOST_METHOD_SIG_HASH=toss_89bed2f687


Scenario 1: User chooses correct answer "Heads"
Details:
  TestName: test_toss_user_chooses_heads_and_wins
  Description: The test should validate that when the user chooses 'Heads' and the toss result is 1, Player 1 wins the toss.
Execution:
  Arrange: Mock the input to return 1 and set the random.randint function to always return 1.
  Act: Call the toss function.
  Assert: Check that the function returned a 1.
Validation:
  This test verifies that the function correctly assigns a win to Player 1 when the user guessing correctly with 'Heads'. This is part of the core functionality of the toss function.

Scenario 2: User chooses incorrect answer "Heads"
Details:
  TestName: test_toss_user_chooses_heads_and_loses
  Description: The test should validate that when the user chooses 'Heads' and the toss result is 2, Player 2 wins the toss.
Execution:
  Arrange: Mock the input to return 1 and set the random.randint function to always return 2.
  Act: Call the toss function.
  Assert: Check that the function returned a 2.
Validation:
  This test verifies that the function correctly assigns a win to Player 2 when the user guessing incorrectly with 'Heads'. It checks that the logic for determining the winner is functioning properly.

Scenario 3: User chooses correct answer "Tails"
Details:
  TestName: test_toss_user_chooses_tails_and_wins
  Description: The test should validate that when the user chooses 'Tails' and the toss result is 2, Player 1 wins the toss.
Execution:
  Arrange: Mock the input to return 2 and set the random.randint function to always return 2.
  Act: Call the toss function.
  Assert: Check that the function returned a 1.
Validation:
  This test ensures that the function accurately assigns a win to Player 1 when the user guessing correctly with 'Tails'. This verifies the correct behavior of the function when 'Tails' is the correct answer.

Scenario 4: User chooses incorrect answer "Tails"
Details:
  TestName: test_toss_user_chooses_tails_and_loses
  Description: The test should validate that when the user chooses 'Tails' and the toss result is 1, Player 2 wins the toss.
Execution:
  Arrange: Mock the input to return 2 and set the random.randint function to always return 1.
  Act: Call the toss function.
  Assert: Check that the function returned a 2.
Validation:
  This test ensures that the function accurately assigns a win to Player 2 when the user guessing incorrectly with 'Tails'. It contributes to the overall testing of the function by covering the remaining potential scenario.
"""

# ********RoostGPT********
import pytest
import random
from HandCricket.main import toss
from unittest.mock import patch


class Test_MainToss:
    @pytest.mark.core
    def test_toss_user_chooses_heads_and_wins(self):
        with patch('builtins.input', return_value='1'):
            with patch('random.randint', return_value=1):
                assert toss() == 1

    @pytest.mark.core
    def test_toss_user_chooses_heads_and_loses(self):
        with patch('builtins.input', return_value='1'):
            with patch('random.randint', return_value=2):
                assert toss() == 2

    @pytest.mark.core
    def test_toss_user_chooses_tails_and_wins(self):
        with patch('builtins.input', return_value='2'):
            with patch('random.randint', return_value=2):
                assert toss() == 1

    @pytest.mark.core
    def test_toss_user_chooses_tails_and_loses(self):
        with patch('builtins.input', return_value='2'):
            with patch('random.randint', return_value=1):
                assert toss() == 2
