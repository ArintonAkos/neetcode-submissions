class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]

        # [ 3, 2, 4, 6]
        # [ 1, 3, 6, 24]
        # [48,24, 6, 1]
        # expected:
        # [48,72,36,24]
        right_product = nums[n-1]
        for i in range(n - 2, -1, -1):
            # print(i)
            res[i] = res[i] * right_product
            right_product *= nums[i]

        return res