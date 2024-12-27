# Problem: Best Sightseeing Pair - https://leetcode.com/problems/best-sightseeing-pair/

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        mx = float('-inf')
        ans = float('-inf')
        for i in range(len(values)):
            ans = max(ans, values[i]+mx-i)
            mx = max(mx, values[i] + i)
        
        return ans