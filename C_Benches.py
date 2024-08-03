from heapq import heapify, heappop, heappush

N = int(input())
M = int(input())
A = []
for _ in range(N):
    A.append(int(input()))

mx = max(A) + M
heapify(A)
for _ in range(M):
    v = heappop(A)
    v += 1
    heappush(A, v)

print(max(A), mx)