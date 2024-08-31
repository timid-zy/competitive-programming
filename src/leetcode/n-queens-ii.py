class Solution:
    def totalNQueens(self, n: int) -> int:

        def markBoard(r, c, board, val):
            for col in range(n):
                board[r][col] += val
            
            for row in range(n):
                if row == r: continue
                board[row][c] += val
            
            x = 1
            while x < n:
                if r + x < n and c + x < n:
                    board[r + x][c + x] += val
                if r - x >= 0 and c - x >= 0:
                    board[r - x][c - x] += val
                if r + x < n and c - x >= 0:
                    board[r + x][c - x] += val
                if r - x >= 0 and c + x < n:
                    board[r - x][c + x] += val
                x += 1
            
        count = 0
        board = [[0] * n for _ in range(n)]
        
        def checkQueens(r, board):
            nonlocal count
            if r >= n:
                count += 1
                return
            
            for c in range(n):
                if board[r][c] == 0:
                    markBoard(r, c, board, 1)
                    checkQueens(r + 1, board)
                    markBoard(r, c, board, -1)
        
        checkQueens(0, board)
        return count