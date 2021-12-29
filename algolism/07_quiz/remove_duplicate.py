# l = [1,3,3,5,5,5,7,9,9,11]
# print(list(set(l)))
# print(list(dict.fromkeys(l)))

from typing import List

def remove_duplicate(numbers:List[int]) -> None:
    len_num = len(numbers) - 1
    while len_num > 0:
        if numbers[len_num] == numbers[len_num - 1]:
            numbers.pop(len_num)
        len_num -= 1
            
if __name__ == '__main__':
    l = [1,3,3,5,5,5,7,9,9,11]
    remove_duplicate(l)
    print(l)
