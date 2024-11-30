class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        heap = [(0, 0, 0)]
        visited = set()
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        
        while heap:
            cd, cr, cc = heappop(heap)
            if (cr, cc) in visited:
                continue
            
            visited.add((cr, cc))
            if cr == N-1 and cc == M-1:
                return cd
            
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = cr+dr, cc+dc
                if 0 <= nr < N and 0 <= nc < M:
                    if grid[nr][nc]-1 <= cd:
                        heappush(heap, (cd+1, nr, nc))
                    else:
                        d = math.ceil((grid[nr][nc] - cd) // 2) * 2
                        heappush(heap, (cd+d+1, nr, nc))
