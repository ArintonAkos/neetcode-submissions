# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None

        def split_middle(head: Optional[ListNode]) -> Optional[ListNode]:
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
        
            res = slow.next
            slow.next = None

            return res

        def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
            if not head:
                return None

            curr = head
            prev = None

            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            return prev

        def merge_lists(head1: Optional[ListNode], head2: Optional[ListNode]):
            dummy = ListNode()
            res = dummy

            k = 0

            while head1 and head2:
                if k % 2 == 0:
                    dummy.next = head1
                    head1 = head1.next
                else:
                    dummy.next = head2
                    head2 = head2.next
                
                dummy = dummy.next
                k += 1

            
            if head1:
                dummy.next = head1
            if head2:
                dummy.next = head2
            
            return res.next

        head2 = split_middle(head)
        head2 = reverse_list(head2)

        merge_lists(head, head2)

        