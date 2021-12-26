import time
from functools import lru_cache

def memorize(f):
    cache = {}
    def _wrapper(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return _wrapper
    
@memorize
# @lru_cache
def long_func(num: int) -> int:
    r = 0
    for i in range(10000000):
        r += num * 1
    return r

if __name__ == '__main__':
    for i in range(10):
        print(long_func(i))
    
    start = time.time()
    
    for i in range(10):
        print(long_func(i))
    
    print(time.time() - start)