from typing import List, NewType

IndexNum = NewType('IndexNum', int)



# リストの最初からサーチする
def linear_search(number:List[int], value:int) -> IndexNum:
    for i in range(0, len(number)):
        if number[i] == value:
            return i
    return -1


# 中間値を計算し、そこから狭めていってサーチする
def binary_search(number:List[int], value:int) -> IndexNum:
    left, right = 0, len(number) - 1
    while left <= right:
        mid = (left + right) // 2
        if number[mid] == value:
            return mid
        elif number[mid] < value:
            left = mid + 1
        elif number[mid] < value:
            right = mid -1
            
# 再帰関数を利用して実装したバージョン
def binary_search_recursive(number:List[int], value:int) -> IndexNum:
    def _binary_search_recursive(number:List[int], value:int, left:IndexNum, right:IndexNum) -> IndexNum:
        if left > right:
            return -1
        mid = (left + right) // 2
        if number[mid] == value:
            return mid
        elif number[mid] < value:
            return _binary_search_recursive(number, value, mid + 1, right)
        elif number[mid] > value:
            return _binary_search_recursive(number, value, left, mid - 1)
        
    return _binary_search_recursive(number, value, 0, len(number) - 1)
    
if __name__ == '__main__':
    nums = [0, 1, 5, 7, 9, 11, 15, 20, 24]
    # print(linear_search(nums, 15))
    print(binary_search_recursive(nums, 15))

