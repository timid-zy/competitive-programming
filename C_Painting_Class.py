from collections import deque

V = int(input())
E = list(map(int, input().split()))
C = list(map(int, input().split()))

adj = [[] for _ in range(V)]

for i in range(len(E)):
    adj[i + 1].append(E[i] - 1)
    adj[E[i] - 1].append(i + 1)

queue = deque([(0, -1)])
visited = set([0])
ops = 0

while queue:
    for __ in range(len(queue)):
        curr, color = queue.popleft()
        if color != C[curr]:
            ops += 1
            color = C[curr]
        
        for ed in adj[curr]:
            if ed not in visited:
                visited.add(ed)
                queue.append((ed, color))


print(ops)