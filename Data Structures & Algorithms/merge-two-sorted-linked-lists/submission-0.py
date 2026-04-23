# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        x, y = list1, list2
        head = ListNode(float('-inf'))
        res = head

        while x and y:
            if x.val < y.val:
                head.next = ListNode(x.val)
                x = x.next
            else:
                head.next = ListNode(y.val)
                y = y.next

            head = head.next

        while x:
            head.next = ListNode(x.val)
            head = head.next
            x = x.next
            
        while y:
            head.next = ListNode(y.val)
            head = head.next
            y = y.next
            
        return res.next