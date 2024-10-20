from collections import defaultdict
from heapq import heappush, heappop

def solve():
    N, M = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(M):
        a, b, w = map(int, input().split())
        graph[a].append((b, w))
        graph[b].append((a, w))
    
    bikes = list(map(int, input().split()))
    heap = [(0, bikes[0], 1)]
    seen = {}
    while heap:
        cd, cb, cn = heappop(heap)
        if cn == N:
            return cd

        if cn in seen and seen[cn] <= cb:
            continue
            
        seen[cn] = cb
        curr_bike = min(cb, bikes[cn-1])
        for nb, weight in graph[cn]:
            heappush(heap, (cd+(weight*curr_bike), curr_bike, nb))

    return -1

for _ in range(int(input())):
    print(solve())