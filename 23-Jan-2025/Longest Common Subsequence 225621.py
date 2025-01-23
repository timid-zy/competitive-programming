# Problem: Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        N, M = len(text1), len(text2)
        dp = [[0] * N for _ in range(M)]
        for j in range(N):
            for i in range(M):
                if i == 0:
                    dp[i][j] = max(dp[i][j-1], 1 if text1[j] == text2[i] else 0)
                    continue
                
                if text2[i] == text1[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        
        return dp[-1][-1]