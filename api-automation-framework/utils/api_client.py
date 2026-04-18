import requests
from utils.config import BASE_URL, TIMEOUT, API_KEY

class APIClient:

    headers = {
        "x-api-key": API_KEY
    }

    @staticmethod
    def get(endpoint, params=None):
        return requests.get(
            f"{BASE_URL}{endpoint}",
            headers=APIClient.headers,
            params=params,
            timeout=TIMEOUT
        )