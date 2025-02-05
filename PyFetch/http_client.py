"""HTTP client implementation for making HTTP requests."""

import requests

from PyFetch.exceptions import HTTPClientError, HTTPConnectionError, ResponseError


class HTTPClient:
    """HTTP client for making HTTP requests."""

    def __init__(self, timeout=30, retries=3, verbose=False):
        self.timeout = timeout
        self.retries = retries
        self.verbose = verbose
        self.allowed_methods = [
            "GET",
            "POST",
            "PUT",
            "PATCH",
            "DELETE",
            "HEAD",
            "OPTIONS",
        ]

    def make_request(self, method, url, **kwargs):
        """Make an HTTP request with automatic retries."""
        if method.upper() not in self.allowed_methods:
            raise ValueError(
                f"Unsupported HTTP method. Allowed methods: {', '.join(self.allowed_methods)}"
            )
        for attempt in range(self.retries):
            if self.verbose:
                print(
                    f"[VERBOSE] Attempt {attempt + 1} of {self.retries}: Sending {method} request to {url} with {kwargs}"
                )
            try:
                response = requests.request(
                    method=method, url=url, timeout=self.timeout, **kwargs
                )
                response.raise_for_status()
                if self.verbose:
                    print(
                        f"[VERBOSE] Received response with status {response.status_code} and headers {response.headers}"
                    )
                return response
            except requests.exceptions.ConnectionError as e:
                if self.verbose:
                    print(f"[VERBOSE] ConnectionError on attempt {attempt + 1}: {e}")
                if attempt == self.retries - 1:
                    raise HTTPConnectionError(
                        f"Failed to connect to {url}: {str(e)}"
                    ) from e
            except requests.exceptions.HTTPError as e:
                if self.verbose:
                    print(f"[VERBOSE] HTTPError on attempt {attempt + 1}: {e}")
                if attempt == self.retries - 1:
                    raise ResponseError(f"HTTP error occurred: {str(e)}") from e
            except requests.exceptions.RequestException as e:
                if self.verbose:
                    print(f"[VERBOSE] RequestException on attempt {attempt + 1}: {e}")
                if attempt == self.retries - 1:
                    raise HTTPClientError(f"Request failed: {str(e)}") from e
            # Optionally add a delay between retries
            # time.sleep(delay)

    def get(self, url, **kwargs):
        """Make a GET request."""
        return self.make_request("GET", url, **kwargs)

    def post(self, url, **kwargs):
        """Make a POST request."""
        return self.make_request("POST", url, **kwargs)

    def put(self, url, **kwargs):
        """Make a PUT request."""
        return self.make_request("PUT", url, **kwargs)

    def patch(self, url, **kwargs):
        """Make a PATCH request."""
        return self.make_request("PATCH", url, **kwargs)

    def delete(self, url, **kwargs):
        """Make a DELETE request."""
        return self.make_request("DELETE", url, **kwargs)

    def head(self, url, **kwargs):
        """Make a HEAD request."""
        return self.make_request("HEAD", url, **kwargs)

    def options(self, url, **kwargs):
        """Make an OPTIONS request."""
        return self.make_request("OPTIONS", url, **kwargs)
