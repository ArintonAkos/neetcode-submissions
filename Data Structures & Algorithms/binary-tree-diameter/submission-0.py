# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_d = 0

        def diameter(root: Optional[TreeNode]):
            if not root:
                return 0

            left_h = diameter(root.left)
            right_h = diameter(root.right)

            curr_d = left_h + right_h

            self.max_d = max(self.max_d, curr_d)

            return 1 + max(left_h, right_h)

        diameter(root)
        return self.max_d