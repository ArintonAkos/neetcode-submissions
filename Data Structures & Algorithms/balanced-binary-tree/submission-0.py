# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def child(root: Optional[TreeNode], h: int) -> int:
            if not root:
                return h

            left_child = child(root.left, h + 1)
            right_child = child(root.right, h + 1)

            if abs(left_child - right_child) > 1:
                raise Error('test')
            
            return max(left_child, right_child)
        
        try:
            child(root, 0)
            return True
        except:
            return False
        

        