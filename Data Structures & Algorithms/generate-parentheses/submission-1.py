class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def parantheses(p_open: int, p_closed: int, seq: str):
            if len(seq) == 2 * n:
                res.append(seq)

            if p_open < n:
                parantheses(p_open + 1, p_closed, seq + "(")

            if p_closed < n and p_open > p_closed:
                parantheses(p_open, p_closed + 1, seq + ")")

        parantheses(0, 0, "")
        return res