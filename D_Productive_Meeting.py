from heapq import heapify, heappop, heappush

for __ in range(int(input())):
    input()
    arr = list(map(int, input().split()))

    heap = []
    for i in range(len(arr)):
        if arr[i] == 0:
            continue

        heap.append((-1 * arr[i], i + 1))

    heapify(heap)
    ans = []
    while len(heap) > 1:
        p1, idx1 = heappop(heap)
        p2, idx2 = heappop(heap)
        p1, p2 = p1 * -1, p2 * -1

        for i in range(p2):
            ans.append((idx2, idx1))
        
        p1 -= p2
        if p1 > 0:
            heappush(heap, (p1 * -1, idx1))
    
    print(len(ans))
    for x, y in ans:
        print(x, y)
