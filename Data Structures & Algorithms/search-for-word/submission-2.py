class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dir_x = [1, 0, -1, 0]
        dir_y = [0, -1, 0, 1]
        
        m, n = len(board), len(board[0])

        def backtrack(i: int, j: int, idx: int) -> bool:
            if len(word) == idx:
                return True

            for x, y in zip(dir_x, dir_y):
                new_i, new_j = i + x, j + y
                if new_i < 0 or new_i >= m or new_j < 0 or new_j >= n:
                    continue
                
                if board[new_i][new_j] == word[idx]:
                    board[new_i][new_j] = '#'
                    res = backtrack(new_i, new_j, idx + 1)
                    board[new_i][new_j] = word[idx]
                    # If found solution, immediately return
                    if res: return True

            return False
            
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    board[i][j] = '#'
                    res = backtrack(i, j, 1)
                    board[i][j] = word[0]
                    if res: return True
        
        return False