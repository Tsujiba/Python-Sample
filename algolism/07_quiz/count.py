"""
Input：'This is a pen. This is an apple. Applepen'
Output：('p', 6)
"""

from typing import Tuple


def count_char(sentence: str) -> Tuple:
    dic = {}
    for char in sentence:
        if char.isspace():
            continue
        
        lc = char.lower()
        if lc in dic.keys():
            dic[lc] += 1
        else:
            dic[lc] = 1
            
    max_kv = max(dic.items(), key=lambda x: x[1])
    return max_kv        


if __name__ == '__main__':
    st = 'This is a pen. This is an apple. Applepen.'
    print(count_char(st))