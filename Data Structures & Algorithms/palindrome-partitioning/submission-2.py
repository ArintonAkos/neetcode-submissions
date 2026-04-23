class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)

        def backtrack(start_index: int, partition: List[str]):
            if start_index == n:
                res.append(partition.copy())

            for i in range(start_index, n):
                substring = s[start_index : i + 1]

                if substring == substring[::-1]:
                    partition.append(substring)
                    backtrack(i + 1, partition)
                    partition.pop()

        backtrack(0, [])
        return res