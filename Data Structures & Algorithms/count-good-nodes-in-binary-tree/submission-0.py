# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root: Optional[TreeNode], max_val: int) -> int:
            if not root:
                return 0

            res = 0
            
            if max_val <= root.val:
                res += 1

            max_val = max(max_val, root.val)
            res += dfs(root.left,  max_val)
            res += dfs(root.right, max_val)

            return res


        return dfs(root, float('-inf'))

            