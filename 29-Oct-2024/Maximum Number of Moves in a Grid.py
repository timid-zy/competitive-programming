class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        def inbound(r, c, R, C):
            return 0 <= r < R and 0 <= c < C
        
        N, M = len(grid), len(grid[0])
        dp = [[-1] * M for _ in range(N)]
        for i in range(N):
            dp[i][0] = 0
        
        res = 0
        for c in range(M):
            to_continue = False
            for r in range(N):
                if dp[r][c] == -1:
                    continue
                
                for dx, dy in [(1, 1), (0, 1), (-1, 1)]:
                    nr, nc = r + dx, c + dy
                    if inbound(nr, nc, N, M) and grid[nr][nc] > grid[r][c]:
                        dp[nr][nc] = dp[r][c] + 1
                        res = max(res, dp[nr][nc])
                        to_continue = True

            if not to_continue:
                break
        
        return res
