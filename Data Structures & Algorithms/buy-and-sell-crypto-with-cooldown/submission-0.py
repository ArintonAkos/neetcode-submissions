class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        n = len(prices)

        def dfs(i: int, has_stock: bool) -> int:
            if i >= n:
                return 0
            
            if (i, has_stock) in dp:
                return dp[(i, has_stock)]

            cooldown = dfs(i + 1, has_stock)
            # If we have stock we can either wait or sell
            if has_stock:
                sell = dfs(i + 2, False) + prices[i]

                return max(sell, cooldown)
            # If we don't have stock, we have to either buy or wait
            else:
                buy = dfs(i + 1, True) - prices[i]

                return max(buy, cooldown)
            
        return dfs(0, False)