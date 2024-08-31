V, E = list(map(int, input().split()))
adj = [[] for _ in range(V)]
for i in range(E):
    x, y = list(map(int, input().split()))
    adj[x - 1].append(y - 1)
    adj[y - 1].append(x - 1)


def checkCycle(i):
    global coloring

    stack = [i]
    cycle = True
    visited = set([i])
    count = 0

    while stack:
        n = stack.pop()
        coloring[n] = 1
        count += 1

        if len(adj[n]) != 2:
            cycle = False
        
        for ed in adj[n]:
            if ed not in visited:
                stack.append(ed)
                visited.add(ed)
    
    if count < 3:
        cycle = False
        

    return cycle


coloring = [0] * V
count = 0
for i in range(V):
    if coloring[i] == 0:
        if checkCycle(i):
            count += 1

print(count)