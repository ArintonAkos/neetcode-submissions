# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode], min_val: int, max_val: int):
            if not root: 
                return True

            print(f"Root val: {root.val} | Min_val: {min_val} | Max_val: {max_val}")
            if min_val is not None and root.val <= min_val:
                print("returning false 1")
                return False

            if max_val is not None and root.val >= max_val:
                print("returning false 2")
                return False

            return dfs(root.left, min_val, root.val) and dfs(root.right, root.val, max_val)

        return dfs(root, None, None)