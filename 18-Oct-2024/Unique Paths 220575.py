# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        t = m + n - 2
        return math.factorial(t) // (math.factorial(n-1) * math.factorial(t-n+1))
