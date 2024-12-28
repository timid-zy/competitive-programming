from collections import defaultdict, deque

MOD = 998244353
def multiply(a, b, p):
    return ((a % p) * (b % p)) % p

def binary_expo(base, exp, p):
    res = 1
    while exp > 0:
        if exp & 1:
            res = multiply(base, res, p)
        
        base = multiply(base, base, p)
        exp >>= 1
    
    return res

def inverse(a, p):
    return binary_expo(a, p-2, p)

def solve():
    N = int(input())
    graph = defaultdict(list)
    for _ in range(N-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    queue = deque([(1, None)])
    dist = defaultdict(int)
    lvl = 0
    while queue:
        for __ in range(len(queue)):
            curr, parent = queue.popleft()
            added = 0
            for nb in graph[curr]:
                if nb != parent:
                    added += 1
                    queue.append((nb, curr))
            
            if added > 0:
                dist[curr] = lvl
            else:
                dist[curr] = float('inf')
        
        lvl += 1
    
    res = []
    for i in range(1, N+1):
        if dist[i] == 0:
            res.append(1)
        elif dist[i] == float('inf'):
            res.append(0)
        else:
            res.append((inverse(2**dist[i], MOD)) % MOD)
    
    print(*res)

for _ in range(int(input())):
    solve()