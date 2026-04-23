class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        atl_visited = set()
        pac_visited = set()

        def dfs(i: int, j: int, v: set, prevH: int):
            if i < 0 or i >= m or j < 0 or j >= n:
                return

            if (i, j) in v:
                return

            if prevH > heights[i][j]:
                return

            v.add((i ,j))

            for x, y in ([-1, 0], [0, -1], [1, 0], [0, 1]):
                new_i, new_j = i + x, j + y
                dfs(new_i, new_j, v, heights[i][j])
            
        # rows
        for i in range(m):
            # First column on every row
            dfs(i, 0,     pac_visited, 0)
            # Last column on every row
            dfs(i, n - 1, atl_visited, 0)

        for i in range(n):
            # Every column on first row
            dfs(0,     i, pac_visited, 0)
            # Every column on last row
            dfs(m - 1, i, atl_visited, 0)

        res = []
        for v in atl_visited:
            if v in pac_visited:
                res.append(v)

        return res