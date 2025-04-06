"""HTTP client implementation for making HTTP requests."""

import requests
from tqdm import tqdm

from PyFetch.exceptions import HTTPClientError, HTTPConnectionError, ResponseError


class HTTPClient:
    """HTTP client for making HTTP requests."""

    def __init__(self, timeout=30, retries=3, verbose=False, show_progress=False):
        self.timeout = timeout
        self.retries = retries
        self.verbose = verbose
        self.show_progress = show_progress
        self.allowed_methods = [
            "GET",
            "POST",
            "PUT",
            "PATCH",
            "DELETE",
            "HEAD",
            "OPTIONS",
        ]
        self.MIN_SIZE_FOR_PROGRESS = 5 * 1024 * 1024  # 5MB

    def _create_progress_bar(self, total, desc):
        """Create a progress bar for file transfer."""
        if self.show_progress and total >= self.MIN_SIZE_FOR_PROGRESS:
            return tqdm(
                total=total,
                unit="B",
                unit_scale=True,
                desc=desc,
                disable=not self.show_progress,
            )
        return None

    def _stream_response(self, response, progress_bar=None):
        """Stream response content with progress indication."""
        chunk_size = 8192
        content = b""

        for chunk in response.iter_content(chunk_size=chunk_size):
            if chunk:
                content += chunk
                if progress_bar:
                    progress_bar.update(len(chunk))

        if progress_bar:
            progress_bar.close()

        return content

    def make_request(self, method, url, **kwargs):
        """Make an HTTP request with automatic retries and progress indication."""
        if method.upper() not in self.allowed_methods:
            raise ValueError(
                f"Unsupported HTTP method. Allowed methods: {', '.join(self.allowed_methods)}"
            )

        # Ensure stream=True for GET requests to enable progress tracking
        if method.upper() == "GET":
            kwargs["stream"] = True

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

                # Handle progress indication for GET requests
                if method.upper() == "GET" and self.show_progress:
                    total = int(response.headers.get("content-length", 0))
                    progress_bar = self._create_progress_bar(
                        total, f"Downloading {url}"
                    )
                    content = self._stream_response(response, progress_bar)
                    response._content = content

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
