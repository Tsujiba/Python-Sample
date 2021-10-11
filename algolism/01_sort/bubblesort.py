import random
from typing import List

"""
バブルソート
Big O Notaion:O(n**2)
"""
# # Tsujiba work
# def bubble_sort(numbers: List[int]) -> List[int]:
#     for i in range(len(numbers)):
#         for j in range(len(numbers) - (i + 1)):
#             if numbers[j] > numbers[j+1]:
#                 tmp = numbers[j]
#                 numbers[j] = numbers[j+1]
#                 numbers[j+1] = tmp
#     return numbers

def bubble_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        for j in range(len_numbers - 1 - i):
            if numbers[j] > numbers[j+1]:
                numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
    return numbers

if __name__ == '__main__':
    nums = [random.randint(1, 1000) for _ in range(10)]
    print(bubble_sort(nums))