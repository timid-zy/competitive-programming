# Problem: The shortest path - https://basecamp.eolymp.com/en/problems/4853

def solve():
    N, M = map(int, input().split())
    S, E = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    parents = {S: None}
    queue = deque([S])
    seen = set([S])
    found = False
    while queue:
        curr = queue.popleft()
        if curr == E:
            found = True
            break

        for nb in graph[curr]:
            if nb not in seen:
                seen.add(nb)
                parents[nb] = curr
                queue.append(nb)

    if not found:
        print(-1)
        return

    res = []
    curr = E
    while curr != None:
        res.append(curr)
        curr = parents[curr]

    
    print(len(res) - 1)
    print(*reversed(res))

solve()