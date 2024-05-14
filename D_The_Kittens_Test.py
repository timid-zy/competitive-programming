import sys
input = sys.stdin.readline

def find(x):
    curr = x
    while curr != parent[curr]:
        curr = parent[curr]
    
    while x != parent[x]:
        nxt = parent[x]
        parent[x] = curr
        x = nxt
    
    return x

def union(x, y):
    X, Y = find(x), find(y)
    parent[Y] = X
    arr[X] += arr[Y]

N = int(input())
parent = [i for i in range(N)]
arr = [[i + 1] for i in range(N)]
for _ in range(N - 1):
    x, y = map(int, input().split())
    union(x - 1, y - 1)

print(*arr[find(0)])                     