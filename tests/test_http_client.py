"""Test cases for the HTTP client class"""

import unittest
from unittest.mock import patch

from http_cli.exceptions import HTTPClientError
from http_cli.http_client import HTTPClient


class TestHTTPClient(unittest.TestCase):
    """Test cases for the HTTP client class"""

    @patch("requests.request")
    def test_get_request_success(self, mock_request):
        """Test a successful GET request"""
        mock_request.return_value.status_code = 200
        mock_request.return_value.text = "Success"

        client = HTTPClient()
        response = client.get("https://api.example.com")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Success")

    @patch("requests.request", side_effect=HTTPClientError)
    def test_get_request_failure(self, _):
        """Test a failed GET request"""
        client = HTTPClient()
        with self.assertRaises(HTTPClientError):
            client.get("https://api.example.com")


if __name__ == "__main__":
    unittest.main()
