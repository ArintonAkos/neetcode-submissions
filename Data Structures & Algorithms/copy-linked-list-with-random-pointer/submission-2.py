"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        curr = head

        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next

        curr = head
        while curr:
            if curr.random is not None:
                curr.next.random = curr.random.next
            
            curr = curr.next.next

        curr = head
        dummy = Node(0)
        copy_curr = dummy

        while curr:
            copy_node = curr.next
            
            # Update the output list to point to the current item
            copy_curr.next = copy_node
            # Set the output list pointer to the current item
            copy_curr = copy_node

            # Skip the additional list
            curr.next = copy_node.next
            # Go to the next item in the original list
            curr = curr.next

        return dummy.next

        
        