from heapq import heappop, heappush

for _ in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))

    heap = []
    score = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            if heap:
                score -= heappop(heap)
            continue
        
        heappush(heap, -arr[i])
    
    print(score)
