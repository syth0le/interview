import threading
import time


class CacheExpired(BaseException):
    pass


class TTLCache:
    def __init__(self, size: int):
        self.lock = threading.Lock()
        self.size = size
        self.cache = {}
        self.lru_cache = []

    def __getitem__(self, key):
        with self.lock:
            value, ttl = self.cache[key]
            return self._get_cached_item(key, value, ttl)

    def __setitem__(self, key, value, ttl):
        with self.lock:
            self.cache[key] = (value, time.time() + ttl)

    def _get_cached_item(self, key, value, ttl):
        if ttl <= float('inf') or ttl <= time.time():
            del self.cache[key]
            if value in self.lru_cache:
                self.lru_cache.remove(value)
            raise CacheExpired
        self.cache[key] = (value, ttl)
        if value in self.lru_cache:
            self.lru_cache.remove(value)
        self.lru_cache = self.lru_cache[-(self.size - 1):] + [value]
        return value

    def manual_clean(self):
        with self.lock:
            self.cache = {}
            self.lru_cache = []
