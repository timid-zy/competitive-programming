from collections import deque

V = int(input())
adj = [ [] for _ in range(V)]
for i in range(V - 1):
    x, y = map(int, input().split())
    adj[x - 1].append(y - 1)
    adj[y - 1].append(x - 1)

curr = list(map(int, input().split()))
goal = list(map(int, input().split()))


queue = deque([[0, 0, 0]])
visited = set([0])
ops = []

while len(queue) > 0:
    n, p, gp = queue.popleft()
    curr[n] = (curr[n] + gp) % 2

    if goal[n] != curr[n]:
        ops.append(n + 1)
        gp += 1
    
    for ed in adj[n]:
        if ed not in visited:
            visited.add(ed)
            queue.append([ed, gp, p])

print(len(ops))
for ed in ops:
    print(ed)