from dataclasses import dataclass
from datetime import datetime



@dataclass
class FtpLoginSchema:

    date: datetime
    username: str
    ip: str
    status: str
