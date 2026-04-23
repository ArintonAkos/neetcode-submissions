from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        m, n = len(grid), len(grid[0])
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q:
            i, j = q.popleft()

            for x, y in directions:
                new_i, new_j = i + x, j + y

                if new_i < 0 or new_i >= m or new_j < 0 or new_j >= n:
                    continue

                if grid[new_i][new_j] != INF:
                    continue

                grid[new_i][new_j] = grid[i][j] + 1
                q.append((new_i, new_j))

