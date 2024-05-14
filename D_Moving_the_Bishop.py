from collections import deque
import sys

input = sys.stdin.readline

def checkBounds(x, y, board):
    return 0 <= x < len(board) and 0 <= y < len(board[0])

N = int(input())
ax, ay = map(int, input().split())
bx, by = map(int, input().split())

ax -= 1
ay -= 1
bx -= 1
by -= 1

board = []
for __ in range(N):
    s = input().strip()
    lvl = []
    for x in s:
        lvl.append(x)
    
    board.append(lvl)


def solve(board):
    queue = deque([(ax, ay)])
    board[ax][ay] = ["V", ""]
    lvl = 0
    if (ax, ay) == (bx, by):
        return lvl

    while queue:
        for _ in range(len(queue)):
            cx, cy = queue.popleft()
            
            directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
            for i in range(len(directions)):
                dx, dy = directions[i]
                nx, ny = cx + dx, cy + dy
                while checkBounds(nx, ny, board) and board[nx][ny] != "#":
                    if (nx, ny) == (bx, by):
                        return lvl + 1
                    if board[nx][ny][0] != "V":
                        board[nx][ny] = ["V", f"{i}"]
                        queue.append((nx, ny))
                    
                    elif str(i) in board[nx][ny][1]:
                        break
                        
                    else:
                        board[nx][ny][1] += str(i)
                    
                    nx += dx
                    ny += dy
        
        lvl += 1
    
    return -1

print(solve(board))