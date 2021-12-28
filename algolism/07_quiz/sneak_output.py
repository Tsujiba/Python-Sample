from typing import List
from typing import List

def sneak_string_v1(chars: str) -> List[List[str]]:
    result = [[], [], []]
    index = len(result) // 2
    up_flag = 1
    for char in chars:
        if index == 0:
            result[0].append(char)
            result[1].append(' ')
            result[2].append(' ')
            index = 1
            up_flag = 0
        elif index == 1: 
            result[0].append(' ')
            result[1].append(char)
            result[2].append(' ')
            if up_flag:
                index -= 1
            else:
                index += 1
        elif index == 2:
            result[0].append(' ')
            result[1].append(' ')
            result[2].append(char)
            up_flag = 1
            index = 1
        
    return result

def sneak_string_v2(chars: str, size: int) -> List[List[str]]:
    result = [[] for _ in range(size)]
    result_index = {i for i in range(len(result))}
    insert_index = len(result) // 2
    up_flag = 1
    
    for char in chars:
        result[insert_index].append(char)
        for rest_index in result_index - {insert_index}:
            result[rest_index].append(' ')
            
        if insert_index == min(result_index):
            insert_index += 1
            up_flag = 0
        elif insert_index == max(result_index):
            insert_index -= 1
            up_flag = 1
        else:
            if up_flag:
                insert_index -= 1
            else:
                insert_index += 1
    
    return result
    

def print_sneak(result: List[List[str]]) -> None:
    for list in result:
        print(''.join(list))
        
        
        
if __name__ == '__main__':
    chars1 = '012345678901234567890123456789'
    chars2 = 'abcdefghijklmnopqrstuzwxyz'
    # result = sneak_string_v1(chars1)
    # print_sneak(result)
    result = sneak_string_v2(chars2, 10)
    print_sneak(result)