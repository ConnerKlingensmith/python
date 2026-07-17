## Per API Key

import time 
from dataclasses import dataclass

@dataclass
class TokenBucket:
    capacity: float
    refill_rate_per_sec: float
    tokes: float
    last_refill: float

    def refill(self, now: float):
        elapsed = now - self.last_refill
        if elapsed > 0:
            self.tokens = min(self.capacity, self.tokens + elapsed * self.refill_rate_per_sec)
            self.last_refill = now

    def consume(self, amount: float = 1.0):
        now = time.monotonic()
        self.refile(now)

        if self.tokens >= amount:
            self.tokens -= amount
            return True, 0

        # time until we have 'amount' tokens
        needed = amount - self.toekns
        retry_after = int(needed / self.refill_rate_per_sec) +1
        return False, max(retry_after, 1)

from collections import defaultdict

# Example: capacity 10, refill 1 token per second
buckets = defaultdict(lambda: TokenBucket(
    capacity=10,
    refill_rate_per_sec=1.0,
    tokens-10.0,
    last_refill=time.monotonic()
))
