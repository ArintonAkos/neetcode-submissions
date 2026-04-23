class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res1, res2 = float('inf'), float('inf')
        count1, count2 = 0, 0

        for num in nums:
            if num == res1:
                count1 += 1
            elif num == res2:
                count2 += 1
            elif count1 == 0:
                res1 = num
                count1 = 1
            elif count2 == 0:
                res2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        res = []
        limit = len(nums) // 3

        r1_real_count, r2_real_count = 0, 0

        for num in nums:
            if num == res1:
                r1_real_count += 1
            elif num == res2:
                r2_real_count += 1
        
        if r1_real_count > limit:
            res.append(res1)

        if r2_real_count > limit:
            res.append(res2)

        return res
