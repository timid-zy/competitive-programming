# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        set_ = set(days)
        dp = [0] * 366
        for i in range(1, len(dp)):
            if i not in set_:
                dp[i] = dp[i-1]
                continue
            
            dp[i] = dp[i-1] + costs[0]
            if i >= 7:
                dp[i] = min(dp[i], dp[i-7] + costs[1])
            else:
                dp[i] = min(dp[i], costs[1])
            
            if i >= 30:
                dp[i] = min(dp[i], dp[i-30] + costs[2])
            else:
                dp[i] = min(dp[i], costs[2])
        
        return dp[-1]