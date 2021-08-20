from datetime import datetime
from event import FtpLoginEvent


class FtpMonitor:
    
    def __init__(self, dispatcher, log_file: str) -> None:
        self.dispatcher = dispatcher
        self.log_file = log_file

    def fetch(self):
        with open(self.log_file, 'r') as f:
            while True:
                line = f.readline()
                sanitized_line = self._sanitize_line(line)
                if line:
                    ftp_login_event = self._create_event(sanitized_line)
                    self.dispatcher.dispatch('ftp.login', ftp_login_event)

    def _sanitize_line(self, line: str) -> dict:
        splitted_line = line.split(' ')
        if "530" in splitted_line:
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
