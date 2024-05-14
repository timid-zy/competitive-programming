def checkBounds(x, y, grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

def canEscape(a, b, grid):
    
    stack = [[a, b]]
    path = [[a, b]]

    while stack:
        x, y = stack.pop()
        if grid[x][y] == 'P' or x == len(grid) - 1 and y == len(grid[0]) - 1:
            for x, y in path:
                grid[x][y] = "P"
            return True

        grid[x][y] = 'C'
        path.append([x, y])
        
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_x = x + dx
            new_y = y + dy
            if checkBounds(new_x, new_y, grid) and grid[new_x][new_y] in ["P", ".", "G"]:
                stack.append([new_x, new_y])
        
    
    return False


        

for i in range(int(input())):
    r, c = map(int, input().split())
    grid = []

    bad = []
    good = []
    for i in range(r):
        lvl = []
        s = input()
        for j in range(len(s)):
            if s[j] == "G":
                good.append([i, j])
            elif s[j] == "B":
                bad.append([i, j])
            lvl.append(s[j])
        grid.append(lvl)
    

    possible = True
    for x, y in bad:
        if not possible:
            break

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_x = x + dx
            new_y = y + dy
            if checkBounds(new_x, new_y, grid) and grid[new_x][new_y] != "#":
                if grid[new_x][new_y] == "G":
                    possible = False
                    break
                
                elif grid[new_x][new_y] == ".":
                    grid[new_x][new_y] = "#"
 
    for x, y in good:
        if grid[x][y] == "P":
            continue

        if not possible or not canEscape(x, y, grid):
            possible = False
            break
    
    for x, y in bad:
        if grid[x][y] == "P":
            possible = False
            break

        if not possible or canEscape(x, y, grid):
            possible = False
            break
    
    if not possible:
        print('No')
    
    else:
        print('Yes')
