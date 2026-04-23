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
        
        # For one group
        next_group_head = right.next
        right.next = None
        left, right = self.reverseList(left)
        right.next = next_group_head
        prev_group_tail = right
        
        res = left
        counter = 1
        while right.next:
            right = right.next
            left = left.next

            if counter % k == 0:
                # print(f"Left: {left.val} | Right: {right.val}")
                # Do the switching
                next_group_head = right.next
                
                right.next = None
                left, right = self.reverseList(left)
                right.next = next_group_head
                
                prev_group_tail.next = left
                prev_group_tail = right

            counter += 1

        return res


        
