# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSame(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True

        if not root1 or not root2:
            return False

        if root1.val != root2.val:
            return False

        return self.isSame(root1.left,  root2.left) and self.isSame(root1.right, root2.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: 
            return False

        # If node vals are the same, check subtree-s
        if root.val == subRoot.val:
            res = self.isSame(root, subRoot)
            # If sub-trees are same, return True
            if res:
                return True

        # Otherwise check left subtree or right subtree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
