# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        i = 1
        curr = head 
        prev = None

        while i < left:
            prev = curr
            curr = curr.next
            i += 1

        def reverse(head: Optional[ListNode], prev: Optional[ListNode]):
            curr = head
            i = 0

            # Reverse nodes
            while curr and i <= right - left:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                
                i += 1

            head.next = curr
            return prev

        reverse_head = reverse(curr, prev)

        if not prev:
            head = reverse_head
        else:
            prev.next = reverse_head

        return head










