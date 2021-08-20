from datetime import datetime
from event import FtpLoginEvent


class FtpMonitor:
    
    def __init__(self, dispatcher) -> None:
        self.dispatcher = dispatcher

    log_file = "/var/log/vsftpd.log"

    def fetch(self):
        with open(self.log_file, 'r') as f:
            while True:
                line = f.readline()
                if line:
                    sanitized_line = self._sanitize_line(line)
                    ftp_login_event = self._create_event(sanitized_line)
                    self.dispatcher.dispatch('ftp.login', ftp_login_event)

    def _sanitize_line(self, line: list) -> dict:
        splitted_line = line.split(' ')
        if "USER" in line:
            username = splitted_line[-1]
        if "530" in line:
            status = "FAILED"
        return {
            "message": line.split(',')[1],
            "ip": line.split(',')[0].split(' ')[-1],
            "date": f"{splitted_line[2]}/{splitted_line[1]}/{splitted_line[4]}-{splitted_line[3]}",
            "username": username,
            "status": status
        }

    def _create_event(self, line: dict) -> FtpLoginEvent:
        return FtpLoginEvent(
            date=self._convert_date(line['date']),
            username=line['username'],
            ip=line['ip'],
            status=line['status']
        )

    def _convert_date(self, full_date: list) -> datetime:
        return datetime.strptime(full_date, '%d/%b/%Y-%H:%M:%S')
