from collections import deque
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        rob1, rob2 = 0, 0
        n = len(nums)

        for i in range(n):
            tmp = max(rob1 + nums[i], rob2)

            rob1 = rob2
            rob2 = tmp

        # No error even on 1 length array, since nums[-1] is pointing to nums' last element (which is nums[0])
        return max(rob1, rob2)