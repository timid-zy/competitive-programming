# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def inbound(self, row, col, grid):
        return 0 <= row < len(grid) and 0 <= col < len(grid[0])

    def dfs(self, row, col, grid):
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        stk = [(row, col)]
        grid[row][col] = "0"
        while stk:
            r, c = stk.pop()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if self.inbound(nr, nc, grid) and grid[nr][nc] == "1":
                    grid[nr][nc] = "0"
                    stk.append((nr, nc))


    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    res += 1
                    self.dfs(r, c, grid)
        
        return res