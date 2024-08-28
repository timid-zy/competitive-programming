from collections import defaultdict, deque
import sys
input = sys.stdin.readline

class Node:
    def __init__(self, val=0):
        self.val = val
        self.children = []
        self.cost = 0

for _ in range(int(input())):
    N, K = map(int, input().split())
    cost = list(map(int, input().split()))
    INF_SUP = set(map(int, input().split()))
    for n in INF_SUP:
        cost[n-1] = 0
    
    nodes = defaultdict(Node)
    indeg = defaultdict(int)
    ans = [0] * N
    for i in range(N):
        NB = list(map(int, input().split()))
        if i not in nodes:
            nodes[i] = Node(i)
        if NB[0] == 0:
            ans[i] = cost[i]
            continue

        for j in range(1, len(NB)):
            nb = NB[j] - 1
            if nb not in nodes:
                nodes[nb] = Node(nb)
            
            nodes[nb].children.append(nodes[i])
            indeg[i] += 1
    
    queue = deque([])
    for i in range(N):
        if indeg[i] == 0:
            queue.append(nodes[i])
    
    while queue:
        for _ in range(len(queue)):
            c = queue.popleft()
            
            for nb in c.children:
                indeg[nb.val] -= 1
                nb.cost += ans[c.val]
                if indeg[nb.val] == 0:
                    ans[nb.val] = min(nb.cost, cost[nb.val])
                    queue.append(nodes[nb.val])

    print(*ans)
    