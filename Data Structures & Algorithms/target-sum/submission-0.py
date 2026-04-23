class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        
        if (total_sum + target) % 2 == 1:
            return 0

        if abs(target) > total_sum:
            return 0

        sum_p = (target + total_sum) // 2
        dp = [0] * (sum_p + 1)
        dp[0] = 1

        # print(f"Dp is: {dp} | sum_p :  {sum_p}")

        for num in nums:
            for j in range(sum_p, num - 1, -1):
                dp[j] += dp[j - num]

         #print(f"Dp is: {dp}")
        return dp[sum_p]