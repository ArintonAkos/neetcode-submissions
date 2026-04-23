# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and not q or q and not p:
            return False

        if not p and not q:
            return True

        isSameLeft  = self.isSameTree(p.left, q.left)
        # Skip Right tree if left is different
        isSame = isSameLeft and self.isSameTree(p.right, q.right)

        return isSame and p.val == q.val