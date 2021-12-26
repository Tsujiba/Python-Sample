from collections import Counter
from typing import List
"""
Input:X:[1,2,3,4,4,5,5,8,10], Y:[4,5,5,5,6,7,8,8,10]
->X:[1,2,3,4,4,10], Y:[5,5,5,6,7,8,8,10]
"""

def min_count_remove(x: List[int], y: List[int]) -> None:
    counter_x = Counter(x)
    counter_y = Counter(y)
    
    # print(counter_x)
    # print(counter_y)
    
    for x_key, x_value in counter_x.items():
        y_value = counter_y.get(x_key)
        if y_value:
            if x_value < y_value:
                x[:] = [i for i in x if i != x_key]
            if x_value > y_value:
                y[:] = [i for i in y if i != x_key]


if __name__ == '__main__':
    x = [1,2,3,4,4,5,5,8,10]
    y = [4,5,5,5,6,7,8,8,10]
    print('x=', x)
    print('y=', y)

    min_count_remove(x, y)
    
    print('x=', x)
    print('y=', y)

