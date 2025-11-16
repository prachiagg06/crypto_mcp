
from tools.cache import cache

def test_cache():
    cache.set("a", 1)
    assert cache.get("a") == 1
