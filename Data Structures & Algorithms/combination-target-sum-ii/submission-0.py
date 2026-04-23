class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        candidates.sort()

        def backtrack(start_index: int, current_sum: int, combination: List[int]):
            if current_sum == target:
                res.append(combination.copy())
                return
            
            if current_sum > target:
                return

            for i in range(start_index, n):
                # Only allow one from the same type per stack
                if candidates[i] == candidates[i - 1] and i > start_index:
                    continue
                
                combination.append(candidates[i])
                backtrack(i + 1, current_sum + candidates[i], combination)
                combination.pop()
            
        backtrack(0, 0, [])
        return res