# Problem: Shortest Path in Binary Matrix - https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

class Solution:
    def inbound(self, x, y, grid):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1]:
            return -1

        queue = deque([(0, 0)])
        dire = [(1, 1), (1, -1), (1, 0), (0, 1), (0, -1), (-1, 0), (-1, 1), (-1, -1)]
        lvl = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == len(grid)-1 and c == len(grid[0])-1:
                    return lvl + 1

                for dr, dc in dire:
                    nr, nc = r + dr, c + dc
                    if self.inbound(nr, nc, grid) and grid[nr][nc] == 0:
                        queue.append([nr, nc])
                        grid[nr][nc] = 1
            
            lvl += 1
        
        return -1
