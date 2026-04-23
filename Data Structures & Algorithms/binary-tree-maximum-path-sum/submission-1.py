# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.global_max = float('-inf')

        def maxPath(root: Optional[TreeNode]):
            if not root:
                return 0

            left_max = max(0, maxPath(root.left))
            right_max = max(0, maxPath(root.right))

            self.global_max = max(self.global_max, left_max + root.val + right_max)

            return root.val + max(left_max, right_max)

        maxPath(root)
        return self.global_max