class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        r, l = 0, 0
        n = len(nums)
        curr_sum = 0
        min_len = float('inf')
        
        while r < n:
            curr_sum += nums[r]

            while l <= r and curr_sum >= target:
                min_len = min(min_len, r - l + 1)
                curr_sum -= nums[l]
                l += 1
            
            r += 1

        return min_len if min_len != float('inf') else 0