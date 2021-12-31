#Q1 [0, 1, 3, 4, 2, 4, 5, 1, 6, 9, 8] -> [0, 4, 2, 4, 6, 8, 1, 3, 5, 1, 9]

from typing import List

# 新たにリストを作成する方法
def order_even_first_odd_last_v1(numbers: List[int]) -> None:
    even_list = []
    odd_list = []
    
    for number in numbers:
        if number % 2 == 0:
            even_list.append(number)
        else:
            odd_list.append(number)
    
    numbers[:] = even_list + odd_list

# 新たにリストを作成しない方法
def order_even_first_odd_last_v2(numbers: List[int]) -> None:
    i, j = 0, len(numbers)-1
    while i < j:
        if numbers[i] % 2 == 0:
            i += 1
        else:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            j -= 1


#Q2 Input:['h', 'y', 'n', 'p', 't', 'o'], [3, 1, 5, 0, 2, 4]
#   Output:python

def order_by_indexlist(strlist: List[str], index_list: List[int]) -> str:
    i = 0
    while i < len(index_list):
        index = index_list[i]
        index_list[i], index_list[index] = index_list[index], index_list[i]
        strlist[i], strlist[index] = strlist[index], strlist[i]
        if i == index_list[i]:
            i += 1
        
    print(strlist)
    return ''.join(strlist)



if __name__ == '__main__':
    # # Q1
    # numbers = [0, 1, 3, 4, 2, 4, 5, 1, 6, 9, 8]
    # order_even_first_odd_last_v2(numbers)
    # print(numbers)
    
    # Q2
    order_by_indexlist(['h', 'y', 'n', 'p', 't', 'o'], [3, 1, 5, 0, 2, 4])