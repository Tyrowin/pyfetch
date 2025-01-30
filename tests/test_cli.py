"""Test cases for the CLI module"""
import unittest
from unittest.mock import patch

from http_cli.cli import main


class TestCLI(unittest.TestCase):
    """Test cases for the CLI module"""

    @patch("sys.argv", ["http_cli", "HELP"])
    def test_help_command(self):
        """Test the HELP command"""
        with patch("builtins.print") as mocked_print:
            main()
            mocked_print.assert_called()

    @patch("sys.argv", ["http_cli", "GET", "https://api.example.com"])
    @patch("http_cli.http_client.HTTPClient.get")
    def test_get_command(self, mock_get):
        """Test the GET command"""
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = "Success"

        with patch("builtins.print") as mocked_print:
            main()
            mocked_print.assert_called_with("Success")

    @patch(
        "sys.argv",
        ["http_cli", "POST", "https://api.example.com", "-d", '{"key": "value"}'],
    )
    @patch("http_cli.http_client.HTTPClient.post")
    def test_post_command(self, mock_post):
        """Test the POST command"""
        mock_post.return_value.status_code = 201
        mock_post.return_value.text = "Created"

        with patch("builtins.print") as mocked_print:
            main()
            mocked_print.assert_called_with("Created")


if __name__ == "__main__":
    unittest.main()
