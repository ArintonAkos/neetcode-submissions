class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        self.res = []

        def backtrack(left: int, curr: List[int]):
            if left > n:
                return

            # print(f"Curr is: {curr} | Left: {left}")
            self.res.append(curr.copy())
            for i in range(left, n):
                curr.append(nums[i])
                # print(f"Nums[i]: {nums[i]}")
                backtrack(i + 1, curr)
                curr.pop()

        backtrack(0, [])

        return self.res

        

