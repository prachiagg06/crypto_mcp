
import time

class Cache:
    def __init__(self):
        self.data = {}
        self.ttl = 5

    def set(self, key, val):
        self.data[key] = (val, time.time())

    def get(self, key):
        if key in self.data:
            val, ts = self.data[key]
            if time.time() - ts < self.ttl:
                return val
        return None

cache = Cache()
