class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p = {}

        for i, num in enumerate(nums):
            p[num] = i

        for i, num in enumerate(nums):
            if p.get(target - num) and i != p[target - num]:
                return [i, p[target - num]]