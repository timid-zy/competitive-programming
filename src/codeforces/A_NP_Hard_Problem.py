def getVertexCover(i):
    global coloring

    stack = [(i, 1)]
    possible = True
    ar1 = []
    ar2 = []
    
    while possible and stack:
        n, e = stack.pop()
        
        if coloring[n] != 0 and coloring[n] != e:
            possible = False
            break
            
        elif coloring[n] == e:
            continue
        
        coloring[n] = e

        if e == 1: ar1.append(n + 1)
        else: ar2.append(n + 1)

        ex = 1 if e == 2 else 2
        for ed in adj[n]:
            if coloring[ed] == 0:
                stack.append([ed, ex])
            
            elif coloring[ed] != ex:
                possible = False
                break
    
    if not possible:
        return None
    
    return (ar1, ar2)

V, E = map(int, input().split())
adj = [[] for _ in range(V)]

for i in range(E):
    x, y = map(int, input().split())
    adj[x - 1].append(y - 1)
    adj[y - 1].append(x - 1)

coloring = [0] * V
left = []
right = []
flag = True
for i in range(len(adj)):
    if coloring[i] == 0:
        if len(adj[i]) == 0: 
            coloring[i] = 1
            continue

        a = getVertexCover(i)
        if a is None:
            flag = False
            break
        
        l, r = a
        left += l
        right += r

if flag:
    print(len(left))
    print(" ".join(map(str, left)))
    print(len(right))
    print(" ".join(map(str, right)))
else:
    print(-1)