# Problem: Max Increase To Keep City Skyline - https://leetcode.com/problems/max-increase-to-keep-city-skyline/

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rows = [max(grid[i]) for i in range(len(grid))]
        cols = [float('-inf')] * len(grid)
        for c in range(len(grid[0])):
            for r in range(len(grid)):
                cols[c] = max(cols[c], grid[r][c])
        
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                res += min(rows[r], cols[c]) - grid[r][c]
        
        return res
