# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Return [list_head, list_tail]
    def reverseList(self, head: Optional[ListNode]):
        curr = head
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev, head
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        left, right = head, head

        for i in range(k - 1):
            if right.next is None:
                return head
            right = right.next
        
        res = right
        prev_group_tail = None
        
        counter = 0
        while right:
            if counter % k == 0:
                # Do the switching
                next_group_head = right.next
                
                right.next = None
                left, right = self.reverseList(left)
                right.next = next_group_head
                
                if prev_group_tail:
                    prev_group_tail.next = left
                prev_group_tail = right

            right = right.next
            left = left.next

            counter += 1

        return res


        
