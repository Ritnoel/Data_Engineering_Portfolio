import requests
from requests.exceptions import HTTPError
import json



class BaseAPI:
    def _init_(self, base_url: str, headers: dict = None) -> None:
        self.base_url = base_url
        self.headers = headers or {}

    def get(self, endpoint, params=None):
        """Send a GET request."""
        url = f"{self.base_url}{endpoint}"
        print(f"URL: {url}")
        try:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            print(f"{response.status_code}")
            return response.json()
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")


class GameAPI(BaseAPI):
    def _init_(self, base_url, headers=None):
        super()._init_(base_url, headers)

    @staticmethod
    def _to_jsonl_buffer(json_data):
        return "\n".join([json.dumps(record) for record in json_data])