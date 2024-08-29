def check(row, col, grid):
    seen = set()
    for r in range(len(grid)):
        if r == row: continue
        seen.add(grid[r][col])
    
    
    for c in range(len(grid)):
        if c == col: continue
        target = grid[row][col] - grid[row][c]
        if target in seen:
            return True


    return False

def solve():
    N = int(input())

    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))

    for r in range(N):
        for c in range(N):
            if grid[r][c] != 1 and not check(r, c, grid):
                return "No"
    
    return "Yes"

print(solve())