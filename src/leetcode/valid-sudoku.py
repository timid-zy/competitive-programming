class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(len(board)):
            seen = set()
            for col in range(len(board[0])):
                if board[row][col] != ".":
                    num = int(board[row][col])
                    if num > 9 or num < 1:
                        return False
                    pre_len = len(seen)
                    seen.add(num)
                    if pre_len == len(seen):
                        return False
        
        for col in range(len(board[0])):
            seen = set()
            for row in range(len(board)):
                if board[row][col] != ".":
                    num = int(board[row][col])
                    if num > 9 or num < 1:
                        return False
                    pre_len = len(seen)
                    seen.add(num)
                    if pre_len == len(seen):
                        return False
        
        for row in range(0, len(board), 3):
            for col in range(0, len(board[0]), 3):
                seen = set()
                for r in range(row, row + 3):
                    for c in range(col, col + 3):
                        if board[r][c] != ".":
                            num = int(board[r][c])
                            if num > 9 or num < 1:
                                return False
                            pre_len = len(seen)
                            seen.add(num)
                            if pre_len == len(seen):
                                return False

        return True