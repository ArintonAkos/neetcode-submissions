class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = count = 0

        for num in nums:
            if num == res:
                count += 1
            elif count > 0:
                count -= 1
            else:
                res = num
                count = 1

        return res
