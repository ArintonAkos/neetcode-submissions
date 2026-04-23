class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(idx: int, length: int, sub_res: List[int]):
            if length == k:
                res.append(sub_res.copy())
                return

            for i in range(idx, n + 1):
                sub_res.append(i)
                backtrack(i + 1, length + 1, sub_res)
                sub_res.pop()

        backtrack(1, 0, [])
        return res
            