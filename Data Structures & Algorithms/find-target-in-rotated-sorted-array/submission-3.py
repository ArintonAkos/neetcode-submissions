class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(left: int, right: int, val: int):
            if left > right:
                return -1

            m = (left + right) // 2

            if nums[m] == target:
                return m

            # Left side ordered
            if nums[left] <= nums[m]:
                # If val is in this range, right should have upper bound as m
                if nums[left] <= val < nums[m]:
                    right = m - 1
                else:
                    left = m + 1
            else:
                if nums[m] < val <= nums[right]:
                    left = m + 1
                else: 
                    right = m - 1

            return bs(left, right, val)
            

        return bs(0, len(nums) - 1, target)