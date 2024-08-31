V = int(input())
adj = [[] for __ in range(V)]

for _ in range(V - 1):
    u, v, c = list(map(int, input().split()))
    adj[u].append((v, c))
    adj[v].append((u, c))

stack = [(0, 0)]
visited = set([0])
max_cost = 0

while stack:
    curr, cost = stack.pop()
    max_cost = max(max_cost, cost)

    for ed, nxt_cost in adj[curr]:
        if ed not in visited:
            visited.add(ed)
            stack.append((ed, cost + nxt_cost))

print(max_cost)