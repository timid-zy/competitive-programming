K, N, M = map(int, input().split())

plates = [] # z, y, x
input()
for _ in range(K):
    grid = []
    for __ in range(N):
        s = input()
        row = []
        for c in s:
            row.append(c)
        grid.append(row)
    input()
    plates.append(grid)
    
def inbound(x, y, z):
    return 0 <= x < N and 0 <= y < M and 0 <= z < K

x, y = map(int, input().split())
directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
stk = [(0, x-1, y-1)]
t = 1
plates[0][x-1][y-1] = "#"

while stk:
    z, x, y = stk.pop()

    for dx, dy, dz in directions:
        nx, ny, nz = x + dx, y + dy, z + dz
        if inbound(nx, ny, nz) and plates[nz][nx][ny] == '.':
            t += 1
            plates[nz][nx][ny] = '#'
            stk.append((nz, nx, ny))


print(t)