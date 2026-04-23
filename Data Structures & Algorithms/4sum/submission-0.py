class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        l, r = 0, n - 1
        res = []

        while l < r:
            s = nums[l] + nums[r]
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else:
                res.append([nums[l], nums[r]])

                while l < r and nums[l] == nums[l + 1]:
                    l += 1

                while l < r and nums[r] == nums[r - 1]:
                    r -= 1

                l += 1
                r -= 1
                
        return res

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.kSum(nums, target, 4)
    
    def kSum(self, nums: List[int], target: int, k: int) -> List[List[int]]:
        res = []

        if not nums:
            return []

        average_val = target // k
        if nums[0] > average_val or nums[-1] < average_val:
            return res

        if k == 2:
            return self.twoSum(nums, target)

        n = len(nums)
        for i in range(n):
            if i == 0 or nums[i - 1] != nums[i]:
                for subset in self.kSum(nums[i + 1:], target - nums[i], k - 1):
                    res.append([nums[i]] + subset)

        return res
