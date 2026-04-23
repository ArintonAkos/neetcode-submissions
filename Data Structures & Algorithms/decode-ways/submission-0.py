class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0

        if s[0] == '0':
            return 0

        n = len(s)
        # Storing how many ways to decode until "i"-th letter
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            num = int(s[i - 1])
            if 1 <= num <= 9:
                dp[i] += dp[i - 1]
            
            num = int(s[i - 2 : i])
            if 10 <= num <= 26:
                dp[i] += dp[i - 2]

        return dp[n]
        # 122030 -> invalid : 30 cannot be decoded
        # 622621
        # 1, 2, 12, 2, 22, 6, 26, 1, 21
        # dp = [1, ]

        # 66666
        # 6,6,6,6,6
        # dp = [1,1,1,1,1]

        # We need to multiply the dp elements ? 