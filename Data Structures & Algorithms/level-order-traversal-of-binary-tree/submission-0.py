# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        q = deque([root])

        while q:
            length = len(q)
            curr = []

            for _ in range(length):
                item = q.popleft()
                curr.append(item.val)

                if item.left:
                    q.append(item.left)
                if item.right:
                    q.append(item.right)

            res.append(curr)

        return res