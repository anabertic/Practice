# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        length = 0
        node = head
        while node:
            node = node.next
            length += 1
        toRemove = length - n
        node = dummy
        for i in range(toRemove):
            node = node.next
        # rewire
        node.next = node.next.next
        return dummy.next

        
