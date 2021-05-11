import re
from tornado import routing

class HostPortMatches(routing.Matcher):
    """Matches requests including the port number in the Host: header"""
    def __init__(self, host_pattern):
        if isinstance(host_pattern, str):
            self.host_pattern = re.compile(host_pattern, re.IGNORECASE)
        else:
            self.host_pattern = host_pattern

    def match(self, request):
        if self.host_pattern.match(request.headers.get("Host") or "127.0.0.1"):
            return {}

        return None

