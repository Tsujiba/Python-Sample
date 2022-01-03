"""
ある数以下の素数を生成する
"""

from typing import List
import time

def generate_primes_v1(number: int) -> List[int]:
    primes = []
    for x in range(2, number + 1):
        for y in range(2, x):
            if x % y == 0:
                break
        else:
            primes.append(x)
    return primes


# cacheを使う考え  
def generate_primes_v2(number: int) -> List[int]:
    primes = []
    cache = {}
    for x in range(2, number + 1):
        is_primes = cache.get(x)
        if is_primes == False:
            continue
        else:
            primes.append(x)
            for y in range(x*2, number + 1, x):
                cache[y] = False
    
    return primes


if __name__ == '__main__':
    start_time = time.time()
    print(generate_primes_v1(300))
    print(time.time() - start_time)
    
    start_time = time.time()
    print(generate_primes_v2(300))
    print(time.time() - start_time)