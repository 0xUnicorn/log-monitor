import requests

class Connector:

    def __init__(self, url):
        self.url = url

    def connect_to_api(self, endpoint, data):
        return self._post_request(
            url=f"{self.url}{endpoint}",
            data=data
        )

    def _post_request(self, url, data):
        return requests.post(
            url=url,
            data=data,
            headers=self._headers()
        )

    def _headers(self):
        return {
            "Content-Type": "application/json"
        }
