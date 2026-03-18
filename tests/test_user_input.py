import unittest
import unittest.mock
import os
import shutil

from budget_tracker.user_input import *
from budget_tracker.constants import CATEGORIES, CASH_FLOW_TYPE, CURRENCIES, TEST_DATA_FOLDER, TEST_TABLE_NAME

# Tests for the write_row() function
class TestWriteRow(unittest.TestCase):
    def setUp(self):
        create_file(TEST_DATA_FOLDER, TEST_TABLE_NAME)
        return super().setUp()

    def tearDown(self):
        if os.path.exists(TEST_DATA_FOLDER):
            shutil.rmtree(TEST_DATA_FOLDER)
        return super().tearDown()

    def test_adding_row(self):
        row = ["17/03/2026", "Expences", "Food", "45", "USD"]
        path = os.path.join(TEST_DATA_FOLDER, TEST_TABLE_NAME)
        write_row(row, path)
        with open(path, "r") as csvfile:
            csvreader = csv.reader(csvfile)
            last_row = list(csvreader)[-1]
            self.assertEqual(row, last_row)
        
# Tests for date input
class TestDateInput(unittest.TestCase):
    def test_enter(self):
        with unittest.mock.patch("budget_tracker.user_input.questionary.text") as my_mock:
            date_input()
            todays_date = my_mock.call_args[1]["default"]
            t = datetime.datetime.now()
            self.assertEqual(todays_date, date_formatter(t))

    def test_adding_valid_date(self):
        entered = "14/03/2026"
        self.assertEqual(validation(entered), True)

    def test_adding_invalid_date(self):
        entered = "abc"
        self.assertEqual(validation(entered), "Please enter the date in format DD/MM/YYYY")

    def test_adding_wrong_formatting(self):
        entered = "14.03.2026"
        self.assertEqual(validation(entered), "Please enter the date in format DD/MM/YYYY")

    def test_adding_impossible_date(self):
        entered = "31/02/2026"
        self.assertEqual(validation(entered), "Please enter the date in format DD/MM/YYYY")
        
# Tests for the type input
class TestTypeInput(unittest.TestCase):
    def test_type_input(self):
        with unittest.mock.patch("budget_tracker.user_input.questionary.select") as my_mock:
            income_expences_choice()
            my_mock.assert_called_with('Pick the type', choices=CASH_FLOW_TYPE)

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

# Tests for the currency input
class TestCurrencyInput(unittest.TestCase):
    def test_currency_input(self):
        with unittest.mock.patch("budget_tracker.user_input.questionary.select") as my_mock:
            currency_input()
            my_mock.assert_called_with('Pick the currency', choices=CURRENCIES)