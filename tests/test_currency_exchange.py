import questionary
import unittest
from unittest.mock import Mock

from budget_tracker.currency_exchange import currency_exchange

class TestSuccessfulCall(unittest.TestCase):
    def test_successful_call(self):
        with unittest.mock.patch("budget_tracker.currency_exchange.requests.get") as my_mock:
            my_mock.return_value.json.return_value = {"usd": {"czk": 21.25585714}}
            result = currency_exchange("17/03/2026", "100", "CZK")
            self.assertEqual(result, "4.7")