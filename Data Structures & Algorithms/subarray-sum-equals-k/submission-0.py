class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        
        prefix_map = defaultdict(int)
        prefix_map[0] = 1

        for num in nums:
            current_sum += num
            diff = current_sum - k

            if diff in prefix_map:
                count += prefix_map[diff]

            prefix_map[current_sum] += 1

        return count