from monitor import FtpMonitor
from connector import Connector
from multiprocessing import Process


def main():

    connector = Connector("IP-ADDRESS")

    monitor = FtpMonitor()

    

    p = Process(target=monitor.fetch)
    p.start()
    p.join()

main()
