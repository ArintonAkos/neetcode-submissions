class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # No. rows
        self.n = len(matrix)
        # No. cols
        self.m = len(matrix[0])
        
        def to2d(x: int) -> tuple[int, int]:
            i = x // self.m
            j = x  % self.m

            # print(f"Converting to 2d: x: {x}, i: {i}, j: {j}")
            return i, j

        def binary2d(left: int, right: int) -> bool:
            if left > right:
                return False

            mid = (left + right) // 2
            i, j = to2d(mid)

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                return binary2d(mid + 1, right)
            else:
                return binary2d(left, mid - 1)

        return binary2d(0, self.n * self.m - 1)