# PyFetch: A Lightweight HTTP CLI

A lightweight command-line interface for making HTTP requests. Built with Python,
this tool provides an easy way to make GET, POST, PUT, PATCH, DELETE, HEAD, and OPTIONS requests with support for JSON data, customizable timeouts, automatic retries on failures, and a verbose mode for detailed logging.

## Features

- Simple command-line interface
- Case-insensitive commands (GET/get, POST/post etc.)
- Support for GET, PUT, POST, PATCH, DELETE, HEAD, and OPTIONS requests
- JSON data handling for POST requests
- Customizable timeout settings and automatic retries on failures
- Verbose mode for debugging: logs requests and responses
- Detailed response output
  - Status code
  - Response headers
  - Response body (pretty-printed if JSON)
- Comprehensive error handling
- Built-in help system

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- virtualenv _(recommended)_

### Setup

1. Clone the repository:

```bash
git clone https://github.com/Tyrowin/PyFetch.git
cd PyFetch
```

2. Create and activate a virtual environment _(recommended)_:

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/MacOS
python3 -m venv venv
source venv/bin/activate
```

3. Install the package in development mode:

```bash
pip install -e .
```

## Usage

### Example Commands

```bash
# Make a GET request
pyfetch GET https://api.example.com

# Make a POST request with JSON data
pyfetch POST https://api.example.com -d '{"key": "value"}'

# Update a resource with PUT
pyfetch PUT https://api.example.com/users/1 -d '{"name": "John"}'

# Partially update with PATCH
pyfetch PATCH https://api.example.com/users/1 -d '{"email": "john@example.com"}'

# Delete a resource
pyfetch DELETE https://api.example.com/users/1

# Make a HEAD request (fetch headers only)
pyfetch HEAD https://api.example.com

# Make an OPTIONS request (see allowed methods)
pyfetch OPTIONS https://api.example.com

# Show help message
pyfetch HELP
```

## Testing

The project includes a comprehensive test suite using Python's unittest framework.

### Running Tests

Run all tests using either of these commands:

```bash
# Using Python's unittest discover
python -m unittest discover tests

# Using pip's installed test suite
pip install -e .
python setup.py test
```

### Test Coverage

The test suite covers:

- HTTP client functionality
- CLI commands and arguments
- Error handling and exceptions
- Input validation
- Response processing

### Writing Tests

Tests are organized in three main files:

- `tests/test_cli.py` - Command-line interface tests
- `tests/test_http_client.py` - HTTP client functionality tests
- `tests/test_exceptions.py` - Exception handling tests

To add new tests:

1. Choose the appropriate test file based on functionality
2. Create a new test method in the relevant test class
3. Use unittest assertions to verify behavior
4. Run the test suite to ensure all tests pass

## Command Reference

### GET Request

```
usage: pyfetch GET [-h] [-t TIMEOUT] url

positional arguments:
  url                   Target URL

options:
  -h, --help            show this help message and exit
  -t TIMEOUT, --timeout TIMEOUT
                        Request timeout in seconds (default: 30)
```

### POST Request

```
usage: pyfetch POST [-h] [-t TIMEOUT] [-d DATA] url

positional arguments:
  url                   Target URL

options:
  -h, --help            show this help message and exit
  -t TIMEOUT, --timeout TIMEOUT
                        Request timeout in seconds (default: 30)
  -d DATA, --data DATA  R|JSON data for request body. Example: '{"key": "value"}'
```

### PUT Request

```
usage: pyfetch PUT [-h] [-t TIMEOUT] [-d DATA] url

positional arguments:
  url                   Target URL

options:
  -h, --help            show this help message and exit
  -t TIMEOUT, --timeout TIMEOUT
                        Request timeout in seconds (default: 30)
  -d DATA, --data DATA  R|JSON data for request body. Example: '{"key": "value"}'
```

### PATCH Request

```
usage: pyfetch PATCH [-h] [-t TIMEOUT] [-d DATA] url

positional arguments:
  url                   Target URL

options:
  -h, --help            show this help message and exit
  -t TIMEOUT, --timeout TIMEOUT
                        Request timeout in seconds (default: 30)
  -d DATA, --data DATA  R|JSON data for request body. Example: '{"key": "value"}'
```

### DELETE Request

```
usage: pyfetch DELETE [-h] [-t TIMEOUT] url

positional arguments:
  url                   Target URL

options:
  -h, --help            show this help message and exit
  -t TIMEOUT, --timeout TIMEOUT
                        Request timeout in seconds (default: 30)
```

### HEAD Request

```
usage: pyfetch HEAD [-h] [-t TIMEOUT] url

positional arguments:
  url                   Target URL

options:
  -h, --help            show this help message and exit
  -t TIMEOUT, --timeout TIMEOUT
                        Request timeout in seconds (default: 30)
```

### OPTIONS Request

```
usage: pyfetch OPTIONS [-h] [-t TIMEOUT] url

positional arguments:
  url                   Target URL

options:
  -h, --help            show this help message and exit
  -t TIMEOUT, --timeout TIMEOUT
                        Request timeout in seconds (default: 30)
```

## Response Format

```
Status Code: 200

Headers:
content-type: application/json
cache-control: no-cache
...

Response Body:
{
    "data": {
        ...
    }
}
```

## Error Handling

The CLI handles various types of errors:

- Connection errors
- Invalid JSON data
- HTTP response errors
- Request timeout errors
- Keyboard interrupts (Ctrl+C)

All errors are displayed with descriptive messages to help diagnose the issue.

## Contributing

1. Fork the repository
2. Create your feature branch (git checkout -b feature/amazing-feature)
3. Commit your changes (git commit -m 'Add some amazing feature')
4. Push to the branch (git push origin feature/amazing-feature)
5. Open a Pull Request

## Troubleshooting

### Common Issues

1. Command not found:
   - Make sure the package is installed (`pip list | findstr PyFetch`)
   - Ensure your virtual environment is activated
2. Import errors:
   - Try reinstalling the package: `pip install -e .`
   - Make sure you're using the correct Python environment
3. JSON errors:
   - Verify your JSON data is properly formatted
   - Use single quotes around the entire JSON string and double quotes inside

## License

This project is licensed under the Apache License, Version 2.0 - see the LICENSE file for details.
