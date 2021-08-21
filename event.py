from dataclasses import dataclass
from datetime import datetime
from whistle import Event



@dataclass
class FtpLoginEvent(Event):

    date: datetime
    ip: str
    status: str

    def as_http_body(self):
        return {
            "date": self.date.isoformat(),
            "ip": self.ip,
            "status": self.status
        }

@dataclass
class EndlesshLoginEvent(Event):

    date: str
    ip: str
    time: float
    bytes_sent: int

    def as_http_body(self):
        return {
            "date": self.date,
            "ip": self.ip,
            "time_wasted": self.time,
            "bytes_sent": self.bytes_sent
        }
