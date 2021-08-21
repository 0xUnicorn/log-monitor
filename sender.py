import json

from connector import Connector


class Sender:

    def __init__(self, connector: Connector, endpoint: str) -> None:
        self.connector = connector
        self.endpoint = endpoint

    def send(self, event):
        print(f"Sending event: {event}")

        response = self.connector.connect_to_api(
            endpoint=self.endpoint,
            data=json.dumps(event.as_http_body())
        )

        print(response.text)
