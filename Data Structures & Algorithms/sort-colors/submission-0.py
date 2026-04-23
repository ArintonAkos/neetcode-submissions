class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0] * 3

        for num in nums:
            counts[num] += 1

        i = 0
        j = 0

        while j < 3 and i < len(nums):
            if counts[j] == 0:
                j += 1
            else:
                nums[i] = j
                counts[j] -= 1
                i += 1