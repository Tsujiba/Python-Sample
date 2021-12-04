import random
from typing import List

"""
Shellソート
Big O Notaion:best:O(nlog(n)),worst:O(n**2)
一定間隔（GAP）でグループ分け→グループ毎にinsertionソート→GAPを詰めてくりかえす
※挿入ソートには、「すでに整列済みになっている部分が多いほど高速になる」という特性があるため、
全体を荒くソートしていくことで、結果的に全体のソートはかなり高速に終えられるという理屈
"""

def shell_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    gap = len_numbers // 2
    while gap > 0:
        for i in range(gap, len_numbers):
            temp = numbers[i]
            j = i
            while j >= gap and numbers[j - gap] > temp:
                numbers[j] = numbers[j - gap]
                j -= gap
            numbers[j] = temp
        gap //= 2
    return numbers 

if __name__ == '__main__':
    nums = [random.randint(1, 1000) for _ in range(10)]
    print(shell_sort(nums))