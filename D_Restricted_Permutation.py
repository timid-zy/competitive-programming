from collections import deque
from heapq import heapify, heappop, heappush

N, K = map(int, input().split())
graph = [set() for _ in range(N)]
degree = [0] * N

for _ in range(K):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    if b not in graph[a]:
        graph[a].add(b)
        degree[b] += 1

queue = []
order = []
for i in range(len(graph)):
    if degree[i] == 0:
        queue.append(i)

heapify(queue)

while queue:
    c = heappop(queue)
    order.append(c)
    for nb in graph[c]:
        degree[nb] -= 1
        if degree[nb] == 0:
            heappush(queue, nb)

if len(order) != N:
    print(-1)

else:
    order = list(map(lambda x: str(x + 1), order))
    print(" ".join(order))
