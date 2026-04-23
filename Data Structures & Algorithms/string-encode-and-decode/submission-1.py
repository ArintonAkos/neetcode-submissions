class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for string in strs:
            res.append(f"{len(string)}#{string}")
        
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        def parse_num(s_num: str) -> int:
            return int(s_num)

        k = 0
        n = len(s)

        res = []
        s_num = ""

        while k < n:
            if s[k] != "#":
                s_num += s[k]
                k += 1
            else:
                # Skip '#'
                k += 1
                # Check the length of the message
                to_skip = parse_num(s_num)
                # Add message to result
                res.append(s[k:k+to_skip])
                # Set back msg len counter
                s_num = ""
                # Jump to end of message
                k += to_skip

        return res