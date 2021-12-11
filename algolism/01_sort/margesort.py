import random
from typing import List

"""
Margeソート
Big O Notaion:best:O(nlog(n)),worst:O(nlog(n))
リストを半分に分割していき、最小単位になったら、各単位をマージして
最終的に並び変える（再帰的な動作をする）
"""

def marge_sort(numbers: List[int]) -> List[int]:
    if len(numbers) <= 1:
        return numbers
    center = len(numbers) // 2
    
    left = numbers[:center]
    right = numbers[center:]
    
    marge_sort(left)
    marge_sort(right)
    
    i = 0 # leftのindex
    j = 0 # rightのindex
    k = 0 # numbersのindex
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            numbers[k] = left[i]
            i += 1
        else:
            numbers[k] = right[j]
            j += 1
        k += 1
    
    while i < len(left):
        numbers[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        numbers[k] = right[j]
        j += 1
        k += 1
    
    return numbers 

if __name__ == '__main__':
    # nums = [random.randint(1, 1000) for _ in range(10)]
    nums = [5, 4, 1, 8, 7, 3, 2, 9]
    print(marge_sort(nums))