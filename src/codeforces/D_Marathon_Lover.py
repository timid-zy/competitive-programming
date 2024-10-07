from collections import defaultdict

def get_edges(u: int, v: int):
    edges = set()
    while u.bit_length() > v.bit_length():
        edges.add((u // 2, u))
        u //= 2
    
    while v.bit_length() > u.bit_length():
        edges.add((v // 2, v))
        v //= 2
    
    while u != v:
        edges.add((v // 2, v))
        edges.add((u // 2, u))
        u //= 2
        v //= 2

    return edges

def handle_get(u, v, paths):
    path = get_edges(u, v)
    cost = 0
    for a, b in path:
        if a > b:
            a, b = b, a

        cost += paths[(a, b)]
    
    print(cost)

def handle_add(u, v, w, paths):
    ps = get_edges(u, v)
    for a, b in ps:
        if a > b:
            a, b = b, a
        
        paths[(a, b)] += w

def solve():
    path_cost = defaultdict(int)
    for _ in range(int(input())):
        op = list(map(int, input().split()))
        if op[0] == 1:
            handle_add(op[1], op[2], op[3], path_cost)
        else:
            handle_get(op[1], op[2], path_cost)

solve()