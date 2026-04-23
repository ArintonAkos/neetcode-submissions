class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        p = []
        close_to_open = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        for c in s:
            if c not in close_to_open:
                p.append(c)
            else:
                if p and p[-1] == close_to_open[c]:
                    p.pop()
                else:
                    return False
        
        return not p