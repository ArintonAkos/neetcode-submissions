# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        left, right = head, head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            right = right.next
            prev = left
            left = left.next

        # When end reached
        if not prev:
            return left.next
            
        prev.next = left.next
        return head