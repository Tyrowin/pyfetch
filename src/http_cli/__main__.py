"""Entry point for the HTTP CLI application."""

import sys

from http_cli.cli import main

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        sys.exit(0)
