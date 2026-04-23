class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # No single pass
        res = float('-inf')
        curr_min, curr_max = 1, 1

        for num in nums:
            tmp = curr_max * num

            # The current maximum is either:
            #   - the current number
            #   - the current number multiplied with the previous maximum
            #   - the current number multiplied with the previous minimum (if current number is negative for example)
            curr_max = max(num, tmp, curr_min * num)
            curr_min = min(num, tmp, curr_min * num)

            # We don't have to reset curr_max to 1 since, if it is negative and we find
            # a new item that would start a new sequence, curr_max will automatically update to that
            # since we add "n" to the max(...) method. Same goes for the min(...)

            # Since we already know that curr_max > curr_min, no need to add it here
            res =  max(res, curr_max)
        
        return res