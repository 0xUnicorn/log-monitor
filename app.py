from sender import Sender
from monitor import FtpMonitor
from connector import Connector


from multiprocessing import Process
from whistle import EventDispatcher


def main():

    connector = Connector("IP-ADDRESS")

    sender = Sender(connector)

    dispatcher = EventDispatcher()

    dispatcher.add_listener('ftp.login', sender.send)

    monitor = FtpMonitor(dispatcher)

    monitor.fetch()

main()
