import random
from typing import List

"""
Gnomeソート（bubbleソートの改良版）
Big O Notaion:O(n**2)
"""

# # Tsujiba's work
# def gnome_sort(numbers: List[int]) -> List[int]:
#     len_numbers = len(numbers)
    
#     for i in range(len_numbers-1):
#         if numbers[i] > numbers[i+1]:
#             numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
#             reverse_check = True
#             j = i
#             while j != 0 & reverse_check:
#                 if numbers[j-1] > numbers[j]:
#                     numbers[j-1], numbers[j] = numbers[j], numbers[j-1]
#                 else:
#                     reverse_check = False
#                 j = j - 1
#     return numbers

def gnome_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    index = 0
    while index < len_numbers:
        if index == 0:
            index += 1
        if numbers[index] >= numbers[index-1]:
            index += 1
        else:
            numbers[index], numbers[index-1] = numbers[index-1], numbers[index]
            index -= 1
    
    return numbers


if __name__ == '__main__':
    # nums = [4, 3, 6, 1, 2]
    nums = [random.randint(1, 1000) for _ in range(10)]
    print(gnome_sort(nums))