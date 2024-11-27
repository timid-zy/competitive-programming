from collections import defaultdict, deque
from heapq import heappop, heappush

N, M = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

indeg = defaultdict(int)
for a in graph:
    indeg[a] = len(graph[a])

queue = deque()
for a in graph:
    if indeg[a] == 1:
        queue.append(a)

mx_dist = defaultdict(int)
seen = set(list(queue))
ans = 0
while queue:
    cn = queue.popleft()
    dists = []
    for nb in graph[cn]:
        indeg[nb] -= 1
        if ((indeg[nb] == 1 and nb != 1) or (indeg[nb] == 0 and nb == 1)) and nb not in seen:
            queue.append(nb)
            seen.add(nb)
        
        if nb in mx_dist and mx_dist[nb] > 0:
            heappush(dists, -mx_dist[nb])
    
    if len(dists) == 0:
        mx_dist[cn] = 1
    else:
        mx_dist[cn] = -dists[0] + 1

    if len(dists) == 1:
        ans = max(ans, -dists[0])
    elif len(dists) > 1:
        ans = max(ans, -(heappop(dists) + heappop(dists)))
    
print(ans)
        
