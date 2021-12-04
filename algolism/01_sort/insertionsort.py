import random
from typing import List

"""
Insertionソート
Big O Notaion:O(n**2)
比較した数字がスワップした場合に、適切な位置になるまで戻ってスワップする
"""

def insertion_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(1, len_numbers):
        temp = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > temp:
                numbers[j+1] = numbers[j]
                j -= 1
        numbers[j+1] = temp
            
    return numbers

if __name__ == '__main__':
    nums = [random.randint(1, 1000) for _ in range(10)]
    print(insertion_sort(nums))