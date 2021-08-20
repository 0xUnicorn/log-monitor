from datetime import datetime
from schema import FtpLoginSchema


class FtpMonitor:      

    log_file = "/var/log/vsftpd.log"

    def fetch(self):
        with open(self.log_file, 'r') as f:
            while True:
                line = f.readline()
                if 'LOGIN' in line:
                    schema = self._add_to_schema(line.split())
                    print(schema)

    def _add_to_schema(self, line: list) -> FtpLoginSchema:
        return FtpLoginSchema(
            date=self._convert_date([line[2], line[1], line[4], line[3]]),
            username=line[7].strip('[]'),
            ip=self._get_ip(line[11]),
            status=line[8]
        )

    def _convert_date(self, date: list) -> datetime:
        _full_date = f"{date[0]}/{date[1]}/{date[2]}-{date[3]}"
        return datetime.strptime(_full_date, '%d/%b/%Y-%H:%M:%S')

    def _get_ip(self, log: str) -> str:
        log_list = log.split(':')
        ip = log_list[3][:-1]
        return ip
