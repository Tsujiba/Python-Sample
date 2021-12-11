import random
from typing import List

"""
Quickソート
Big O Notaion:best:O(nlog(n)),worst:O(n**2)
基準値（pivot）を設定し、基準値より小さい、大きいグループに分割（partition）、
分割後に各グループにおいて、同様の操作を繰り返すことですデータ整列を行う
"""

# 最後の値をpivotにしている、pivotの挿入されたインデックス番号をかえす
def partition(numbers: List[int], low: int, high: int) -> int:
    i = low - 1
    pivot = numbers[high]
    for j in range(low, high):
        if numbers[j] <= pivot:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]
    numbers[i+1], numbers[high] = numbers[high], numbers[i+1]
    return i+1

def quick_sort(numbers: List[int]) -> List[int]:
    def _quick_sort(numbers: List[int], low: int, high:int) -> None:
        print(numbers)
        if low < high:
            partition_index = partition(numbers, low, high)
            _quick_sort(numbers, low, partition_index-1)
            _quick_sort(numbers, partition_index+1, high)
    _quick_sort(numbers, 0, len(numbers)-1)
    return numbers 

if __name__ == '__main__':
    nums = [random.randint(1, 1000) for _ in range(10)]
    # nums = [1, 8, 3, 9, 4, 5, 7]
    print(quick_sort(nums))