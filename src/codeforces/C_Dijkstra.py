from collections import deque, defaultdict
from heapq import heappop, heappush

def solve():
    n, e = list(map(int, input().split()))
    graph = defaultdict(list)
    for _ in range(e):
        u, v, w = list(map(int, input().split()))
        graph[u].append((v, w))
        graph[v].append((u, w))

    D = [float('inf')] * (n + 1)
    D[1] = 0
    seen = set()
    fringe = [(0, 1, None)]
    parent = {1: None}
    while fringe:
        cd, cn, prev = heappop(fringe)
        if cn in seen:
            continue

        parent[cn] = prev
        seen.add(cn)
        for nb, weight in graph[cn]:
            if D[cn] + weight < D[nb]:
                D[nb] = D[cn] + weight
                heappush(fringe, (D[nb], nb, cn))

    if D[n] == float('inf'):
        return [-1]

    path = []
    curr = n
    while curr is not None:
        path.append(curr)
        curr = parent[curr]
    
    return path[::-1]

ans = solve()
print(*ans)
