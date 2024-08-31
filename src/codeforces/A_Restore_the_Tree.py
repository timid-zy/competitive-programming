from collections import deque

N, M = list(map(int, input().split()))

adj = [[] for _ in range(N)]
indeg = [0] * N
for i in range(N - 1 + M):
    a, b = map(int, input().split())
    adj[a - 1].append(b - 1)
    indeg[b - 1] += 1

queue = deque()
for i in range(len(indeg)):
    if indeg[i] == 0:
        queue.append(i)

parents = [0] * N
while queue:
    for _ in range(len(queue)):
        c = queue.popleft()

        for nb in adj[c]:
            indeg[nb] -= 1
            if indeg[nb] == 0:
                parents[nb] = c + 1
                queue.append(nb)

for p in parents:
    print(p)