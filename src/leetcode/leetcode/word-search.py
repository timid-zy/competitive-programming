class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        w = len(board[0])
        h = len(board)

        def backtrack(r, c, idx=0):
            if idx == len(word) or (idx == len(word) - 1 and board[r][c] == word[idx]): return True
            if board[r][c] != word[idx]: return False
            
            for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if r + x >= 0 and r + x < h and c + y >= 0 and c + y < w:
                    board[r][c] = "."
                    if backtrack(r+x, c+y, idx+1):
                        return True
                    board[r][c] = word[idx]
            
            return False
        

        candidates = []
        for i in range(h):
            for j in range(w):
                if board[i][j] == word[0]: candidates.append((i, j))

        for x, y in candidates:
            if backtrack(x, y):
                return True
        return False