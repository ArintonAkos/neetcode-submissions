# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val:
            p, q = q, p

        while root:
            # Root is lower
            if root.val == p.val:
                return p
            elif root.val == q.val:
                return q
            else:
                if root.val < p.val < q.val:
                    return self.lowestCommonAncestor(root.right, p, q)
                elif p.val < root.val < q.val:
                    return root
                else:
                    return self.lowestCommonAncestor(root.left, p, q)