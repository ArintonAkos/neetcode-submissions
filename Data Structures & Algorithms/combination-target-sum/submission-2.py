class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()

        def backtrack(start_index: int, current_sum: int, combination: List[int]):
            if current_sum == target:
                res.append(combination.copy())
                return
            
            if current_sum > target:
                return

            for i in range(start_index, n):
                if current_sum + nums[i] > target:
                    continue
                
                combination.append(nums[i])
                backtrack(i, current_sum + nums[i], combination)
                combination.pop()
            
        backtrack(0, 0, [])
        return res