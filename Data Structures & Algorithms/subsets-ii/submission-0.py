class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()

        def backtrack(start_index: int, subset: List[int]):
            res.append(subset.copy())

            for i in range(start_index, n):
                if i > start_index and nums[i] == nums[i - 1]:
                    continue

                # Add current element
                subset.append(nums[i])
                backtrack(i + 1, subset)
                # Pop current element
                subset.pop()

        backtrack(0, [])            
        return res