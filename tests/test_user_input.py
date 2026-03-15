import unittest
import unittest.mock

from budget_tracker.user_input import *

# The three test cases below are identical as for now that's what they have to check
class TestDateInput(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
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
        