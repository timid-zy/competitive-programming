from collections import deque

for ___ in range(int(input())):
    input()
    n, f = map(int, input().split())
    
    friends = list(map(int, input().split()))
    for i in range(len(friends)): friends[i] -= 1

    adj = [[] for _ in range(n)]
    for i in range(n - 1):
        x, y = list(map(int, input().split()))
        adj[x - 1].append(y - 1)
        adj[y - 1].append(x - 1)
    
    times = [float('inf')] * (n)
    for d in friends:
        times[d] = 0

    queue = deque(friends)
    lvl = 1
    while queue:
        for _ in range(len(queue)):
            c = queue.popleft()

            for ed in adj[c]:
                if times[ed] == float('inf'):
                    times[ed] = lvl
                    queue.append(ed)
        
        lvl += 1
    
    queue = deque([0])
    visited = set([0])
    lvl = 0
    found = False

    while queue:
        for _ in range(len(queue)):
            c = queue.popleft()
            if c != 0 and len(adj[c]) == 1:
                found = True
                break
            
            for ed in adj[c]:
                if lvl + 1 < times[ed] and ed not in visited:
                    queue.append(ed)
                    visited.add(ed)
        
        lvl += 1
    
    if found:
        print('YES')
    else:
        print('NO')