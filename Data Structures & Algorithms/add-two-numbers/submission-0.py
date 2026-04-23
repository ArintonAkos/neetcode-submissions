# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2

        dummy = ListNode()
        sum_list = dummy
        has_overflow = False

        while p1 and p2:
            nodes_sum = p1.val + p2.val

            if has_overflow:
                nodes_sum += 1

            has_overflow = nodes_sum >= 10
            nodes_sum = nodes_sum % 10 

            sum_list.next = ListNode(nodes_sum)
            sum_list = sum_list.next
            p1 = p1.next
            p2 = p2.next

        # Different scnearios we need to handle

        # P1 is shorter than P2
        while p2:
            node_val = p2.val + 1 if has_overflow else p2.val
            
            has_overflow = node_val >= 10
            node_val = node_val % 10
            
            sum_list.next = ListNode(node_val)
            sum_list = sum_list.next

            p2 = p2.next

        # P2 is shorter than P1
        while p1:
            node_val = p1.val + 1 if has_overflow else p1.val
            
            has_overflow = node_val >= 10
            node_val = node_val % 10
            
            sum_list.next = ListNode(node_val)
            sum_list = sum_list.next
            
            p1 = p1.next

        # They are the same length, but has an overflow at the end
        # It means we need to insert an additional "1" at the end
        if not p1 and not p2 and has_overflow:
            sum_list.next = ListNode(1)

        return dummy.next