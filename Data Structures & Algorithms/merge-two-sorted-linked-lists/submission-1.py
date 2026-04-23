# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        x, y = list1, list2
        tail = ListNode()
        res = tail

        while x and y:
            if x.val < y.val:
                tail.next = x
                x = x.next
            else:
                tail.next = y
                y = y.next

            tail = tail.next

        if x:
            tail.next = x
        if y:
            tail.next = y
            
        return res.next