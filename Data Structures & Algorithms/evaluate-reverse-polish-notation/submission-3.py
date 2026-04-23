import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda x, y: int(x / y),
        }

        for token in tokens:
            if token in ops:
                right, left = stack.pop(), stack.pop()
                stack.append(ops[token](left, right))
            else:
                num = int(token)
                stack.append(num)

        return stack.pop()
