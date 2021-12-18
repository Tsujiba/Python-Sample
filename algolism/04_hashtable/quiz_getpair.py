from typing import List, Tuple, Optional

#1 Input:[11, 2, 5, 9, 10, 3], 12  -> Output:(2,10) or None
#2 Input:[11, 2, 5, 9, 10, 3]  -> Output:(11,9) or None  11+9=2+5+10+3


def get_pair_1(list: List, target: int) -> Tuple:
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] + list[j] == target:
                return (list[i], list[j])
            j += 1
        i += 1
        
        
if __name__ == '__main__':
    list = [11, 2, 5, 9, 10, 3]
    print(get_pair_1(list, 13))
            