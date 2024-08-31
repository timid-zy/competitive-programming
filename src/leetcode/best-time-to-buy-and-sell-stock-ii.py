class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_p = prices[0]
        min_p = prices[0]
        profit = 0
        for i in range(len(prices)):
            max_p = max(max_p, prices[i])
            if prices[i] < max_p:
                profit += max_p - min_p
                min_p = prices[i]
                max_p = prices[i]
        
        return profit + max_p - min_p