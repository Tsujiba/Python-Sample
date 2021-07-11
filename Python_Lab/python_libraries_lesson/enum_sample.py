"""
#############################################################################:
・functools.lru_cache
　・キャッシュを操作できる
#############################################################################
"""

import functools

# LRU形式のキャッシュ（maxsizeが5だと6~10番目の計算結果が格納される）
@functools.lru_cache(maxsize=5)
def long_func(n):
    result = 0
    for i in range(10000000):
        result += n * i
    return result

for i in range(10):
    print(long_func(i))

print(long_func.cache_info())

    
print('Next Run!')

for i in reversed(range(10)):
    print(long_func(i))
    
print(long_func.cache_info())

