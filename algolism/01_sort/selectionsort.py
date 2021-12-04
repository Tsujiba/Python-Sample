import random
from typing import List

"""
Selectionソート（bubbleソートの改良版）
Big O Notaion:O(n**2)
１番小さい（大きい）ものを見つけ、Tempに入れ、最後にあるべき場所と入れ替える
"""

def selection_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    
    for i in range(len_numbers):
        tmp = i
        for j in range(i+1, len_numbers, 1):
            if numbers[tmp] > numbers[j]:
                tmp = j
        numbers[i], numbers[tmp] = numbers[tmp],numbers[i]
    return numbers

if __name__ == '__main__':
    # nums = [4, 3, 6, 1, 2]
    nums = [random.randint(1, 1000) for _ in range(10)]
    print(selection_sort(nums))