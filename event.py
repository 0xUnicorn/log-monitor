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
