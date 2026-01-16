# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNone = newList = ListNode(0,None)
        while list1 and list2:
            if list1.val > list2.val:
                newList.next = list2
                list2 = list2.next
            else:
                newList.next = list1
                list1 = list1.next
            newList = newList.next
        newList.next = list1 or list2
        return dummyNone.next

        
