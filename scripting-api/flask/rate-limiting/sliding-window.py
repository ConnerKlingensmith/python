## NOT FLASK ##

import time
from collections import defaultdict, deque

RATE_LIMIT = 10 # requests
WINDOW = 10 # seconds
request_log = defaultdict(deque)

def sliding_window_check(api_key: str):
    # time.monotonic() is more accurate that time.time
    now = time.monotonic()
    log = request_log[api_key]

    # Remove timestampe outside the windows
    cutoff = now - WINDOW
    while log and log[0] < cutoff:
        log.popleft()

    if len(log) < RATE_LIMIT:
        log.append(now)
        return True, 0

    # Oldest request still in-window determines when we can retry
    retry_after = int((log[0] + WINDOW) - now) +1
    return False, max(retry_after, 1)

