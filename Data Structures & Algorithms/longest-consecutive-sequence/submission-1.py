class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 1:
            return n
        
        num_set = set(nums)

        max_len = 1
        for num in nums:
            if num - 1 not in num_set:
                k = 1
                while num + k in num_set:
                    k += 1

                max_len = max(max_len, k)

        return max_len
            
