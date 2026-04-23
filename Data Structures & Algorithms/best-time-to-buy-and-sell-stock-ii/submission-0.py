from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        @cache
        def dfs(curr_day: int, has_stock: bool) -> int:
            nonlocal n
            if curr_day >= n:
                return 0

            curr_price = prices[curr_day]
            if has_stock:
                # If we have stock, we can either keep it or sell it
                # Either way, we need the max
                sell_strategy = dfs(curr_day + 1, False) + curr_price
                keep_strategy = dfs(curr_day + 1, has_stock)

                return max(sell_strategy, keep_strategy)
            else:
                # If we don't have stock we can either buy or keep waiting
                buy_strategy = dfs(curr_day + 1, True) - curr_price
                wait_strategy = dfs(curr_day + 1, has_stock)

                return max(buy_strategy, wait_strategy)

        return dfs(0, False)