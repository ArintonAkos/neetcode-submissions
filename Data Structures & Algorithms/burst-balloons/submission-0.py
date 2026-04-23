class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        cache = {}
        nums = [1] + nums + [1]
        n = len(nums)

        def dfs(left: int, right: int) -> int:
            if left + 1 == right:
                return 0

            if (left, right) in cache:
                return cache[(left, right)]

            res = 0
            for i in range(left + 1, right):
                left_part  = dfs(left, i)
                right_part = dfs(i, right)
                curr_part  = nums[i] * nums[left] * nums[right]

                curr = left_part + curr_part + right_part
                res = max(res, curr)

            cache[(left, right)] = res
            return res

        return dfs(0, n - 1)