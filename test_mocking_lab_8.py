import unittest
from unittest import TestCase
from unittest.mock import patch

import mocking_lab_8

class TestMocking(TestCase):

    @patch('mocking_lab_8.request_rates')
    def test_bitcoin_to_target(self, mock_rates):
        mock_rate = 20000.12
        example_api_response = {"bpi": {"USD": {"rate_float": mock_rate}}}
        mock_rates.side_effect = [ example_api_response ]
        converted = mocking_lab_8.convert_bitcoin_to_target(10, 'USD')
        expected = 20000.12 * 10
        self.assertEqual(expected, converted)

if __name__ == '__main__':
    unittest.main()