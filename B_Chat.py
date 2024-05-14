from heapq import heappop, heappush

N, K, Q = map(int, input().split())

heap = []
active = [0] * N
arr = list(map(int, input().split()))

for __ in range(Q):
    c, idx = map(int, input().split())
    idx -= 1

    if c == 2:
        if active[idx] == 0:
            print('NO')
        else:
            print('YES')
        continue

    heappush(heap, (arr[idx], idx))
    active[idx] = 1
    if len(heap) == K + 1:
        v, i = heappop(heap)
        active[i] = 0
    
    
