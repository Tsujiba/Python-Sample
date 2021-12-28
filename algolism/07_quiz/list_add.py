"""
[1] -> [2] -> 2
[8, 9] -> [9, 0] -> 90
[9, 9] -> [1, 0, 0] -> 100
[0, 0, 0, 9, 9, 9, 9] -> [1, 0, 0, 0, 0] -> 10000
"""

# 文字列に変換するやり方はなし
# l = [1, 2, 3]
# print(int(''.join([str(i) for i in l])) + 1)

from typing import List

def remove_zero(nums: List[int]) -> None:
    if nums[0] == 0:
        nums.pop(0)
        remove_zero(nums)
        
def list_to_int(nums: List[int]) -> int:
    sum_nums = 0
    for i, num in enumerate(reversed(nums)):
        sum_nums += num *(10**i) 
    return sum_nums
        

def list_add(nums : List[int]) -> int:
    result_list = []
    first_place_flag = 1
    advance = 0
    for num in reversed(nums):
        if first_place_flag == 1:
            if num == 9:
                result_list.insert(0, 0)
                advance = 1
            else:
                result_list.insert(0, num + 1)
            first_place_flag = 0            
        elif advance:
            if num == 9:
                result_list.insert(0, 0)
            else:
                result_list.insert(0, num + 1)
                advance = 0
        else:
            result_list.insert(0, num) 
        
    if advance:
        result_list.insert(0, 1)
        
    remove_zero(result_list)
    
    return list_to_int(result_list)  
        
            


if __name__ == '__main__':
    l1 = [1]
    l2 = [8, 9]
    l3 = [9, 9]
    l4 = [0, 0, 0, 9, 9, 9, 9]
    print(list_add(l1))
    print(list_add(l2))
    print(list_add(l3))
    print(list_add(l4))