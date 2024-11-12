import argparse
import json
import textwrap
from http_cli.http_client import HTTPClient
from http_cli.exceptions import HTTPClientError


def show_examples():
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
    print(textwrap.dedent(examples))


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


def create_parser():
    class CustomFormatter(argparse.HelpFormatter):
        def _split_lines(self, text, width):
            if text.startswith("R|"):
                return text[2:].splitlines()
            return argparse.HelpFormatter._split_lines(self, text, width)

    parser = argparse.ArgumentParser(
        description="HTTP CLI client supporting GET, POST, PUT, PATCH, and DELETE methods",
        formatter_class=CustomFormatter,
        add_help=True,
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # HELP command
    help_parser = subparsers.add_parser(
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

    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()

    command = args.command.upper() if args.command else None

    if not command or command == "HELP":
        parser.print_help()
        print("\n")
        show_examples()
        return

    client = HTTPClient(timeout=args.timeout)

    try:
        # Prepare request kwargs
        kwargs = {}
        if hasattr(args, "data") and args.data:
            kwargs["json"] = json.loads(args.data)

        # Make the request based on the command
        response = getattr(client, command.lower())(args.url, **kwargs)

        # Print response
        print(f"Status Code: {response.status_code}")
        print("\nHeaders:")
        for key, value in response.headers.items():
            print(f"{key}: {value}")
        print("\nResponse Body:")
        print(response.text)

    except json.JSONDecodeError:
        print("Error: Invalid JSON data")
        print("Make sure your JSON data is properly formatted.")
        print('Example: \'{"key": "value"}\'')
        exit(1)
    except HTTPClientError as e:
        print(f"Error: {str(e)}")
        exit(1)
