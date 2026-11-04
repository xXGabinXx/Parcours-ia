from datetime import datetime
from ipaddress import ip_address

from loganalyzer.errors import ParseError
from loganalyzer.models import FailedLogin


def parse_line(line: str, year: int) -> FailedLogin | None:
    """Transforme une ligne de log en FailedLogin, ou None si elle ne concerne pas un échec SSH."""
    if "Failed password" not in line:                 # la ligne ne contient pas "Failed password"
        return None

    try:
        morceaux = line.split()
        user = morceaux[morceaux.index("from") - 1]
        ip = ip_address(morceaux[morceaux.index("from") + 1])
        port = int(morceaux[morceaux.index("port") + 1])
        invalid_user = "invalid" in morceaux
        texte_date = f"{year} {morceaux[0]} {morceaux[1]} {morceaux[2]}"
        timestamp = datetime.strptime(texte_date, "%Y %b %d %H:%M:%S")
    except ValueError as e:
        raise ParseError(f"Ligne illisible : {line!r}") from e

    return FailedLogin(timestamp, user, ip, port, invalid_user)