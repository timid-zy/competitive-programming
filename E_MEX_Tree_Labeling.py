from collections import defaultdict, deque

def solve():
    N = int(input())
    res = [-1] * (N-1)
    idx = {}
    graph = defaultdict(list)
    indeg = defaultdict(int)
    for _ in range(N-1):
        a, b = map(int, input().split())
        if a > b:
            a, b = b, a
        
        idx[(a, b)] = _
        graph[a].append(b)
        graph[b].append(a)
        indeg[a] += 1
        indeg[b] += 1

    c = 0
    for k in graph:
        if indeg[k] == 1:
            nb = graph[k][0]
            a, b = k, nb
            if a > b:
                a, b = b, a
            
            if res[idx[(a, b)]] == -1:
                res[idx[(a, b)]] = c
                c += 1

    for i in range(len(res)):
        if res[i] == -1:
            res[i] = c
            c += 1
    
    return res

res = solve()
for n in res: print(n)