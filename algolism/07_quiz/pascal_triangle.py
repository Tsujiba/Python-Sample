from typing import List

def generate_pascal_triangle(depth: int) -> List[List[int]]:
    data = [[1] * (i + 1) for i in range(depth)]
    
    for l in data: 
        if len(l) < 3:
            tmp = l
            continue       
        for i in range(1, len(l)-1):
            l[i] = tmp[i-1] + tmp[i]
        tmp = l 
        
    return data
    
if __name__ == '__main__':
    print(generate_pascal_triangle(7))