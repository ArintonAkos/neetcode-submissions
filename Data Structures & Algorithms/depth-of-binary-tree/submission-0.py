# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(root: Optional[TreeNode], d: int) -> int:
            if not root:
                return d

            left_depth = depth(root.left, d + 1)
            right_depth = depth(root.right, d + 1)

            return max(left_depth, right_depth)

        return depth(root, 0)
    