
# The Ascension of Vexa
# Neural Bridge Automated Tests

import unittest
from unittest.mock import patch, MagicMock
from vexa.brain import ask_vexa


class TestVexaBrain(unittest.TestCase):

    @patch("vexa.brain.urllib.request.urlopen")
    def test_ask_vexa(self, mock_urlopen):

        mock_response = MagicMock()
        mock_response.read.return_value = (
            b'{"response": "Greetings, Captain!"}'
        )

        mock_urlopen.return_value.__enter__.return_value = (
            mock_response
        )

        result = ask_vexa("Hello")

        self.assertEqual(result, "Greetings, Captain!")
        mock_urlopen.assert_called_once()


if __name__ == "__main__":
    unittest.main()
