class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dir_x = [1, 0, -1, 0]
        dir_y = [0, -1, 0, 1]
        
        m, n = len(board), len(board[0])

        def backtrack(i: int, j: int, idx: int) -> bool:
            if len(word) == idx:
                return True
            
            if i < 0 or i >= m or j < 0 or j >= n:
                return False

            if board[i][j] != word[idx]:
                return False 
            
            res = False
            board[i][j] = '#'

            for x, y in zip(dir_x, dir_y):
                new_i, new_j = i + x, j + y
                if backtrack(new_i, new_j, idx + 1):
                    res = True
                    break

            board[i][j] = word[idx]
            return res
            
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        
        return False