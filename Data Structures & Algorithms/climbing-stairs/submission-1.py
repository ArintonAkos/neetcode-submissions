from functools import cache 

class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dp(i: int):
            if i == 0:
                return 1
            if i < 0:
                return 0

            return dp(i - 1) + dp(i - 2)

        return dp(n)