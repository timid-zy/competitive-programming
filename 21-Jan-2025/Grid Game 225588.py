# Problem: Grid Game - https://leetcode.com/problems/grid-game/

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        N = len(grid[0])
        if N <= 1: return 0
        prefix = [0] * N; prefix[0] = grid[1][0]
        suffix = [0] * N; suffix[-1] = grid[0][-1]
        for i in range(1, N):
            prefix[i] = prefix[i-1] + grid[1][i]
            suffix[-i-1] = suffix[-i] + grid[0][-i-1]
        
        mn = min(suffix[1], prefix[-2])
        for i in range(1, N-1):
            mn = min(mn, max(prefix[i-1], suffix[i+1]))
        
        return mn