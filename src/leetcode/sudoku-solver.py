class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def validate(r, c, val):
            if val in board[r]: # check in row
                return False
            
            if val in [ board[row][c] for row in range(9)]: # check in col
                return False

            x = (r // 3) * 3 + 1
            y = (c // 3) * 3 + 1

            if val in [board[x][y], board[x-1][y-1], board[x-1][y], board[x][y-1], board[x-1][y+1], board[x+1][y-1], board[x+1][y], board[x][y+1], board[x+1][y+1]]: # check in grid
                return False
            
            return True
        

        def solve(r, c):
            if r == 8 and c == 9:
                return True
            elif c == 9:
                return solve(r + 1, 0)
        
            if board[r][c] == ".":
                for val in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    if validate(r, c, val):
                        board[r][c] = val
                        if solve(r, c + 1):
                            return True
                        board[r][c] = "."
                return False
            else:
                return solve(r, c + 1)

        solve(0, 0)