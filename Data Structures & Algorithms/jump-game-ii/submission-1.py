class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        i = 0
        curr_end = 0
        farthest = 0
        num_steps = 0

        while i < n - 1:
            farthest = max(farthest, i + nums[i])

            if i >= curr_end:
                curr_end = farthest
                num_steps += 1
            
            i += 1

        return num_steps