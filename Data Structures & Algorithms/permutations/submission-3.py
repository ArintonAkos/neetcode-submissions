class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        visited = [False] * n
        res = []

        def permutate(curr: List[int]):
            if len(curr) == n:
                res.append(curr.copy())

            for i in range(n):
                if not visited[i]:
                    visited[i] = True
                    curr.append(nums[i])
                    permutate(curr)
                    curr.pop()
                    visited[i] = False

        permutate([])
        return res