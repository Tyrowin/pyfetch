# HTTP CLI

A lightweight command-line interface for making HTTP requests. Built with Python, 
this tool provides an easy way to make GET and POST requests with support for JSON data and customizable timeouts.

## Features

- Simple command-line interface
- Case-insensitive commands (GET/get, POST/post etc.)
- Support for GET, PUT, POST, PATCH and DELETE requests
- JSON data handling for POST requests
- Customizable timeout settings
- Detailed response output
  - Status code
  - Response headers
  - Response body
- Comprehensive error handling
- Built-in help system

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- virtualenv *(recommended)*

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/http-cli.git
cd http-cli
```

2. Create and activate a virtual environment *(recommended)*:
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
http_cli GET https://api.example.com

# Make a POST request with JSON data
http_cli POST https://api.example.com -d '{"key": "value"}'

# Update a resource with PUT
http_cli PUT https://api.example.com/users/1 -d '{"name": "John"}'

# Partially update with PATCH
http_cli PATCH https://api.example.com/users/1 -d '{"email": "john@example.com"}'

# Delete a resource
http_cli DELETE https://api.example.com/users/1

# Show help message
http_cli HELP
```

## Command Reference

### GET Request

```
usage: http_cli GET [-h] [-t TIMEOUT] url

positional arguments:
  url                   Target URL

options:
  -h, --help            show this help message and exit
  -t TIMEOUT, --timeout TIMEOUT
                        Request timeout in seconds (default: 30)
```

### POST Request

```
usage: http_cli POST [-h] [-t TIMEOUT] [-d DATA] url

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
usage: http_cli PUT [-h] [-t TIMEOUT] [-d DATA] url

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
usage: http_cli PATCH [-h] [-t TIMEOUT] [-d DATA] url

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
usage: http_cli DELETE [-h] [-t TIMEOUT] url

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
   - Make sure the package is installed (```pip list | findstr http-cli```)
   - Ensure your virtual environment is activated
2. Import errors:
   - Try reinstalling the package: ```pip install -e .```
   - Make sure you're using the correct Python environment
3. JSON errors:
   - Verify your JSON data is properly formatted
   - Use single quotes around the entire JSON string and double quotes inside

## License

This project is licensed under the Apache License, Version 2.0 - see the LICENSE file for details.