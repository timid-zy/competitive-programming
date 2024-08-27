from collections import defaultdict


def find(x, parent):
    curr = x
    while curr != parent[curr]:
        curr = parent[curr]
    
    while x != parent[x]:
        nx = parent[x]
        parent[x] = curr
        x = nx
    
    return curr

def union(x, y, parent):
    X, Y = find(x, parent), find(y, parent)
    if X != Y:
        parent[Y] = X

for _ in range(int(input())):
    genre = defaultdict(list)
    artists = defaultdict(list)
    parents = {}
    A = []
    for i in range(int(input())):
        g, a = input().split()
        genre[g].append((g, a, i))
        artists[a].append((g, a, i))
        parents[(g, a, i)] = (g, a, i)
        A.append((g, a, i))

    for k in genre:
        rep = genre[k][0]
        for val in genre[k]:
            union(rep, val, parents)
    
    for k in artists:
        rep = artists[k][0]
        for val in artists[k]:
            union(rep, val, parents)
    
    set_counts = defaultdict(int)
    for x in A:
        set_counts[find(x, parents)] += 1
    
    print(len(A) - max(set_counts.values()))
