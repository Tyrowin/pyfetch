import requests
from src.http_cli.exceptions import ConnectionError, ResponseError, HTTPClientError


class HTTPClient:
    def __init__(self, timeout=30):
        self.timeout = timeout

    def make_request(self, method, url, **kwargs):
        try:
            response = requests.request(
                method=method,
                url=url,
                timeout=self.timeout,
                **kwargs
            )
            response.raise_for_status()
            return response
        except requests.exceptions.ConnectionError as e:
            raise ConnectionError(f"Failed to connect to {url}: {str(e)}")
        except requests.exceptions.HTTPError as e:
            raise ResponseError(f"HTTP error occurred: {str(e)}")
        except requests.exceptions.RequestException as e:
            raise HTTPClientError(f"Request failed: {str(e)}")

    def get(self, url, **kwargs):
        return self.make_request("GET", url, **kwargs)

    def post(self, url, **kwargs):
        return self.make_request("POST", url, **kwargs)