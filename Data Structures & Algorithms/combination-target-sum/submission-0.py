class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        self.res = []

        def backtrack(combination: List[int], sum: int):
            if sum > target:
                return

            if sum == target:
                self.res.append(combination.copy())

            for i in range(n):
                if not combination or (combination and combination[-1] <= nums[i]):
                    combination.append(nums[i])
                    backtrack(combination, sum + nums[i])
                    combination.pop()
            
        backtrack([], 0)
        return self.res