import argparse
import json
from src.http_cli.http_client import HTTPClient
from src.http_cli.exceptions import HTTPClientError

def create_parser():
    parser = argparse.ArgumentParser(description='Simple HTTP CLI client')
    parser.add_argument('method', choices=['GET', 'POST'], help='HTTP method')
    parser.add_argument('url', help='Target URL')
    parser.add_argument('-d', '--data', help='JSON data for POST requests')
    parser.add_argument('-t', '--timeout', type=int, default=30, help='Request timeout in seconds')
    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()

    client = HTTPClient(timeout=args.timeout)

    try:
        if args.method == 'GET':
            response = client.get(args.url)
        else:  # post
            data = json.loads(args.data) if args.data else None
            response = client.post(args.url, json=data)

        print(f"Status Code: {response.status_code}")
        print("\nHeaders:")
        for key, value in response.headers.items():
            print(f"{key}: {value}")
        print("\nResponse Body:")
        print(response.text)

    except json.JSONDecodeError:
        print("Error: Invalid JSON data")
        exit(1)
    except HTTPClientError as e:
        print(f"Error: {str(e)}")
        exit(1)