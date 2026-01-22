# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find half
        first, second = head, head.next
        while second and second.next:
            first = first.next
            second = second.next.next
        current = first.next
        first.next, prev = None, None # split the list
        # reverse second half
        while current:
            nextt = current.next
            current.next = prev
            prev = current
            current = nextt
        list_2 = prev
        list_1 = head
        while list_1 and list_2:
            # remember
            next_1 = list_1.next
            next_2 = list_2.next
            # rewire
            list_1.next = list_2
            list_2.next = next_1
            # advance
            list_1 = next_1
            list_2 = next_2

        
