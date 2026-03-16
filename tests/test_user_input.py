import unittest
import unittest.mock

from budget_tracker.user_input import *
from budget_tracker.constants import CATEGORIES, TYPE

# The three test cases below are identical as for now that's what they have to check
class TestDateInput(unittest.TestCase):
    
    def test_enter(self):
        with unittest.mock.patch("budget_tracker.user_input.input", return_value=""):
            result = date_input()
            t = datetime.datetime.now()
            self.assertEqual(
                f"{t.strftime('%d')}/{t.strftime('%m')}/{t.strftime('%Y')}",
                result
            )

    def test_adding_valid_date(self):
        entered = "14/03/2026"
        with unittest.mock.patch("budget_tracker.user_input.input", return_value=entered):
            result = date_input()
            self.assertEqual(entered, result)

    def test_adding_invalid_date(self):
        entered = "abc"
        with self.assertRaises(ValueError):
            validate_date(entered)

    def test_adding_wrong_formatting(self):
        entered = "14.03.2026"
        with self.assertRaises(ValueError):
            validate_date(entered)

    def test_adding_impossible_date(self):
        entered = "31/02/2026"
        with self.assertRaises(ValueError):
            validate_date(entered)
        
# Tests for the type input
class TestTypeInput(unittest.TestCase):
    def test_type_input(self):
        with unittest.mock.patch("budget_tracker.user_input.questionary.select") as my_mock:
            income_expences_choice()
            my_mock.assert_called_with('Pick the category', choices=TYPE)

# Tests for the category input
class TestCategoryInput(unittest.TestCase):
    def test_category_input(self):
        with unittest.mock.patch("budget_tracker.user_input.questionary.select") as my_mock:
            category_input()
            my_mock.assert_called_with('Pick the category', choices=CATEGORIES)

# Tests for the amount input
class TestAmountInput(unittest.TestCase):

    def test_integer_amount_input(self):
        with unittest.mock.patch("budget_tracker.user_input.questionary.text") as my_mock:
            amount_input()
            validate = my_mock.call_args[1]["validate"]
            self.assertTrue(validate("111"))
    
    def test_non_integer_amount_input(self):
        with unittest.mock.patch("budget_tracker.user_input.questionary.text") as my_mock:
            amount_input()
            validate = my_mock.call_args[1]["validate"]
            self.assertEqual(validate("111.1"), 'Please enter an integer')
    
    def test_empty_amount_input(self):
        with unittest.mock.patch("budget_tracker.user_input.questionary.text") as my_mock:
            amount_input()
            validate = my_mock.call_args[1]["validate"]
            self.assertEqual(validate(""), 'Please enter an integer')
    
    def test_negative_amount_input(self):
        with unittest.mock.patch("budget_tracker.user_input.questionary.text") as my_mock:
            amount_input()
            validate = my_mock.call_args[1]["validate"]
            self.assertEqual(validate("-111"), 'Please enter an integer')