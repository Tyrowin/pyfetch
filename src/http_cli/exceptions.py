class HTTPClientError(Exception):
    """Base exception for HTTP client errors"""
    pass

class ConnectionError(HTTPClientError):
    """Raised when connection fails"""
    pass

class ResponseError(HTTPClientError):
    """Raised when response is invalid"""
    pass