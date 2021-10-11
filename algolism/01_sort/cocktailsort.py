import random
from typing import List

"""
Cocktailソート（bubbleソートの改良版）
Big O Notaion:O(n**2)
swapがFalseの時点でソートが終了するため、bubbleよりも少しはやい
"""
# Tsujiba work
def cocktail_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    under_limit = 1
    swap = False
    for i in range(len_numbers):
        for j in range(len_numbers - 1 - i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                swap = True
        if not swap:
            break
        else:
            swap = False
            for k in range(j, under_limit, -1):
                if numbers[k-1] > numbers[k]:
                    numbers[k-1], numbers[k] = numbers[k], numbers[k-1]
                    swap = True 
            under_limit += 1
        if not swap:
            break
    return numbers


if __name__ == '__main__':
    # nums = [2, 3, 5, 9, 1]
    nums = [random.randint(1, 1000) for _ in range(10)]
    print(cocktail_sort(nums))