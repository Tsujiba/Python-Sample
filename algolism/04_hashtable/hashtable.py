import hashlib
from typing import Any

class HashTable(object):
    
    def __init__(self, size: int) -> None:
        self.size = size
        self.table = [[] for _ in range(self.size)]
        
    def hash(self, key) -> int:
        return int(hashlib.md5(key.encode()).hexdigest(), base=16) % 10
    
    def add(self, key, value) -> None:
        index = self.hash(key)
        
        for data in self.table[index]:
            if data[0] == key:
                data[1] = value
                break
        else:
            self.table[index].append([key, value]) 
            
    def get(self, key) -> Any:
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                return data[1]
            
        
    def print(self) -> None:
        for index in range(self.size):
            print(index, end=' ')
            for data in self.table[index]:
                print('-->', end=' ')
                print(data, end=' ')
            print()
    
    def __setitem__(self, key, value) -> None:
        self.add(key, value)
        
    def __getitem__(self, key) -> Any:
        return self.get(key)
    


if __name__ == '__main__':
    ht = HashTable(10)
    # print(ht.table)
    # print(ht.hash('pc'))
    ht.add('pc', 'windows')
    ht.add('sns', 'instagram')
    ht.add('hard', 'ha8000v')
    ht.add('car', 'susuki')
    ht['name'] = 'Tsujiba'
    # print(ht.table)
    ht.print()
    print('###################')
    # print(ht.get('car'))
    print(ht['name'])
    

