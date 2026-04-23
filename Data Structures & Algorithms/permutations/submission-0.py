class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        visited = [False] * n
        res = []

        def permutate(word_len: int, curr: List[int]):
            if word_len == n:
                res.append(curr.copy())

            for i in range(n):
                if not visited[i]:
                    visited[i] = True
                    curr.append(nums[i])
                    permutate(word_len + 1, curr)
                    curr.pop()
                    visited[i] = False

            
        
        permutate(0, [])
        return res