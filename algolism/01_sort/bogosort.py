import random
from typing import List

"""
bogosort
ランダムに並び替えて、順番通りに一致するかまでランダムにシャッフルする
・適当だから遅い、ラッキー狙い、あまりつかわれない
"""

def in_order(numbers: List[int]) -> bool:
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i+1]:
            return False
    return True 

def bogo_sort(numbers: List[int]) -> List[int]:
    while not in_order(numbers):
        random.shuffle(numbers)
    return numbers


if __name__ == '__main__':
    nums = [random.randint(1, 1000) for _ in range(10)]
    # print(nums)
    print(bogo_sort(nums))
    
    