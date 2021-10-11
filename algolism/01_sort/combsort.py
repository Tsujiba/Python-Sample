import random
from typing import List

"""
Combソート（bubbleソートの改良版）
Big O Notaion:計算量がGAPによる変わる
"""

def comb_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    gap = len_numbers
    swapped = True
    
    while gap != 1 or swapped:
        gap = int(gap / 1.3)
        if gap < 1:
            gap = 1

        swapped = False
        for i in range(0, len_numbers - gap):
            if numbers[i] > numbers[i+gap]:
                numbers[i], numbers[i+gap] = numbers[i+gap], numbers[i]
                swapped = True
    return numbers

if __name__ == '__main__':
    nums = [random.randint(1, 1000) for _ in range(10)]
    print(comb_sort(nums))