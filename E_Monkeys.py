def find(x, P):
    curr = x
    while curr != P[curr]:
        curr = P[curr]
    
    while x != P[x]:
        nx = P[x]
        P[x] = curr
        x = nx
    
    return curr


def union(x, y, P):
    X, Y = find(x, P), find(y, P)
    P[Y] = X


V, E = map(int, input().split())
hands = {}
for i in range(V):
    l, r = map(lambda x: int(x) - 1, input().split())
    hands[i] = (l, r)

edges = []
for _ in range(E):
    pi, hi = map(lambda x: int(x) - 1, input().split())
    edges.append((pi, hands[pi][hi]))

edges.reverse()
t = len(edges) - 1 # current time
end = {}
p = [i for i in range(V)]
ct = [i for i in range(V)]

for x, y in edges:
    if x == 0 or find(x, p) == find(0, p):
        union(x, y, p)
        end[find(y, ct)] = max(end.get(find(y, ct), 0), t)
    
    elif y == 0 or find(y, p) == find(0, p):
        union(x, y, p)
        end[find(x, ct)] = max(end.get(find(x, ct), 0), t)
    
    else:
        union(x, y, p)
        union(x, y, ct)

    t -= 1

ans = [-1] * V
for i in range(V):
    if find(i, ct) in end:
        ans[i] = end[find(i, ct)] 

for e in ans:
    print(e)
