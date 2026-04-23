class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False

        target = total_sum // 2
        dp = {0}

        for num in nums:
            tmp_set = set()

            for existing_sum in dp:
                tmp_set.add(existing_sum + num)

            for tmp in tmp_set:
                dp.add(tmp)

        return target in dp
