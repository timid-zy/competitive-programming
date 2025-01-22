# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        def inbound(x, y):
            return 0 <= x < N and 0 <= y < M

        N, M = len(isWater), len(isWater[0])
        visited = set()
        queue = deque()
        res = [[0] * M for _ in range(N)]
        dire = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for r in range(N):
            for c in range(M):
                if isWater[r][c] == 0:
                    continue
                
                for dr, dc in dire:
                    nr, nc = r + dr, c + dc
                    if inbound(nr, nc) and isWater[nr][nc] == 0 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
        
        lvl = 0
        while queue:
            for _ in range(len(queue)):
                cr, cc = queue.popleft()
                res[cr][cc] = lvl + 1
                for dr, dc in dire:
                    nr, nc = cr + dr, cc + dc
                    if inbound(nr, nc) and isWater[nr][nc] == 0 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            
            lvl += 1

        return res


