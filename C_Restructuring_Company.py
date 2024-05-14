import sys
input = sys.stdin.readline

def find(x):
    curr = x
    while curr != parent[curr]:
        curr = parent[curr]
    
    while x != parent[x]:
        nx = parent[x]
        parent[x] = curr
        x = nx
    
    return curr

def union(x, y):
    X, Y = find(x), find(y)
    if X != Y:
        if size[X] > size[Y]:
            parent[Y] = X
            size[X] += size[Y]
        
        else:
            parent[X] = Y
            size[Y] += size[X]

N, Q = map(int, input().split())
parent = [i for i in range(N)]
size = [1] * N

for i in range(Q):
    t, x, y = map(int, input().split())
    x, y = x-1, y-1
    
    if t == 1:
        union(x, y)
    
    elif t == 2:
        for z in range(x + 1, y + 1):
            union(x, z)
        
    else:
        ans = "YES" if find(x) == find(y) else "NO"
        print(ans)