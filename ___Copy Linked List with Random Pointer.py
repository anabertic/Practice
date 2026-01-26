"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        newList = None
        current = head
        storage = {}
        if not head:
            return None
        while current:
            node = Node(current.val, None, None)
            storage[current] = node 
            current = current.next
        current = head
        for i in storage.keys():
            storage[i].next = storage.get(i.next)
            storage[i].random = storage.get(i.random)
        return storage[head]


        
    
