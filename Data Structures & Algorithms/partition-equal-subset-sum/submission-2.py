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
                if existing_sum + num > target:
                    continue
                if existing_sum + num == target:
                    return True
                tmp_set.add(existing_sum + num)

            dp.update(tmp_set)

        return target in dp
