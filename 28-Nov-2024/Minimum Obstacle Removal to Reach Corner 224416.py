# Problem: Minimum Obstacle Removal to Reach Corner - https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        def inbound(x, y, matrix):
            return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])

        visited = set()
        heap = [(0, 0, 0)] if grid[0][0] == 0 else [(1, 0, 0)]
        while heap:
            cd, cr, cc = heappop(heap)
            add = 0 if grid[cr][cc] == 0 else 1
            if cr == len(grid)-1 and cc == len(grid[0]) - 1:
                return cd + add
            
            if (cr, cc) in visited:
                continue
            
            visited.add((cr, cc))
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = cr + dr, cc + dc
                if inbound(nr, nc, grid) and (nr, nc) not in visited:
                    heappush(heap, (cd + add, nr, nc))
                
