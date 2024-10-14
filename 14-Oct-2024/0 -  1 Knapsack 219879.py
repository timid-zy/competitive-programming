# Problem: 0 -  1 Knapsack - https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val):
        dp = [[0] * (W + 1) for _ in range(len(wt) + 1)]
        for i in range(len(dp)-2, -1, -1):
            for curw in range(len(dp[0])):
                dp[i][curw] = dp[i+1][curw]
                if curw + wt[i] <= W:
                    dp[i][curw] = max(dp[i][curw], dp[i+1][curw + wt[i]] + val[i])
        
        return dp[0][0]