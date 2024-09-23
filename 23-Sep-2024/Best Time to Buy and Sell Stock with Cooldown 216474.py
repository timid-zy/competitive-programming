# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(i, f):
            if i >= len(prices):
                return 0
            
            if f:
                return max(
                    dp(i+1, f),
                    dp(i+2, not f) + prices[i]
                )

            return max(
                dp(i+1, f),
                dp(i+1, not f) - prices[i]
            )

        return dp(0, False)
        
