from dataclasses import dataclass
from datetime import datetime
from whistle import Event



@dataclass
class FtpLoginEvent(Event):

    date: datetime
    username: str
    ip: str
    status: str

    def as_http_body(self):
        return {
            "date": self.date,
            "username": self.username,
            "ip": self.ip,
            "status": self.status
        }
