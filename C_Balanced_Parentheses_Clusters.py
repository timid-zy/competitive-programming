def find(x):
    curr = x
    while x != parent[x]:
        x = parent[x]
    
    while curr != parent[curr]:
        nxt = parent[curr]
        parent[curr] = x
        curr = nxt
    
    return curr

def union(x, y):
    r1, r2 = find(x), find(y)
    parent[r1] = r2

for _ in range(int(input())):
    N = int(input())
    s = input()
    parent = [i for i in range(2*N)]
    dct = {}

    lvl = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == ")":
            if lvl in dct and dct[lvl] != -1:
                union(dct[lvl], i)
            dct[lvl] = i
            lvl += 1
        
        else:
            lvl -= 1
            dct[lvl + 1] = -1 
            union(dct[lvl], i)

    visited = set()
    for i in parent:
        visited.add(find(i))
    
    print(len(set(visited)))
