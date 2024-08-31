def find(x):
    while x != parent[x]:
        x = parent[parent[x]]
    
    return x

def union(x, y):
    r1, r2 = find(x), find(y)
    if r1 != r2:
        if size[r1] > size[r2]:
            parent[r2] = r1
            size[r1] += size[r2]
            exp[r1] += exp[r2]
        else:
            parent[r1] = r2
            size[r2] += size[r1]

N, M = map(int, input().split())
parent = [i for i in range(N)]
size = [1] * N
exp = [0] * N
excess = [0] * N

for __ in range(M):
    op = input().split()
    op.append("1")
    x, y = int(op[1]) - 1, int(op[2])

    if op[0] == "add":
        exp[find(x)] += y
    
    if op[0] == "join":
        union(x, y - 1)
    
    if op[0] == "get":
        print(exp[x])