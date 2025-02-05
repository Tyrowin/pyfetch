"""Custom exceptions for the HTTP CLI client."""


class HTTPClientError(Exception):
    """Base exception for HTTP client errors"""


class HTTPConnectionError(HTTPClientError):
    """Raised when connection fails"""


class ResponseError(HTTPClientError):
    """Raised when response is invalid"""
