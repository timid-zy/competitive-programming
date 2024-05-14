def find(x):
    if x == parent[x]:
        return x
    
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    r1, r2 = find(x), find(y)
    if r1 != r2:
        if size[r1] > size[r2]:
            parent[r2] = r1
            size[r1] += size[r2]
        else:
            parent[r1] = r2
            size[r2] += size[r1]

V, E, M = map(int, input().split())
for _ in range(E): input()
queries = []
for _ in range(M):
    queries.append(input())

parent = [i for i in range(V)]
size = [1] * V
res = []

for i in range(len(queries) - 1, -1, -1):
    op, a, b = queries[i].split()
    a = int(a) - 1
    b = int(b) - 1

    if op == "ask":
        ans = "YES" if find(a) == find(b) else "NO"
        res.append(ans)
    
    else:
        union(a, b)

for i in range(len(res) - 1, -1, -1):
    print(res[i])
