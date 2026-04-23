# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        def inorder(node: Optional[TreeNode]) -> None:
            if not node:
                return

            nonlocal res
            # Visit left sub-tree first
            inorder(node.left)
            # Add current item to the list
            res.append(node.val)
            # Visit right sub-tree at last
            inorder(node.right)

        inorder(root)
        return res