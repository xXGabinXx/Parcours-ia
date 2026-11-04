
class LogAnalyzerError(Exception):
    """Erreur de base de loganalyzer."""


class ParseError(LogAnalyzerError):
    """Une ligne de log n'a pas pu être analysée."""