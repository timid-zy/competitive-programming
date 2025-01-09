# Problem: Knight Probability in Chessboard - https://leetcode.com/problems/knight-probability-in-chessboard/

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        @cache
        def dp(r, c, moves):
            if not (0 <= r < n and 0 <= c < n):
                return 0

            if moves == 0:
                return 1
            
            p = 0
            for dr, dc in [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]:
                p += 1/8 * dp(r + dr, c + dc, moves-1)
            
            return p
        
        return dp(row, column, k)