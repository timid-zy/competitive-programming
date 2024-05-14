def find(x):
    curr = x
    while x != parent[x]:
        x = parent[x]
    
    while curr != parent[curr]:
        nxt = parent[curr]
        parent[curr] = x
        curr = nxt
    
    return curr

def union(x, y):
    r1, r2 = find(x), find(y)
    parent[r2] = r1

N = int(input())
arr = list(map(int, input().split()))
parent = [i for i in range(N)]

for i in range(len(arr)):
    union(arr[i] - 1, i)

visited = set()
for x in parent:
    visited.add(find(x))

print(len(visited))