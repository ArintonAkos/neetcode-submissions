class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        p = []
        match     = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        for c in s:
            if c in match:
                p.append(c)
            elif p:
                c_pair = p.pop()

                if match[c_pair] != c:
                    return False
            else:
                return False
        
        return len(p) == 0 