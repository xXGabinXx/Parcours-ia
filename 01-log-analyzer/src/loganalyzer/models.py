
from dataclasses import dataclass
from datetime import datetime
from ipaddress  import IPv4Address, IPv6Address

@dataclass(frozen=True) # lit seulement annotation (: differnet =)
class FailedLogin:
    timestamp: datetime
    user: str
    ip: IPv4Address | IPv6Address
    port: int
    invalid_user: bool
