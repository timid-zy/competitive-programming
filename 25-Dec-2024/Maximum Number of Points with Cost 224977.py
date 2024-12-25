# Problem: Maximum Number of Points with Cost - https://leetcode.com/problems/maximum-number-of-points-with-cost/

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        N, M = len(points), len(points[0])
        dp = [[0] * M for _ in range(N)]
        dp[0] = points[0]
        for i in range(1, N):
            mx = -1
            for j in range(M):
                mx = max(mx-1, dp[i-1][j])
                dp[i][j] = max(dp[i][j], mx + points[i][j])
            
            mx = -1
            for j in range(M-1, -1, -1):
                mx = max(mx-1, dp[i-1][j])
                dp[i][j] = max(dp[i][j], mx + points[i][j])
        
        return max(dp[-1])