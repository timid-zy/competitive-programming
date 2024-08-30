from collections import defaultdict

def find(x, parent):
    curr = x
    while curr != parent[curr]:
        curr = parent[curr]
    
    while x != parent[x]:
        nx = parent[x]
        parent[x] = curr
        x = nx
    
    return curr

def union(x, y, parent):
    X, Y = find(x, parent), find(y, parent)
    parent[X] = Y
    return X

N, M = map(int, input().split())
parents = {}
for _ in range(M):
    a, b, c = map(int, input().split())
    if c not in parents:
        parents[c] = [i for i in range(N+1)]
    
    union(a, b, parents[c])

for __ in range(int(input())):
    a, b = map(int, input().split())
    count = 0
    for c in parents:
        if find(a, parents[c]) == find(b, parents[c]):
            count += 1
    
    print(count)
