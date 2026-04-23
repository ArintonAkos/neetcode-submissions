class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 1:
            return n
        
        s = set()

        for num in nums:
            s.add(num)

        max_len = 1
        for num in nums:
            if num - 1 not in s:
                k = 1
                while num + k in s:
                    k += 1

                max_len = max(max_len, k)

        return max_len
            
