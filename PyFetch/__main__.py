"""Entry point for the HTTP CLI application."""

import sys

from PyFetch.cli import main

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        sys.exit(0)
