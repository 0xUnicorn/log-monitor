from sender import Sender
from monitor import FtpMonitor
from connector import Connector

from whistle import EventDispatcher


def main():

    connector = Connector(url="http://192.168.10.10:8000")
    sender = Sender(connector, endpoint="/ftp-login/")

    dispatcher = EventDispatcher()
    dispatcher.add_listener('ftp.login', sender.send)

    monitor = FtpMonitor(dispatcher)
    monitor.fetch()

if __name__ == "__main__":
    main()
