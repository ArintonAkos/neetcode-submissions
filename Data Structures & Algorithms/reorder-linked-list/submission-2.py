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

        def zip_merge(head1: Optional[ListNode], head2: Optional[ListNode]):
            # [2,  4, 6]
            # [10, 8]

            # head2 is always shorter or equal to head1
            while head2:
                tmp1, tmp2 = head1.next, head2.next
                # Connect 2 to 10
                head1.next = head2
                # Connect 10 to 4
                head2.next = tmp1

                # Set the new head to 4
                head1 = tmp1
                # Set the new head to 8
                head2 = tmp2

        head2 = split_middle(head)
        head2 = reverse_list(head2)

        zip_merge(head, head2)

        