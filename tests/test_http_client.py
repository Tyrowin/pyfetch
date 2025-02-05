"""Test cases for the HTTP client class"""

import unittest
from unittest.mock import patch

from PyFetch.exceptions import HTTPClientError
from PyFetch.http_client import HTTPClient


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

    @patch("requests.request")
    def test_head_request_success(self, mock_request):
        """Test a successful HEAD request"""
        mock_request.return_value.status_code = 200
        mock_request.return_value.text = ""
        client = HTTPClient()
        response = client.head("https://api.example.com")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "")

    @patch("requests.request")
    def test_options_request_success(self, mock_request):
        """Test a successful OPTIONS request"""
        mock_request.return_value.status_code = 200
        mock_request.return_value.text = ""
        client = HTTPClient()
        response = client.options("https://api.example.com")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "")


if __name__ == "__main__":
    unittest.main()
