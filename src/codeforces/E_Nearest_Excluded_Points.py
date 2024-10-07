from collections import deque

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

seen = set()
ans = {}
idx = {}
for i in range(int(input())):
    p = tuple(map(int, input().split()))
    seen.add(p)
    ans[p] = None
    idx[p] = i

queue = deque()
for x, y in seen:
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if (nx, ny) not in seen and ans[(x, y)] is None:
            ans[(x, y)] = (nx, ny)
            queue.append((x, y))

while queue:
    for _ in range(len(queue)):
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (nx, ny) in seen and ans[(nx, ny)] is None:
                ans[(nx, ny)] = ans[(x, y)]
                queue.append((nx, ny))

res = [None] * len(seen)
for k, v in ans.items(): 
    i = idx[k]
    res[i] = v

for x, y in res:
    print(x, y)