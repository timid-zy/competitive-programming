from collections import defaultdict, deque

def solve():
    N, M = map(int, input().split())
    graph = defaultdict(set)
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].add(b)
        graph[b].add(a)

    is_rail = False
    if N in graph[1]:
        is_rail = True

    queue = deque([1])
    seen = set([1])
    lvl = 0

    while queue:
        for _ in range(len(queue)):
            c = queue.popleft()
            if c == N:
                print(lvl)
                return

            for nb in range(1, N+1):
                if (is_rail and nb in graph[c]) or (not is_rail and nb not in graph[c]):
                    continue
                
                if nb not in seen:
                    seen.add(nb)
                    queue.append(nb)
        
        lvl += 1

    print(-1)

solve()