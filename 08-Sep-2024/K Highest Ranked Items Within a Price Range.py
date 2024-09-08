class Solution:
    def highestRankedKItems(self, grid: List[List[int]], P: List[int], start: List[int], k: int) -> List[List[int]]:
        def inbound(x, y):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0])
        
        start = tuple(start)
        queue = deque([start])
        seen = set([start])
        heap = []
        d = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if grid[r][c] > 1 and P[0] <= grid[r][c] <= P[1]:
                    heappush(heap, (d, grid[r][c], r, c))
                
                for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nx, ny = r + dx, c + dy
                    if (nx, ny) not in seen and inbound(nx, ny) and grid[nx][ny] > 0:
                        queue.append((nx, ny))
                        seen.add((nx, ny))

            d += 1

        i, res = 0, []
        while heap and i < k:
            i += 1
            _, _, r, c = heappop(heap)
            res.append((r, c))
        
        return res
