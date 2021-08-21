from multiprocessing import Process

from sender import Sender
from monitor import EndlesshMonitor, FtpMonitor
from connector import Connector

from whistle import EventDispatcher


def main():

    connector = Connector(url="http://192.168.10.10:8000")
    
    ftp_sender = Sender(connector, endpoint="/ftp-login/")
    endlessh_sender = Sender(connector, endpoint="/endlessh-login/")

    dispatcher = EventDispatcher()
    dispatcher.add_listener('ftp.login', ftp_sender.send)
    dispatcher.add_listener('endlessh.login', endlessh_sender.send)

    # ftp_monitor = FtpMonitor(dispatcher, "./ftp_logfile.log")
    ftp_monitor = FtpMonitor(dispatcher, "/var/log/ftp/vsftpd.log")
    p_ftp = Process(target=ftp_monitor.fetch)

    # endlessh_monitor = EndlesshMonitor(dispatcher, "./endlessh_logfile.log")
    endlessh_monitor = EndlesshMonitor(dispatcher, "/var/log/endlessh/current")
    p_ssh = Process(target=endlessh_monitor.fetch)
    
    p_ftp.start()
    p_ssh.start()
    p_ftp.join()
    p_ssh.join()

if __name__ == "__main__":
    main()
