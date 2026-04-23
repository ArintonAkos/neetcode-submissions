from collections import deque
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) < 3:
            return max(nums)

        # [5, 1, 2, 10, 6,   2, 7, 9, 3, 1]
        # [5, 1, 7, 12, 13, 14, 20, 23]

        # nums=[2,9,1,1,6]
        # [2,9,3,10,9] -> Incorrect
        # [2,9,3,10,15]
        prev = [nums[0]]
        n = len(nums)
        for i in range(2, n):
            prev_max, prev_min = max(prev), min(prev)
            nums[i] = prev_max + nums[i]

            if len(prev) < 2:
                prev.append(nums[i - 1])
            else:
                prev[0], prev[1] = prev_max, max(nums[i - 1], prev_min)
            

        # No error even on 1 length array, since nums[-1] is pointing to nums' last element (which is nums[0])
        return max(nums[n - 1], nums[n - 2])