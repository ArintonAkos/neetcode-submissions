class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        cur_stack = []
        num = 0
        cur = ""

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "[":
                num_stack.append(num)
                cur_stack.append(cur)
                cur = ""
                num = 0
            elif c == "]":
                tmp = cur
                cur = cur_stack.pop()
                count = num_stack.pop()
                cur += tmp * count
            else:
                cur += c

        return cur