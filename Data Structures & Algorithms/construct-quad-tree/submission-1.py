"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n: int, r: int, c: int) -> 'Node':
            if n == 1:
                return Node(grid[r][c], True)

            n //= 2
            topLeft     = dfs(n, r, c)
            topRight    = dfs(n, r, c + n)
            bottomLeft  = dfs(n, r + n, c)
            bottomRight = dfs(n, r + n, c + n)

            if (topLeft.isLeaf and topRight.isLeaf and
                bottomLeft.isLeaf and bottomRight.isLeaf and
                topLeft.val == topRight.val == bottomLeft.val == bottomRight.val):
                return Node(topLeft.val, True)
            
            return Node(1, False, topLeft, topRight, bottomLeft, bottomRight)

        return dfs(len(grid), 0, 0)
