from __future__ import annotations
from typing import Any, Counter

class Node(object):
    def __init__(self, data: Any, next_node=None) -> None:
        self.data = data
        self.next = next_node
        

class LinkedList(object):
    def __init__(self, head=None) -> None:
        self.head = head
        
    def append(self, data: Any) -> None:
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
    
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def insert(self, data: Any) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def print(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
    
    def remove(self, data: Any) -> None:
        current_node = self.head
        
        # リストの最初のデータが削除対象の場合
        if current_node and current_node.data == data:
            self.head = current_node.next
            current_node = None
            return
        
        previos_node = None
        while current_node and current_node.data != data:
            previos_node = current_node
            current_node = current_node.next
                    
        if current_node is None:
            return
        
        previos_node.next = current_node.next
        current_node = None
        
    def revrese_iterative(self) -> None:
        previous_node = None
        cuurent_node = self.head
        
        while cuurent_node:
            next_node = cuurent_node.next
            cuurent_node.next = previous_node
            previous_node = cuurent_node
            cuurent_node = next_node
        
        self.head = previous_node
        
    def reverse_recursive(self) -> None:
        def _reverse_recursive(current_node: Node, previous_node: Node) -> None:
            if not current_node:
                return previous_node
            
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
            return _reverse_recursive(current_node, previous_node)
            
        self.head = _reverse_recursive(self.head, None)
        
    def reverse_even(self) -> None:
        pass            

                
    
if __name__ == '__main__':
    list = LinkedList()
    list.append(1)
    list.append(2)
    list.append(3)
    list.insert(0)
    list.print()
    print('################')
    # list.remove(2)
    # list.print()
    
    list.revrese_iterative()
    list.print()
    print('################')
    list.reverse_recursive()
    list.print() 