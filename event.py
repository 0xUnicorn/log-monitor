from dataclasses import dataclass
from datetime import datetime
from whistle import Event



@dataclass
class FtpLoginEvent(Event):

    date: datetime
    ip: str
    status: str

    def __repr__(self) -> str:
        return f"FTP Login - Date: {self.date} | IP: {self.ip} | Status: {self.status}"

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

    def __repr__(self) -> str:
        return f"Endlessh Login - Date: {self.date} | IP: {self.ip} | Time: {self.time} | Bytes: {self.bytes_sent}"

    def as_http_body(self):
        return {
            "date": self.date,
            "ip": self.ip,
            "time_wasted": self.time,
            "bytes_sent": self.bytes_sent
        }
