import sys
from cache import LRUCache

print("Python version: {}.{}".format(sys.version_info.major, sys.version_info.minor))

cache = LRUCache(100)
cache.set('Jesse', 'Pinkman')
cache.set('Walter', 'White')
cache.set('Jesse', 'James')
print(cache.get('Jesse')) # вернёт 'James'
cache.remove('Walter')
print(cache.get('Walter')) # вернёт ''