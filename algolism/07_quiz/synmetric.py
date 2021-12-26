from typing import List


"""
Synmetric
Input：[(1, 2), (3, 5), (4, 7), (5, 3), (7, 4)]
Output：[(5, 3), (7, 4)]
"""

def symmetric(list: List) -> List:
    
    result = []
    check = []
    for t in list:
        if t in check:
            result.append(t)
        else:
            check.append((t[1], t[0]))
        print(check)
        
    return result


if __name__ == '__main__':
    l = [(1, 2), (3, 5), (4, 7), (5, 3), (7, 4),(2, 1)]
    print(symmetric(l))