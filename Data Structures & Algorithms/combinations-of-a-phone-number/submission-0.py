class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_letter_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        n = len(digits)
        res = []

        def backtrack(idx: int, partition: list[str]):
            if len(partition) == n:
                res.append("".join(partition))
                return

            for letter in digit_letter_map[digits[idx]]:
                partition.append(letter)
                backtrack(idx + 1, partition)
                partition.pop()

        backtrack(0, [])
        return res