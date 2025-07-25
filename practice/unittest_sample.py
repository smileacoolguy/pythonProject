# test_weather.py
import unittest
from unittest.mock import patch

from practice.weather import get_temperature

class TestWeather(unittest.TestCase):
    @patch("weather.requests.get")
    def test_get_temperature(self, mock_get):
        mock_get.return_value.json.return_value = {"temperature": 25}
        temp = get_temperature("London")
        self.assertEqual(temp, 25)
        mock_get.assert_called_once_with("http://api.weather.com/London")

if __name__ == "__main__":
    unittest.main()



