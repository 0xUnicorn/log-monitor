from datetime import datetime
from event import EndlesshLoginEvent, FtpLoginEvent


class FtpMonitor:
    
    def __init__(self, dispatcher, log_file: str) -> None:
        self.dispatcher = dispatcher
        self.log_file = log_file

    def fetch(self):
        with open(self.log_file, 'r') as f:
            while True:
                line = f.readline()
                sanitized_line = self._sanitize_line(line)
                if sanitized_line:
                    ftp_login_event = self._create_event(sanitized_line)
                    # print(ftp_login_event)
                    self.dispatcher.dispatch('ftp.login', ftp_login_event)

    def _sanitize_line(self, line: str) -> dict:
        splitted_line = line.split(' ')
        if '"530' in splitted_line:
            if "Login" in splitted_line:
                status = "FAIL"
            else:
                return
        elif '"220' in splitted_line:
            status = "NEW"
        elif '"230' in splitted_line:
            status = "OK"
        else:
            return
        return {
            "ip": line.split(',')[0].split(' ')[-1].strip('"'),
            "date": f"{splitted_line[2]}/{splitted_line[1]}/{splitted_line[4]}-{splitted_line[3]}",
            "status": status
        }

    def _create_event(self, line: dict) -> FtpLoginEvent:
        return FtpLoginEvent(
            date=self._convert_date(line['date']),
            ip=line['ip'],
            status=line['status']
        )

    def _convert_date(self, full_date: list) -> datetime:
        return datetime.strptime(full_date, '%d/%b/%Y-%H:%M:%S')


class EndlesshMonitor:
    
    def __init__(self, dispatcher, log_file: str) -> None:
        self.dispatcher = dispatcher
        self.log_file = log_file

    def fetch(self):
        with open(self.log_file, 'r') as f:
            while True:
                line = f.readline()
                if "CLOSE" in line:
                    endlessh_login_event = self._create_event(line)
                    # print(endlessh_login_event)
                    self.dispatcher.dispatch('endlessh.login', endlessh_login_event)

    def _create_event(self, line:str):
        splitted_line = line.split(' ')
        return EndlesshLoginEvent(
            date=splitted_line[3],
            ip=splitted_line[5].split(':')[-1],
            time=splitted_line[8].split('=')[1],
            bytes_sent=splitted_line[-1].split('=')[1].strip('\n')
        )
