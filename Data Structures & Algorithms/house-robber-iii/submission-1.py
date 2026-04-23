# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def maxSum(root: Optional[TreeNode]) -> int:
            if not root:
                # Sum [with, without]
                return [0, 0]

            left  = maxSum(root.left)
            right = maxSum(root.right)

            # Without left + without right + with current
            with_node = left[1] + right[1] + root.val
            # Max of with or without left + max of with or without right 
            without_node = max(left) + max(right)
        
            return [with_node, without_node]

        return max(maxSum(root))