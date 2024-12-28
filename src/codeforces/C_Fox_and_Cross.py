def inbound(x, y, board):
    return 0 <= x < len(board) and 0 <= y < len(board[0])

def draw_down(x, y, board):
    cands = [(x, y), (x+1, y), (x+2, y), (x+1, y-1), (x+1, y+1)]
    for r, c in cands:
        if not inbound(r, c, board) or board[r][c] == ".":
            return False
    
        board[r][c] = "."
    
    return True

def solve():
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(input()))

    for r in range(N):
        for c in range(N):
            if board[r][c] == "#" and not draw_down(r, c, board):
                return "NO"

    return "YES"

print(solve())