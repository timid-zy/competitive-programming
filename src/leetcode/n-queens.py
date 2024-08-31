class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        # mark the board with value, for each cell:
        # n > 0 - can be attacked by n queens
        # n == 0 - free
        def markBoard(r, c, board, val):
            for col in range(n):
                board[r][col] += val
            
            for row in range(n):
                board[row][c] += val
            
            x = 1
            while x < n:
                if r + x < n and c + x < n:
                    board[r + x][c + x] += val
                if r + x < n and c - x >= 0:
                    board[r + x][c - x] += val
                if r - x >= 0 and c + x < n:
                    board[r - x][c + x] += val
                if r - x >= 0 and c - x >= 0:
                    board[r - x][c - x] += val
                x += 1
            
        board = [ [0] * n for i in range(n)]
        solutions = []
        def backtrack(r, board, queens):
            nonlocal solutions
            if r >= n:
                solutions.append(queens[:])
                return
            
            for c in range(n):
                if board[r][c] == 0:
                    markBoard(r, c, board, 1)
                    queens.append(c)
                    backtrack(r + 1, board, queens)
                    markBoard(r, c, board, -1)
                    queens.pop()
        
        backtrack(0, board, [])
        
        # change the indicies to boards
        for i in range(len(solutions)):
            for j in range(len(solutions[i])):
                s = ""
                for k in range(n):
                    if k == solutions[i][j]:
                        s += "Q"
                    else:
                        s += "."
                solutions[i][j] = s

        return solutions