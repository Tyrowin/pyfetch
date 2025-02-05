"""Test cases for the exceptions module"""

import unittest

from PyFetch.exceptions import HTTPClientError


class TestHTTPClientError(unittest.TestCase):
    """Test cases for the HTTPClientError exception"""

    def test_http_client_error_message(self):
        """Test the error message of HTTPClientError"""
        error_message = "An error occurred"
        exception = HTTPClientError(error_message)
        self.assertEqual(str(exception), error_message)

    def test_http_client_error_type(self):
        """Test the type of HTTPClientError"""
        exception = HTTPClientError("Error")
        self.assertIsInstance(exception, Exception)


if __name__ == "__main__":
    unittest.main()
