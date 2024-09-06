# Problem: E - Beef in M.A.A.D City - https://codeforces.com/gym/538762/problem/E

from collections import defaultdict, deque

def solve():
    N, K, D = map(int, input().split())
    graph = defaultdict(list)
    indeg = defaultdict(int)
    for __ in range(N):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        indeg[a] += 1
        indeg[b] += 1
    
    if K == D:
        return "NO"
    
    seen = set()
    queue = deque()
    for k in indeg:
        if indeg[k] == 1:
            queue.append(k)
    
    while queue:
        curr = queue.popleft()
        seen.add(curr)
        for nb in graph[curr]:
            indeg[nb] -= 1
            if indeg[nb] == 1:
                queue.append(nb)

    dct = defaultdict(str)
    dct[D] = "D"
    dct[K] = "K"
    queue = deque([(K, "K"), (D, "D")])
    while queue:
        for _ in range(len(queue)):
            curr, sign = queue.popleft()
            for nb in graph[curr]:
                if dct[nb] == "":
                    dct[nb] = sign
                    queue.append((nb, sign))
    
    for n in graph:
        if n not in seen and dct[n] == "D":
            return "YES"
    
    return "NO"


for _ in range(int(input())):
    print(solve())
