from collections import deque
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        def rob(arr: List[int]) -> int:
            rob1, rob2 = 0, 0

            for i in range(len(arr)):
                tmp = max(rob1 + arr[i], rob2)

                rob1 = rob2
                rob2 = tmp

            return max(rob1, rob2)

        return max(rob(nums[:-1]), rob(nums[1:]))