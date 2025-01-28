# Problem: Maximum Number of Fish in a Grid - https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def inbound(x, y):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0])

        def bfs(sr, sc):
            queue = deque([(sr, sc)])
            res = grid[sr][sc]
            grid[sr][sc] = 0
            while queue:
                cr, cc = queue.popleft()
                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nr, nc = cr+dr, cc+dc
                    if inbound(nr, nc) and grid[nr][nc] > 0:
                        queue.append((nr, nc))
                        res += grid[nr][nc]
                        grid[nr][nc] = 0
            
            return res

        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] > 0:
                    res = max(res, bfs(r, c))
        
        return res
                        