from collections import deque

def find(x, parent):
    curr = x
    while curr != parent[curr]:
        curr = parent[curr]
    
    while x != parent[x]:
        nxt = parent[x]
        parent[x] = curr
        x = nxt
    
    return curr


def union(x, y, parent):
    X, Y = find(x, parent), find(y, parent)
    parent[Y] = parent[X]


def get_cycle(st, end, adj):
    adj[st].remove(end)
    queue = deque([(st, f"{st + 1}")])
    visited = set([st])
    while queue:
        for _ in range(len(queue)):
            c, p = queue.popleft()
            if c == end:
                return p
            
            for nb in adj[c]:
                if nb not in visited:
                    visited.add(nb)
                    queue.append((nb, p + f" {nb + 1}"))


for _ in range(int(input())):
    N, M = map(int, input().split())
    edges = []
    for i in range(M):
        edges.append(list(map(int, input().split())))
    
    edges.sort(key=lambda x: x[2], reverse=True)
    
    adj = [[] for _ in range(N)]
    parent = [i for i in range(N)]
    min_e = None
    min_w = float('inf')
    for x, y, w in edges:
        if find(x - 1, parent) == find(y - 1, parent):
            min_e = (x-1, y-1)
            min_w = w
        
        union(x - 1, y - 1, parent)
        adj[x-1].append(y-1)
        adj[y-1].append(x-1)
        
    
    path = get_cycle(*min_e, adj).strip()
    print(min_w, (len(path) - 1) // 2 + 1)
    print(path)
