for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    grid = []
    for i in range(n):
        grid.append(list(map(int, (input().split()))))

    def checkBounds(x, y):
        return 0 <= x < n and 0 <= y < m

    def getVolume(x, y):
        stack = [[x, y]]
        ans = 0
        while stack:
            x, y = stack.pop()
            ans += grid[x][y]
            grid[x][y] = 0
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if checkBounds(x + dx, y + dy) and grid[x + dx][y + dy] > 0:
                    stack.append([x + dx, y + dy])
        
        return ans
    

    ans = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0:
                ans = max(ans, getVolume(i, j))
    
    print(ans)