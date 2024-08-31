from collections import defaultdict, deque

for _ in range(int(input())):
    V, E = map(int, input().split())
    graph = defaultdict(set)
    indeg = defaultdict(int)
    undirected = defaultdict(set)
    edges = []

    for __ in range(E):
        t, a, b = map(int, input().split())
        if t == 0:
            undirected[a].add(b)
            undirected[b].add(a)
            graph[a].add(b)
            graph[b].add(a)

        else:
            edges.append((a, b))
            indeg[b] += 1
            graph[a].add(b)

    queue = deque()
    count = 0
    for key in range(1, V + 1):
        if key not in indeg:
            queue.append(key)
            count += 1
            for ud in undirected[key]:
                edges.append((key, ud))
                indeg[ud] += 1
                undirected[ud].remove(key)
    
    while queue:
        for _ in range(len(queue)):
            c = queue.popleft()
            for nb in graph[c]:
                indeg[nb] -= 1
                if indeg[nb] == 0:
                    count += 1
                    queue.append(nb)
                
                    for ud in undirected[nb]:
                        edges.append((nb, ud))
                        indeg[ud] += 1
                        undirected[ud].remove(nb)

    if count == V:
        print('YES')
        for x, y in edges:
            print(x, y)
    
    else:
        print('NO')
    