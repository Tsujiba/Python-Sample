"""
1.最大部分和問題
Input:[1, -2, 3, 6, -1, 2, 4, -5, 2]
Output:14(3, 6, -1 , 2, 4)

"""

from typing import List

def maximum_subarray_sum(list: List[int]) -> int:
    max_sum = list[0]
    
    for i in range(len(list)):
        current_sum = list[i]
        for j in range(i + 1, len(list)):
            current_sum += list[j]
            if(current_sum > max_sum):
                max_sum = current_sum
    
    return max_sum
    
if __name__ == '__main__':
    l = [1, -2, 3, 6, -1, 2, 4, -5, 2]
    print(maximum_subarray_sum(l))
            