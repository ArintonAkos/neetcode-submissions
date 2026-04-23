class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        # [1...amount]
        # [1, 5, 10], a=12
        # [1...12]
        # 1 > 
        for i in range(1, amount + 1):
            for coin in coins:
                if coin > i:
                    break
                
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1
        # 12
        # [1, 6, 9]
        # fewest amount: 6 + 6 -> 2 coins
        # with greedy from the end: 9 + 1 + 1 + 1 + 1 -> 5 coins

        # we need a dp array, storing amount X can be paid with at least X number of coins
        # so we need dp * 10001 ?
        # and once we have this we go trough the coins and check the least? 
        # i mean for coin in coins:
        # res = min(dp[coin] + dp[amount - coin], res)