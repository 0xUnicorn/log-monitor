from connector import Connector

class Sender:

    def __init__(self, connector: Connector) -> None:
        self.connector = connector

    def send(self, event):
        print(event)
