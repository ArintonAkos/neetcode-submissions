class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        n = len(nums)

        for i, num in enumerate(nums):
            # Positive numbers can't add up to 0
            if num > 0:
                break

            l, r = i + 1, n - 1

            while l < r:
                summ = num + nums[l] + nums[r]

                if summ > 0:
                    r -= 1
                elif summ < 0:
                    l += 1
                else:
                    res.add((num, nums[l], nums[r]))
                    l += 1

        return list(res)