# Problem: Minimum Obstacle Removal to Reach Corner - https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        D = {}
        for i in range(N):
            for j in range(M):
                D[(i, j)] = float('inf')

        D[(0, 0)] = 0
        seen = set()
        heap = [(0, 0, 0)]
        while heap:
            cd, cr, cc = heappop(heap)
            if (cr, cc) in seen:
                continue
            
            if cr == N-1 and cc == M-1:
                return cd
            
            seen.add((cr, cc))
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nr, nc = cr + dx, cc + dy
                if 0 <= nr < N and 0 <= nc < M:
                    newd = cd + 1 if grid[nr][nc] == 1 else cd
                    if D[(nr, nc)] > newd:
                        D[(nr, nc)] = newd
                        heappush(heap, (newd, nr, nc))
    