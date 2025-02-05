"""Command-line interface for making HTTP requests with support for common HTTP methods."""

import argparse
import json
import sys
import textwrap

from http_cli.exceptions import HTTPClientError
from http_cli.http_client import HTTPClient


def show_examples(suppress_output=False):
    """Show examples of how to use the HTTP CLI client."""
    examples = """
Examples:
    1. Make a GET request:
       http_cli GET https://api.example.com

    2. Make a POST request with JSON data:
       http_cli POST https://api.example.com -d '{"key": "value"}'

    3. Update a resource with PUT:
       http_cli PUT https://api.example.com/users/1 -d '{"name": "John"}'

    4. Partially update with PATCH:
       http_cli PATCH https://api.example.com/users/1 -d '{"email": "john@example.com"}'

    5. Delete a resource:
       http_cli DELETE https://api.example.com/users/1

    6. Show this help message:
       http_cli HELP
    """
    if not suppress_output:
        print(textwrap.dedent(examples))
    return textwrap.dedent(examples)


def add_common_arguments(parser):
    """Add arguments that are common to multiple commands"""
    parser.add_argument("url", help="Target URL")
    parser.add_argument(
        "-t",
        "--timeout",
        type=int,
        default=30,
        help="Request timeout in seconds (default: 30)",
    )
    parser.add_argument(
        "-H",
        "--header",
        action="append",
        help="HTTP header in 'Key: Value' format. Can be used multiple times.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose logging for debugging.",
    )


def create_parser():
    """Create an argument parser for the HTTP CLI client."""

    class CustomFormatter(argparse.HelpFormatter):
        """Custom formatter for the HTTP CLI client."""

        def _split_lines(self, text, width):
            if text.startswith("R|"):
                return text[2:].splitlines()
            return super()._split_lines(text, width)

    parser = argparse.ArgumentParser(
        description="HTTP CLI client supporting GET, POST, PUT, PATCH, DELETE, HEAD, and OPTIONS methods",
        formatter_class=CustomFormatter,
        add_help=True,
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # HELP command
    subparsers.add_parser(
        "HELP", help="Show detailed help and examples", aliases=["help"]
    )

    # GET command
    get_parser = subparsers.add_parser(
        "GET", help="Make a GET request", aliases=["get"]
    )
    add_common_arguments(get_parser)

    # POST command
    post_parser = subparsers.add_parser(
        "POST", help="Make a POST request", aliases=["post"]
    )
    add_common_arguments(post_parser)
    post_parser.add_argument(
        "-d",
        "--data",
        help='R|JSON data for request body.\nExample: \'{"key": "value"}\'',
    )

    # PUT command
    put_parser = subparsers.add_parser(
        "PUT", help="Make a PUT request", aliases=["put"]
    )
    add_common_arguments(put_parser)
    put_parser.add_argument(
        "-d",
        "--data",
        help='R|JSON data for request body.\nExample: \'{"key": "value"}\'',
    )

    # PATCH command
    patch_parser = subparsers.add_parser(
        "PATCH", help="Make a PATCH request", aliases=["patch"]
    )
    add_common_arguments(patch_parser)
    patch_parser.add_argument(
        "-d",
        "--data",
        help='R|JSON data for request body.\nExample: \'{"key": "value"}\'',
    )

    # DELETE command
    delete_parser = subparsers.add_parser(
        "DELETE", help="Make a DELETE request", aliases=["delete"]
    )
    add_common_arguments(delete_parser)

    # HEAD command
    head_parser = subparsers.add_parser(
        "HEAD", help="Make a HEAD request", aliases=["head"]
    )
    add_common_arguments(head_parser)

    # OPTIONS command
    options_parser = subparsers.add_parser(
        "OPTIONS", help="Make an OPTIONS request", aliases=["options"]
    )
    add_common_arguments(options_parser)

    return parser


def main(suppress_output=False):
    """Main function for the HTTP CLI client."""
    parser = create_parser()
    args = parser.parse_args()

    command = args.command.upper() if args.command else None

    if not command or command == "HELP":
        if not suppress_output:
            parser.print_help()
            print("\n")
        show_examples(suppress_output)
        return

    client = HTTPClient(timeout=args.timeout, verbose=args.verbose)

    try:
        # Prepare request kwargs
        kwargs = {}
        if hasattr(args, "data") and args.data:
            kwargs["json"] = json.loads(args.data)
        # Parse headers if provided
        if hasattr(args, "header") and args.header:
            headers = {}
            for item in args.header:
                if ":" in item:
                    key, value = item.split(":", 1)
                    headers[key.strip()] = value.strip()
            if headers:
                kwargs["headers"] = headers

        # Make the request based on the command
        response = getattr(client, command.lower())(args.url, **kwargs)

        # Print response
        print(f"Status Code: {response.status_code}")
        print("\nHeaders:")
        for key, value in response.headers.items():
            print(f"{key}: {value}")

        # Only print Response Body if there is content
        if response.text.strip():
            print("\nResponse Body:")
            try:
                json_data = json.loads(response.text)
                pretty_response = json.dumps(json_data, indent=4)
                print(pretty_response)
            except ValueError:
                print(response.text)

    except json.JSONDecodeError:
        print("Error: Invalid JSON data")
        print("Make sure your JSON data is properly formatted.")
        print('Example: \'{"key": "value"}\'')
        sys.exit(1)
    except HTTPClientError as e:
        print(f"Error: {str(e)}")
        sys.exit(1)
