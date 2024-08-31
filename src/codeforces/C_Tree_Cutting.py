import functools

# edges except y
graph = {}
# @functools.cache
def getCount(x, y):
    global graph
    ans = len(graph[x])
    for key in graph[x]:
        if key != y:
            ans += getCount(key, x) - 1

    return ans

for i in range(int(input())):
    v, ops = list(map(int, input().split()))
    edges = {}

    for _ in range(v - 1):
        x, y = list(map(int, input().split()))
        if x not in graph:
            graph[x] = {y}
        
        if y not in graph:
            graph[y] = {x}
        
        graph[x].add(y)
        graph[y].add(x)
        edges[(x, y)] = (0, 0)

    for key in edges:
        x, y = key
        edges[key] = (getCount(x, y), getCount(y, x))
    
    print(edges)