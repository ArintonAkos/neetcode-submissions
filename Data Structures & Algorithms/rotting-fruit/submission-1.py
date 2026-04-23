from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        m, n = len(grid), len(grid[0])
        fresh_count = 0
        time = 0

        for i in range(m):
            for j in range(n):
                # If fresh
                if grid[i][j] == 1:
                    fresh_count += 1
                # If rotten
                if grid[i][j] == 2:
                    q.append((i, j))

        if fresh_count == 0:
            return 0

        while q and fresh_count > 0:
            for _ in range(len(q)):
                i, j = q.popleft()
                
                for x, y in ([-1, 0], [0, -1], [1, 0], [0, 1]):
                    new_i, new_j = i + x, j + y

                    if new_i < 0 or new_i >= m or new_j < 0 or new_j >= n:
                        continue

                    if grid[new_i][new_j] == 1:
                        grid[new_i][new_j] = 2
                        q.append((new_i, new_j))
                        fresh_count -= 1
            
            time += 1

        return time if fresh_count == 0 else -1
        