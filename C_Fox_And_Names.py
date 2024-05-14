from collections import defaultdict, deque

def solve():
    t = int(input())
    words = []
    for i in range(t):
        words.append(input())

    graph = defaultdict(list)
    indeg = defaultdict(int)
    valid = True
    for i in range(1, len(words)):
        p = words[i - 1]
        c = words[i]

        d_idx = 0
        while d_idx < len(p) and d_idx < len(c):
            if p[d_idx] != c[d_idx]: break
            d_idx += 1
        
        if d_idx == len(c) and d_idx < len(p):
            valid = False
            break
        
        if d_idx < len(p) and d_idx < len(c):
            graph[p[d_idx]].append(c[d_idx])
            indeg[c[d_idx]] += 1

    if not valid:
        print('Impossible')
        return

    queue = deque()
    order = []
    for key in graph:
        if key not in indeg:
            queue.append(key)
            order.append(key)

    while queue:
        for _ in range(len(queue)):
            c = queue.popleft()
            for nb in graph[c]:
                indeg[nb] -= 1
                if indeg[nb] == 0:
                    order.append(nb)
                    queue.append(nb)

    if len(order) != len(graph):
        print('Impossible')

    else:
        for un in range(97, 123):
            if chr(un) not in order:
                order.append(chr(un))
        
        print("".join(order))

solve()